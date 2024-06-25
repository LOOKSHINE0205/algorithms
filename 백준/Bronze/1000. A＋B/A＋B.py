# "1 2"
raw_input = input()
raw_input = raw_input.split() # ["1", "2"]

a= raw_input[0] # "1"
b =raw_input[1] # "2"

a = int (a) # 1
b = int (b) # 2

print( a + b )