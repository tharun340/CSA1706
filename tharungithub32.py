def is_variable(x):
    return isinstance(x, str) and x[0].isupper()

def match(pattern, term, bindings=None):
    """
    Attempts to match pattern to term.
    Returns a dict of variable bindings if match succeeds, else None.
    """

    if bindings is None:
        bindings = {}

    # If pattern is a variable
    if is_variable(pattern):
        if pattern in bindings:
            # Variable already bound: check consistency
            if bindings[pattern] == term:
                return bindings
            else:
                return None
        else:
            bindings[pattern] = term
            return bindings
    if not isinstance(pattern, (list, tuple)) and not isinstance(term, (list, tuple)):
        if pattern == term:
            return bindings
        else:
            return None
    if (isinstance(pattern, (list, tuple)) and isinstance(term, (list, tuple))
        and len(pattern) == len(term)):
        for p_elem, t_elem in zip(pattern, term):
            bindings = match(p_elem, t_elem, bindings)
            if bindings is None:
                return None
        return bindings
    return None

if __name__ == "__main__":
    tests = [
        (("foo", "X", "b"), ("foo", "a", "b")),
        (("bar", "X", "Y"), ("bar", "a", "b")),
        (("foo", "a", "b"), ("foo", "a", "b")),
        (("foo", "X", "b"), ("foo", "a", "c")),
        ("X", ("foo", "a", "b"))
    ]

    for i, (pattern, term) in enumerate(tests, 1):
        result = match(pattern, term)
        print(f"Test {i}: match({pattern}, {term}) => {result}")
