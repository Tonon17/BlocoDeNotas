import tkinter as tk
from tkinter import filedialog, messagebox

class BlocoDeNotas:
  def __init__(self,root):
    self.root = root
    self.root.title("Bloco de Notas")
    self.root.geometry("800x600")

    self.text_area = tk.Text(self.root, wrap='word', font = ('Arial', 12))
    self.text_area.pack(expand=True,fill='both')

    self.menu_bar = tk.Menu(self.root)
    self.root.config(menu=self.menu_bar)

    self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
    self.menu_bar.add_cascade (label = "Arquivo", menu=self.file_menu)
    self.file_menu.add_command(label="Novo", command=self.novo_arquivo)
    self.file_menu.add_command(label="Abrir", command=self.abrir_arquivo)
    self.file_menu.add_command(label="Salvar",command=self.salvar_arquivo)
    self.file_menu.add_separator()
    self.file_menu.add_command(label="Sair", command=self.root.quit)

  def novo_arquivo(self):
    self.text_area.delete(1.0, tk.END)
  def abrir_arquivo(self):
    arquivo_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Todos os arquivos","*.*"), ("Arquivos de texto", "*.txt")])
    if arquivo_path:
      try:
        with open(arquivo_path, "r") as file:
          self.text_area.delete(1.0, tk.END)
          self.text_area.insert(tk.END, file.read())
      except Exception as e:
        messagebox.showerror("Error", e)
  def salvar_arquivo(salvar):
    arquivo_path = filedialog.asksaveasfilename(defaultextension = ".txt", filetypes = [("Todos os arquivos", "*.*"), ("Arquivos de texto", "*.txt")])
    

if __name__ =="__main__":
  root = tk.Tk()
  app = BlocoDeNotas(root)
  root.mainloop()