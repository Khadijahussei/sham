# st="mango,banana,orange,passion,strawberry,apple"
# t=[]
# for i in st:
#     if i not in t:
#         t.append(i)
# print(t)
# for p in t:
#    q=st.count(p)
#    print(f"{p}--{q}")
    
    
    
a=input("enter  a letter")
t=0
for i in a:
    if i.isdigit():
        t+=1
print(f"There are {t} digits in total")
    