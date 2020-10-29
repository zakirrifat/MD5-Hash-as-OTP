import random
import string
import hashlib
from twilio.rest import Client

def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    #print("Random alphanumeric String is:", result_str)
    return result_str

res1 = get_random_alphanumeric_string(32)

res = hashlib.md5(res1.encode())
result= res.hexdigest()
print(result)
account_sid = 'Your account_sid'
auth_token = 'your auth_token '
client = Client(account_sid, auth_token)

message = client.messages.create(
        body= 'Your OTP For mobile Banking Security Is -' +str(result),
        from_='+12072237309',
        to= 'phone number here'
)


v = input("Enter Your Hash")
if v == result:
    print("Successfully Login with Valid Hash")
else:
    print("Hash is Not valid!!! Please Try again")