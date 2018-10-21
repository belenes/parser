from lexer import lexer

backtrack_id = 0
token_idex = 0


def principal(tokens):
    tokens = tokens + $
    error = False
    n = 0
    s(n)
    if (error == False) and (tokens[n] == $):
        Pertenece == True
        return listaProducciones
    else:
        Pertenece == False

def s():
    j = 0
    aux = n
    while (error == True) and (j < k):
        n = aux
        error = False
        procesar( p(0,1), n )
        j = j + 1

def procesar( q, pw):

def parser(listaTokens, cadena):
    pertenece(cadena)
    return listaProducciones

def pertenece():
    while (error == False):
        for i = 0 range (0, len(cadena)):
            if (proximo == cadena[i]):
                proximo = proximoToken()
            else:

                error = True


listaNoTerminales = [
Funcion(),
ListaArgumentos(),
Argumento(),
Declaracion(),
Tipo(),
ListaIdent(),
Sentencia(),
SentFor(),
SentWhile(),
SentIf(),
SentenciaCompuesta(),
ListaSentencia(),
Expr(),
ValorR(),
X(),
Comparacion(),
Mag(),
Mag2(),
Termino(),
Termino2(),
Factor()
]




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
