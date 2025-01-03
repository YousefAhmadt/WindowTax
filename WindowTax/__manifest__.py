{
    'name': 'Windw Tax',
    'description': """A module for managing tickets and users.""",
    'depends': ['base', 'web'],  # Add relevant dependencies
    'category': 'Extra Tools',
    'auto_install': False,
    'data': [
        'security/ir.model.access.csv',
        'report/templates.xml',
        'views/res_users_views.xml',  # Uncomment if needed# Uncomment if needed

    ],
    'assets': {
        'web.assets_tests': [
            # 'auth_totp/static/tests/**/*',  # Uncomment when ready
        ],
        'web.assets_backend': [
            # 'auth_totp/static/src/**/*',    # Uncomment when ready
        ],
    },
    'license': 'LGPL-3',
}
