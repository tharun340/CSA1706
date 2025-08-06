can_fly = {"eagle", "sparrow", "parrot"}
cannot_fly = {"penguin", "ostrich", "kiwi"}

def bird_can_fly(bird):
    bird = bird.lower()
    if bird in can_fly:
        print(f"{bird.capitalize()} can fly.")
    elif bird in cannot_fly:
        print(f"{bird.capitalize()} cannot fly.")
    else:
        print(f"Unknown if {bird.capitalize()} can fly.")
if __name__ == "__main__":
    bird_can_fly("eagle"
                 )     
    bird_can_fly("penguin")  
    bird_can_fly("duck")      
