import sys
s=input()
if s =="C":
    s1=""
    s2=""
    d="0"
    sn=""
    while True:
        d=input()
        b=0
        if d in "Cc":
            print("Calculator off")
            b=1
            break
        if d.isdigit():
            s1=s1+d
            print(s1)
        elif d in "+-*/^":
            print(d)
            if sn=="":
                s2=s1
                s1=""
                sn=d
                continue
            elif sn=="+":
                c=float(s2)+float(s1)
                s2=str(c)
                print(s2)
                s1=""
                sn=d
                continue
            elif sn=="-":
                c=float(s2)-float(s1)
                s2=str(c)
                print(s2)
                s1=""
                sn=d
                continue
            elif sn=="*":
                c=float(s2)*float(s1)
                s2=str(c)
                print(s2)
                s1=""
                sn=d
                continue
            elif sn=="/":
                c=float(s2)/float(s1)
                s2=str(c)
                print(s2)
                s1=""
                sn=d
                continue
            elif sn=="^":
                c=float(s2)**float(s1)
                s2=str(c)
                print(s2)
                s1=""
                sn=d
                continue
        elif d=="=":
            print(d)
            if s1=="":
                print(s2)
                continue
            if sn == "+":
                c = float(s2) + float(s1)
            elif sn == "-":
                c = float(s2) - float(s1)
            elif sn == "*":
                c = float(s2) * float(s1)
            elif sn == "/":
                c = float(s2) / float(s1)
            elif sn == "^":
                c = float(s2) ** float(s1)
            s2=str(c)
            print(s2)
            s1=""
            sn=""
            continue
    if b==1:
        sys.exit()
