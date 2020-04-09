x = [1, 2, 3, 4]
x_squared = []
for item in x:
    x_squared.append(item * item)

print("x_squared:{}".format(x_squared))

x_squared_1 = [item * item for item in x ]
print("x_squared_1:{}".format(x_squared_1))

x_squared_2 = {item: item * item for item in x}
print("x_squared_2:{}".format(x_squared_2))


if __name__ == '__main__':
    print('--------')
