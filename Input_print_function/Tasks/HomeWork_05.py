#Once, visiting a stationery store, Jack bought X pencils, Y pens, and Z markers. It is known that the price of
#a pen is 2 $ more than the price of a pencil and 7 $ less than the price of a marker. It is also known that the
#cost of a pencil is 3 $. The task is to determine the total cost of the

a, b, c = map(int, input().split())

print(a * 3 + b * (3 + 2) + c * (5 + 7))