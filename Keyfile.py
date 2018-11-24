# Version: 0.1

# Class for managing keyfile (creating pass file, encryption/decryption of each line)
#
# format (after decryption):
#       site username password

class Keyfile():
    def __init__(self, path):
        self.path = path

    def write_line(self, line):
        with open(self.path, 'a') as f:
            f.write(line)

    def read_line(self, num):
        with open(self.path, 'r') as f:
            for i, line in enumerate(f):
                if i == num:
                    return line

    def encrypt_line(self, line):
        pass

    def decrypt_line(self, line):
        pass