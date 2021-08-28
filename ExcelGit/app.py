import pandas as pd
archivo = 'Filtrar Excel\libro.xlsx'
datos = pd.read_excel(archivo)
print("Sin filtro:\n",datos.head(10))

datos = datos[datos["Universidad"] == "itcj"]

print("Con filtro:\n", datos.head(10))

