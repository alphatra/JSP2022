samogloski = ['a', 'e', 'i', 'o', 'u', 'ą', 'ę', 'ó']
krotka_samo={}

def licz_samo(text='',samo=0):
    text = text.lower()
    text=text.split()
    for word in text:
        samo=0
        for char in word:
            if char in samogloski:
                samo+=1
                krotka_samo[word]=samo
    krotka_samo[word] = samo
    suma = 0
    for word, count in krotka_samo.items():
        suma+=count
        print(f'Liczba samogłosek w zdaniu {word} to -> {count}')
    print(f'suma to {suma}')
licz_samo(text="Ala ma kota")
