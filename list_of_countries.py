#List is a collection of elements  in a particular order.List a data type that store values of various datatypes.
LIST
countries = ["Autralia", "Malawi", "Russia", "Nigeria", "Usa", "Iran"]
print(countries[0])


#TASK1
my_favorite_movies = ["Marlin", "Game of throne", "Avengers", "Walking death", "Prince of persia"]
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_info = ["macham", 18, False, "male", 5.8, "blue"]
my_provisions = ["cabin","garri", "sugar", "milk", "palm-oil", "maggi"]

print(my_favorite_movies)
print(my_numbers)
print(my_info)
print(my_provisions)


android = ["Samsung", "Techno", "Itel", "Redmi", "Oppo"]
ios = ["11-pro-max", "15-pro", "Xr", "16 plus", "7 plus"]
phones = [android, ios]
print(phones)

code = ["x","H","e","z","l","l","i","p","o","-","n"," ","W","@","r","d","o","#"]
#task

H = (code[1])
e = (code[2])
l = (code[4])
l = (code[5])
o = (code[8])
print(H+e+l+l+o)


w= (code[12])
o= (code[8])
r= (code[14])
l= (code[4])
d= (code[15])
print(w+o+r+l+d)


reverse_code = code[::-1]
print(reverse_code)

#TASK2
grid = [["The","sky","is"], ["full","of","stars"],["shining","bright","tonight"]]

#1
the =grid[0][0]
sky = grid[0][1]
print(the,sky)

#2
The = grid[0][0]
stars = grid[1][2]
shine = grid[2][0]
print(The,stars,"are",shine)
rev_second = grid[1][::-1]
print(rev_second)


favorite_fruits = ["mango","apple","pieapple","kiwi","banana"]
print(favorite_fruits)
print("before update>>>>>")
favorite_fruits[0] = "coco-nut"
print("after update>>>>>>")
print(favorite_fruits)
print("new update")
favorite_fruits[-1] = "straw berry"
print(favorite_fruits)


#TASK
playlist = ["Song A", "Song B", "Song C"]


playlist[1] = "Song D"
print(playlist)

playlist.append("Song E")
print(playlist)
 

print("intro",playlist)

print(playlist[-1])

#TASK2
desk = [ ]
students_name1 = input("Enter names:")
students_name2 = input("Enter names:")
students_name3 = input("Enter names:")
desk.append(students_name1)
desk.append(students_name2)
desk.append(students_name3)
print(desk)

another_student = input("Enter your name:")
desk[1] = another_student
print(desk)
student4 = input("Enter your name:")

print(desk.insert(1, student4))
print(desk)









































