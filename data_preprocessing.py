import joblib
import numpy as np
import pandas as pd


# Load additional encoders and scalers
# encoder_Admission_Grade_Bins = joblib.load("model/encoder_Admission_Grade_Bins.joblib")
encoder_Application_mode = joblib.load("model/encoder_Application_mode.joblib")
# encoder_Application_order = joblib.load("model/encoder_Application_order.joblib")
encoder_Course = joblib.load("model/encoder_Course.joblib")
encoder_Daytime_evening_attendance = joblib.load("model/encoder_Daytime_evening_attendance.joblib")
encoder_Debtor = joblib.load("model/encoder_Debtor.joblib")
encoder_Displaced = joblib.load("model/encoder_Displaced.joblib")
encoder_Educational_special_needs = joblib.load("model/encoder_Educational_special_needs.joblib")
encoder_Fathers_occupation = joblib.load("model/encoder_Fathers_occupation.joblib")
encoder_Fathers_qualification = joblib.load("model/encoder_Fathers_qualification.joblib")
encoder_Gender = joblib.load("model/encoder_Gender.joblib")
encoder_International = joblib.load("model/encoder_International.joblib")
encoder_Marital_status = joblib.load("model/encoder_Marital_status.joblib")
encoder_Mothers_occupation = joblib.load("model/encoder_Mothers_occupation.joblib")
encoder_Mothers_qualification = joblib.load("model/encoder_Mothers_qualification.joblib")
encoder_Previous_qualification = joblib.load("model/encoder_Previous_qualification.joblib")
encoder_Scholarship_holder = joblib.load("model/encoder_Scholarship_holder.joblib")
# encoder_Status = joblib.load("model/encoder_Status.joblib")
encoder_Tuition_fees_up_to_date = joblib.load("model/encoder_Tuition_fees_up_to_date.joblib")
encoder_target = joblib.load("model/encoder_target.joblib")

scaler_Admission_grade = joblib.load("model/scaler_Admission_grade.joblib")
scaler_Age_at_enrollment = joblib.load("model/scaler_Age_at_enrollment.joblib")
scaler_Application_order = joblib.load("model/scaler_Application_order.joblib")
scaler_Curricular_units_1st_sem_approved = joblib.load("model/scaler_Curricular_units_1st_sem_approved.joblib")
scaler_Curricular_units_1st_sem_credited = joblib.load("model/scaler_Curricular_units_1st_sem_credited.joblib")
scaler_Curricular_units_1st_sem_enrolled = joblib.load("model/scaler_Curricular_units_1st_sem_enrolled.joblib")
scaler_Curricular_units_1st_sem_evaluations = joblib.load("model/scaler_Curricular_units_1st_sem_evaluations.joblib")
# scaler_Curricular_units_1st_sem_grade = joblib.load("model/scaler_Curricular_units_1st_sem_grade.joblib")
# scaler_Curricular_units_2nd_sem_grade = joblib.load("model/scaler_Curricular_units_2nd_sem_grade.joblib")
# scaler_GDP = joblib.load("model/scaler_GDP.joblib")
# scaler_Inflation_rate = joblib.load("model/scaler_Inflation_rate.joblib")
# scaler_Previous_qualification_grade = joblib.load("model/scaler_Previous_qualification_grade.joblib")
# scaler_Unemployment_rate = joblib.load("model/scaler_Unemployment_rate.joblib")

# Define additional preprocessing steps
def additional_preprocessing(data):
    print(data)
    data = data.copy()
    # df = pd.DataFrame()
    df = data.copy()

    df["Admission_grade"] = scaler_Admission_grade.transform(np.asarray(data["Admission_grade"]).reshape(-1, 1))[0]
    df["Age_at_enrollment"] = scaler_Age_at_enrollment.transform(np.asarray(data["Age_at_enrollment"]).reshape(-1, 1))[0]
    df["Application_order"] = scaler_Application_order.transform(np.asarray(data["Application_order"]).reshape(-1, 1))[0]
    df["Curricular_units_1st_sem_approved"] = scaler_Curricular_units_1st_sem_approved.transform(np.asarray(data["Curricular_units_1st_sem_approved"]).reshape(-1, 1))[0]
    df["Curricular_units_1st_sem_credited"] = scaler_Curricular_units_1st_sem_credited.transform(np.asarray(data["Curricular_units_1st_sem_credited"]).reshape(-1, 1))[0]
    df["Curricular_units_1st_sem_enrolled"] = scaler_Curricular_units_1st_sem_enrolled.transform(np.asarray(data["Curricular_units_1st_sem_enrolled"]).reshape(-1, 1))[0]
    df["Curricular_units_1st_sem_evaluations"] = scaler_Curricular_units_1st_sem_evaluations.transform(np.asarray(data["Curricular_units_1st_sem_evaluations"]).reshape(-1, 1))[0]
    # df["Curricular_units_1st_sem_grade"] = scaler_Curricular_units_1st_sem_grade.transform(np.asarray(data["Curricular_units_1st_sem_grade"]).reshape(-1, 1))[0]
    # df["Curricular_units_2nd_sem_grade"] = scaler_Curricular_units_2nd_sem_grade.transform(np.asarray(data["Curricular_units_2nd_sem_grade"]).reshape(-1, 1))[0]
    # df["GDP"] = scaler_GDP.transform(np.asarray(data["GDP"]).reshape(-1, 1))[0]
    # df["Inflation_rate"] = scaler_Inflation_rate.transform(np.asarray(data["Inflation_rate"]).reshape(-1, 1))[0]
    # df["Previous_qualification_grade"] = scaler_Previous_qualification_grade.transform(np.asarray(data["Previous_qualification_grade"]).reshape(-1, 1))[0]
    # df["Unemployment_rate"] = scaler_Unemployment_rate.transform(np.asarray(data["Unemployment_rate"]).reshape(-1, 1))[0]
    # # encoder_Admission_Grade_Bins for that
    # df["Admission_Grade_Bins"] = encoder_Admission_Grade_Bins.transform(np.asarray(data["Admission_Grade_Bins"]).reshape(-1, 1))[0]


    # df["Application_mode"] = encoder_Application_mode.transform(data["Application_mode"].values)
    # df["Application_order"] = encoder_Application_order.transform(data["Application_order"].values)
    # df["Course"] = encoder_Course.transform(data["Course"].values)
    # df["Daytime_evening_attendance"] = encoder_Daytime_evening_attendance.transform(data["Daytime_evening_attendance"].values)
    # df["Debtor"] = encoder_Debtor.transform(data["Debtor"].values)
    # df["Displaced"] = encoder_Displaced.transform(data["Displaced"].values)
    # df["Educational_special_needs"] = encoder_Educational_special_needs.transform(data["Educational_special_needs"].values)
    # df["Fathers_occupation"] = encoder_Fathers_occupation.transform(data["Fathers_occupation"].values)
    # df["Fathers_qualification"] = encoder_Fathers_qualification.transform(data["Fathers_qualification"].values)
    # df["Gender"] = encoder_Gender.transform(data["Gender"].values)
    # df["International"] = encoder_International.transform(data["International"].values)
    # df["Marital_status"] = encoder_Marital_status.transform(data["Marital_status"].values)
    # df["Mothers_occupation"] = encoder_Mothers_occupation.transform(data["Mothers_occupation"].values)
    # df["Mothers_qualification"] = encoder_Mothers_qualification.transform(data["Mothers_qualification"].values)
    # df["Previous_qualification"] = encoder_Previous_qualification.transform(data["Previous_qualification"].values)
    # df["Scholarship_holder"] = encoder_Scholarship_holder.transform(data["Scholarship_holder"].values)
    # # df["Status"] = encoder_Status.transform(data["Status"].values)
    # df["Tuition_fees_up_to_date"] = encoder_Tuition_fees_up_to_date.transform(data["Tuition_fees_up_to_date"].values)

    return df
