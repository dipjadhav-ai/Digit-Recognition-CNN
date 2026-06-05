from fastapi import FastAPI, UploadFile, File
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io

from model import predict

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "Digit Classifier Running"
    }

@app.post("/predict")
async def predict_digit(
    file: UploadFile = File(...)
):

    image_bytes = await file.read()

    image = Image.open(
        io.BytesIO(image_bytes)
    )

    prediction = predict(image)

    return {
        "prediction": prediction
    }