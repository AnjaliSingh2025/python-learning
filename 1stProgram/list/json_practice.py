import json
d='{"cname":"Python","fees":1200,"duration":"2months"}'
s=type(d)
print(s)
x = json.loads(d)
print(x)
print(type(x))

# employees.json
file=open("/Applications/XAMPP/xamppfiles/htdocs/git_python/python-learning/1stProgram/list/employees.json", "r")
x=file.read()
finaldata = json.loads(x)
print(type(finaldata))
for a in finaldata:
    print(a['employee'])