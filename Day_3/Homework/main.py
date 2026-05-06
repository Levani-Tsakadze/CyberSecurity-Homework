#  მომხმარებელმა შეიყვანოს სახელი და დაბეჭდე.
name = input("Enter the name: ")
print(name)

# მომხმარებელმა შეიყვანოს რიცხვი და დაბეჭდე.
age = int(input("Enter the age: "))
print(age)

# მომხამრებლმა შეიყვანოს სახელი და დაუმატე 'hello'
name = input("Enter the name: ")
print("hello, " + name)

# შეიყვანე რიცხვი და დაუმატე 1.

age = int(input("Enter the age: "))
age = age + 1

# შეიყვანე 2 რიცხვი და დაბეჭდე ჯამი.

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print(x + y)

#  შეიყვანე ათწილადი რიცხვი და დაბეჭდე.

x = 3.14
print(type(x))

# შეიყვანე რიცხვი და გაამრავლე 2-ზე.

x = int(input("Enter number: "))
print(x*2)

# მომხმარებელს შემოაყვანინე ინფორმაცია და მოახდინე ყველა ნასწავლ მათემატიკურ ოპერატორებზე 
# მათემატიკური ოპერაციები(+ ; - ; * ; ** ; / ; // ; %)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print(x+y)
print(x-y)
print(x*y)
print(x**y)
print(x/y)
print(x//y)
print(x%y)