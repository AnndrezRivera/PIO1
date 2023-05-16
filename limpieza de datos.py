import pandas as pd
import json


# Cargar las partes divididas
df_parte1 = pd.read_csv('dataset\\parte1.csv')
df_parte2 = pd.read_csv('dataset\\parte2.csv')

# Concatenar las partes en un solo DataFrame
df = pd.concat([df_parte1, df_parte2])

def procesador(df, columna):
    # Reemplazar valores faltante por cadenas vacías
    df[columna].fillna('', inplace=True)

    # Convierte los valores a cadenas de texto y luego remplaza comillas simples por comillas dobles para el correcto funcionamiento de json
    df[columna] = df[columna].astype(str).str.replace("'", '"')

    # Convertir las cadenas en diccionarios utilizando json.loads()
    def extractor(valores):
        try:
            # Convertir el valor JSON a un objeto de Python
            cadenas = json.loads(valores)
            # Verifica que sea una lista
            if isinstance(cadenas, list):
                # Crea una lista llamada names que contiene los valores de la clave 'name' de cada elemento en la lista 
                # Agrega cadena vacia si el elemento no tiene una clave 'name'
                names = [item.get('name', '') for item in cadenas]
                #En caso de haber varios elementos en la lista 'names', los une y separa con una coma (,)
                return ', '.join(names)
                #Si el objeto no es lista, se verifica si es diccionario
            elif isinstance(cadenas, dict):
                # Retornar el valor asociado a la clave 'name', si no existe, se retorna una cadena vacia
                return cadenas.get('name', '')
        # Captura posibles errores al decodificar el archivo
        except json.JSONDecodeError:
            # Retorna cadena vacia al ocurrir un error
            return ''

    df[columna] = df[columna].apply(extractor)

    return df

df = procesador(df, 'spoken_languages')
df = procesador(df, 'belongs_to_collection')
df = procesador(df, 'genres')
df = procesador(df, 'production_companies')
df = procesador(df, 'production_countries')

# Eliminar columnas innecesarias
df = df.drop(['video', 'imdb_id', 'adult', 'original_title', 'vote_count', 'poster_path', 'homepage'], axis=1)
# Cambiar valores nulos o vacios por 0
df['revenue'] = df['revenue'].fillna(0)
df['budget'] = df['budget'].fillna(0)
# Cambiar el formato de la columna "release_date" a "AAAA-mm-dd"
df['release_date'] = pd.to_datetime(df['release_date'], format='%Y-%m-%d', errors='coerce')
# Eliminar filas con valores nulos en la columna "release_date"
df = df.dropna(subset=['release_date'])
# Crear la columna "release_year" que contenga el año extraído de la columna "release_date"
df['release_year'] = df['release_date'].dt.year

# Convertir los elementos a valores numéricos y reemplazar los no numéricos por NaN
df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')
df['budget'] = pd.to_numeric(df['budget'], errors='coerce')
df['popularity'] = pd.to_numeric(df['popularity'], errors='coerce')
df['id'] = pd.to_numeric(df['id'], errors='coerce')

# Calcular el retorno de inversión y crear la columna "return"
df['return'] = df['revenue'] / df['budget']
# Cambiar los valores NaN por 0 en las columnas "revenue" y "budget"
df['revenue'] = df['revenue'].fillna(0)
df['budget'] = df['budget'].fillna(0)
df['return'] = df['return'].fillna(0)
# Reemplazar los valores infinitos (resultado de dividir por 0) por 0
df['return'] = df['return'].replace([float('inf')], 0)


print(df.head())
