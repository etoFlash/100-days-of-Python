import pickle


if __name__ == '__main__':
    d = {"a": 123, "b": 456}
    file_name = "dict_file"
    print(d)

    with open(file_name, "wb") as f:
        pickle.dump(d, f)

    d = {}
    print(d)

    with open(file_name, "rb") as f:
        d = pickle.load(f)

    print(d)
