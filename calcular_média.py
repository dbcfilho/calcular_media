import tkinter as tk

# Função para calcular a média e determinar a situação do aluno
def calcular_situacao():
    nome = entry_nome.get()
    notas = [float(entry_nota1.get()), float(entry_nota2.get())]
    presencas = int(entry_presenca.get())
    falta = int(entry_falta.get())
    
    if presencas + falta > 0:
        frequencia = (presencas / (presencas + falta)) * 100
    else:
        frequencia = 0
    
    media = sum(notas) / len(notas)
    
    if media >= 6 and frequencia >= 75:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    
    resultado_label.config(text=f"Nome: {nome}\nMédia: {media:.2f}\nFrequência: {frequencia:.2f}%\nSituação: {situacao}")

# Criação da janela principal
root = tk.Tk()
root.title("Sistema de Notas e Frequência")

# Labels
label_nome = tk.Label(root, text="Nome do Aluno:")
label_nota1 = tk.Label(root, text="Nota 1:")
label_nota2 = tk.Label(root, text="Nota 2:")
label_presenca = tk.Label(root, text="Presenças:")
label_falta = tk.Label(root, text="Faltas:")

# Entradas
entry_nome = tk.Entry(root)
entry_nota1 = tk.Entry(root)
entry_nota2 = tk.Entry(root)
entry_presenca = tk.Entry(root)
entry_falta = tk.Entry(root)

# Botão para calcular a situação
calcular_button = tk.Button(root, text="Calcular Situação", command=calcular_situacao)

# Resultado
resultado_label = tk.Label(root, text="")

# Layout
label_nome.grid(row=0, column=0)
label_nota1.grid(row=1, column=0)
label_nota2.grid(row=2, column=0)
label_presenca.grid(row=3, column=0)
label_falta.grid(row=4, column=0)

entry_nome.grid(row=0, column=1)
entry_nota1.grid(row=1, column=1)
entry_nota2.grid(row=2, column=1)
entry_presenca.grid(row=3, column=1)
entry_falta.grid(row=4, column=1)

calcular_button.grid(row=5, column=0, columnspan=2)
resultado_label.grid(row=6, column=0, columnspan=2)

# Iniciar a interface gráfica
root.mainloop()

