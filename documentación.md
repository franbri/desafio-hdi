# Instructivo para Desafío Técnico de Machine Learning Engineer

Bienvenido al desafío técnico para el cargo de Machine Learning Engineer. Este documento proporciona las instrucciones necesarias para completar el desafío de manera exitosa.

Este desafío tiene como objetivo evaluar tus habilidades y conocimientos. Asegúrate de leer todas las indicaciones cuidadosamente antes de comenzar.

## Datos de Entrada

El dataset de predicción **claims_dataset.csv**, esta es la información que tu API recibirá para predecir.

- ‘claim_id’: Número de identificación del siniestro.
- ‘marca_vehiculo’: Marca del vehículo siniestrado.
- ‘antiguedad_vehiculo’: Antiguedad del vehículo en años desde su año de fabricación hasta el año del siniestro.
- ‘tipo_poliza’: Identificador del tipo de póliza asociada al vehículo siniestrado.
- ‘taller’: Identificador del taller donde se realizarán las reparaciones del vehículo.
- ‘partes_a_reparar’: Número de partes del vehículo que necesitan reparación.
- ‘partes_a_reemplazar’: Número de partes del vehículo que deben ser reemplazadas.

## Pipelines de Preprocesamiento

El pipeline del modelo, creado y entregado por un Data Scientist, consta de cinco archivos `.pkl` que ejecutan diferentes tareas sobre un dataframe, creando nuevas columnas. Estas son sus interdependencias:

1. **pipeline_1.pkl**: Independiente.
2. **pipeline_2.pkl**: Dependiente de *pipeline_1.pkl*.
3. **pipeline_3.pkl**: Independiente.
4. **pipeline_4.pkl**: Dependiente de *pipeline_2.pkl*.
5. **pipeline_5.pkl**: Dependiente de *pipeline_3.pkl*.

Estos pipelines se ejecutan con el método **pipeline(df)**. Donde;
- **pipeline**: objeto creado con libreria **dill** de python.
- **df**: dataframe que alimenta al pipeline para su procesamiento.

Asegúrate de revisar cada interacción para entender cómo se integran en el pipeline completo.

## Diccionario de Imputación

Corresponde al diccionario de imputación de nulos que el Data Scientist, desarrollador del modelo, no agregó como pipeline cuando envió el modelo.

**Nombre Columna** | **Valor a Imputar**
diccionario_imputacion = {
    'log_total_piezas': 1.4545,
    'marca_vehiculo_encoded': 0,
    'valor_vehiculo': 3560,
    'valor_por_pieza': 150,
    'antiguedad_vehiculo': 1,
    'tipo_poliza': 1,
    'taller': 1,
    'partes_a_reparar': 3,
    'partes_a_reemplazar': 1
}

## Condiciones especiales

1. El cliente que utilizará y consumirá el output del modelo predictivo, indicó expresamente que cuando el tipo de póliza es igual a 4, el modelo predictivo debe devolver siempre un valor de -1. Ya que este tipo de pólizas deben ser manejadas de forma especial.

2. El cliente indica que el tiempo de respuesta de la API debe ser lo más rápida posible. Para tiempos de respuesta muy altos, el sistema que realiza el API Request asumirá un error por **timeout**.

## Modelo Predictivo

El archivo **linnear_regression.pkl** contiene un modelo de Machine Learning entrenado con data histórica. Devuelve el tiempo en semanas que tardaría un vehículo en entrar y salir del taller mecánico. El modelo necesita de las siguientes features para predecir:

**Nombre Columna** | **Formato del Campo en Entrenamiento**
- 'log_total_piezas': float64
- 'marca_vehiculo_encoded': int64
- 'valor_vehiculo': int64
- 'valor_por_pieza': int64
- 'antiguedad_vehiculo': int64