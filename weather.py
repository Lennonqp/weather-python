import requests
import os

api_key = os.getenv('OPENWHATER_API_KEY', 'a54f6325c37cc685ad2e8d1232be84df')
base_url = 'https://api.openweathermap.org/data/2.5/weather'

while True:
    cidade = input('\nDigite o nome da cidade que queira ver a temperatura:')

    params = {
        'q': cidade,
        'appid': api_key,
        'units': 'metric',
        'lang': 'pt_br'    
    }

    print (f'Buscando o clima de {cidade}...')

    try:
        
        response = requests.get(base_url, params=params)
        
        response.raise_for_status()
        
        data = response.json()
        
        descricao_clima = data ['weather'][0]['description'].capitalize()
        temperatura_atual = data ['main']['temp']
        sensacao_termica = data ['main']['feels_like']
        temp_minima = data ['main']['temp_min']
        temp_maxima = data ['main']['temp_max']
        umidade = data ['main']['humidity']
        
        print('-'*30)
        print(f'O clima em {data['name']} está: {descricao_clima}')
        print(f'Temperatura atual {temperatura_atual :.1f}°C')
        print(f'Sensação térmica de {sensacao_termica :.1f}°C')
        print(f'Com mínima de {temp_minima :.1f}°C e máxima de {temp_maxima :.1f}°C')
        print(f'Umidade no ar: {umidade}%')
        print('-'*30)
        
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 401:
            print('Erro de autenticação: Verifique sua chave de API')
        elif response.status_code == 404:
            print(f"Erro: Cidade '{cidade}' não encontrada.")
        else:
            print(f'Erro HTTP: {http_err}')
    except requests.exceptions.RequestException as err:
        print(f'Erro na requisição: {err}')
    except KeyError:
        print('Erro ao processar os dados recebidos da API. A estrutura pode tem mudado.')
        
    while True:
        try:
            continuar = int(input('Deseja visualizar o tempo de outra cidade? 1 - SIM | 2-Não'))
            
            if continuar == 2:
                print('Obrigado por usar')
                exit()
            elif continuar == 1:
                break
            else:
                print('Resposta não reconhecida. Por favor responda de novo')
        except ValueError:
            print('Por favor, digite 1 ou 2')            

