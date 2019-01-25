import re

text = 'dksaj Dimitar Zahariev @Ramsess dsa\ndksaj Jhoni Zahariev @Ramsess dsa'
pattern = re.compile(r'(?P<fname>[A-Z][a-z]*)\s*(?P<lname>[A-Z][a-z]*)\s*(?P<prqkor>@[A-z]*)')
matches = re.finditer(pattern, text)


print(*[match.group('fname') for match in matches])
