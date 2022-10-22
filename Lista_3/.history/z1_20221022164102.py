import string

samo = list('a','e','i','o','u','y','ą','ę')
spol = list(i for i in string.ascii_lowercase if i == x for x in samo)
print(spol)