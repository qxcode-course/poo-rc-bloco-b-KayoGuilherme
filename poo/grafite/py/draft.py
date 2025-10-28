class Grafite:
    def __init__(self, calibre: float, dureza: str, tamanho: int):
        self.calibre = calibre
        self.dureza = dureza
        self.size = int(tamanho)


    def usagePerSheet(self) -> int:
        gasto = {
            "HB": 1,
            "2B": 2,
            "4B": 4,
            "6B": 6
        }
        return gasto.get(self.dureza, 0)
    
    def __str__(self) -> str:
        return f"{self.calibre}:{self.dureza}:{self.size}mm"
    

class Lapiseira:
    def __init__(self, calibre: float = None):
        if calibre:
            self.calibre = float(calibre)
        else:
            self.calibre = None
        self.ponta: Grafite | None = None

    def __str__(self):
        if self.calibre is not None:
            calibre = str(self.calibre)
        else:
            calibre = "None"
        if self.ponta is not None:
            return f"calibre: {calibre}, grafite: [{self.ponta.calibre}:{self.ponta.dureza}:{self.ponta.size}]"
        else:
            return f"calibre: {calibre}, grafite: null"

    def hasGrafite(self) -> bool:
        return self.ponta is not None
    
    def insert(self, grafite: Grafite) -> bool:
        if self.calibre is None:
            print("fail: calibre incompativel")
            return False
        if abs(self.calibre - float(grafite.calibre)) > 1e-9:
            print("fail: calibre incompativel")
            return False
        if self.ponta is not None:
            print("fail: ja existe grafite")
            return False
        self.ponta = grafite
        return True
    
    def remover(self):
        if self.ponta is None:
            print("fail: nao existe grafite")
            return None
        self.ponta = None
        return True
    
    def writePage(self):
        if self.ponta is None:
            print("fail: nao existe grafite")
            return False
        if 10 >= self.ponta.size:
            print("fail: tamanho insuficiente")
            return False
        usage = self.ponta.usagePerSheet()
        if 0 >= usage:
            print("fail: dureza invalida")
            return False
        if(self.ponta.size - usage) < 10:
            self.ponta.size = 10
            print("fail: folha incompleta")
            return False
        else:
            self.ponta.size -= usage
            return True
        
def main():
    lapiseira = Lapiseira
    while True:
        line = input()
        print("$" + line)
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "init":
            calibre = float(args[1])
            lapiseira = Lapiseira(calibre)
        elif args[0] == "insert":
            calibre = float(args[1])
            dureza = args[2]
            tamanho = int(args[3])
            grafite = Grafite(calibre, dureza, tamanho)
            lapiseira.insert(grafite)
        elif args[0] == "remover" or args[0] == "remove":
            if lapiseira is None:
                print("fail: lapiseira nao iniciada")
                continue
            lapiseira.remover()
        elif args[0] == "write":
            lapiseira.writePage()
        elif args[0] == "show":
            print(lapiseira)

main()