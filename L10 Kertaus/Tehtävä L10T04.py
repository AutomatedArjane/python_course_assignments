#Lab10 Tehtävä 04

# create a list with n elements
list = ["abc", 123, "Hello World!", 3.1415]

try: # try changing element n+1
    list[len(list)+1] = 42
except: # if an index error occurs, print the following statement
    print(f"There are only {len(list)} elements in this list. The item you try to change is out of range.")
