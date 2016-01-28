__author__ = 'user'

# typedef for pairing
# typedef std::pair<int, int> Connection
class Connection:
    def __init__(self):
        self.first = None
        self.second = None

    def set_first(self, first):
        self.first = first

    def set_second(self, second):
        self.second = second

    def get_first(self):
        return self.first

    def get_second(self):
        return self.second

# Functor that determines the length of a connection
# Maintains a pointer to both input paths, and requires (binary) subtraction operator and length() memeber
# function for Point datatype
class ConnectionLength:
    def __init__(self):
        return


# Class to determine the "connection" between two paths.

