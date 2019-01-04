def print_dashes():
    print('---------------------')


def print_head():
    print('CASH RECEIPT')
    print_dashes()


def print_body():
    print('Charged to___________')
    print('Received by__________')


def print_footer():
    print_dashes()
    print('Softuni')


def print_cash():
    print_head()
    print_body()
    print_footer()


print_cash()
