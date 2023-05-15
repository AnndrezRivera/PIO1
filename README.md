# Modelo de Recomendación para Servicios de Agregación de Plataformas de Streaming

## Descripción del problema

En este repositorio se presenta una solución para llevar un modelo de recomendación de películas y series del ámbito de la investigación y desarrollo al mundo real. El objetivo es implementar un sistema de recomendación en una start-up que provee servicios de agregación de plataformas de streaming.

## Contexto

El contexto de este proyecto se encuentra en una start-up que busca ofrecer a sus usuarios recomendaciones personalizadas de películas y series de diversas plataformas de streaming. 

### Como trabajo de desarrollan los siguientes puntos: 
- Analizar los datos existentes y comprender su estructura y calidad.
- Realizar tareas de Data Engineering para limpiar, transformar y preparar los datos de manera adecuada para el modelo de recomendación.
- Diseñar e implementar un modelo de Machine Learning que pueda generar recomendaciones personalizadas.

# Desarrollo API
Tiene como objetivo disponibilizar los datos de la empresa mediante una API utilizando el framework FastAPI. Las consultas que se proponen son las siguientes:

### Endpoints disponibles
Se han creado 6 funciones para los endpoints que se consumirán en la API. Cada función tiene un decorador que define el método HTTP correspondiente (@app.get('/')).

#### peliculas_mes(mes)
Esta función recibe un mes y devuelve la cantidad de películas que se estrenaron históricamente en ese mes. La respuesta se presenta en un formato JSON con el mes y la cantidad de películas.

#### peliculas_dia(dia)
Esta función recibe un día y devuelve la cantidad de películas que se estrenaron históricamente en ese día. La respuesta se presenta en un formato JSON con el día y la cantidad de películas.

#### franquicia(franquicia)
Esta función recibe una franquicia y devuelve la cantidad de películas, la ganancia total y el promedio de ganancias de la franquicia. La respuesta se presenta en un formato JSON con la franquicia, la cantidad de películas, la ganancia total y el promedio de ganancias.

#### peliculas_pais(pais)
Esta función recibe un país y devuelve la cantidad de películas producidas en ese país. La respuesta se presenta en un formato JSON con el país y la cantidad de películas producidas.

#### productoras(productora)
Esta función recibe una productora y devuelve la ganancia total y la cantidad de películas que produjo. La respuesta se presenta en un formato JSON con la productora, la ganancia total y la cantidad de películas producidas.

#### retorno(pelicula)
Esta función recibe una película y devuelve la inversión, la ganancia, el retorno y el año en que se lanzó. La respuesta se presenta en un formato JSON con la película, la inversión, la ganancia, el retorno y el año en que se lanzó.

#### recomendacion(titulo)
Esta función recibe el título de una película y devuelve una lista de 5 películas similares recomendadas. La respuesta se presenta en un formato JSON con la lista recomendada de películas similares.
