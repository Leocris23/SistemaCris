class Enfermedad:
    def __init__(self, fecha, hora, paciente, enfermedad, detalle):
        self.fecha = fecha
        self.hora = hora
        self.paciente = paciente
        self.enfermedad = enfermedad
        self.detalle = detalle

    def __str__(self):
        return f"{self.fecha} {self.hora} - {self.paciente}: {self.enfermedad} ({self.detalle})"