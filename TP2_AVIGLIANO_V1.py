# hola soy un parser

from avigliano_lexer_v3 import lexer

derivaciones=[]

def Principal (tokens):

    contador = 0
    error = False
    ProcedureN()
    if error==False and FinCadena == True :
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
        Cosa = tuplas[0]

# derivacion desde el simbolo inicial
def SimboloInicial (Cosa):
    auxiliar = [<Funcion>]
    if Tipo():
    elif Identificador()
    elif "("
    elif ListaArgumentos()
    elif ")"
    elif SentenciaCompuesta()

def Tipo():
    auxiliar.append(<Tipo>)
    if "Int" == Cosa
        derivaciones.append(auxiliar.append(Int))
    elif "Float" == Cosa
        derivaciones.append(<Funcion><Tipo><Int>)

def Identificador():


def ListaArgumentos():
    if Argumento()
    else :
        if Argumento()
        elif ","
        elif ListaArgumentos()

def Argumento():
    if Tipo()
    elif Identificador()



def SentenciaCompuesta():
    if "{"
    elif ListaSentencia()
    elif "}"

def ListaSentencia():
    if Sentencia()
    else:
        if Sentencia()
        elif ListaSentencia()

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

def SentFor():
    if "for"
    elif "("
    elif Expr()
    elif ","
    elif Expr()
    elif ","
    elif Expr()
    elif ")"
    elif Sentencia()
    else:
        if "for"
        elif "("
        elif Expr()
        elif ","
        elif " "
        elif ","
        elif Expr()
        elif ")"
        elif Sentencia()
    else:
        if "for"
        elif "("
        elif Expr()
        elif ","
        elif Expr()
        elif ","
        elif " "
        elif ")"
        elif Sentencia()
    else:
        if "for"
        elif "("
        elif Expr()
        elif ","
        elif " "
        elif ","
        elif " "
        elif ")"
        elif Sentencia()

def SentWhile():
    if while()
    elif "("
    elif ")"
    elif Expr()
    elif Sentencia()

def Expr():
    if Identeficador():
    elif ":"
    elif "="
    elif Expr()
else:
    if ValorR()

def ValorR():
    if Mag()
    elif X()
    else:
        if Mag()

def X():
    if Comparacion()
    elif Mag()
else:
    if Comparacion()
    elif Mag()
    elif X()

def Comparacion():
    if "=="
else:
    if ">"
else:
    if "<"
else:
    if "="
    elif">"
else:
    if "="
    elif"<"
else:
    if "!"
    elif "="

def Mag():
    if Termino()
    elif Mag2()

def Mag2():
    if "-"
    elif Termino()
    elif Mag2()
else:
    if "+"
    elif Termino()
    elif Mag2()

def Termino():
    if Factor()
    elif Termino2()

def SentIf():
    if "if"
    elif "("
    elif Expr()
    elif ")"
    elif Sentencia()
    elif "else"
    elif "("
    elif ")"
    elif Sentencia()
else:
    if "if"
    elif "("
    elif Expr()
    elif ")"
    elif Sentencia()

def Declaracion():
    if Tipo()
    elif ListaIdent()
    elif ";"

def ListaIdent():
    if Identificador()
    elif ","
    elif ListaIdent()
    else:
        if Identificador()

def Termino2():
    if "/"
    elif Factor()
    elif Termino2()
else:
    if "*"
    elif Factor()
    elif Termino2()
def Factor():
    if "("
    elif Expr()
    elif")"
else:
    if "+"
    elif Factor()
else:
    if "-"
    elif Factor()
else:
    if Numero()
else:
    if Identificador()



#<Funcion> →  <Tipo> <Identificador> ( <ListaArgumentos> ) <SentenciaCompuesta>
#<ListaArgumentos> → <Argumento>
#<ListaArgumentos> → <Argumento> , <ListaArgumentos>
#<Argumento> → <Tipo><Identificador>
#<Declaracion> → <Tipo><ListaIdent> ;
#<Tipo> → int
#<Tipo> → float
#<ListaIdent> → <Identificador> , <ListaIdent>
#<ListaIdent> → <Identificador>
#<Sentencia> → <SentFor>
#<Sentencia> → <SentWhile>
#<Sentencia> → <Expr> ;
#<Sentencia> → <SentIf>
#<Sentencia> → <SentenciaCompuesta>
#<Sentencia> → <Declaracion> ;
#<SentFor> → for (<Expr> , <Expr>, <Expr>) <Sentencia>
#<SentFor> → for (<Expr> , ,<Expr>) <Sentencia>
#<SentFor> → for (<Expr> , <Expr>, ) <Sentencia>
#<SentFor> → for (<Expr> , , ) <Sentencia>
#<SentWhile> → while (<Expr>) <Sentencia>
#<SentIf> → if (<Expr>) <Sentencia> else(<Sentencia>)
#<SentIf> → if (<Expr>) <Sentencia>
#<SentenciaCompuesta> → {<ListaSentencia>}
#<ListaSentencia> → <Sentencia>
#<ListaSentencia> → <Sentencia><ListaSentencia>
#<Expr> → <identificador>:= <Expr>
#<Expr> → <ValorR>
#<ValorR> → <Mag><X>
#<ValorR> → <Mag>
#<X> →  <Comparacion><Mag>
#<X> →  <Comparacion><Mag><X>
#<Comparacion> → ==
#<Comparacion> → >
#<Comparacion> → <
#<Comparacion> → =>
#<Comparacion> → =<
#<Comparacion> → !=
#<Mag> → <Termino> <Mag2>
#<Mag2> → - <Termino> <Mag2>
#<Mag2> → + <Termino> <Mag2>
#<Termino> →  <Factor> <Termino2>
#<Termino2> → / <Factor> <Termino2>
#<Termino2> →  * <Factor> <Termino2>
#<Factor> →  (<Expr>)
#<Factor> →  + <Factor>
#<Factor> →  - <Factor>
#<Factor> → <Numero>
#<Factor> → <Identificador>

