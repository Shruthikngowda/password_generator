import random
import string

def random_Password(password_len):
    """Generating a random password contains uppercase,lowercase,digit and symbol """
    random_Source = string.ascii_letters + string.digits + string.punctuation
    #print(random_Source)
    Random_password = random.choice(string.ascii_lowercase)
    #print("1 ", Random_password)
    Random_password += random.choice(string.ascii_uppercase)
    #print("2 ",Random_password)
    Random_password += random.choice(string.digits)
    #print("3 ", Random_password)
    Random_password += random.choice(string.punctuation)
    #print("4 ", Random_password)
    for j in range(password_len-4):
        Random_password += random.choice(random_Source)
        #print("loop : ", Random_password)
    password_List = list(Random_password)
    #print("password_List: ", password_List)
    random.SystemRandom().shuffle(password_List)
    password = ''.join(password_List)
    return password
try:
  user_input = int(input("Hi, how much length password you require?"))
  if user_input <= 4:
    print("password must be more than 4 characters")
  else :
    print ("Your Random Password is ", random_Password(user_input))
except :
  print("Please enter digits between 5 and 10 only")


