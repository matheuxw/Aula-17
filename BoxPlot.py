import pandas as pd

df = pd.read_csv(r"C:\Users\matheus.sandrade\Downloads\funcionarios.csv")
s = df["lucro"]

q1, q2, q3 = s.quantile([0.25, 0.5, 0.75])
iqr = q3 - q1
lim_inf = q1 - 1.5 * iqr
lim_sup = q3 + 1.5 * iqr

outliers = df[(s < lim_inf) | (s > lim_sup)]