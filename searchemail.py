import re

file_path = r'PATH' # input path to txt file
regular = r'[\w\d._-]+@[\w\d.-]+' # regular expression

text_file = open(file_path, 'r') # open file to read
text = text_file.read() # read all txt file

results = re.findall(regular, text) # search regular expression in text

for i in results: # outputs results
    print(i)
