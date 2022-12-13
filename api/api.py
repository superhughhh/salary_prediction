from fastapi import FastAPI
import pandas as pd
import pickle
from possibles_values import *


def make_predict_df(job_title, company_size, company_country_location, experience_level, employee_country_residence, remote_ratio):
    predict_df = pd.DataFrame({'job_title': [job_title],
                               'company_size': [company_size],
                               'company_country_location': [company_country_location],
                               'experience_level': [experience_level],
                               'employee_country_residence': [employee_country_residence],
                               'remote_ratio': [remote_ratio]
                               })
    return predict_df


app = FastAPI()

@app.get("/")
async def root(job_title: Job_title,
               company_size: Company_size,
               company_country_location: Company_country_location,
               experience_level: Experience_level,
               employee_country_residence: Employee_country_residence,
               remote_ratio: Remote_ratio):
    
    predict_df = make_predict_df(job_title, company_size, company_country_location, experience_level, employee_country_residence, remote_ratio)
    infile = open('data_salary_prediction_model.plk', 'rb')
    my_model = pickle.load(infile)
    prediction = my_model.predict(predict_df)
    infile.close()
    return {"prediction du tips en $": int(prediction[0][0])}
