import os

class Rostergrade():
    def __init__(self):
        self.dirfiles = os.listdir()
        self.def_dir = os.getcwd()
        self.filelist = []
        t_num = 0
        print('Which file would you like to check?')
        for file in self.dirfiles:
            if file[-3:] == 'txt':
                self.filelist.append(file)
        for file in self.filelist:
            t_num += 1
            print(str(t_num) + ') ' + file)
        choice = input()
        number = int(choice) - 1
        file_name = self.filelist[number]
        roster = self.getroster()
        parlist = self.parcheck(file_name)
        self.rcompare(parlist, roster)
        self.moveFile(file_name)

    def getroster(self):
        import os
        t_num = 0
        path = os.getcwd() + chr(92) + 'rosters'
        filelist = os.listdir(path)
        print('Which roster would you like to use?')
        for file in filelist:
            t_num += 1
            print(str(t_num) + ') ' + file)
        choice = input()
        number = int(choice) - 1
        rostername = filelist[number]
        return rostername


    def rcompare(self,parlist, rostername):
        import os
        _object = os.getcwd() + chr(92) + 'rosters' + chr(92) + rostername
        with open(_object, 'r') as file_object:
            contents = file_object.read()
            rosterlist = contents.splitlines()
            absent = []
            unknown = []
            for name in rosterlist:
                if name not in parlist:
                    absent.append(name)
            for name in parlist:
                if name not in rosterlist:
                    unknown.append(name)
        # placeholder, need it to write to the file
        self.anames(rostername, absent)
        if unknown:
            self.unames(rostername, unknown)


    def anames(self,filename, listname):  # Generates the list of names of students that have particpated
        import os
        path = os.getcwd() + chr(92) + self.date()
        access_rights = 0o755
        try:
            os.mkdir(path, access_rights)
        except:
            print('')
        with open(path + chr(92) + filename[:-4] + '.txt', 'w') as file_object:
            file_object.write('List of students not present/did not participate:\n\n')
            for name in listname:
                file_object.write(name + '\n')


    def unames(self,filename, listname):  # Generates the list of names of students that have particpated
        import os
        path = os.getcwd() + chr(92) + self.date()
        access_rights = 0o755
        try:
            os.mkdir(path, access_rights)
        except:
            print('')
        with open(path + chr(92) + filename[:-4] + '.txt', 'a') as file_object:
            file_object.write('\n\nList of unknown participants/students:\n\n')
            for name in listname:
                file_object.write(name + '\n')


    def date(self):  # Used to get the date for the other functions
        from time import strftime
        cdate = strftime("%m-%d-%y")
        return cdate

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

    def moveFile(self, input):  # Used to move the file already processed by wNames
        import os
        inipath = os.getcwd() + chr(92)
        path = os.getcwd() + chr(92) + self.date() + chr(92) + 'checked' + chr(92)
        access_rights = 0o755
        try:
            os.mkdir(path, access_rights)
        except:
            print('')
        os.rename(inipath + input, path + input)