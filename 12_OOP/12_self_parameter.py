# self parameter -

class Tata :
    def service(self):
        print("Tata car servicing done...")

class Mahindra :
    def service(self):
        print("Mahindra car servicing done...")
    def allServices(self, other):
        self.service()
        other.service()


nexon = Tata()
thar = Mahindra()

thar.allServices(nexon)





