samogloski = ['a', 'e', 'i', 'o', 'u', 'ą', 'ę', 'ó']
krotka_samo={}

def licz_samo(text='',samo=0):
    text=text.split()
    for word in text:
        for char in word:
            if char in samogloski:
                samo += 1
    krotka_samo[text] = samo
    for word, count in krotka_samo.items():
        print(f'Liczba samogłosek w zdaniu {word}  to -> {count}')

licz_samo(text="Ala ma kota")