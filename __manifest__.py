{
    "name": "Theme Ninja Quiz",
    "description": "Un tema parecido a Kahoot",
    "category": "Theme/Creative",
    "version": "1.0",
    "author": "Michael Vahos",
    "license": "LGPL-3",
    "depends": ["web", "website", "survey"],
    "data": [
        "views/kahoot_page.xml",
        "views/kahoot_play.xml",
        "views/kahoot_waiting_page.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "theme_ninja_quiz/static/src/css/kahoot_theme.css",
            "theme_ninja_quiz/static/src/css/theme.css",
            'theme_ninja_quiz/static/src/js/kahoot.js'
                ],
}