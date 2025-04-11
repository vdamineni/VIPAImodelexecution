import streamlit as st
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import matplotlib.pyplot as plt

# Page title
st.set_page_config(page_title="SAT-2 Text Classifier", layout="centered")
st.title("📚 SAT-2 English Text Classifier")
st.write("This app uses a fine-tuned DistilBERT model to classify text related to SAT-2 English exam topics.")

# Text input
user_input = st.text_area("Enter your text below:", height=200)

# Help and examples
with st.expander("💡 Help & Examples"):
    st.markdown("""
    - This model is fine-tuned to recognize topics in English SAT-2 exam texts.
    - Try pasting a paragraph from a literature article or grammar question.
    - **Example Input:** _'The protagonist's moral struggle illustrates the conflict between personal duty and societal norms.'_
    """)

# Button to run classification
if st.button("Classify"):
    if user_input.strip() == "":
        st.error("❗ Please enter some text to classify.")
    else:
        with st.spinner("Classifying..."):
            try:
                # Load model and tokenizer
                tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
                model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english",trust_remote_code=True )


                # Prepare pipeline
                classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)

                # Perform classification
                result = classifier(user_input)[0]

                # Display results
                st.success("✅ Classification Result")
                st.markdown(f"### 🏷️ Predicted Label: `{result['label']}`")
                st.markdown(f"### 🔢 Confidence Score: `{result['score']:.4f}`")

                # Optional bar visualization
                st.bar_chart({"Confidence": [result["score"]]})

            except Exception as e:
                st.error("⚠️ An error occurred during classification.")
                st.text(f"Details: {e}")
