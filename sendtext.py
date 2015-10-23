from twilio import rest
#from twilio.rest import TwilioRestClient 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACdc42ea0b20e7a189f5d30f4d1750521a"
auth_token  = "932d4b5296718c77fa5610cac7169262"
client = rest.TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="My name is GM<3",
    to="+919845504724",    # Replace with your phone number
    from_="+14155992671") # Replace with your Twilio number
print (message.sid)
