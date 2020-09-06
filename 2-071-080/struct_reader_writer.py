import struct


def read_struct(file_name, record_format):
    record_size = struct.calcsize(record_format)
    result = []

    with open(file_name, "rb") as f:
        while True:
            record = f.read(record_size)

            if not record:
                break

            result.append(struct.unpack(record_format, record))

    return result


def write_struct(file_name, record_format, record_list):
    with open(file_name, "wb") as f:
        for record in record_list:
            f.write(struct.pack(record_format, *record))


if __name__ == '__main__':
    write_struct("data", "hd4s", (
        [5, 55.5, b"hihi"],
        [2, 22.23, b"flsh"],
    ))
    print(read_struct("data", "hd4s"))
