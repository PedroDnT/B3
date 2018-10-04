import pandas as pd


def parse_dataset(filepath):

    global df
    df = pd.DataFrame()  # Empty dataframe to fill; with file data.
    path = filepath
    wid_ref = [
        2, 8, 2, 12, 3, 12, 10, 3, 4, 13, 13, 13, 13, 13, 13, 13, 5, 18,
        18, 13, 1, 8, 7, 13, 12, 3]

    df = pd.read_fwf(path, widths=wid_ref, dtype=str, skiprows=1, skipfooter=1)

    df.columns = [
        'RecordType', 'Date', 'BDICode', 'Ticker', 'MarketType', 'FirmName',
        'Especs', 'DaysDue(fut)', 'Currency', 'OpenPrice', 'HighPrice',
        'LowPrice', 'AvgPrice', 'ClosePrice', 'BestBid', 'BestAsk', '#Trades',
        '#BondTrades', 'Volume', 'ExecutionPrice(Futures)', 'Adjust',
        'ExpiringDate', 'LoteSize', 'ExecutionPricePoints',
        'IsinCode', 'DistributionCode']
    df.Date = pd.to_datetime(df.Date)
    df['ExpiringDate'] = pd.to_datetime(df['ExpiringDate'], errors='coerce')
    df['ExecutionPrice(Futures)'] = pd.to_numeric(df['ExecutionPrice(Futures)'], errors='coerce')/ 100


    df.LoteSize = pd.to_numeric(df.LoteSize)
    df = df.drop(['ExecutionPricePoints'], axis=1)
    df = df.drop(['DistributionCode'], axis=1)

    df = translate_bdi(df)
    df = market_type(df)
    df = price_mod(df)
    df = set_numerics(df)

    return df

def translate_bdi(df):
    bdi = {
        '02': 'LOTE PADRAO',
        '05': 'SANCIONADAS PELOS REGULAMENTOS BMFBOVESPA',
        '06': 'CONCORDATARIAS',
        '07': 'RECUPERACAO EXTRAJUDICIAL',
        '08': 'RECUPERACAO JUDICIAL',
        '09': 'RAET - REGIME DE ADMINISTRACAO ESPECIAL TEMPORARIA',
        '10': 'DIREITOS E RECIBOS',
        '11': 'INTERVENCAO',
        '12': 'FUNDOS IMOBILIARIOS',
        '14': 'CERT.INVEST/TIT.DIV.PUBLICA',
        '18': 'OBRIGACOES',
        '22': 'BONUS (PRIVADOS)',
        '26': 'APOLICES/BONUS/TITULOS PUBLICOS',
        '32': 'EXERCICIO DE OPCOES DE COMPRA DE INDICES',
        '33': 'EXERCICIO DE OPCOES DE VENDA DE INDICES',
        '38': 'EXERCICIO DE OPCOES DE COMPRA',
        '42': 'EXERCICIO DE OPCOES DE VENDA',
        '46': 'LEILAO DE NAO COTADOS',
        '48': 'LEILAO DE PRIVATIZACAO',
        '49': 'LEILAO DO FUNDO RECUPERACAO ECONOMICA ESPIRITO SANTO',
        '50': 'LEILAO',
        '51': 'LEILAO FINOR',
        '52': 'LEILAO FINAM',
        '53': 'LEILAO FISET',
        '54': 'LEILAO DE ACÕES EM MORA',
        '56': 'VENDAS POR ALVARA JUDICIAL',
        '58': 'OUTROS',
        '60': 'PERMUTA POR ACÕES',
        '61': 'META',
        '62': 'MERCADO A TERMO',
        '66': 'DEBENTURES COM DATA DE VENCIMENTO ATE 3 ANOS',
        '68': 'DEBENTURES COM DATA DE VENCIMENTO MAIOR QUE 3 ANOS',
        '70': 'FUTURO COM RETENCAO DE GANHOS',
        '71': 'MERCADO DE FUTURO',
        '74': 'OPCOES DE COMPRA DE INDICES',
        '75': 'OPCOES DE VENDA DE INDICES',
        '78': 'OPCOES DE COMPRA',
        '82': 'OPCOES DE VENDA',
        '83': 'BOVESPAFIX',
        '84': 'SOMA FIX',
        '90': 'TERMO VISTA REGISTRADO',
        '96': 'MERCADO FRACIONARIO',
        '99': 'TOTAL GERAL'
    }

    df['BDICode'].replace(bdi, inplace=True)

    return df

def market_type(df):
    mkt = {
        '010': 'VISTA',
        '012': 'CALL EXERCISE',
        '013': 'PUT EXERCISE',
        '017': 'LEILAO',
        '020': 'FRACIONARIO',
        '030': 'TERMO',
        '050': 'FUTURO COM RETENCAO',
        '060': 'FUTURO CONTINUO',
        '070': 'CALL OPTION',
        '080': 'PUT OPTION'
    }

    df['MarketType'].replace(mkt, inplace=True)
    return df

def price_mod(df):
    """

    :type df: object

    """
    df.OpenPrice = pd.to_numeric(df.OpenPrice) / 100
    df.HighPrice = pd.to_numeric(df.HighPrice) / 100
    df.LowPrice = pd.to_numeric(df.LowPrice) / 100
    df.AvgPrice = pd.to_numeric(df.AvgPrice) / 100
    df.ClosePrice = pd.to_numeric(df.ClosePrice) / 100
    df.BestBid = pd.to_numeric(df.BestBid) / 100
    df.BestAsk = pd.to_numeric(df.BestAsk) / 100

    return df

def set_numerics(df):

    df['DaysDue(fut)'] = pd.to_numeric(df['DaysDue(fut)'], errors='coerce')
    df['#Trades'] = pd.to_numeric(df['#Trades'], errors='coerce')
    df['#BondTrades'] = pd.to_numeric(df['#BondTrades'], errors='coerce')
    df['Volume'] = pd.to_numeric(df['Volume']) / 100
    return df

