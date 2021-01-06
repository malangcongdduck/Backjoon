n=int(input())
count=0

for i in range(n):
    word=input()
    if list(word)==sorted(word,key=word.find):
        #key값을 기준으로 오름차순 정렬
        #word를 key값인 처음 나오는 문자의 인덱스를 기준으로 오름차순 정렬한다
        #happy면 h a p p y
        #natural이면 n a a t u r l
        count+=1
print(count)

#더한갯수- (처음 인덱스-끝인덱스) == 1이면 그룹단어
