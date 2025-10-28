class Bateria:
    def __init__(self, capacidade: int):
        self.__capacidade: int = capacidade
        self.__carga: int = capacidade

    def getCapacidade(self) -> int:
        return self.__capacidade
    
    def getCarga(self) -> int:
        return self.__carga
    
    def gastar(self, tempo: int):
        if tempo > self.__carga:
            gasto_real = self.__carga
            self.__carga = 0
            return gasto_real
        else:
            self.__carga -= tempo
            return tempo
        
    def carregar(self, quantidade: int):
        self.__carga += quantidade
        if self.__carga > self.__capacidade:
            self.__carga = self.__capacidade

    def mostrar(self):
        print(f"({self.__carga}/{self.__capacidade})")

class Carregador:
    def __init__(self, potencia: int) -> None:
        self.__potencia = potencia

    def getPotencia(self):
        return self.__potencia
    
    def mostrar(self):
        print(f"Potência {self.__potencia}")

    
class Notbook:
    def __init__(self) -> None:
        self.__ligado: bool = False
        self.__bateria: Bateria | None = None
        self.__carregador: Carregador | None = None

    def getBateria(self):
        return self.__bateria
    
    def setBateria(self, bateria: Bateria):
        self.__bateria = Bateria

    def rmBateria(self):
        if self.__bateria:
            print("bateria removida")
            temp = self.__bateria
            self.__bateria = None
            return temp
        else:
            print("nenhuma bateria para remover")

    def setCarregador(self, carregador: Carregador):
        self.__carregador = carregador

    def ligar(self):
        carga = self.__bateria.getCarga() if self.__bateria else 0
        if carga > 0 or self.__carregador:
            self.__ligado = True
            print("Notbook ligado")
        else:
            print("não foi possivel ligar")

    def desligar(self):
        if self.__ligado:
            self.__ligado = False
            print("notbook desligado")

    def mostrar(self):
        if self.__ligado:
            estado = "Ligado"
        else:
            estado = "Desligado"

        if self.__bateria is None:
            bateria_status = "(Nenhuma)"
        else:
            bateria_status = f"({self.__bateria.getCarga()}/{self.__bateria.getCapacidade()})"

        if self.__carregador is None:
            carregador_status = "(Desconectado)"
        else:
            carregador_status = f"(Potência {self.__carregador.getPotencia()})"

        print("Status:", estado, ", Bateria:", bateria_status, ", Carregador:", carregador_status)

    def usar(self, tempo: int):
        if not self.__ligado or self.__bateria is None or self.__bateria.getCarga() == 0:
            print("erro: ligue o notbook primeiro")
        else:
            gasto = self.__bateria.gastar(tempo)
            if gasto < tempo:
                print(f"Usando por {gasto} minutos")
                self.__ligado = False
            else:
                print(f"Usando por {tempo} minutos")
