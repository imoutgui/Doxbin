import csv
import os
import unicodedata
import json
import re
os.system ("clear")

print ("\033[91m")


os.system ("figlet DOXBIN")

print ("\033[0m")
print ("                  ..                            ..     ")
print ("                 ...                            ...  ")
print ("                .   .       .............       .   . ")
print ("               .    .     ..             ..     .    . ")
print ("              .     .   ..                 ..   .     . ")
print ("             .      .. .                     .  ..      . ")
print ("            .        ...  :                : ....         . ")
print ("            .           .                   .             . ")
print ("            .           .                   .             . ") 
print ("             .          .                   .            .")
print ("      ..      `.........                     ...........'     .. ")
print ("          .  ..    .                                   .   ..  . ")
print ("           .   ..   .                                 .  ..   . ")
print ("           .         .                               .        . ")
print ("           .         .  :             '            : .        .  ")
print ("           ..        .  .....        .    :      ... .       ..  ")
print ("             .      .     .  `...    .      ...'  .   .     . ")    
print ("              .    .       :     `...    ...'    :     .   .  ")
print ("                ..          ....'           ....'       ..     ")
print ("                 .                                      .              ")
print ("                  ..     ..        .    .        ..   ..  ")
print ("                    ..      ...   .      .   ....   ..   ")
print ("                     ..     .  ..  .    .  ..   . ..   ")
print ("                     ..     .    .. .  .  ..   .  ..  ")                    
print ("                       ..    .       .   ..  .  ..  ")
print ("                         ..   .  ........'  . ..   ")
print ("                          ..     .         .  ..   ")
print ("                           ..     `......'  ..    ")
print ("                            ..'.         .'..    ")
print ("                              .............   ")
print ("                                .........     ")                 
print ("")
print ("\033[96m                   creado por the dark society")
print ("\033[92m                           unetenos!!!!! ")
print ("\033[91m                     seleccione una persona \033[0m")
print ("")
print ("                         _________________________      ")
print ("                         |   busque o            |   ")
print ("                         |         /             |  ")
print ("                         ————————————————————————- ")
print ("")
print ("pasando por las 4 secciones de filtracion, alumnos, docentes, personas de america del sur y unas personas adicionales")
print ("\033[91m")



def normalizar_nombre(nombre):
    nfkd = unicodedata.normalize('NFKD', str(nombre))
    ascii_str = nfkd.encode('ASCII', 'ignore').decode('ASCII')
    clean = re.sub(r'[^a-zA-Z\s]', '', ascii_str).lower().strip()
    return re.sub(r'\s+', '_', clean)

print("[*] Cargando bases de datos, por favor espera...")


alumnos_dict = {}
try:
    with open('alumnos_full.json', 'r', encoding='utf-8') as f:
        data_alumnos = json.load(f)
    lista_alumnos = data_alumnos.get('students', data_alumnos) if isinstance(data_alumnos, dict) else data_alumnos
    for alumno in lista_alumnos:
        if isinstance(alumno, dict) and 'nombre' in alumno:
            alumnos_dict[normalizar_nombre(alumno['nombre'])] = alumno
except Exception as e:
    print(f"[!] Error al cargar alumnos: {e}")


docentes_dict = {}
try:
    with open('docentes.json', 'r', encoding='utf-8') as f:
        data_docentes = json.load(f)
    lista_docentes = data_docentes.get('docentes', data_docentes) if isinstance(data_docentes, dict) else data_docentes
    for docente in lista_docentes:
        if isinstance(docente, dict):
            p_nombre = docente.get('primerNombre', '')
            s_nombre = docente.get('segundoNombre', '')
            p_apellido = docente.get('primerApellido', '')
            s_apellido = docente.get('segundoApellido', '')
            
            nombre_completo = f"{p_nombre} {s_nombre} {p_apellido} {s_apellido}"
            nombre_completo = " ".join(nombre_completo.split())
            
            if nombre_completo:
                docentes_dict[normalizar_nombre(nombre_completo)] = docente
                docente['nombre_completo'] = nombre_completo
except Exception as e:
    print(f"[!] Error al cargar docentes: {e}")


arg_dict = {}
try:
    with open('DB.ARG.csv', mode='r', encoding='utf-8', errors='ignore') as f:
        lector = csv.DictReader(f)
        for fila in lector:
            p_nombre = fila.get('PRIMER_NOMBRE', '')
            o_nombres = fila.get('OTROS_NOMBRES', '')
            p_apellido = fila.get('PRIMER_APELLIDO', '')
            o_apellidos = fila.get('OTROS_APELLIDOS', '')
            
           
            partes = [p_nombre, o_nombres, p_apellido, o_apellidos]
            nombre_completo = " ".join([p for p in partes if p and p != '-'])
            nombre_completo = " ".join(nombre_completo.split())
            
            if nombre_completo:
                arg_dict[normalizar_nombre(nombre_completo)] = fila
                fila['nombre_completo'] = nombre_completo
except Exception as e:
    print(f"[!] Error al cargar DB.ARG.csv: {e}")

print(f"[+] ¡Listo! Se cargaron {len(alumnos_dict)} alumnos, {len(docentes_dict)} docentes y {len(arg_dict)} registros de ARG.\n")


while True:
    print("=" * 45)
    print("          MENÚ PRINCIPAL - BÚSQUEDA")
    print("=" * 45)
    print("1. Buscar Alumno")
    print("2. Buscar Docente")
    print("3. Buscar en Base ARG (CSV)")
    print("4. seccion de personas addicionales")
    
    opcion_menu = input("\nElige una opción (1, 2, 3 o 4): ").strip()
    
    if opcion_menu == '4':
        print("pasando a la seccion 4...")
        break
        
    elif opcion_menu == '1':
        busqueda = input("\n¿A qué alumno buscas?: ").strip()
        busqueda_limpia = normalizar_nombre(busqueda)
        
        if busqueda_limpia in alumnos_dict:
            al = alumnos_dict[busqueda_limpia]
            print("\n" + "=" * 50)
            print("         INFORMACIÓN COMPLETA DEL ALUMNO")
            print("=" * 50)
            print(json.dumps(al, indent=4, ensure_ascii=False))
            print("=" * 50 + "\n")
        else:
            print(f"\n[!] No se encontró al alumno: '{busqueda}'\n")
            
    elif opcion_menu == '2':
        busqueda = input("\n¿A qué docente buscas?: ").strip()
        busqueda_limpia = normalizar_nombre(busqueda)
        
        if busqueda_limpia in docentes_dict:
            doc = docentes_dict[busqueda_limpia]
            print("\n" + "=" * 50)
            print("         INFORMACIÓN COMPLETA DEL DOCENTE")
            print("=" * 50)
            print(json.dumps(doc, indent=4, ensure_ascii=False))
            print("=" * 50 + "\n")
        else:
            print(f"\n[!] No se encontró al docente: '{busqueda}'\n")
            
    elif opcion_menu == '3':
        busqueda = input("\n¿A quién buscas en Base ARG?: ").strip()
        busqueda_limpia = normalizar_nombre(busqueda)
        
        if busqueda_limpia in arg_dict:
            registro = arg_dict[busqueda_limpia]
            print("\n" + "=" * 50)
            print("         INFORMACIÓN COMPLETA (BASE ARG)")
            print("=" * 50)
            print(json.dumps(registro, indent=4, ensure_ascii=False))
            print("=" * 50 + "\n")
        else:
            print(f"\n[!] No se encontró el registro: '{busqueda}'\n")
            
    else:
        print("\n[!] Opción no válida. Elige 1, 2, 3 o 4.\n")


paris = "paris danae edad 13 años telefono iphone provedor de internet megacable su tiktok es user4389115588 instagram ko0ki001 numero de telefono +52 472 105 4659 sangitario ciudad silao gto ademas cumple años el 23 de noviembre"
juan_mateo = "juan mateo contreras edad 13 años ciudad silao gto escuela telesecundaria 530 nacio en mayo cuenta de instagram mateo contreras"
raymundo_valencia = "raymundo valencia estrada actualmente trabaja de maestro en la telesecundaria 530 y la secundaria efrain huerta, ademas de tener un puesto de pollos dorados. esta casado y vive en sliao gto. el pasado 30 de junio hizo un en vivo mientras paso por la calle bailleres Pte. de silao gto, hiba en un carro"
catalina = "catalina, vive en chile y en una villa llamada don pablo. tiene 13 años, un novio de 17 años y va a un liceo. su numero es +56 9 2970 9079. su ip es 179.60.67.159. su novio cumple años el 7 de octubre y es de guatemala"
jonathan = "jonathan guadalupe edad 13 años. escuela telesecundaria 530, tiene una cuenta de tiktok llamada jonathanguadalupe231, es de sliao gto y vive en https://maps.app.goo.gl/o3u2SwMQZDVXz91w7"
fransisco_perez_quijas = "fransisco perez quijas, vive en leon guanajuato, tiene una hija y un hijo"
coco_martinez = "coco martinez, vive en silao esta soltera y su facebook es coco martinez"
juana_gomez = "juana gomez, vive en leon guanajuato. esta divorciada actualmente"
alejandro_valentin_lezama = "alejandro valentin lezama, vive en Ciudad Juárez, Chihuahua, México. esta soltero. tiene un hijo llamado juan y el hijo cumple años en el 24 de junio"
britzy = "britzy, tiene 13 años, vive en silao gto, va a la secundaria miguel hidalgo su whatsapp es +52 472 113 1117. y su cuenta de tiktok es nirvalina.1"
rosario_guzman = "rosario guzman, vive en santa tecla. actualmente en una relacion. tiene 2 hijas y un hijo, ademas su cuenta de faceebook es Rosario Guzman"
lidia_del_socorro_sanchez = "lidia del socorro sanchez alonso, cedulaidentidad 0012112910066T nacio el 21/12/1991"
nancy_del_socorro_rivera = "nancy del socorro rivera sanarucia, cedulaidentidad 0010809870036K echa de nascimiento 1987-9-8 numero de telefono 84255886 idbarrio 176 direccion del porton de la pepsi 1C abajo "


print ("\033[91m")

opcion = input ("a quien buscas?:")

if opcion == "paris":
     print (paris)
if opcion == "juan_mateo":
     print (juan_mateo)
if opcion == "raymundo_valencia":
     print (raymundo_valencia)
if opcion == "catalina":
     print (catalina)
if opcion == "jonathan":
     print (jonathan)
if opcion == "fransisco perez quijas":
     print (fransisco_perez_quijas)
if opcion == "coco martinez":
     print (coco_martinez)
if opcion == "juana gomez":
     print (juana_gomez)
if opcion == "alejandro valentin lezama":
     print (alejandro_valentin_lezama)
if opcion == "britzy":
     print (britzy)
if opcion == "rosario guzman":
     print (rosario_guzman)
if opcion == "lidia del socorro sanchez":
     print (lidia_del_socorro_sanchez)
if opcion == "nancy del socorro rivera":
     print (nancy_del_socorro_rivera)
