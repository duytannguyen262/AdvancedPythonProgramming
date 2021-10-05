def read_molecule(reader):
    line = reader.readline()
    if not line:
        return None
    key, name = line.split() 
    molecule = [name]
    reading = True
    serial_number = 1
    while reading:
        line = reader.readline()
        if line.startswith('END'):
            reading = False
        else:
            key, num, atom_type, x, y, z = line.split()
            if int(num) != serial_number:
                print('Expected serial number ' + serial_number + ', but got ' + num)
            molecule.append([atom_type, x, y, z])
            serial_number += 1
    return molecule