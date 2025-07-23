#==========LIST METHODS===========

#replace ()

txt = "one one was a race horse,two two was one two."
x = txt.replace("one", "three", 2)
print(txt)
print(x)

#append ()
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)

#clear ()
fruits = ['Cherry', 'banana', 'mango']
fruits.clear()
print(fruits)

#copy ()
fruits = ['Cherry', 'banana', 'mango']
x = fruits.copy()
print(x)

#count ()
fruits = ['Cherry', 'banana', 'mango']
x = fruits.count("banana")
print(x)

#extend
fruits = ['cherry', 'banana', 'mango']
cars = ['benz', 'wagon', 'lamborghini']
fruits.extend(cars)
print(fruits)

#index
fruits = ['cherry', 'banana', 'mango']
x = fruits.index("mango")
print(x)

#insert ()
fruits = ['cherry', 'banana', 'mango']
fruits.insert(1, "pineapple")
print(fruits)

#pop  ()
fruits = ['cherry', 'banana', 'mango']
fruits.pop(1)
print(fruits)

#remove ()
fruits = ['cherry', 'banana', 'mango']
fruits.remove("banana")
print(fruits)

#reverse ()
fruits = ['cherry', 'banana', 'mango']
fruits.reverse()
print(fruits)

#sort ()
fruits = ['cherry', 'banana', 'mango']
fruits.sort()
print(fruits)




























