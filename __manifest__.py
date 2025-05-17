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
            'theme_ninja_quiz/static/src/js/kahoot.js',from odoo import http
from odoo.http import request

class KahootGameController(http.Controller):

    @http.route('/kahoot', type='http', auth='public', website=True)
    def kahoot_participant(self, **kwargs):
        # Generar un user_input si no existe
        survey = request.env['survey.survey'].sudo().search([], limit=1)
        user_input = request.env['survey.user_input'].sudo().create({
            'survey_id': survey.id,
            'partner_id': request.env.user.partner_id.id,
            'state': 'new',
        })
        return request.render('theme_ninja_quiz.kahoot_page', {
            'survey_id': survey.id,
            'input_id': user_input.id,
        })

            'theme_ninja_quiz/static/src/js/kahoot_participant.js',
        ]
    },
    "installable": True,
    "application": False,
    "auto_install": False
}
