import matplotlib.pyplot as plt

N = 100000
S = N - 1
I = 1
R = 0
beta = 0.25    
gamma = 0.08   
dias = 160

S_hist = []
I_hist = []
R_hist = []

for t in range(dias):
    novos_infectados = beta * S * I / N
    novos_recuperados = gamma * I

    S -= novos_infectados
    I += novos_infectados - novos_recuperados
    R += novos_recuperados

    S_hist.append(S)
    I_hist.append(I)
    R_hist.append(R)

plt.figure(figsize=(10, 6))
plt.plot(S_hist, label="Suscetíveis")
plt.plot(I_hist, label="Infectados")
plt.plot(R_hist, label="Recuperados")
plt.xlabel("Dias")
plt.ylabel("Número de indivíduos")
plt.title("Modelo SIR Discreto – Simulação Computacional")
plt.legend()
plt.grid(True)
plt.show()
