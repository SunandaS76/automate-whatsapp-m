from twilio.rest import Client 
 
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token) 
def send():
	message = client.messages.create( 
	                              from_='whatsapp:+14155238886',  
	                              body='I think you have forgotten me🥺! ',      
	                              to='whatsapp:+91 mobile number' 
	                        ) 
	 
	print(message.sid)
