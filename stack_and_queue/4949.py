while(True):
    word=input()

    s = []
    if word=='.':
        break

    for w in word:
        if w=='(' or w=='[':
            s.append(w)
        elif w==')':
            if len(s)!=0 and s[-1]=='(':
                s.pop()
            else:
                s.append(w)
                break
        elif w==']': 
            if len(s)!=0 and s[-1]=='[':
                s.pop()
            else:
                s.append(w)
                break

    if len(s)==0:
        print('yes')
    else:
        print('no')