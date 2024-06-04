import random
import string

pass_len = 12 
rstrings = string.ascii_letters + string.digits + string.punctuation 

# list comprehension for i in range (n)
# password = "".join([random.choice(rstrings) for i in range (pass_len)])


password = ""
for i in range(pass_len):
    password += random.choice(rstrings)
print("Your random password is:", password)

