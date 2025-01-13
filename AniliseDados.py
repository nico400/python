import pandas as pd #usar "as PD" é para nao chamar escrever pandas toda hora, pd é tipo um apelido
table = pd.read_excel("Vendas.xlsx")
Total_billing = table["Valor Final"].sum()
billing_store = table[["ID Loja", "Produto", "Valor Final"]].groupby(["ID Loja", "Valor Final"]).sum()
print(billing_store)