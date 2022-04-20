# Data_Engineering

### COVID-19 Data Pipeline & Visualization

App can be found here https://share.streamlit.io/tesung/data_engineering/main/covid_tracker_streamlit.py

##### Abstract

The purpose of this project is to construct a data engineering pipeline from data acquistion, to storage, to processing, and finally - to production. I am interested in COVID-19 data so I wanted to use publicly accessible data to build a user-friendly visualization product that could display filtered information depending on user-input. 

##### Design

The project stems from a hypothetical situation where a client wants to get data surrounding new COVID-19 cases and deaths in the United States; the client is also interested to see how the disease has affected individual states since the pandemic began. I downloaded public data obtained from the [CDC](https://data.cdc.gov/Case-Surveillance/United-States-COVID-19-Cases-and-Deaths-by-State-o/9mfq-cb36), stored it in a local SQL database, processed the data with a python script, and then created a web-app using streamlit. Unit testing methods were set up to ensure the code runs smoothly, and if not, it points to the exact location where it breaks. 

##### Data

The total data set had 48,480 rows with 15 columns. Most of the columns are integers with only a few categorical columns. I targeted all the numerical columns since those are the data points I am interested in. For columns that were objects, I only used two: column with all the state names and I converted the date column from object into datetime format. There were a lot of missing data points scattered throughout different dates, states, and categories, which can be attributed to the chaos the pandemic caused. That said, all the missing data points were filled with '0' because I am not targeting averages, but instead the overall trend.

##### Algorithms

I used SQLite as my connection to the local SQL database; Pandas as my main data processing tool since not a lot of cleaning was required, therefore I opted out of using PySpark; unittest package for unit testing. The main character of this project is the user-interactive web-app. I built my app using Streamlit. 

##### Tools

SQLite
Pandas
Python Scripts
Unit testing
Streamlit
Altair
