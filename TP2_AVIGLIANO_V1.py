from lexer import lexer

#esto viene del Lexer
listaTokens = tokens

#Constantes para operar
Lexeme = 2
Puntero = 0

# esto me da el primer token para comparar
proximo = proximoToken()

#El parser debe devolver las producciones si la cadena pertenece
def parser(listaTokens, cadena):
    pertenece(cadena)
    return listaProducciones

#Para darle el siguiente para el analisis
def proximoToken:
    simboloDesignado = listaTokens[Puntero[Lexeme]]
    return simboloDesignado
#Se fija si pertenece, chequeando los tokens con la cadena
def pertenece():
    while (error == False):
        for i=0 range(0, len(cadena)):
            if (proximo == cadena[i]):
                proximo = proximoToken()
            else:
                error = True
                break

#Los no terminales empiezan acá
def funcion:
    if (proximo == simbolo):
    else:
        error = True
#
#Lista de los no terminales completar con todas, falta terminar
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
