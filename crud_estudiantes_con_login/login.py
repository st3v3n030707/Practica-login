import pwinput  # Se importa la librería 'pwinput', que permite ocultar la contraseña al escribirla (como con asteriscos).

# Función que carga los usuarios y contraseñas desde un archivo de texto
def cargar_usuarios():
    usuarios = {}  # Se crea un diccionario vacío para almacenar los usuarios y sus contraseñas.
    try:
        # Se intenta abrir el archivo 'usuarios.txt' en modo lectura.
        with open("usuarios.txt", "r") as archivo:
            # Se recorre cada línea del archivo.
            for linea in archivo:
                # Se eliminan espacios en blanco y saltos de línea, y se separa la línea por comas.
                partes = linea.strip().split(",")
                # Si hay exactamente dos elementos (usuario y contraseña), se agregan al diccionario.
                if len(partes) == 2:
                    usuarios[partes[0]] = partes[1]
    except FileNotFoundError:
        # Si el archivo no se encuentra, se muestra un mensaje de advertencia.
        print("Archivo de usuarios no encontrado.")
    return usuarios  # Se devuelve el diccionario con los usuarios cargados.

# Función que permite iniciar sesión
def iniciar_sesion():
    usuarios = cargar_usuarios()  # Se cargan los usuarios desde el archivo.
    intentos = 3  # Se permite un máximo de 3 intentos para iniciar sesión.
    
    # Mientras queden intentos disponibles:
    while intentos > 0:
        usuario = input("Usuario: ")  # Se solicita el nombre de usuario por consola.
        # Se solicita la contraseña, ocultando los caracteres con asteriscos.
        contraseña = pwinput.pwinput(prompt="Contraseña: ", mask="*")
        
        # Se verifica si el usuario existe y si la contraseña es correcta.
        if usuario in usuarios and usuarios[usuario] == contraseña:
            print("\nAcceso concedido.\n")  # Si los datos son correctos, se permite el acceso.
            return True  # Finaliza la función con éxito.
        else:
            # Si los datos son incorrectos, se resta un intento y se informa al usuario.
            intentos -= 1
            print(f"El usuario o la contraseña son incorrectos, le quedan los siguientes intentos: {intentos}")
    
    # Si se agotan los intentos, se niega el acceso.
    print("Acceso denegado, realizo demasiados intentos")
    return False  # Finaliza la función indicando que no se pudo iniciar sesión.