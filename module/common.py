def updateFile(fname, id, replace):
    state = 0
    f = open('./storage/' + fname, 'r+')
    lines = f.read()
    lines = lines.split('\n')
    # print(lines)
    new_line_arr = []
    for line in lines:
        print(str(line.split(' ')[0]))
        if line.split(' ')[0] == id:
            new_line_arr.append(replace)
            state = 1
        else:
            new_line_arr.append(line + '\n')

    if state == 0:
        new_line_arr.append(replace)

    f.close()

    f = open('./storage/' + fname, 'w')

    newStr = ''.join(new_line_arr)
    f.write(newStr)
    # print(task)
    f.close()