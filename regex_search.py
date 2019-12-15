from re import findall

regex_user = input('Enter a regular expression you would  ')

os.system('clear')

print('Working Directory is %s ' % os.getcwd())

def find_regex():
    for files in os.listdir('./'):
        if files.endswith(".txt"):
            text = open(files , 'r' , encoding = 'UTF-8')
            contents = text.read()
            matches  = findall(regex_user , contents)
            if len(contents) > 0:
                print('%s was found  on "%s"' % (matches , files ) )
            else:
                print('no result was found in this Directory ')


print(find_regex())
