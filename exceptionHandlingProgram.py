def extract_unique_names(filename):
    unique_names=set()
    try:
        with open(filename,"r") as file:
            lines=file.readlines()

            if not lines:
                raise ValueError("File is empty")
            if lines[0].strip().lower().startswith("id"):
                lines=lines[1:]

            for line_no, line in enumerate(lines,start=1):
                try:
                    parts = line.strip().split(",")
                    if len(parts) < 4:
                        raise IndexError(f"{line_no} is malformed {line.strip()}")
                    name = parts[1].strip().strip('"')
                    if not name.isalpha():
                        raise TypeError(f"Name is not a valid String at line {line_no}")
                    unique_names.add(name)

                except IndexError as ie:
                    print(f"Index Error",ie)
                except TypeError as te:
                    print(f"Type Error",te)
    except FileNotFoundError as fnfe:
        print(f"File not found",fnfe)
    except Exception as e:
        print(f"Error Occurred",e)
    return unique_names

filename="file.txt"
unique_names=extract_unique_names(filename)
print(unique_names)
