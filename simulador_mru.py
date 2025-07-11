#Simulador de MRU 📘

""" 
Programa: Simulador de MRU
Autor: Jheremy💻✨
Fecha: 08/07/25

Introduccion: El programa consiste en resolver ejercicios de
MRU. El usuario selecciona la operacion a realizar, da los
datos, el programa resuelve y entrega el resultado.
"""

def op_d(v, t): 
    return v * t

def op_v(d, t): 
    return d / t

def op_t(d, v): 
    return d / v

def inicio(): 
    return input("""
Comencemos 🤓💪. Ahora necesito que ingreses
la operacion que quieres realizar. Buscar distancia,
buscar velocidad o tiempo:

1.Ingresa "d" para distancia 🎈.
2.Ingresa "v" para velocidad 🥏.
3.Ingresa "t" para tiempo 🕰️.\n
""").lower()

again = input(""" 
Hola Usuario ☺️ 🩵. Bienvenido a este simulador de MRU.
Aqui te ayudaremos a resolver tus ejercicios en base
al dato que necesites hallar. Solo necesitas igresar
los datos que tienes, y el resto lo hago yo 🤓. 

Ingresa "si" para iniciar 🤓 o "no" para dejarlo para otro dia 🥹.
\n
""").lower() 

if again == "si":
    while True:
        user_op = inicio() 
        if user_op == "d": 
            try: 
                v = float(input("\nMuy bien ☺️ ✨. Ahora ingresa el valor de velocidad 🥏 \n"))
            except ValueError: 
                print("\nOpps 😵‍💫. El valor ingresado no es valido. \nIntentalo otra vez ☺️\n")
                continue
            else:
                try: 
                    t = float(input("\nAhora, ingresa el valor del tiempo 🕰️ \n")) 
                except ValueError:
                    print("\nOpps 😵‍💫. El valor ingresado no es valido. \nIntentalo otra vez ☺️\n")
                    continue
                else:
                    print(f"La distancia 🎈 del objeto es de {op_d(v, t)} metros 🤓☝️.\n")
                    again = input("""
Ahora ¿Quieres seguir calculando datos? 🥹 
Ingresa si para continuar y no para finalizar ☺️ ✨\n
""").lower()
                    if again != "si":
                        print("\nHa sido un gusto calcular la distancia 🎈 🤓 🩵\n")
                        break
        elif user_op == "v": 
            print("""\n
Nota: Asegurate de que el numerador (d) no sea cero (0),
ya que al dar el resultado dara error 😵‍💫. (No se puede dividir entre 0 🤓☝️).

Y si el denominador (t) es cero (0), el resultado
automaticamente sera 0. 🤓☝️\n
""")
            try:
                d = float(input("\nMuy bien ☺️ ✨. Ahora ingresa el valor de distancia 🎈 \n")) 
            except ValueError: 
                print("\nOpps 😵‍💫. El valor ingresado no es valido. \nIntentalo otra vez ☺️\n") 
                continue
            else:
                try:
                    t = float(input("\nAhora, ingresa el valor del tiempo 🕰️ \n"))
                except ValueError: 
                    print("\nOpps 😵‍💫. El valor ingresado no es valido. \nIntentalo otra vez ☺️\n") 
                    continue
                else:
                    print(f"La valocidad 🥏 del objeto es de {op_v(d, t)} m/s 🤓☝️.\n")
                    again = input("""
Ahora ¿Quieres seguir calculando datos? 🥹 
Ingresa si para continuar y no para finalizar ☺️ ✨\n
""").lower()
                    if again != "si":
                        print("\nHa sido un gusto calcular la velocidad 🥏 🤓 🩵\n")
                        break
        elif user_op == "t":
            print("""\n
Nota: Asegurate de que el numerador (d) no sea cero (0),
ya que al dar el resultado dara error 😵‍💫. (No se puede dividir entre 0 🤓☝️).

Y si el denominador (v) es cero (0), el resultado
automaticamente sera 0. 🤓☝️\n
""")
            try:
                d = float(input("\nMuy bien ☺️ ✨. Ahora ingresa el valor de distancia 🎈 \n"))
            except ValueError:
                print("\nOpps 😵‍💫. El valor ingresado no es valido. \nIntentalo otra vez ☺️\n") 
                continue
            else:
                try:
                    v = float(input("\nAhora, ingresa el valor de la velocidad 🥏 \n"))
                except ValueError:
                    print("\nOpps 😵‍💫. El valor ingresado no es valido. \nIntentalo otra vez ☺️\n")
                    continue
                else:
                    print(f"El tiempo del objeto es de {op_t(d, v)} segundos 🤓☝️.\n") 
                    again = input("""
Ahora ¿Quieres seguir calculando datos? 🥹 
Ingresa si para continuar y no para finalizar ☺️ ✨\n
""").lower()
                    if again != "si":
                        print("\nHa sido un gusto calcular el tiempo 🕰️ 🤓 🩵\n")
                        break
        else:
            print("\nOops 😵‍💫. Algo ha salido mal. Vuelve a intentarlo ☺️ ✨")
else: 
    print("""
\nMuy bien ☺️. Resolvemos problemas otra ocasion 🥹 🩵.
O asegurate de haber ingresado la respuesta correcta. ☺️🩵
\n""")

