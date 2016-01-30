#!usr/bin/python

from twilio.rest import TwilioRestClient

# Your account SID and auth token from twilio.com/user/account
account_sid = "AC532996b95801d975b8faf3e9a23299fa"		# Enter your account SID
auth_token = "a16acf1c6b8cc991"							# Enter your authentication token
client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
	body="Hi! My name is Aakash Sethi.",
	to="",			# Replace with the recipient #
	from_="+13437004565")		# Replace with your Twilio #
print message.sid