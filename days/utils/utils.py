def get_input(file_name):
    with open(f'./days/{file_name}') as f:
        return f.read().splitlines()
