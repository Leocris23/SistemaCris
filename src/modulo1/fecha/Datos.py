import json
from src.modulo1.entidades import Paciente, Enfermedad, Medicamento

class DatoUsuario:
    def __init__(self):
        self.enfermedad = []
        self.medicamento = []
        self.paciente = []

    def agregar_enfermedad(self, enfermedad):
        self.enfermedad.append(enfermedad)

    def agregar_medicamento(self, medicamento):
        self.medicamento.append(medicamento)

    def agregar_paciente(self, paciente):
        self.paciente.append(paciente)

    def guardar_datos(self):
        pacientes_dato = [p.__dict__ for p in self.paciente]
        enfermedad_dato = [e.__dict__ for e in self.enfermedad]
        medicamento_dato = [m.__dict__ for m in self.medicamento]

        with open("datos.json","w") as f:
            json.dump({
                "pacientes": pacientes_dato,
                "enfermedad": enfermedad_dato,
                "medicamento": medicamento_dato

            }, f)

    def cargar_datos(self):
        try:
            with open("datos.json","r") as f:
                datos = json.load(f)
            self.paciente = [Paciente(**p) for p in datos["pacientes"]]
            self.enfermedad = [Enfermedad(**e) for e in datos["enfermedad"]]
            self.medicamento = [Medicamento(**m) for m in datos["medicamento"]]
        except FileNotFoundError:
            pass