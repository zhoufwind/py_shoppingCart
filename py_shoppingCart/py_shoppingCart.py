
_salary = input("Enter how many salary you got: ")

_menu = ['apple', 10, 'banana', 20, 'pineapple', 30, 'watermelon', 35]

_loop = (_menu.index(_menu[-1]) + 1) / 2
print "Menu: \n"
for i in range(_loop):
    print _menu[i*2], _menu[i*2+1]

_buyornot = True
while _buyornot:
    _select = raw_input("What do you want to buy? ").strip()
    _rest = _salary - _menu[_menu.index(_select)+1]
    if (_rest) >= 0:
        print "BUY\nYou have:", _rest, "left!"
        _salary = _rest;
        _buyornot = raw_input("Do you want to continue?(y/n)").strip()
        if _buyornot == 'n':
            _buyornot = False
    else:
        print "You don't have enough money to buy it!"
        break
else:
    print "Thanks for coming! See you next time!"