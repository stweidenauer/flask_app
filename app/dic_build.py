import os

# Linux
pic_directory = os.path.join('/home/steffen/GitHub/flask_app/app/', 'static')

# for Windows testing see also Dictionaries_tries.ipynb
pic_directory = os.path.join('C:\\Users\\Pilot\\Documents\\GitHub\\flask_app\\app', 'static')
directories_current_dates = [r for r in os.listdir(pic_directory) if r.startswith('20')]
# Idee Dictonary mit Date als schlüssel und eine liste der Bilder als value
dicy = {}
for item in directories_current_dates:
    dicy[item] = os.listdir(os.path.join(pic_directory, item))
# print(dicy)

for key in dicy:
    print(key)
    dicy[key].sort()
    print(dicy[key][:5])
    print()