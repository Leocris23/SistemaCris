import customtkinter as ctk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime
from src.modulo1.entidades import Enfermedad, Medicamento, Paciente
from src.modulo1.fecha.Datos import DatoUsuario
import tkinter.messagebox as messagebox



ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

class interfaz_customtkinter(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("SintomaApp - Registro de Enfermedad y Medicamentos")
        self.geometry("800x600")

        self.Datos = DatoUsuario()
        self.Datos.cargar_datos()

        self.tab_view = ctk.CTkTabview(self)
        self.tab_view.pack(fill="both", expand=True, padx=20, pady=20)
        self.tab_view.add("Pacientes")
        self.tab_view.add("Enfermedad")
        self.tab_view.add("Medicamento")
        self.tab_view.add("Registros")
        self.interfaz_pacientes()
        self.interfaz_enfermedad()
        self.interfaz_medicamento()
        self.interfaz_registro()

    def interfaz_pacientes(self):
        frame = ctk.CTkFrame(self.tab_view.tab("Pacientes"))
        frame.pack(fill="both", expand=True, padx=20, pady=20)
        label = ctk.CTkLabel(frame, text="Agregar Paciente", font=ctk.CTkFont(size=16, weight="bold"))
        label.pack(pady=(10,5))
        self.entry_paciente = ctk.CTkEntry(frame, placeholder_text="Nombre del paciente")
        self.entry_paciente.pack(pady=(5,10))
        self.boton_agregar = ctk.CTkButton(frame, text="Agregar Paciente", command=self.agregar_paciente)
        self.boton_agregar.pack(pady=10)

    def interfaz_enfermedad(self):
        frame = ctk.CTkFrame(self.tab_view.tab("Enfermedad"))
        frame.pack(fill="both", expand=True, padx=20, pady=20)
        label = ctk.CTkLabel(frame, text= "Registrar Enfermedad", font=ctk.CTkFont(size=16, weight="bold"))
        label.pack(pady=(10,5))

        self.combo_paciente_enfermedad = ctk.CTkComboBox(frame, values=[p.nombre for p in self.Datos.paciente])
        self.combo_paciente_enfermedad.pack(pady=(5,10))
        self.date_enfermedad = DateEntry(frame, width=12, background='darkblue', foreground='white', bordewidth=2)
        self.date_enfermedad.pack(pady=(5,10))
        time_frame = ctk.CTkFrame(frame)
        time_frame.pack(pady=(5,10))
        self.hora_enfermedad = ctk.CTkEntry(time_frame, width=50, placeholder_text="HH")
        self.hora_enfermedad.grid(row=0, column=0, padx=(0,5))
        self.minuto_enfermedad = ctk.CTkEntry(time_frame, width=50, placeholder_text="MM")
        self.minuto_enfermedad.grid(row=0, column=1)
        self.entry_enfermedad = ctk.CTkEntry(frame, placeholder_text="Enfermedad")
        self.entry_enfermedad.pack(pady=(5,10))
        self.entry_detalle_enfermedad = ctk.CTkEntry(frame, placeholder_text="Detalle")
        self.entry_detalle_enfermedad.pack(pady=(5,10))
        boton = ctk.CTkButton(frame, text="Registrar Enfermedad", command=self.registrar_enfermedad)
        boton.pack(pady=(5,10))

    def interfaz_medicamento(self):
        frame = ctk.CTkFrame(self.tab_view.tab("Medicamento"))
        frame.pack(fill="both", expand=True, padx=20, pady=20)
        label = ctk.CTkLabel(frame, text="Registrar Medicamento", font=ctk.CTkFont(size=16, weight="bold"))
        label.pack(pady=(10, 5))
        self.combo_paciente_medicamento = ctk.CTkComboBox(frame, values=[p.nombre for p in self.Datos.paciente])
        self.combo_paciente_medicamento.set("Selecciona el paciente")
        self.combo_paciente_medicamento.pack(pady=(5, 10))
        self.date_medicamento = DateEntry(frame, width=12, background='darkblue', foreground='white', bordewidth=2)
        self.date_medicamento.pack(pady=(5, 10))
        time_frame = ctk.CTkFrame(frame)
        time_frame.pack(pady=(5, 10))
        self.hora_medicamento = ctk.CTkEntry(time_frame, width=50, placeholder_text="HH")
        self.hora_medicamento.grid(row=0, column=0, padx=(0, 5))
        self.minuto_medicamento = ctk.CTkEntry(time_frame, width=50, placeholder_text="MM")
        self.minuto_medicamento.grid(row=0, column=1)
        self.entry_medicamento = ctk.CTkEntry(frame, placeholder_text="Medicamento")
        self.entry_medicamento.pack(pady=(5, 10))
        self.entry_detalle_medicamento = ctk.CTkEntry(frame, placeholder_text="Detalle")
        self.entry_detalle_medicamento.pack(pady=(5, 10))
        boton = ctk.CTkButton(frame, text="Registrar Medicamento", command=self.registrar_medicamento)
        boton.pack(pady=(5, 10))

    def interfaz_registro(self):
        frame = ctk.CTkFrame(self.tab_view.tab("Registros"))
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        label_titulo = ctk.CTkLabel(frame, text="Registro de Pacientes")
        label_titulo.pack(pady=10)
        self.valor_paciente_seleccionado = ""

        def imprimir_seleccion(valor):
            self.valor_paciente_seleccionado = valor
            self.actualizar_tabla_pacientes()

        self.combo_paciente_registro = ctk.CTkComboBox(frame, values=[], command=imprimir_seleccion)
        self.combo_paciente_registro.pack(pady=10)

        self.actualizar_combos_pacientes()

        columns = ("nombre", "fecha", "hora", "enfermedad", "medicamento", "detalle")
        self.tabla_pacientes = ttk.Treeview(frame, columns=columns, show="headings")
        self.tabla_pacientes.pack(fill="both", expand=True, pady=10)

        self.tabla_pacientes.heading("nombre", text="Nombre")
        self.tabla_pacientes.heading("fecha", text="Fecha")
        self.tabla_pacientes.heading("hora", text="Hora")
        self.tabla_pacientes.heading("enfermedad", text="Enfermedad")
        self.tabla_pacientes.heading("medicamento", text="Medicamento")
        self.tabla_pacientes.heading("detalle", text="Detalle")

        for col in columns:
            self.tabla_pacientes.column(col, width=100)

        self.actualizar_tabla_pacientes()

    def actualizar_tabla_pacientes(self):
        for row in self.tabla_pacientes.get_children():
            self.tabla_pacientes.delete(row)

        for enfermedad in self.Datos.enfermedad:
            if enfermedad.paciente == self.valor_paciente_seleccionado:
                for medicamento in self.Datos.medicamento:
                    if medicamento.paciente == self.valor_paciente_seleccionado:
                        self.tabla_pacientes.insert("", "end",
                                        values=(enfermedad.paciente, enfermedad.fecha, enfermedad.hora,enfermedad.enfermedad,medicamento.medicamento, enfermedad.detalle))

    def agregar_paciente(self):

        nombre = self.entry_paciente.get()

        if nombre:
            paciente = Paciente(nombre)
            print(f"Paciente creado: {paciente.nombre}")
            self.Datos.agregar_paciente(paciente)
            self.actualizar_combos_pacientes()
            self.entry_paciente.delete(0, ctk.END)
            self.mostrar_mensaje("Bien", f"Paciente {nombre} agregado correctamente")
            self.Datos.guardar_datos()
        else:
            self.mostrar_mensaje("Mal", "Por favor, ingrese el nombre del paciente")

    def registrar_enfermedad(self):
        paciente = self.combo_paciente_enfermedad.get()
        print(paciente)
        fecha = self.date_enfermedad.get_date().strftime("%Y-%m-%d")
        hora = f"{self.hora_enfermedad.get()}:{self.minuto_enfermedad.get()}"
        enfermedad = self.entry_enfermedad.get()
        detalle = self.entry_detalle_enfermedad.get()
        if paciente and enfermedad:
            nueva_enfermedad = Enfermedad(fecha, hora, paciente, enfermedad, detalle)
            print(nueva_enfermedad)
            self.Datos.agregar_enfermedad(nueva_enfermedad)
            self.limpiar_campos_enfermedad()
            self.mostrar_mensaje("Bien", "Enfermedad registrado correctamente")
            self.Datos.guardar_datos()
        else:
            self.mostrar_mensaje("Mal", "Por favor, complete todos los campos requeridos")

    def registrar_medicamento(self):
        paciente = self.combo_paciente_medicamento.get()
        fecha = self.date_medicamento.get_date().strftime("%Y-%m-%d")
        hora = f"{self.hora_medicamento.get()}:{self.minuto_medicamento.get()}"
        medicamento = self.entry_medicamento.get()
        detalle = self.entry_detalle_medicamento.get()
        if paciente and medicamento:
            nuevo_medicamento = Medicamento(fecha, hora, paciente, medicamento, detalle)
            self.Datos.agregar_medicamento(nuevo_medicamento)
            self.limpiar_campos_medicamento()
            self.mostrar_mensaje("Bien", "Medicamento registrado correctamente")
            self.Datos.guardar_datos()
        else:
            self.mostrar_mensaje("Mal", "Por favor, complete todos los campos requeridos")

    def actualizar_combos_pacientes(self):
        pacientes = [p.nombre for p in self.Datos.paciente]
        self.combo_paciente_enfermedad.configure(values=pacientes)
        self.combo_paciente_medicamento.configure(values=pacientes)
        self.combo_paciente_registro.configure(values=pacientes)

    def limpiar_campos_enfermedad(self):
        self.combo_paciente_enfermedad.set("Seleccionar paciente")
        self.entry_enfermedad.delete(0, ctk.END)
        self.entry_detalle_enfermedad.delete(0, ctk.END)

    def limpiar_campos_medicamento(self):
        self.combo_paciente_medicamento.set("Seleccionar paciente")
        self.entry_medicamento.delete(0, ctk.END)
        self.entry_detalle_medicamento.delete(0, ctk.END)

    def mostrar_mensaje(self, titulo, mensaje):
        messagebox.showinfo(title=titulo, message=mensaje)