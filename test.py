import pandas as pd
import dill

df = pd.read_csv("claims_dataset.csv", delimiter="|")
diccionario_imputacion = {
    "log_total_piezas": 1.4545,
    "marca_vehiculo_encoded": 0,
    "valor_vehiculo": 3560,
    "valor_por_pieza": 150,
    "antiguedad_vehiculo": 1,
    "tipo_poliza": 1,
    "taller": 1,
    "partes_a_reparar": 3,
    "partes_a_reemplazar": 1,
}
# df.fillna(diccionario_imputacion)


data = dill.load(open("pipeline_1.pkl", "rb"))
# print(data)


bruh = data(df)
print(bruh)
