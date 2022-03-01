def best_fit(memory, files):
    for file in files:
        diff = 3000
        best_fit_index = None
        index = 0
        for cell in memory:
            if cell.size_left - file.size < diff and cell.size_left - file.size >= 0:
                diff = cell.size_left - file.size
                best_fit_index = index
            index += 1
        if best_fit_index is not None:
            memory[best_fit_index].size_left -= file.size
            file.saved = [True, memory[best_fit_index].address]
    
    for file in files:
        if file.saved[0]:
            print("File {} saved in cell {}".format(file.n_file, file.saved[1]))
        else:
            print("File {} not saved".format(file.n_file))

def first_fit(memory, files):
    for file in files:
        for cell in memory:
            if cell.size_left - file.size >= 0:
                cell.size_left -= file.size
                file.saved = [True, cell.address]
                break
    
    for file in files:
        if file.saved[0]:
            print("File {} saved in cell {}".format(file.n_file, file.saved[1]))
        else:
            print("File {} not saved".format(file.n_file))

def worst_fit(memory, files):
    for file in files:
        diff = 0
        worst_fit_index = None
        index = 0
        for cell in memory:
            if cell.size_left - file.size > diff:
                diff = cell.size_left - file.size
                worst_fit_index = index
            index += 1
        if worst_fit_index is not None:
            memory[worst_fit_index].size_left -= file.size
            file.saved = [True, memory[worst_fit_index].address]
    
    for file in files:
        if file.saved[0]:
            print("File {} saved in cell {}".format(file.n_file, file.saved[1]))
        else:
            print("File {} not saved".format(file.n_file))