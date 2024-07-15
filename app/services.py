# app/services.py
import requests
from models import session, Quiz, Tutorial, Lab

OPENAI_API_KEY = 'PLACE HOLDER'

def generate_quiz_question():
    response = requests.post(
        'https://api.openai.com/v1/engines/davinci-codex/completions',
        headers={'Authorization': f'Bearer {OPENAI_API_KEY}'},
        json={
            'prompt': 'Generate a cybersecurity quiz question',
            'max_tokens': 150
        }
    )
    data = response.json()
    return data['choices'][0]['text'].strip()

def save_quiz_question(question, options, correct_option, explanation):
    quiz = Quiz(question=question, options=options, correct_option=correct_option, explanation=explanation)
    session.add(quiz)
    session.commit()

def get_tutorials():
    return session.query(Tutorial).all()

def get_labs():
    return session.query(Lab).all()
