samogloski = ['a', 'e', 'i', 'o', 'u', 'ą', 'ę', 'ó']

def licz_samo(text='',samo=0):
    for char in text:
        if char in samogloski:
            samo += 1
    print(f'Liczba samogłosek w zdaniu {text}  to -> {samo}')

licz_samo(text="Ala ma kota")