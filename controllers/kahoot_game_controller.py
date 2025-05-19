from odoo import http
from odoo.http import request

class KahootGameController(http.Controller):

    @http.route('/kahoot/<int:survey_id>', type='http', auth='public', website=True)
    def kahoot_participant(self, survey_id, **kwargs):
        # Buscar la encuesta por ID
        survey = request.env['survey.survey'].sudo().browse(survey_id)
        if not survey.exists():
            return request.not_found()

        # Crear user_input para el participante
        user_input = request.env['survey.user_input'].sudo().create({
            'survey_id': survey.id,
            'partner_id': request.env.user.partner_id.id,
            'state': 'new',
        })

        return request.render('theme_ninja_quiz.kahoot_page', {
            'survey_id': survey.id,
            'input_id': user_input.id,
        })
