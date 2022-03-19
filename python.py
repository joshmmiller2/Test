names = ['josh', 'shelby', 'hyde', 'harper']
message = f"You are invited to a special Dinner {names[0].title()}."
message2 = f"You are invited to a special Dinner {names[1].title()}."
message3 = f"You are invited to a special Dinner {names[2].title()}."
message4 = f"You are invited to a special Dinner {names[3].title()}."
print(message)
print(message2)
print(message3)
print(message4)
message5 = f"Sorry you couldnt make it {names[2].title()}"
print(message5)
del names[2]
print(names)
names.insert(2, "ney ney")
print(names)
message = f"You are invited to a special Dinner {names[0].title()}."
message2 = f"You are invited to a special Dinner {names[1].title()}."
message3 = f"You are invited to a special Dinner {names[2].title()}."
message4 = f"You are invited to a special Dinner {names[3].title()}."
print(message)
print(message2)
print(message3)
print(message4)
names.insert(0, "erin")
names.insert(2, "hazel")
names.append("indy")
print(names)
message = f"You are invited to a special Dinner {names[0].title()}."
message2 = f"You are invited to a special Dinner {names[1].title()}."
message3 = f"You are invited to a special Dinner {names[2].title()}."
message4 = f"You are invited to a special Dinner {names[3].title()}."
message5 = f"You are invited to a special Dinner {names[4].title()}."
message6 = f"You are invited to a special Dinner {names[5].title()}."
message7 = f"You are invited to a special Dinner {names[6].title()}."
print(message)
print(message2)
print(message3)
print(message4)
print(message5)
print(message6)
print(message7)
message8 = f" You are only allowed to invite two people for dinner"
message9 = f"I am sorry I cannot invite you to dinner"
print(message8)
popped_names = names.pop(0)
print(names)
print(f"sorry I cannot invite you to dinner the messed up our reservation {popped_names.title()},")
popped_names = names.pop(0)
print(names)
print(f"sorry I cannot invite you to dinner the messed up our reservation {popped_names.title()},")
popped_names = names.pop(0)
print(names)
print(f"sorry I cannot invite you to dinner the messed up our reservation {popped_names.title()},")
popped_names = names.pop(0)
print(names)
print(f"sorry I cannot invite you to dinner the messed up our reservation {popped_names.title()},")
popped_names = names.pop(0)
print(names)
print(f"sorry I cannot invite you to dinner the messed up our reservation {popped_names.title()},")
message = f"You are invited to a special Dinner {names[0].title()}."
message2 = f"You are invited to a special Dinner {names[1].title()}."
print(message)
print(message2)
del names[0]
print(names)
del names[0]
print(names)

magicians = ['alice','david','josh']
for magician in magicians:
    #print(magician.title())
    print(f"{magician.title()}, that was a good trick!!")
    print(f"I can't wait for your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")

pizzas = ['peperoni pizza','sausage pizza','veggie pizza']
for pizza in pizzas:
    print(pizza.title())
    print(f" I Love {pizza.title()}.\n")
print(f"I really love pizza!.\n")

#animals
animals = ['tiger','lion',"leopard"]
for animal in animals:
    print(animal.title())
    print(f"{animal.title()} hunts at night time for food.\n")
print(f"All of these animals are predators.")

for value in range(1,21):
    print(value)


my_foods = ['pizza','eggs','cheesebugers','tofu','sushi']
print("The first three items in the list are:")
print(my_foods[0:3])
print("Three items from the middle of the list are:")
print(my_foods[1:4])
print("The last three items in the list are:")
print(my_foods[2:5])

my_pizzas = ['peperoni pizza','sausage pizza','veggie pizza']
friends_pizza = my_pizzas[:]
print("My Favorite pizzas are: ")
print(my_pizzas)
print("\nMy friend's favorite pizzas are:")
print(friends_pizza)
my_pizzas.append('supreme')
friends_pizza.append('spinach and mushroom')
print("My Favorite pizzas are: ")
print(my_pizzas)
print("\nMy friend's favorite pizzas are:")
print(friends_pizza)


