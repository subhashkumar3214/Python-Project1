## Project name:- Random Password Generator

# ## 1st method
# import random
# import string

# pass_len = 12
# charValues = string.ascii_letters + string.digits  + string.punctuation

# password = ""
# for i in range(pass_len):
#     password += random.choice(charValues)

# print("Your random password is :", password)



## 2nd method :-> using list comprehensions [function for i in range(n)]

import random
import string

pass_len = 12
charValues = string.ascii_letters + string.digits  + string.punctuation

# using list comprehensions [function for i in range(n)]
password = "".join([random.choice(charValues) for i in range(pass_len)])

print("Your random password is :", password)