# desafio-hdi
## ejecucion
### Forma recomendada (Docker compose)
Para utilizar por favor ejecutar docker compose up y automaticamente se creara la imagen y el contenedor exponiendo la aplicacion en el puerto 8000.
### Forma manual (FastAPI)
Si bien la aplicacion deberia estar lista para ser desplegada en un entorno docker, tambien es posible hacerlo utilizando fastAPI de manera local.

lo primero es instalar las dependencias definidas en el archivo ***requirements.txt***, preferiblemente utilizando un venv para no contaminar otros proyectos con dependencias no necesarias.

Luego de instalar venv y las dependencias necesarias, es necesario activar el ambiente venv, como esto varia de SO a SO, esto tendra que ser investigado a parte.

Luego con el ambiente venv activado solo es necesario ejecutar "fastapi run app/main.py"

tambien es posible leer la documentacion de la api utilizando el endpoint docs, gracias a la creacion automatica de dicha pagina por parte de fastAPI (http://127.0.0.1:8000/docs)

## envio de requests
Para facilitar el uso de fastAPI, el metodo de entrada seleccionado fue un GET request con un body json al endpoint /predict (http://127.0.0.1:8000/predict), el cual contiene la informacion necesaria para obtener la informacion requerida, un ejemplo es:
```
{
	"claim_id": "561205",
	"marca_vehiculo": "ferd",
	"antiguedad_vehiculo": "1",
	"tipo_poliza": "3",
	"taller": "4",
	"partes_a_reparar": "3",
	"partes_a_reemplazar": "2"
}
```
si bien se pueden excluir ciertas variables al no incluirlas en el json lo mas recomendable es incluirlas de todas formas.

Como resultado de la solicitud fastAPI respondera con las variables incluidas en la request y con el resultado en el valor "tiempo_en_taller", como por ejemplo:
```
[
	{
		"claim_id": 561205,
		"marca_vehiculo": "ferd",
		"antiguedad_vehiculo": 1,
		"tipo_poliza": 4,
		"taller": null,
		"partes_a_reparar": 3,
		"partes_a_reemplazar": 2,
		"tiempo_en_taller": -1
	}
]
```

# Otros
## endpoint predict_csv
Durante un periodo de pruebas se creo en endpoint predict_csv, al cual se le puede enviar una request con un body de texto plano que contenga los datos en el formato encontrado en el archivo ***claims_dataset.csv***, este endpoint se dejo en la aplicacion ya que es mas rapido ya que aplica la pipeline completa a un conjunto mas grande de datos, comparado con el ingreso manual de _claims_

## consideraciones tomadas
- Se encontro que el pipeline 5, es innecesario ya que los datos que agrega no son utilizados por el modelo, ademas de que su tiempo de ejecucion es relativamente largo. Por lo tanto este no es utilizado en la ejecucion
- Se encontro que el pipeline 4 es dependiente del pipeline 3 en lugar del pipeline 2, pero no se produjeron cambios a partir de este descubrimiento
- Se utilizo fastAPI ya que es una forma rapida y facil de crear API, ademas de que cuenta con un gran soporte gracias a su extendida documentacion y utilizacion por parte de la comunidad
- Entre las librerias que se instalaron de manera manual se encuentran dill, fastAPI, numpy, pandas, Scikit-learn
- Al principio el proyecto utilizaba python 3.14 pero por problemas para cargar los archivos pkl, se termino utilizando python 3.11, si bien en ninguna parte aparece documentado la version utilizada, me parece bueno comentarlo en este README

## Posiblidades de mejora
- Cambiar la carga y ejecucion a un modulo como tal, para evitar utilizar _quick fixes_
- aumentar los formatos de entrada y salida
- mejorar el formato de registros para incluir otros valores como tiempo de ejecucion.