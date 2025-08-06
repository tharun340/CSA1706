def hanoi(n, source, target, auxiliary):
    """
    Solves the Towers of Hanoi problem.

    Parameters:
    - n: Number of disks
    - source: Name of the source peg
    - target: Name of the target peg
    - auxiliary: Name of the auxiliary peg
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
    else:
        hanoi(n - 1, source, auxiliary, target)
        print(f"Move disk {n} from {source} to {target}")
        hanoi(n - 1, auxiliary, target, source)
if __name__ == "__main__":
    num_disks = 3  
    hanoi(num_disks, 'left', 'right', 'center')

