# def sum(a,b,c):
#     print(a,b,c)

# sum(1,2,3)
# def names_of_people(*args):
#     for names in args:
#         print(names)
# names_of_people("jonn","peaper")
# # def name_of_person(name,age):
# #     print(f"hi i'm (name),and i'm (age)years old")
# # name_of_person(name = chisom ,age=27 )
# def nmae_of_funtion(age):
#     if age >10:
#         print("hi")
#         return  "hi"
#     else:
#         print("old")
#         return "old"
# response =nmae_of_funtion(20)
# print(response)
def sum(a,b):
    print(a,b)
    a-=1
    if a>0:
        sum(a,b)
      
 
