# PyRedeMet
A Python interface to API-RedeMet (https://ajuda.decea.gov.br/artigo-categoria/redemet/).

A API da REDEMET é um produto de interfaces de programação de aplicativos(APIs), que irá proporcionar acesso a vários produtos meteorológicos, hoje disponibilizados no site da REDEMET, de modo rápido e seguro para serem utilizados em diversos fins.

## Produtos disponíveis
Para a obtenção de cada produto há uma sintase própria de solicitação que pode ser conferida na lista abaixo:

* Aeródromos
* Aeródromos Status
* Aeródromos Info
* Produtos AMDAR
* Produtos MODELO
* Produtos RADAR
* Produtos SATÉLITE
* Produtos STSC
* Mensagem Aviso de Aeródromo
* Mensagem GAMET
* Mensagem METAR
* Mensagem Meteograma
* Mensagem PILOT
* Mensagem SIGMET
* Mensagem TAF
* Mensagem TEMP

## Mode de utilização:

`import pyredemet`
 
`redemet = pyredemet(api="SUA_API_KEY")`

`response = redemet.get_aerodromos(pais=Brasil)`
