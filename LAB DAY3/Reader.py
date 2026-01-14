def read_file(filename):
    try:
        with open(filename, "r") as file:
            data = file.read()
            print("File content:\n")
            print(data)

    except FileNotFoundError:
        print("Error: File not found")

    except PermissionError:
        print("Error: Permission denied")

    except Exception as e:
        print("Unexpected error:", e)
