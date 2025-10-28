class Tamagotchi:
    def __init__(self, energyMax: int, cleanMax: int):
        self.energyMax = energyMax
        self.cleanMax = cleanMax
        self.energy = energyMax
        self.clean = cleanMax
        self.age = 0
        self.alive = True

    def set_energy(self, value: int):
        if value <= 0:
            self.energy = 0
            self.alive = False
            return "fail: pet morreu de fraqueza"
        elif value > self.energyMax:
            self.energy = self.energyMax
        else:
            self.energy = value
        return None
    
    def set_clean(self, value: int):
        if value <= 0:
            self.clean = 0
            self.alive = False
            return "fail: pet morreu de sujeira"
        elif value > self.cleanMax:
            self.clean = self.cleanMax
        else:
            self.clean = value
        return None
    
    def isAlive(self):
        return self.alive
    
    def show(self):
        return f"E:{self.energy}/{self.energyMax}, L:{self.clean}/{self.cleanMax}, I:{self.age}"
    

class Game:
    def __init__(self):
        self.pet = None

    def init(self, energyMax, cleanMax):
        self.pet = Tamagotchi(energyMax, cleanMax)

    def play(self):
        if not self.pet.isAlive():
            return "fail: pet esta morto"
        
        self.pet.age += 1
        
        msg_energy = self.pet.set_energy(self.pet.energy - 2)
        msg_clean = self.pet.set_clean(self.pet.clean - 3)
        if msg_energy: 
            return msg_energy
        if msg_clean: 
            return msg_clean

        return None

    def sleep(self):
        if not self.pet.isAlive():
            return "fail: pet esta morto"
            
        if self.pet.energy > self.pet.energyMax - 5:
            return "fail: nao esta com sono"
        
        turnos = self.pet.energyMax - self.pet.energy
        msg = self.pet.set_energy(self.pet.energyMax)
        if msg:
            return msg
        self.pet.age += turnos
        return None

    def shower(self):
        if not self.pet.isAlive():
            return "fail: pet esta morto"
        self.pet.age += 2
        
        msg_energy = self.pet.set_energy(self.pet.energy - 3)
        msg_clean = self.pet.set_clean(self.pet.cleanMax)
        
        if msg_energy: 
            return msg_energy
        if msg_clean: 
            return msg_clean
        
        return None

    def show(self):
        return self.pet.show()
    

def main():
    game = Game()

    while True:
        try:
            line = input().strip()
        except EOFError:
            break
        if line == "":
            continue
        print(f"${line}")

        if line == "end":
            break

        args = line.split()
        cmd = args[0]

        if cmd == "init":
            e, c = map(int, args[1:])
            game.init(e, c)
        elif cmd == "show":
            print(game.show())
        elif cmd == "play":
            msg = game.play()
            if msg:
                print(msg)
        elif cmd == "sleep":
            msg = game.sleep()
            if msg:
                print(msg)
        elif cmd == "shower":
            msg = game.shower()
            if msg:
                print(msg)
main()
