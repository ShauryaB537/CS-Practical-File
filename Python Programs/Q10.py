line_numbers = input("Enter the line numbers separated by comma: ")
line_numbers_list=line_numbers.split(',')

source_file = open('YouAreMySunshine.txt', 'r')
lines = source_file.readlines()

destination_file = open('MyOnlySunshine.txt', 'w')
for i in line_numbers_list:
    destination_file.write(lines[int(i) - 1])

print(f"Lines {line_numbers} have been copied to {destination_file}.")


#WHY IS THIS NOT WORKING??
