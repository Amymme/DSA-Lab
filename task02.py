def overlap(u, v):
    '''
    Computes the set-theoretic intersection of two lists.

    Parameters
    ----------
    u : list
    v : list

    Returns
    -------
    w : list
        The list obtained by keeping only the common elements
        of the given lists

    '''
    w = [] # Initialise an empty list for later extensions
    
    # The common elements must exists in u, so loop through u
    # but keep only those elements which also lie in v, without repeats.
    [w.append(x) for x in u if (x in v) and (x not in w)]
    return w


def join(u, v):
    '''
    Computes the set-theoretic union of two lists.

    Parameters
    ----------
    u : list
    v : list

    Returns
    -------
    w : list
        The list obtained by keeping all the elements of u and v,
        without any repeats

    '''
    w = [] # Initialise an empty list for later extensions

    # Add all the elements of u (then v) to w, unless they have already been added
    # Don't collect the resulting list
    [w.append(x) for x in u if x not in w]
    [w.append(x) for x in v if x not in w]
    return w


def main():
    # Call each function with the appropriate input(s) to inspect the output(s)
    print(overlap([1.0, 2.5, 4.5], [2.5, 4.0, 5.0]))
    print(overlap([1.0, 2.0, 2.0, 4.5], [2.0, 4.5, 5.0]))
    
    print(join([1.0, 4.5], [2.0, 4.5, 5.0]))
    print(join([1.0, 2.0, 1.0, 4.5], [2.0, 4.5, 5.0]))



if __name__ == '__main__':
    main()