Thumbtack Code Challenge
========================

Prompt:
Your task is create a very simple database, which has a very limited command set. We aren't going to be storing that much data, so you don't have to worry about storing anything on disk; in-memory is fine. All of the commands are going to be fed to you one line at a time via stdin, and your job is the process the commands and perform whatever operation the command dictates. Here are the basic commands you need to handle:

* SET [name] [value]: Set a variable [name] to the value [value]. Neither variable names or values will ever contain spaces.
* GET [name]: Print out the value stored under the variable [name]. Print NULL if that variable name hasn't been set.
* UNSET [name]: Unset the variable [name]
* END: Exit the program
So here is a sample input:

SET a 10
GET a
UNSET a
GET a
END
And its corresponding output:

10
NULL
Now, as I said this was a database, and because of that we want to add in a few transactional features to help us maintain data integrity. So there are 3 additional commands you will need to support:

* BEGIN: Open a transactional block
* ROLLBACK: Rollback all of the commands from the most recent transaction block. If no transactional block is open, print out INVALID ROLLBACK
* COMMIT: Permanently store all of the operations from any presently open transactional blocks
Our database supports nested transactional blocks as you can tell by the above commands. Remember, ROLLBACK only rolls back the most recent transaction block, while COMMIT closes all open transactional blocks. Any command issued outside of a transactional block commits automatically.

Even though we aren't dealing with a ton of data, we still want to use memory efficiently. Typically, we will already have committed a lot of data when we begin a new transaction, but the transaction will only modify a few values. So, your solution should be efficient about how much memory is allocated for new transactions, i.e., it is bad if beginning a transaction nearly doubles your program's memory usage.
