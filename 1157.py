w=input().upper()
ans=[w.count(chr(c)) for c in range (ord('A'), ord('Z')+1)]

max_alpha=max(ans)
if ans.count(max_alpha)==1:
    print(chr(ans.index(max_alpha)+ord('A')))
else:
    print('?')