# 📚 SAT-2 English Text Classifier

This Streamlit web app allows non-expert users to classify English text related to SAT-2 content using a fine-tuned DistilBERT model. 
It demonstrates Milestone 2.1 of the Airavata VIP Spring 2025 project: **Designing for Non-Expert Users**.

---

## 🚀 Features

- Simple and intuitive UI using Streamlit
- Input English academic/literary text and get a predicted label
- Uses a Hugging Face model for classification
- Displays label and confidence score
- Includes error handling and user guidance

---

## 🛠️ How to Run the App Locally

### 1. Clone or Download This Project

```bash
cd C:\Users\YourUsername
git clone <your-repo-url>
cd sat2_classifier

Or manually create the folder sat2_classifier and place app.py inside.

3. Install Required Packages
pip install streamlit transformers torch matplotlib

4. Run the App
python -m streamlit run app.py
Then open your browser to:
http://localhost:8501

✏️ Example Input
The protagonist’s moral struggle illustrates the conflict between personal duty and societal norms.

📦 Dependencies
•  Python 3.10 or 3.12
•  Streamlit
•  Hugging Face Transformers
•  PyTorch
•  Matplotlib (optional for visual confidence bar)
```
## Cybershuttle Usage
1. Access notebook on Cybershuttle: https://hub.cybershuttle.org/hub/user-redirect/lab/tree/notebook.ipynb (local version is notebook.ipynb)
2. Modify line of code with user input text
3. Run all cells of notebook


