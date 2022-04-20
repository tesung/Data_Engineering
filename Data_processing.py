import pandas as pd

def data_cleaning(info):
    df = info.fillna(0)
    df = df.astype({'confirmed_cases':int,'confirmed_death':int})
    df['submission_date'] = pd.to_datetime(df['submission_date'])
    df.sort_values(by='submission_date', ascending = False, inplace=True)
    df = df[['submission_date','state','total_cases','confirmed_cases','new_cases','total_death','confirmed_death','new_death']]
    return df 

def case_v_death(info):
    df = info[['submission_date','new_cases','new_death']]
    df = df.groupby('submission_date').sum().sort_values(by='submission_date',ascending=False)
    return df
