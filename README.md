# PyRedeMet
A Python interface to API-RedeMet (https://ajuda.decea.gov.br/artigo-categoria/redemet/).

A API da REDEMET é um produto de interfaces de programação de aplicativos(APIs), que irá proporcionar acesso a vários produtos meteorológicos, hoje disponibilizados no site da REDEMET, de modo rápido e seguro para serem utilizados em diversos fins.

## Produtos disponíveis
Para a obtenção de cada produto há uma sintase própria de solicitação que pode ser conferida na lista abaixo:

* Aeródromos - `get_aerodromos(pais)`
* Aeródromos Status - `get_aerodromos_status(pais)`
* Aeródromos Info - `get_aerodromos_info(localidade, metar, taf, datahora)`
* Produtos AMDAR - `get_produtos_amdar(data)`
* Produtos MODELO - `get_produtos_modelo(modelo, area, produto, nivel, anima, timeout)`
* Produtos RADAR - `get_produto_radar(tipo, area, data, anima, timeout)`
* Produtos SATÉLITE - `get_produto_satelite(api_key, tipo, data, anima)`
* Produtos STSC - `get_produto_stsc(api_key, data, anima)`
* Mensagem Aviso de Aeródromo - `get_mensagens_aviso(api_key, localidades, data_ini, data_fim, page_tam)`
* Mensagem GAMET - `get_mensagens_gamet(api_key, pais, data_ini, data_fim, page_tam)`
* Mensagem METAR - `get_mensagens_metar(api_key, localidades, data_ini, data_fim, page_tam)`
* Mensagem Meteograma - `get_mensagens_meteograma(api_key, localidade, data_hora)`
* Mensagem PILOT - `get_mensagens_pilot(api_key, estacao, data_ini, data_fim, page_tam)`
* Mensagem SIGMET - `get_mensagens_sigmet(api_key, pais, data_ini, data_fim, page_tam)`
* Mensagem TAF - `get_mensagens_taf(api_key, localidades, data_ini, data_fim, page_tam, fim_linha)`
* Mensagem TEMP - `get_mensagens_temp(api_key, estacao, data_ini, data_fim, page_tam)`

## Mode de utilização:

    import pyredemet
 
    api_key = 'SUA_API_KEY'
    redemet = pyredemet(api_key)

    ## Aerodromos
    result = redemet.get_aerodromos(pais='Brasil')

    result = redemet.get_aerodromos_status(pais='Brasil')

    result = redemet.get_aerodromos_info(localidade='SBBR', metar='sim', taf='sim')

    ## Produtos
    result = redemet.get_produtos_amdar(data='2020032415')

    result = redemet.get_produtos_modelo(modelo='wifs',area='b1',produto='vento-altitude-barb',nivel='600',anima=2)

    result = redemet.get_produto_radar(tipo='maxcappi',area='tm',data='2020032410',anima=2)

    result = redemet.get_produto_satelite(tipo='vis', data='2020032410', anima=2)

    result = redemet.get_produto_stsc(data='2020032410', anima=2)

    ## Mensagens
    result = redemet.get_mensagens_aviso(localidades='SBBR,SBPA', data_ini='2020030912', data_fim='2020030912')

    result = redemet.get_mensagens_gamet(pais='Brasil', data_ini='202006120300',data_fim='202006120300')

    result = redemet.get_mensagens_metar(localidades='SBBR,SBPA', data_ini='2020030912',data_fim='2020030912')

    result = redemet.get_mensagens_meteograma(localidade='SBBR', data_hora='2020030912', horas=12)

    result = redemet.get_mensagens_pilot(estacao=83378,data_ini='2020030912',data_fim='2020030912')

    result = redemet.get_mensagens_sigmet(pais='Brasil', data_ini='202007071200',data_fim='202007071800')

    result = redemet.get_mensagens_taf(localidades='SBBR,SBPA', data_ini='2020030912',data_fim='2020030912', page_tam=100, fim_linha='texto')

    result = redemet.get_mensagens_temp(estacao=83378,data_ini='2020030912',data_fim='2020030912')
