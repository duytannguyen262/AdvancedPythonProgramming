def read_molecule(reader):
    line = reader.readline()
    if not line:
        return None
    if not (line.startswith('CMNT') or line.isspace()):
        key, name = line.split()
        molecule = [name]
    else:
        molecule = None
    reading = True
    while reading:
        line = reader.readline()
        if line.startswith('END'):
            reading = False
        elif not (line.startswith('CMNT') or line.isspace()):
            key, num, atom_type, x, y, z = line.split()
            if molecule == None:
                molecule = []
            molecule.append([atom_type, x, y, z])
    return molecule