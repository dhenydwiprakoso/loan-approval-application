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

def applicant_income_func(data):
    if data < 81000//5:
        return 0
    elif data >= 81000//5 and data < 2*81000//5:
        return 1
    elif data >= 2*81000//5 and data < 3*81000//5:
        return 2
    elif data >= 3*81000//5 and data < 4*81000//5:
        return 3
    elif data >= 4*81000//5:
        return 4
def coapplicant_income_func(data):
    if data < 2000:
        return 0
    elif data >= 2000 and data < 4000:
        return 1
    elif data >= 4000 and data < 6000:
        return 2
    elif data >= 6000 and data < 8000:
        return 3
    elif data >= 8000:
        return 4

def loan_amount_func(data):
    if data < 700//5:
        return 0
    elif data >= 700//5 and data < 2*700//5:
        return 1
    elif data >= 2*700//5 and data < 3*700//5:
        return 2
    elif data >= 3*700//5 and data < 4*700//5:
        return 3
    elif data >= 4*700//5:
        return 4

def loan_amount_term_func(data):
    if data < 480//5:
        return 0
    elif data >= 480//5 and data < 2*480//5:
        return 1
    elif data >= 2*480//5 and data < 3*480//5:
        return 2
    elif data >= 3*480//5 and data < 4*480//5:
        return 3
    elif data >= 4*480//5:
        return 4

def get_approval(gender, married, dependents, education, self_employed, applicantincome, coapplicantincome,loanamount, loan_amount_term, credit_history, property_area):
    x = np.zeros(len(__data_columns))
    x[0] = gender_dict[gender]
    x[1] = yes_no_dict[married]
    x[2] = dependents_func(dependents)
    x[3] = education_dict[education]
    x[4] = yes_no_dict[self_employed]
    x[5] = applicant_income_func(applicantincome)
    x[6] = coapplicant_income_func(coapplicantincome)
    x[7] = loan_amount_func(loanamount)
    x[8] = loan_amount_term_func(loan_amount_term)
    x[9] = credits_dict[credit_history]
    x[10] = area_dict[property_area]

    return approval[int(__model.predict([x]))]

def load_saved_artifacts():
    print("loading saved artifacts...start")
    
    path = os.path.dirname(__file__) 
    artifacts = os.path.join(path, "artifacts"),

    global __data_columns
    with open(artifacts[0]+"/columns.json", "r") as f:
        __data_columns= json.load(f)['data_columns']
    
    global __model
    if __model is None:
        with open(artifacts[0]+"/loan_no loan_rf_model.pkl", 'rb') as f:
            __model = joblib.load(f)

    print ('loading model artifacts...done')

def get_data_columns():
    return __data_columns

load_saved_artifacts()

