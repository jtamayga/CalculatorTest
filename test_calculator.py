import unittest

def sumar(num1,num2):
    suma = num1 + num2
    print("el resultado de la suma es: ", suma)
    return suma 

def restar(num1,num2):
    resta = num1 - num2
    print("el resultado de la resta es: ", resta)
    return resta

def multiplicar(num1,num2):
    multiplicacion = num1 * num2
    print("el resultado de la multiplicacion es: ", multiplicacion)
    return multiplicacion 

def dividir(num1,num2):
    division = num1 / num2
    print("el resultado de la division es: ", division)
    return division

num1 = input("ingrese un numero: ")
num2 = input("ingrese un numero: ")

class test_resultados(unittest.TestCase):
    
    def test_suma(self):
        result_suma = num1 + num2
        self.assertEqual(sumar(num1,num2), result_suma)

    def test_resta(self):
        result_resta = num1 - num2
        self.assertEqual(restar(num1,num2), result_resta)

    def test_multiplicar(self):
        result_multiplicar = num1 * num2
        self.assertEqual(multiplicar(num1,num2), result_multiplicar)

    def test_dividir(self):
        result_dividir = num1 / num2
        self.assertEqual(dividir(num1,num2), result_dividir)

     

if __name__ == '__main__':
    unittest.main()