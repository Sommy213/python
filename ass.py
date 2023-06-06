def find_common_element(list1 , list2):
      common_element =[]
      for element in list1:
            if element in list2 and element not in common_element:
               common_element.append(element)   
      return common_element
list1  = [2,3,4,5,6,7,8,9,10,11,11,112]   
list2 = [1,2,3,7,9,10]   
common_element= find_common_element(list1,list2)

print(common_element)
   
