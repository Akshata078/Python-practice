# Abstract Base Class -

# for this - we have to import module - 
from abc import ABC, abstractmethod   # ABC aur abstractmethod ko import kiya from abc 

# hum Animal class ko abstract class banana chahte hai - 
# abstract class => aisa class jo dusre class ko restriction deta hai.

class Animal(ABC): # ABC ko inherit kiya Animal class me, Animal class koABC se inherit krte hi Animal class abstract class bann jayega
    def eat(self) :
        print("eating")
    
    @abstractmethod  # die name ke function ko abstractmethod banane ke liye, isko hum decorator bolte hai.
    def die(self) :  # restriction wala method
        pass 


class Bird(Animal):   # inherit animal class
    def fly(self) :
        print("flying")
    def die(self) :  # restriction wala method
        print("Bird die on land")




# above example me - humne Animal class ko abstract class bana diya hai, aur isme jo die name wala method hai usko restricted kr diya hai. means agr koi dusra class Animal class ko inherit krega toh usko restriction hoga ki die wala method bhi banaye, agr nhi banayega toh fir error aayega.

bird1 = Bird()