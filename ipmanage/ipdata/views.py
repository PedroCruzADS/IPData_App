import json
import urllib

from deep_translator import GoogleTranslator
from django.shortcuts import render
from django.utils import timezone

from .models import Ip


def index(request):
    """View principal do site, onde está o campo de pesquisa do ip e onde é mostrado o resultado da pesquisa.

    Args:
        request (_type_): recebe uma requisição POST

    Returns:
        _type_: Retorna uma render com os dados da requisição nos campos de resultado.
    """
    context = {}

    if request.method == 'POST':
        erros = {}
        search = request.POST.get('search')

        if search == '':
            erros['vazio'] = "Campo vazio. Preencha com um IP válido. Exemplo: 8.8.8.8"

        elif search == '0.0.0.0':
            erros['invalido'] = "O IP submetido é inválido. Insira um ip válido."

        elif str(search).startswith('192'):
            erros['reservado'] = "O IP submetido é reservado localmente. Insira um ip válido."

        else:
            response = urllib.request.urlopen(
                f'http://ip-api.com/json/{search}')
            data = json.loads(response.read())

            en = [data['country'], data['regionName'],
                  data['city'], data['timezone']]
            pt_br = [GoogleTranslator(
                source='auto', target='pt').translate(x) for x in en]

            ip_instance = Ip(ip=data['query'],
                             pais=pt_br[0],
                             estado=pt_br[1],
                             cidade=pt_br[2],
                             pub_date=timezone.now())
            ip_instance.save()

            context = {"data": data}

            context['data'].update({
                "country": pt_br[0],
                "regionName": pt_br[1],
                "city": pt_br[2],
                "timezone": pt_br[3]
            })

        if erros:
            context['erros'] = erros

    return render(request, 'index.html', context=context)


def log(request):
    """View do histórico de buscas"""
    
    log_list = Ip.objects.all().order_by('-pub_date')
    return render(request, 'log.html', {'log_list': log_list})
