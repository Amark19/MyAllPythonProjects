from gingerit.gingerit import GingerIt
text = 'Donald Trump lose the presendential election, Joe Biden is the new president of Amrica.'
result = GingerIt().parse(text)
print(result['result'])
n=len(list(result['corrections']))
d=[]
a=[]
for i in range(n):
    dash=list(result['corrections'][i].items())
    d.append(dash[0][1])
d.reverse()
i=0
while i<(len(result['text'])):
    if i in d: 
        for j in range(i,len(result['text'])):
            if result['text'][j]==" ":
                break
        a.append("\u0332".join(text[i:j+1]))
        # print("\u0332".join(text[i]))
        i=j
    else:
        a.append(result['text'][i])
    i+=1 
text=""
for i in a:
    text+=i


