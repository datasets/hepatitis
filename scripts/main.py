from urllib.request import urlopen

with open("../data/hepatitis.csv", "w") as output_file:
    data_found = False
    attributes = []
    for line in urlopen("https://www.openml.org/data/download/55/dataset_55_hepatitis.arff"):
        decoded_line = line.decode('UTF-8').strip()
        if '@attribute' in decoded_line:
            apos = [pos for pos, char in enumerate(decoded_line) if char == "\'"]
            attributes.append(decoded_line[apos[0]: apos[1]].replace('\'', ''))
        if data_found:
            decoded_line = decoded_line.replace("yes", "true")
            decoded_line = decoded_line.replace("no", "false")
            decoded_line = decoded_line.replace("?", "")
            output_file.write(decoded_line.lower() + '\n')

        if decoded_line == "@data":
            output_file.write(','.join(attributes).lower() + '\n')
            data_found = True

    output_file.close()
