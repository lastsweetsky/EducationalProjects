import re

f = open('\\Users\\WSA\\PycharmProjects\\EducationalProjects\\web_course\\week2_ex1.txt', 'r')
content = f.read()

string_numbers = re.findall('[0-9]+', content)
integer_numbers = [int(x) for x in string_numbers]

answer = sum(integer_numbers)
print(answer)


