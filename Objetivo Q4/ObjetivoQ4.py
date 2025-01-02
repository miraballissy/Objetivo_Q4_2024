import requests
import pandas as pd

#URL de la API
api_url= "https://api-intranet-jira.portinos.com/v1/api/get-time-issue/DEVLAR-1738"
#Solicitud GET a la API
response= requests.get(api_url)
#Verificación exitosa
if response.status_code == 200:
    #convertir la respuesta JSON a un diccionario de Python
    data = response.json()
    #Crear dataframe de pandas a partir de los datos
    df = pd.DataFrame(data)
    print(df)
else:
    print(f"Error en la solicitud: {response.status_code}")