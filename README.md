# DataShopService

This repo is an example for Breast cancer prediction service. 

**In order to use this template:**
-Clone the repo.
-Remove BreastCancerPicklemodel.pkl
-Remove scalar.pkl
-Change Preprocess and Postprocess functions according to your model/service.


This template consists of three stages:

**1. Preprocess**

- download the file from url return the file location (or) save the json input in to variable and return the variable.
 
**2. Model**

- Build/run the model and save the results and return the results file path. 

**3. Postprocess**

- upload the results file to s3 and, update the results link in the datashop server. 

**Building a docker**

Include necessary packages for your model in requirements.txt. We prefer you to use pip freeze > requirements.txt 


**docker build** dockerimagename:tagname .

**RUN Command for DOCKER**

docker run -d -e BACKEND_URL=ADDRESSOFDATASHOP -p 5000:5000 dockerimagename:tagname
