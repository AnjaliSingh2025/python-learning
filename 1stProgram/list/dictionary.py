d={
    'name':'Python',
    'fees':8000,
    'duration':'2 Months'
}
n=d['fees']
print(n)
# Dictionary functions

e = {
    'name':'Anjali',
    'age' : 22,
    'tech' : 'Python'
    }
# p=e.get('age')
# print(p)
# Use of keys in dictionary
# for a in e.keys():
#     print(a)
# Use of values in dictionary
for a in e.values():
     print(a)
    #     print(a)
# Use of items in dictionary
for c,d in e.items():
    print(c,d)

Ju=e.pop('age')
print(e)
# update(),clear(),dict()
Anjali = {
    'course':'Python',
    'fees' : 8000,
    'duration' : '2 Months'
}
Anjali.update({'fees':100000})
print(Anjali)
del Anjali['fees']
print(Anjali)
# Ashu= Anjali.pop('course')
# print(Ashu)


Anjali['project'] = "To do list"
print(Anjali)