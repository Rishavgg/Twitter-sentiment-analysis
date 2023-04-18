import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
nltk.download('stopwords')
ps=PorterStemmer()
#background image
import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
    
add_bg_from_local('mount.png') 
def transform_text(text):
  text=text.lower()
  text=nltk.word_tokenize(text)
  
  y=[]
  for i in text:
    if i.isalnum():
      y.append(i)
  # cloning
  text=y[:]
  y.clear()

  for i in text:
    if i not in stopwords.words('english') and i not in string.punctuation:
      y.append(i)

  text=y[:]
  y.clear()
  for i in text:
    y.append(ps.stem(i))
  return " ".join(y)

tfidf=pickle.load(open('vectorizer3.pkl','rb'))
model2=pickle.load(open('model3.pkl','rb'))
st.title("Sentiment Analysis")

input_tweet = st.text_input("Enter the tweet")
        # Display the probability score for each sentiment
def probability():
    probs = model2.predict_proba(vector_input)
    st.write(f"Probability for negative sentiment: {probs[0][0]:.2f}")
    st.write(f"Probability for neutral sentiment: {probs[0][1]:.2f}")
    st.write(f"Probability for positive sentiment: {probs[0][2]:.2f}")
  #button
if st.button('Predict'):
    # Preprocess the input tweet
    transform_tweet = transform_text(input_tweet)

    # Vectorize the preprocessed tweet
    vector_input = tfidf.transform([transform_tweet])

    # Make the prediction
    prediction = model2.predict(vector_input)[0]

    # Display the results
    if prediction == 0:
        st.write('The sentiment is: negative')
        probability()
    elif prediction == 2:
        st.write('The sentiment is: positive')
        probability()
    else:
        st.write('The sentiment is: neutral')
        probability()


