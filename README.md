# personality_check
 A short explanation of how the code works
## Importing necessary libraries

The code begins by importing necessary libraries. SentimentIntensityAnalyzer from vaderSentiment is used to analyze the sentiment of news headlines and descriptions. streamlit is used to create the user interface for the app. requests is used to fetch news articles from an API. pandas is used to manipulate data in a tabular format. matplotlib.pyplot is used to visualize data in the form of a pie chart.

## Setting up user interface

The title of the application is set as "Personality Identifier" using st.title(). A text input field is created using st.text_input() to allow the user to enter the name of the person they want to analyze.

## Fetching news articles

The code fetches news articles related to the entered name using an API from newsdata.io. The API key is provided in the URL along with the name of the person as a query parameter. The response is then converted to a pandas dataframe for easier manipulation.

## Analyzing sentiment of news articles

The code then proceeds to analyze the sentiment of news headlines and descriptions using SentimentIntensityAnalyzer(). The compound score is used to calculate the percentage of negative, positive, and neutral sentiment for each news article.

## Visualizing the results

The results are then displayed using st.write(). A pie chart is also plotted using matplotlib.pyplot to visually represent the percentages of negative, positive, and neutral sentiment. It is then displayed in the app using st.pyplot().
