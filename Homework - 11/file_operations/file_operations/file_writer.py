#4. Define `write_file` function in file_writer.py. This function accepts two arguments(file_path, content).

def write_file(path, content):

    with open(path,'w') as file:
        file.write(content)
        print(f"Content written successfully to {path}")
        