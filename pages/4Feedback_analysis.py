import streamlit as st
from textblob import TextBlob

def analyze_sentiment(text):
    """Analyzes the sentiment of the provided text using TextBlob.

    Args:
        text (str): The text to be analyzed.

    Returns:
        str: The sentiment label (positive, neutral, or negative).
    """
    testimonial = TextBlob(text)
    polarity = testimonial.sentiment.polarity
    if polarity > 0:
        return 'Positive'
    elif polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'

st.title("Feedback Analysis")

# Feedback section
feedback_text = st.text_area("Enter your comment or feedback:", height=150)
submit_button = st.button("Submit Feedback")

if submit_button:
    if feedback_text:
        sentiment = analyze_sentiment(feedback_text)
        # st.write(f"Feedback Type: {sentiment}")

        # Optionally, store or process the feedback based on sentiment
        if sentiment == "Positive":
            st.success(f"Feedback Type: {sentiment}")
            st.success("Thank you for your positive feedback!")
        elif sentiment == "Neutral":
            st.warning(f"Feedback Type: {sentiment}")
            st.warning("We apologize for any inconvenience. Suggest some recommendations")
        elif sentiment == "Negative":
            st.error(f"Feedback Type: {sentiment}")
            st.error("We apologize for any inconvenience. Please let us know how we can improve.")
        else:
            st.info("Thank you for your feedback!")
    else:
        st.warning("Please enter some feedback before submitting.")