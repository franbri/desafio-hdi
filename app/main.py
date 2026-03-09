import dill
import pandas as pd
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
 

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

class InputData(BaseModel):
    claim_id: int | None = None
    marca_vehiculo: str
    antiguedad_vehiculo: int
    tipo_poliza: int
    taller: int
    partes_a_reparar: int
    partes_a_reemplazar: int

class MLModel():
    def __init__(self):
        self.pipeline1 = dill.load(open('./app/pipeline_1.pkl', 'rb'))
        self.pipeline2 = dill.load(open('./app/pipeline_2.pkl', 'rb'))
        self.pipeline3 = dill.load(open('./app/pipeline_3.pkl', 'rb'))
        self.pipeline4 = dill.load(open('./app/pipeline_4.pkl', 'rb'))
        self.pipeline5 = dill.load(open('./app/pipeline_5.pkl', 'rb'))
        self.linnear_regression = dill.load(open('./app/linnear_regression.pkl', 'rb'))
    


app = FastAPI()

@app.on_event("startup")
async def startup_event():
    # load class on startup
    app.state.model = MLModel()
    # literal quickfix para que el pipeline encuentre a numpy
    app.state.model.pipeline2.__globals__['np'] = np

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.get("/datain")
def datain(inputdata: InputData, q: str | None = None):
    X = inputdata.model_dump()
    return pd.DataFrame(data=[X])

@app.get("/predict")
def predict(inputdata: InputData):
    X = inputdata.model_dump()
    df = pd.DataFrame(data=[X])
    out1 = app.state.model.pipeline1(df)
    out2 = app.state.model.pipeline2(out1)
    out3 = app.state.model.pipeline3(df)
    out4 = app.state.model.pipeline4(out3)
    #out5 = app.state.model.pipeline5(out3)
    df[["log_total_piezas","marca_vehiculo_encoded","valor_vehiculo","valor_por_pieza","antiguedad_vehiculo"]]
    print(out4)
    predict_data = pd.concat([out2["log_total_piezas"], out3["marca_vehiculo_encoded"], out4[["valor_vehiculo", "valor_por_pieza"]], df["antiguedad_vehiculo"]], axis=1)
    predict_data.fillna(diccionario_imputacion)
    prediction = app.state.model.linnear_regression.predict(predict_data)
    predict_data["tiempo_en_talle"] = prediction
    return predict_data.to_json(orient="records")

@app.get("/predict_list")
def predict_list(inputdata: list[InputData]):
    print(inputdata)
    X = inputdata.model_dump()
    df = pd.DataFrame(data=[X])
    out1 = app.state.model.pipeline1(df)
    out2 = app.state.model.pipeline2(out1)
    out3 = app.state.model.pipeline3(df)
    out4 = app.state.model.pipeline4(out2)
    out5 = app.state.model.pipeline5(out3)
    predict_data = pd.concat([out4, out5], axis=1)
    predict_data.fillna(diccionario_imputacion)
    prediction = app.state.model.linnear_regression.predict(predict_data)

    print(prediction)
    return prediction.to_json(orient="records")