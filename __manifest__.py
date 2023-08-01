##############################################################################
#
#   OpenERP, Open Source Management Solution
##############################################################################

{
    'name': 'fistrepair',
    'version': '16.0.2.0.2',
    'author': 'Pablo holguin',
    'maintainer': 'Pablo holguin',
    'website': 'http://www.ithesk.com',
    'license': 'AGPL-3',
    'category': 'Extra Tools',
    'summary': 'Short summary.',
    'depends': ['base','repair'],
    'data': [
      'views/repair_views.xml',
      'report/repair_reports1.xml',
      'report/repair_reports2.xml',
      'report/repair_reports.xml',      
      'report/repair_templates_repair_order1.xml',
      'report/repair_templates_repair_order2.xml',
      'report/repair_templates_repair_order.xml',     
    ],
    'images': ['static/description/banner.png'],
}
