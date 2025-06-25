import pwinput

def cargar_usuarios():
    usuarios = {}
    try:
        with open("usuarios.txt", "r") as archivo:
            for linea in archivo:
                partes = linea.strip().split(",")
                if len(partes) == 2:
                    usuarios[partes[0]] = partes[1]
    except FileNotFoundError:
        print("Archivo de usuarios no encontrado.")
    return usuarios

def iniciar_sesion():
    usuarios = cargar_usuarios()
    intentos = 3
    while intentos > 0:
        usuario = input("Usuario: ")
        contraseña = pwinput.pwinput(prompt="Contraseña: ", mask="*")
        
        if usuario in usuarios and usuarios[usuario] == contraseña:
            print("\n Acceso concedido.\n")
            return True
        else:
            intentos -= 1
            print(f" Usuario o contraseña incorrecta. Intentos restantes: {intentos}")
    
    print(" Acceso denegado. Demasiados intentos.")
    return False
