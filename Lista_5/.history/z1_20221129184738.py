def Slownie (Liczba):    
    Liczby = [
        [''         ,''               ,''                 ,''            ],
        ['jeden '   ,'jedenaście '    ,'dziesięć '        ,'sto '        ],
        ['dwa '     ,'dwanaście '     ,'dwadzieścia '     ,'dwieście '   ],
        ['trzy '    ,'trzynaście '    ,'trzydzieści '     ,'trzysta '    ],
        ['cztery '  ,'czternaście '   ,'czterdzieści '    ,'czterysta '  ],
        ['pięć '    ,'piętnaście '    ,'pięcdziesiąt '    ,'pięćset '    ],
        ['sześć '   ,'szesnaście '    ,'sześćdziesiąt '   ,'sześćset '   ],
        ['siedem '  ,'siedemnaście '  ,'siedemdziesiąt '  ,'siedemset '  ],
        ['osiem '   ,'osiemnaście '   ,'osiemdziesiąt '   ,'osiemset '   ],
        ['dziewięć ','dziewiętnaście ','dziewięćdziesiąt ','dziewięćset ']]

    Grupy = [
        [''        ,''         ,''          ],
        ['tysiąc ' ,'tysiące ' ,'tysięcy '  ],
        ['milion ' ,'miliony ' ,'milionów ' ],
        ['miliard ','miliardy ','miliardów '],
        ['bilion ' ,'biliony ' ,'bilionów ' ],
        ['biliard ','biliardy ','biliardów '],
        ['trylion ','tryliony ','trylionów ']]

    J, N, D, S, G, K = 0, 0, 0, 0, 0, 0     #Jednostki,Nastki,Dziesiatki,Setki,Grupy,Koncowki
    Ciag, Znak = "", ""
    
    if Liczba < 0:
        Znak = "minus "
        Liczba = -Liczba
    if Liczba == 0:
        Ciag = "zero "
    while not Liczba == 0:
        S = Liczba % 1000 // 100
        D = Liczba % 100 // 10
        J = Liczba % 10
        if D == 1 and J > 0:                #Warunek do obsługi nastek
            N = J
            D = 0
            J = 0
        else:
            N = 0
        if J == 1:                          #Tu zawiera sie cała gramatyka, wybór końcówki
            if S + D + N > 0:
                K = 2
            else:
                K = 0;
        elif J in [2,3,4]:
            K = 1
        else:
            K = 2        
        if S + D + N + J > 0:
            Ciag = Liczby[S][3] + Liczby[D][2] + Liczby[N][1] + Liczby[J][0] + Grupy[G][K] + Ciag
        G = G + 1
        Liczba = Liczba // 1000;
    return Znak + Ciag
Slownie(12)
