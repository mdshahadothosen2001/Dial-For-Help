import Heading.Head as H
import Log.log as L
import Data.data as D
import Data.data as DB
import Service.service as SS


data=D.store()

H.headInfo()

while(True):
    print(".............................")
    print("...                         .")
    print("... 1     Adminastration    .")
    print("... 2       Employees       .")
    print("... 3         Members       .")
    print("... 4           Exit        .")
    print(".............................")

    print("\n.........")
    press=int(input(": Press ::"))
    print(".........\n")
    if press==1:
        L.AdminPanel()
    elif press==2:
        L.login()
        for i in range(100):
            print('1=>[Member Data] 2=>[Service history] 3=>[Back]\n')
            print("\n.........")
            pas=int(input(": Chose ::"))
            print(".........\n")
            if pas==1:
               DB.GET()
                
            if pas==2:
                data.get()
            if pas==3:
                print("  ..............................")
                print("  . <Backed From Serive Pannel .")
                print("  ..............................\n\n\n")
                break
        
    elif press==3:
        
        for i in range(100):
            print("\n1=>Be Membership 2=>Take Service 3=>Login/Logout")    
            print("\n.........")
            check=int(input(": Chose ::"))
            print(".........\n")
            if check==1:
                DB.POST()
            
            elif check==2:
                data.post()
                SS.talk()
                SS.services()
            elif check==3:
                print("\nChose 1 for Login OR 0 for Logout\n")
                print("\n.........")
                log=int(input(": Chose ::"))
                print(".........\n")
                if log==1:
                    L.login()
                    print("  ........................")
                    print("  . <Backed with login   .")
                    print("  ........................\n\n\n")  
                elif log==0:
                    L.logout()
                    print("  ........................")
                    print("  . <Backed with logout  .")
                    print("  ........................\n\n\n")    
                break
    elif press==4:
        L.logout()
        print("  ............")
        print("  .  Exited  .")
        print("  ............\n\n\n")
        break
    else:
        print("\nInvalid Key Pressed\n")


ins=input()        