from Class import Usuario, Conductor, Ruta, Notificacion, Calificacion

usuarios_registrados = []
rutas_disponibles = []

def registrar_conductor_o_usuario(tipo, id, nombre, correo_institucional, foto, contraseña, foto_carro=None, placa=None):
    if not usuario_existente(correo_institucional):
        if tipo == "conductor":
            usuario = Conductor(id, nombre, correo_institucional, foto, contraseña, foto_carro, placa)
        else:
            usuario = Usuario(id, nombre, correo_institucional, foto, contraseña)
        usuarios_registrados.append(usuario)
        return usuario
    else:
        raise ValueError("El usuario ya está registrado.")

def iniciar_sesion(correo_institucional, contraseña):
    for usuario in usuarios_registrados:
        if usuario.correo_institucional == correo_institucional and usuario.contraseña == contraseña:
            return usuario
    raise ValueError("Correo o contraseña incorrectos.")

def ofrecer_ruta(conductor, origen, destino, horario, cupos):
    ruta = Ruta(len(rutas_disponibles) + 1, conductor, origen, destino, horario)
    ruta.cupos_disponibles = cupos
    rutas_disponibles.append(ruta)
    conductor.ofrecer_ruta(ruta)

def buscar_rutas(origen, destino, horario):
    rutas_encontradas = [ruta for ruta in rutas_disponibles if ruta.origen == origen and ruta.destino == destino and ruta.horario == horario]
    return rutas_encontradas

def reservar_puesto(estudiante, ruta):
    if ruta.cupos_disponibles > 0:
        ruta.reservar_puesto(estudiante)
        return True
    else:
        raise ValueError("No hay cupos disponibles en esta ruta.")

def calificar_conductor(estudiante, conductor, puntuacion, comentario):
    calificacion = Calificacion(len(rutas_disponibles) + 1, conductor, estudiante, puntuacion, comentario)
    conductor.calificacion_promedio = (conductor.calificacion_promedio + puntuacion) / 2
    return calificacion

def usuario_existente(correo_institucional):
    for usuario in usuarios_registrados:
        if usuario.correo_institucional == correo_institucional:
            return True
    return False

def enviar_notificacion(usuario, mensaje, tipo):
    notificacion = Notificacion(len(usuarios_registrados) + 1, usuario, mensaje, tipo)
    notificacion.enviar()
