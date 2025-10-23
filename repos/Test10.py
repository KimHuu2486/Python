s = "Hey there! what should this string be?"
s = s[0:20]
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
s = s[5:]
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
s = s[:1] + "a" + s[2:]
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))


print("\n")
class NumberHolder:

   def __init__(self, number):
       self.number = number

   def returnNumber(self):
       return self.number

var = NumberHolder(7)
print(var.returnNumber()) #Prints '7'

print("\n")
my_dict = {"b": 3, "a": 5, "c": 1}

sorted_dict = sorted(my_dict.items())
print(sorted_dict)

if __name__ == '__main__':
    print(0)
