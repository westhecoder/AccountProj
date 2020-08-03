
Project 1
We need to design an dimplement a class that will be used to represent bank accounts.

We want the following functionality and characteristics:
- accounts are uniquely identified by an **account number** (assume it will just be passed in the initializer)
- account holders have a **first** and **last** name
- accounts have an associated **preferred time zone offset** (e.g. -7 for MST)
- **balances** need to be zero or higher, and should not be directly settable.
- but, **deposits** and **withdrawals** can be made (given sufficient funds)
    - if a withdrawal is attempted that would result in nagative funds, the transaction should be declined.
- a **monthly interest rate** exists and is applicable to all accounts **uniformly**. There should be a method that can be called to calculate the interest on the current balance using the current interest rate, and **add it** to the balance.
- each deposit and withdrawal must generate a **confirmation number** composed of:
    - the transaction type: `D` for deposit, and `W` for withdrawal, `I` for interest deposit, and `X` for declined (in which case the balance remains unaffected)
    - the account number
    - the time the transaction was made, using UTC
    - an incrementing number (that increments across all accounts and transactions)
    - for (extreme!) simplicity assume that the transaction id starts at zero (or whatever number you choose) whenever the program starts
    - the confirmation number should be returned from any of the transaction methods (deposit, withdraw, etc)
- create a **method** that, given a confirmation number, returns:
    - the account number, transaction code (D, W, etc), datetime (UTC format), date time (in whatever timezone is specified in te argument, but more human readable), the transaction ID
    - make it so it is a nicely structured object (so can use dotted notation to access these three attributes)
    - I purposefully made it so the desired timezone is passed as an argument. Can you figure out why? (hint: does this method require any information from any instance?)
