frappe.ui.form.on("Item Price", {
    setup: function(frm) {
        frm.set_df_property('price_list_rate', 'label', 'Actual Sell');

//        frm.set_value("user_a_0010", frappe.session.user);
//        frm.set_df_property('brand', 'in_list_view', 0);

    },

    refresh: function(frm) {
        frm.set_df_property('price_list_rate', 'label', 'Actual Sell');
    },

    onload: function(frm) {
          frm.set_df_property('price_list_rate', 'label', 'Actual Sell');
    },

});

