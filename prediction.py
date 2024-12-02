
import joblib
import pandas as pd
from data_preprocessing import additional_preprocessing


model = joblib.load("model/Random Forest_best_model.joblib")
result_target = joblib.load("model/encoder_target.joblib")

def prediction(data):
    """Making prediction
 
    Args:
        data (Pandas DataFrame): Dataframe that contain all the preprocessed data
 
    Returns:
        str: Prediction result (Dropout, Enrolled, or Graduated)
    """
    result = model.predict(data)
    return result

# data = pd.read_csv("student_performance.csv", sep=';')
# #drop Status column
# data = data.drop(columns="Status")

# results = []
# for _ in range(10):
#     sampled_data = additional_preprocessing(data.sample(1))
#     prediction_result = prediction(sampled_data)
#     results.append(prediction_result)

# print(results)
# sampled_data.to_csv("processed_student_performance.csv", index=False)
