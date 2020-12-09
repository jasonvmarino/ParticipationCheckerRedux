import participation as p
import roster as r

while True:
    choice = input('''What would you like to do?\n1)Check for participation/attendance with rosters
2)Check for participation/attendance without rosters\n3)Quit\n''')
    if choice == '1':
        r.Rostergrade()

    if choice == '2':
        p.Allcheck()

    if choice == '3':
        break