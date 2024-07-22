import pandas as pd
import re
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from joblib import load
from sqlalchemy import create_engine
import unidecode

# Configuración de la base de datos
db_uri = 'postgresql+psycopg://postgres:xpango2011@ciyadbaws.cakcdqyqgv2b.us-east-1.rds.amazonaws.com/ciyadatabase'
engine = create_engine(db_uri)

# Cargar modelos
model_nb = load('best_model_naive_bayes.pkl')
model_lr = load('best_model_logistic_regression.pkl')

# Cargar archivos JSON con carreras y software
with open('carreras_posibles.json', 'r') as f:
    carreras_posibles = json.load(f)
    print(f"Carreras posibles cargadas: {carreras_posibles}")  # Debugging line

with open('software_posibles.json', 'r') as f:
    software_posibles = json.load(f)

def normalize_text(text):
    # Convierte a minúsculas y elimina tildes
    text = text.lower()
    text = unidecode.unidecode(text)
    return text

def find_carrera(keyword, carreras_posibles):
    keyword_normalized = normalize_text(keyword)
    print(f"Keyword normalizado: {keyword_normalized}")  # Debugging line
    for carrera in carreras_posibles:
        carrera_normalized = normalize_text(carrera)
        print(f"Carrera normalizada: {carrera_normalized}")  # Debugging line
        if carrera_normalized in keyword_normalized:
            return carrera
    return "No se encontró una carrera adecuada."

@api_view(['POST'])
def predictLabView(request):
    if model_nb is None or model_lr is None:
        return Response({'error': 'Models not found'}, status=500)

    keyword = request.data.get('keyword', '')
    if not keyword:
        return Response({'error': 'No keyword provided'}, status=400)

    keyword_normalized = normalize_text(keyword)

    num_students_match = re.search(r'\b(\d+|diez)\b', keyword_normalized)
    if num_students_match:
        num_students_str = num_students_match.group(1).lower()
        num_students = 10 if num_students_str == 'diez' else int(num_students_str)
    else:
        num_students = None

    carrera = find_carrera(keyword, carreras_posibles)
    print(f"Carrera encontrada: {carrera}")  # Debugging line

    software = None
    for sw in software_posibles:
        if normalize_text(sw) in keyword_normalized:
            software = sw
            break

    try:
        # Predicciones con Naive Bayes
        probs_nb = model_nb.predict_proba([keyword])[0]
        lab_ids_nb = model_nb.classes_
        prob_dict_nb = dict(zip(lab_ids_nb, probs_nb))
        sorted_prob_dict_nb = dict(sorted(prob_dict_nb.items(), key=lambda item: item[1], reverse=True))

        # Predicciones con Logistic Regression
        probs_lr = model_lr.predict_proba([keyword])[0]
        lab_ids_lr = model_lr.classes_
        prob_dict_lr = dict(zip(lab_ids_lr, probs_lr))
        sorted_prob_dict_lr = dict(sorted(prob_dict_lr.items(), key=lambda item: item[1], reverse=True))

        # Selección del mejor modelo
        best_model = 'Naive Bayes'
        if max(probs_lr) > max(probs_nb):
            best_model = 'Logistic Regression'
            sorted_prob_dict = sorted_prob_dict_lr
        else:
            sorted_prob_dict = sorted_prob_dict_nb

        result = [
            {
                'idLab': int(lab_id),
                'prediction': f"{prob * 100:.2f}",
                'carrera': carrera
            } for lab_id, prob in sorted_prob_dict.items() if prob > 0.1
        ]

        if not result:
            result = [{"message": "No se encontraron resultados con probabilidad mayor al 10%."}]

        response = {
            "predictions": result,
            "bestModel": best_model,
            "software": software
        }

        return Response(response)
    except Exception as e:
        return Response({'error': str(e)}, status=500)
