from re import findall
from os import system, listdir, getcwd

files = listdir(getcwd())
if len(files) == 0:
    print('no files was found in this Directory ')
    exit()

regex_user = input('Enter a regular expression you would:  ')

found = False # u will see why
for file in files:
    if file.endswith(".txt"):
        text = open(file, 'r', encoding='UTF-8')
        contents = text.read()
        matches = findall(regex_user, contents)
        if matches:
            found = True
            print('%s was found  on "%s"' % (matches, file))
if not(found):
    print('no results was found for \'%s\''%regex_user)