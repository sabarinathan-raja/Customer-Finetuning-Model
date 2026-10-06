
import streamlit as st
from transformers import pipeline

# Load our trained model
classifier = pipeline(
    "text-classification",
    model="./customer_support_model",
    tokenizer="./customer_support_model"
)

# Page title
st.title("🎫 Customer Support Ticket Classifier")

st.write("Enter a customer message and the AI will predict its category.")

# Text input
message = st.text_area(
    "Customer Message",
    placeholder="Example: I was charged twice for my payment"
)

# Prediction button
if st.button("Predict"):

    if message.strip() == "":
        st.warning("Please enter a customer message.")

    else:
        result = classifier(message)[0]

        label = result["label"]
        score = result["score"]

        st.success(f"Predicted Category: {label}")
        st.info(f"Confidence: {score * 100:.2f}%")
