import pandas as pd
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
import joblib
import json

# Crear una conexión a la base de datos PostgreSQL usando SQLAlchemy
db_uri = 'postgresql+psycopg://postgres:xpango2011@ciyadbaws.cakcdqyqgv2b.us-east-1.rds.amazonaws.com/ciyadatabase'
engine = create_engine(db_uri)

# Consulta para extraer los datos
query = """
SELECT
id_res,
fk_id_doc,
fk_id_lab,
tema_res,
comentario_res,
fecha_hora_res,
numero_participantes_res,
materiales_res,
fecha_creacion_res,
fecha_actualizacion_res,
fecha_hora_fin_res,
observaciones_finales_res,
asistencia_res,
curso_res,
materia_res,
fk_id_car,
paralelo_res,
tipo_texto_res,
fk_id_usu,
software_res,
public.carrera.nombre_car
FROM
    laboratorios.reserva
INNER JOIN public.carrera ON public.carrera.id_car = laboratorios.reserva.fk_id_car
WHERE
  laboratorios.reserva.software_res IS NOT NULL
AND
  laboratorios.reserva.software_res != ''
AND
  laboratorios.reserva.asistencia_res IS NOT NULL
AND
  laboratorios.reserva.materia_res IS NOT NULL
AND
  laboratorios.reserva.materia_res != ''
AND
  laboratorios.reserva.materia_res !~ '^[0-9]+$'
AND
  laboratorios.reserva.fk_id_doc IS NOT NULL
AND
  laboratorios.reserva.fk_id_lab IS NOT NULL
AND
  laboratorios.reserva.numero_participantes_res IS NOT NULL
AND
  laboratorios.reserva.fk_id_car IS NOT NULL
"""

# Leer los datos en un DataFrame de pandas usando SQLAlchemy
df = pd.read_sql(query, engine)

# Calcular el promedio de numero_participantes_res y redondearlo a un número entero
avg_num_participantes = int(round(df['numero_participantes_res'].mean()))

# Guardar las carreras, software y materias posibles en archivos JSON
carreras_posibles = df['nombre_car'].unique().tolist()
software_posibles = df['software_res'].unique().tolist()
materias_posibles = df['materia_res'].unique().tolist()

# Limpiar y eliminar duplicados (incluyendo espacios)
carreras_posibles = list(set(car.strip() for car in carreras_posibles))
software_posibles = list(set(soft.strip() for soft in software_posibles))
materias_posibles = list(set(mat.strip() for mat in materias_posibles))

# Guardar los archivos JSON
with open('carreras_posibles.json', 'w', encoding='utf-8') as f:
    json.dump(carreras_posibles, f, ensure_ascii=False, indent=4)
with open('software_posibles.json', 'w', encoding='utf-8') as f:
    json.dump(software_posibles, f, ensure_ascii=False, indent=4)
with open('materias_posibles.json', 'w', encoding='utf-8') as f:
    json.dump(materias_posibles, f, ensure_ascii=False, indent=4)

# Seleccionar las columnas relevantes para la búsqueda
text_columns = ["tema_res", "comentario_res", "materiales_res", "observaciones_finales_res", "materia_res", "software_res", "fk_id_car"]

# Convertir todas las columnas seleccionadas a cadenas y concatenarlas en una nueva columna 'text'
df['text'] = df[text_columns].astype(str).fillna('').apply(lambda x: ' '.join(x), axis=1)

# Seleccionar las columnas de interés
df = df[["fk_id_lab", "text"]]

# Eliminar filas con valores faltantes
df.dropna(inplace=True)

# Eliminar las clases con menos de 2 instancias
df = df[df.groupby('fk_id_lab')['fk_id_lab'].transform('count') > 1]

# Crear variables de entrada y salida
X = df["text"]
y_lab = df["fk_id_lab"]

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train_lab, X_test_lab, y_train_lab, y_test_lab = train_test_split(X, y_lab, test_size=0.2, random_state=42, stratify=y_lab)

# Crear una pipeline para el procesamiento de texto y el entrenamiento del modelo
pipeline_lab_nb = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english')),
    ('clf', MultinomialNB())
])

pipeline_lab_lr = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english')),
    ('clf', LogisticRegression(max_iter=200))
])

# Definir los parámetros para GridSearchCV
param_grid_nb = {
    'tfidf__ngram_range': [(1, 1), (1, 2), (1, 3)],
    'tfidf__max_df': [0.75, 0.85, 1.0],
    'tfidf__min_df': [1, 2, 5],
    'clf__alpha': [0.01, 0.1, 0.5, 1.0]  # Este parámetro es para MultinomialNB
}

param_grid_lr = {
    'tfidf__ngram_range': [(1, 1), (1, 2), (1, 3)],
    'tfidf__max_df': [0.75, 0.85, 1.0],
    'tfidf__min_df': [1, 2, 5],
    'clf__C': [0.01, 0.1, 1, 10]  # Parámetro para LogisticRegression
}

# Utilizar StratifiedKFold con 5 splits
cv = StratifiedKFold(n_splits=5)

# Realizar GridSearchCV para encontrar los mejores hiperparámetros
grid_search_nb = GridSearchCV(pipeline_lab_nb, param_grid_nb, cv=cv, n_jobs=-1, verbose=2)
grid_search_lr = GridSearchCV(pipeline_lab_lr, param_grid_lr, cv=cv, n_jobs=-1, verbose=2)

grid_search_nb.fit(X_train_lab, y_train_lab)
grid_search_lr.fit(X_train_lab, y_train_lab)

# Evaluar el modelo en el conjunto de prueba
nb_best_score = grid_search_nb.best_score_
lr_best_score = grid_search_lr.best_score_

# Imprimir los resultados de los modelos
print(f"Naive Bayes Best Score: {nb_best_score}")
print(f"Logistic Regression Best Score: {lr_best_score}")
print(f"Average Number of Participants: {avg_num_participantes}")

# Guardar los mejores modelos
joblib.dump(grid_search_nb.best_estimator_, 'best_model_naive_bayes.pkl')
joblib.dump(grid_search_lr.best_estimator_, 'best_model_logistic_regression.pkl')

# Crear un diccionario con los resultados
results = {
    "naive_bayes_best_score": nb_best_score,
    "logistic_regression_best_score": lr_best_score,
    "average_num_participantes_res": avg_num_participantes
}

# Guardar resultados en un archivo JSON
with open('model_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

print("Modelos y resultados guardados exitosamente.")
