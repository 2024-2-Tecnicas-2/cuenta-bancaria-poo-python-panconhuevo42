class CuentaBancaria:
    def __init__(self, titular, numero_cuenta, saldo):
        self.__titular = titular
        self.__numero_cuenta = numero_cuenta
        self.__saldo = saldo
        

    def get_titular(self):
        return self.__titular

    def set_titular(self, nuevo_titular):
        self.__titular = nuevo_titular

    def get_numero_cuenta(self):
        return self.__numero_cuenta

    def get_saldo(self):
        return self.__saldo

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
        else:
            print("debe ser positivo")

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("Fondos insuficientes o cantidad a retirar invalida")


    def calcular_interes(self, interes):
        if 0 < interes <= 10:
            interes = self.__saldo * (interes / 100)
            return self.__saldo + interes
        else:
            print("el tipo de interes debe estar entre 0% y 10%")
