def min_cost_to_buy_stamps(input_data):
    '''Returns the minimum cost for buying stamps'''
    N, M, K, intervals = input_data

    # check inputs
    if not (1 <= N <= 1000):
        return "N (Numarul de pagini) trebuie sa fie intre 1 si 1000"

    if not (1 <= M <= 10000):
        return "M (Numarul de intervale) trebuie sa fie intre 1 si 10000"

    if not (1 <= K <= 1000):
        return "K (Lungimea maxima a intervalelor) trebuie sa fie intre 1 si 1000"

    if len(intervals) != M:
        return "Numarul de perechi (mi, ci) trebuie sa fie M"

    for i, (mi, ci) in enumerate(intervals):
        if not (1 <= mi <= 100000):
            return "mi (Limita superioara a intervalului i) trebuie sa fie intre (0, 100000)"

        # non-equivalent mutant that will not be killed
        # This change allows intervals with a cost of 0,
        # but since the provided test case doesn't have any intervals with a cost of 0, this change won't be detected.
        if not (0 <= ci <= 10000):
            return "ci (Costul intervalului i) trebuie sa fie intre (0 si 10000)"

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

        # decrease the number of pages by the maximum length of a subsequence
        N -= K

    return c