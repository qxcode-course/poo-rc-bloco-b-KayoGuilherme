class Battery:
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__charge = capacity
    
    def getBattery(self):
        return f"{self.__charge}/{self.__capacity}"
    
    def usingBattery(self, time: int):
        self.__charge -=time
        if self.__charge < 0:
            self.__charge = 0

    def carregar(self, power: int, time: int):
        self.__charge += power * time
        if self.__charge > self.__capacity:
            self.__charge = self.__capacity

    def hasCharge(self):
        return self.__charge > 0
    
    def getCharge(self):
        return self.__charge
    
    def getCapacity(self):
        return self.__capacity
    
class Charger:
    def __init__(self, power: int):
        self.__power = power
    
    def getPower(self):
        return self.__power

class Not:
    def __init__(self):
        self.__on = False
        self.__userTime = 0
        self.__battery: Battery | None = None
        self.__charger: Charger | None = None

    def ligar(self):
        if (self.__battery and self.__battery.hasCharge()) or self.__charger:
            self.__on = True
        else:
            print("fail: não foi possível ligar")

    def desligar(self):
        if not self.__on:
            print("fail: já desligado")
            return
        self.__on = False
    
    def setBateria(self, capacity: int):
        if self.__battery:
            print("fail: bateria ja conectada")
            return
        self.__battery = Battery(capacity)

    def rmBateria(self):
        if not self.__battery:
            print("fail: Sem bateria")
            return
        print(f"Removido {self.__battery.getBattery()}")
        self.__battery = None
        if not self.__charger:
            self.__on = False

    def setCarregador(self, power: int):
        if self.__charger:
            print("fail: carregador já conectado")
            return
        self.__charger = Charger(power)

    def rmCarregador(self):
        if not self.__charger:
            print("fail: Sem carregador")
            return
        
        print(f"Removido {self.__charger.getPower()}W")
        self.__charger = None
        if not self.__battery:
            self.__on = False
    
    def usar(self, time: int):
        if not self.__on:
            print("fail: desligado")
            return
        time = int(time)
        self.__userTime += time
        
        if self.__battery and self.__charger:
            self.__battery.carregar(self.__charger.getPower(), time)
        elif self.__battery:
            start_charge = self.__battery.getCharge()
            self.__battery.usingBattery(time)
            if not self.__battery.hasCharge():
                print("fail: descarregou")
                self.__on = False
                self.__userTime -= (time - start_charge)
        elif self.__charger:
            pass
        else:
            print("fail: desligado")
            self.__on = False
    
    def show(self):
        status = "ligado" if self.__on else "desligado"

        text = f"Notebook: {status}"
        if self.__on:
            text += f" por {self.__userTime} min"
        
        parts = []
        if self.__charger:
            parts.append(f"Carregador {self.__charger.getPower()}W")
        if self.__battery:
            parts.append(f"Bateria {self.__battery.getBattery()}")
        if parts:
            text += ", " + ", ".join(parts)
        print(text)

def main():
    notebook = Not()
    while True:
        line = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            notebook.show()
        elif args[0] == "turn_on":
            notebook.ligar()
        elif args[0] == "turn_off":
            notebook.desligar()
        elif args[0] == "use":
            notebook.usar(int(args[1]))
        elif args[0] == "set_charger":
            notebook.setCarregador(int(args[1]))
        elif args[0] == "rm_charger":
            notebook.rmCarregador()
        elif args[0] == "set_battery":
            notebook.setBateria(int(args[1]))
        elif args[0] == "rm_battery":
            notebook.rmBateria()
        else:
            print("fail: comando invalido")
main()
        
    