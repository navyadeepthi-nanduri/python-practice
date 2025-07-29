# set operations performed on friends data
friends={'veera','shiva','ram','navya','mani','bhavya','sudha','ruthvi'}
friends1={'hema','rithu','smitha','nandhu','madhu','ruthvi','navya'}
friends2={'hemu','sohan','ruthvi','shvan','suresh','madhu','vara'}
common_friends = friends.intersection(friends1)
print(common_friends)
common_friends1=friends1.intersection(friends2,friends)
print(common_friends1)
common_friends2=friends1.intersection(friends2)
print(common_friends2)
total_friends=friends.union(friends2,friends1)
print(total_friends)
friends1.add("mahadev")
friends1.update(['navya','bhavya','sudha'])
print(friends1)
print(len(friends))
print(len(friends1))
print(len(friends2))
friends3=friends2.copy()
print(friends3)
print("navya" in friends)
print("mahadev" not in friends)

print(friends1.issuperset(friends2))
print(friends1.issubset(friends2))
print(friends1.isdisjoint(friends3))
for name in friends:
    print(name)
for name in friends1:
    print(name, end=" ")
count=0
for name in friends2:
    print(name)
    count+=1
friends.union(common_friends)
print(friends)
all_friends1=friends.union(friends1)-friends2
print("sent follow request:")
for name in all_friends1:
    print(name)
    all_friends2=friends1.union(friends2)-friends
print("sent follow request:",all_friends2,end=" ")


friends.discard("navya")
print(friends)
friends1.clear()
print(friends1)
friends2.pop()
print(friends2)




