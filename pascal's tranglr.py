rows = 5
triangle = []

#using for loop for printing the numbers in this tringle variable 

for i in range(rows):
    row = [1]

    if i > 0 :
        last_row = triangle[i- 1]

        for j in range(1,i):
            new_number = last_row[j-1]+last_row[j]
            row.append(new_number)

        row.append(1)

    triangle.append(row)
    spaces = " "*(rows - i )
    numbers = " ".join("*" * x for x in row)

    print(spaces + numbers )   