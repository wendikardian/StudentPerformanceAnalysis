import streamlit as st
import pandas as pd
from data_preprocessing import additional_preprocessing
from prediction import prediction

# Dictionaries for mapping numerical values to descriptions
marital_status_dict = {1: 'Single', 2: 'Married', 3: 'Widower', 4: 'Divorced', 5: 'Facto union', 6: 'Legally separated'}
application_mode_dict = {1: '1st phase - general contingent', 2: 'Ordinance No. 612/93', 5: '1st phase - special contingent (Azores Island)', 7: 'Holders of other higher courses', 10: 'Ordinance No. 854-B/99', 15: 'International student (bachelor)', 16: '1st phase - special contingent (Madeira Island)', 17: '2nd phase - general contingent', 18: '3rd phase - general contingent', 26: 'Ordinance No. 533-A/99, item b2) (Different Plan)', 27: 'Ordinance No. 533-A/99, item b3 (Other Institution)', 39: 'Over 23 years old', 42: 'Transfer', 43: 'Change of course', 44: 'Technological specialization diploma holders', 51: 'Change of institution/course', 53: 'Short cycle diploma holders', 57: 'Change of institution/course (International)'}
course_dict = {33: 'Biofuel Production Technologies', 171: 'Animation and Multimedia Design', 8014: 'Social Service (evening attendance)', 9003: 'Agronomy', 9070: 'Communication Design', 9085: 'Veterinary Nursing', 9119: 'Informatics Engineering', 9130: 'Equinculture', 9147: 'Management', 9238: 'Social Service', 9254: 'Tourism', 9500: 'Nursing', 9556: 'Oral Hygiene', 9670: 'Advertising and Marketing Management', 9773: 'Journalism and Communication', 9853: 'Basic Education', 9991: 'Management (evening attendance)'}
daytime_evening_attendance_dict = {1: 'Daytime', 0: 'Evening'}
previous_qualification_dict = {1: 'Secondary education', 2: 'Higher education - bachelor\'s degree', 3: 'Higher education - degree', 4: 'Higher education - master\'s', 5: 'Higher education - doctorate', 6: 'Frequency of higher education', 9: '12th year of schooling - not completed', 10: '11th year of schooling - not completed', 12: 'Other - 11th year of schooling', 14: '10th year of schooling', 15: '10th year of schooling - not completed', 19: 'Basic education 3rd cycle (9th/10th/11th year) or equiv.', 38: 'Basic education 2nd cycle (6th/7th/8th year) or equiv.', 39: 'Technological specialization course', 40: 'Higher education - degree (1st cycle)', 42: 'Professional higher technical course', 43: 'Higher education - master (2nd cycle)'}
nationality_dict = {1: 'Portuguese', 2: 'German', 6: 'Spanish', 11: 'Italian', 13: 'Dutch', 14: 'English', 17: 'Lithuanian', 21: 'Angolan', 22: 'Cape Verdean', 24: 'Guinean', 25: 'Mozambican', 26: 'Santomean', 32: 'Turkish', 41: 'Brazilian', 62: 'Romanian', 100: 'Moldova (Republic of)', 101: 'Mexican', 103: 'Ukrainian', 105: 'Russian', 108: 'Cuban', 109: 'Colombian'}
qualification_dict = {1: 'Secondary Education - 12th Year of Schooling or Eq.', 2: 'Higher Education - Bachelor\'s Degree', 3: 'Higher Education - Degree', 4: 'Higher Education - Master\'s', 5: 'Higher Education - Doctorate', 6: 'Frequency of Higher Education', 9: '12th Year of Schooling - Not Completed', 10: '11th Year of Schooling - Not Completed', 11: '7th Year (Old)', 12: 'Other - 11th Year of Schooling', 14: '10th Year of Schooling', 18: 'General commerce course', 19: 'Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.', 22: 'Technical-professional course', 26: '7th year of schooling', 27: '2nd cycle of the general high school course', 29: '9th Year of Schooling - Not Completed', 30: '8th year of schooling', 34: 'Unknown', 35: 'Can\'t read or write', 36: 'Can read without having a 4th year of schooling', 37: 'Basic education 1st cycle (4th/5th year) or equiv.', 38: 'Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.', 39: 'Technological specialization course', 40: 'Higher education - degree (1st cycle)', 41: 'Specialized higher studies course', 42: 'Professional higher technical course', 43: 'Higher Education - Master (2nd cycle)', 44: 'Higher Education - Doctorate (3rd cycle)'}
occupation_dict = {0: 'Student', 1: 'Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers', 2: 'Specialists in Intellectual and Scientific Activities', 3: 'Intermediate Level Technicians and Professions', 4: 'Administrative staff', 5: 'Personal Services, Security and Safety Workers and Sellers', 6: 'Farmers and Skilled Workers in Agriculture, Fisheries and Forestry', 7: 'Skilled Workers in Industry, Construction and Craftsmen', 8: 'Installation and Machine Operators and Assembly Workers', 9: 'Unskilled Workers', 10: 'Armed Forces Professions', 90: 'Other Situation', 99: '(blank)', 122: 'Health professionals', 123: 'Teachers', 125: 'Specialists in information and communication technologies (ICT)', 131: 'Intermediate level science and engineering technicians and professions', 132: 'Technicians and professionals, of intermediate level of health', 134: 'Intermediate level technicians from legal, social, sports, cultural and similar services', 141: 'Office workers, secretaries in general and data processing operators', 143: 'Data, accounting, statistical, financial services and registry-related operators', 144: 'Other administrative support staff', 151: 'Personal service workers', 152: 'Sellers', 153: 'Personal care workers and the like', 171: 'Skilled construction workers and the like, except electricians', 173: 'Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like', 175: 'Workers in food processing, woodworking, clothing and other industries and crafts', 191: 'Cleaning workers', 192: 'Unskilled workers in agriculture, animal production, fisheries and forestry', 193: 'Unskilled workers in extractive industry, construction, manufacturing and transport', 194: 'Meal preparation assistants'}

col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://resources.finalsite.net/images/f_auto,q_auto,t_image_size_2/v1571764997/wflbocesorg/gwjzpw8mvmkyhypyyzj8/schooltool-logo-10-22-19.png", width=130)
with col2:
    st.header('Student Performance Analysis App (Prototype)')

data = pd.DataFrame()
col1, col2, col3 = st.columns(3)
with col1:
    Marital_status = st.selectbox(label='Marital status', options=list(marital_status_dict.values()), index=0)
    data["Marital_status"] = [list(marital_status_dict.keys())[list(marital_status_dict.values()).index(Marital_status)]]

with col2:
    Application_mode = st.selectbox(label='Application mode', options=list(application_mode_dict.values()), index=0)
    data["Application_mode"] = [list(application_mode_dict.keys())[list(application_mode_dict.values()).index(Application_mode)]]

with col3:
    Application_order = int(st.number_input(label='Application order', value=0))
    data["Application_order"] = [Application_order]

col1, col2, col3 = st.columns(3)

with col1:
    Course = st.selectbox(label='Course', options=list(course_dict.values()), index=0)
    data["Course"] = [list(course_dict.keys())[list(course_dict.values()).index(Course)]]

with col2:
    Daytime_evening_attendance = st.selectbox(label='Daytime/evening attendance', options=list(daytime_evening_attendance_dict.values()), index=0)
    data["Daytime_evening_attendance"] = [list(daytime_evening_attendance_dict.keys())[list(daytime_evening_attendance_dict.values()).index(Daytime_evening_attendance)]]

with col3:
    Previous_qualification = st.selectbox(label='Previous qualification', options=list(previous_qualification_dict.values()), index=0)
    data["Previous_qualification"] = [list(previous_qualification_dict.keys())[list(previous_qualification_dict.values()).index(Previous_qualification)]]

col1, col2, col3 = st.columns(3)

with col1:
    Previous_qualification_grade = float(st.number_input(label='Previous qualification (grade)', value=0.0))
    data["Previous_qualification_grade"] = [Previous_qualification_grade]

with col2:
    Nationality = st.selectbox(label='Nationality', options=list(nationality_dict.values()), index=0)
    data["Nacionality"] = [list(nationality_dict.keys())[list(nationality_dict.values()).index(Nationality)]]

with col3:
    Mothers_qualification = st.selectbox(label="Mother's qualification", options=list(qualification_dict.values()), index=0)
    data["Mothers_qualification"] = [list(qualification_dict.keys())[list(qualification_dict.values()).index(Mothers_qualification)]]

col1, col2, col3 = st.columns(3)

with col1:
    Fathers_qualification = st.selectbox(label="Father's qualification", options=list(qualification_dict.values()), index=0)
    data["Fathers_qualification"] = [list(qualification_dict.keys())[list(qualification_dict.values()).index(Fathers_qualification)]]

with col2:
    Mothers_occupation = st.selectbox(label="Mother's occupation", options=list(occupation_dict.values()), index=0)
    data["Mothers_occupation"] = [list(occupation_dict.keys())[list(occupation_dict.values()).index(Mothers_occupation)]]

with col3:
    Fathers_occupation = st.selectbox(label="Father's occupation", options=list(occupation_dict.values()), index=0)
    data["Fathers_occupation"] = [list(occupation_dict.keys())[list(occupation_dict.values()).index(Fathers_occupation)]]

col1, col2, col3 = st.columns(3)

with col1:
    Admission_grade = float(st.number_input(label='Admission grade', value=0.0))
    data["Admission_grade"] = [Admission_grade]

with col2:
    Displaced = st.selectbox(label='Displaced', options=['Yes', 'No'], index=0)
    data["Displaced"] = [1 if Displaced == 'Yes' else 0]

with col3:
    Educational_special_needs = st.selectbox(label='Educational special needs', options=['Yes', 'No'], index=0)
    data["Educational_special_needs"] = [1 if Educational_special_needs == 'Yes' else 0]

col1, col2, col3 = st.columns(3)

with col1:
    Debtor = st.selectbox(label='Debtor', options=['Yes', 'No'], index=0)
    data["Debtor"] = [1 if Debtor == 'Yes' else 0]

with col2:
    Tuition_fees_up_to_date = st.selectbox(label='Tuition fees up to date', options=['Yes', 'No'], index=0)
    data["Tuition_fees_up_to_date"] = [1 if Tuition_fees_up_to_date == 'Yes' else 0]

with col3:
    Gender = st.selectbox(label='Gender', options=['Male', 'Female'], index=0)
    data["Gender"] = [1 if Gender == 'Male' else 0]

col1, col2, col3 = st.columns(3)

with col1:
    Scholarship_holder = st.selectbox(label='Scholarship holder', options=['Yes', 'No'], index=0)
    data["Scholarship_holder"] = [1 if Scholarship_holder == 'Yes' else 0]

with col2:
    Age_at_enrollment = int(st.number_input(label='Age at enrollment', value=18))
    data["Age_at_enrollment"] = [Age_at_enrollment]

with col3:
    International = st.selectbox(label='International', options=['Yes', 'No'], index=0)
    data["International"] = [1 if International == 'Yes' else 0]

col1, col2, col3 = st.columns(3)

with col1:
    Curricular_units_1st_sem_credited = int(st.number_input(label='Curricular units 1st sem (credited)', value=0))
    data["Curricular_units_1st_sem_credited"] = [Curricular_units_1st_sem_credited]

with col2:
    Curricular_units_1st_sem_enrolled = int(st.number_input(label='Curricular units 1st sem (enrolled)', value=0))
    data["Curricular_units_1st_sem_enrolled"] = [Curricular_units_1st_sem_enrolled]

with col3:
    Curricular_units_1st_sem_evaluations = int(st.number_input(label='Curricular units 1st sem (evaluations)', value=0))
    data["Curricular_units_1st_sem_evaluations"] = [Curricular_units_1st_sem_evaluations]

col1, col2, col3 = st.columns(3)

with col1:
    Curricular_units_1st_sem_approved = int(st.number_input(label='Curricular units 1st sem (approved)', value=0))
    data["Curricular_units_1st_sem_approved"] = [Curricular_units_1st_sem_approved]

with col2:
    Curricular_units_1st_sem_grade = float(st.number_input(label='Curricular units 1st sem (grade)', value=0.0))
    data["Curricular_units_1st_sem_grade"] = [Curricular_units_1st_sem_grade]

with col3:
    Curricular_units_1st_sem_without_evaluations = int(st.number_input(label='Curricular units 1st sem (without evaluations)', value=0))
    data["Curricular_units_1st_sem_without_evaluations"] = [Curricular_units_1st_sem_without_evaluations]

col1, col2, col3 = st.columns(3)

with col1:
    Curricular_units_2nd_sem_credited = int(st.number_input(label='Curricular units 2nd sem (credited)', value=0))
    data["Curricular_units_2nd_sem_credited"] = [Curricular_units_2nd_sem_credited]

with col2:
    Curricular_units_2nd_sem_enrolled = int(st.number_input(label='Curricular units 2nd sem (enrolled)', value=0))
    data["Curricular_units_2nd_sem_enrolled"] = [Curricular_units_2nd_sem_enrolled]

with col3:
    Curricular_units_2nd_sem_evaluations = int(st.number_input(label='Curricular units 2nd sem (evaluations)', value=0))
    data["Curricular_units_2nd_sem_evaluations"] = [Curricular_units_2nd_sem_evaluations]

col1, col2, col3 = st.columns(3)

with col1:
    Curricular_units_2nd_sem_approved = int(st.number_input(label='Curricular units 2nd sem (approved)', value=0))
    data["Curricular_units_2nd_sem_approved"] = [Curricular_units_2nd_sem_approved]

with col2:
    Curricular_units_2nd_sem_grade = float(st.number_input(label='Curricular units 2nd sem (grade)', value=0.0))
    data["Curricular_units_2nd_sem_grade"] = [Curricular_units_2nd_sem_grade]

with col3:
    Curricular_units_2nd_sem_without_evaluations = int(st.number_input(label='Curricular units 2nd sem (without evaluations)', value=0))
    data["Curricular_units_2nd_sem_without_evaluations"] = [Curricular_units_2nd_sem_without_evaluations]

col1, col2, col3 = st.columns(3)

with col1:
    Unemployment_rate = float(st.number_input(label='Unemployment rate', value=0.0))
    data["Unemployment_rate"] = [Unemployment_rate]

with col2:
    Inflation_rate = float(st.number_input(label='Inflation rate', value=0.0))
    data["Inflation_rate"] = [Inflation_rate]

with col3:
    GDP = float(st.number_input(label='GDP', value=0.0))
    data["GDP"] = [GDP]

with st.expander("View the Raw Data"):
    st.dataframe(data=data, width=800, height=10)

if st.button('Predict'):
    new_data = additional_preprocessing(data=data)
    # export new_data
    new_data.to_csv("model_result.csv", index=False)
    with st.expander("View the Preprocessed Data"):
        st.dataframe(data=new_data, width=800, height=10)
    st.write("Student Performance Prediction: {}".format(prediction(new_data)))
