# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict central data structure
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType


# number type

# x = 20
# print(type(x))
# y = 30.6
# print(type(y))
#
# z = int(y)
#
# print(type(z))
# print(z)

# a = 20
# b = float(a)
# print(b)
# print(type(b))
#
# c = 2+1j
# print(type(c))
# d = complex(a)
# print(type(d))

# Sequence Types:	list, tuple, range

# list

subject_name = ["ban","eng","math","database",(1,2,3,4,5,6,7,8,9)]
# print(subject_name)
# print(type(subject_name))
# print(subject_name)
# print(type(subject_name))
# print(subject_name[-2])
# print(subject_name[4][-5])

# tuple

# user_name = ("jodu","modhu","kodu")
# print(user_name)
# print(type(user_name))
# print(user_name[-1])


# range

# x = range(100)
#
# for i in x:
#     print(i)
#
# y = range(0,51,5)
#
# for i in y:
#     print(i)

# z = range(51, 4, -5)
#
# for a in z:
#     print(a)


# import array as arr
#
# a = arr.array("i",(1,2,3,4,5))
# print(type(a))
# b = arr.array("s",(1,2,3,4,5))
# print(b)

# set

# a = {"apple","banana"}
# print(a)
# print(type(a))


# Mapping Type:	dict central data structure
# key value নিয়ে কাজ করে

# address = {
#     "dict" : "dinajpur",
#     "upo" : "birol"
# }
#
# print(address.keys())
# print(address.values())
# print(address["upo"])
# print(type(address))
#
# print(address["upo"])

byte_arr = bytearray('ABCDE','utf-8')
print(byte_arr)

memory = memoryview(byte_arr)
print(memory)

print(byte_arr[1])

byte_arr[0] = 97

print(byte_arr)





































