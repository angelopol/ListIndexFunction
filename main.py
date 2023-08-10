def ListIndexFunction():

    """
    Funcion que almacena strings en una lista con la funcion "append" y despues de tener 4 elementos te pide que busques la posicion de alguno
    usando la funcion "index".

    list = variable donde se alamcenan los strings
    """

    list = []

    # ciclo infinito.
    while True:

        list.append(input("type a word "))

        # ciclo que comienza cuando la lista tenga mas de 3 elementos.
        while len(list) > 3:

            try:

                print(list.index(input("search a entered word ")))

            except:
                # si el usuario introduce datos no deseados imprime este mensaje de error.
                print("the word is not registered in the list")