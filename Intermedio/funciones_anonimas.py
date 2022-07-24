#lambda argumentos : expresion
#las fuinciones lambda solo permite una linea de codigo y se almacena en una 
#sola variable, para el ejemplo, se almacena en palindrome

#ejemplo de palindromo con funcion lambda
palindrome=lambda string:string == string[::-1]

def run():
    print(palindrome("anita laba la tina"))

if __name__ == "__main__":
    run()

