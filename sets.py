
name = input("Enter the first name : ")
name1= input("Enter the second name :")
name2 = input("Enter the third name: ")

T = ({name,name1,name2})
print(T)

if T == {"Rajdeep","Rahul","Ryan"}:
	print("They have gotten thanks giving card")

elif T == {"Rajdeep","Rahul",""}:
	print("They have gotten thanks giving card")
	
elif T == {"Rahul","Ryan",""}:
	print("They have gotten thanks giving card")
	
elif T == {"Ryan","Rajdeep",""}:
	print("They have gotten thanks giving card")

else :
	print("They not get thanks giving card")
	
print("Thanks")