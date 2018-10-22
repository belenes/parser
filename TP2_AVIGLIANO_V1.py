# hola soy un parser

from avigliano_lexer_v3 import lexer

derivaciones=[]

def Principal (tokens):

    contador = 0
    error = False
    ProcedureN()
    if error==False and FinCadena == True :
        #Esto me devuelve un Booleano
        Pertenece()

def ProcedureN (tokens) :
    kk = 0

    while error = False and kk <= len(tokens) :
        tokens[kk]
        error = False
        Procesar(tokens[kk])
        kk = kk + 1

def Procesar ():
        tuplas = tokens[kk]
        Cosa = tuplas[1]

# Todas las derivaciones desde el simbolo inicial

#<Funcion> →  <Tipo> <Identificador> ( <ListaArgumentos> ) <SentenciaCompuesta>
def SimboloInicial (Cosa):
    auxiliar = ["<Funcion>"]
    if Tipo():
    elif Identificador()
    elif "("
    elif ListaArgumentos()
    elif ")"
    elif SentenciaCompuesta()
    else:
         error = True

#<Tipo> → int
#<Tipo> → float
def Tipo():
    auxiliar.append("<Tipo>")
    if "Int" == Cosa
        derivaciones.append("Int")
    elif "Float" == Cosa
        derivaciones.append("Float")

def Identificador()


#<ListaArgumentos> → <Argumento>
#<ListaArgumentos> → <Argumento> , <ListaArgumentos>
def ListaArgumentos():
    if Argumento()
    else :
        if Argumento()
    elif ",":
        derivaciones.append(",")
        elif ListaArgumentos()

#<Argumento> → <Tipo><Identificador>
def Argumento():
    if Tipo()
    elif Identificador()

#<SentenciaCompuesta> → {<ListaSentencia>}
def SentenciaCompuesta():
    if "{":
        derivaciones.append("{")
    elif ListaSentencia()
    elif "}":
        derivaciones.append("}")

#<ListaSentencia> → <Sentencia>
#<ListaSentencia> → <Sentencia><ListaSentencia>
def ListaSentencia():
    if Sentencia()
    else:
        if Sentencia()
        elif ListaSentencia()

#<Sentencia> → <SentFor>
#<Sentencia> → <SentWhile>
#<Sentencia> → <Expr> ;
#<Sentencia> → <SentIf>
#<Sentencia> → <SentenciaCompuesta>
#<Sentencia> → <Declaracion> ;
def Sentencia():
    if SentFor()
    else :
        SentWhile()
    else :
        Expr()
    else:
        SentIf()
    else :
        SentenciaCompuesta()
    else:
        Declaracion()

#<SentFor> → for (<Expr> , <Expr>, <Expr>) <Sentencia>
#<SentFor> → for (<Expr> , ,<Expr>) <Sentencia>
#<SentFor> → for (<Expr> , <Expr>, ) <Sentencia>
#<SentFor> → for (<Expr> , , ) <Sentencia>
def SentFor():
    if "for":
        derivaciones.append("for")
    elif "(":
        derivaciones.append("(")
    elif Expr()
    elif ",":
        derivaciones.append(",")
    elif Expr()
    elif ",":
        derivaciones.append(",")
    elif Expr()
    elif ")":
        derivaciones.append(")")
    elif Sentencia()
    else:
        if "for":
            derivaciones.append("for")
        elif "(":
            derivaciones.append("(")
        elif Expr()
        elif ",":
            derivaciones.append(",")
        elif " "
        elif ",":
            derivaciones.append(",")
        elif Expr()
        elif ")":
            derivaciones.append(")")
        elif Sentencia()
    else:
        if "for":
            derivaciones.append("for")
        elif "(":
            derivaciones.append("(")
        elif Expr()
        elif ",":
            derivaciones.append(",")
        elif Expr()
        elif ",":
            derivaciones.append(",")
        elif " "
        elif ")":
            derivaciones.append(")")
        elif Sentencia()
    else:
        if "for":
            derivaciones.append("for")
        elif "(":
            derivaciones.append("(")
        elif Expr()
        elif ",":
            derivaciones.append(",")
        elif " "
        elif ",":
            derivaciones.append(",")
        elif " "
        elif ")":
            derivaciones.append(")")
        elif Sentencia()

#<SentWhile> → while (<Expr>) <Sentencia>
def SentWhile():
    if while()
    elif "(":
        derivaciones.append("(")
    elif ")":
        derivaciones.append(")")
    elif Expr()
    elif Sentencia()

#<Expr> → <identificador>:= <Expr>
#<Expr> → <ValorR>
def Expr():
    if Identeficador():
    elif ":=":
        derivaciones.append(":=")
    elif Expr()
else:
    if ValorR()

#<ValorR> → <Mag><X>
#<ValorR> → <Mag>
def ValorR():
    if Mag()
    elif X()
    else:
        if Mag()

#<X> →  <Comparacion><Mag>
#<X> →  <Comparacion><Mag><X>
def X():
    if Comparacion()
    elif Mag()
else:
    if Comparacion()
    elif Mag()
    elif X()

#<Comparacion> → ==
#<Comparacion> → >
#<Comparacion> → <
#<Comparacion> → >=
#<Comparacion> → <=
#<Comparacion> → !=
def Comparacion():
    if "==":
        derivaciones.append("==")
else:
    if ">":
        derivaciones.append(">")
else:
    if "<":
        derivaciones.append("<")
else:
    if ">=":
        derivaciones.append(">=")
else:
    if "<=":
        derivaciones.append("<=")
else:
    if "!=":
        derivaciones.append("!=")

#<Mag> → <Termino> <Mag2>
def Mag():
    if Termino()
    elif Mag2()

#<Mag2> → - <Termino> <Mag2>
#<Mag2> → + <Termino> <Mag2>
def Mag2():
    if "-":
        derivaciones.append("-")
    elif Termino()
    elif Mag2()
else:
    if "+":
        derivaciones.append("+")
    elif Termino()
    elif Mag2()

#<Termino> →  <Factor> <Termino2>
def Termino():
    if Factor()
    elif Termino2()

#<Termino2> → / <Factor> <Termino2>
#<Termino2> →  * <Factor> <Termino2>
def Termino2():
    if "/":
        derivaciones.append("/")
    elif Factor()
    elif Termino2()
else:
    if "*":
        derivaciones.append("*")
    elif Factor()
    elif Termino2()

#<SentIf> → if (<Expr>) <Sentencia> else(<Sentencia>)
#<SentIf> → if (<Expr>) <Sentencia>
def SentIf():
    if "if":
        derivaciones.append("if")
    elif "(":
        derivaciones.append("(")
    elif Expr()
    elif ")":
        derivaciones.append(")")
    elif Sentencia()
    elif "else":
        derivaciones.append("else")
    elif "(":
        derivaciones.append("(")
    elif ")":
        derivaciones.append(")")
    elif Sentencia()
else:
    if "if":
        derivaciones.append("if")
    elif "(":
        derivaciones.append("(")
    elif Expr()
    elif ")":
        derivaciones.append(")")
    elif Sentencia()

#<Declaracion> → <Tipo><ListaIdent> ;
def Declaracion():
    if Tipo()
    elif ListaIdent()
    elif ";":
        derivaciones.append(";")

#<ListaIdent> → <Identificador> , <ListaIdent>
#<ListaIdent> → <Identificador>
def ListaIdent():
    if Identificador()
    elif ",":
        derivaciones.append(",")
    elif ListaIdent()
    else:
        if Identificador()

#<Factor> →  (<Expr>)
#<Factor> →  + <Factor>
#<Factor> →  - <Factor>
#<Factor> → <Numero>
#<Factor> → <Identificador>
def Factor():
    if "(":
        derivaciones.append("(")
    elif Expr()
    elif ")":
        derivaciones.append(")")
else:
    if "+":
        derivaciones.append("+")
    elif Factor()
else:
    if "-":
        derivaciones.append("-")
    elif Factor()
else:
    if Numero()
else:
    if Identificador()
