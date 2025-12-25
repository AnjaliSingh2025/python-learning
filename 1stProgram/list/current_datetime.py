import datetime
x = datetime.datetime.now()
print(x)
print(x.strftime("%d-%m-%Y"))
print(x.strftime("%H:%M:%S"))




# Code	Meaning	Example
# %Y	Year (4 digits)	2025
# %y	Year (2 digits)	25
# %m	Month (01–12)	12
# %d	Day (01–31)	24
# %B	Full month name	December
# %b	Short month name	Dec
# %A	Full weekday	Tuesday
# %a	Short weekday	Tue
# %H	Hour (24‑hour)	14
# %I	Hour (12‑hour)	02
# %p	AM / PM	PM
# %M	Minutes	30
# %S	Seconds	45
