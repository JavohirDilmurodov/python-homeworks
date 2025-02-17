#4.  Define `read_file` function in file_reader.py. This function accepts one argument(file_path).

def read_file(path):
    with open(path, 'r') as file:
        content = file.read()
        print(content)

