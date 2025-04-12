#გააკეთეთ Sum Of Odd Numbers. მიზანი: შეკრიბეთ ყველა კენტი რიცხვი და შეინახეთ სიაში შემდეგ ეგ სია დაპრინტეთ 10 ჯერ
list = [1,2,3,4,5,6,7,8,9,10] 
list2 = []
for i in list : 
    if i %2==0:
        list2.append(i)
        list.remove(i)
print(sum(list2))

