{
    'name': 'Sistema de Administración de Usuarios',
    'version': '19.0.1.0.0',
    'category': 'Administration',
    'summary': 'Sistema completo para gestionar usuarios y contraseñas',
    'description': """
Sistema de Administración de Usuarios
======================================
Un sistema completo y moderno para gestionar usuarios del sistema.

Características principales:
---------------------------
- Diseño moderno con gradientes y animaciones
- Creación rápida de usuarios con validación
- Edición y eliminación de usuarios
- Restablecimiento de contraseñas
- Búsqueda y filtrado en tiempo real
- Paginación de resultados
- Estadísticas en tiempo real
- Tarjetas de usuario con avatar automático
- Notificaciones toast
- Soporte para grupos y permisos
- Interfaz responsive
    """,
    'author': 'Custom',
    'website': 'https://www.odoo.com',
    'license': 'LGPL-3',
    'depends': ['base', 'mail', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'security/user_admin_security.xml',
        'views/user_admin_views.xml',
        'views/res_users_views.xml',
        'data/user_admin_data.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'user_admin_panel/static/src/css/user_admin.css',
            'user_admin_panel/static/src/js/user_admin.js',
            'user_admin_panel/static/src/xml/user_admin_templates.xml',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}
