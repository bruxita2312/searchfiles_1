import sys

class Menu:
    '''display a  Menu that serponse to select an option'''

    def __init__(self):
     self.valid = valid()
     self.elections ={
        "1": self.search_by_name,
        "2": self.search_by_size,
        "3": self.search_by_extension,
        "4": self. quit
     }


     def show_menu(self):
         print ("""
         Search Menu
         1 Search by name
         2 Search by side
         3 Search by extension
         4 Exit
         """)


     def run (self):
          '''display menu and response the user election'''
          while True:
              self.show_menu()
              election= input("Enter an option:")
              action= self.elections.get(election)
              if action:
                  action()
              else:
                  print ("{0} it is no valid option".format(election))

     def search_name(self):
         '''name= self.valid.search(filter)'''
         path = input("Enter Path")
         name= input ("enter name")
         self.search_by_name(name)



     def quit (self):
         print ("Bye bye :)")
         sys.exit(0)

         
     if __name__ == "__main__":
         Menu() .run()