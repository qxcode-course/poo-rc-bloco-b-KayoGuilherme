class People:
    def __init__(self, name: str, money: float) -> None:
        self.__name: str = name
        self.__money: float = money

    def __str__(self) -> str:
        if self.__money.is_integer():
            return f"{self.__name}:{int(self.__money)}"
        else:
            return f"{self.__name}:{self.__money:.2f}"

    def getName(self) -> str:
        return self.__name

    def getMoney(self) -> float:
        return self.__money

    def pay(self, value: float) -> float:
        if self.__money >= value:
            self.__money -= value
            return value
        else:
            paid = self.__money
            self.__money = 0
            return paid

    def receive(self, value: float) -> None:
        self.__money += value


class Cycle:
    def __init__(self) -> None:
        self.__cost = 0.0
        self.__passenger: People | None = None
        self.__driver: People | None = None

    def setDriver(self, person: People) -> None:
        self.__driver = person

    def mountDriver(self, person: People) -> None:
        if self.__driver is not None:
            print("fail: no driver")
            return
        self.__driver = person

    def dismountDriver(self) -> None:
        if self.__driver is None:
            print("fail: nao tem motorista")
            return
        self.__driver = None

    def mountPassenger(self, person: People) -> None:
        if self.__passenger is not None:
            print("fail: tem passageiro")
            return
        if self.__driver is None:
            print("fail: no driver")
            return
        self.__passenger = person
        self.__cost = 0.0

    def dismountPassenger(self) -> None:
        if self.__passenger is None:
            print("fail: nao tem passa")
            return

        payment = self.__cost
        if self.__driver is not None:
            self.__driver.receive(payment)

        print(f"{self.__passenger.getName()}:{int(self.__passenger.getMoney())} left")
        self.__passenger = None
        self.__cost = 0.0

    def drive(self, km: float) -> None:
        if self.__passenger is None:
            print("fail: nao ha passageiro para dirigir")
            return
        self.__cost += km * 1.0

    def leavePassenger(self) -> None:
        if self.__passenger is None:
            print("fail: não tem passageiro")
            return

        totalCost = self.__cost
        paid = self.__passenger.pay(totalCost)

        if paid < totalCost:
            print("fail: Passenger does not have enough money")

        if self.__driver is not None:
            self.__driver.receive(totalCost)

        print(f"{self.__passenger.getName()}:{int(self.__passenger.getMoney())} left")

        self.__passenger = None
        self.__cost = 0.0

    def getDriver(self) -> People | None:
        return self.__driver

    def __str__(self) -> str:
        driver = str(self.__driver) if self.__driver else "None"
        passenger = str(self.__passenger) if self.__passenger else "None"
        return f"Cost: {int(self.__cost)}, Driver: {driver}, Passenger: {passenger}"

def main():
    cycle = Cycle()
    people = {}

    while True:
        line = input()
        print("$" + line)
        args = line.split()

        if args[0] == "end":
            break

        elif args[0] == "setDriver":
            name = args[1]
            money = float(args[2])
            if name not in people:
                people[name] = People(name, money)
            cycle.setDriver(people[name])

        elif args[0] == "mountDriver":
            name = args[1]
            money = float(args[2])
            if name not in people:
                people[name] = People(name, money)
            cycle.mountDriver(people[name])

        elif args[0] == "dismountDriver":
            cycle.dismountDriver()

        elif args[0] == "setPass":
            name = args[1]
            money = float(args[2])
            if name not in people:
                people[name] = People(name, money)
            cycle.mountPassenger(people[name])

        elif args[0] == "leavePass":
            cycle.leavePassenger()

        elif args[0] == "drive":
            km = float(args[1])
            cycle.drive(km)

        elif args[0] == "show":
            print(cycle)

main()
