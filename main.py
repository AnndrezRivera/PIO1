import pandas as pd
import uvicorn
from fastapi import FastAPI

df = pd.read_csv('dataset/datos.csv')


app = FastAPI()

@app.get('/peliculas_mes/{mes}')
def peliculas_mes(mes: str):
    # Filtrar el DataFrame por el mes específico
    df['release_date'] = pd.to_datetime(df['release_date'])
    peliculas_mes = df[df['release_date'].dt.month == int(mes)]
    # Obtener la cantidad de películas estrenadas ese mes
    cantidad = len(peliculas_mes)
    return {'mes': mes, 'cantidad': cantidad}

@app.get('/peliculas_dia/{dia}')
def peliculas_dia(dia:str):
    df['release_date'] = pd.to_datetime(df['release_date'])
    peliculas_dia = df[df['release_date'].dt.day == int(dia)]  
    cantidad = len(peliculas_dia)  
    return {'dia':dia, 'cantidad':cantidad}

@app.get('/franquicia/{franquicia}')
def franquicia(franquicia: str):
    peliculas_franquicia = df[df['belongs_to_collection'] == franquicia]
    cantidad = len(peliculas_franquicia)
    # Calcular la ganancia total de la franquicia
    ganancia_total = peliculas_franquicia['revenue'].sum()
    # Calcular la ganancia promedio de la franquicia
    ganancia_promedio = peliculas_franquicia['revenue'].mean()
    return {'franquicia': franquicia, 'cantidad': cantidad, 'ganancia_total': ganancia_total, 'ganancia_promedio': ganancia_promedio}

@app.get('/peliculas_pais/{pais}')
def peliculas_pais(pais: str):
    mask = df['production_countries'].notnull()
    df_filtered = df[mask]
    peliculas_pais = df_filtered[df_filtered['production_countries'].str.contains(pais, case=False)]
    cantidad = len(peliculas_pais)
    return {'pais': pais, 'cantidad': cantidad}

@app.get('/productoras/{productora}')
def productoras(productora: str):
    peliculas_productora = df[df['production_companies'] == productora]
    ganancia_total = peliculas_productora['revenue'].sum()
    cantidad = len(peliculas_productora)
    return {'productora': productora, 'ganancia_total': ganancia_total, 'cantidad': cantidad}

@app.get('/retorno/{pelicula}')
def retorno(pelicula: str):
    pelicula_info = df[df['title'] == pelicula]

    if pelicula_info.empty:
        raise HTTPException(status_code=404, detail="Pelicula no encontrada")

    inversion = int(pelicula_info['budget'].iloc[0])
    ganancia = int(pelicula_info['revenue'].iloc[0])
    retorno = float(pelicula_info['return'].iloc[0])
    anio = int(pelicula_info['release_year'].iloc[0])

    return {
        'pelicula': pelicula,
        'inversion': inversion,
        'ganancia': ganancia,
        'retorno': retorno,
        'anio': anio
    }


@app.get('/')
def root():
    return {'mensaje': 'Bienvenido a la API!'}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)
