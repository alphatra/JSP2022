samogloski = ['a', 'e', 'i', 'o', 'u', 'ą', 'ę', 'ó']
krotka_samo={}

def licz_samo(text='',samo=0):
    text = text.lower()
    text=text.split()
    print(text)
    for word,x in text:
        print(word,x)
        for char in word:
            print(char)
            if char in samogloski:
                samo+=1
                krotka_samo[word]=samo
            
    krotka_samo[word] = samo
    for word, count in krotka_samo.items():
        print(f'Liczba samogłosek w zdaniu {word}  to -> {count}')
    print(krotka_samo)

licz_samo(text="Ala ma ")
