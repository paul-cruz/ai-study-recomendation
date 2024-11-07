import os
import vertexai
from flask_cors import CORS
from flask import Flask, request, jsonify
from vertexai.generative_models import GenerativeModel, SafetySetting

app = Flask(__name__)
CORS(app)

@app.route('/get_study_recomendation', methods=['GET'])
def get_study_recomendation():
    study_topic = request.args.get('topic')
    if not study_topic:
        return jsonify({'Error': 'Sin tema para recomendar'}), 400
    return jsonify(generate_ai_study_recomendation(study_topic)), 200


def generate_ai_study_recomendation(topic: str) -> str:
    vertexai.init(
        project=os.environ.get('GCP_PROJECT_ID'), 
        location=os.environ.get('GCP_VERTEX_AI_LOCATION'))
    
    model = GenerativeModel(
        "gemini-1.5-flash-002",
    )
    responses = model.generate_content(
        [f"""Sugiere una lista de temas para aprender: {topic}"""],
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=True,
    )

    response = ''
    for r in responses:
        response += r.text
    return response


generation_config = {
    "max_output_tokens": 8192,
    "temperature": 1,
    "top_p": 0.95,
}

safety_settings = [
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
]


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))