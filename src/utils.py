def find_full_matches(sequence, answer):
    return find_sub_list(answer, sequence)


def find_matches(sequence, answer):
    elements = set(answer)
    return [index for index, value in enumerate(sequence) if value in elements]


def find_sub_list(sublist, list):
    results = []
    sll = len(sublist)
    for ind in (i for i, e in enumerate(list) if e == sublist[0]):
        if list[ind:ind + sll] == sublist:
            results.append(range(ind, ind + sll))

    return results


def is_sublist(sublist, list):
    sll = len(sublist)
    try:
        for ind in (i for i, e in enumerate(list) if e == sublist[0]):
            if list[ind:ind + sll] == sublist:
                return True
    except IndexError:
        print(sublist)
        print(list)
        raise
    return False


def get_chunks(sequence, chunk_size, key):
    """
    Computes the lower limit and the upper limit of a collection of documents
    :param sequence:
    :param chunk_size:
    :return: The doc id for the lower and upper limits
    """
    for j in range(0, len(sequence), chunk_size):
        chunck = sequence[j:j + chunk_size]
        lower = chunck[0][key]
        upper = chunck[-1][key]
        yield (lower, upper)
