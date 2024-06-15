import random

class Cats():
    def __init__(self,pattern,colour,personality):
        self.pattern=pattern
        self.colour=colour 
        self.personality=personality
        self.catlist=["calico","blackcat"]

    def get_shape(self): 
        return self.shape 
    
    def set_shape(self,newshape):
        self.shape=newshape 

    def catshow(self):
        print("Meow! I'm a cat with the pattern {}, the colour {}, and the personality {}.".format(self.pattern,self.colour,self.personality))

calico=Cats("multicolour","orange black white","loyal")
blackcat=Cats("single colour","black","mysterious")

print(calico.catlist[random.randint(0,1)])




    
    

    






