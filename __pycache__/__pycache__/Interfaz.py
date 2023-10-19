import tkinter as tk
from tkinter import messagebox, Toplevel, Entry, Label, Button, Listbox, Radiobutton, StringVar
import funcionalidades as func

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Wheels - Inicio de Sesión")

        # Widgets para iniciar sesión
        Label(root, text="Correo Institucional:").pack(pady=10)
        self.entry_email = Entry(root)
        self.entry_email.pack(pady=10)

        Label(root, text="Contraseña:").pack(pady=10)
        self.entry_password = Entry(root, show="*")
        self.entry_password.pack(pady=10)

        Button(root, text="Iniciar Sesión", command=self.iniciar_sesion).pack(pady=20)
        Button(root, text="Registrar", command=self.registrar).pack(pady=10)

    def iniciar_sesion(self):
        email = self.entry_email.get()
        password = self.entry_password.get()
        usuario = func.iniciar_sesion(email, password)
        if usuario:
            self.root.destroy()
            MainApp(usuario)
        else:
            messagebox.showerror("Error", "Correo o contraseña incorrectos.")

    def registrar(self):
        self.registro_ventana = Toplevel(self.root)
        self.registro_ventana.title("Registro")

        Label(self.registro_ventana, text="Nombre:").pack(pady=10)
        self.entry_nombre = Entry(self.registro_ventana)
        self.entry_nombre.pack(pady=10)

        Label(self.registro_ventana, text="Correo Institucional:").pack(pady=10)
        self.entry_email_registro = Entry(self.registro_ventana)
        self.entry_email_registro.pack(pady=10)

        Label(self.registro_ventana, text="Contraseña:").pack(pady=10)
        self.entry_password_registro = Entry(self.registro_ventana, show="*")
        self.entry_password_registro.pack(pady=10)

        self.tipo_registro = StringVar()
        Radiobutton(self.registro_ventana, text="Usuario", variable=self.tipo_registro, value="usuario").pack(pady=10)
        Radiobutton(self.registro_ventana, text="Conductor", variable=self.tipo_registro, value="conductor").pack(pady=10)

        Button(self.registro_ventana, text="Registrar", command=self.completar_registro).pack(pady=20)

    def completar_registro(self):
        nombre = self.entry_nombre.get()
        email = self.entry_email_registro.get()
        password = self.entry_password_registro.get()
        tipo = self.tipo_registro.get()
        usuario = func.registrar_conductor_o_usuario(tipo, len(func.usuarios_registrados)+1, nombre, email, None, password, None, None)

        if usuario:
            messagebox.showinfo("Éxito", f"{tipo.capitalize()} registrado con éxito!")
            self.registro_ventana.destroy()
        else:
            messagebox.showerror("Error", "Error al registrar. Intenta de nuevo.")

class MainApp:
    def __init__(self, usuario):
        self.root = tk.Tk()
        self.usuario = usuario
        self.root.title(f"Wheels - Bienvenido {usuario.nombre}")

        # Botones para acceder a diferentes funcionalidades
        if isinstance(self.usuario, func.Conductor):
            Button(self.root, text="Ofrecer Ruta", command=self.ofrecer_ruta).pack(pady=10)
        else:  # Si es un usuario
            Button(self.root, text="Buscar Ruta", command=self.buscar_ruta).pack(pady=10)
            Button(self.root, text="Reservar Ruta", command=self.reservar_ruta).pack(pady=10)
            Button(self.root, text="Calificar Conductor", command=self.calificar_conductor).pack(pady=10)

        Button(self.root, text="Cerrar Sesión", command=self.cerrar_sesion).pack(pady=20)

        self.root.mainloop()
    
    def ofrecer_ruta(self):
        self.ofrecer_ventana = Toplevel(self.root)
        self.ofrecer_ventana.title("Ofrecer Ruta")

        Label(self.ofrecer_ventana, text="Origen:").pack(pady=10)
        self.entry_origen = Entry(self.ofrecer_ventana)
        self.entry_origen.pack(pady=10)

        Label(self.ofrecer_ventana, text="Destino:").pack(pady=10)
        self.entry_destino = Entry(self.ofrecer_ventana)
        self.entry_destino.pack(pady=10)

        Label(self.ofrecer_ventana, text="Horario:").pack(pady=10)
        self.entry_horario = Entry(self.ofrecer_ventana)
        self.entry_horario.pack(pady=10)

        Label(self.ofrecer_ventana, text="Cupos disponibles:").pack(pady=10)
        self.entry_cupos = Entry(self.ofrecer_ventana)
        self.entry_cupos.pack(pady=10)


        Button(self.ofrecer_ventana, text="Ofrecer", command=self.completar_oferta).pack(pady=20)

    def completar_oferta(self):
        origen = self.entry_origen.get()
        destino = self.entry_destino.get()
        horario = self.entry_horario.get()
        
        try:
            cupos = int(self.entry_cupos.get())
            ruta = func.ofrecer_ruta(self.usuario, origen, destino, horario, cupos)
            messagebox.showinfo("Éxito", "Ruta ofrecida con éxito!")
            self.ofrecer_ventana.destroy()
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce un número válido de cupos.")
        except Exception as e:
            messagebox.showerror("Error", str(e))


    def buscar_ruta(self):
        self.buscar_ventana = Toplevel(self.root)
        self.buscar_ventana.title("Buscar Ruta")

        Label(self.buscar_ventana, text="Origen:").pack(pady=10)
        self.entry_origen_buscar = Entry(self.buscar_ventana)
        self.entry_origen_buscar.pack(pady=10)

        Label(self.buscar_ventana, text="Destino:").pack(pady=10)
        self.entry_destino_buscar = Entry(self.buscar_ventana)
        self.entry_destino_buscar.pack(pady=10)

        Button(self.buscar_ventana, text="Buscar", command=self.completar_busqueda).pack(pady=20)

    def completar_busqueda(self):
        origen = self.entry_origen_buscar.get()
        destino = self.entry_destino_buscar.get()
        rutas = func.buscar_rutas(origen, destino)
        if rutas:
            self.listbox_rutas = Listbox(self.buscar_ventana)
            for ruta in rutas:
                self.listbox_rutas.insert(tk.END, f"Ruta de {ruta.conductor.nombre} - Origen: {ruta.origen} - Destino: {ruta.destino}")
            self.listbox_rutas.pack(pady=20)
        else:
            messagebox.showinfo("Información", "No se encontraron rutas disponibles.")

    def reservar_ruta(self):
        self.reservar_ventana = Toplevel(self.root)
        self.reservar_ventana.title("Reservar Ruta")

        Label(self.reservar_ventana, text="Origen:").pack(pady=10)
        self.entry_origen_reservar = Entry(self.reservar_ventana)
        self.entry_origen_reservar.pack(pady=10)

        Label(self.reservar_ventana, text="Destino:").pack(pady=10)
        self.entry_destino_reservar = Entry(self.reservar_ventana)
        self.entry_destino_reservar.pack(pady=10)

        Button(self.reservar_ventana, text="Reservar", command=self.completar_reserva).pack(pady=20)

    def completar_reserva(self):
        origen = self.entry_origen_reservar.get()
        destino = self.entry_destino_reservar.get()
        ruta = func.reservar_puesto(self.usuario, origen, destino)
        if ruta:
            messagebox.showinfo("Éxito", "Ruta reservada con éxito!")
            self.reservar_ventana.destroy()
        else:
            messagebox.showerror("Error", "No hay rutas disponibles para reservar.")

    def calificar_conductor(self):
        self.calificar_ventana = Toplevel(self.root)
        self.calificar_ventana.title("Calificar Conductor")

        Label(self.calificar_ventana, text="Conductor:").pack(pady=10)
        self.entry_conductor = Entry(self.calificar_ventana)
        self.entry_conductor.pack(pady=10)

        Label(self.calificar_ventana, text="Puntuación (1-5):").pack(pady=10)
        self.entry_puntuacion = Entry(self.calificar_ventana)
        self.entry_puntuacion.pack(pady=10)

        Label(self.calificar_ventana, text="Comentario:").pack(pady=10)
        self.entry_comentario = Entry(self.calificar_ventana)
        self.entry_comentario.pack(pady=10)

        Button(self.calificar_ventana, text="Calificar", command=self.completar_calificacion).pack(pady=20)

    def completar_calificacion(self):
        conductor_nombre = self.entry_conductor.get()
        puntuacion = int(self.entry_puntuacion.get())
        comentario = self.entry_comentario.get()

        conductor = next((user for user in func.usuarios_registrados if isinstance(user, func.Conductor) and user.nombre == conductor_nombre), None)
        if conductor:
            func.calificar_conductor(self.usuario, conductor, puntuacion, comentario)
            messagebox.showinfo("Éxito", "Conductor calificado con éxito!")
            self.calificar_ventana.destroy()
        else:
            messagebox.showerror("Error", "No se encontró el conductor especificado.")

    def cerrar_sesion(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()