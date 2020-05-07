# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    """
        bill -> list
        k -> item index not eaten
        b -> amount paid by Anna

        -> calculate amount to be paid by Anna
            -> remove k index from bill
            -> sum(bill) / 2
        -> subtract amount from amount paid
        -> return bonAppitit if Ammount == Amount paid or change if Amount paid > Amount
    """

    bill.remove(bill[k])
    amount = sum(bill)/2
    difference = int(b - amount)
    print("Bon Appetit" if difference == 0 else difference)
