from motorcycle_klasy import Motorcycle, MotoGP, SportMotorcycle, Tyre


class Garage:
    """Garage store motorcycle and  restore them"""

    def __init__(self, spaces, name):
        self.name = str(name)
        self.spaces = int(spaces)
        self.inventory = []
        self.motorcycle = Motorcycle
        self.details = Motorcycle.show_brand

    def add_motorcycle(self, motorcycle):
        """If is enough space adding motorcycle to garage"""
        if self.spaces == 0:
            print("Sorry mate not enough space in garage")
        elif self.spaces > 0:
            self.inventory.append(motorcycle)
            self.spaces -= 1
            self.details = " ".join(motorcycle.show_brand())
            print(f"Adding motorcycle {self.details} to the garage.")

    def del_motorcycle(self, motorcycle):
        """Remove motorcycle from garage list"""
        if motorcycle not in self.inventory:
            print("Sorry the garage is empty, I don't know what"
                  " happen to your motorcycle.")
        if motorcycle in self.inventory:
            self.inventory.remove(motorcycle)
            self.spaces += 1
            self.details = " ".join(motorcycle.show_brand())
            print(f"Removing motorcycle {self.details} from garage.")

    def show_garage(self):
        """Show all motorcycle in inventory and give a name of garage"""
        print(f"In garage {self.name} we have:")
        for moto in self.inventory:
            print(moto)
            print(moto.speck())

    def get_ready_for_race(self):
        """Upgrade motorcycle parts for better performance"""
        print("Time to get ready for the race")
        for moto in self.inventory:
            print(moto.speck())
            print("We upgraded you're bike new parameters are: ")
            self.motorcycle = moto.lose_weight()
            self.motorcycle = moto.sport_exhaust()
            print(moto.speck())


val = Motorcycle("Yamaha", "R6", 600, 120, 180, 260, 3.2, 22)
mar = SportMotorcycle("Honda", "CBR", 100, 190)
gar = Garage(2, "Warsztat u bronka")
gar.add_motorcycle(val)
