import re

data_file = open('3.txt', 'r')
data_str = data_file.read()
data_file.close()

pattern = "[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+"
all_small = ''.join(re.findall(pattern, data_str))
