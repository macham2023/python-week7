#LIST INDEXING AND SLICING IN PYTHON

countries = ["Spain", "Malawi", "Iran", "Usa" ]
details = countries[0:3]
country1,*country2 = countries[0:3]
print(country1)
#you can assign the rest of the items to a particular variable,example:
print(country2)

fav_countries = ["Spain", "Malawi", "Iran", "Usa"]
print(fav_countries)
fav_countries.remove("Spain")
print(fav_countries)


#TASK
account = [["1001","Joy","Savings","1500"],["1002","David","Cuurent","2000"],["1003","Ruth","Savings","1800"]]

rem_account = account.remove(account[1])
print(account)
#2

ruth_account = account[1]
name_of, account_of = ruth_account[1:3]

joy_account = account[0]
joy_n,account_n = joy_account[1:3]
print(name_of)
print(account_of)
print(joy_n)
print(account_n)

