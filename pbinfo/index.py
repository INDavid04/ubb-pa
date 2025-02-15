# https://www.pbinfo.ro/probleme/197/combinari

def combinari():
    # {1, 2, 3, 4} luam cate doua
    # 12 13 14 23 24 34
    # for i in range(n - k + 1)
    with open("combinari.in", 'r') as input_file:
        n, k = list(map(int, input_file.readline().split()))
    with open("combinari.out", 'w') as output_file:
        solutie = [0] * (k + 1)
        def afisare_combinare():
            solutie_str = "".join(list(map(str, solutie)))
            solutie_str = solutie_str[1:]
            output_file.write(f"{solutie_str}\n")
        def back(pas):
            for i in range(solutie[pas - 1] + 1, n - k + pas + 1):
                solutie[pas] = i
                if pas < k:
                    back(pas + 1)
                else:
                    afisare_combinare()
        back(1)
combinari()

# https://www.pbinfo.ro/probleme/125/permutari2

def permutari2():
    with open("permutari2.in", 'r') as input_file:
        n = int(input_file.readline())
        multime = list(map(int, input_file.readline().split()))
        multime.sort()
    ap = [0] * 101
    x = [0] * n
    with open("permutari2.out", 'w') as output_file:
        def afisare_permutare():
            solutie = "".join(list(map(str, x)))
            output_file.write(solutie + "\n")
        def back(k):
            for i in multime:
                if not ap[i]:
                    x[k] = i
                    ap[i] = 1
                    if k < n - 1:
                        back(k + 1)
                    else:
                        afisare_permutare()
                    ap[i] = 0
        back(0)
# permutari2()

# https://www.pbinfo.ro/probleme/124/permutari1

def permutari1():
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
# permutari1()

# https://www.pbinfo.ro/probleme/123/permutari

def permutari():
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
# permutari()
