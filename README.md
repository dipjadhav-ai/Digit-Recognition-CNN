# Handwritten Digit Recognition using CNN

A Machine Learning web application that recognizes handwritten digits (0–9) from uploaded images using a Convolutional Neural Network (CNN) built with PyTorch.

## Live Demo

Working Link: [[Click Here](https://6a27f6f223e9ce042d534afc--lively-semifreddo-f67b45.netlify.app/)]

Backend API: [[Click Here](https://digit-recognition-cnn-arau.onrender.com/predict)]

---

## Project Overview

This project implements an end-to-end handwritten digit recognition system:

- Trained a CNN model using PyTorch
- Built a FastAPI backend for model inference
- Created a frontend using HTML, CSS, and JavaScript
- Deployed the backend on Render
- Deployed the frontend on Netlify

Users can upload an image containing a handwritten digit and receive the predicted digit instantly.

---

## Features

- Image upload interface
- Real-time digit prediction
- CNN-based classification
- REST API using FastAPI
- Cloud deployment

---

## Tech Stack

### Machine Learning

- PyTorch
- NumPy
- Pillow

### Backend

- FastAPI
- Uvicorn

### Frontend

- HTML
- CSS
- JavaScript

### Deployment

- Render (Backend)
- Netlify (Frontend)

---

## Model Architecture

```python
Input: 1 x 28 x 28

Conv2D(1 → 32)
ReLU
MaxPool

Conv2D(32 → 64)
ReLU
MaxPool

Conv2D(64 → 128)
ReLU
MaxPool

Flatten

Linear(1152 → 256)
ReLU

Linear(256 → 10)
```

The model outputs probabilities for digits:

```text
0 1 2 3 4 5 6 7 8 9
```

---

## Project Structure

```text
DIGIT-RECOGNITION-CNN
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── models/
│   ├── app.py
│   ├── model.py
│   ├── cnn.pth
│   └── requirements.txt
│
├── notebooks/
│
└── README.md
```

---

## API Endpoints

### Health Check

```http
GET /
```

Response

```json
{
  "message": "Digit Classifier Running"
}
```

---

### Predict Digit

```http
POST /predict
```

Request:

Multipart form data containing an image file.

Response:

```json
{
  "prediction": 7
}
```

---

## Local Setup

### Clone Repository

```bash
git clone https://github.com/<your-username>/Digit-Recognition-CNN.git

cd Digit-Recognition-CNN
```

### Install Dependencies

```bash
pip install -r models/requirements.txt
```

### Run Backend

```bash
cd models

uvicorn app:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

---

### Run Frontend

Open:

```text
frontend/index.html
```

in your browser.

---

## Screenshots

### Application Interface

Add screenshots inside the `screenshots` folder and reference them here.

```md
![Home Page](screenshots/home.png)
```

---

## Learning Outcomes

This project helped me learn:

- Practical Implementation of the Convolutional Neural Networks (CNNs) using PyTorch
- Image preprocessing techniques
- Model deployment using FastAPI
- REST API development
- Frontend–Backend integration
- Cloud deployment with Render and Netlify
- Git and GitHub workflow
---

## Author

**Dip Rajhans Jadhav**

Mechanical Engineering, IIT Madras

GitHub: https://github.com/<dipjadhav-ai>

LinkedIn: [[Click Here](https://www.linkedin.com/in/dip-jadhav-70883134a/)]

---
