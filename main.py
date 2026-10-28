from fastapi import FastAPI, HTTPException, status
from transformers import pipeline
from pydantic import BaseModel

app = FastAPI()

classifier = pipeline(
    task = "text-classification",
    model = "distilbert-base-uncased-finetuned-sst-2-english"
)

class PredictionInput(BaseModel):
    text: str


@app.get("/")
def home():
    return {
        "task": "text-classification",
        "model": "distilbert-base-uncased-finetuned-sst-2-english",
        "message": "Welcome to text-classication API test"
    }


@app.get("/health")
def health_check():
    if classifier is None:
        raise HTTPException(
            status_code = status.HTTP_503_SERVICE_UNAVAILABLE,
            detail = "System is not ready because the model has not loaded."
        )

    return{
        "status": "healthy",
        "model_loaded": True
    }


@app.post("/predict")
def predict(data: PredictionInput):
    message = data.text.strip()

    if len(message) == 0:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "Message must not be empty or only whitespaces."
        )

    try:
        output = classifier(message)
        result = output[0]

        return{
            "input_text": message,

            "prediction": {               
                "label": result["label"],
                "score": result["score"]
            },

            "status": "success"
        }

    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = f"Error during model's reasoning process: {str(e)}"
        )

