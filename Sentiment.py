from textblob import TextBlob
print("This is a text message")
blob = TextBlob("I love this phone,it works great!")
print("Polarity :", blob.sentiment.polarity)

"""Output :
This is a text message
Polarity : 0.75"""
        
# Sample review data
def get_sentiment(polarity):
    if polarity >0.1:
        return "Positive"
    elif polarity<-0.1:
        return  "Negative"
    else:
        return  "Neutral"
reviews = [
    "The phone is amazing and the camera quality is amazing", 
    "Battery life is terrible and it drains too quickly", 
    "Design is decent, but performance is not good", 
    "Absolutely loved the interface and smooth experience!", 
    "The product is okay, nothing special!", 
    "Speaker volume is poor, but the display is great"
]



    
print("Sentiment analysis report :")
    
for review in reviews :
        blob = TextBlob(review)
        polarity = blob.sentiment.polarity
        sentiment = get_sentiment(polarity)
        
        print(f"review\"{review}\"")
        print(f"Polarity score :{polarity}")
        print(f"sentiment : {sentiment}")
        
"""Output : 
        entiment analysis report :
review"The phone is amazing and the camera quality is amazing"
Polarity score :0.6000000000000001
sentiment : Positive
review"Battery life is terrible and it drains too quickly"
Polarity score :-0.33333333333333337
sentiment : Negative
review"Design is decent, but performance is not good"
Polarity score :-0.09166666666666666
sentiment : Neutral
review"Absolutely loved the interface and smooth experience!"
Polarity score :0.6
sentiment : Positive
review"The product is okay, nothing special!"
Polarity score :0.4732142857142857
sentiment : Positive
review"Speaker volume is poor, but the display is great"
Polarity score :0.2
sentiment : Positive"""
        
        
      