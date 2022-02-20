import json
import pre_process
import post_process
import model


def lambda_handler(event, context):
    """
    title:: 
        lambda_handler
    description:: 
        Gets the dataset from the user, run the models and get predictions
    inputs::
        event
             request from the Datashop application.
    returns::
             response to the Datashop application. 
    """
    #Loads the body of the event.
    input_dict = json.loads(event['body'])
    inputdata = input_dict["dataFileURL"]
    
    #running the preprocessing steps for the model. It takes dataset URL, jobID, json as input, download the dataset and read the input.
    inputPayloadForService = pre_process.run(input_dict["jobID"], inputdata["url"],inputdata["json"])
    print("DF's in lambda",inputPayloadForService)
    
    #model buliding/ getting the predictions here. It takes jobID and inputPayloadForService as input, run the model and get precitions saved in the temp folder of lambda.
    insightsDataFileLocation = model.run(input_dict["jobID"],inputPayloadForService)
    
    #It takes insightsDataFileLocation, jobID as Input, upload the insights file to s3 and get the downloadable link for the same. and also send the jobID and insights link to the Datashop application. 
    status_map = post_process.run(input_dict["jobID"],insightsDataFileLocation) 
    
    return  { "statusCode": status_map["status_code"], "body": status_map["json_response"] }


