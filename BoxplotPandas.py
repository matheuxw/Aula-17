import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\matheus.sandrade\Downloads\funcionarios.csv")


print(df)

salario = df["salario"].to_numpy()

print(salario)

q1 = np.percentile(salario, 25)
q2 = np.percentile(salario, 50)
q3 = np.percentile(salario, 75)

print("Primeiro Quartil\n")
print(q1)
print("\nmediana\n")
print(q2)
print("\nTerceiro Quartil\n")
print(q3)