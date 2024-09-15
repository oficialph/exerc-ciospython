largura_sala = float(input("Digite a largura da sala (em metros): "))
comprimento_sala = float(input("Digite o comprimento da sala (em metros): "))
area_sala = largura_sala * comprimento_sala

largura_quarto = float(input("Digite a largura do quarto (em metros): "))
comprimento_quarto = float(input("Digite o comprimento do quarto (em metros): "))
area_quarto = largura_quarto * comprimento_quarto

largura_banheiro = float(input("Digite a largura do banheiro (em metros): "))
comprimento_banheiro = float(input("Digite o comprimento do banheiro (em metros): "))
area_banheiro = largura_banheiro * comprimento_banheiro

area_total = area_sala + area_quarto + area_banheiro

print(f"Área da sala: {area_sala:.2f} m²")
print(f"Área do quarto: {area_quarto:.2f} m²")
print(f"Área do banheiro: {area_banheiro:.2f} m²")
print(f"Área total: {area_total:.2f} m²")