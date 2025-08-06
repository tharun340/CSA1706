class FamilyTree:
    def __init__(self):
        self.parents = {}
        self.genders = {}

    def add_parent(self, parent, child):
        if parent in self.parents:
            self.parents[parent].append(child)
        else:
            self.parents[parent] = [child]

    def set_gender(self, person, gender):
        self.genders[person] = gender

    def children_of(self, parent):
        return self.parents.get(parent, [])

    def parents_of(self, child):
        return [p for p, children in self.parents.items() if child in children]

    def mother(self, child):
        return [p for p in self.parents_of(child) if self.genders.get(p) == 'female']

    def father(self, child):
        return [p for p in self.parents_of(child) if self.genders.get(p) == 'male']

    def siblings(self, person):
        siblings_set = set()
        for parent in self.parents_of(person):
            for sibling in self.children_of(parent):
                if sibling != person:
                    siblings_set.add(sibling)
        return list(siblings_set)

    def brothers(self, person):
        return [sib for sib in self.siblings(person) if self.genders.get(sib) == 'male']

    def sisters(self, person):
        return [sib for sib in self.siblings(person) if self.genders.get(sib) == 'female']

    def grandparents(self, person):
        grandparents_set = set()
        for parent in self.parents_of(person):
            for grandparent in self.parents_of(parent):
                grandparents_set.add(grandparent)
        return list(grandparents_set)

    def ancestors(self, person, ancestors_set=None):
        if ancestors_set is None:
            ancestors_set = set()
        for parent in self.parents_of(person):
            if parent not in ancestors_set:
                ancestors_set.add(parent)
                self.ancestors(parent, ancestors_set)
        return ancestors_set


family = FamilyTree()

family.add_parent('john', 'mary')
family.add_parent('john', 'michael')
family.add_parent('susan', 'mary')
family.add_parent('susan', 'michael')
family.add_parent('mary', 'alice')
family.add_parent('mary', 'bob')
family.add_parent('michael', 'james')

family.set_gender('john', 'male')
family.set_gender('michael', 'male')
family.set_gender('bob', 'male')
family.set_gender('james', 'male')
family.set_gender('susan', 'female')
family.set_gender('mary', 'female')
family.set_gender('alice', 'female')


print("Children of John:", family.children_of('john'))            
print("Parents of Mary:", family.parents_of('mary'))              
print("Mother of Mary:", family.mother('mary'))                   
print("Father of Mary:", family.father('mary'))                   
print("Siblings of Mary:", family.siblings('mary'))               
print("Brothers of Mary:", family.brothers('mary'))               
print("Sisters of Michael:", family.sisters('michael'))           
print("Grandparents of Alice:", family.grandparents('alice'))     
print("Ancestors of Alice:", family.ancestors('alice'))           
