import os
path='c:\\ID\\ПС Крем константиновка Ф-210 КТП 1 (60545353-f39a-4086-a1a2-8778b7704665)_ок'
def obxodFile(path, level=1):
    print('Level=', level, 'Content:',os.listdir(path))
    for i in os.listdir(path): 
        if os.path.isdir(path+'\\'+i):
            print('Спускаемся ',path+'\\'+i)
            obxodFile(path+'\\'+i, level+1)
            print('Возвращаемся в', path)
obxodFile(path)
