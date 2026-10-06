class InvalidCredentialsError(Exception):
  def __init__(self,msg):
    self.msg=msg
def login(userid,pwd):
  user_credentials={'id':'1234','pwd':'anudip@123'}
  if userid==user_credentials['id'] and pwd==user_credentials['pwd']:
    print('Login Successful')
  else:
    raise InvalidCredentialsError('UserId or Password Misssmatch')
id=input("Enter User Id")
password=input("Enter Password")
try:
  login(id,password)
except InvalidCredentialsError as e:
  print(e.msg)