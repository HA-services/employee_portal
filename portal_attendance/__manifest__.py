

{
    "name": "Portal Attendance | Employee Attendance Portal ",
    "summary": """This module enables portal users to both view and mark their attendance in Odoo""",
    "version": "16.0.1",
    "description": """
        This module enables portal users to view and mark their attendance in Odoo. It also includes features for sorting and searching attendance records by date.
    """,    
    "author": "Axsync",
    "maintainer": "Axsync",
    "license" :  "Other proprietary",
    "website": "https://www.axsync.com",
    "images": ["static/description/icon1.png"],
    "category": "Attendances",
    "depends": [
        "base",
        "hr",
        "hr_attendance",
        "website",
    ],
    "data": [
        "security/ir.model.access.csv",

        "views/res_config_settings.xml",
        "views/hr_employee_views.xml",
        "views/hr_attendance_templates.xml",
        "views/hr_attendance_reasons_view.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "/portal_attendance/static/src/css/portal.css",
            "/portal_attendance/static/src/lib/sweetalert2/sweetalert2.css",
            "/portal_attendance/static/src/lib/sweetalert2/sweetalert2.js",
            "/portal_attendance/static/src/js/portal_attendance.js",
        ],
        "web.assets_backend": [
            "/portal_attendance/static/src/lib/sweetalert2/sweetalert2.css",
            "/portal_attendance/static/src/lib/sweetalert2/sweetalert2.js",

            "/portal_attendance/static/src/css/drawing.css",
            "/portal_attendance/static/src/css/attendance.css",

         
            "/portal_attendance/static/src/js/my_attendances.js",
            
            "/portal_attendance/static/src/xml/*.xml",
        ],
        "web.assets_qweb": [
            "/portal_attendance/static/src/xml/*.xml"
        ],
    },
    "installable": True,
    "application": True,
    "price"                 :  40,
    "currency"              :  "USD",
    "pre_init_hook"         :  "pre_init_check",
}
