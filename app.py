import streamlit as st
import numpy as np
import pickle as pic

st.title("Churn Prediction")
st.subheader("Enter Details")

# Model 
model = pic.load(
    open("Model_churn.pkl", "rb")
)

# Inputs
# ---------
# ['Gender',
#  'Senior Citizen',
#  'Partner',
#  'Dependents',
#  'tenure',
#  'Phone Service',
#  'Multiple Lines',
#  'Paperless Billing',
#  'Monthly Charges',
#  'Total Charges',
#  'Internet Service_DSL',
#  'Internet Service_Fiber optic',
#  'Internet Service_No',
#  'Online Security_No',
#  'Online Security_No internet service',
#  'Online Security_Yes',
#  'Online Backup_No',
#  'Online Backup_No internet service',
#  'Online Backup_Yes',
#  'Device Protection_No',
#  'Device Protection_No internet service',
#  'Device Protection_Yes',
#  'Tech Support_No',
#  'Tech Support_No internet service',
#  'Tech Support_Yes',
#  'Streaming TV_No',
#  'Streaming TV_No internet service',
#  'Streaming TV_Yes',
#  'Streaming Movies_No',
#  'Streaming Movies_No internet service',
#  'Streaming Movies_Yes',
#  'Contract_Month-to-month',
#  'Contract_One year',
#  'Contract_Two year',
#  'Payment Method_Bank transfer (automatic)',
#  'Payment Method_Credit card (automatic)',
#  'Payment Method_Electronic check',
#  'Payment Method_Mailed check']


# Gender Input Using Selection Box
gender = st.selectbox(
    "Gender",
    ["Select Gender","Male", "Female"],
    index=0
)
if gender == "Select Gender":
    st.warning("Please Select Correctly")
    gender_value = None
else:
    gender_map = {
        "Male": 1,
        "Female" : 0
    }
    gender_value = gender_map[gender]


# Senior Citizen
sc = st.selectbox(
    "Senior Citizen",
    ["Select Senior Citizen or Not","Yes", "No"],
    index=0
)
if sc == "Select Senior Citizen or Not":
    st.warning("Please Select Correctly")
    sc_value = None
else:
    sc_map = {
        "Yes" : 1,
        "No"  : 0
    }
    sc_value = sc_map[sc]


# Partner
partner = st.selectbox(
    "Married",
    ["Select Married or Not","Yes", "No"],
    index=0
)
if partner == "Select Married or Not":
    st.warning("Please Select Married or Not")
    partner_value = None
else:
    partner_map = {
        "Yes" : 1,
        "No"  : 0
    }
    partner_value = partner_map[partner]



# 'Dependents'
dependents = st.selectbox(
    "Dependents",
    ["Select Dependent or Not", "Yes", "No"],
    index=0
)
if dependents == "Select Dependent or Not":
    st.warning("Please Select Dependents")
    dependents_value = None
else:
    dependents_map = {
        "Yes" : 1,
        "No"  : 0
    }
    dependents_value = dependents_map[dependents]


#  'tenure'
tenure = st.number_input(
    "Tenure",
    min_value=0,
    max_value=100,
    value=1,
    step=1
)


#  'Phone Service'
ps = st.selectbox(
    "Phone Service",
    ["Service Available or not", "Yes", "No"],
    index=0
)
if ps == "Service Available or not":
    st.warning("Please select Phone Service")
    ps_value = None
else:
    ps_map = {
        "Yes" : 1,
        "No"  : 0
    }
    ps_value = ps_map[ps]


#  'Multiple Lines'
ml = st.selectbox(
    "Multiple Lines",
    ["Multiple Service Availability", "Yes", "No"],
    index=0
)
if ml == "Multiple Service Availability":
    st.warning("Please select Multiple Service")
    ml_value = None
else:
    ml_map = {
        "Yes" : 1,
        "No"  : 0
    }
    ml_value = ml_map[ml]


#  'Paperless Billing'
pb = st.selectbox(
    "Paperless Billing",
    ["Billing", "Yes", "No"],
    index=0
)
if pb == "Billing":
    st.warning("Please select Billing")
    pb_value = None
else:
    pb_map = {
        "Yes" : 1,
        "No"  : 0
    }
    pb_value = pb_map[pb]


#  'Monthly Charges'
mch = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    max_value=150.0,
    value=18.25,
    step=0.01
)


#  'Total Charges'
tch = st.number_input(
    "Total Charges",
    min_value=0.0,
    max_value=10000.0,
    value=18.85,
    step=0.01
)


#  'Internet Service_DSL',
#  'Internet Service_Fiber optic',
#  'Internet Service_No',

ins = st.selectbox(
    "Internet Service",
    ["Select Service", "DSL", "Fiber optic", "No"],
    index=0   
)
if ins == "Select Service":
    st.warning("Please select Internet Service")
    ins_dsl = None
    ins_fiber = None
    ins_no = None
else:
    ins_dsl = 1 if ins == "DSL" else 0
    ins_fiber = 1 if ins == "Fiber optic" else 0
    ins_no = 1 if ins == "No" else 0


#  'Online Security_No',
#  'Online Security_No internet service',
#  'Online Security_Yes',
os = st.selectbox(
    "Online Security",
    ["Security",
     "Online Security_No", 
     "Online Security_No internet service", 
     "Online Security_Yes"],
     index=0
)
if os == "Security":
    st.warning("Please Select Security")
    os_no = None
    os_nis = None
    os_yes = None
else:
    os_no = 1 if os == "Online Security_No" else 0
    os_nis = 1 if os == "Online Security_No internet service" else 0
    os_yes = 1 if os == "Online Security_Yes" else 0


#  'Online Backup_No',
#  'Online Backup_No internet service',
#  'Online Backup_Yes',
ob = st.selectbox(
    "Online Backup",
    ["Backup",
     "Online Backup_No", 
     "Online Backup_No internet service", 
     "Online Backup_Yes"],
     index=0
)
if ob == "Backup":
    st.warning("Please Select Backup")
    ob_no = None
    ob_nis = None
    ob_yes = None
else:
    ob_no = 1 if ob == "Online Backup_No" else 0 
    ob_nis = 1 if ob == "Online Backup_No internet service" else 0
    ob_yes = 1 if ob == "Online Backup_Yes" else 0


#  'Device Protection_No',
#  'Device Protection_No internet service',
#  'Device Protection_Yes',
dp = st.selectbox(
    "Device Protection",
    ["Protection", 
     "Device Protection_No", 
     "Device Protection_No internet service",
     "Device Protection_Yes"],
     index=0
)
if dp =="Protection":
    st.warning("Please Select Protection")
    dp_no = None
    dp_nis = None
    dp_yes = None
else:
    dp_no = 1 if dp == "Device Protection_No" else 0
    dp_nis = 1 if dp == "Device Protection_No internet service" else 0
    dp_yes = 1 if dp == "Device Protection_Yes" else 0


#  'Tech Support_No',
#  'Tech Support_No internet service',
#  'Tech Support_Yes',
ts = st.selectbox(
    "Tech Support",
    ["Support", 
     "Tech Support_No", 
     "Tech Support_No internet service",
     "Tech Support_Yes"],
     index=0
)
if ts =="Support":
    st.warning("Please Select Support")
    ts_no = None
    ts_nis = None
    ts_yes = None
else:
    ts_no = 1 if ts == "Tech Support_No" else 0
    ts_nis = 1 if ts == "Tech Support_No internet service" else 0
    ts_yes = 1 if ts == "Tech Support_Yes" else 0

#  'Streaming TV_No',
#  'Streaming TV_No internet service',
#  'Streaming TV_Yes',
stv = st.selectbox(
    "Television",
    ["Streaming_TV", 
     "Streaming TV_No", 
     "Streaming TV_No internet service",
     "Streaming TV_Yes"],
     index=0
)
if stv =="Streaming_TV":
    st.warning("Please Select Streaming_TV")
    stv_no = None
    stv_nis = None
    stv_yes = None
else:
    stv_no = 1 if stv == "Streaming TV_No" else 0
    stv_nis = 1 if stv == "Streaming TV_No internet service" else 0 
    stv_yes = 1 if stv == "Streaming TV_Yes" else 0


#  'Streaming Movies_No',
#  'Streaming Movies_No internet service',
#  'Streaming Movies_Yes',
stm = st.selectbox(
    "Television",
    ["Streaming_Movies", 
     "Streaming Movies_No", 
     "Streaming Movies_No internet service",
     "Streaming Movies_Yes"],
     index=0
)
if stm =="Streaming_Movies":
    st.warning("Please Select Streaming_Movies")
    stm_no = None
    stm_nis = None
    stm_yes = None
else:
    stm_no = 1 if stm == "Streaming Movies_No" else 0
    stm_nis = 1 if stm == "Streaming Movies_No internet service" else 0
    stm_yes = 1 if stm == "Streaming Movies_Yes" else 0


#  'Contract_Month-to-month',
#  'Contract_One year',
#  'Contract_Two year',
contract = st.selectbox(
        "Contract",
        ["Contract or Not", 
        "Contract_Month-to-month", 
        "Contract_One year",
        "Contract_Two year"],
        index=0
)
if contract =="Contract Details":
    st.warning("Please Select Contract")
    contract_m = None
    contract_1 = None
    contract_2 = None
else:
    contract_m = 1 if contract == "Contract_Month-to-month" else 0
    contract_1 = 1 if contract == "Contract_One year" else 0
    contract_2 = 1 if contract == "Contract_Two year" else 0


#  'Payment Method_Bank transfer (automatic)',
#  'Payment Method_Credit card (automatic)',
#  'Payment Method_Electronic check',
#  'Payment Method_Mailed check']

Payment = st.selectbox(
        "Payment Method",
        ["payment", 
        "Payment Method_Bank transfer (automatic)", 
        "Payment Method_Credit card (automatic)",
        "Payment Method_Electronic check",
        "Payment Method_Mailed check"],
        index=0
)
if Payment =="payment":
    st.warning("Please Select Payment")
    Payment_bt = None
    Payment_cc = None
    Payment_ec = None
    Payment_mc = None
else:
    Payment_bt = 1 if Payment == "Payment Method_Bank transfer (automatic)" else 0
    Payment_cc = 1 if Payment == "Payment Method_Credit card (automatic)" else 0
    Payment_ec = 1 if Payment == "Payment Method_Electronic check" else 0
    Payment_mc = 1 if Payment == "Payment Method_Mailed check" else 0


# columns = [gender,sc, partner, dependents, tenure, ps, ml, pb, mch, tch, ins, os, ob, dp, ts, stv, stm, contract, Payment]


input_data = np.array([[
    gender_value, sc_value, partner_value, dependents_value, tenure,
    ps_value, ml_value, pb_value, mch, tch, 
    ins_dsl, ins_fiber, ins_no,
    os_no, os_nis, os_yes, 
    ob_no, ob_nis, ob_yes, 
    dp_no, dp_nis, dp_yes,
    ts_no, ts_nis, ts_yes,
    stv_no, stv_nis, stv_yes,
    stm_no, stm_nis, stm_yes,
    contract_m, contract_1, contract_2,
    Payment_bt, Payment_cc, Payment_ec, Payment_mc
]])

churn_map = {
    1 : "Customer Churned ( Discontinued )",
    0 : "Customer Not Churned ( Using Service )"
}

if st.button("Predict"):
    churn_prediction = model.predict(input_data)[0]
    st.success(f"Churn: {churn_map[churn_prediction]}")



