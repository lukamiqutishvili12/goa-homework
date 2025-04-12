#გააკეთეთ Filter Odd Numbers. მიზანი: გაფილტრეთ ყველრა კენტი რიცხვი და ჩაამატეთ ახალ სიაში და შემდეგ ეგ სია დაპრინტეთ
list = [1,2,3,4,5,6,7,8,9,10] 
list2 = []
for i in list : 
    if i %2==1:
        list2.append(i)
        list.remove(i)
print(list2)

