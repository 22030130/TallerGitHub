class Suma:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def obtener_datos(self):
        print("\nOpción 1: Suma")
        try:
            self.num1 = float(input("Ingresa el primer número: "))
            self.num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Por favor, ingresa números válidos.")
            return False
        return True

    def calcular(self):
        return self.num1 + self.num2

# Prueba de la clase Suma
if __name__ == "__main__":
    operacion = Suma()
    if operacion.obtener_datos():
        print(f"Resultado de la suma: {operacion.calcular()}")