class store:
    ToMem=0
    ToSer=0
    ToPan=0
    def post(self):
        self.ToMem=self.ToMem+1
        self.ToSer=self.ToSer+1

    def get(self):
        print("\n\n      _________________")
        print("      |      History   |           ")
        print("__________________________________")
        print("| Total Member  : ",self.ToMem,"    |")
        print("| Total Service : ",self.ToSer,"    |")
        print("| Total Panding : ",self.ToPan,"    |")
        print("__________________________________\n\n")



class server:
    q='name'
    w='phone'
    e='address'
    r='no member'
    t=1
    DB={1:{q:r,w:r,e:r}}
    def postData(self,i,b,f,d):
        pd={i:{self.q:b,self.w:f,self.e:d}}
        self.DB.update(pd)
        
    def getData(self,id):
        tem=self.DB[id]
        print("\n\n      _________________")
        print("      | Member Details |    ")
        print("_________________________________________________")
        print("|  ",tem.get(self.q),"           |  |  |")
        print("|  ",tem.get(self.w),"                     |  |  |")
        print("|  ",tem.get(self.e),"                    |  |  |")
        print("|__________________________________________\n\n")


def POST():
    hg=server()
    print("\n\n..................................")
    NM=input(". Name    : ")
    ID=int(input(". ID/BOD  : "))
    PH=input(". Phone   : ")
    AR=input(". Address : ")
    print("...................................\n\n")
 
    hg.postData(ID,NM,PH,AR)

def GET():
    hg=server()
    ID=int(input("| Enter ID/BOD : | "))
    hg.getData(ID)







          

