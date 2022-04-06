
def shifr_cez():
    lang_=[chr(i) for i in range(65,91)]+[chr(j) for j in range(97,123)]
    for i in range(len(k)):
            if k[i].isalpha():
                    if k[i].isupper():
                        print(lang_[(lang_.index(k[i]) + zdv) % moch], end = '')
                    else:
                        print(lang_[(lang_.index(k[i]) + zdv) % moch + moch], end='')
            else:
                print(k[i], end='')
txt_=[i for i in input().split(' ')]
moch=26
zdv=0
k=''
for i in txt_:
    for h in i:
        if h.isalpha():
            zdv+=1
        k+=h   
    shifr_cez()
    zdv=0
    k=' '