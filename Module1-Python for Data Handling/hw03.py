# Importamos pandas
import pandas as pd

# Leemos nuetsro archivo
df = pd.read_csv('data/weather_data.csv')

# Filtramos dada una ciudad en especifico
dfCiudad = df[df['Location'] == 'San Antonio']

# Creamos nueva columna con vientos mayores a 21 kmh
dfCiudad['viento_peligroso'] = dfCiudad['Wind_Speed_kmh'] >= 21.0

# Creamos nueva columna con basado en humidity menor a 40%
dfCiudad['clima_seco'] = dfCiudad['Humidity_pct'] <= 40

# Redondeamos la temperatura
dfCiudad['Temperature_C'] = dfCiudad['Temperature_C'].apply(round)

# Mostramos los primeros 50 datos
print(dfCiudad.head(50))