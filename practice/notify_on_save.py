import frappe

def notify_on_save(doc, method):

    print("This___________________________________________________________________")

    frappe.msgprint(f"Invoice {doc.name} has been submitted by {frappe.session.user}")

    message= f"""
Hello Dear {doc.full_name},
You are new Student in my School
"""
    if doc.email:   
        frappe.sendmail(
                recipients=[doc.email],
                subject= "Student Record Saved",
                message=message
        )
    print(doc.__dict__)