class TextBlob:
    def __init__(self, text):
        self.text = text

    def sentiment(self):
        # Basic sentiment analysis (polarity score)
        polarity_score = self.calculate_polarity()
        if polarity_score > 0:
            return "positive 😀"
        elif polarity_score < 0:
            return "negative 😞"
        else:
            return "neutral 😐"

    def calculate_polarity(self):
        # A simple method to calculate polarity score (for demonstration purposes)
        positive_words = ["good", "great", "awesome", "excellent"]
        negative_words = ["bad", "terrible", "awful", "horrible"]
        
        # Count positive and negative words
        num_positive = sum(self.text.lower().count(word) for word in positive_words)
        num_negative = sum(self.text.lower().count(word) for word in negative_words)
        
        # Calculate polarity score
        polarity_score = (num_positive - num_negative) / len(self.text.split())
        return polarity_score

    def part_of_speech_tagging(self):
        # Basic part-of-speech tagging (for demonstration purposes)
        tagged_words = []
        for word in self.text.split():
            # Assume every word is a noun for simplicity
            tagged_words.append((word, "NOUN"))
        return tagged_words

    def noun_phrase_extraction(self):
        # Basic noun phrase extraction (for demonstration purposes)
        return [phrase for phrase in self.text.split() if len(phrase) > 1]

# Example usage
text = "TextBlob is a simple and easy-to-use library for natural language processing."
blob = TextBlob(text)

print("Sentiment:", blob.sentiment())
print("Part-of-speech Tags:", blob.part_of_speech_tagging())
print("Noun Phrases:", blob.noun_phrase_extraction())
