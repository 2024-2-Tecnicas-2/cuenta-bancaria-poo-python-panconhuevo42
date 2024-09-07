from cuenta_bancaria import CuentaBancaria
if __name__ == '__main__':
    cuenta1 = CuentaBancaria("Nicolas", "123456789", 10000)
    print(cuenta1.get_titular())  
    cuenta1.ingresar(700)
    print(cuenta1.get_saldo())   
    print(cuenta1.calcular_interes(10)) 
