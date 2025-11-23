# tuple basics

mytup=(50,65,85,96,52,63,52,88)

fruittup=("apple","banana","cherry")

print(mytup)
print(fruittup)

print(fruittup[1])

#  empty tuple
emptytup=()
print(type(emptytup))
print(type(mytup))

singlevaluetup=(50,) # to create a single value tuple we have to add comma at the end
print(type(singlevaluetup))

print(fruittup.index("cherry"))
print(mytup.count(52))


