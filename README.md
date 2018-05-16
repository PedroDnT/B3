# B3 File Parser

A function that reads and formats Bovespa/B3's historical data downloaded from their website. The website is currently the only free source of financial data due to depreciation of yahoo finance and google finance API
to extract informations. 

Files Download: [BMFBOV - COTACOES HISTORICAS](http://www.bmfbovespa.com.br/pt_br/servicos/market-data/historico/mercado-a-vista/cotacoes-historicas/)

### Usage
To import:
```
from B3 import *
```
To parse data:
```
x = parse_dataset( filepath )  # Loads dataset into pandas dataframe
translate_bdi(x)  # Translates BDI Codes and returns pandas df mofied
market_type(x)  # Translates market_types Codes and returns pandas df mofied
price_mod(x)  # Returns price fields formated as currency
```

## Authors

* **Pedro Todescan** - *GitHub Profile* - [PedroDnT](https://github.com/PedroDnT)


## License

This project is licensed under the Apache License 2.0 - see the [LICENSE.md](LICENSE.md) file for details
