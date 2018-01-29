import sys
'''import Validator'''


class Menu:
    '''Muestra un menu y responde a elecciones cuando se ejecuta.'''

    def __init__(self):
        '''self.validator = Validator()'''
        #self.elections = {
         #   "1": self.search_by_name,
         #   "2": self.search_by_extension,
         #   "3": self.search_by_size,
         #   "4": self.quit
        #}

    def show_menu(self):
        print("_*_*_*_*_*_ Menu _*_*_*_*_*_")
        print(" 1 Search by Name")
        print(" 2 Search by Extension")
        print(" 3 Search by Size")
        print(" 4 quit")


    def run(self):

        while True:
            self.show_menu()
            election = int(input("enter an option:  "))
            if election==1:
                print ("you select 1")
                Menu.search_by_name()
                break
            elif election == 2:
                print("you select 2")
                Menu.search_by_extension()
                break
            elif election == 3:
                print("you select 3")
                Menu.search_by_extension()
                break
            elif election == 4:
                print("you select 4")
                print("Bye Bye >)")
                sys.exit(0)
            elif  election >5 and election <= 9:
                print("Please, introduce the valid value")
            elif election == 0:
                break
            else:
                print("miauuuuu")
            #action = self.elections.get(election, None)
            #print(self.elections[election])
            #DANEEEEEEEEEEEE aca necesito que me vuelva un trueeeee...helps meee#
            #if action:
            #   action()
            #else:
            #
            #   print("{0} option not valid".format(election))



    def search_by_name (self):

        path =input("Enter path")
        '''true = self.validator.search(filter)'''
        name= input("Enter name")
        '''true = self.validator.search(filter)'''
        print ("path is "+path+"name: "+name)


    def search_by_extension(self):
        path = input("Enter path")
        '''true = self.validator.search(filter)'''
        name = input("Enter name")
        '''true = self.validator.search(filter)'''
        print ("path is " + path + "name: " + name)

    def search_by_size(self):
        path = input("Enter path")
        '''true = self.validator.search(filter)'''
        name = input("Enter name")
        '''true = self.validator.search(filter)'''
        print ("path is " + path + "name: " + name)

    def quit(self):
        print("Bye Bye >)")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()