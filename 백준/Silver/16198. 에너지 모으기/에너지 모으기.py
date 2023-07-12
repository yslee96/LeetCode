import sys
input = sys.stdin.readline
num_beads = int(input())
energy = list(map(int, input().split()))
max_energy = 0
def get_max_energy(options, cur_energy):
    global max_energy
    if len(options) == 2:
        max_energy = max(max_energy, cur_energy)
        return
    
    for i in range(1, len(options)-1):
        new_enrergy = cur_energy + options[i-1] * options[i+1]
        new_options = options[:i] + options[i+1:]
        get_max_energy(new_options, new_enrergy)
        
get_max_energy(energy, 0)
print(max_energy)