if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())


x_all = [i for i in range(x+1)]
y_all = [i for i in range(y+1)]
z_all = [i for i in range(z+1)]

result = []

for each_x in x_all:
    for each_y in y_all:
        for each_z in z_all:
            if (each_x+each_y+each_z != n):
                tmp_list = [each_x, each_y, each_z]
                result.append(tmp_list)

print(result)