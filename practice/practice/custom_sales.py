import frappe
@frappe.whitelist()
def test(doc):
    print("----____________________________",doc)
    return doc