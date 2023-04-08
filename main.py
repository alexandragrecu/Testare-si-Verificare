def check_inputs(N, M, K, intervals):
    if not (1 <= N <= 1000):
        raise ValueError("N (Numarul de pagini) trebuie sa fie intre 1 si 1000")

    if not (1 <= M <= 10000):
        raise ValueError("M (Numarul de intervale) trebuie sa fie intre 1 si 10000")

    if not (1 <= K <= 1000):
        raise ValueError("K (Lungimea maxima a intervalelor) trebuie sa fie intre 1 si 1000")

    if len(intervals) != M:
        raise ValueError("Numarul de perechi (mi, ci) trebuie sa fie M")

    for i, (mi, ci) in enumerate(intervals):
        if not (1 <= mi <= 100000):
            raise ValueError("mi (Limita superioara a intervalului i) trebuie sa fie intre (0, 100000)")

        if not (1 <= ci <= 10000):
            raise ValueError("ci (Costul intervalului i) trebuie sa fie intre (0 si 10000)")

def min_cost_to_buy_stamps(input_data):
    '''Returns the minimum cost for buying stamps'''
    N, M, K, intervals = input_data

    check_inputs(N, M, K, intervals)
    # sort the given intervals by cost
    intervals.sort(key=lambda x: x[1])

    # create a set to store the costs
    cost = set()
    i = M - 1
    c = 0

    # loop until all pages have stamps
    while N > 0:
        # add the cost of the interval if it has enough stamps for the remaining pages
        while i >= 0 and intervals[i][0] >= N:
            cost.add(intervals[i][1])
            i -= 1

        # check if the cost set is not empty before finding the minimum value
        if cost:
            # add the minimum cost to the total cost and remove it from the set
            c += min(cost)
            cost.remove(min(cost))
        else:
            break

        # decrease the number of pages by the maximum length of a subsequence
        N -= K

    print(intervals)
    return c

input_data = (4, 3, 2, [(5, 3), (2, 1), (6, 2)])

# output_str = "3"

result = min_cost_to_buy_stamps(input_data)

print(result)
