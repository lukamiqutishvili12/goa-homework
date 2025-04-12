#გააკეთეთ Sum Of Even Numbers. მიზანი: შეკრიბეთ ყველა ლუწი რიცხვი და შეინახეთ სიაში შემდეგ ეგ სია დაპრინტეთ 10 ჯერ
list = [1,2,3,4,5,6,7,8,9,10] 
list2 = []
for i in list : 
    if i %2==1:
        list2.append(i)
        list.remove(i)
print(sum(list2))

