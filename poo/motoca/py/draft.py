class Pessoa:
    def __init__(self, name: str, age: int):
        self.__name = name 
        self.__age = age 
    
    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def __str__ (self):
        return f"{self.__name}:{self.__age}"

class Motoca:
    def __init__(self, potencia = 1, ):
        self.__potencia = potencia
        self.__time = 0
        self.__pessoa: Pessoa | None = None

    def inserir(self, pessoa:Pessoa) -> bool:
        if self.__pessoa is not None:
            print("fail: busy motorcycle")
            return False
        self.__pessoa = pessoa
        return True

    def __str__(self):
        if self.__pessoa is not None:
            return f"power:{self.__potencia}, time:{self.__time}, person:({str(self.__pessoa)})"
        else:
            return f"power:{self.__potencia}, time:{self.__time}, person:(empty)"

    def remover(self):
        if self.__pessoa is None:
            print("fail: empty motorcycle")
            return None
        else:
            pessoa_removida = self.__pessoa
            self.__pessoa = None
            return pessoa_removida

    def buyTime(self, time:int):
        self.__time += time

    def drive(self, time:int):
        if self.__time == 0:
            print("fail: buy time first")
            return
        if self.__pessoa is None:
            print("fail: empty motorcycle")
            return
        if self.__pessoa.getAge() > 10:
            print("fail: too old to drive")
            return
        if time >= self.__time:
            print(f"fail: time finished after {self.__time} minutes")
            self.__time = 0
        else:
            self.__time -= time

    def honk(self):
        return "P" + ("e" * self.__potencia) + "m"

def main():
    motoca = Motoca()
    while True:
        line = input()
        print("$" + line)
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "init":
            power = int(args[1])
            motoca = Motoca(power)
        elif args[0] == "show":
            print(motoca)
        elif args[0] == "buy":
            time = int(args[1])
            motoca.buyTime(time)
        elif args[0] == "enter":
            name = args[1]
            age = int(args[2])
            pessoa = Pessoa(name, age)
            motoca.inserir(pessoa)
        elif args[0] == "leave":
            pessoa = motoca.remover()
            if pessoa is not None:
                print(pessoa)
        elif args[0] == "drive":
            tempo = int(args[1])
            motoca.drive(tempo)
        elif args[0] == "honk":
            print(motoca.honk())

main()
        
        









































































