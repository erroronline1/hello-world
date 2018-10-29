import os

def rename(fldr,actn,strng):
    dir=os.listdir(fldr)
    fileindex=0
    try:
        for file in dir:
            name=file[0:file.rindex('.')]
            extension=file[file.rindex('.'):]
            if actn=='r' and os.path.isfile(fldr+'/'+file): #rename
                newname='{0}({1}){2}'.format(strng,fileindex,extension)
                os.rename(fldr+'/'+file,fldr+'/'+newname)
                fileindex+=1
            if actn=='s': #strip
                newname='{0}{1}'.format(name.replace(strng,''),extension)
                os.rename(fldr+'/'+file,fldr+'/'+newname)
            print('file ',file,' renamed to ',newname)
    except Exception as e:
        print(e,': some error occured, mostly because a file with new name already exists. program aborted.')        



print("""rename all files in specified folder.
choose if you want to rename all the same (as in file(0).mp3, file(1).mp3, ...)
or strip parts of filenames (as in file_1_security_copy.mp3, file_2_security_copy.mp3, ...)
exit every time typing [exit]

all files in the given folder will be renamed regardless of file-type! folders remain untouched.
don't mess up your system.""")

folder=input('specify folder: ')
if folder=='exit':
    print('bye...')
elif not os.path.isdir(folder):
    print('folder ',folder,' not found, program aborted...')
else:
    print('listing content of folder ',folder)
    dir=os.listdir(folder)
    for file in dir:
        print(file, end='\t\t')
    
    print('\n')
    action=input('[r]ename or [s]trip part? ')
    if action=='r':
        string=input('enter new filename to start renaming immediately: ')
    elif action=='s':
        string=input('enter to be stripped part to start renaming immediately: ')
    else:
        print('bye...')
        exit()
    
    if string=='exit':
        print('bye...')
        exit()
    else:
        rename(folder,action,string)
        print('bye...')