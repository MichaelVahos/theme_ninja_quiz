from odoo import http
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
