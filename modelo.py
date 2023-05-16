from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import pairwise_distances
import pandas as pd
import joblib

df = pd.read_csv('datos.csv')

# Submuestreo de 20000 y semilla aleatoria 
sample_size = 20000  # ajusta el valor a la memoria
df_1 = df.sample(n=sample_size, random_state=42)

# Llena valores vacios, separa por coma ',' y uno por '|'
df_1['genres'] = df_1['genres'].fillna('')
df_1['genres'] = df_1['genres'].str.split(', ').apply(lambda x: '|'.join(x))

# Se crea un objeto TfidfVectorizer para calcular la matriz TF-IDF de los géneros
vectores = TfidfVectorizer()
matriz_tf = vectores.fit_transform(df_1['genres'])

#Calcula una matriz de similitud de coseno entre las filas de la matriz TF-IDF.
matriz_de_similitud = 1 - pairwise_distances(matriz_tf, metric='cosine')

# Create a DataFrame con los titulos de peliculas similares.
df_2 = pd.DataFrame(matriz_de_similitud, index=df_1['title'], columns=df_1['title'])

# Guarda la matriz de similitud y el vectorizador con joblib
joblib.dump(df_2, 'matriz_de_similitud.joblib')
joblib.dump(vectores, 'vectores.joblib')

# Carga los archivos creados
df_2 = joblib.load('matriz_de_similitud.joblib')
vectores = joblib.load('vectores.joblib')

# Definimos la funcion de recomendacion
def recomendaciones(title):
    pelis = df_2[title]
    peliculas_similares = pelis.sort_values(ascending=False)[1:6].index.tolist()
    return peliculas_similares

# Cargamos a fastapi
from fastapi import FastAPI

app = FastAPI()

@app.get('/recomendacion/{title}')
def recomendacion(title: str):
    peliculas_similares = recomendaciones(title)
    return {'recommended_list': peliculas_similares}
