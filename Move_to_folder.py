import os
entries = os.listdir('C:/')
for entry in entries:
    if 'Users' in entry:
        print '____________________'
        print '# Find Users Folder '
        print '____________________'
        entries = os.listdir('C:/Users')
        for entry in entries:
            print entry
            if 'golcatlman' in entry:
                path = '/golcatlman'
                print '-------------------------'
                print '# Find golcatlman Folder '
                print '-------------------------'
                entries = os.listdir('C:/Users/golcatlman')



