

# Read a given .txt or .sql file
def read_basic_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

# Write a basic file line by line - this is a write form and not append
def write_txt(data, path: str):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(data)