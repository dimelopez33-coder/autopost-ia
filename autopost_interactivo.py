import os
import datetime
import random
from simple_term_menu import TerminalMenu

# ===============================
# CONFIGURACIÓN
# ===============================
CARPETA_SALIDA = "posts_generados"
os.makedirs(CARPETA_SALIDA, exist_ok=True)

temas = {
    1: "Motivación personal",
    2: "Productividad",
    3: "Tecnología y conciencia",
    4: "Arte y percepción",
    5: "Otro tema personalizado"
}

tonos = ["inspirador", "profesional", "poético", "casual"]

frases_motivacion = [
    "Cada paso pequeño construye el camino que soñás.",
    "Tu enfoque determina tu destino.",
    "El silencio también enseña cuando sabés escucharlo.",
    "Nada real puede ser amenazado. Nada irreal existe.",
    "El momento presente es el punto de poder."
]

# ===============================
# FUNCIONES
# ===============================
def generar_post(tema, tono):
    base = random.choice(frases_motivacion)
    return f"[{tema}] ({tono}) — {base}"

def menu_principal():
    opciones = ["Crear nuevo post", "Ver posts generados", "Salir"]
    menu = TerminalMenu(opciones, title="\n🧠 AUTOPOST IA+ — MENÚ PRINCIPAL")
    eleccion = menu.show()
    return eleccion

def elegir_tema():
    opciones = list(temas.values())
    menu = TerminalMenu(opciones, title="\n📂 Elegí un tema")
    idx = menu.show()
    return temas[idx + 1]

def elegir_tono():
    menu = TerminalMenu(tonos, title="\n🎨 Elegí un tono")
    idx = menu.show()
    return tonos[idx]

# ===============================
# PROGRAMA PRINCIPAL
# ===============================
while True:
    opcion = menu_principal()

    if opcion == 0:
        tema = elegir_tema()
        tono = elegir_tono()
        texto = generar_post(tema, tono)
        fecha = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        archivo_salida = os.path.join(CARPETA_SALIDA, f"post_{fecha}.txt")

        with open(archivo_salida, "w") as f:
            f.write(texto)

        print(f"\n✅ Post generado y guardado:\n{archivo_salida}\n")
        print(f"📝 {texto}\n")

    elif opcion == 1:
        print("\n📁 Publicaciones generadas:\n")
        archivos = os.listdir(CARPETA_SALIDA)
        if not archivos:
            print("Aún no hay publicaciones.\n")
        else:
            for f in archivos:
                print("•", f)
        input("\nPresioná ENTER para volver al menú...")

    elif opcion == 2:
        print("\n👋 Saliendo de AUTOPOST IA+...\n")
        break
