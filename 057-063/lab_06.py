import string


if __name__ == '__main__':
    with open("moby_01.txt") as infile, \
         open("moby_01_clean.txt", "w") as outfile:
        words = []
        for line in infile:
            for s in line.lower().replace("-", " ").split():
                words.append(s.strip(string.punctuation))
        outfile.write("\n".join(words))
