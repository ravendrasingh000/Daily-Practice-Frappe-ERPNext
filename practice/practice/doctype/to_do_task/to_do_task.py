# Copyright (c) 2025, Ravin and contributors
# For license information, please see license.txt


import frappe
from frappe.model.document import Document
from frappe.utils import today, getdate

# Due date field field ko validate kiya gya hai ki due date aaj ki ya aage ki hone chahiye
class ToDoTask(Document):
    def validate(self):
        if getdate(self.due_date) >= getdate(today()):
            pass
        else:
            frappe.throw("Due date should be today or a future date.")


#isko JS se call kiya ja rha hai jo ki form me mark as completed par click karne par call ho raha hai  button JS se create kiya gaya hai
# @frappe.whitelist()
# def mark_completed(docname):
#     doc = frappe.get_doc("To-Do Task", docname)
#     doc.status = "Completed"
#     doc.save()
#     return "Marked as Completed"


# Frappe REST API Create(Python function ko API ki tarah call karna)
@frappe.whitelist(allow_guest=True)
def get_tasks():
    tasks = frappe.get_all("To-Do Task", fields=["name", "tittle", "status"])
    return tasks