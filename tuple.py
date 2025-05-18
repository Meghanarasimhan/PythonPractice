#make it one tuple
test_tuple=([5,6],[6,7,8,9],[3])
result=()
for i in test_tuple:
    new_var=tuple(i)
    result=result+new_var
print(result)

#to return exponential values of two tuple
tuple1=(10,2,3,5,6)
tuple2=(3,6,4,3)
list1=[]
for i in range(min(len(tuple1),len(tuple2))):
        answer=tuple1[i] ** tuple2[i]
        numeric_list=[answer]
        list1=list1+numeric_list
print(tuple(list1))
