# Version: 0.1

# Class for managing keyfile (creating pass file, encryption/decryption of each line)
#
# format (after decryption):
#       site username password

class Keyfile():
    def __init__(self, path):
        self.path = path

    def write_line(self, path, line):
        with open(path, 'a') as f:
            f.write(line)

    def read_line(self, path, num):
        with open(path, 'r') as f:
            for i, line in enumerate(f):
                if i == num:
                    return line

