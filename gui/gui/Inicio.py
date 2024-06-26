import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from PyQt6.QtWidgets import QApplication
from quarto.tela_quarto import Tela_Quarto  # Importando a classe Tela_Quarto
from servicos_adicionais.Tela_servicos_adicionais import Tela_Servicos_Adicionais  # Importando a classe Tela_Servicos_Adicionais

def abrir_tela_cliente():
    app = QApplication.instance()
    if not app:
        app = QApplication([])
    from cliente2.tela_cliente2 import Tela_Cliente
    tela_cliente = Tela_Cliente()
    tela_cliente.show()
    app.exec()

def abrir_tela_reserva():
    app = QApplication.instance()
    if not app:
        app = QApplication([])
    from reserva.Tela_Reserva import Tela_Reserva
    tela_reserva = Tela_Reserva()
    tela_reserva.show()
    app.exec()

def abrir_tela_quarto():
    app = QApplication.instance()
    if not app:
        app = QApplication([])
    tela_quarto = Tela_Quarto()  # Instanciando a tela de operações de quarto
    tela_quarto.show()
    app.exec()

def abrir_tela_servicos_adicionais():
    app = QApplication.instance()
    if not app:
        app = QApplication([])
    tela_servicos = Tela_Servicos_Adicionais()  # Instanciando a tela de serviços adicionais
    tela_servicos.show()
    app.exec()

# Inicializa a aplicação principal do Tkinter
root = tk.Tk()
root.title("Interface Principal")
root.geometry("400x400")

# Carrega a imagem de fundo
bg_image = Image.open(r"C:\Users\peter\OneDrive\Documentos\programação\PAV\hotel2_Atual\gui\gui\icons\theme_hotel.jpg")
bg_image = bg_image.resize((400, 400), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Label para a imagem de fundo
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Frame transparente para conteúdo sobreposto
frame_conteudo = ttk.Frame(root)
frame_conteudo.place(relx=0.5, rely=0.5, anchor="center")

# Título
titulo = ttk.Label(frame_conteudo, text="Menu Principal", font=('Helvetica', 18, 'bold'), background="#ffffff")
titulo.pack(pady=10)

# Frame para a lista com rolagem
frame_lista = ttk.Frame(frame_conteudo)
frame_lista.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Adicionar uma barra de rolagem
scrollbar = ttk.Scrollbar(frame_lista, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Lista de palavras
palavras = [
    ("Cliente", abrir_tela_cliente),
    ("Hóspede", lambda: print("Abrir janela de Hóspede")),
    ("Reserva", abrir_tela_reserva),
    ("Operações de Quarto", abrir_tela_quarto),  # Adicionando a opção de operações de quarto
    ("Serviços Adicionais", abrir_tela_servicos_adicionais),  # Adicionando a opção de serviços adicionais
    ("Promoção", lambda: print("Abrir janela de Promoção")),
    ("Tarifa", lambda: print("Abrir janela de Tarifa")),
    ("Feedback", lambda: print("Abrir janela de Feedback"))
]

# Caixa de listagem
listbox = tk.Listbox(frame_lista, yscrollcommand=scrollbar.set, font=('Helvetica', 12), bg='#ffffff', selectbackground='#0078d7')
for palavra, comando in palavras:
    listbox.insert(tk.END, palavra)

listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=listbox.yview)

# Evento de clique na lista
def on_select(event):
    selecionado = listbox.curselection()
    if selecionado:
        _, comando = palavras[selecionado[0]]
        comando()  # Chama a função correspondente ao item selecionado

listbox.bind("<<ListboxSelect>>", on_select)

# Iniciar o loop principal do Tkinter
root.mainloop()
