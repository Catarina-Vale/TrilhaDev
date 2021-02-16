
def process_numbers(input):
    if not isinstance(input, list):
        return []
    output = []
    for entry in input :
        if isinstance(entry,int):
            output.append(entry)
        else :
            if entry.isnumeric():
                output.append(int(entry))

    output.sort()
    return output


def process_names(input):
    if not isinstance(input, list):
        return []
    output = []
    for entry in input :
        if isinstance(entry,str):
            if not entry.isnumeric():
                output.append(entry)
    
    output.sort()
    return output
