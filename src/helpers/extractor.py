import nbformat

def extract_code_cells(nb_path):
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    return [cell['source'] for cell in nb['cells'] if cell['cell_type'] == 'code']
