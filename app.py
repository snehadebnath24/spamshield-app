import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import time

# ------------------ SETUP ------------------
st.set_page_config(page_title="SpamShield", page_icon="🛡️", layout="centered")

ps = PorterStemmer()

# ------------------ UI STYLE ------------------

st.markdown("""
<style>


/*  Animation Clean Dark Colors */
.stApp {
    background: linear-gradient(-45deg,#0f172a, #1e293b, #0f172a, #020617);
    background-size: 700% 700%;
    animation: gradientMove 4s ease infinite;
    color: #e2e8f0;
}

/* SAME animation (unchanged) */
@keyframes gradientMove {
    0% {background-position: 0% 50%;}
    25% {background-position: 50% 100%;}
    50% {background-position: 100% 50%;}
    75% {background-position: 50% 0%;}
    100% {background-position: 0% 50%;}
}

/* Card */
.card {
    background-color: rgba(30, 41, 59, 0.85);
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0px 0px 25px rgba(0,0,0,0.7);
}

/* ✨ Glowing Button */
.stButton>button {
    background: linear-gradient(45deg, #22c55e, #4ade80);
    color: black;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 16px;
    transition: all 0.3s ease;
    box-shadow: 0 0 10px rgba(34,197,94,0.5);
}

/* Hover Glow */
.stButton>button:hover {
    box-shadow: 0 0 25px rgba(34,197,94,0.9);
    transform: scale(1.05);
}

/* Text area */
textarea {
    background-color: #0f172a !important;
    color: white !important;
    border-radius: 10px !important;
    border: 1px solid #4ade80 !important;
}

/* Label */
label {
    color: #e2e8f0 !important;
    font-size: 16px !important;
    font-weight: 500;
}

/* Hide top bar */
header {visibility: hidden;}

</style>
""", unsafe_allow_html=True)



# ------------------ LOAD MODEL ------------------
tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

# ------------------ NLP FUNCTION ------------------
def transform_text(text):
    text = text.lower()
    words = nltk.word_tokenize(text)

    filtered = []
    for w in words:
        if w.isalnum() and w not in stopwords.words('english'):
            filtered.append(ps.stem(w))

    return " ".join(filtered)

# ------------------ LINK CHECK ------------------
def contains_link(text):
    return "http" in text or "www" in text

# ------------------ SPAM WORD HIGHLIGHT ------------------
spam_keywords = ["win", "free", "prize", "click", "offer", "urgent", "money"]

def highlight_spam_words(text):
    words = text.split()
    highlighted = []
    for w in words:
        if w.lower() in spam_keywords:
            highlighted.append(f"<span style='color:red;font-weight:bold'>{w}</span>")
        else:
            highlighted.append(w)
    return " ".join(highlighted)

# ------------------ MAIN UI ------------------


st.markdown("""
<div style='text-align: center; margin-bottom: 20px;'>
    <h1 style='margin-bottom: 5px;'>🛡️ SpamShield</h1>
    <p style='color: #94a3b8; font-size: 16px;'>
        AI-based spam detection and user protection system
    </p>
</div>
""", unsafe_allow_html=True)

input_sms = st.text_area("Enter your message:", height=150)

if st.button("Analyze Message"):
    if input_sms.strip() == "":
        st.warning("Please enter a message")
    else:
        #  Loading animation
        with st.spinner("Analyzing message..."):
            time.sleep(1)

            transformed_sms = transform_text(input_sms)
            vector_input = tfidf.transform([transformed_sms])

            result = model.predict(vector_input)[0]
            prob = model.predict_proba(vector_input)[0][1]

        st.markdown("---")

        #  RESULT
        if result == 1:
            st.error("SPAM DETECTED")

            st.warning("""
Safety Tips:
• Do NOT click unknown links  
• Do NOT share OTP or passwords  
• Block suspicious sender  
""")
        else:
            st.success("SAFE MESSAGE")



        #  Link warning
        if contains_link(input_sms):
            st.info("This message contains a link — be careful")

      

st.markdown('</div>', unsafe_allow_html=True)
