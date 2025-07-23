# Copyright (c) 2025, Ravin and contributors
# For license information, please see license.txt


import frappe
from frappe.model.document import Document
from frappe.utils import today, getdate


class ToDoTask(Document):
    def validate(self):
        if getdate(self.due_date) >= getdate(today()):
            pass
        else:
            frappe.throw("Due date should be today or a future date.")

@frappe.whitelist()
def mark_completed(docname):
    doc = frappe.get_doc("To-Do Task", docname)
    doc.status = "Completed"
    doc.save()
    return "Marked as Completed"

