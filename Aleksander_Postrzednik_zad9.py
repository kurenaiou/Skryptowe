try:
    with open("input.txt", 'r') as input:
        with open("output.txt",'w') as output:
            for line in input:
                output.write(line)
except IOError as e:
    print(f"Operation error: {e.strerror}")

#finally:
#    print(data)
