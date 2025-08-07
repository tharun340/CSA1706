class ForwardChainingEngine:
    def __init__(self):
        self.facts = set(['a', 'b'])
        self.rules = {
            'c': ['a', 'b'],
            'd': ['c'],
            'e': ['d', 'b']
        }

    def infer(self):
        new_fact_added = True
        while new_fact_added:
            new_fact_added = False
            for conclusion, prerequisites in self.rules.items():
                if conclusion not in self.facts and all(p in self.facts for p in prerequisites):
                    self.facts.add(conclusion)
                    print(f"Inferred fact: {conclusion}")
                    new_fact_added = True

    def query(self, fact):
        return fact in self.facts

if __name__ == "__main__":
    engine = ForwardChainingEngine()
    print("Initial facts:", engine.facts)
    
    engine.infer()
    print("All inferred facts:", engine.facts)
    queries = ['a', 'c', 'e', 'x']
    for q in queries:
        print(f"Is '{q}' true? {'Yes' if engine.query(q) else 'No'}")
