#Automatas
def a_int(src):
    s = 1
    for c in src:
        if s == 1 and c == "i":
            s = 2
        elif s == 2 and c == "n":
            s = 3
        elif s == 3 and c == "t":
            s = 4
        else:
            s = -1
            break
    return s == 4

def a_float(src):
    s = 1
    for c in src:
        if s == 1 and c == 'f':
            s = 2
        elif s == 2 and c == 'l':
            s = 3
        elif s == 3 and c == 'o':
            s = 4
        elif s == 4 and c == 'a':
            s = 5
        elif s == 5 and c == 't':
            s = 6
        else:
            s = -1
            break
    return s == 6

def a_if(src):
    s = 1
    for c in src:
        if s == 1 and c=='i':
            s = 2
        elif s == 2 and c=='f':
            s = 3
        else:
            s = -1
            break
    return s == 3

def a_for(src):
    s = 1
    for c in src:
        if s == 1 and c == 'f':
            s = 2
        elif s == 2 and c=='o':
            s = 3
        elif s == 3 and c =='r':
            s = 4
        else:
            s = -1
            break
    return s == 4

def a_while(src):
    s = 1
    for c in src:
        if s == 1 and c == "w":
            s = 2
        elif s == 2 and c == "h":
            s = 3
        elif s == 3 and c == "i":
            s = 4
        elif s == 4 and c == "l":
            s = 5
        elif s == 5 and c == "e":
            s = 6
        else:
            s = -1
            break
    return s == 6

def a_ParAbierto(src):
    s = 1
    for c in src:
        if s == 1 and c=="(":
            s = 2
        else:
            s = -1
            break
    return s == 2

def a_ParCerrado(src):
    s = 1
    for c in src:
        if s == 1 and c==")":
            s = 2
        else:
            s = -1
            break
    return s == 2

def a_LLaAbierta(src):
    s = 1
    for c in src:
        if s==1 and c=="{":
            s = 2
        else:
            s = -1
            break
    return s == 2

def a_LLaCerrada(src):
    s = 1
    for c in src:
        if s == 1 and c=="}":
            s = 2
        else:
            s = -1
            break
    return s == 2

def a_Mas(src):
    s = 1
    for c in src:
        if s == 1 and c == '+':
            s = 2
    return s == 2

def a_Menos(src):
    s = 1
    for c in src:
        if s == 1 and c=='-':
            s = 2
        else:
            s = -1
            break
    return s == 2

def a_Por(src):
    s = 1
    for c in src:
        if s == 1 and c == '*':
            s = 2
        else:
            s = -1
            break
    return s == 2

def a_Dividido(src):
    s = 1
    for c in src:
        if s == 1 and c=='/':
            s = 2
        else:
            s = -1
            break
    return s == 2

def a_Coma(src):
    s = 1
    for c in src:
        if s == 1 and c==',':
            s = 2
        else:
            s = -1
            break
    return s == 2

def a_PuntoComa(src):
    s = 1
    for c in src:
        if s == 1 and c == ';':
            s = 2
        else:
            s = -1
            break
    return s == 2

def a_PuntoIgual(src):
    s = 1
    for c in src:
        if s == 1 and c ==':':
            s = 2
        elif s == 2 and c == '=':
            s = 3
        else:
            s = -1
            break
    return s == 3

def a_Igual(src):
    s = 1
    for c in src:
        if s == 1 and c == '=':
            s = 2
        else:
            s = -1
            break
    return s == 2

def a_Menor(src):
    s = 1
    for c in src:
        if s == 1 and c == '<':
            s = 2
        else:
            s = -1
            break
    return s == 2

def a_Mayor(src):
    s = 1
    for c in src:
        if s == 1 and c == '>':
            s = 2
        else:
            s = -1
            break
    return s == 2

def a_MayorIgual(src):
     s = 1
     for c in src:
         if s == 1 and c == '>':
             s = 2
         elif s == 2 and c == '=':
             s = 3
         else:
            s = -1
            break
     return s == 3

def a_MenorIgual(src):
    s = 1
    for c in src:
        if s == 1 and c == '<':
            s = 2
        elif s == 2 and c == '=':
            s = 3
        else:
            s = -1
            break
    return s == 3

def a_Distinto(src):
    s = 1
    for c in src:
        if s == 1 and c == '!':
            s = 2
        elif s == 2 and c == '=':
            s = 3
        else:
            s = -1
            break
    return s == 3

def a_IgualIgual(src):
    s = 1
    for c in src:
        if s == 1 and c == '=':
            s = 2
        elif s == 2 and c == '=':
            s = 3
        else:
            s = -1
            break
    return s == 3

def a_Num(src):
    s = 1
    for c in src:
        if s == 1 and c.isdigit():
            s = 2
        elif s == 2 and c.isdigit():
            s = 2
        else:
            s = -1
            break
    return s == 2

def a_Id(src):
    s = 1
    for c in src:
        if s == 1 and c.isalpha():
            s = 2
        elif s == 2 and c.isalpha():
            s = 2
        else:
            s = -1
            break
    return s == 2

def ERROR_TOKEN_PARCIAL(src):
    s = 1
    for c in src:
        if s == 1 and c == ":":
            s = 2
        elif s == 1 and c == "!":
            s = 2
        elif s == 1 and c == "=":
            s = 2
        else:
            s = -1
            break
    return s == 2

Token_Clasificacion = [
      ("Int", a_int),
      ("Float", a_float),
      ("If", a_if),
      ("For", a_for),
      ("While", a_while),
      ("(", a_ParAbierto),
      (")", a_ParCerrado),
      ("{", a_LLaAbierta),
      ("}", a_LLaCerrada),
      ("+", a_Mas),
      ("-", a_Menos),
      ("*", a_Por),
      ("/", a_Dividido),
      (",", a_Coma),
      (";", a_PuntoComa),
      (":=", a_PuntoIgual),
      ("Comparacion", a_Menor),
      ("Comparacion", a_Mayor),
      ("Comparacion", a_MayorIgual),
      ("Comparacion", a_MenorIgual),
      ("Comparacion",a_Distinto),
      ("Comparacion", a_IgualIgual),
      ("Numero", a_Num),
      ("Identificador", a_Id),
      ("ERROR_TP", ERROR_TOKEN_PARCIAL)
]

def lexer(src):
    tokens = []
    src = src + " "
    i = 0
    start = 0
    state = 0
    while i<len(src):
        c = src[i]
        word = src[start: i+1]
        if state == 0:
            if c.isspace():
                i+=1
                state = 0
            else:
                start = i
                state = 1
        elif state == 1:
            if es_aceptada(word) and not c.isspace():
                i+=1
                state = 1
            else:
                i-=1
                state = 2
        elif state == 2:
            candidatos = []
            candidatos = calc_candidatos(word)
            if len(candidatos) > 0:
                if candidatos[0] == "ERROR_TP":
                    print ("ERROR_TP: La candena ingresada es invalida")
                else:
                    token = (candidatos[0], word)
                    tokens.append(token)
            else:
                tokens = []
                print ("ERROR: La cadena ingresada es invalida")
                return tokens
            i+=1
            start = i
            state = 0
        else:
            print("ERROR: Cadena no aceptada")
    return tokens



def es_aceptada(word):
    candidatos = calc_candidatos(word)
    if len(candidatos) > 0:
        return True
    else:
        return False


def calc_candidatos(word):
    candidatos = []
    for (clasi, afd) in Token_Clasificacion:
          if afd(word):
                candidatos.append(clasi)
    return candidatos

print ("1", lexer("for{ x>5, y<=26 };"))
print ("2", lexer("while (abc - 6)*77 float 553 "))
print ("3", lexer("float hola := 123"))
print ("4", lexer("  % "))
print ("5", lexer("  != kkkk ;"))
print ("6", lexer(" if >= { 123 } ac / hola (10-5)"))
print ("7", lexer(" int >= 885232 + asd (x/655622) "))
print ("8", lexer(" abc123"))
print ("9", lexer("(x>4,55) int ((8*8)/(56+265)) ;"))
print ("10", lexer(" : "))
