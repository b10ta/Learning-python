from re import findall
from os import system, listdir, getcwd

regex_user = input('Enter a regular expression you would:  ')

print('Working Directory is %s ' % getcwd())

for files in listdir('./'):
    if files.endswith(".txt"):
        text = open(files, 'r', encoding='UTF-8')
        contents = text.read()  # contents is the file content, it's length is always >0
        matches = findall(regex_user, contents)
        if len(contents) > 0:
            # hey? whats that?, this is always false
            print('%s was found  on "%s"' % (matches, files))
        else:
            print('no result was found in this Directory ')