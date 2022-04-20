import streamlit as st
import pandas as pd
import numpy as np
from Data_processing import data_cleaning, case_v_death
import sqlite3
from datetime import datetime
import altair as alt
import unittest

#data set downloaded from 'https://data.cdc.gov/Case-Surveillance/United-States-COVID-19-Cases-and-Deaths-by-State-o/9mfq-cb36'
#establish connection between .py file and SQLite database
#convert SQLite to pandas dataframe
try:
    connect = sqlite3.connect('Covid19_data_USA.db')
    print('Success')
except Failed as e:
    print('Error during connection: ',str(e))
    
covid_data = pd.read_sql_query(
    '''
    SELECT * 
    FROM Covid19_data_USA''', connect)

#Title of app
st.title('COVID-19 Tracker')
    
#code processing/cleaning with imported functions
clean = data_cleaning(covid_data)
graph = case_v_death(clean)

#test to see if the data connection is there
#and if data cleaning functions are working
class TestPipeLine(unittest.TestCase):
    
    def test_fails_without_df(self):
        with self.assertRaises(TypeError):
            data_cleaning()
            case_v_death() 
            
    def test_fails_with_three_args(self):
        with self.assertRaises(TypeError):
            data_cleaning(1,2,3)
            case_v_death(1,2,3)
            
    def test_output_type_of_both_functions(self):
        self.assertIs(type(data_cleaning(covid_data)), type(pd.DataFrame()))
        self.assertIs(type(case_v_death(clean)),type(pd.DataFrame()))
            
    def test_column_types_clean_data_set(self):
        clean_df = clean
        self.assertTrue("submission_date" in clean_df.columns)
        self.assertTrue(clean_df['submission_date'].dtype == 'datetime64[ns]')

unittest.main(TestPipeLine(), argv=['first-arg-is-ignored'], exit=False)   

#offer option to show all data
if st.checkbox('Show raw data'):
   st.subheader('Raw data')
   st.write(clean)
    
st.subheader('Nationwide New Cases & Deaths Since 2020')

st.bar_chart(graph['new_cases'])
st.bar_chart(graph['new_death'])
    
st.subheader('Covid Data By Date & State')

#create drop-down filter based on state
state = clean['state'].drop_duplicates().sort_values()
filter_state = st.selectbox('Select your state:', state)
df_filtered = clean[['submission_date','state','total_cases','total_death']]
df_filtered = df_filtered[df_filtered['state']==(filter_state)]
                  
#plot double-y-axis chart using altair in streamlit
base = alt.Chart(df_filtered).encode(
    alt.X('submission_date:T', axis=alt.Axis(title='Date')))

line1 = base.mark_line(stroke='green', interpolate='monotone').encode(
    alt.Y('total_cases',
          axis=alt.Axis(title='Total Cases', titleColor='green')))

line2 = base.mark_line(stroke='red', interpolate='monotone').encode(
    alt.Y('total_death',
          axis=alt.Axis(title='Total Death', titleColor='red')))

final = alt.layer(line1, line2).resolve_scale(y = 'independent')

st.altair_chart(final, use_container_width=True)