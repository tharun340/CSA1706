
facts = {
    ('parent', 'alice', 'bob'),
    ('parent', 'bob', 'carol'),
    ('parent', 'carol', 'dave'),
}

rules = [
    {
        'head': ('ancestor', 'X', 'Y'),
        'body': [('parent', 'X', 'Y')]
    },
    {
        'head': ('ancestor', 'X', 'Y'),
        'body': [('parent', 'X', 'Z'), ('ancestor', 'Z', 'Y')]
    }
]

def unify(x, y, theta):
    """Unify two terms with substitution theta."""
    if theta is None:
        return None
    elif x == y:
        return theta
    elif is_variable(x):
        return unify_var(x, y, theta)
    elif is_variable(y):
        return unify_var(y, x, theta)
    elif isinstance(x, tuple) and isinstance(y, tuple) and len(x) == len(y):
        for a, b in zip(x, y):
            theta = unify(a, b, theta)
            if theta is None:
                return None
        return theta
    else:
        return None

def unify_var(var, x, theta):
    if var in theta:
        return unify(theta[var], x, theta)
    elif x in theta:
        return unify(var, theta[x], theta)
    else:
        theta2 = theta.copy()
        theta2[var] = x
        return theta2

def is_variable(x):
    return isinstance(x, str) and x[0].isupper()

def substitute(statement, theta):
    return tuple(theta.get(x, x) for x in statement)

def backward_chain(goal, theta=None):
    if theta is None:
        theta = {}
    substituted_goal = substitute(goal, theta)
    if substituted_goal in facts:
        yield theta
        return
    for rule in rules:
        rule_head = rule['head']
        theta_prime = unify(rule_head, goal, theta)
        if theta_prime is not None:
        
            body = rule['body']
            for theta_final in backward_chain_body(body, theta_prime):
                yield theta_final

def backward_chain_body(goals, theta):
    if len(goals) == 0:
        yield theta
    else:
        first, rest = goals[0], goals[1:]
        for theta_prime in backward_chain(first, theta):
            yield from backward_chain_body(rest, theta_prime)

if __name__ == "__main__":
    query = ('ancestor', 'alice', 'dave')

    print(f"Query: {query}")
    results = list(backward_chain(query))
    if results:
        for res in results:
            print("Yes,", res)
    else:
        print("No.")
