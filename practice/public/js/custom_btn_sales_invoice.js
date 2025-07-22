frappe.ui.form.on('Sales Invoice', {
    refresh: function(frm) {
        frm.add_custom_button(__('My Custom Button'), function() {
            frappe.call({
                method: "practice.practice.custom_sales.test",
                args:{
                    doc: frm.doc
                },
                callback: function(r) {
                    frappe.msgprint("Yeh custom button click hua hai!",r.massage);
                }
            });
        });
    }
});
