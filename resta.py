def restar(a, b):
    return a - b

if __name__ == "__main__":
    print("Calculadora de resta")
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    resultado = restar(num1, num2)
    print(f"El resultado de la resta es: {resultado}")
