#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
import os
import csv
import json
import requests
from bs4 import BeautifulSoup

URL_BASE = 'https://opcoes.net.br/opcoes/bovespa/'
BASE_DIR = os.getcwd()

LIST_MENU_BA = ['BBAS3', 'BBDC3', 'BBDC4', 'BBTG11', 'BRSR6', 'ITSA4', 'ITUB3', 'ITUB4', 'SANB11']

LIST_MENU_ML = ['ABEV3', 'AZUL4', 'B3SA3', 'BBAS3', 'BBDC3', 'BBDC4', 'BBSE3', 'BOVA11', 'BRAP4', 'BRFS3', 'BRKM5', 'BRML3',
                'BTOW3', 'CIEL3', 'CMIG4', 'COGN3', 'CSAN3', 'CSNA3', 'CYRE3', 'ELET3', 'ELET6', 'EMBR3', 'EQTL3', 'GGBR4',
                'GOAU4', 'HYPE3', 'IRBR3', 'ITSA4', 'ITUB4', 'JBSS3', 'LAME4', 'LREN3', 'MGLU3', 'MRFG3', 'PCAR3', 'PETR3',
                'PETR4', 'RADL3', 'RAIL3', 'SANB11', 'SBSP3', 'SUZB3', 'TAEE11', 'USIM5', 'VALE3', 'VIVT4', 'VVAR3', 'WEGE3', 'YDUQ3'
                ]

LIST_MENU_PV = ['PETR3', 'PETR4', 'VALE3', 'VALE5']

LIST_MENU_PO = ['ABEV3', 'AZUL4', 'B3SA3', 'BBAS3', 'BBDC3', 'BBDC4', 'BBSE3', 'BEEF3', 'BOVA11', 'BRAP4', 'BRDT3', 'BRFS3',
                'BRKM5', 'BRML3', 'BRSR6', 'BTOW3', 'CCRO3', 'CIEL3', 'CMIG4', 'COGN3', 'CSAN3', 'CSNA3', 'CVCB3', 'CYRE3',
                'ECOR3', 'EGIE3', 'ELET3', 'ELET6', 'EMBR3', 'ENAT3', 'ENBR3', 'EQTL3', 'FLRY3', 'GFSA3', 'GGBR4', 'GOAU4',
                'GOLL4', 'HYPE3', 'IRBR3', 'ITSA4', 'ITUB4', 'JBSS3', 'JHSF3', 'KLBN11', 'LAME4', 'LREN3', 'MEAL3', 'MGLU3',
                'MRFG3', 'MRVE3', 'MULT3', 'NEOE3', 'PCAR3', 'PETR3', 'PETR4', 'POMO4', 'PRIO3', 'RADL3', 'RAIL3', 'SANB11',
                'SBSP3', 'SMLS3', 'SUZB3', 'TAEE11', 'TIET11', 'TIMS3', 'UGPA3', 'USIM5', 'VALE3', 'VIVT4', 'VLID3', 'VVAR3',
                'WEGE3', 'YDUQ3'
                ]

LIST_MENU_TA = ['ABEV3', 'ALPA4', 'ALSO3', 'ALUP11', 'ARZZ3', 'AZUL4', 'B3SA3', 'BBAS3', 'BBDC3', 'BBDC4', 'BBSE3', 'BEEF3', 'BKBR3', 'BOVA11',
                'BOVV11', 'BPAC11', 'BPAN4', 'BRAP4', 'BRDT3', 'BRFS3', 'BRKM5', 'BRML3', 'BRSR6', 'BTOW3', 'CCRO3', 'CESP6', 'CIEL3', 'CMIG4',
                'COGN3', 'CPFE3', 'CPLE6', 'CRFB3', 'CSAN3', 'CSMG3', 'CSNA3', 'CVCB3', 'CYRE3', 'DIRR3', 'DTEX3', 'ECOR3', 'EGIE3', 'ELET3', 'ELET6',
                'EMBR3', 'ENAT3', 'ENBR3', 'ENEV3', 'ENGI11', 'EQTL3', 'EVEN3', 'EZTC3', 'FLRY3', 'GFSA3', 'GGBR4', 'GNDI3', 'GOAU4', 'GOLL4', 'GRND3',
                'HAPV3', 'HBOR3', 'HGTX3', 'HYPE3', 'IBOV11', 'IGTA3', 'IRBR3', 'ITSA4', 'ITUB3', 'ITUB4', 'IVVB11', 'JBSS3', 'JHSF3', 'KLBN11',
                'LAME3', 'LAME4', 'LCAM3', 'LIGT3', 'LINX3', 'LOGN3', 'LREN3', 'LWSA3', 'MDIA3', 'MEAL3', 'MGLU3', 'MOVI3', 'MRFG3', 'MRVE3',
                'MULT3', 'MYPK3', 'NEOE3', 'NTCO3', 'ODPV3', 'PCAR3', 'PCAR4', 'PETR3', 'PETR4', 'POMO4', 'PRIO3', 'PSSA3', 'QUAL3', 'RADL3',
                'RAIL3', 'RAPT4', 'RENT3', 'SANB11', 'SAPR11', 'SBSP3', 'SEER3', 'SMAL11', 'SMLS3', 'SMTO3', 'STBP3', 'SULA11', 'SUZB3', 'TAEE11',
                'TIET11', 'TIMP3', 'TIMS3', 'TOTS3', 'TRPL4', 'TUPY3', 'UGPA3', 'USIM5', 'VALE3', 'VIVT4', 'VLID3', 'VVAR3', 'WEGE3', 'YDUQ3'
                ]


class Browser(object):

    def __init__(self):
        """
        Inicia o objeto...
        """
        self.response = None
        self.session = requests.Session()
        self.soup_parser = {'features': 'html5lib'}

    def headers(self):
        """
        Obtem o cabeçalho inicial da requisição.
        :return:
        """
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0)'
                          ' Gecko/20100101 Firefox/72.0',
        }
        return headers

    def send_request(self, url, method, soup_cnf, **kwargs):
        """
        Envia a requisição GET salvando a sessão para consulta posterior.
        Retorna com as informações da consulta e o código fonte da página.
        :param url:
        :param method:
        :param kwargs:
        :return:
        """
        try:
            response = self.session.request(method, url, **kwargs)
        except ValueError:
            return None
        if response.status_code == 200:
