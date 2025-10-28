class Watch:
    def __init__(self, hora:int, minuto:int, segundo: int) -> None:
        self.__hora: int = 0
        self.__minuto: int = 0
        self.__segundo: int = 0

        self.setHora(hora)
        self.setMin(minuto)
        self.setSeg(segundo)

    def __str__(self) -> str:
        return f"{self.__hora:02d}:{self.__minuto:02d}:{self.__segundo:02d}"    

    def getHora(self) -> int:
        return self.__hora
    
    def getMin(self) -> int:
        return self.__minuto
    
    def getSeg(self) -> int:
        return self.__segundo
    
    def setHora(self, valor: int) -> None:
        if valor not in range(0, 24):
           print("fail: hora invalida")
        else:   
            self.__hora = valor
      
    def setMin(self, valor: int) -> None:
        if valor not in range(0, 60):
            print("fail: minuto invalido")
        else:    
            self.__minuto = valor

    def setSeg(self, valor: int) -> None:
         if valor not in range(0, 60):
              print("fail: segundo invalido")
         else:   
             self.__segundo = valor 
                

    def nextSecond(self) -> None:
        self.__segundo += 1
        if self.__segundo == 60:
          self.__segundo = 0
          self.__minuto += 1
          if self.__minuto == 60:
            self.__minuto = 0
            self.__hora += 1
            if self.__hora == 24:
                self.__hora = 0
          
def main():
    watch = Watch(00, 00, 00)

    while True:
        line = input()
        print("$" + line)
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "init":
            watch = Watch(int(args[1]), int(args[2]), int(args[3]))
        elif args[0] == "set":
            watch.setHora(int(args[1]))
            watch.setMin(int(args[2]))
            watch.setSeg(int(args[3]))
        elif args[0] == "show":    
            print(watch)
        elif args[0] == "next":
            watch.nextSecond()
        else:
            print("comando inválido")
            
main()
        

       

        






        