{
    'name' : 'Custom security stuff',
    'version' : '1.0.0',
    'author' : 'Ivan Yelizariev',
    'category' : 'Base',
    'website' : 'https://it-projects.info',
    'description': """
    Tested on 8.0 ab7b5d7.

    """,
    'depends' : ['access_base', 'res_users_clear_access_rights', 'base', 'account', 'sale', 'crm', 'hr_payroll', 'project', 'purchase', 'hr_recruitment', 'hr_holidays', 'hr_evaluation', 'board', 'marketing'],
    'data':[
        'views.xml',
        'security.xml',
        'ir.model.access.csv',
        ],
    'demo':[
        'demo.xml'
    ],
    'installable': True
}
