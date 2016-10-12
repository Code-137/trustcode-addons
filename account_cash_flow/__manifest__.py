# -*- coding: utf-8 -*-
# © 2016 Danimar Ribeiro, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


{
    'name': 'Cash Flow Report - Base Account',
    'summary': """Create the base for the cash flow""",
    'version': '10.0.1.0.0',
    'category': 'Tools',
    'author': 'Trustcode',
    'license': 'AGPL-3',
    'website': 'http://www.trustcode.com.br',
    'contributors': [
        'Danimar Ribeiro <danimaribeiro@gmail.com>',
    ],
    'depends': [
        'account',
    ],
    'data': [
        'views/cash_flow_view.xml',
        'wizard/cash_flow.xml',
        'reports/account_cash_flow.xml',
    ],
}
