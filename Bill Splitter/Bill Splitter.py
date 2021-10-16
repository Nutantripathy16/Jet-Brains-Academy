import random
bill = {}
print("Enter the number of friends joining (including you):\n")
num = int(input())
if num > 0:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(num):
        name =input()
        bill.update({name:0})
    #print(bill)
    amount = float(input("Enter the total bill value:\n"))
    amount_each = amount / num
    final_amount_each = round(amount_each,2)
    bill2 = {key:final_amount_each for key in bill}
    #print(bill2)
    choice = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if choice == "Yes":
        names = list()
        for key in bill.keys():
            names.append(key)
        lucky = random.choice(names)
        print(lucky, "is the lucky one!")
        re_split_amount = amount / (num - 1)
        bill3 = {key: (re_split_amount if key != lucky else 0) for (key,values) in bill.items()}
        print(bill3)
    else:
        print("No one is going to be lucky")
        print(bill2)
else:
    print("No one is joining for the party")