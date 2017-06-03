from enum import Enum
import sys, random

class Tipo(Enum):
    ARROZ    = 1
    PASTA    = 2
    SOPA     = 3
    PESCADO  = 4
    CARNE    = 5
    ENSALADA = 6

    def getFormattedName(self):
        return self.name.lower()

class Ordinal(Enum):
    PRIMERO    = 1
    SEGUNDO    = 2


class Plato:
    def __init__(self,nombre,ordinal,tipo,precio,calorias):
        self.nombre = nombre
        self.ordinal = ordinal
        self.tipo = tipo
        self.precio = round(precio)
        self.calorias = calorias

    def __repr__(self):
        return str(self.__dict__)

    def getFormattedName(self):
        return self.nombre.lower().replace(" ","_")
    def getFormattedType(self):
        return self.tipo.getFormattedName()

# USAGE -------------
if (len(sys.argv) < 4):
    print("Wrong number of arguments. 3 Required, {0} found\n  Usage: python3 proGen.py <num_extension> <num_incompatibilities> <num_dias_plato_fijo>".format(len(sys.argv)-1))
    sys.exit()
if (int(sys.argv[3]) > 5):
    print("<num_dias_plato_fijo> has to be 5 or less, but {0} found\n  Usage: python3 proGen.py <num_extension> <num_incompatibilities> <num_dias_plato_fijo>".format(sys.argv[3]))
    sys.exit()

num_ext = int(sys.argv[1])

listaPlatos = []
listaPlatos.append(Plato("Arroz tres delicias"            ,Ordinal.PRIMERO,Tipo.ARROZ,5.75,450))
listaPlatos.append(Plato("Arroz con lentejas"             ,Ordinal.PRIMERO,Tipo.ARROZ,4   ,350))
listaPlatos.append(Plato("Arroz al curry"                 ,Ordinal.PRIMERO,Tipo.ARROZ,4.5 ,350))
listaPlatos.append(Plato("Arroz integral con quinoa"      ,Ordinal.PRIMERO,Tipo.ARROZ,4,   350))
listaPlatos.append(Plato("Rissoto de setas"               ,Ordinal.PRIMERO,Tipo.ARROZ,6.85,450))
listaPlatos.append(Plato("Rissoto de vegetales"           ,Ordinal.PRIMERO,Tipo.ARROZ,8.5 ,450))
listaPlatos.append(Plato("Ensalada de arroz con legumbres",Ordinal.PRIMERO,Tipo.ARROZ,4.25,350))
listaPlatos.append(Plato("Arroz con bogavante"            ,Ordinal.PRIMERO,Tipo.ARROZ,12.5,550))
listaPlatos.append(Plato("Arroz con conejo"               ,Ordinal.PRIMERO,Tipo.ARROZ,6.15,450))
listaPlatos.append(Plato("Arroz basmati"                  ,Ordinal.PRIMERO,Tipo.ARROZ,4.6, 350))


listaPlatos.append(Plato("Pasta fresca al pomodoro"          ,Ordinal.PRIMERO,Tipo.PASTA,4   ,250))
listaPlatos.append(Plato("Macarrones al pesto"               ,Ordinal.PRIMERO,Tipo.PASTA,5.75,450))
listaPlatos.append(Plato("Ravioli funghi"                    ,Ordinal.PRIMERO,Tipo.PASTA,7.5 ,450))
listaPlatos.append(Plato("Tortellini a la provenzana"        ,Ordinal.PRIMERO,Tipo.PASTA,5.35,350))
listaPlatos.append(Plato("Espirales con frutos rojos"        ,Ordinal.PRIMERO,Tipo.PASTA,4.5 ,375))
listaPlatos.append(Plato("Lasagne de espinacas"               ,Ordinal.PRIMERO,Tipo.PASTA,8.65,550))
listaPlatos.append(Plato("Canelones de salmon ahumado"       ,Ordinal.PRIMERO,Tipo.PASTA,7.85,550))
listaPlatos.append(Plato("Espaguetis a la bolognese"         ,Ordinal.PRIMERO,Tipo.PASTA,3.65,450))
listaPlatos.append(Plato("Ensalada de pasta y verduras"      ,Ordinal.PRIMERO,Tipo.PASTA,6.5 ,250))
listaPlatos.append(Plato("Pasta a escoger con salsa especial",Ordinal.PRIMERO,Tipo.PASTA,6   ,450))


listaPlatos.append(Plato("Pollo al limon"           ,Ordinal.SEGUNDO,Tipo.CARNE,6.8 ,750))
listaPlatos.append(Plato("Pollo al chilindron"      ,Ordinal.SEGUNDO,Tipo.CARNE,8.6 ,750))
listaPlatos.append(Plato("Pollo al ast"             ,Ordinal.SEGUNDO,Tipo.CARNE,6   ,850))
listaPlatos.append(Plato("Entrecot de ternera"      ,Ordinal.SEGUNDO,Tipo.CARNE,17.5,850))
listaPlatos.append(Plato("Chuletillas de cerdo"     ,Ordinal.SEGUNDO,Tipo.CARNE,9   ,750))
listaPlatos.append(Plato("Carne rebozada"           ,Ordinal.SEGUNDO,Tipo.CARNE,6   ,650))
listaPlatos.append(Plato("Carpaccio de ternera"     ,Ordinal.SEGUNDO,Tipo.CARNE,5.5 ,450))
listaPlatos.append(Plato("Alitas de pollo"          ,Ordinal.SEGUNDO,Tipo.CARNE,6   ,650))
listaPlatos.append(Plato("Albondigas a la jardinera",Ordinal.SEGUNDO,Tipo.CARNE,9   ,750))
listaPlatos.append(Plato("Pies de cerdo"            ,Ordinal.SEGUNDO,Tipo.CARNE,9   ,750))


listaPlatos.append(Plato("Sopa de verduras"   ,Ordinal.PRIMERO,Tipo.SOPA,3.75   ,250))
listaPlatos.append(Plato("Sopa de marisco"    ,Ordinal.PRIMERO,Tipo.SOPA,8.75   ,350))
listaPlatos.append(Plato("Sopa de galets"     ,Ordinal.PRIMERO,Tipo.SOPA,4.75   ,250))
listaPlatos.append(Plato("Sopa de caldo"      ,Ordinal.PRIMERO,Tipo.SOPA,7.75   ,550))
listaPlatos.append(Plato("Estofado de ternera",Ordinal.PRIMERO,Tipo.SOPA,7.75   ,550))
listaPlatos.append(Plato("Sopa de ajo"        ,Ordinal.PRIMERO,Tipo.SOPA,3.75   ,250))
listaPlatos.append(Plato("Sopa de apio"       ,Ordinal.PRIMERO,Tipo.SOPA,3.85   ,275))
listaPlatos.append(Plato("Pure de verduras"   ,Ordinal.PRIMERO,Tipo.SOPA,4.05   ,250))
listaPlatos.append(Plato("Sopa de setas"      ,Ordinal.PRIMERO,Tipo.SOPA,4.75   ,350))
listaPlatos.append(Plato("Caldo casero"       ,Ordinal.PRIMERO,Tipo.SOPA,3.75   ,450))


listaPlatos.append(Plato("Filete de salmon"     ,Ordinal.SEGUNDO,Tipo.PESCADO,9.6 ,750))
listaPlatos.append(Plato("Pastelitos de salmon" ,Ordinal.SEGUNDO,Tipo.PESCADO,8   ,650))
listaPlatos.append(Plato("Sardinillas marinadas",Ordinal.SEGUNDO,Tipo.PESCADO,9   ,750))
listaPlatos.append(Plato("Merluza a la plancha" ,Ordinal.SEGUNDO,Tipo.PESCADO,7   ,750))
listaPlatos.append(Plato("Lubina con albahaca"  ,Ordinal.SEGUNDO,Tipo.PESCADO,9.5 ,750))
listaPlatos.append(Plato("Bacalao a la Vizcaina",Ordinal.SEGUNDO,Tipo.PESCADO,9   ,750))
listaPlatos.append(Plato("Paella de pescado"    ,Ordinal.SEGUNDO,Tipo.PESCADO,12  ,750))
listaPlatos.append(Plato("Fideua de pescado"    ,Ordinal.SEGUNDO,Tipo.PESCADO,12  ,850))
listaPlatos.append(Plato("Calamares a la romana",Ordinal.SEGUNDO,Tipo.PESCADO,7.5 ,650))
listaPlatos.append(Plato("Sepia en su tinta"    ,Ordinal.SEGUNDO,Tipo.PESCADO,9   ,750))

listaPlatos.append(Plato("Ensalada cesar"                    ,Ordinal.PRIMERO,Tipo.ENSALADA,5   ,250))
listaPlatos.append(Plato("Ensalada de espinacas"             ,Ordinal.PRIMERO,Tipo.ENSALADA,5.4 ,240))
listaPlatos.append(Plato("Ensalada de lentejas"              ,Ordinal.PRIMERO,Tipo.ENSALADA,5   ,210))
listaPlatos.append(Plato("Ensalada de garbanzos"             ,Ordinal.PRIMERO,Tipo.ENSALADA,5.1 ,150))
listaPlatos.append(Plato("Ensalada campera"                  ,Ordinal.PRIMERO,Tipo.ENSALADA,5   ,250))
listaPlatos.append(Plato("Ensalada tropical"                 ,Ordinal.PRIMERO,Tipo.ENSALADA,6   ,250))
listaPlatos.append(Plato("Ensalada mediterranea"             ,Ordinal.PRIMERO,Tipo.ENSALADA,6.4 ,250))
listaPlatos.append(Plato("Ensalada con frutos secos"         ,Ordinal.PRIMERO,Tipo.ENSALADA,5.7 ,290))
listaPlatos.append(Plato("Ensalada de moras y queso de cabra",Ordinal.PRIMERO,Tipo.ENSALADA,7   ,350))
listaPlatos.append(Plato("Ensalada de la huerta"             ,Ordinal.PRIMERO,Tipo.ENSALADA,5   ,250))

dias_semana = ["lunes", "martes", "miercoles", "jueves", "viernes"]

f = open("ext{}.prob".format(sys.argv[1]),'w')

def header():
    inicio = """(define (problem ext{0}_prob)
    (:domain ext{0}_dom)
    (:objects
    ; Dias de la semana
    lunes martes miercoles jueves viernes - dia

    ; Primeros platos
    """.format(sys.argv[1])

    f.write(inicio)

    for p in [p for p in listaPlatos if p.ordinal == Ordinal.PRIMERO]:
        f.write(p.getFormattedName()+" ")

    f.write("- primer_plato\n\n")

    f.write("""    ; Segundos platos
    """)

    for p in [p for p in listaPlatos if p.ordinal == Ordinal.SEGUNDO]:
        f.write(p.getFormattedName()+" ")

    f.write("- segundo_plato\n\n")

    f.write("""    ; Tipos de plato
    """)

    for p in [p for p in Tipo]:
        f.write(p.getFormattedName()+" ")

    f.write("- tipo_plato\n\n")

 # ----------- INIT -------------

def openInit():
    f.write("""    )
    (:init\n\n""")

def diaSiguiente():
    f.write("    ; Dia siguiente\n")
    f.write("    (primer_dia lunes)\n")
    for i in range(len(dias_semana)-1):
        f.write("    (dia_consecutivo {0} {1})\n".format(dias_semana[i], dias_semana[i+1]))
    f.write("\n\n")

def tiposPlato():
    f.write("    ; Tipos de plato\n")
    for p in listaPlatos:
        f.write("    (tiene_tipo {0} {1})\n".format(p.getFormattedName(), p.getFormattedType() ))
    f.write("\n\n")

def precioPlatos():
    f.write("    ; Precio\n")
    f.write("    (= (precio_total) 0)\n")
    for p in listaPlatos:
        f.write("    (= (precio_plato {0}) {1})\n".format(p.getFormattedName(), p.precio ))
    f.write("\n\n")


def caloriasPlatos():
    f.write("    ; Calorias platos\n")
    for p in listaPlatos:
        f.write("    (= (calorias_plato {0}) {1})\n".format(p.getFormattedName(), p.calorias ))
    f.write("\n\n")

def caloriasDiasSemana():
    f.write("    ; Calorias dias semana\n")
    for p in ["lunes", "martes", "miercoles", "jueves", "viernes"]:
        f.write("    (= (calorias_dia {0}) 0)\n".format(p))
    f.write("\n\n")

def incompatiblesPlatos():
    f.write("    ; Incompatibilidades\n")
    for i in range(int(sys.argv[2])):
        f.write("    (incompatible {0} {1})\n".format( \
        random.choice([p for p in listaPlatos if p.ordinal == Ordinal.PRIMERO]).getFormattedName(),
        random.choice([p for p in listaPlatos if p.ordinal == Ordinal.SEGUNDO]).getFormattedName()
        ))
    f.write("\n\n")

def diasFijos():
    f.write("    ; Dias fijos\n")
    dias_posibles = dias_semana
    for i in range(int(sys.argv[3])):
        index_dia_chosen = random.choice(range(len(dias_posibles)))
        index_plato_chosen = random.choice(range(len(listaPlatos)))
        f.write("    (plato_fijo {0} {1})\n".format( \
        listaPlatos[index_plato_chosen].getFormattedName(),
        dias_posibles[index_dia_chosen]
        ))
        #f.write("    (cocinado {})\n".format(listaPlatos[index_plato_chosen].getFormattedName()))
        #f.write("  ({0} {1} {2})\n".format(listaPlatos[index_plato_chosen].getFormattedName()))
        del dias_posibles[index_dia_chosen]
        del listaPlatos[index_plato_chosen]
    f.write("\n\n")

def closeInit():
    f.write("\n  ) ; Closing :init\n\n")

def goal():
    f.write("  (:goal\n")
    f.write("    (forall (?dia - dia) (tiene_menu ?dia))\n")
    f.write("  ) ; Closing :goal\n")

def closeFile():
    f.close()

def closeDefine():
    f.write(") ; Closing define\n")

def main():
    header()
    openInit()

    incompatiblesPlatos()

    if num_ext >= 2:
        diaSiguiente()
        tiposPlato()

    if num_ext >= 3:
        diasFijos()

    if num_ext >= 4:
        caloriasPlatos()
        caloriasDiasSemana()

    if num_ext >= 5:
        precioPlatos()

    closeInit()
    goal()
    closeDefine()
    closeFile()

#RUN
main()
