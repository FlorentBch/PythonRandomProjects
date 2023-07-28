from fastapi import FastAPI, Query
import pandas as pd

app = FastAPI()

# Charger les données depuis les fichiers JSON et CSV
data_csv = pd.read_csv('Data/csv/VesselsParticular.csv')

# Endpoint pour récupérer les informations sur plusieurs bateaux en fonction de leurs codes
@app.get("/Vessels")
async def get_multiple_vessel_info(codes: list[str] = Query(...)):
    # Filtrer les informations sur les bateaux correspondant aux codes depuis le fichier CSV
    vessel_info = data_csv.loc[data_csv['vesselCode'].isin(codes), ['vesselCode', 'vesselName', 'flagCountry']]
    return vessel_info.to_dict(orient='records')
    
# Endpoint pour récupérer les informations de tous les bateaux
@app.get("/Vessels/AllVessels")
async def get_all_vessels():
    return data_csv.to_dict(orient='records')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
