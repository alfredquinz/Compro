str_input = input("Input your string: ")
result_str = ""
for char in str_input:
    if char in ["aeiouAEIOU"]:
        result_str = result_str + char
    else:
        result_str = result_str + char 
print("The results is", result_str)