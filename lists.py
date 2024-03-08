# initialize an empty list
my_list= [];
# print(my_list);
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
# print(my_list);

my_list=[10, 20, 30, 40];

my_list.insert(1,15)
# print(my_list);

extension=[50, 60, 70]

my_list.extend(extension);
# print(my_list);

# Remove the last element
my_list.pop()
# print(my_list);

# Sort the list in ascending order
my_list.sort()
# print(my_list);

# Find and print the index of the value 30
index_of_30 = my_list.index(30)
print("Index of 30 in my_list:", index_of_30)

