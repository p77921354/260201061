def pascal_triangle(n):

    if n == 1:
        return [[1]]
    else:
        line = [1]

        all_lines = pascal_triangle(n-1)

        last_line = all_lines[-1]

        for i in range(len(last_line)-1):

            line.append(last_line[i] + last_line[i+1])

        line += [1]

        all_lines.append(line)

    return all_lines

print(pascal_triangle(6))
