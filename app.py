import uvicorn
import pandas as pd
from fastapi import FastAPI, Query

################################################################################ 
# DEMARRAGE DE L'INSTANCE FASTAPI
################################################################################

app = FastAPI(title="Awesome API",
    description="API de requête de données RH d'IBM",
    version="0.0.7" 
)
##############################################################################
# LISTE DES ENDPOINTS DISPONIBLES
##############################################################################
# /
# /preview
# /unique-values
# /groupby
# /filter-by
# /quantile


##############################################################################
# CHARGEMENT DU DATASET DANS DF
##############################################################################

df = pd.read_excel("ibm_hr_attrition.xlsx")


##############################################################################
# DEFINITION DES ENDPOINTS
##############################################################################

# endpoint racine "/"
@app.get("/")
async def index():

    message = "Welcome to the awesome API of the Back-End Development Team ! " \
    "This `/` is the most simple and default endpoint. " \
    "If you want to learn more, check out documentation of the api at `/docs`"

    return message

# endpoint preview

@app.get("/preview")
async def preview(n: int = 5):
    return df.head(n).to_dict(orient="records")  # to_dict parce que Fastapi ne sait pas utiliser les df (orient permet d'avoir ligne/ligne)


# endpoint unique

@app.get("/unique-values")
async def unique_values(column : str ="EmployeeNumber"):
    return df[column].unique().tolist()         # tolist() parce que unique() renvoie un array

# endpoint groupby

@app.get("/groupby")
async def group_by(column : str ="Department",
                   target : str = "MonthlyIncome",
                   aggregator : str = "mean"
                   ) :
    agg_result = df.groupby(column)[target].agg(aggregator).round(2)
    return agg_result.to_dict()

# endpoint filter-by

@app.get("/filter-by")
async def filter_by(column : str ="Department",
                    cat : list[str]= Query(["Sales"])  #La fonction Query de FastAPI nécessaire pour prendre en compte une liste
                    ):
         filter_result = df[df[column].isin(cat)]
         return filter_result.to_dict(orient="records")


# endpoint quantile

@app.get("/quantile")
async def quantile(column : str ="MonthlyIncome",
                   position : int=0,    # 0 pour bottom , 1 pour top
                   quant : float=0.1):  # float de 0 à 1 définit le quantile
     if position == 0 :
          result = df[df[column] <= df[column].quantile(quant)]
     else :
          result = df[df[column] >= df[column].quantile(1-quant)]
          
     return result.to_dict(orient="records")
