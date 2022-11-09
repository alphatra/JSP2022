import re

password = input("Podaj hasło")
match len(password) > 6 and len(password) <12:
    case True:
        match re.search(["a-zA-Z\d",password]):
            case True:
                pass
            case False:
                print("hasło powinno zawierać litery od a-z, A-Z oraz cyfry 0-9")
        match re.search(["$#@",password]):
            case True:
                pass
            case False:
                print("hasło powinno zawierać znaki $#@")
    case False:
        print("Długość hasła powinna być większ niz 6 oraz mniejsza niz 12")

