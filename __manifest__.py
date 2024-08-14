{
'name': "Exportaciones",
'version': '1.0',
'depends': ['base','dtm_ordenes_compra'],
'author': "Rafael Guzmán",
'category': 'DTM',
'description': "Modulo para llevar el control de las exportaciones",
# data files always loaded at installation
'data': [
    'security/ir.model.access.csv',
    'views/dtm_exportaciones_view.xml',
],
    'license': 'LGPL-3',
}
