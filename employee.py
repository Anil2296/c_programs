class employee:
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal
    def process(self):
        if self.sal>=50000:
          self.hra=self.sal*.4
          self.da=self.sal*.3
          self.pf=self.sal*.2
        
        else:
           self.hra=self.sal*.4
           self.da=self.sal*.3
           self.pf=self.sal*.2
        self.gsal=self.sal+self.hra+self.da
        self.nsal=self.gsal-self.pf
    def output(self):
            print("employee id =",self.id)
            print("employee name =",self.name)
            print("employee sal =",self.sal)
e1=employee(100,"sai",20000)
e2=employee(200,"chandu",50000)
e1.process()
e2.process()
e1.output()
e2.output()

