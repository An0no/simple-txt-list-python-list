def txt_to_list(filename):
    with open(filename, 'r') as file:
        content = file.readlines()
    content = [x.strip() for x in content]
    return content
filename = input('Input filename: ')
my_list = txt_to_list(filename)
print(my_list)
