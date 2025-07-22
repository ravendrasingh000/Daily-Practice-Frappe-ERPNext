// Copyright (c) 2025, Ravin and contributors
// For license information, please see license.txt

frappe.ui.form.on("About Fields", {
	refresh(frm) {

	},
    get_age(frm){
        frm.get_field('age').$wrapper.append("<h1>AGE: 24</h1>")
        frm.get_field('get_age')?.$wrapper?.hide();
    }
});
