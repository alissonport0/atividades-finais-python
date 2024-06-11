import tkinter as tk

def add_task():
    task = entry_task.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        entry_task.delete(0, tk.END)

def remove_task():
    try:
        selected_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_index)
    except IndexError:
        pass

def main():
    root = tk.Tk()
    root.title("Lista de Tarefas")

    tk.Label(root, text="Tarefa:").grid(row=0, column=0, padx=10, pady=5)
    entry_task = tk.Entry(root)
    entry_task.grid(row=0, column=1, padx=10, pady=5)

    tk.Button(root, text="Adicionar Tarefa", command=add_task).grid(row=0, column=2, padx=10, pady=5)
    tasks_listbox = tk.Listbox(root)
    tasks_listbox.grid(row=1, columnspan=3, padx=10, pady=5)

    tk.Button(root, text="Remover Tarefa", command=remove_task).grid(row=2, columnspan=3, padx=10, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
