## Student information
**Full name**: Trần Kiên Cường \
**Student ID**: 25127025

## Model
**Name**: DistilBERT base uncased finetuned SST-2 \
**Link**: https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english

## System's Functionality
The system is a Web API built with FastAPI for sentiment analysis (text classification). It receives an input text message from the user, uses the Hugging Face model `distilbert-base-uncased-finetuned-sst-2-english` to classify its sentiment into **POSITIVE** or **NEGATIVE** with a confidence score, and returns the result in JSON format.

## Dependencies
Download the required dependencies using the command below:
```
pip install -r requirements.txt
```

## How to run
First, create a virtual environment:
```
python -m venv venv
```
Then download the required dependencies:
```
pip install -r requirements.txt
```
Now start the server:
```
uvicorn main:app --reload
```
Run the test (example requests & responses):
```
python test.py
```

## Demonstration video
Youtube link: https://www.youtube.com/watch?v=gOphUHEM4FY
