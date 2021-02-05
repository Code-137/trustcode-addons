{  # pylint: disable=C8101,C8103
    'name': 'Integração Boleto Cloud',
    'version': '13.0.1.0.0',
    'category': 'account',
    'author': 'Trustcode',
    'website': 'http://www.trustcode.com.br',
    'contributors': [
        'Danimar Ribeiro <danimaribeiro@gmail.com>',
    ],
    'depends': [
        'l10n_br_account',
        'l10n_br_automated_payment',
    ],
    'data': [
        'views/account_journal.xml',
        'views/res_company.xml',
    ],
}