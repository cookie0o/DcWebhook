# Imports
import requests


class Values():
    # define webhook url
    webhook = ""

    # get the output mode
    output_mode = "1" # 1=All / 2=Only Errors / 3=Only Successes / 4=Nothing

class ResponseHandler():
    def Log(message):
        # check output mode
        if Values.output_mode == "1" or Values.output_mode == "3":
            # return error message
            ##return("[+]      "+ str(message))    
            print("[+]     "+ str(message))

    def Error(e):
        # check output mode
        if Values.output_mode == "1" or Values.output_mode == "2":
            # return error message
           ## return ("[ERROR] "+ str(e))
            print("[ERROR] "+ str(e))

    def CheckResponse(response):
        # check if response is ok
        if response.status_code == 200:
            return "no_error"
        elif response.status_code == 400:
            ResponseHandler.Error("400: Bad Request")
            return "error"
        elif response.status_code == 429:
            ResponseHandler.Error("429: Rate Limit reached.")
            return "error"

###--------------------------------------------------------------###

class DcWebhook():

    # SEND MESSAGE
    def send_message(message):
        try:
            # define payload
            payload = {
                "content": message
            }
            # send message
            x = requests.post(Values.webhook, json=payload)

            # check for errors
            if ResponseHandler.CheckResponse(x) == "error":
                pass
            else:
                ResponseHandler.Log("Message successfully sent!")
        except Exception as e:
            ResponseHandler.Error(e)

    # SEND FILE
    def send_file(file_path):
        try:
            # define payload
            payload = {
                "file": open(file_path, 'rb')
            }
            # send message
            x = requests.post(Values.webhook, files=payload)

            # check for errors
            if ResponseHandler.CheckResponse(x) == "error":
                pass
            else:
                ResponseHandler.Log("Message successfully sent!")
        except Exception as e:
            ResponseHandler.Error(e)

    # SEND EMBED
    def send_embed(title, content, thumbnail, image, color):
        # check if color is a string else return error
        if type(color) is str:
            # check output mode
            if Values.output_mode == "1" or Values.output_mode == "2":
                # return error message
                ResponseHandler.Error("color code cant be a string! Please define the raw color code!")
        try:
            # define payload
            payload = {
                "embeds": [{
                    "title": title,
                    "description": content,
                    "thumbnail": {
                        "url": thumbnail
                    },
                    "image": {
                        "url": image
                    },
                    "color": color
                }]
            }

            # send message
            x = requests.post(Values.webhook, json=payload)
            
            # check for errors
            if ResponseHandler.CheckResponse(x) == "error":
                pass
            else:
                ResponseHandler.Log("Message successfully sent!")
        except Exception as e:
            ResponseHandler.Error(e)
           
    # SEND RAW EMBED
    def send_raw_embed(raw_embed):
        try:
            # define payload
            payload = raw_embed

            # send message
            x = requests.post(Values.webhook, json=payload)
            
            # check for errors
            if ResponseHandler.CheckResponse(x) == "error":
                pass
            else:
                ResponseHandler.Log("Message successfully sent!")
        except Exception as e:
            ResponseHandler.Error(e)
