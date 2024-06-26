import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Funções para abrir novas janelas
def abrir_cliente():
    nova_janela('Cliente')

def abrir_hospede():
    nova_janela('Hóspede')

def abrir_reserva():
    nova_janela('Reserva')

def abrir_promocao():
    nova_janela('Promoção')

def abrir_tarifa():
    nova_janela('Tarifa')

def abrir_servicos_adicionais():
    nova_janela('Serviços Adicionais')

def abrir_quarto():
    nova_janela('Quarto')

def abrir_feedback():
    nova_janela('Feedback')

def nova_janela(titulo):
    nova = tk.Toplevel()
    nova.title(titulo)
    nova.geometry("300x200")
    tk.Label(nova, text=f"Esta é a página de {titulo}", font=('Helvetica', 14)).pack(pady=40)

# Configuração da janela principal
root = tk.Tk()
root.title("Interface Principal")
root.geometry("400x400")

# Carregar imagem de fundo
bg_image = Image.open("C:\\Users\\peter\\OneDrive\\Documentos\\programação\\PAV\\hotel2_Atual\\gui\\login_sistema\\THEME_HOTEL_SIGN_FIVE_STARS_FACADE_BUILDING_GettyImages-1320779330-3-1640x1312.jpg")
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
    ("Cliente", abrir_cliente),
    ("Hóspede", abrir_hospede),
    ("Reserva", abrir_reserva),
    ("Promoção", abrir_promocao),
    ("Tarifa", abrir_tarifa),
    ("Serviços Adicionais", abrir_servicos_adicionais),
    ("Quarto", abrir_quarto),
    ("Feedback", abrir_feedback)
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
        comando()

listbox.bind("<<ListboxSelect>>", on_select)

# Iniciar o loop principal
root.mainloop()
