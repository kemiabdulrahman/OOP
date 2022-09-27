import json
x = '{"Name":"AbdulRahman", "Age":"34", "Country":"New-York"}'
y = json.loads(x)
print(y['Age'])

x = {"Name":"AbdulRahman", "Age":"34", "Country":"New-York"}

y = json.dumps(x, indent=4, separators=(".", "="))
print(y)

js_file = '{"Name":"Adeleke", "Class":"JSS3", "Date Of Birth":"January 30, 2009","":"","":"",
"":"", "":"", "":"", "":"",
"":"", "":""}'



