class Camisa:
    def __init__(self):
        self.tamanho: str = ""


    def getTamanho(self) -> str:
        return self.tamanho 
    

    def setTamanho(self, valor: str) -> None:
        valido = ["PP", "P", "M", "G", "GG", "XG"]

        if valor not in valido:
            print(f"Erro: tamanho inválido")
        else:
            self.tamanho = valor


def main():
    camisa: Camisa = Camisa()      
    while camisa.getTamanho() == "":
        tamanho = input()
        camisa.setTamanho(tamanho)

    print(f"Parabens! Você comprou uma camisa do tamanho {camisa.getTamanho()}.")

main()