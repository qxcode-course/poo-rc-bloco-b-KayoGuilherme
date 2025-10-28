class Camisa:
    def __init__(self):
        self.tamanho: str = ""


    def __str__(self) -> str:
       if self.tamanho == "":
        return "size: ()"
       else:
           return f"size: ({self.tamanho})"

    def getTamanho(self) -> str:
        return self.tamanho 
    

    def setTamanho(self, valor: str) -> None:
        valido = ["PP", "P", "M", "G", "GG", "XG"]

        if valor not in valido:
           print(f"fail: Valor inválido, tente PP, P, M, G, GG ou XG")
        else:
           self.tamanho = valor
        
  
def main():
    camisa: Camisa = Camisa()      
    
    while True:

        line = input()
        print("$" + line)
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(camisa)
        elif args[0] == "size":
            camisa.setTamanho(args[1])
        else:
            print("fail: comando inválido")
main()