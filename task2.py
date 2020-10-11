from collections import namedtuple

denomination = 1000


def zeros(rows, cols):
    row = []
    data = []
    for i in range(cols):
        row.append(0)
    for i in range(rows):
        data.append(row[:])
    return data


def knapsack_dp(weights, values, capacity):
    n = len(values)
    table = zeros(n + 1, capacity + 1)
    keep = zeros(n + 1, capacity + 1)

    for i in range(1, n + 1):
        for w in range(0, capacity+1):
            wi = weights[i-1]
            vi = values[i-1]
            if (wi <= w) and (vi + table[i-1][w-wi] > table[i-1][w]):
                table[i][w] = vi + table[i-1][w-wi]
                keep[i][w] = 1
            else:
                table[i][w] = table[i-1][w]

    picks = []
    c = capacity

    for i in range(n, 0, -1):
        if keep[i][c] == 1:
            picks.append(i)
            c -= weights[i-1]
    picks.sort()
    # Change indexes offset.
    picks = [x-1 for x in picks]

    max_val = table[n][capacity]
    return max_val, picks


def main():
    with open('input2') as f:
        n, m, s = map(int, f.readline().split())  # n - дни, m - лоты, s - средства
        lots = []
        Lot = namedtuple('Lot', 'day name price amount')
        lines = f.readlines()  # Will be used to form the output.
        for line in lines:
            d = line.split()
            day = int(d[0])
            name = d[1]
            price = float(d[2])
            amount = int(d[3])
            lot = Lot(day, name, price, amount)
            lots.append(lot)

    # Get income and price for each lot.
    incomes = []
    prices = []
    last_day = n + 30
    for lot in lots:
        # Income is equal to ((last_lot_day + 30 + discount income) * count).
        # Discount value is based on its price. Can be negative or positive.
        days_that_deliver = last_day - lot.day
        # Price in percents. Assumed the price has only one decimal place after the point. Not more.
        one_price = int(lot.price * denomination / 100)
        discount = denomination - one_price
        # A bond deliver only one conventional unit per day.
        income = (days_that_deliver*1 + discount) * lot.amount
        incomes.append(income)
        price = one_price * lot.amount
        prices.append(price)

    # Right now we have incomes and prices. It is a typical 0-1 knapsack problem now.
    # So we have incomes as values, prices as weights and our money as maximum weights capacity.
    # Actually it might be solved with some Linear Programming lib.
    result = knapsack_dp(prices, incomes, s)

    with open('output2', 'w') as f:
        f.write(str(result[0]) + '\n')
        for pick in result[1]:
            f.write(lines[pick])  # The lines have their \n already.


if __name__ == '__main__':
    main()
