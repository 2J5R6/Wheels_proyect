# clases.py

class Usuario:
    def __init__(self, id, nombre, correo_institucional, foto, contraseña):
        self.id = id
        self.nombre = nombre
        self.correo_institucional = correo_institucional
        self.foto = foto
        self.contraseña = contraseña
        self.ubicacion_actual = None

class Conductor(Usuario):
    def __init__(self, id, nombre, correo_institucional, foto, contraseña, foto_carro, placa):
        super().__init__(id, nombre, correo_institucional, foto, contraseña)
        self.foto_carro = foto_carro
        self.placa = placa
        self.calificacion_promedio = 0
        self.rutas_ofrecidas = []

    def ofrecer_ruta(self, ruta):
        self.rutas_ofrecidas.append(ruta)

class Ruta:
    def __init__(self, id, conductor, origen, destino, horario):
        self.id = id
        self.conductor = conductor
        self.origen = origen
        self.destino = destino
        self.horario = horario
        self.cupos_disponibles = 0
        self.estudiantes = []

    def reservar_puesto(self, estudiante):
        if self.cupos_disponibles > 0:
            self.estudiantes.append(estudiante)
            self.cupos_disponibles -= 1

class Notificacion:
    def __init__(self, id, usuario_destino, mensaje, tipo):
        self.id = id
        self.usuario_destino = usuario_destino
        self.mensaje = mensaje
        self.tipo = tipo

    def enviar(self):
        pass

class Calificacion:
    def __init__(self, id, conductor, estudiante, puntuacion, comentario):
        self.id = id
        self.conductor = conductor
        self.estudiante = estudiante
        self.puntuacion = puntuacion
        self.comentario = comentario
