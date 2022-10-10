#Exercise here ("https://drive.google.com/file/d/10RUsyp8WKjBSdawZOGYHFuwQ9pguCS5X/view?usp=sharing")
#csv file ("https://drive.google.com/file/d/1MlkkICtn7NWjBxypShQQmcskdVHy2V9n/view?usp=sharing")

import csv, json
import pandas as pd
import numpy as np

def solucion():

    df = pd.read_csv("JandJ.csv")
    df ["restaC-O"] = (df["Close"] - df["Open"])

    df ["abs Diferencia Close-Open"] = abs(df["restaC-O"])

    df ["Comportamiento de la accion"] = ""
    coldif = df["restaC-O"]
    df.loc [coldif>0, "Comportamiento de la accion"] = "SUBE"
    df.loc [coldif<0, "Comportamiento de la accion"] = "BAJA"
    df.loc [coldif==0, "Comportamiento de la accion"] = "ESTABLE"

    df2 = df[["Date", "Comportamiento de la accion", "abs Diferencia Close-Open"]]
    df_output = df2.rename({"Date": "Fecha analizada"}, axis = "columns")
    df_output.to_csv("analisis_archivo.csv", index = False, sep="\t", encoding = "UTF-8")

    indice_min_vol = df["Volume"].idxmin()
    fecha_min_vol = df.at[indice_min_vol, "Date"]
    min_vol = df["Volume"].min()

    indice_max_vol = df["Volume"].idxmax()
    fecha_max_vol = df.at[indice_max_vol, "Date"]
    max_vol = df["Volume"].max()

    lamedia_vol = df["Volume"].mean()

    indice_max_resta = df["abs Diferencia Close-Open"].idxmax()
    fecha_max_resta = df.at[indice_max_resta, "Date"]
    max_resta = df["abs Diferencia Close-Open"].max()

    archivo_json = {
        "date_lowest_volume": fecha_min_vol,
        "lowest_volume": str(min_vol),
        "date_highest_volume" : fecha_max_vol,
        "highest_volume" : str(max_vol),
        "mean_volume" : str(lamedia_vol),
        "date_greatest_difference": fecha_max_resta,
        "greatest_difference": str(max_resta)
    }

    
    with open("detalles.json","w") as file:
        json.dump(archivo_json,file)