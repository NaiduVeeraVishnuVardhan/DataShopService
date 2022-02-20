# import json
import pandas
import numpy
# import boto3
# import os

import pickle

def run(jobID, dataInput):
  """
  title:: 
      run
  description:: 
      Run the model/get the predictions according the service.
  inputs::
      jobID 
            Job ID from datashop application
      dataInput
           input Payload For the Service
  returns::
      insightsDataFileLocation
           insights data file location. 
  """
  model = pickle.load(open('BreastCancerPicklemodel.pkl', 'rb'))
  scaler = pickle.load(open('scaler.pkl', 'rb'))
  features = [float(x) for x in dataInput.split(",")]
  final_features = [numpy.array(features)]
  final_features = scaler.transform(final_features)
  print(final_features)
  prediction = model.predict(final_features)
  output = round(prediction[0], 2)
  print(type(prediction))
  # creating insightFile in the lambda temporary folder
  df = pandas.DataFrame(columns=["Preds","Value"])
  df.loc[0] = ["Prediction",output]
  print(df)
  insightsDataFileLocation = f"tmp/{jobID}-insights.csv"
  df.to_csv(insightsDataFileLocation)
  return insightsDataFileLocation
