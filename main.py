def readProgramFromFile(filename):
    with open(filename, 'r') as file:
        program = file.readlines()
    return [line.strip() for line in program]


def writeProgramToFile(filename, endStrings):
    with open(filename, 'w') as file:
        for line in endStrings:
            file.write(line + '\n')


def fileProcessing(programArray):
    programArray = [line.split(' ') for line in programArray]
    instructionDictionary = {'TAKE': 1, 'ADD': 2, 'SUB': 3, 'SAVE': 4,
                             'JMP': 5, 'TST': 6, 'INC': 7, 'DEC': 8, 'NULL': 9, 'HLT': 10}
    opt = []
    var = {}
    varValues = {}
    goto = {}
    endStrings = []
    print(programArray)
    for line in programArray:
        # print(line)
        if line[0] in instructionDictionary.keys():
            opt.append(line[0])
        else:
            var[line[0]] = programArray.index(line)
            varValues[line[0]] = line[1]
            # pass

        if len(line) == 3:
            goto[line[2]] = opt.index(line[0])

    print(opt)
    print(var)
    print(goto)

    for item in programArray:
        # item = item.split(' ')
        # print(item)
        if item[0] == 'JMP':
            if item[1] in goto.keys():
                # print(str(instructionDictionary[item[0]]) + str(goto[item[1]]).zfill(3))
                endStrings.append(
                    str(instructionDictionary[item[0]]) + str(goto[item[1]]).zfill(3))
                # pass
            else:
                print("error")
                # pass
            continue

        if item[0] == 'HLT':
            # print('10000')
            endStrings.append('10000')
            continue

        if item[1] in var.keys():
            # print(str(instructionDictionary[item[0]]) + str(var[item[1]]).zfill(3))
            endStrings.append(
                str(instructionDictionary[item[0]]) + str(var[item[1]]).zfill(3))
            # print(str(var[item[1]]).zfill(3))
            # pass
        elif len(item[1]) == 3:
            # print(str(instructionDictionary[item[0]]) + item[1])
            endStrings.append(str(instructionDictionary[item[0]]) + item[1])
            # pass
        else:
            if item[0] in var.keys():
                # print(str(var[item[0]]).zfill(3))
                endStrings.append(str(varValues[item[0]]).zfill(3))
                # endStrings.append(str(var[item[0]]).zfill(3))
                # pass
            else:
                cAddr = max(var.values())
                # print(str(instructionDictionary[item[0]]) + str(cAddr + 1).zfill(3))
                endStrings.append(
                    str(instructionDictionary[item[0]]) + str(cAddr + 1).zfill(3))
                # pass

    print(endStrings)
    # fill up endStrings with 000 till 1000
    while len(endStrings) < 1000:
        endStrings.append('000')
    return endStrings


def main():
    programArray = readProgramFromFile('programToTranslate.txt')
    # print(programArray)
    endStrings = fileProcessing(programArray)
    # print(endStrings)
    name = str(input("Input the name of .ram file: "))
    writeProgramToFile(f'{name}.ram', endStrings)


if __name__ == '__main__':
    main()
