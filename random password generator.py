import random
def password(length=8):
    l = ['@','#','$','%','&']
    upper = chr(random.randint(65,90))
    lower = chr(random.randint(97,122))
    special = random.choice(l)
    digit = random.randint(10000,99999)
    generate = upper + lower + special + str(digit)
    l = random.sample(generate)
    generate = ("").join(l)
    return generate 

result = password(5)
print(result)
