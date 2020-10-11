from decimal import Decimal, getcontext


def normalize(shares):
    getcontext().prec = 3
    sum_ = sum(shares)
    result = [s / sum_ for s in shares]
    return result


def main():
    with open('input1') as f:
        shares = []
        _ = f.readline()
        for line in f.readlines():
            share = Decimal(line)
            shares.append(share)

    result = normalize(shares)

    # There is some ambiguous in the task. So I output not percents
    # but the share. As it is in the task's output data.
    with open('output1', 'w') as f:
        for r in result:
            f.write(f'{r:.3f}\n')


if __name__ == '__main__':
    main()
