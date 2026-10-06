# Customer Support Fine-Tuning Model

An AI-powered Customer Support Classification system built using
Transformer-based NLP and Fine-Tuning.

## Project Overview

This project fine-tunes a Transformer model to classify customer
support messages into different support categories.

## Features

- Customer support message classification
- Transformer-based NLP model
- Fine-tuning on custom customer support data
- Confidence score for predictions
- Streamlit web application
- Easy-to-use user interface

## Support Categories

- Account / Login Issue
- Payment Issue
- Delivery Issue
- Refund Request
- Product Issue
- Cancellation Request

## Technologies Used

- Python
- Transformers
- Hugging Face
- PyTorch
- Datasets
- Accelerate
- Streamlit

## Project Workflow

Customer Message  
↓  
Text Preprocessing  
↓  
Tokenizer  
↓  
Fine-Tuned Transformer Model  
↓  
Prediction  
↓  
Support Category + Confidence Score

## Project Files

- `Customer_Finetuning_model.ipynb` – Model training and fine-tuning
- `app.py` – Streamlit application
- `requirements.txt` – Required Python packages

## How to Run

Install the required packages:

```bash
pip install -r requirements.txt
