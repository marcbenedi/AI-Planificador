from enum import Enum

class Tipo(Enum):
    ARROZ    = 1
    PASTA    = 2
    SOPA     = 3
    PESCADO  = 4
    CARNE    = 5
    ENSALADA = 6
    
class Ordinal(Enum):
    PRIMERO    = 1
    SEGUNDO    = 2


class Plato:
    def __init__(self,nombre,primero,tipo,precio,calorias):
        self.nombre = nombre
        self.primero = primero #True si es primero, False si no
        self.tipo = tipo
        self.precio = precio
        self.calorias = calorias
        
    def __repr__(self):
        return str(self.__dict__)
    

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
listaPlatos.append(Plato("Lasaña de espinacas"               ,Ordinal.PRIMERO,Tipo.PASTA,8.65,550))
listaPlatos.append(Plato("Canelones de salmón ahumado"       ,Ordinal.PRIMERO,Tipo.PASTA,7.85,550))
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
listaPlatos.append(Plato("Albóndigas a la jardinera",Ordinal.SEGUNDO,Tipo.CARNE,9   ,750))
listaPlatos.append(Plato("Pies de cerdo"            ,Ordinal.SEGUNDO,Tipo.CARNE,9   ,750))


listaPlatos.append(Plato("Sopa de verduras"   ,Ordinal.PRIMERO,Tipo.SOPA,3.75   ,250))
listaPlatos.append(Plato("Sopa de marisco"    ,Ordinal.PRIMERO,Tipo.SOPA,8.75   ,350))
listaPlatos.append(Plato("Sopa de galets"     ,Ordinal.PRIMERO,Tipo.SOPA,4.75   ,250))
listaPlatos.append(Plato("Sopa de caldo"      ,Ordinal.PRIMERO,Tipo.SOPA,7.75   ,550))
listaPlatos.append(Plato("Estofado de ternera",Ordinal.PRIMERO,Tipo.SOPA,7.75   ,550))
listaPlatos.append(Plato("Sopa de ajo"        ,Ordinal.PRIMERO,Tipo.SOPA,3.75   ,250))
listaPlatos.append(Plato("Sopa de apio"       ,Ordinal.PRIMERO,Tipo.SOPA,3.85   ,275))
listaPlatos.append(Plato("Puré de verduras"   ,Ordinal.PRIMERO,Tipo.SOPA,4.05   ,250))
listaPlatos.append(Plato("Sopa de setas"      ,Ordinal.PRIMERO,Tipo.SOPA,4.75   ,350))
listaPlatos.append(Plato("Caldo casero"       ,Ordinal.PRIMERO,Tipo.SOPA,3.75   ,450))


listaPlatos.append(Plato("Filete de salmón"     ,Ordinal.SEGUNDO,Tipo.PESCADO,9.6 ,750))
listaPlatos.append(Plato("Pastelitos de salmón" ,Ordinal.SEGUNDO,Tipo.PESCADO,8   ,650))
listaPlatos.append(Plato("Sardinillas marinadas",Ordinal.SEGUNDO,Tipo.PESCADO,9   ,750))
listaPlatos.append(Plato("Merluza a la plancha" ,Ordinal.SEGUNDO,Tipo.PESCADO,7   ,750))
listaPlatos.append(Plato("Lubina con albahaca"  ,Ordinal.SEGUNDO,Tipo.PESCADO,9.5 ,750))
listaPlatos.append(Plato("Bacalao a la Vizcaína",Ordinal.SEGUNDO,Tipo.PESCADO,9   ,750))
listaPlatos.append(Plato("Paella de pescado"    ,Ordinal.SEGUNDO,Tipo.PESCADO,12  ,750))
listaPlatos.append(Plato("Fideuá de pescado"    ,Ordinal.SEGUNDO,Tipo.PESCADO,12  ,850))
listaPlatos.append(Plato("Calamares a la romana",Ordinal.SEGUNDO,Tipo.PESCADO,7.5 ,650))
listaPlatos.append(Plato("Sepia en su tinta"    ,Ordinal.SEGUNDO,Tipo.PESCADO,9   ,750))

listaPlatos.append(Plato("Ensalada césar"                    ,Ordinal.PRIMERO,Tipo.ENSALADA,5   ,250))
listaPlatos.append(Plato("Ensalada de espinacas"             ,Ordinal.PRIMERO,Tipo.ENSALADA,5.4 ,240))
listaPlatos.append(Plato("Ensalada de lentejas"              ,Ordinal.PRIMERO,Tipo.ENSALADA,5   ,210))
listaPlatos.append(Plato("Ensalada de garbanzos"             ,Ordinal.PRIMERO,Tipo.ENSALADA,5.1 ,150))
listaPlatos.append(Plato("Ensalada campera"                  ,Ordinal.PRIMERO,Tipo.ENSALADA,5   ,250))
listaPlatos.append(Plato("Ensalada tropical"                 ,Ordinal.PRIMERO,Tipo.ENSALADA,6   ,250))
listaPlatos.append(Plato("Ensalada mediterránea"             ,Ordinal.PRIMERO,Tipo.ENSALADA,6.4 ,250))
listaPlatos.append(Plato("Ensalada con frutos secos"         ,Ordinal.PRIMERO,Tipo.ENSALADA,5.7 ,290))
listaPlatos.append(Plato("Ensalada de moras y queso de cabra",Ordinal.PRIMERO,Tipo.ENSALADA,7   ,350))
listaPlatos.append(Plato("Ensalada de la huerta"             ,Ordinal.PRIMERO,Tipo.ENSALADA,5   ,250))

for p in listaPlatos:
    print(p.nombre)
