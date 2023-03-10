# Importing necessary libraries
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Defining the labels for the pie chart
labels = 'Postive', 'Negative', 'Neutral'

# Setting the title of the Streamlit app
st.title("Personality Identifier")

# Asking the user to enter a name
name=st.text_input("Enter the name")

# Formatting the name for API call
name=name.split()
name="%20".join(name)
name="&q="+name

# Setting the API endpoint and parameters
url="https://newsdata.io/api/1/news?apikey=pub_14912d9a2a9ade17902f701bc34c4cab428e1&language=en"
url=url+name

# Making the API call and converting the response to a Pandas DataFrame
response=requests.get(url)
df=pd.DataFrame(response.json()['results'])

# Checking if there are any news articles returned for the given name
if(df.shape[0]==0):
    st.write("No news were found with the given name")

else:
    # Filtering the DataFrame to only include title and description columns
    df=df[['title','description']]

    # Initializing the Vader sentiment analyzer
    analyzer=SentimentIntensityAnalyzer()

    # Initializing lists to hold sentiment scores for each news article
    negative=[]
    positive=[]
    neutral=[]

    # Looping through each news article and calculating sentiment scores
    cnt=0
    df.dropna(inplace=True)
    if(df.shape[0]==0):
        st.write("No news were found with the given name")
    else:
        for i in range(df.shape[0]):
            title=df.iloc[i,0]
            description=df.iloc[i,1]
            title_analyzed=analyzer.polarity_scores(title)
            description_analyzed=analyzer.polarity_scores(description)
            negative.append((title_analyzed['neg']+description_analyzed['neg'])/2)
            positive.append((description_analyzed['pos']+title_analyzed['pos'])/2)
            neutral.append((description_analyzed['neu']+title_analyzed['neu'])/2)
            cnt+=2

        # Calculating the percentage of negative, positive and neutral sentiment scores
        negative_per=sum(negative)*10
        positive_per=sum(positive)*10
        neutral_per=sum(neutral)*10
        rem=100-(negative_per+positive_per+negative_per)

        # Displaying the sentiment analysis results
        st.write("The person is {}% negative".format(negative_per))
        st.write("The person is {}% positive".format(positive_per))
        st.write("The person is {}% neutral".format(neutral_per))
        st.write("The remaining percentage is in compounded news")

        # Creating the pie chart to display the sentiment analysis results visually
        sizes=[]
        sizes.append(negative_per)
        sizes.append(positive_per)
        sizes.append(neutral_per)
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
        ax1.axis('equal')
        st.pyplot(fig1)
