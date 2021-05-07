from enum import Enum
from random import randint


class Motorcycle:
    """Motorcycle"""

    def __init__(self, brand: str, model: str, engine_cc: int,
                 hp: int, weight: int, top_speed: int,
                 acceleration: float, id_number):
        """

        :param brand:
        :param model:
        :param engine_cc:
        :param hp:
        :param weight:
        :param top_speed:
        :param acceleration:
        """
        self.brand = brand
        self.model = model
        self.engine_cc = int(engine_cc)
        self.hp = int(hp)
        self.tyre = Tyre.all
        self.weight = int(weight)
        self.top_speed = int(top_speed)
        self.acceleration = float(acceleration)
        self.id_number = int(id_number)

    def __str__(self):
        return f"Motorcycle {self.brand} {self.model} " \
               f"{self.engine_cc}-CC and {self.hp}-HP " \
               f"fitted with {self.tyre} tyres. " \
               f"Plate number is {self.id_number}."

    def show_brand(self):
        return self.brand, self.model

    def sport_exhaust(self):
        """Better exhaust more power you've got"""
        self.hp += 20

    def slick_tyre(self):
        """Dry tyre improve grip, but when it's raining be careful."""
        self.tyre = Tyre.slick
        print(f"You can use all your {self.hp}HP on every corner.")

    def wet_tyre(self):
        """Wet tyre keep you safe when is raining"""
        self.tyre = Tyre.wet

    def rain(self):
        if self.tyre == Tyre.slick:
            print("Crash!!!")
        elif self.tyre == Tyre.wet or Tyre.all:
            print("It's all fine")

    def show_acceleration(self):
        for km in range(0, self.top_speed):
            print(km, "KPH")

    def breaking(self):
        for km in range(self.top_speed, 0, -4):
            print(km, "KPH")
        print("Stop")

    def speck(self):
        return str(f"{self.brand} {self.model}\n"
                   f"Weight : {self.weight} kg\n"
                   f"Top speed : {self.top_speed} kmh\n"
                   f"Acceleration 0-100 : {self.acceleration} s")

    def lose_weight(self):
        """Lighter you faster you go"""
        self.weight -= 10
        self.acceleration -= 0.2

    def bigger_back_sprocket(self):
        """Better top speed"""
        self.top_speed += 20
        self.acceleration += 0.2

    def smaller_back_sprocket(self):
        """Better acceleration"""
        self.top_speed -= 20
        self.acceleration -= 0.2


class Tyre(str, Enum):
    all = "all weather"
    slick = "slick tyre"
    wet = "wet_tyre"


class SportMotorcycle(Motorcycle):
    """Sport bikes"""

    def __init__(self, brand, model, engine_cc, hp):

        super(SportMotorcycle, self).__init__(brand=brand,
                                              model=model,
                                              engine_cc=engine_cc,
                                              hp=hp, weight=180,
                                              top_speed=260,
                                              acceleration=3.20,
                                              id_number=int())

    def __str__(self):
        return f"Motorcycle {self.brand} {self.model} " \
               f" {self.engine_cc}-CC and {self.hp}-HP " \
               f"fitted with {self.tyre} tyres " \
               f"dry weight is {self.weight}."


class MotoGP(Motorcycle):
    """Top of the top end motorcycle ever made"""

    def __init__(self, brand):
        super(MotoGP, self).__init__(brand=brand,
                                     model="MotoGP",
                                     engine_cc=1000,
                                     hp=270, weight=180,
                                     top_speed=365,
                                     acceleration=2.20,
                                     id_number=int())


