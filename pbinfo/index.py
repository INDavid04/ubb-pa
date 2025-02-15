# https://www.pbinfo.ro/probleme/124/permutari1
with open("permutari.in", 'r') as input_file:
    n = int(input_file.readline())
ap = [0] * (n + 1)
x = [0] * n
with open("permutari1.out", 'w') as output_file:
    def afisare_permutare():
        permutare_str = "".join(list(map(str, x)))
        output_file.write(permutare_str + "\n")
    def valid(i):
        if ap[i]:
            return False
        return True
    def back(k):
        for i in range(n, 0, -1):
            if valid(i):
                x[k] = i
                ap[i] = 1
                if k < n - 1:
                    back(k + 1)
                else:
                    afisare_permutare()
                ap[i] = 0
    back(0)

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
