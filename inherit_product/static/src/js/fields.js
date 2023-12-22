odoo.define('inherit_product.Fields', function (require) {
"use strict";

var relational_fields = require('web.relational_fields');
var FieldMany2One = relational_fields.FieldMany2One;

FieldMany2One.include({
_search: async function (searchValue = "") {
const value = searchValue.trim();
const domain = this.record.getDomain(this.recordParams);
const context = Object.assign(
this.record.getContext(this.recordParams),
this.additionalContext
);
var values = await this._super.apply(this, arguments);

if (this.attrs.name == 'sale_order'){
    this.limit=2
}
    
// Add "Search more..." option even if results count is lower than the limit of 7
// if (this.limit >= values.length) {
// values = this._manageSearchMore(values, value, domain, context);
// }
// values = this._manageSearchMore(values, value, domain, context);


return values;
},
})
});