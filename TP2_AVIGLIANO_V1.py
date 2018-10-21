from lexer import lexer


def parser(tokenType, lexeme):
    backtrack_id = 0
    tokens = tokens
    token_idex = 0


def principal(src):
    error = False
    n = 0
    s(n)
    if (error == False) and (w[n] == $):
        wPertenece == True
    else:
        wPertenece == False

def S(n):
    j = 0
    aux = n
    while (error == True) and (j < k):
        n = aux
        error = False
        procesar( p(0,1), n )
        j = j + 1

def procesar( q, pw):



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
