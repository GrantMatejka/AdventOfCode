
def build_directory(lines):
    path = ['/']
    directory = {}

    for line in lines:
        print(path)
        path_str = ''.join(path)
        if line.startswith('$ cd ..'):
            path = path[:-1]
        elif line.startswith('$ cd /'):
            path = [path[0]]
        elif line.startswith('$ cd'):
            path += [line.split(" ")[2]]
        elif '$ ls' in line:
            if path_str not in directory:
                directory[path_str] = []
        else:
            line_split = line.split(" ")
            if line_split[0] == 'dir':
                directory[path_str + line_split[1]] = []
                directory[path_str] += [line_split[1]]
            else:
                directory[path_str] += [line_split[0]]
    
    return directory

def sum_dir_size(path, directory):
    return sum([int(v) if v.isdigit() else sum_dir_size(path + v, directory) for v in directory[path]])

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    directory = build_directory(lines)

    result = 0
    for contents in directory:
        size = sum_dir_size(contents, directory)
        if size < 100000:
            result += size

    print(result)

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    directory = build_directory(lines)

    result = []
    total_size = sum_dir_size('/', directory)
    for contents in directory:
        size = sum_dir_size(contents, directory)
        if 70000000 - total_size + size > 30000000:
            result.append(size)

    print(min(result))