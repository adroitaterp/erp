odoo.define('inherit_product.wedgit', function (require) {
    'use strict';

    var FieldDate = require('web.basic_fields').FieldDate;

    FieldDate.include({
        _render: function () {
            var value = this.value;
            if (!value) {
                this.$el.text("Date is empty");
            } else {
                this._super.apply(this, arguments);
            }
        },
    });
});