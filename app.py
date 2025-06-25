from itertools import combinations

MOD = 10**9 + 7

def median_of_sorted(seq):
    return sorted(seq)[len(seq)//2]

def solve():
    t = int(input("Enter number of test cases: ").strip())
    
    for test in range(t):
        n_k = input(f"Test case #{test+1} - Enter n and k separated by space: ").strip()
        while not n_k:
            n_k = input("Please enter valid n and k: ").strip()

        n, k = map(int, n_k.split())
        
        s_input = input(f"Enter {n} binary numbers separated by space (0 or 1): ").strip()
        while not s_input:
            s_input = input("Please enter the array: ").strip()
        
        s = list(map(int, s_input.split()))
        
        total = 0
        for comb in combinations(s, k):
            total = (total + median_of_sorted(comb)) % MOD
        
        print(f"Output for Test Case #{test+1}: {total}")

# Run the function
solve()
