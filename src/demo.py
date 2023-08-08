import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from agent_a import Agent_A
from agent_maria import Agent_Maria
from bce import BCE
from need import Need
from generator import Generator
import random

LEN_DEGREE=4

bce_sensaciones_biologicas = [
            ("Relajación", BCE(Need(0, 1), Need(0, 1), Need(0, 1))),
            ("Hambre", BCE(Need(1, 1), Need(0, 0), Need(1, 1))),
            ("Sueño", BCE(Need(1, 1), Need(1, 1), Need(1, 1)))
        ]

bce_sensaciones_culturales = [


            ("Nostalgia", BCE(Need(0, 0), Need(1, 1), Need(1, 1))),
            ("Ignorancia", BCE(Need(0, 0), Need(1, 2), Need(1, 1))),
            ("Estres", BCE(Need(1, 1), Need(1, 3), Need(1, 2)))
        ]

bce_sensaciones_emocionales = [
            ("Felicidad", BCE(Need(0, 1), Need(0, 0), Need(0, 1))),
            ("Amor", BCE(Need(0, 1), Need(0, 0), Need(0, 1))),
            ("Tristeza", BCE(Need(1, 1), Need(0, 1), Need(1, 1))),
            ("Ira", BCE(Need(1, 1), Need(0, 0), Need(1, 2))),

        ]

bce_time = [
            ("Hora_de_comer", BCE(Need(1, 2), Need(0, 0), Need(0, 0))),
            ("Hora_de_estudiar", BCE(Need(0, 0), Need(1, 1), Need(0, 0))),
            ("Hora_de_disfrutar", BCE(Need(1, 1), Need(1, 1), Need(1, 2))),
            ("neutro", BCE(Need(0, 0), Need(0, 0), Need(0, 0)))
        ]

tup_BIO = [
    ("Muerte corporal_B", BCE(Need(1, 3), Need(1, 0), Need(1, 0))),
    ("Enfermedad corporal_B", BCE(Need(1, 3), Need(0, 0), Need(1, 0))),
    ("Ansiedad corporal_B", BCE(Need(1, 2), Need(0, 0), Need(0, 0))),
    ("Incomodidad_B", BCE(Need(1, 1), Need(0, 0), Need(0, 2))),
    ("Menos incomodidad_B", BCE(Need(1, 0), Need(0, 0), Need(0, 0))),
    ("Menos comodidad_B", BCE(Need(0, 0), Need(0, 0), Need(0, 0))),
    ("Comodidad_B", BCE(Need(0, 1), Need(0, 0), Need(0, 1))),
    ("Ansiedad mental_B", BCE(Need(0, 2), Need(0, 0), Need(0, 0))),
    ("Enfermedad mental_B", BCE(Need(0, 3), Need(1, 1), Need(0, 1))),
    ("Muerte Mental_B", BCE(Need(0, 3), Need(1, 1), Need(1, 1)))
]

# Tuplas de tuplas para Cultural
tup_CUL = [
    ("Muerte Vegetativo_C", BCE(Need(0, 0), Need(1, 3), Need(1, 1))),
    ("Ignorante_C", BCE(Need(0, 0), Need(1, 3), Need(0, 0))),
    ("Torpe_C", BCE(Need(0, 0), Need(1, 2), Need(0, 0))),
    ("Inseguro_C", BCE(Need(0, 0), Need(1, 1), Need(0, 0))),
    ("Menos inseguro_C", BCE(Need(0, 0), Need(1, 0), Need(0, 0))),
    ("Menos seguro_C", BCE(Need(0, 0), Need(0, 0), Need(0, 0))),
    ("Seguro_C", BCE(Need(0, 0), Need(0, 1), Need(0, 0))),
    ("Soberbia_C", BCE(Need(0, 0), Need(0, 2), Need(0, 0))),
    ("Delirio_C", BCE(Need(0, 0), Need(0, 3), Need(0, 0))),
    ("Muerte Mental_C", BCE(Need(0, 0), Need(0, 3), Need(0, 0)))
]

# Tuplas de tuplas para Emocional
tup_EMO = [
    ("Muerte corporal_E", BCE(Need(1, 1), Need(1, 1), Need(1, 3))),
    ("Depresivo corporal_E", BCE(Need(0, 0), Need(0, 0), Need(1, 3))),
    ("Agitado corporal_E", BCE(Need(0, 0), Need(0, 0), Need(1, 2))),
    ("Triste_E", BCE(Need(0, 0), Need(0, 0), Need(1, 1))),
    ("Menos triste_E", BCE(Need(0, 0), Need(0, 0), Need(1, 0))),
    ("Menos alegre_E", BCE(Need(0, 0), Need(0, 0), Need(0, 0))),
    ("Alegre_E", BCE(Need(0, 0), Need(0, 0), Need(0, 1))),
    ("Eufórico mental_E", BCE(Need(0, 0), Need(0, 0), Need(0, 2))),
    ("Maniaco mental_E", BCE(Need(0, 0), Need(0, 0), Need(0, 3))),
    ("Muerte Mental_E", BCE(Need(0, 0), Need(0, 0), Need(0, 3)))
]

arr_patternes_bce_sight=bce_sensaciones_biologicas+bce_sensaciones_culturales+bce_sensaciones_emocionales+tup_BIO+tup_CUL+tup_EMO
arr_patternes_bce_hearing=bce_sensaciones_biologicas+bce_sensaciones_culturales+bce_sensaciones_emocionales+tup_BIO+tup_CUL+tup_EMO
arr_patternes_bce_smell=bce_sensaciones_biologicas+bce_sensaciones_culturales+bce_sensaciones_emocionales+tup_BIO+tup_CUL+tup_EMO
arr_patternes_bce_taste=bce_sensaciones_biologicas+bce_sensaciones_culturales+bce_sensaciones_emocionales+tup_BIO+tup_CUL+tup_EMO
arr_patternes_bce_touch=bce_sensaciones_biologicas+bce_sensaciones_culturales+bce_sensaciones_emocionales+tup_BIO+tup_CUL+tup_EMO
arr_patternes_bce_body=bce_sensaciones_biologicas+bce_sensaciones_culturales+bce_sensaciones_emocionales+tup_BIO+tup_CUL+tup_EMO
arr_patternes_bce_time=bce_time+tup_EMO+tup_CUL+tup_BIO


arr_patternes_bce=[arr_patternes_bce_sight,arr_patternes_bce_hearing,arr_patternes_bce_smell,arr_patternes_bce_taste,arr_patternes_bce_touch,arr_patternes_bce_body,arr_patternes_bce_time]

# def get_all_items(tree, parent_item=''):
#     all_items = set()
#     for item in tree.get_children(parent_item):
#         all_items.add(tree.item(item)['text'])
#         all_items.update(get_all_items(tree, item))  # Llamada recursiva para buscar hijos
#     return all_items

def get_all_items(tree, parent_item=''):
    all_items = set()
    for item in tree.get_children(parent_item):
        item_text = tree.item(item)['text']
        children = tree.get_children(item)
        if not children:  # Verificar si el nodo no tiene hijos (es una hoja)
            all_items.add(item_text)  # Agregar el nodo a la lista de nodos hoja
        all_items.update(get_all_items(tree, item))  # Llamada recursiva para buscar en los hijos
    return all_items


def find_item_with_text(text, tree, parent_item=''):
    # Iterar a través de todos los elementos en el árbol bajo el nodo padre dado
    for item in tree.get_children(parent_item):
        # Obtener el texto del elemento
        item_text = tree.item(item, 'text').strip()
        # Comprobar si el texto coincide con lo que estamos buscando
        if item_text == text:
            return item
        # Llamada recursiva para buscar en los hijos del elemento actual
        found_item = find_item_with_text(text, tree, item)
        if found_item is not None:
            return found_item
    return None


agent_maria= Agent_Maria()
agent = Agent_A()
gen = Generator()
#all_patterns=[]
agent = Agent_A()

agent.rn_senses.init_patterns(arr_patternes_bce)

all_patterns= agent.rn_senses.status()

print(agent.status_ai_bce())

# Función para agregar el contenido de los campos de entrada al árbol
def add_to_tree_auto():
    all_patterns=agent.rn_senses.status()

    for i, tree in enumerate(tree_list):
        added_roots=list_added_roots[i]
        added_parents=list_added_parents[i]

        for pattern, id_bce in all_patterns[i].items():
            neuron_id = id_bce[0]
            bce = id_bce[1]

            root_text = str(neuron_id)
            if root_text:
                if root_text not in added_roots and root_text not in added_parents:
                    root_id = tree.insert("", "end", text=root_text)
                    added_roots.add(root_text)
            

            child_text = pattern

            if child_text:
                if child_text not in added_parents:
                    tree_id=find_item_with_text(root_text, tree)
                    if tree_id:
                        tree.insert(tree_id, "end", text=child_text)
                        added_parents.add(child_text)
        

            update_combobox(tree)
        tree.see(tree.get_children()[-1])

        #print(element_entries[i]['values'][0])
        element_entries[i].set(element_entries[i]['values'][random.randint(0, len(element_entries[i]['values']) - 1)])

def expand_all_items(tree, parent_item=''):
    for item in tree.get_children(parent_item):
        tree.item(item, open=True)
        expand_all_items(tree, item)

# Función para agregar el contenido de los campos de entrada al árbol
def add_to_tree():
    for i, tree in enumerate(tree_list):
        added_roots=list_added_roots[i]
        added_parents=list_added_parents[i]

        root_text = element_entries[i].get().strip()
        #print(root_text)
        if root_text:
            if root_text not in added_roots and root_text not in added_parents:
                root_id = tree.insert("", "end", text=root_text)
                added_roots.add(root_text)
        

        child_text = subelement_entries[i].get().strip()

        if child_text:
            if child_text not in added_parents:
                tree_id=find_item_with_text(root_text, tree)
                if tree_id:
                    tree.insert(tree_id, "end", text=child_text)
                    added_parents.add(child_text)
        
        update_combobox(tree)
        expand_all_items(tree)

def mostrar_mensaje_terminado():
    messagebox.showinfo("Terminado", "El agente ha llegado a un estado final")


def next():

    #all_patterns = agent.rn_senses.status()
    for entry in subelement_entries:
        if entry.get().strip() == "":
            messagebox.showwarning("Campos Incompletos de Eventos", "Falta llenar uno o más campos de los eventos.")
            return

   # Verificar si algún Entry está vacío
    for entry in element_entries:
        if entry.get().strip() == "":
            messagebox.showwarning("Campos Incompletos Patrones", "Falta llenar uno o más campos de los patrones.")
            return

    
    evento_sensorial=[]
    for i, tree in enumerate(tree_list):
        
        pattern = element_entries[i].get().strip()
        event = subelement_entries[i].get().strip()
        evento_sensorial.append(pattern+":"+event)

    #print(evento_sensorial)
    agent.set_event(evento_sensorial)
    #agent.set_event(gen.gen_event())
    arr_bce = agent_maria.comparator(agent.status_ai_bce())
    bce_7 = agent.update_neuron(arr_bce)

    #Aqui estan los BCE
    for i, tree in enumerate(tree_list):
        bce_entrys[i].config(state="normal")
        bce_entrys[i].delete(0, tk.END)
        bce_entrys[i].insert(0, bce_7[i][0])
        bce_entrys[i].config(state="readonly")

        subelement_entries[i].delete(0, tk.END)
        subelement_entries[i].insert(tk.END, "Evento"+str(random.randint(0, 10)))


    

    print(agent_maria.general_evaluator_bce(bce_7)[0][0])
    bce_to_add = agent_maria.general_evaluator_bce(bce_7)[0][0][1]
    bce_entry_2.config(state="normal")
    bce_entry_2.delete(0, tk.END)
    bce_entry_2.insert(0, bce_to_add)
    bce_entry_2.config(state="readonly")

    agent.update_bce(bce_to_add)
    update_entry_text()
    for factor in agent.status_ai_bce().state():
        if factor[1] == LEN_DEGREE:
            print("DEAD") 
            mostrar_mensaje_terminado()  

    add_to_tree_auto()

def reset_combobox(tree):
    for i, tree in enumerate(tree_list):
        element_entries[i].set("")
        element_entries[i]['values']=[]
        


def update_combobox(tree):

    for i, tree in enumerate(tree_list):
        all_items = get_all_items(tree)
        element_entries[i]['values'] = list(all_items)
        


    #for i, tree in enumerate(tree_list):
    #    element_entries[i]['values'] = list(all_items_tree)  

def update_combobox_tree(event, tree, combobox):
    item = tree.focus()
    if item:
        item_text = tree.item(item, "text")
        combobox.set(item_text)
        


def update_entry_text():

    entry_actual.config(state="normal")
    entry_anterior.config(state="normal")
    current_text = entry_actual.get()

    new_text = agent.status_ai_bce()  # Texto que quieres establecer en el Entry
    entry_anterior.delete(0, tk.END)  # Eliminar todo el texto actual del Entry
    entry_anterior.insert(0, current_text)  # Insertar el nuevo texto al inicio del Entry

    entry_actual.delete(0, tk.END)  # Eliminar todo el texto actual del Entry
    entry_actual.insert(0, new_text)  # Insertar el nuevo texto al inicio del Entry

    entry_actual.config(state="readonly")
    entry_anterior.config(state="readonly")


# Crear ventana
window = tk.Tk()
window.title("Demo Módulo A")

tree_list = []

# Lista de nombres de header
header_names = ["sight", "hearing", "smell", "taste", "touch", "body", "time"]

# Agregar campos de entrada para elementos principales y subelementos
element_entries = []
subelement_entries = []

bce_entrys = []

list_added_roots = []
list_added_parents = []
# Crear 7 árboles y colocarlos uno al lado del otro
for i in range(7):
    tree = ttk.Treeview(window)
    tree.grid(row=0, column=i+1, padx=5, pady=5)
    tree.heading("#0", text=header_names[i], anchor=tk.W)

    # Guardar el identificador del árbol en la lista
    tree_list.append(tree)

    list_added_roots.append(set())
    list_added_parents.append(set())

    tree.bind("<<TreeviewSelect>>", lambda event, index=i: update_combobox_tree(event, tree_list[index], element_entries[index]))

# Conjuntos para realizar seguimiento de elementos agregados
#added_roots = set()
#added_parents = set()



#label
tk.Label(window, text="Patterns:").grid(row=2, column=0, padx=5, pady=2, sticky="w")
for i in range(7):
    combo_sensations  = ttk.Combobox(window, values=[""])
    combo_sensations.grid(row=2, column=i+1, padx=5, pady=2, sticky="w")
    element_entries.append(combo_sensations)
    
#label
tk.Label(window, text="Events:").grid(row=3+2, column=0, padx=5, pady=2, sticky="w")
tk.Label(window, text="BCE:").grid(row=3+3, column=0, padx=5, pady=2, sticky="w")
for i in range(7):
    entry = tk.Entry(window)
    bce_entry=tk.Entry(window,width=30)
    entry.insert(tk.END, "Evento"+str(i+1))
    entry.grid(row=3+2, column=i+1, padx=5, pady=2, sticky="w")
    bce_entry.grid(row=3+3, column=i+1, padx=5, pady=2, sticky="w")
    subelement_entries.append(entry)
    bce_entrys.append(bce_entry)


# Etiqueta y campo para el estado actual
label_actual = tk.Label(window, text="Actual state:")
label_actual.grid(row=10+2, column=2, padx=5, pady=5, sticky=tk.E)

entry_actual = tk.Entry(window, state="readonly",width=50)
entry_actual.grid(row=10+2, column=3, padx=12, pady=5, sticky=tk.W)

# Etiqueta y campo para el estado anterior
label_anterior = tk.Label(window, text="Previous state:")
label_anterior.grid(row=9+2, column=2, padx=5, pady=5, sticky=tk.E)

entry_anterior = tk.Entry(window, state="readonly",width=50)
entry_anterior.grid(row=9+2, column=3, padx=12, pady=5, sticky=tk.W)

bce_label = tk.Label(window, text="BCE Ganador:")
bce_label.grid(row=9+5, column=2, padx=5, pady=5, sticky=tk.E)

bce_entry_2 = tk.Entry(window, state="readonly",width=50)
bce_entry_2.grid(row=9+5, column=3, padx=12, pady=5, sticky=tk.W)



# Agregar botón "Agregar al Árbol"
add_button = tk.Button(window, text="Add", command=next)
add_button.grid(row=9+2, column=0, columnspan=2, padx=10, pady=10)

def reset_tree():
    for i, tree in enumerate(tree_list):
        added_roots=list_added_roots[i]
        added_parents=list_added_parents[i]
        tree.delete(*tree.get_children())
        added_roots.clear()
        added_parents.clear()
        reset_combobox(tree)
    agent.ai_bce.reset()
    agent.reset()
    agent.rn_senses.init_patterns(arr_patternes_bce)
    #print(len(agent.rn_senses.status()[1]))
    #agent.reset()
    update_entry_text()
    add_to_tree_auto()
    for i, tree in enumerate(tree_list):
        expand_all_items(tree)
    lambda event, index=i: update_combobox_tree(event, tree_list[index], element_entries[index])
    
    

# Resetear arbol
reset_button = tk.Button(window, text="Reset", command=reset_tree)
reset_button.grid(row=10+2, column=0, columnspan=2, padx=10, pady=10)


#add_to_tree_auto()
for i, tree in enumerate(tree_list):
    expand_all_items(tree)
update_entry_text()

# Ejecutar la interfaz gráfica
window.mainloop()
