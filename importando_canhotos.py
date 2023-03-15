import csv
from projeto.canhoto.models import Canhoto

def csv_to_list(filename: str) -> list:
    '''
    lê um csv e retorna um OrderDIct
    http://bit.ly/2FLDHsH
    '''
    with open(filename) as csv_file:
        reader = csv.DictReader(csv_file)
        csv_data = [line for line in reader]
    return csv_data

def save_data(data):
    '''
    Salva os dados no banco
    '''
    aux = []
    for item in data:
        codigo = item.get('codigo')
        data = item.get('data')
        valor = item.get('valor')
        tipo = item.get('tipo')
        obj = Canhoto(
            codigo=codigo,
            data=data,
            valor=valor,
            tipo=tipo,
        )
        aux.append(obj)
    Canhoto.objects.bulk_create(aux)

data = csv_to_list('fix/canhotos.csv')
save_data(data)



'''
verificação com python shell

> Canhoto.objects.all().count()
> Canhoto.objects.all.delete()


adicionar com
> python manage.py shell < importando_canhotos.py
'''