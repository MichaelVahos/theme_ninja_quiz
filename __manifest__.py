{
    'name': 'Theme Ninja Quiz',
    'version': '1.0',
    'author': 'Michael Vahos',
    'category': 'Theme',
    'license': 'LGPL-3',
    'depends': ['website', 'web', 'ninja_quiz'],
    'data': [
        'views/kahoot_page.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            'ninja_quiz/static/src/components/KahootPlayer/KahootPlayer.js'
        ]
    },
    'installable': True,
    'auto_install': False
}
