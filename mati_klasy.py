class Human:
    """Klasa matka czlowiek jaki jest kazdy widzi"""

    def __init__(self, name, age, job, salary):
        self.age = age
        self.job = job
        self.name = name.capitalize()
        self.salary = salary

    def __str__(self):
        return f"{self.name} {self.age} his job is {self.job} and salary is {self.salary}."

    def pay_for_social(self, amount):
        self.salary -= amount

    def pay_for_social_500(self):
        self.salary -= 500

    def spell_name(self):
        for letter in self.name:
            print(letter)

    def capital_case(self):
        print(f"{self.name.upper()} {self.age} his job is {self.job} and salary is {self.salary}.")

    def create_email(self):
        print(f"{self.name.lower()}_{self.age}@gmail.com")


class OfficeWorker(Human):
    """Pracuje powoili i bardzo nudno"""

    def __init__(self, name):
        super(OfficeWorker, self).__init__(name=name, age=30, job="office job", salary=2000)
        self.stapler = True

    def boring_work(self):
        """Nudna praca cie postarza"""
        self.age = self.age + 5


class Cleaner(Human):
    """Konserwuje powieschnie gladkie"""

    def __init__(self, name):
        super(Cleaner, self).__init__(name=name, age=25, job="cleaning surface", salary=1500)
        self.brush = True


class Lesser(Human):
    """Bierze zasilek i nic nie robi"""

    def __init__(self, name):
        super(Lesser, self).__init__(name=name, age=45, job="unemployed", salary=0)

    def social(self):
        self.salary += 500


class Patus(Lesser):
    """Taki leser tylko jeszcze kradnie"""

    def __init__(self, name):
        super(Patus, self).__init__(name=name)




jac = Human()