import os

class Allcheck:
    def __init__(self):
        self.dirfiles = os.listdir()
        self.def_dir = os.getcwd()
        self.filelist = []
        for file in self.dirfiles:
            if file[-3:] == 'txt':
                self.filelist.append(file)
        for files in self.filelist:
            filename = files
            text = self.parcheck(filename)
            self.wNames(filename, text)
            self.moveFile(files)


    def parcheck(self,input): #returns list of names without duplicates
        import os
        path = os.getcwd() + chr(92) + self.date()
        access_rights = 0o755
        try:
            os.mkdir(path, access_rights)
        except:
            print('')
        with open(input) as file_object:
            contents = file_object.read()
            content = contents.splitlines()
            name = []
            names = []
            rawnames = []
            fnames = []
            for items in content:
                lpos = items.find('From') + 5
                rpos = items.find('to',lpos) - 1
                if rpos > 1:
                    name.append(items[lpos:rpos])
                for item in name:
                    if item not in names:
                        names.append(item)
            for name in names:
                fname = name.lower()
                rawnames.append(fname)
            for names in rawnames:
                lastpos = names.rfind(' ')
                lastname = names[lastpos + 1:]
                firstname = names[:lastpos]
                name = lastname.title() + ', ' + firstname.title()
                fnames.append(name)
            output = sorted(fnames)
            return output

    def wNames(self,filename,listname): #Generates the list of names of students that have particpated
        import os,time
        path = os.getcwd() + chr(92) + self.date()
        access_rights = 0o755
        time = str(time.strftime('%H%M%S'))
        try:
            os.mkdir(path, access_rights)
        except:
            print('')
        with open(path + chr(92) + filename[:-4] + time + '.txt','w') as file_object:
            file_object.write('List of participants:\n\n')
            for name in listname:
                file_object.write(name + '\n')

    def moveFile(self,input): #Used to move the file already processed by wNames
        import os,time
        inipath = os.getcwd() + chr(92)
        time = str(time.strftime('%H%M%S'))
        path = os.getcwd() + chr(92) + self.date() + chr(92) + 'checked' + chr(92)
        access_rights = 0o755
        try:
            os.mkdir(path, access_rights)
        except:
            print('')
        os.rename(inipath + input,path + time + input)

    def date(self): #Used to get the date for the other functions
        from time import strftime
        date = strftime("%m-%d-%y")
        return date
