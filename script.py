from usuario import Usuario

usuarios = []

with open("usuarios.txt", "r") as archivo:
    for linea in archivo:
        usuario = linea.strip().split(",")

        usuario_nombre = usuario[0].replace('{"nombre": ', "")

        usuario_apellido = usuario[1].replace(' "apellido": ', "")

        usuario_email = usuario[2].replace(' "email": ', "")
        usuario_email = usuario_email.replace(' email": ', "")

        usuario_genero = usuario[3].replace(' "genero": ', "")
        usuario_genero = usuario_genero.replace("}", "")
        usuario_genero = usuario_genero.replace('"', "")
        usuario_genero = '"' + usuario_genero + '"'
        
        try:
            usuarios.append(Usuario(usuario_nombre, usuario_nombre, usuario_email, usuario_genero))
        except Exception as ex:
            with open("error.log", "wt") as log:
                log.writelines(Exception)
                log.writelines("\n")
        
