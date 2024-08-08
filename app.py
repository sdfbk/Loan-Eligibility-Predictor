import streamlit as st
import pickle
import sklearn
with open('Loan_Predictor.pkl','rb') as pkl:
    train_model = pickle.load(pkl)
def main():
    html_temp = """
    <div style = "background-color:white;padding:12px">
    <h1 style = "color:black;text-align:center">Loan Eligibility Predictor</h1>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    gender = st.selectbox('Gender',('Male','Female'))
    married = st.selectbox('Married',('Yes','No'))
    dependent = st.selectbox('Dependents',('None','One','Two','Three or more'))
    education = st.selectbox('Education',('Graduate','Not Graduate'))
    self_employed = st.selectbox('Self Employed',('Yes','No'))
    applicant_income = st.slider('Applicant Income in dollar',150,9703)
    coapplicant_income = st.slider('Co-Applicant Income in dollar',0,33837)
    loan_Amount = st.slider('Loan Amount in dollar',9,150)
    loan_tenure = st.slider('Loan Tenure in days',12,480)
    creditHistory = st.number_input('Credit History',0.0,1.0)
    propertyArea = st.selectbox('Property Area',('Semiurban','Urban','Rural'))
    button = st.button('Predict')
    
    def predict(gender,married,dependent,education,self_employed,applicant_income,coapplicant_income,loan_Amount,loan_tenure,creditHistory,propertyArea):
        gen = 1 if gender == 'Male' else 0
        mar = 1 if married == 'Yes' else 0
        dep = int(0 if dependent == 'None' else 1 if dependent == 'One' else 2 if dependent == 'Two' else 3)
        edu = 1 if education == 'Not Graduate' else 0
        sem = 1 if self_employed == 'Yes' else 0
        a = applicant_income
        co = coapplicant_income
        l = loan_Amount
        lt = loan_tenure
        ch = creditHistory
        pro = 0 if propertyArea == 'Rural' else 1 if propertyArea == 'Semiurban' else 2
        
        prediction = train_model.predict([[gen,mar,dep,edu,sem,a,co,l,lt,ch,pro]])
        
        verdict = 'Not Eligible' if prediction == 0 else 'Eligible'
        return verdict

    
    if button:
        result = predict(gender,married,dependent,education,self_employed,applicant_income,coapplicant_income,loan_Amount,loan_tenure,creditHistory,propertyArea)
        st.success(f'You are {result} for the loan')
    
    
if __name__ == '__main__':
    main()
    
