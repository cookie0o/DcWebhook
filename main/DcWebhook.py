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

    def RateLimit(message):
        # for future versions:
        print ("[RL]   "+ "Rate limit reached. Wait for " + str(message) + " seconds and retry.")

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
            requests.post(Values.webhook, json=payload)
    

            ResponseHandler.Log("Message successfully sent!")
        except Exception as e:
            ResponseHandler.Error(e)

    # SEND FILE
    def send_File(file_path):
        try:
            # define payload
            payload = {
                "file": open(file_path, 'rb')
            }
            # send message
            requests.post(Values.webhook, files=payload)

                
            ResponseHandler.Log("File successfully sent!")
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
            requests.post(Values.webhook, json=payload)


            ResponseHandler.Log("Embed successfully sent!")
        except Exception as e:
            ResponseHandler.Error(e)
           
    # SEND RAW EMBED
    def send_raw_embed(raw_embed):
        try:
            # define payload
            payload = raw_embed

            # send message
            requests.post(Values.webhook, json=payload)


            ResponseHandler.Log("Raw Embed successfully sent!")
        except Exception as e:
            ResponseHandler.Error(e)


"""
DcWebhook.send_message("Hello World!")
###
DcWebhook.send_File(r"A:\test.jpg")
###
DcWebhook.send_embed(
    "This is a Test title.", 
    "this is a test embed.",
    "https://i.imgur.com/w3duR07.png",
    "https://i.imgur.com/w3duR07.png",
    0xFF0000,
    )
###
DcWebhook.send_raw_embed({
    "embeds": [
        {
        "title": "This is a Test title.",
        "description": "This is a test raw embed.",
        "color": 0x00FFFF,
        "thumbnail": {
            "url": "https://i.imgur.com/w3duR07.png",
        },
        "image": {
            "url": "https://i.imgur.com/w3duR07.png"
        },
        }
    ]
    })
"""