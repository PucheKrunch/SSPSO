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
            memory[best_fit_index].files.append(f"{file.n_file} {file.size}kb")
            file.saved = [True, memory[best_fit_index].address]
    
    print("Memory:")
    for cell in memory:
        print(cell)
    print("\nUnsaved files:")
    for file in files:
        if not file.saved[0]:
            print(file)

def first_fit(memory, files):
    for file in files:
        for cell in memory:
            if cell.size_left - file.size >= 0:
                cell.size_left -= file.size
                cell.files.append(f"{file.n_file} {file.size}kb")
                file.saved = [True, cell.address]
                break
    
    print("Memory:")
    for cell in memory:
        print(cell)
    print("\nUnsaved files:")
    for file in files:
        if not file.saved[0]:
            print(file)

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
            memory[worst_fit_index].files.append(f"{file.n_file} {file.size}kb")
            file.saved = [True, memory[worst_fit_index].address]
    
    print("Memory:")
    for cell in memory:
        print(cell)
    print("\nUnsaved files:")
    for file in files:
        if not file.saved[0]:
            print(file)