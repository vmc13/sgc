import csv
with open('fix/canhotos.csv', 'w') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow([
        'codigo', 'data', 'valor', 'tipo'
    ])
    # escrever mais de uma linha com writerows - plural
    rows = [
        [123, '2023-03-15', 12.50, 'Venda'],
        [345, '2023-03-15', 12.50, 'Venda'],
        [567, '2023-03-15', 12.50, 'Venda'],
        [789, '2023-03-15', 12.50, 'Venda'],
        [107, '2023-03-15', 12.50, 'Venda'],
    ] 
    csv_writer.writerows(rows)

# rodar no terminal com "python escrevendo_csv.py"
# arquivo gerado na pasta fix