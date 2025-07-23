// Copyright (c) 2025, Ravin and contributors
// For license information, please see license.txt


// frappe.ui.form.on('To-Do Task', {
//     refresh: function(frm) {
//         console.log("Status is:", frm.doc.status); // debug line
//         if (frm.doc.status === 'Completed') {
//             frm.set_df_property('tittle', 'read_only', 1);
//         }
//     }
// });


frappe.ui.form.on('To-Do Task', {
    refresh: function(frm) {
        frm.add_custom_button("Mark Completed", () => {
            frappe.call({
                method:'practice.practice.doctype.to_do_task.to_do_task.mark_completed',
                args: { docname: frm.doc.name },
                 callback: function(r) {
                    frappe.msgprint(r.message);
                    frm.reload_doc();
                }  
            })
        })
    }
})