from odoo import http
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)

class KahootGameController(http.Controller):

    @http.route('/kahoot', type='http', auth='public', website=True)
    def kahoot_page(self, **kw):
        _logger.info("Entrando en /kahoot correctamente")
        return request.render('theme_ninja_quiz.kahoot_page', {})

    @http.route('/kahoot/join', type='http', auth='public', methods=['POST'], website=True, csrf=False)
    def kahoot_join(self, **post):
        pin = post.get('pin')
        try:
            pin = int(pin)
        except (ValueError, TypeError):
            _logger.warning(f'PIN inválido recibido: {pin}')
            return request.render('theme_ninja_quiz.kahoot_page', {
                'error': 'El PIN debe ser un número.'
            })

        game = request.env['survey.game.session'].sudo().search([('id', '=', pin)], limit=1)
        _logger.info(f"PIN recibido: {pin} | Resultado búsqueda: {game}")

        if game:
            return request.redirect(f'/kahoot/play/{game.id}')
        else:
            return request.render('theme_ninja_quiz.kahoot_page', {
                'error': 'PIN no válido. Intenta de nuevo.'
            })

    @http.route('/kahoot/play/<int:game_id>', type='http', auth='public', website=True)
    def kahoot_play(self, game_id):
        game = request.env['survey.game.session'].sudo().browse(game_id)
        if not game.exists():
            return request.not_found()
        return request.render('theme_ninja_quiz.kahoot_play_page', {
            'game': game,
        })

    @http.route('/kahoot/waiting/<int:game_id>', type='http', auth='public', website=True)
    def kahoot_waiting(self, game_id):
        game = request.env['survey.game.session'].sudo().browse(game_id)
        if not game.exists():
            return request.not_found()
        return request.render('theme_ninja_quiz.kahoot_waiting_page', {
            'game': game,
        })

    @http.route('/kahoot/submit_answer', type='json', auth='public', csrf=False)
    def submit_answer(self, participant_id, question_id, answer_id):
        participant = request.env['survey.game.participant'].sudo().browse(participant_id)
        if not participant.exists():
            return {'status': 'error', 'message': 'Participante no válido.'}

        request.env['survey.game.participant.answer'].sudo().create({
            'participant_id': participant_id,
            'question_id': question_id,
            'answer_id': answer_id
        })

        return {
            'status': 'ok',
            'redirect': f'/kahoot/waiting/{participant.session_id.id}'
        }
