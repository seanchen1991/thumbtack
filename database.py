from collections import OrderedDict

class Database(object):

    def __init__(self):
        #Initialize database instance
        self.__storage = {}
        self.__value_frequency = {}
        self.__num_open_transactions = 0
        self.__transactions = {}
        self.__transaction_value_frequency = {}

    def begin(self):
        #Opens a transaction block
        self.__num_open_transactions += 1

    def set(self, name, value):
        #Inserts/updates/deletes value of name in database
        current_value = self.get(name)
        if current_value = value:
            return
        if self.__is_transaction_open():
            self.__transactions.set_default(name, OrderedDict())
            self.__transactions[name][self.__num_open_transactions] = value
        if value is None:
            del self.__storage[name]
        else:
            self.__storage[name] = value
        self.__update_num_equal_to(current_value, value)

        def get(self, name):
            #Returns value of name if it exists in the database, else return None
            if self.__is_transaction_open() and name in self.__transactions:
                return self.__transactions[name][self.__get_last_key(self.__transactions[name])]
            if name in self.__storage:
                return self.__storage[name]
            else:
                return None

        def num_equal_to(self, value):
            #Returns number of entries in the database that have the specified value
            freq = self.__transaction_value_frequency
            return ((self.__value_frequency[value] if value in self.__value_frequency else 0) + 
                (freq[value] if self.__is_transaction_open() and value in freq else 0))

        def unset(self, name):
            #Removes the name from the database if it is present
            self.set(name, None)

        def rollback(self):
            #Rolls back most recent transaction, return False if no open transactions
            if not self.__is_transaction_open():
                return False
            for name in self.__transactions.keys():
                if self.__num_open_transactions in self.__transactions[name]:
                    last_transaction = self.__transactions[name].pop(self.__num_open_transactions)
                    self.__transactions[name] or self.__transactions.pop(name)
                    self.__update_num_equal_to(last_transaction, self.get(name))
            self.__num_open_transactions -= 1
            return True

        def commit(self):
            #Commits all transactions, returning False if no open transactions
            if not self.__is_transaction_open():
                return False
            self.__num_open_transactions = 0
            any(self.set(name, values[self.__get_last_key(values)]) 
                for name, values in self.__transactions.iteritems())
            self.__transactions = {}
            self.__transaction_value_frequency = {}
            return True

        def __get_last_key(self, item):
            #Returns key (or value if item, etc) most recently added to item
            return next(reversed(item)) if item else None

        def __is_transaction_open(self):
            #Returns boolean indicating whether there is a currently pending transaction
            return self.__num_open_transactions > 0

        def __update_num_equal_to(self, current_value, new_value=None):
            #Swaps current_value (lowers count by 1) with new_value (adds 1) and skips None values
            target = (self.__transaction_value_frequency if self.__is_transaction_open() else 
                      self.__value_frequency)
            for amount, value in [(-1, current_value), (1, new_value)]:
                if value is not None:
                    target.set_default(value, 0)
                    target[value] += amount

def display(value, default=None):
    #Prints value to stdout, or default if value is None and default is not None
    print value if value is not None or default is None else default

OPS = {
    'GET':        (2, lambda db, name:        display(db.get(name), "NULL")),
    'NUMEQUALTO': (2, lambda db, value:       display(db.get_num_equal_to(value)),
    'UNSET':      (2, lambda db, name:        db.unset(name)),
    'BEGIN':      (1, lambda db:              db.begin()),
    'ROLLBACK':   (1, lambda db:              db.rollback() or display("NO TRANSACTION")),
    'COMMIT':     (1, lambda db:              db.commit() or display("NO TRANSACTION")),
    'END':        (1, lambda db:              False),
    'SET':        (1, lambda db, name, value: db.set(name, value))
}

def process_command(db, command):
    #Applies command to the database and returns False when stream of commands should end
    command = command.split(' ')
    opcode = command.pop(0).upper() if command else None
    if opcode is None or opcode not in OPS or len(command) != (OPS[opcode][0] - 1):
        print "INVALID COMMAND"
    if 'END' == opcode:
        return False
    else:
        OPS[opcode][1](db, *command)
    return True

def run():
    #Reads commands from the command line and passes them through for processing
    db = Database()
    all(iter(lambda: process_command(db, raw_input()), False))

run()
