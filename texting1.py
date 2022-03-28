from twilio.rest import Client 

accountSID = 'AC27a44827015ea06c5fba802ef92fa619'

authToken = '406178700f0ec43cbc132a5fd1db5b58'

client = Client(accountSID, authToken)

TwilioNumber = '+17623374113'

mycellphone = '+19197471849'

textmessage = client.messages.create(to = mycellphone, from_ = TwilioNumber, body = 'Hello World')

print(textmessage.status)

#make phone call

cell = client.calls.create(url = 'http://demo.twilio.com/docs/voice.xml', to = mycellphone, from_ = TwilioNumber)