import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer

tw_df = pd.read_csv("D:/projects/twttr/Tweets/Tweets.csv")


tw_df = tw_df.rename(columns={'airline_sentiment': 'Sentiment', 
    'airline_sentiment_confidence': 'confidence'})

tw_df['Sentiment'].replace({'positive':'0','negative':'1'})

tw_df=tw_df[tw_df['Sentiment']!='neutral']


import re
def cleaning_text(sample):
    """Remove URLs from a sample string"""
    sample=re.sub(r"http\S+", "", sample)
    sample=re.sub(r'@\w+ ?', '',sample )
    sample=re.sub(r'# \w+ ?', '',sample )
    sample= re.sub(r'\[[0-9]*\]','',sample)
    return sample

tw_df['text']=tw_df['text'].apply(cleaning_text)