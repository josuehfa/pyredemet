#!/usr/bin/ebv python
# coding=utf-8

""" 

Author = Josue H. F. Andrade        
License = MIT
Version = 1.0.1
Email = josuehfa@gmail.com
Status = Development

"""

import os
import sys
#import logging
import unittest
sys.path.insert(0, os.path.abspath(".."))
from pyredemet.src.pyredemet import pyredemet

class test_pyredemet(unittest.TestCase):

    def test_init(self):
        api_key = "banana"
        with self.assertRaises(TypeError):
            result = pyredemet(api_key=api_key)
        
        server_url = 123
        with self.assertRaises(TypeError):
            result = pyredemet(api_key='NniTZlc8mk00BhImNU0WH4173jo3j62YAh4CwAeW', server_url=server_url)


    def setUp(self):
        self.redemet = pyredemet(api_key = 'NniTZlc8mk00BhImNU0WH4173jo3j62YAh4CwAeW')


    def test_get_aerodromos(self):
        #API destina à retornar informações de Aeródromos de países disponíveis no banco de dados da REDEMET.
        #https://api-redemet.decea.gov.br/aerodromos
        #Parâmetros
        #    Nome	Requerido	Descrição	Valor Padrão	Exemplo
        #    pais	Não	Nome do país.	Brasil	Argentina
        #Exemplo de Solicitação
        #    https://api-redemet.decea.gov.br/aerodromos?api_key=SUA_CHAVE_AQUI&pais=Argentina
        pais = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_aerodromos(pais=pais)


    def test_get_aerodromos_status(self):
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
        pais = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_aerodromos_status(pais=pais)


    def test_get_aerodromos_info(self):
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
        localidade = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_aerodromos_info(localidade=localidade)
        localidade = 'SBB'
        with self.assertRaises(TypeError):
            result = self.redemet.get_aerodromos_info(localidade=localidade)

        localidade = 'SBBR'
        metar = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_aerodromos_info(localidade=localidade,metar=metar)

        taf = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_aerodromos_info(localidade=localidade,taf=taf)

        datahora = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_aerodromos_info(localidade=localidade,datahora=datahora)
        datahora = '123'
        with self.assertRaises(TypeError):
            result = self.redemet.get_aerodromos_info(localidade=localidade,datahora=datahora)


    def test_get_produtos_amdar(self):
        # GET produtos/amdar
        # API destina à retornar informações do AMDAR

        # Endereço de Acesso
        # https://api-redemet.decea.gov.br/produtos/amdar

        # Parâmetros
        # Nome	Requerido	Descrição	Valor Padrão	Exemplo
        # data	Não	Data no formato YYYYMMDDHH	Data atual	2020051200
        # Exemplo de Solicitação
        # https://api-redemet.decea.gov.br/produtos/amdar?api_key=SUA_CHAVE_AQUI&data_ini=2020030313&data=2020032415
        data = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_produtos_amdar(data=data)
        data = 'SBB'
        with self.assertRaises(TypeError):
            result = self.redemet.get_produtos_amdar(data=data)


    def test_get_produtos_modelo(self):
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
        modelo = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_produtos_modelo(modelo=modelo)
        
        modelo = 'wifs'
        produto = 'incldturb'
        nivel = '850'

        area = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_produtos_modelo(modelo=modelo,area=area,produto=produto,nivel=nivel)
        area = 'ab'
        with self.assertRaises(TypeError):
            result = self.redemet.get_produtos_modelo(modelo=modelo,area=area,produto=produto,nivel=nivel)

        modelo = 'wifs'
        nivel = '850'
        area = 'as'

        produto = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_produtos_modelo(modelo=modelo,area=area,produto=produto,nivel=nivel)
        produto = 'abc'
        with self.assertRaises(TypeError):
            result = self.redemet.get_produtos_modelo(modelo=modelo,area=area,produto=produto,nivel=nivel)

        modelo = 'wifs'
        produto = 'incldturb'
        area = 'as'

        nivel = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_produtos_modelo(modelo=modelo,area=area,produto=produto,nivel=nivel)
        nivel = 'abc'
        with self.assertRaises(TypeError):
            result = self.redemet.get_produtos_modelo(modelo=modelo,area=area,produto=produto,nivel=nivel)

        modelo = 'wifs'
        produto = 'incldturb'
        nivel = '850'
        area = 'as'

        anima = '123'
        with self.assertRaises(TypeError):
            result = self.redemet.get_produtos_modelo(modelo=modelo,area=area,produto=produto,nivel=nivel,anima=anima)
        anima = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_produtos_modelo(modelo=modelo,area=area,produto=produto,nivel=nivel,anima=anima)

    def test_get_produto_radar(self):
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
        area='al'

        tipo = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_produto_radar(tipo=tipo,area=area)
        tipo = 'ab'
        with self.assertRaises(TypeError):
            result = self.redemet.get_produto_radar(tipo=tipo,area=area)

        tipo='maxcappi'

        area = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_produto_radar(tipo=tipo,area=area)
        area = 'abc'
        with self.assertRaises(TypeError):
            result = self.redemet.get_produto_radar(tipo=tipo,area=area)

        area='al'
        tipo='maxcappi'

        data = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_produto_radar(tipo=tipo,area=area,data=data)
        data = 'abc'
        with self.assertRaises(TypeError):
            result = self.redemet.get_produto_radar(tipo=tipo,area=area,data=data)

        area='al'
        tipo='maxcappi'

        anima = '123'
        with self.assertRaises(TypeError):
            result = self.redemet.get_produto_radar(tipo=tipo,area=area,anima=anima)
        anima = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_produto_radar(tipo=tipo,area=area,anima=anima)

    def test_get_produto_satelite(self):
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
        
        tipo = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_produto_satelite(tipo=tipo)
        tipo = 'ab'
        with self.assertRaises(TypeError):
            result = self.redemet.get_produto_satelite(tipo=tipo)

        tipo='realcada'

        data = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_produto_satelite(tipo=tipo,data=data)
        data = 'abc'
        with self.assertRaises(TypeError):
            result = self.redemet.get_produto_satelite(tipo=tipo,data=data)

        tipo='realcada'

        anima = '123'
        with self.assertRaises(TypeError):
            result = self.redemet.get_produto_satelite(tipo=tipo,anima=anima)
        anima = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_produto_satelite(tipo=tipo,anima=anima)

    def test_get_produto_stsc(self):
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
        data = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_produto_stsc(data=data)
        data = 'abc'
        with self.assertRaises(TypeError):
            result = self.redemet.get_produto_stsc(data=data)

        tipo='realcada'

        anima = '123'
        with self.assertRaises(TypeError):
            result = self.redemet.get_produto_stsc(anima=anima)
        anima = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_produto_stsc(anima=anima)


    def test_get_mensagens_aviso(self):
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
        
        localidades = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_aviso(localidades=localidades)
        
        localidades = 'SBBR, SBCF'
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_aviso(localidades=localidades)

        localidades = 'SBBR,SBCF'

        data_ini = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_aviso(localidades=localidades,data_ini=data_ini)
        data_ini = 'abc'
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_aviso(localidades=localidades,data_ini=data_ini)

        data_fim = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_aviso(localidades=localidades,data_fim=data_fim)
        data_fim = 'abc'
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_aviso(localidades=localidades,data_fim=data_fim)

    def test_get_mensagens_gamet(self):
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
        pais = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_gamet(pais=pais)

        pais = 'Brasil'

        data_ini = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_gamet(pais=pais,data_ini=data_ini)
        data_ini = 'abc'
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_gamet(pais=pais,data_ini=data_ini)

        data_fim = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_gamet(pais=pais,data_fim=data_fim)
        data_fim = 'abc'
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_gamet(pais=pais,data_fim=data_fim)

    def test_get_mensagens_metar(self):
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
        localidades = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_metar(localidades=localidades)
        
        localidades = 'SBBR, SBCF'
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_metar(localidades=localidades)

        localidades = 'SBBR,SBCF'

        data_ini = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_metar(localidades=localidades,data_ini=data_ini)
        data_ini = 'abc'
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_metar(localidades=localidades,data_ini=data_ini)

        data_ini = '2020050512'
        data_fim = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_metar(localidades=localidades,data_ini=data_ini,data_fim=data_fim)
        data_fim = 'abc'
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_metar(localidades=localidades,data_ini=data_ini,data_fim=data_fim)

    def test_get_mensagens_meteograma(self):
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
        
        localidade = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_meteograma(localidade=localidade)
        
        localidade = 'SBBR, SBCF'
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_meteograma(localidade=localidade)

        localidade = 'SBBR'

        data_hora = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_meteograma(localidade=localidade,data_hora=data_hora)
        data_hora = 'abc'
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_meteograma(localidade=localidade,data_hora=data_hora)


    def test_get_mensagens_pilot(self):
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
        estacao = 83378
        data_ini = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_pilot(estacao=estacao,data_ini=data_ini)
        data_ini = 'abc'
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_pilot(estacao=estacao,data_ini=data_ini)

        data_ini = '2020050512'
        data_fim = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_pilot(estacao=estacao,data_ini=data_ini,data_fim=data_fim)
        data_fim = 'abc'
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_pilot(estacao=estacao,data_ini=data_ini,data_fim=data_fim)

    def test_get_mensagens_sigmet(self):
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
        pais = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_sigmet(pais=pais)

        pais = 'Brasil'

        data_ini = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_sigmet(pais=pais,data_ini=data_ini)
        data_ini = 'abc'
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_sigmet(pais=pais,data_ini=data_ini)

        data_ini = '2020050512'
        data_fim = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_sigmet(pais=pais,data_ini=data_ini,data_fim=data_fim)
        data_fim = 'abc'
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_sigmet(pais=pais,data_ini=data_ini,data_fim=data_fim)

    def test_get_mensagens_taf(self):
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
        localidades = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_taf(localidades=localidades)
        
        localidades = 'SBBR, SBCF'
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_taf(localidades=localidades)

        localidades = 'SBBR,SBCF'

        data_ini = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_taf(localidades=localidades,data_ini=data_ini)
        data_ini = 'abc'
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_taf(localidades=localidades,data_ini=data_ini)

        data_ini = '2020050512'
        data_fim = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_taf(localidades=localidades,data_ini=data_ini,data_fim=data_fim)
        data_fim = 'abc'
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_taf(localidades=localidades,data_ini=data_ini,data_fim=data_fim)

        fim_linha = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_taf(localidades=localidades,fim_linha=fim_linha)
        fim_linha = 'abc'
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_taf(localidades=localidades,fim_linha=fim_linha)

    def test_get_mensagens_temp(self):
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
        estacao = 83378
        data_ini = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_temp(estacao=estacao,data_ini=data_ini)
        data_ini = 'abc'
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_temp(estacao=estacao,data_ini=data_ini)

        data_ini = '2020050512'
        data_fim = 123
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_temp(estacao=estacao,data_ini=data_ini,data_fim=data_fim)
        data_fim = 'abc'
        with self.assertRaises(TypeError):
            result = self.redemet.get_mensagens_temp(estacao=estacao,data_ini=data_ini,data_fim=data_fim)
    
