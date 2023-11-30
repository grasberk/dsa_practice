def find_single_number(nums):
    unq_list=[]
    counter=0
    for elem in nums:
        if elem not in unq_list:
            unq_list+=[{elem : 1}]
        else:
            print(elem)            
    # print(unq_list)

list1=[]
find_single_number(list1)
