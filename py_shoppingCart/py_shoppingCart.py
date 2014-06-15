
_salary = input("Enter how many salary you got: ")

_products = ['apple', 'banana', 'pineapple', 'watermelon']
_prices = [10, 20, 30, 35]

print "Products: \n"
for p in _products:
    print p, _prices[_products.index(p)]

_buyornot = True
while _buyornot:
    _select = raw_input("What do you want to buy? ").strip()
    if len(_select) == 0: continue
    _rest = _salary - _prices[_products.index(_select)]
    if (_rest) >= 0:
        print "BUY:",_select, "cost you:",_prices[_products.index(_select)],"\nYou have:", _rest, "left!"
        _salary = _rest;
        _buyornot = raw_input("Do you want to continue?(y/n)").strip()
        if _buyornot == 'n':
            _buyornot = False
    else:
        print "You don't have enough money to buy it!"
        break
else:
    print "Thanks for coming! See you next time!"