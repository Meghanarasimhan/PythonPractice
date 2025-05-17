list1=[1,2,3,4,5,6,7,8,9,10]
new_list=["even" for i in list1 if i%2==0 ]
print(new_list)
new_list1=["even" if i%2==0 else "odd" for i in list1]
print(new_list1)

 