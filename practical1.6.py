# Implicit type conversion 
a = 10       # int 
b = 2.5      # float 
result = a + b 
print("Implicit Conversion (int + float):", result) 
print("Type:", type(result)) 

# Explicit type conversion (correct usage) 
x = 10 
y = "5" 
y = int(y)   # converting string to integer 
result2 = x + y 
print("\nExplicit Conversion (int + str converted to int):", result2) 
