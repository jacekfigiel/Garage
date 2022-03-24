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
            self.details = motorcycle.show_brand()
            print(f"Adding motorcycle {self.details} to the garage.")

    def del_motorcycle(self, motorcycle):
        """Remove motorcycle from garage list"""
        if motorcycle not in self.inventory:
            print("Sorry the garage is empty, I don't know what"
                  " happen to your motorcycle.")
        elif motorcycle in self.inventory:
            self.inventory.remove(motorcycle)
            self.spaces += 1
            self.details = motorcycle.show_brand()
            print(f"Removing motorcycle {self.details} from garage.")

    def show_garage(self):
        """Show all motorcycle in inventory and give a name of garage"""
        if len(self.inventory) == 0:
            print("The garage is empty.")
        elif len(self.inventory) > 0:
            print(f"In garage {self.name} we have:")
            for moto in self.inventory:
                print(moto)

    def get_ready_for_race(self):
        """Upgrade motorcycle parts for better performance"""
        print("Time to get ready for the race")
        for moto in self.inventory:
            print(moto.speck())
            print("We upgraded you're bike new parameters are: ")
            self.motorcycle = moto.lose_weight()
            self.motorcycle = moto.sport_exhaust()
            self.motorcycle = moto.slick_tyre()
            print(moto.speck())
            print()

    def get_ready_for_off_road_race(self):
        """Upgrade motorcycle for better performance on dirt track"""
        print("time to get dirty.")
        for moto in self.inventory:
            print(moto.speck())
            print("We upgraded you're bike new parameters are: ")
            self.motorcycle = moto.off_road_settings()
            self.motorcycle = moto.smaller_back_sprocket()
            print(moto.speck())
            print()

    def go_back_on_road(self):
        """Bring back motorcycle to factory settings"""
        print("Let's go back on the road.")
        for moto in self.inventory:
            self.motorcycle = moto.public_road_settings()

    def move_to_other_garage(self):
        """Moving motorcycle between garages"""
        machine = self.motorcycle.pop()
        self.inventory.append(machine)


val = Motorcycle("Yamaha", "R6", 600, 120, 180, 260, 3.2, 22)
mar = SportMotorcycle("Honda", "CBR", 100, 190)
gar = Garage(2, "Warsztat u bronka")
gar2 = Garage(2, "Warsztat u Zenka")
gar.add_motorcycle(val)
gar.add_motorcycle(mar)
gar.get_ready_for_race()
gar.show_garage()

