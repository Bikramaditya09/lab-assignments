from fastapi import APIRouter, Form 
import pandas as pd 
from services.service import PredictionService
import os 
from fastapi.responses import JSONResponse

router = APIRouter()

artifact_path = os.path.join(
    os.path.dirname(__file__),
    '..',
    'artifact',
    'linear_regression_model.pkl'
)

artifact_path = os.path.abspath(artifact_path)

prediction_service = PredictionService(model_path=artifact_path)

@router.post('/predict')
async def predict(
    SquareFeet: int = Form(...),
    Bedrooms: int = Form(...),
    Bathrooms: int = Form(...),
    Neighborhood: str = Form(...)
):
    input_features = [{
        'SquareFeet': SquareFeet,
        'Bedrooms': Bedrooms,
        'Bathrooms': Bathrooms,
        'Neighborhood': Neighborhood
    }]
    features = pd.DataFrame(input_features)
    predicted_price = prediction_service.predict(features)
    return JSONResponse(content={"price": predicted_price})


    