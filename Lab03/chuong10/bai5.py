import time_series

def smallest_value_skip(reader):
    line = time_series.skip_header(reader).strip()
    if line != '':
        smallest = int(line)
        for line in reader:
            line = line.strip()
            if line != '-':
                value = int(line)
                smallest = min(smallest, value)
        return smallest

if __name__ == '__main__':
    with open('hebron.txt', 'r') as input_file:
        print(smallest_value_skip(input_file))
