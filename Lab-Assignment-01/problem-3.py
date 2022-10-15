""" -----------------------------------------------------------------------------------------------------

Go to this repo: https://pypi.org/project/pyjokes/ and try to make a chat bot to tell you joke using pyjokes.
Write a function named tell_some_jokes() and write your code inside this function.

-------------------------------------------------------------------------------------------------------"""

def tell_some_jokes():
    import pyjokes

    while 1:
        comand = input("I am you joker bot, comand me \n")

        if(comand == "tell a joke" or comand == "another one"):
            print(pyjokes.get_joke(language="en", category="neutral"))
        else:
            print("Good buy")
            break


tell_some_jokes()


