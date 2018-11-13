from lexer import lexer

#Lista de simbolos terminales
VT = [
    "Int",
    "Float",
    "If",
    "Else",
    "For",
    "While",
    "(",
    ")",
    "{",
    "}",
    "+",
    "-",
    "*",
    "/",
    ",",
    ";",
    ":=",
    "<",
    ">",
    ">=",
    "<=",
    "!=",
    "==",
    "Numero",
    "Identificador",
    "ERROR_TP"
]

#Lista de simbolos no terminales
VN = [
    'Funcion',
    'ListaArgumentos',
    'Argumento',
    'Declaracion',
    'Tipo',
    'ListaIdent',
    'Sentencia',
    'SentFor',
    'SentWhile',
    'SentIf',
    'SentenciaCompuesta',
    'ListaSentencia',
    'Expr',
    'ValorR',
    'X',
    'Comparacion',
    'Mag',
    'Mag2',
    'Termino',
    'Termino2',
    'Factor'
]

producciones = {

'Funcion': [
    ["Tipo", "Identificador", "(", "ListaArgumentos", ")", "SentenciaCompuesta"]
],

'ListaArgumentos': [
    ["Argumento"],
    ["Argumento", ",", "ListaArgumentos"]
],

'Argumento': [
    ["Tipo", "Identificador"]
],

'Declaracion': [
    ["Tipo", "ListaIdent"]
],

'Tipo': [
    ["Int"],
    ["Float"]
],

'ListaIdent': [
    ["Identificador"],
    ["Identificador", ",", "ListaIdent"]
],

'Sentencia': [
    ["Declaracion"],
    ["SentFor"],
    ["SentWhile"],
    ["Expr"],
    ["SentIf"],
    ["SentenciaCompuesta"],
    [";"]
],

'SentFor': [
    ["For", "(", "Expr", ",", "Expr", ",", "Expr", ")", "Sentencia"],
    ["For", "(", "Expr", ",", ",", "Expr", ")", "Sentencia"],
    ["For", "(", "Expr", ",", "Expr", ",", ")", "Sentencia"],
    ["For", "(", "Expr", ",", ",", ")", "Sentencia"]
],

'SentWhile': [
    ["While", "(", "Expr", ")", "Sentencia"]
],

'SentIf': [
    ["If", "(", "Expr", ")", "Sentencia", "Else", "(", "Sentencia", ")"],
    ["If", "(", "Expr", ")", "Sentencia"]
],

'SentenciaCompuesta': [
    ["{", "ListaSentencia", "}"]
],

'ListaSentencia': [
    ["Sentencia"],
    ["Sentencia", "ListaSentencia"]
],

'Expr': [
    ["ValorR"],
    ["Identificador", ":=", "Expr"]
],

'ValorR': [
    ["Mag"],
    ["Mag", "X"]
],

'X': [
    ["Comparacion", "Mag"],
    ["Comparacion", "Mag", "X"]
],

'Comparacion': [
    ["=="],
    [">"],
    ["<"],
    [">="],
    ["<="],
    ["!="]
],

'Mag': [
    ["Termino"],
    ["Termino", "Mag2"]
],

'Mag2': [
    ["-", "Termino"],
    ["+", "Termino"],
    ["-", "Termino", "Mag2"],
    ["+", "Termino", "Mag2"]
],

'Termino': [
    ["Factor"],
    ["Factor" "Termino2"]
],

'Termino2': [
    ["/", "Factor"],
    ["*", "Factor"],
    ["/", "Factor", "Termino2"],
    ["*", "Factor", "Termino2"]
],

'Factor': [
    ["(", "Expr", ")"],
    ["+", "Factor"],
    ["-", "Factor"],
    ["Numero"],
    ["Identificador"]
]
}

estado = {
'tokens': [],
'puntero': 0,
'error': False,
'producciones': []
}


def obtenertokens(src):
    lista = []
    cadena = lexer(src)

    for token in cadena:
        lista.append(token[0])
    lista.append('#') #Simbolo de fin de candena
    return lista


def parser(src):
    estado['puntero'] = 0
    estado['error'] = False
    estado['tokens'] = obtenertokens(src)
    cadena = estado['tokens']

    pn('Funcion')

    if estado['error'] == False and cadena[estado['puntero']] == '#':
        print('La candena: ', cadena , 'PERTENECE al lenguaje')
        print(estado['producciones'])
        return True
    else:
        print('La candena: ', cadena , 'NO PERTENECE al lenguaje')
        print(estado['producciones'])
        return False


def pn(noTerminal):
    puntero_original = estado['puntero']

    for parteDerecha in producciones[noTerminal]:
        estado['error'] = False
        estado['puntero'] = puntero_original
        procesar(parteDerecha)
        if estado['error'] == True:
             estado['puntero'] = puntero_original
        else:
            estado['producciones'].append(noTerminal)
            estado['producciones'].append(parteDerecha)
            break


def procesar(parteDerecha):
    estado['error'] = False
    cadena = estado['tokens']

    for simbolo in parteDerecha:
            if simbolo in VT:
                if simbolo == cadena[estado['puntero']]:
                    estado['puntero'] = estado['puntero'] + 1
                else:
                    estado['error'] = True
                    break
            if simbolo in VN:
                pn(simbolo)
                if estado['error'] == True:
                    break






print(1)
assert parser('float variable ( int variable ) { float var }') == True
print(2)
assert parser('int') == False
print(3)
assert parser('int hola ( int var , for ) { 25 }') == False
print(4)
assert parser('float var ( float ab ) { abc }') == True
print(5)
assert parser('int var ( float ab ) { 6 }') == True
print(6)
assert parser('float word ( int var ) { while ( 25 ) hola }') == True
print(7)
assert parser('int palabra (int palabra ) { for ( 15 , 30 , 1 ) hacer }') == True
print(8)
assert parser('float variable (float var) { if then }') == False
print(9)
assert parser('variable int (variable float)') == False
print(10)
assert parser('int hola ( float beta ) { 34 }') == True
