def pascal_triangle(n):
    if n <= 0:
        return []

    # to tart with the first row
    triangle = [[1]]

    # Generate subsequent rows
    for i in range(1, n):
        row = [1]  # Each row starts with 1

        # Compute the values in between the first and last 1's
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])

        row.append(1)  # Each row ends with 1
        triangle.append(row)

    return triangle

