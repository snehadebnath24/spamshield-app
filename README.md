# spamshield-app
SpamShield – Spam Detection Web App
• Developed an NLP-based spam detection system using Python and Scikit-learn
• Implemented text preprocessing techniques including tokenization, stopword removal, and stemming
• Built an interactive UI using Streamlit with real-time spam classification
• Added features like risk-level detection, link warning, and highlighted suspicious keywords
• Deployed the application on Streamlit Cloud

# Live Demo

👉 https://spamshield-app-77.streamlit.app/

# Features
- Spam Detection using Machine Learning
- NLP-based Text Processing
- Risk Level Classification (High / Suspicious / Low)
- Link Detection Warning
- Highlighting Suspicious Words
- Interactive Web App using Streamlit
# Tech Stack
- Python
- Streamlit
- Scikit-learn
- NLTK
- Pickle
  # How It Works
- User enters a message  
- Text is preprocessed using NLP:
  - Tokenization  
  - Stopword removal  
  - Stemming  
- Text is converted using TF-IDF Vectorizer  
- Machine Learning model predicts:
  - Spam or Not Spam  
- App displays:
  - Result  
  - Risk level  
  - Safety tips  
  - Highlighted keywords  
# Project Structure
SpamShield/
│── app.py
│── model.pkl
│── vectorizer.pkl
│── requirements.txt
│── README.md
# Run Locally
pip install -r requirements.txt
streamlit run app.py
# Screenshots


Add screenshots of your app here
