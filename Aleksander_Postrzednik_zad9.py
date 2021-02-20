#odczytac zawartosc pliku i zapisac w drugim
with open('input.txt') as f:
    try:
        with open('input.txt') as input_file:
            data = input_file.read()
        with open('output.txt', 'w') as output_file:
            output_file.write(data)
    except:
        print("cos poszlo nie tak !")
    finally:
        print(data)
