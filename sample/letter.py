class Letter:
    def __init__(self, chr,pos,count,more):
        self.chr = chr
        self.pos = pos
        self.count = count
        self.more = more

    def valoresFijos(self):
        total=0
        for i in self.pos:
            if(i==1):
                total+=1
        return total
            

    def print(self):
        if(self.more):
            print("la letra: ",self.chr," aparece: ", self.count, " veces, en las posiciones: "
        , self.pos, " puede haber más")
        elif(not self.more and self.count ==0):
            print("La letra: ",self.chr," no aparece ")
        else:
            print("la letra: ",self.chr," aparece: ", self.count, " veces, en las posiciones: "
        , self.pos, " no hay más")
    
    