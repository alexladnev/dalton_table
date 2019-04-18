import math
import random

def get(n, k):
    count = 0
    az = 0
    Q = [0] * 1000001
    Z = [0] * 1000001
    while count < 100:
        i = 0
        t = 0
        j = 0
        w = 0
        d = 0
        asa = 0
        asas = 0
        v = 1
        p = 0
        m = 1
        A = [0] * 1000001
        B = [0] * 1000001
        C = [0] * 1000001
        D = [0] * 1000001
        F = [0] * 1000001
        if n == 0:
            m = 1

        while i < n:
            m = 2 * m
            i = i + 1

        while j < n + 1:
            u = n - j
            g = math.factorial(n) // math.factorial(j)
            A[j] = g * 1000000 // math.factorial(u)
            t = t + A[j]
            j = j + 1

        while p < n + 1:
            B[p] = A[p] * 1000000 // t
            p = p + 1

        C[0] = 0

        while v < n + 2:
            C[v] = B[v - 1] + C[v - 1]
            v = v + 1

        while w < k:
            F[w] = random.randint(0, 1000000)
            if F[w] >= C[0] and F[w] < C[1]:
                D[0] = D[0] + 1

            elif F[w] >= C[1] and F[w] < C[2]:
                D[1] = D[1] + 1

            elif F[w] >= C[2] and F[w] < C[3]:
                D[2] = D[2] + 1

            elif F[w] >= C[3] and F[w] < C[4]:
                D[3] = D[3] + 1

            elif F[w] >= C[4] and F[w] < C[5]:
                D[4] = D[4] + 1

            elif F[w] >= C[5] and F[w] < C[6]:
                D[5] = D[5] + 1

            elif F[w] >= C[6] and F[w] < C[7]:
                D[6] = D[6] + 1

            elif F[w] >= C[7] and F[w] < C[8]:
                D[7] = D[7] + 1

            elif F[w] >= C[8] and F[w] < C[9]:
                D[8] = D[8] + 1

            elif F[w] >= C[9] and F[w] < C[10]:
                D[9] = D[9] + 1

            elif F[w] >= C[10] and F[w] < C[11]:
                D[10] = D[10] + 1

            w = w + 1

        while asas < n + 1:
            Q[asas] = Q[asas] + D[asas]
            asas = asas + 1

        count = count + 1
    result = []
    while az < n + 1:
        Z[az] = Q[az] / 100
        if (Z[az]-(Z[az]//1)) >= 0.5:
            Q[az]=int((Z[az]//1 + 1))
        else:
            Q[az]=int((Z[az]//1))
        result.append(Q[az])
        az = az + 1
    return result
