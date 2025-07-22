app_name = "practice"
app_title = "Practice"
app_publisher = "Ravin"
app_description = "only for practice"
app_email = "ravendra24@navgurukul.org"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "practice",
# 		"logo": "/assets/practice/logo.png",
# 		"title": "Practice",
# 		"route": "/practice",
# 		"has_permission": "practice.api.permission.has_app_permission"
# 	}
# ]




doctype_js = {
    "Sales Invoice": "public/js/custom_btn_sales_invoice.js"
}





# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "practice.public.css.Custom_Desk"
# app_include_js = "practice.public.js.Custom_Desk.frappe.ready"

# app_include_js = "/assets/practice/js/Custom_Desk.js"
# app_include_css = "/assets/practice/css/Custom_Desk.css"


# include js, css files in header of web template
# web_include_css = "/assets/practice/css/practice.css"
# web_include_js = "/assets/practice/js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "practice/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "practice/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "practice.utils.jinja_methods",
# 	"filters": "practice.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "practice.install.before_install"
# after_install = "practice.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "practice.uninstall.before_uninstall"
# after_uninstall = "practice.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "practice.utils.before_app_install"
# after_app_install = "practice.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "practice.utils.before_app_uninstall"
# after_app_uninstall = "practice.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "practice.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Students": {
        "before_save": "practice.notify_on_save.notify_on_save"
    }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"practice.tasks.all"
# 	],
# 	"daily": [
# 		"practice.tasks.daily"
# 	],
# 	"hourly": [
# 		"practice.tasks.hourly"
# 	],
# 	"weekly": [
# 		"practice.tasks.weekly"
# 	],
# 	"monthly": [
# 		"practice.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "practice.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "practice.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "practice.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["practice.utils.before_request"]
# after_request = ["practice.utils.after_request"]

# Job Events
# ----------
# before_job = ["practice.utils.before_job"]
# after_job = ["practice.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"practice.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

