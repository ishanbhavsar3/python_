import random

lowercase = "abcdefghijklmnopqrstuvwxyz";
uppercase = lowercase.upper();
numbers = "0123456789";
symbols = "[]{}();*/-_";
 
all = lowercase + uppercase + numbers + symbols
length = 16;
password = "".join(random.sample(all, length))
print(password)
