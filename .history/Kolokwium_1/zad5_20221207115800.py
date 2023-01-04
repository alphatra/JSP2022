samogloski = ['a', 'e', 'i', 'o', 'u', 'ą', 'ę', 'ó']
krotka_samo={}

def licz_samo(text='',samo=0):
    text=text.split()
    for char in text:
        if char in samogloski:
            samo += 1
    krotka_samo[text] = samo

    print(f'Liczba samogłosek w zdaniu {text}  to -> {samo}')

licz_samo(text="Ala ma kota")