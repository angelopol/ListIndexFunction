def ListIndexFunction():

    list = []

    while True:

        list.append(input("type a word "))

        while len(list) > 3:

            try:

                print(list.index(input("search a entered word ")))

            except:

                print("the word is not registered in the list")