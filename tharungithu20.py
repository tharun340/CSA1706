class VacuumEnvironment:
    def __init__(self):
        self.locations = {'A': 'Dirty', 'B': 'Dirty'}
        self.agent_location = 'A'  

    def is_clean(self):
        return self.locations['A'] == 'Clean' and self.locations['B'] == 'Clean'

    def clean_location(self):
        print(f"Cleaning location {self.agent_location}")
        self.locations[self.agent_location] = 'Clean'

    def move(self, direction):
        if direction == 'Left':
            self.agent_location = 'A'
        elif direction == 'Right':
            self.agent_location = 'B'
        print(f"Moving {direction} to location {self.agent_location}")

    def get_status(self):
        return self.locations[self.agent_location]

def vacuum_agent(env):
    while not env.is_clean():
        status = env.get_status()
        if status == 'Dirty':
            env.clean_location()
        else:
            if env.agent_location == 'A':
                env.move('Right')
            else:
                env.move('Left')

if __name__ == "__main__":
    env = VacuumEnvironment()
    print(f"Initial state: {env.locations}")
    vacuum_agent(env)
    print(f"Final state: {env.locations}")
