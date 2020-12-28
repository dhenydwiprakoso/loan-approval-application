import json
import joblib
import numpy as np
import os

__data_columns = None
__model = None

gender_dict = {'Male':0, 'Female':1}
yes_no_dict = {'No':0, 'Yes':1}
education_dict = {'Not Graduate':0, 'Graduate':1}
area_dict = {'Rural':0, 'Semiurban':1, 'Urban':2}
credits_dict = {'Not Paid':0, 'Has All Debts Paid':1}
approval = {0:'Rejected', 1:'Approved'}
def dependents_func (data):
    try:
        float(data)
    except:
        return 3
    return float(data)

def get_approval(gender, married, dependents, education, self_employed, applicantincome, coapplicantincome,loanamount, loan_amount_term, credit_history, property_area):
    x = np.zeros(len(__data_columns))
    x[0] = gender_dict[gender]
    x[1] = yes_no_dict[married]
    x[2] = dependents_func(dependents)
    x[3] = education_dict[education]
    x[4] = yes_no_dict[self_employed]
    x[5] = applicantincome
    x[6] = coapplicantincome
    x[7] = loanamount
    x[8] = loan_amount_term
    x[9] = credits_dict[credit_history]
    x[10] = area_dict[property_area]

    return approval[int(__model.predict([x]))]

def load_saved_artifacts():
    print("loading saved artifacts...start")
    
    global __data_columns
    with open("./artifacts/columns.json", 'r') as f:
        __data_columns= json.load(f)['data_columns']
    
    global __model
    if __model is None:
        with open("./artifacts/loan_no loan_rf_model.pkl", 'rb') as f:
            __model = joblib.load(f)

    print ('loading model artifacts...done')

def get_data_columns():
    return __data_columns

load_saved_artifacts()

