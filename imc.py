import tkinter as tk

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de IMC")

        tk.Label(root, text="Altura (m):").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(root, text="Peso (kg):").grid(row=1, column=0, padx=10, pady=5)

        self.entry_altura = tk.Entry(root)
        self.entry_altura.grid(row=0, column=1, padx=10, pady=5)

        self.entry_peso = tk.Entry(root)
        self.entry_peso.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(root, text="Calcular IMC", command=self.calculate_bmi).grid(row=2, columnspan=2, padx=10, pady=5)

        self.label_resultado = tk.Label(root)
        self.label_resultado.grid(row=3, columnspan=2, padx=10, pady=5)

    def calculate_bmi(self):
        try:
            altura = float(self.entry_altura.get())
            peso = float(self.entry_peso.get())
            bmi = peso / (altura ** 2)
            categoria = "Abaixo do peso" if bmi < 18.5 else "Peso normal" if bmi < 25 else "Sobrepeso" if bmi < 30 else "Obesidade"
            self.label_resultado.config(text=f"Seu IMC é: {bmi:.2f}\nCategoria: {categoria}")
        except ValueError:
            self.label_resultado.config(text="Erro: Por favor, insira valores válidos.")

def main():
    root = tk.Tk()
    calculator = BMICalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
