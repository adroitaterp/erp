from odoo import api, fields, models, tools, _,Command
import logging
from markupsafe import Markup
from odoo.tools import config, date_utils, get_lang
from bs4 import BeautifulSoup
import markupsafe
import datetime


_logger = logging.getLogger(__name__)

class AccountReport(models.AbstractModel):
    _inherit = 'account.partner.ledger'

    @api.model
    def _get_report_name(self):
        return _('Statement of Account')
    

#     def get_html(self, options, line_id=None, additional_context=None):
#         '''
#         return the html value of report, or html value of unfolded line
#         * if line_id is set, the template used will be the line_template
#         otherwise it uses the main_template. Reason is for efficiency, when unfolding a line in the report
#         we don't want to reload all lines, just get the one we unfolded.
#         '''
        
#         _logger.warning("AAAAAAAAAAAAA _____________ JJJJJJJJJJJJJJJJ _________________ KKKKKKKKKKKKK s% ",options)
#         # Prevent inconsistency between options and context.
#         self = self.with_context(self._set_context(options))

#         templates = self._get_templates()
#         report_manager = self._get_report_manager(options)

#         render_values = self._get_html_render_values(options, report_manager)
#         if additional_context:
#             render_values.update(additional_context)

#         # Create lines/headers.
#         if line_id:
#             headers = options['headers']
#             lines = self._get_lines(options, line_id=line_id)
#             template = templates['line_template']
#         else:
#             headers, lines = self._get_table(options)
#             options['headers'] = headers
#             template = templates['main_template']
#         if options.get('hierarchy'):
#             lines = self._create_hierarchy(lines, options)
#         if options.get('selected_column'):
#             lines = self._sort_lines(lines, options)

#         lines = self._format_lines_for_display(lines, options)

#         render_values['lines'] = {'columns_header': headers, 'lines': lines}

#         # Manage footnotes.
#         footnotes_to_render = []
#         if self.env.context.get('print_mode', False):
#             # we are in print mode, so compute footnote number and include them in lines values, otherwise, let the js compute the number correctly as
#             # we don't know all the visible lines.
#             footnotes = dict([(str(f.line), f) for f in report_manager.footnotes_ids])
#             number = 0
#             for line in lines:
#                 f = footnotes.get(str(line.get('id')))
#                 if f:
#                     number += 1
#                     line['footnote'] = str(number)
#                     footnotes_to_render.append({'id': f.id, 'number': number, 'text': f.text})

#         # Render.
#         html = self.env.ref(template)._render(render_values)
#         if self.env.context.get('print_mode', False):
#             for k,v in self._replace_class().items():
#                 html = html.replace(k, v)
#             # append footnote as well
#             html = html.replace(markupsafe.Markup('<div class="js_account_report_footnotes"></div>'), self.get_html_footnotes(footnotes_to_render))
#         return html


    def get_pdf(self, options):
        _logger.warning("QQQQQQQQQQQQQQQQQQQQQQ _____________ EEEEEEEEEEEEE _________________ ZZZZZZZZZZZZZZZZZ s% ",options)
        # res=super(AccountReport,self).get_pdf(options)
        _logger.warning("JJJJJJJJJJJJJJJJJJJJ _____________ FFFFFF FFFFFFF _________________ SSSSSSSSSSS  : s% ",options)
        # return res
        # As the assets are generated during the same transaction as the rendering of the
        # templates calling them, there is a scenario where the assets are unreachable: when
        # you make a request to read the assets while the transaction creating them is not done.
        # Indeed, when you make an asset request, the controller has to read the `ir.attachment`
        # table.
        # This scenario happens when you want to print a PDF report for the first time, as the
        # assets are not in cache and must be generated. To workaround this issue, we manually
        # commit the writes in the `ir.attachment` table. It is done thanks to a key in the context.
        if not config['test_enable']:
            self = self.with_context(commit_assetsbundle=True)
        # options.pop('account_type', None)
        base_url = self.env['ir.config_parameter'].sudo().get_param('report.url') or self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        rcontext = {
            'mode': 'print',
            'base_url': base_url,
            'company': self.env.company,
        }

        body_html = self.with_context(print_mode=True).get_html(options)
        body = self.env['ir.ui.view']._render_template(
            "account_reports.print_template",
            values=dict(rcontext, body_html=body_html),
        )
        footer = self.env['ir.actions.report']._render_template("web.internal_layout", values=rcontext)
        footer = self.env['ir.actions.report']._render_template("web.minimal_layout", values=dict(rcontext, subst=True, body=Markup(footer.decode())))

        landscape = False
        if len(self.with_context(print_mode=True).get_header(options)[-1]) > 5:
            landscape = True

        html_content = body

        # Parse the HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find and remove the specified elements
        elements_to_remove = [
            "th.o_account_report_column_header:contains('Account')",
            "th.o_account_report_column_header:contains('Matching Number')",
            "th.o_account_report_column_header.number:contains('Initial Balance')",
            "th.o_account_report_column_header:contains('Due Date')"
        ]

        for element_selector in elements_to_remove:
            elements = soup.select(element_selector)
            for element in elements:
                element.extract()
        body = Markup(str(soup))
       
        soup = BeautifulSoup(body, 'html.parser')

        # Find all rows except the first and last
        rows = soup.find_all('tr')[2:-1]

        first_row=soup.find_all('tr')[1]
        all_th=soup.find('tr').find_all('th')
        

        ref_index = None
        for i, th in enumerate(all_th):
            if th.get_text(strip=True) == 'Ref':
                ref_index = i
                break

        # Create a new 'th' element with the value 'Product'
        new_th = soup.new_tag('th', **{'class': 'o_account_report_column_header'})
        new_th.string = 'Products'

        # Insert the new 'th' element after the 'Ref' 'th' element
        if ref_index is not None:
            all_th[ref_index].insert_after(new_th)
       
        first_td = first_row.find('td')

        if first_td.has_attr('colspan'):
            first_td['colspan']=4

        all_td=first_row.find_all('td')

        for index in [1]:

            all_td[index].decompose()


        last_row=soup.find_all('tr')[-1]
       
        last_td = last_row.find('td')

        if last_td.has_attr('colspan'):
            last_td['colspan']=4

        all_td=last_row.find_all('td')

        for index in [1]:

            all_td[index].decompose()


        col_4_div = soup.find('div', class_='col-4')
        if col_4_div:
            # Get the text before the <br> tag
            text_before_br = col_4_div.find(text=True, recursive=False)
            # Replace the text with today's date
            date=datetime.datetime.now().strftime("%d-%m-%y")
            date="As of Date "+date
            text_before_br.replace_with(date)

        # Loop through each row
        for row in rows:
            # Find all td elements
            tds = row.find_all('td')
            for index in [2,4,5,6]:
                tds[index].decompose()

            print("TTTTTTTTTTT : ",tds[3])
            print("TTTTTTTTTTT : ",type(tds[3]))
            bb=Markup(str(tds[3]))
            new_s = BeautifulSoup(bb, 'html.parser')

            # Find the span tag within the td element
            span_tag = new_s.find('td').find('span')
            span_add = new_s.find('td')

            new_td = new_s.new_tag('td')
            # Get the text inside the span tag
            value = span_tag.text.strip()
            all=self.env['account.move'].search([('name','=',value),('move_type','in',['in_invoice','out_invoice'])])
            for rec in all.invoice_line_ids:
                sp=new_s.new_tag('p')
                print("PPPPPPPPPPRRRRRRRRRRRRRRRRR : ",rec.product_id.name)
                sp.string=rec.name
                new_td.append(sp)
            tds[3].insert_after(new_td)


        # Get the modified HTML
        body = soup.prettify()

        return self.env['ir.actions.report']._run_wkhtmltopdf(
            [body],
            footer=footer.decode(),
            landscape=landscape,
            specific_paperformat_args={
                'data-report-margin-top': 10,
                'data-report-header-spacing': 10
            }
        )