import time
import datetime

def calculate_fare(stop_time, moving_time):
    tarifa_base = 2.5  
    tarifa_movi = moving_time * 0.2
    tarifa_espera = stop_time * 0.5  
    return tarifa_base + tarifa_movi + tarifa_espera

def registrar_trayecto(nombre_responsable, nombre_nino, silla_bebe, stop_time, moving_time, total_fare):
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    silla_texto ="Con silla para niños" if silla_bebe.lower() == "si" else "Sin silla para niños"

    registro =(
        f"{fecha_hora} | Responsable: {nombre_responsable} | Destino {nombre_nino} |"
        f"{silla_texto} | Tiempo detenido: {stop_time:.1f}s |En movimiento: {moving_time} | Total: ${total_fare:.2f} \n"
    )

    with open("historial_trayectos.txt", "a") as archivo: 
        archivo.write(registro)

def solicitar_datos_usuario():
    print("Bienvenidos a Familia en Movimiento. Somos la única empresa de transportes que ofrece servicio a familias con niños")

    nombre_padre_o_madre = input("Indícame el nombre del padre o madre que solicita el servicio: ")
    nombre_niño = input(f"¡Genial! {nombre_padre_o_madre}, ahora dime el nombre de tu hijo o hija: ")


    while True:
        silla_bebe = input("¿Tu hijo es menor de 12 años? (si/no): ").lower()
        if silla_bebe == "si":
            print(f"{nombre_niño} necesita una silla de niños, según las normas del DGT. ¡No te preocupes! La llevaremos por ti sin costo adicional.") 
            break
        elif silla_bebe == "no":
            print("Perfecto, no es necesario llevar silla de niños.") 
            break
        else:
            print("No te entendí. Por favor responde si o no.") 

    print(f"\nUn conductor llegará a recogerlos en breve. Gracias por elegirnos, {nombre_padre_o_madre} y {nombre_niño}.")
    print("🚕, 🚕, 🔊 bippp bipppp. ¡Su transporte ha llegado. Buen viaje!")
    
    return {
        "nombre_padre_o_madre": nombre_padre_o_madre,
        "nombre_niño": nombre_niño,
        "silla_bebe": silla_bebe 
    }

def taximeter():
    datos_usuario = solicitar_datos_usuario()

    momento_actual = datetime.datetime.now()
    print(f"Son las {momento_actual.strftime('%H:%M:%S')}, y comienza el viaje\n")

    print("Estos son los comandos para tu transporte: start, stop, move, finish, exit")

    trip_activate = False
    start_time = 0
    stop_time = 0
    moving_time = 0
    state = None
    state_start_time = 0

    while True:
        command = input(">").strip().lower()
        
        if command == "start":
            if trip_activate:
                print("Error: el viaje ya ha iniciado")
                continue
            trip_activate = True
            start_time = time.time()
            stop_time = 0 
            moving_time = 0 
            state = "stop"
            state_start_time = time.time()
            print("El viaje ha iniciado")

        elif command in ("stop", "move"):
            if not trip_activate:
                print("Error: el viaje no ha iniciado")
                continue
            duration = time.time() - state_start_time

            if state == "stop":
                stop_time += duration
            elif state == "moving":
                moving_time += duration

            state = "stop" if command == "stop" else "moving"
            state_start_time = time.time()
            print(f"El estado cambió a {state}")

        elif command == "finish":
            if not trip_activate:
                print("Error: el viaje no ha iniciado")
                continue

            duration = time.time() - state_start_time
            if state == "stop":
                stop_time += duration
            elif state == "moving":
                moving_time += duration

            # Resumen del viaje
            print("\nResumen del viaje:")
            print(f"Pasajero responsable: {datos_usuario['nombre_padre_o_madre']}")
            print(f"Niño o niña: {datos_usuario['nombre_niño']}")
            if datos_usuario["silla_bebe"] == "si":
                print("Viajó con silla para niños.")
            else:
                print("No necesitó silla para niños.")

            # Calcular tarifa
            total_fare = calculate_fare(stop_time, moving_time)
            print(f"Tiempo detenido: {stop_time:.1f} segundos")
            print(f"Tiempo en movimiento: {moving_time:.1f} segundos")
            print(f"Total a pagar: ${total_fare:.2f}")

            registrar_trayecto(datos_usuario['nombre_padre_o_madre'], datos_usuario['nombre_niño'], datos_usuario["silla_bebe"], stop_time, moving_time, total_fare)

            trip_activate = False
            state = None

        elif command == "exit":
            print("Gracias por viajar con nosotros. Hasta luego")
            break

        else:
            print("Comando no válido. Usa: start, stop, move, finish, exit")

if __name__ == "__main__":
    taximeter()
