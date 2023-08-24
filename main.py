import os
import sys

# Add the parent directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from fastapi import FastAPI
from starlette.responses import JSONResponse

from my_folder_.predictor.predict import ModelPredictor
from my_folder_.Load.load_data import DataLoader
app = FastAPI()

@app.get('/', status_code=200)
async def healthcheck():
    return 'Bankruptcy classifier is all ready to go!'

@app.post('/predict')
def predict(bankrupcy_features: DataLoader):
    predictor = ModelPredictor("my_folder_\My_model\My_model_regression")
    X = [bankrupcy_features.Operating_gross_margin,
        bankrupcy_features.Operating_profit_rate,
        bankrupcy_features.tax_rate,
        bankrupcy_features.interest_expense_ratio,
        bankrupcy_features.cash_flow_to_equity,
        bankrupcy_features.gross_profit_to_sales]
    print([X])
    prediction = predictor.predict([X])
    return JSONResponse(f"Resultado predicción: {prediction}")
    