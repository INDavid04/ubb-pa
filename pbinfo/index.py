# https://www.pbinfo.ro/probleme/123/permutari

with open("permutari.in", 'r') as file_input:
    n = int(file_input.readline())
ap = [0] * (n + 1)
permutare = [0] * (n + 1)

with open("permutari.out", 'w') as file_output:
    def afisare_permutare():
        permutare_str = "".join(list(map(str, permutare)))
        permutare_str = permutare_str[1:]
        file_output.write(permutare_str + "\n")

    def back(k):
        for i in range(1, n + 1):
            if not ap[i]:
                permutare[k] = i
                ap[i] = 1
                if k < n:
                    back(k + 1)
                else:
                    afisare_permutare()
                ap[i] = 0
    back(1)
