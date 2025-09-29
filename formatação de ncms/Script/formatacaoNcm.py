import os


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
entrada_path = os.path.join(base_dir, "Listas", "NcmBruto.txt")
saida_path = os.path.join(base_dir, "Listas", "NcmFormatado.txt")

with open(entrada_path, "r") as f:
    linhas = f.readlines()

# aqui ele quebra o numero em blocos de 8 digitos cada (tamanho padrao dos codigos ncm)
ncm_Unico = sorted(set(linha.strip() for linha in linhas if linha.strip()))

# Formata com aspas simples e vírgula
ncms_formatados = ', '.join(f"'{codigo}'" for codigo in ncm_Unico)

with open(saida_path, "w") as f:
    f.write(ncms_formatados)

print(f"ncms formatados! Arquivo salvo em: {saida_path}")