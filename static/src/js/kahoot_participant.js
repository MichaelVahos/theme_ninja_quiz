// File: theme_ninja_quiz/static/src/js/kahoot_participant.js

/** OWL Component to play survey like Kahoot */
import { Component, onWillStart, useState } from '@odoo/owl';
import { xml } from '@odoo/owl';
import { useRef } from '@odoo/owl';
import { rpc } from 'web.core';

export class KahootParticipant extends Component {
    setup() {
        this.state = useState({
            question: null,
            answers: [],
            loading: true,
            error: null,
        });

        this.container = useRef('kahootContainer');

        onWillStart(async () => {
            try {
                const surveyId = parseInt(this.props.surveyId);
                const inputId = parseInt(this.props.inputId);
                const result = await rpc.query({
                    model: 'survey.user_input',
                    method: 'get_current_question_and_answers',
                    args: [surveyId, inputId],
                });
                this.state.question = result.question;
                this.state.answers = result.answers;
            } catch (e) {
                this.state.error = 'Error cargando la pregunta';
            } finally {
                this.state.loading = false;
            }
        });
    }

    async submitAnswer(answerId) {
        try {
            await rpc.query({
                model: 'survey.user_input',
                method: 'submit_answer',
                args: [this.props.inputId, this.state.question.id, answerId],
            });
            window.location.reload();
        } catch (e) {
            alert('No se pudo enviar la respuesta');
        }
    }

    static template = xml`
        <div t-ref="kahootContainer" class="kahoot-wrapper">
            <t t-if="state.loading">
                <p>Cargando pregunta...</p>
            </t>
            <t t-elif="state.error">
                <p t-esc="state.error" class="text-danger" />
            </t>
            <t t-else>
                <h2 t-esc="state.question.title" class="mb-3" />
                <ul>
                    <t t-foreach="state.answers" t-as="ans">
                        <li>
                            <button t-on-click="() => this.submitAnswer(ans.id)">
                                <t t-esc="ans.value" />
                            </button>
                        </li>
                    </t>
                </ul>
            </t>
        </div>`;
}

KahootParticipant.props = ['surveyId', 'inputId'];

