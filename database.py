class Database(object):

    def __init__(self):
        #Initialize database instance
        self.__storage = {}
        self.__transactions = {}
        self.__open_transactions = 0
        self.__value_frequency = {}
        self.__transaction_frequency = {}

    def begin(self):
        #Opens a transaction block

    def set(self, name, value):
        #Inserts/updates/deletes value of name in database

    def get(self, name):
        #Returns the value associated with the given name, if it exists, else returns None

    def num_equal_to(self, value):
        #Returns number of entries in the database that have the specified value

    def unset(self, name):
        #Removes the name from the database if it is present

    def rollback(self):
        #Rolls back the most recent transaction, returns False if no open transactions 

    def commit(self):
        #Commits all transactions, returning False if no open transactions

    def __get_last_key(self, item):
        #Returns key most recently added to item

    def __is_transaction_open(self):
        #Returns boolean indicating whether there is an open transaction block

    def __update_num_equal_to(self, current_value, new_value=None):
        #Swaps current value (lowers count by 1) with new_value (adds 1)

def display(value, default=None):
    #Prints value to stdout or default if value is None and default is not None

OPS = {}

def process_command(db, command):
    #Applies command to the database and returns False when stream of commands ends

def run():
    #Reads commands from the command line and passes them through for processing
