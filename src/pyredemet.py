#!/usr/bin/ebv python
# coding=utf-8

import json
import requests

class pyredemet:
    """[summary] A API da REDEMET é um produto de interfaces de programação de aplicativos(APIs), que proporciona acesso a vários produtos meteorológicos.
    """
    def __init__(self, api_key, server_url="https://api-redemet.decea.gov.br", log_level=None,):

        """[summary]

        Args:
            api_key ([type]): [description]
        """

        self.api_key = api_key
        self.log_level = log_level
        self.server_url = server_url

        if len(self.api_key) < 40:
            raise TypeError("Tamanho da chave API_KEY menor que 40")

        if not isinstance(self.server_url, str):
            raise TypeError("O servidor não é uma string")

    def get_aerodromos(self, pais=None):
        #API destina à retornar informações de Aeródromos de países disponíveis no banco de dados da REDEMET.
        #https://api-redemet.decea.gov.br/aerodromos
        #Parâmetros
        #    Nome	Requerido	Descrição	Valor Padrão	Exemplo
        #    pais	Não	Nome do país.	Brasil	Argentina
        #Exemplo de Solicitação
        #    https://api-redemet.decea.gov.br/aerodromos/?api_key=SUA_CHAVE_AQUI&pais=Argentina
        
        params = { 'api_key': self.api_key }

        if pais is not None:
            if (isinstance(pais, str)):
                params.update({'pais': pais})
            else:
                raise TypeError("Error: O pais não é uma string")

        try:
            url = self.server_url + "/aerodromos/"
            response = requests.get(url, params=params)
        except Exception as ex:
            raise RuntimeError("Error: " + repr(ex))

        if response.status_code == 200:
            response = response.json() 
            if response['status'] == False:
                print('get_aerodromos [!] HTTP status == False')
            if response['message'] != '':
                print('get_aerodromos [!] HTTP message == ' + str(response['message']))
            return response['data']
        else:
            print('get_aerodromos [!] HTTP {0} calling [{1}]'.format(response.status_code, response.request.url))
            return None

    def get_aerodromos_status(self, pais):
        # GET aerodromos/status
        # API destina à retornar status das localidades em cores.
        # As cores são obtidas através de avaliação de parâmetros baseados em visibilidade e teto da localidade, conforme tabela abaixo.

        # Valor	Visibilidade(m)	Condição	Teto(ft)
        # g	>= 5000	e	>= 1500
        # y	< 5000 e >= 1500	e/ou	< 1500 e > 500
        # r	< 1500	e/ou	< 600
        # Endereço de Acesso
        # https://api-redemet.decea.gov.br/aerodromos/status
        # Parâmetros
        # Nome	Requerido	Descrição	Valor Padrão	Exemplo
        # pais	Sim	País que se deseja as informações de status.
        # Para obter informações de mais de um país, basta informar separados por vígula.	BRASIL	BRASIL,ARGENTINA
        # Exemplo de Solicitação
        # https://api-redemet.decea.gov.br/aerodromos/status?api_key=SUA_CHAVE_AQUI

        params = { 'api_key': self.api_key }

        if isinstance(pais, str):
            params.update({'pais': pais})
        else:
            raise TypeError("Error: O pais não é uma string")

        try:
            url = self.server_url + "/aerodromos/status"
            response = requests.get(url, params=params)
        except Exception as ex:
            raise RuntimeError("Error: " + repr(ex))

        if response.status_code == 200:
            response = response.json() 
            if response['status'] == False:
                print('get_aerodromos_status [!] HTTP status == False')
            if response['message'] != '':
                print('get_aerodromos_status [!] HTTP message == ' + str(response['message']))
            return response['data']
        else:
            print('get_aerodromos_status [!] HTTP {0} calling [{1}]'.format(response.status_code, response.request.url))
            return None

    def get_aerodromos_info(self, localidade, metar=None, taf=None, datahora=None):
        # API destina à retornar informações das condições meteorológicas de uma localidade disponível no banco de dados da REDEMET.

        # Endereço de Acesso
        # https://api-redemet.decea.gov.br/aerodromos/info

        # Parâmetros
        # Nome	Requerido	Descrição	Valor Padrão	Exemplo
        # localidade	Sim	Indicativo de localidade ICAO.	Não há	SBBR
        # metar	Não	METAR codificado da localidade.	sim	sim
        # taf	Não	TAF codificado da localidade	nao	sim
        # datahora	Não	Data no formato (YYYYMMDDHH)	Data e hora atual	2019010100
        # Exemplo de Solicitação
        # https://api-redemet.decea.gov.br/aerodromos/info?api_key=SUA_CHAVE_AQUI&localidade=SBBR&datahora=2019010100

        params = { 'api_key': self.api_key }

        if isinstance(localidade, str):
            if len(localidade) == 4:
                params.update({'localidade': localidade})
            else:
                raise TypeError("Error: A localidade não esta no formato certo (4 chars)")
        else:
            raise TypeError("Error: A localidade não é uma string")
        
        if metar is not None:
            if (isinstance(metar, str)):
                params.update({'metar': metar})
            else:
                raise TypeError("Error: A metar não é uma str")
        if taf is not None:
            if (isinstance(taf, str)):
                params.update({'taf': taf})
            else:
                raise TypeError("Error: A taf não é uma string")
        
        if datahora is not None:
            if (isinstance(datahora, str)):
                if len(datahora) == 10:
                    params.update({'datahora': datahora})
                else:
                    raise TypeError("Error: A datahora não esta no formato correto (YYYYMMDDHH)")    
            else:
                raise TypeError("Error: A datahora não é uma string")

        try:
            url = self.server_url + "/aerodromos/info"
            response = requests.get(url, params=params)
        except Exception as ex:
            raise RuntimeError("Error: " + repr(ex))

        if response.status_code == 200:
            response = response.json() 
            if response['status'] == False:
                print('get_aerodromos_info [!] HTTP status == False')
            if response['message'] != '':
                print('get_aerodromos_info [!] HTTP message == ' + str(response['message']))
            return response['data']
        else:
            print('get_aerodromos_info [!] HTTP {0} calling [{1}]'.format(response.status_code, response.request.url))
            return None

    def get_produtos_amdar(self, data):
        # GET produtos/amdar
        # API destina à retornar informações do AMDAR

        # Endereço de Acesso
        # https://api-redemet.decea.gov.br/produtos/amdar

        # Parâmetros
        # Nome	Requerido	Descrição	Valor Padrão	Exemplo
        # data	Não	Data no formato YYYYMMDDHH	Data atual	2020051200
        # Exemplo de Solicitação
        # https://api-redemet.decea.gov.br/produtos/amdar?api_key=SUA_CHAVE_AQUI&data=2020032415

        params = { 'api_key': self.api_key }

        if isinstance(data, str):
            if len(data) == 10:
                params.update({'data': data})
            else:
                raise TypeError("Error: A data não esta no formato correto (YYYYMMDDHH)")    
        else:
            raise TypeError("Error: A data não é uma string")

        try:
            url = self.server_url + "/produtos/amdar"
            response = requests.get(url, params=params)
        except Exception as ex:
            raise RuntimeError("Error: " + repr(ex))

        if response.status_code == 200:
            response = response.json() 
            if response['status'] == False:
                print('get_produtos_amdar [!] HTTP status == False')
            if response['message'] != '':
                print('get_produtos_amdar [!] HTTP message == ' + str(response['message']))
            return response['data']
        else:
            print('get_produtos_amdar [!] HTTP {0} calling [{1}]'.format(response.status_code, response.request.url))
            return None

    def get_produtos_modelo(self, modelo, area, produto, nivel, anima=None, timeout=180):
        # GET produtos/modelo
        # API destina à retornar informações de imagens geradas pela modelagem numérica disponíveis na REDEMET.

        # Endereço de Acesso
        # https://api-redemet.decea.gov.br/produtos/modelo

        # Parâmetros
        # Nome	Requerido	Descrição	Valor Padrão	Exemplo
        # modelo	Sim	     wifs       Não há	        wifs
        # area	    Sim	      x         Não há	        b1
        # produto	Sim	      x         Não há	        cb_top
        # nivel	    Sim	      x         Não há	        600
        # anima	    Não	      x     	Não há	        5
        # Exemplo de Solicitação
        # https://api-redemet.decea.gov.br/produtos/modelo?api_key=SUA_CHAVE_AQUI&modelo=wifs&area=b1&produto=vento-altitude-barb&nivel=600&anima=2

        params = { 'api_key': self.api_key }

        if isinstance(modelo, str):
            params.update({'modelo': modelo})
        else:
            raise TypeError("Error: O modelo não é uma string")
        
        if isinstance(area, str):
            if area in ('b1','as','az','ao','bs','cw','re'):
                params.update({'area': area})
            else:
                raise TypeError("Error: A area informada não está disponivel")
        else:
            raise TypeError("Error: A area não é uma string")

        if isinstance(produto, str):
            if produto in ('vento-altitude-barb','vento-altitude-corrente',
                           'vento-altitude-magnitude','vento-temperatura-altitude',
                           'temperatura-altitude-shaded','temperatura-altitude-grid',
                           'temperatura-altitude-contour','umidade-relativa-shaded',
                           'umidade-relativa-contour','cb_cobertura','cb_base',
                           'cb_topo','pot_max_fga_shaded','pot_max_fga_contour',
                           'cat_max_pot','incldturb'):
                params.update({'produto': produto})
            else:
                raise TypeError("Error: O produto informado não está disponivel")
        else:
            raise TypeError("Error: O produto não é uma string")
            
        if isinstance(nivel, str):
            if nivel in ('850','700','600','500','400','350','300',
                         '275','250','225','200','150','100'):
                params.update({'nivel': nivel})
            else:
                raise TypeError("Error: O nivel informado não está disponivel")
        else:
            raise TypeError("Error: O nivel não é uma string")
        
        if anima is not None:
            if anima <= 11:
                params.update({'anima': anima})
            else:
                raise TypeError("Error: O anima informado é maior que 11")
        
        try:
            url = self.server_url + "/produtos/modelo"
            response = requests.get(url, params=params, timeout=timeout)
        except Exception as ex:
            raise RuntimeError("Error: " + repr(ex))

        if response.status_code == 200:
            response = response.json() 
            if response['status'] == False:
                print('get_produtos_modelo [!] HTTP status == False')
            if response['message'] != '':
                print('get_produtos_modelo [!] HTTP message == ' + str(response['message']))
            return response['data']
        else:
            print('get_produtos_modelo [!] HTTP {0} calling [{1}]'.format(response.status_code, response.request.url))
            return None 

    def get_produto_radar(self, tipo, area, data=None, anima=None, timeout=180):
        # GET produtos/radar
        # API destina à retornar imagens de eco de Radar Meteorológico.
        # Há disponibilidade de METAR desde 01/01/2006 até a presente data.

        # Endereço de Acesso
        # https://api-redemet.decea.gov.br/produtos/radar/{tipo}

        # Parâmetros
        # Nome	Requerido	Descrição	Valor Padrão	Exemplo
        # tipo	Sim	Tipo de eco disponíveis
        # maxccapi	07km
        # data	Não	Data no formato YYYYMMDDHH	Data atual	2020031211
        # area	Sim	Radares disponíveis
        # Não há	pv
        # anima	Não	Informe a quantidade de ecos de radar que deseja animar.
        # A animação tem como referência a opção data como última imagem.
        # O valor máximo permitido para a animação é 15.	1	10
        # Exemplo de Solicitação
        # https://api-redemet.decea.gov.br/produtos/radar/maxcappi?api_key=SUA_CHAVE_AQUI&data=2020032410

        params = { 'api_key': self.api_key }

        if isinstance(tipo, str):
            if tipo in ('maxcappi','10km','07km','05km','03km'):
                tipo_url = tipo
            else:
                raise TypeError("Error: O tipo informado não está disponivel")
        else:
            raise TypeError("Error: O tipo não é uma string")
        
        if data is not None:
            if isinstance(data, str):
                if len(data) == 10 :
                    params.update({'data': data})
                else:
                    raise TypeError("Error: A data informada não está no formato correto (YYYYMMDDHH) ")
            else:
                raise TypeError("Error: A data não é uma string")

        if isinstance(area, str):
            if area in ('al','be','bv','cn','cz','ga','jr',
                        'mq','mo','mn','mi','nt','pl','pc',
                        'pv','sv','sn','st','sg','sf','ua',
                        'sl','sr','tt','tf','tm'):
                params.update({'area': area})
            else:
                raise TypeError("Error: A area informada não está disponivel")
        else:
            raise TypeError("Error: A area não é uma string")
            
        if anima is not None:
            if anima <= 15:
                params.update({'anima': anima})
            else:
                raise TypeError("Error: O anima informado é maior que 11")
        
        try:
            url = self.server_url + "/produtos/radar/" + tipo_url
            response = requests.get(url, params=params, timeout=timeout)
        except Exception as ex:
            raise RuntimeError("Error: " + repr(ex))

        if response.status_code == 200:
            response = response.json() 
            if response['status'] == False:
                print('get_produto_radar [!] HTTP status == False')
            if response['message'] != '':
                print('get_produto_radar [!] HTTP message == ' + str(response['message']))
            return response['data']
        else:
            print('get_produto_radar [!] HTTP {0} calling [{1}]'.format(response.status_code, response.request.url))
            return None 

    def get_produto_satelite(self, tipo, data=None, anima=None, timeout=180):
        # GET produtos/satelite
        # API destina à retornar informações de imagens de satélite disponíveis na REDEMET.

        # Endereço de Acesso
        # https://api-redemet.decea.gov.br/produtos/satelite/{tipo}

        # Parâmetros
        # Nome	Requerido	Descrição	Valor Padrão	Exemplo
        # tipo	Sim	Tipos disponíveis
        # Não há	realcada
        # data	Não	Data no formato YYYYMMDDHH	Data atual	2020051200
        # anima	Não	Informe a quantidade de imagens que deseja animar.
        # A animação tem como referência a opção data como última imagem.
        # O valor máximo permitido para a animação é 15.	1	10
        # Exemplo de Solicitação
        # https://api-redemet.decea.gov.br/produtos/satelite/realcada?api_key=SUA_CHAVE_AQUI&data=2020032114
        params = { 'api_key': self.api_key }

        if isinstance(tipo, str):
            if tipo in ('ir','realcada','vis'):
                tipo_url = tipo
            else:
                raise TypeError("Error: O tipo informado não está disponivel")
        else:
            raise TypeError("Error: O tipo não é uma string")
        
        if data is not None:
            if isinstance(data, str):
                if len(data) == 10 :
                    params.update({'data': data})
                else:
                    raise TypeError("Error: A data informada não está no formato correto (YYYYMMDDHH) ")
            else:
                raise TypeError("Error: A data não é uma string")

        if anima is not None:
            if anima <= 15:
                params.update({'anima': anima})
            else:
                raise TypeError("Error: O anima informado é maior que 11")
        
        try:
            url = self.server_url + "/produtos/satelite/" + tipo_url
            response = requests.get(url, params=params, timeout=timeout)
        except Exception as ex:
            raise RuntimeError("Error: " + repr(ex))

        if response.status_code == 200:
            response = response.json() 
            if response['status'] == False:
                print('get_produto_satelite [!] HTTP status == False')
            if response['message'] != '':
                print('get_produto_satelite [!] HTTP message == ' + str(response['message']))
            return response['data']
        else:
            print('get_produto_satelite [!] HTTP {0} calling [{1}]'.format(response.status_code, response.request.url))
            return None 

    def get_produto_stsc(self, data=None, anima=None, timeout=180):
        # GET produtos/stsc
        # API destina à retornar mensagens as informação de ocorrência de trovoada.

        # Endereço de Acesso
        # https://api-redemet.decea.gov.br/produtos/stsc

        # Parâmetros
        # Nome	Requerido	Descrição	Valor Padrão	Exemplo
        # data	Não	Data no formato YYYYMMDDHH	Data atual	2020051200
        # anima	Não	Informe a quantidade de ocorrências que deseja animar.
        # A animação tem como referência a opção data como última imagem.
        # O valor máximo permitido para a animação é 60.	1	10
        # Exemplo de Solicitação
        # https://api-redemet.decea.gov.br/produtos/satelite/stsc?api_key=SUA_CHAVE_AQUI&data=2020032114
        params = { 'api_key': self.api_key }

        if data is not None:
            if isinstance(data, str):
                if len(data) == 10 :
                    params.update({'data': data})
                else:
                    raise TypeError("Error: A data informada não está no formato correto (YYYYMMDDHH) ")
            else:
                raise TypeError("Error: A data não é uma string")

        if anima is not None:
            if anima <= 60:
                params.update({'anima': anima})
            else:
                raise TypeError("Error: O anima informado é maior que 11")
        
        try:
            url = self.server_url + "/produtos/stsc"
            response = requests.get(url, params=params, timeout=timeout)
        except Exception as ex:
            raise RuntimeError("Error: " + repr(ex))

        if response.status_code == 200:
            response = response.json() 
            if response['status'] == False:
                print('get_produto_stsc [!] HTTP status == False')
            if response['message'] != '':
                print('get_produto_stsc [!] HTTP message == ' + str(response['message']))
            return response['data']
        else:
            print('get_produto_stsc [!] HTTP {0} calling [{1}]'.format(response.status_code, response.request.url))
            return None 

    def get_mensagens_aviso(self, localidades, data_ini=None, data_fim=None, page_tam=None):
        # GET mensagens/aviso
        # API destina à retornar mensagens Aviso de Aeródromo das localidades disponíveis no banco de dados da REDEMET.
        # Há disponibilidade de mensagens desde 01/01/2003 até a presente data.

        # Endereço de Acesso
        # https://api-redemet.decea.gov.br/mensagens/aviso/{localidades}

        # Parâmetros
        # Nome	Requerido	Descrição	Valor Padrão	Exemplo
        # localidades	Sim	Indicativo de localidade ICAO.
        # Quando precisar informar mais de uma localidade, basta informar separado por vírgula sem intervalo.	Não há	SBBR
        # data_ini	Não	Data no formato YYYYMMDDHH	Data atual	2020051200
        # data_fim	Não	Data no formato YYYYMMDDHH	Data atual	2020051206
        # page_tam	Não	Número de registros por página	150	100
        # Exemplo de Solicitação
        # https://api-redemet.decea.gov.br/mensagens/aviso/SBBG?api_key=SUA_CHAVE_AQUI&data_ini=2020030313&data_fim=2020030313
        params = { 'api_key': self.api_key }

        if isinstance(localidades, str):
            check = len(localidades) - 4 # SBBR,SBCF ... [4],[4] -> 9 elementos: Possibilidades 4,9,14,18,24 (4)+(5)*(Numero adicional de localidades)
            if check % 5 == 0:
                localidades_url = localidades
            else:
                raise TypeError("Error: As localidades não estão no padrao correto [SBBR,SBCF,..]")
        else:
            raise TypeError("Error: A localidades não são uma string")

        if data_ini is not None:
            if isinstance(data_ini, str):
                if len(data_ini) == 10 :
                    params.update({'data_ini': data_ini})
                else:
                    raise TypeError("Error: A data_ini informada não está no formato correto (YYYYMMDDHH) ")
            else:
                raise TypeError("Error: A data_ini não é uma string")
        
        if data_fim is not None:
            if isinstance(data_fim, str):
                if len(data_fim) == 10 :
                    params.update({'data_fim': data_fim})
                else:
                    raise TypeError("Error: A data_fim informada não está no formato correto (YYYYMMDDHH) ")
            else:
                raise TypeError("Error: A data_fim não é uma string")


        if page_tam is not None:
            params.update({'page_tam': page_tam})
        
        try:
            url = self.server_url + "/mensagens/aviso/" + localidades_url
            response = requests.get(url, params=params)
        except Exception as ex:
            raise RuntimeError("Error: " + repr(ex))

        if response.status_code == 200:
            response = response.json() 
            if response['status'] == False:
                print('get_mensagens_aviso [!] HTTP status == False')
            if response['message'] != '':
                print('get_mensagens_aviso [!] HTTP message == ' + str(response['message']))
            return response['data']
        else:
            print('get_mensagens_aviso [!] HTTP {0} calling [{1}]'.format(response.status_code, response.request.url))
            return None 

    def get_mensagens_gamet(self, pais, data_ini=None, data_fim=None, page_tam=None):
        # GET mensagens/gamet
        # API destina à retornar mensagens GAMET dos países disponíveis no banco de dados da REDEMET.

        # Endereço de Acesso
        # https://api-redemet.decea.gov.br/mensagens/gamet

        # Parâmetros
        # Nome	Requerido	Descrição	Valor Padrão	Exemplo
        # pais	Sim	Nome do País	Brasil	Argentina
        # data_ini	Não	Data no formato YYYYMMDDHHII	Data atual	202005120000
        # data_fim	Não	Data no formato YYYYMMDDHHII	Data atual	202005120600
        # page_tam	Não	Número de registros por página	150	100
        # Exemplo de Solicitação
        # https://api-redemet.decea.gov.br/mensagens/gamet/?api_key=SUA_CHAVE_AQUI&data_ini=202006120300&data_fim=202006120300
        params = { 'api_key': self.api_key }

        if isinstance(pais, str):
            params.update({'pais': pais})
        else:
            raise TypeError("Error: O pais não é uma string")

        if data_ini is not None:
            if isinstance(data_ini, str):
                if len(data_ini) == 12 :
                    params.update({'data_ini': data_ini})
                else:
                    raise TypeError("Error: A data_ini informada não está no formato correto (YYYYMMDDHHII) ")
            else:
                raise TypeError("Error: A data_ini não é uma string")
        
        if data_fim is not None:
            if isinstance(data_fim, str):
                if len(data_fim) == 12 :
                    params.update({'data_fim': data_fim})
                else:
                    raise TypeError("Error: A data_fim informada não está no formato correto (YYYYMMDDHHII) ")
            else:
                raise TypeError("Error: A data_fim não é uma string")


        if page_tam is not None:
            params.update({'page_tam': page_tam})
        
        try:
            url = self.server_url + "/mensagens/gamet" 
            response = requests.get(url, params=params)
        except Exception as ex:
            raise RuntimeError("Error: " + repr(ex))

        if response.status_code == 200:
            response = response.json() 
            if response['status'] == False:
                print('get_mensagens_gamet [!] HTTP status == False')
            if response['message'] != '':
                print('get_mensagens_gamet [!] HTTP message == ' + str(response['message']))
            return response['data']
        else:
            print('get_mensagens_gamet [!] HTTP {0} calling [{1}]'.format(response.status_code, response.request.url))
            return None 

    def get_mensagens_metar(self, localidades, data_ini=None, data_fim=None, page_tam=None):
        # GET mensagens/metar
        # API destina à retornar mensagens METAR das localidades disponíveis no banco de dados da REDEMET.
        # Há disponibilidade de mensagens desde 01/01/2003 até a presente data.

        # Endereço de Acesso
        # https://api-redemet.decea.gov.br/mensagens/metar/{localidades}

        # Parâmetros
        # Nome	Requerido	Descrição	Valor Padrão	Exemplo
        # localidades	Sim	Indicativo de localidade ICAO.
        # Quando precisar informar mais de uma localidade, basta informar separado por vírgula sem intervalo.	Não há	SBBR
        # data_ini	Não	Data no formato YYYYMMDDHH	Data atual	2020051200
        # data_fim	Não	Data no formato YYYYMMDDHH	Data atual	2020051206
        # page_tam	Não	Número de registros por página	150	100
        # Exemplo de Solicitação
        # https://api-redemet.decea.gov.br/mensagens/metar/SBGL,SBBR?api_key=SUA_CHAVE_AQUI&data_ini=2019010100&data_fim=2019010101
        params = { 'api_key': self.api_key }

        if isinstance(localidades, str):
            check = len(localidades) - 4 # SBBR,SBCF ... [4],[4] -> 9 elementos: Possibilidades 4,9,14,18,24 (4)+(5)*(Numero adicional de localidades)
            if check % 5 == 0:
                localidades_url = localidades
            else:
                raise TypeError("Error: As localidades não estão no padrao correto [SBBR,SBCF,..]")
        else:
            raise TypeError("Error: A localidades não são uma string")

        if data_ini is not None:
            if isinstance(data_ini, str):
                if len(data_ini) == 10 :
                    params.update({'data_ini': data_ini})
                else:
                    raise TypeError("Error: A data_ini informada não está no formato correto (YYYYMMDDHH) ")
            else:
                raise TypeError("Error: A data_ini não é uma string")
        
        if (data_fim is not None) and (data_ini is not None):
            if isinstance(data_fim, str) and isinstance(data_ini, str):
                if len(data_fim) == 10 and len(data_ini) == 10:
                    params.update({'data_fim': data_fim})
                else:
                    raise TypeError("Error: A data_fim ou data ini informadas não estão no formato correto (YYYYMMDDHH) ")
            else:
                raise TypeError("Error: A data_fim ou data ini não são strings")


        if page_tam is not None:
            params.update({'page_tam': page_tam})
        
        try:
            url = self.server_url + "/mensagens/metar/" + localidades_url
            response = requests.get(url, params=params)
        except Exception as ex:
            raise RuntimeError("Error: " + repr(ex))

        if response.status_code == 200:
            response = response.json() 
            if response['status'] == False:
                print('get_mensagens_metar [!] HTTP status == False')
            if response['message'] != '':
                print('get_mensagens_metar [!] HTTP message == ' + str(response['message']))
            return response['data']
        else:
            print('get_mensagens_metar [!] HTTP {0} calling [{1}]'.format(response.status_code, response.request.url))
            return None 

    def get_mensagens_meteograma(self, localidade, data_hora=None, horas=None):
        # GET mensagens/meteograma
        # API destina à retornar informações de mensagens de METAR, TAF e Aviso de Aeródromo das localidades disponíveis no banco de dados da REDEMET.

        # Além de retornar as mensagens acima mencionadas, algumas informações também são disponibilizadas, tais como:

        # Decodificação de METAR e TAF da data e hora solicitada
        # Informações de até 96 horas passadas com base na data e hora solicitada
        # Separação de grupos do METAR
        # Há disponibilidade de mensagens desde 01/01/2003 até a presente data.
        # Endereço de Acesso
        # https://api-redemet.decea.gov.br/mensagens/meteograma/{localidades}

        # Parâmetros
        # Nome	Requerido	Descrição	Valor Padrão	Exemplo
        # localidade	Sim	Indicativo de localidade ICAO.
        # Somente será permitido uma localidade por solicitação.	Não há	SBBR
        # data_hora	Não	Data no formato YYYYMMDDHH	Data atual	2020051200
        # horas	Não	Determina quantas horas passadas a partir de data_hora	96	72
        # Exemplo de Solicitação
        # https://api-redemet.decea.gov.br/mensagens/meteograma/SBBR?api_key=SUA_CHAVE_AQUI&data_hora=2020042114
        params = { 'api_key': self.api_key }

        if isinstance(localidade, str):
            if len(localidade) == 4:
                localidade_url = localidade
            else:
                raise TypeError("Error: A localidade não esta no padrao correto [SBBR,SBCF,..]")
        else:
            raise TypeError("Error: A localidade não é uma string")

        if data_hora is not None:
            if isinstance(data_hora, str):
                if len(data_hora) == 10 :
                    params.update({'data_hora': data_hora})
                else:
                    raise TypeError("Error: A data_hora informada não está no formato correto (YYYYMMDDHH) ")
            else:
                raise TypeError("Error: A data_hora não é uma string")
        
        if horas is not None:
            params.update({'horas': horas})
            
        try:
            url = self.server_url + "/mensagens/meteograma/" + localidade_url
            response = requests.get(url, params=params)
        except Exception as ex:
            raise RuntimeError("Error: " + repr(ex))

        if response.status_code == 200:
            response = response.json() 
            if response['status'] == False:
                print('get_mensagens_meteograma [!] HTTP status == False')
            if response['message'] != '':
                print('get_mensagens_meteograma [!] HTTP message == ' + str(response['message']))
            return response['data']
        else:
            print('get_mensagens_meteograma [!] HTTP {0} calling [{1}]'.format(response.status_code, response.request.url))
            return None 

    def get_mensagens_pilot(self, estacao, data_ini=None, data_fim=None, page_tam=None):
        # GET mensagens/pilot
        # API destina à retornar mensagens PILOT das estações disponíveis no banco de dados da REDEMET.

        # Endereço de Acesso
        # https://api-redemet.decea.gov.br/mensagens/pilot

        # Parâmetros
        # Nome	Requerido	Descrição	Valor Padrão	Exemplo
        # estacao	Sim	Número sinótico da Estação.	Não há	83378
        # data_ini	Não	Data no formato YYYYMMDDHH	Data atual	2020051200
        # data_fim	Não	Data no formato YYYYMMDDHH	Data atual	2020051206
        # page_tam	Não	Número de registros por página	150	100
        # Exemplo de Solicitação
        # https://api-redemet.decea.gov.br/mensagens/pilot?api_key=SUA_CHAVE_AQUI&estacao=83378&data_ini=2020032912&data_fim=2020032912
        params = { 'api_key': self.api_key }

        params.update({'estacao': estacao})

        if data_ini is not None:
            if isinstance(data_ini, str):
                if len(data_ini) == 10 :
                    params.update({'data_ini': data_ini})
                else:
                    raise TypeError("Error: A data_ini informada não está no formato correto (YYYYMMDDHH) ")
            else:
                raise TypeError("Error: A data_ini não é uma string")
        
        if (data_fim is not None) and (data_ini is not None):
            if isinstance(data_fim, str) and isinstance(data_ini, str):
                if len(data_fim) == 10 and len(data_ini) == 10:
                    params.update({'data_fim': data_fim})
                else:
                    raise TypeError("Error: A data_fim ou data ini informadas não estão no formato correto (YYYYMMDDHH) ")
            else:
                raise TypeError("Error: A data_fim ou data ini não são strings")


        if page_tam is not None:
            params.update({'page_tam': page_tam})
        
        try:
            url = self.server_url + "/mensagens/pilot"
            response = requests.get(url, params=params)
        except Exception as ex:
            raise RuntimeError("Error: " + repr(ex))

        if response.status_code == 200:
            response = response.json() 
            if response['status'] == False:
                print('get_mensagens_pilot [!] HTTP status == False')
            if response['message'] != '':
                print('get_mensagens_pilot [!] HTTP message == ' + str(response['message']))
            return response['data']
        else:
            print('get_mensagens_pilot [!] HTTP {0} calling [{1}]'.format(response.status_code, response.request.url))
            return None 

    def get_mensagens_sigmet(self, pais, data_ini=None, data_fim=None, page_tam=None):
        # GET mensagens/sigmet
        # API destina à retornar mensagens SIGMET dos países disponíveis no banco de dados da REDEMET.

        # Endereço de Acesso
        # https://api-redemet.decea.gov.br/mensagens/sigmet

        # Parâmetros
        # Nome	Requerido	Descrição	Valor Padrão	Exemplo
        # pais	Sim	Nome do País	Brasil	Argentina
        # data_ini	Não	Data no formato YYYYMMDDHHII	Data atual	202005120000
        # data_fim	Não	Data no formato YYYYMMDDHHII	Data atual	202005120600
        # page_tam	Não	Número de registros por página	150	100
        # Exemplo de Solicitação
        # https://api-redemet.decea.gov.br/mensagens/sigmet/?api_key=SUA_CHAVE_AQUI&data_ini=202003291200&data_fim=202003291200
        params = { 'api_key': self.api_key }

        if isinstance(pais, str):
            params.update({'pais': pais})
        else:
            raise TypeError("Error: O pais não é uma string")

        if data_ini is not None:
            if isinstance(data_ini, str):
                if len(data_ini) == 12 :
                    params.update({'data_ini': data_ini})
                else:
                    raise TypeError("Error: A data_ini informada não está no formato correto (YYYYMMDDHHII) ")
            else:
                raise TypeError("Error: A data_ini não é uma string")
        
        if (data_fim is not None) and (data_ini is not None):
            if isinstance(data_fim, str) and isinstance(data_ini, str):
                if len(data_fim) == 12 and len(data_ini) == 12:
                    params.update({'data_fim': data_fim})
                else:
                    raise TypeError("Error: A data_fim ou data ini informadas não estão no formato correto (YYYYMMDDHHII) ")
            else:
                raise TypeError("Error: A data_fim ou data ini não são strings")


        if page_tam is not None:
            params.update({'page_tam': page_tam})
        
        try:
            url = self.server_url + "/mensagens/sigmet" 
            response = requests.get(url, params=params)
        except Exception as ex:
            raise RuntimeError("Error: " + repr(ex))

        if response.status_code == 200:
            response = response.json() 
            if response['status'] == False:
                print('get_mensagens_sigmet [!] HTTP status == False')
            if response['message'] != '':
                print('get_mensagens_sigmet [!] HTTP message == ' + str(response['message']))
            return response['data']
        else:
            print('get_mensagens_sigmet [!] HTTP {0} calling [{1}]'.format(response.status_code, response.request.url))
            return None 

    def get_mensagens_taf(self, localidades, data_ini=None, data_fim=None, page_tam=None, fim_linha=None):
        # GET mensagens/taf
        # API destina à retornar mensagens TAF das localidades disponíveis no banco de dados da REDEMET.
        # Há disponibilidade de mensagens desde 01/01/2003 até a presente data.

        # Endereço de Acesso
        # https://api-redemet.decea.gov.br/mensagens/taf/{localidades}

        # Parâmetros
        # Nome	Requerido	Descrição	Valor Padrão	Exemplo
        # localidades	Sim	Indicativo de localidade ICAO.
        # Quando precisar informar mais de uma localidade, basta informar separado por vírgula sem intervalo.	Não há	SBBR
        # data_ini	Não	Data no formato YYYYMMDDHH	Data atual	2020051200
        # data_fim	Não	Data no formato YYYYMMDDHH	Data atual	2020051206
        # page_tam	Não	Número de registros por página	150	100
        # fim_linha	Não	Utilizado para formatar o TAF
        # Valores possíveis:
        # texto: para a quebra de linha com “\n”
        # html: para a quebra de linha com “<br \>”
        # Não há	texto
        # Exemplo de Solicitação
        # https://api-redemet.decea.gov.br/mensagens/taf/SBBR,SBGL?api_key=SUA_CHAVE_AQUI&data_ini=2020031005&data_fim=2020031005&fim_linha=texto
        params = { 'api_key': self.api_key }

        if isinstance(localidades, str):
            check = len(localidades) - 4 # SBBR,SBCF ... [4],[4] -> 9 elementos: Possibilidades 4,9,14,18,24 (4)+(5)*(Numero adicional de localidades)
            if check % 5 == 0:
                localidades_url = localidades
            else:
                raise TypeError("Error: As localidades não estão no padrao correto [SBBR,SBCF,..]")
        else:
            raise TypeError("Error: A localidades não são uma string")

        if data_ini is not None:
            if isinstance(data_ini, str):
                if len(data_ini) == 10 :
                    params.update({'data_ini': data_ini})
                else:
                    raise TypeError("Error: A data_ini informada não está no formato correto (YYYYMMDDHH) ")
            else:
                raise TypeError("Error: A data_ini não é uma string")
        
        if (data_fim is not None) and (data_ini is not None):
            if isinstance(data_fim, str) and isinstance(data_ini, str):
                if len(data_fim) == 10 and len(data_ini) == 10:
                    params.update({'data_fim': data_fim})
                else:
                    raise TypeError("Error: A data_fim ou data ini informadas não estão no formato correto (YYYYMMDDHH) ")
            else:
                raise TypeError("Error: A data_fim ou data ini não são strings")


        if page_tam is not None:
            params.update({'page_tam': page_tam})

        if fim_linha is not None:
            if isinstance(fim_linha, str):
                if fim_linha in ['texto','html']:
                    params.update({'fim_linha': fim_linha})
                else:
                    raise TypeError("Error: O fim_linha informadas não está no formato correto (text ou html) ")
            else:
                raise TypeError("Error: O fim_linha não é strings")
        
        try:
            url = self.server_url + "/mensagens/taf/" + localidades_url
            response = requests.get(url, params=params)
        except Exception as ex:
            raise RuntimeError("Error: " + repr(ex))

        if response.status_code == 200:
            response = response.json() 
            if response['status'] == False:
                print('get_mensagens_taf [!] HTTP status == False')
            if response['message'] != '':
                print('get_mensagens_taf [!] HTTP message == ' + str(response['message']))
            return response['data']
        else:
            print('get_mensagens_taf [!] HTTP {0} calling [{1}]'.format(response.status_code, response.request.url))
            return None 
        
    def get_mensagens_temp(self, estacao, data_ini=None, data_fim=None, page_tam=None):
        # GET mensagens/temp
        # API destina à retornar mensagens TEMP das estações disponíveis no banco de dados da REDEMET.
        # Há disponibilidade de mensagens desde 01/01/2003 até a presente data.

        # Endereço de Acesso
        # https://api-redemet.decea.gov.br/mensagens/temp

        # Parâmetros
        # Nome	Requerido	Descrição	Valor Padrão	Exemplo
        # estacao	Sim	Número sinótico da Estação.
        # Permitido somente uma estação por solicitação	Não há	83378
        # data_ini	Não	Data no formato YYYYMMDDHH	Data atual	2020051200
        # data_fim	Não	Data no formato YYYYMMDDHH	Data atual	2020051206
        # page_tam	Não	Número de registros por página	150	100
        # Exemplo de Solicitação
        # https://api-redemet.decea.gov.br/mensagens/temp?api_key=SUA_CHAVE_AQUI&estacao=83378&data_ini=2020030912&data_fim=2020030912
        params = { 'api_key': self.api_key }

        params.update({'estacao': estacao})

        if data_ini is not None:
            if isinstance(data_ini, str):
                if len(data_ini) == 10 :
                    params.update({'data_ini': data_ini})
                else:
                    raise TypeError("Error: A data_ini informada não está no formato correto (YYYYMMDDHH) ")
            else:
                raise TypeError("Error: A data_ini não é uma string")
        
        if (data_fim is not None) and (data_ini is not None):
            if isinstance(data_fim, str) and isinstance(data_ini, str):
                if len(data_fim) == 10 and len(data_ini) == 10:
                    params.update({'data_fim': data_fim})
                else:
                    raise TypeError("Error: A data_fim ou data ini informadas não estão no formato correto (YYYYMMDDHH) ")
            else:
                raise TypeError("Error: A data_fim ou data ini não são strings")


        if page_tam is not None:
            params.update({'page_tam': page_tam})
        
        try:
            url = self.server_url + "/mensagens/temp"
            response = requests.get(url, params=params)
        except Exception as ex:
            raise RuntimeError("Error: " + repr(ex))

        if response.status_code == 200:
            response = response.json() 
            if response['status'] == False:
                print('get_mensagens_temp [!] HTTP status == False')
            if response['message'] != '':
                print('get_mensagens_temp [!] HTTP message == ' + str(response['message']))
            return response['data']
        else:
            print('get_mensagens_temp [!] HTTP {0} calling [{1}]'.format(response.status_code, response.request.url))
            return None 

if __name__ == '__main__':
    api_key = 'NniTZlc8mk00BhImNU0WH4173jo3j62YAh4CwAeW'
    redemet = pyredemet(api_key)
    #Aerodromos
    result = redemet.get_aerodromos(pais='Brasil')
    result = redemet.get_aerodromos_status(pais='Brasil')
    result = redemet.get_aerodromos_info(localidade='SBBR', metar='sim', taf='sim')
    #Produtos
    result = redemet.get_produtos_amdar(data='2020032415')
    result = redemet.get_produtos_modelo(modelo='wifs',area='b1',produto='vento-altitude-barb',nivel='600',anima=2)
    result = redemet.get_produto_radar(tipo='maxcappi',area='tm',data='2020032410',anima=2)
    result = redemet.get_produto_satelite(tipo='vis', data='2020032410', anima=2)
    result = redemet.get_produto_stsc(data='2020032410', anima=2)
    #Mensagens
    result = redemet.get_mensagens_aviso(localidades='SBBR,SBPA', data_ini='2020030912', data_fim='2020030912')
    result = redemet.get_mensagens_gamet(pais='Brasil', data_ini='202006120300',data_fim='202006120300')
    result = redemet.get_mensagens_metar(localidades='SBBR,SBPA', data_ini='2020030912',data_fim='2020030912')
    result = redemet.get_mensagens_meteograma(localidade='SBBR', data_hora='2020030912', horas=12)
    result = redemet.get_mensagens_pilot(estacao=83378,data_ini='2020030912',data_fim='2020030912')
    result = redemet.get_mensagens_sigmet(pais='Brasil', data_ini='202007071200',data_fim='202007071800')
    result = redemet.get_mensagens_taf(localidades='SBBR,SBPA', data_ini='2020030912',data_fim='2020030912', page_tam=100, fim_linha='texto')
    result = redemet.get_mensagens_temp(estacao=83378,data_ini='2020030912',data_fim='2020030912')
    print ("Done!")