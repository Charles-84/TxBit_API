⚠️ AVERTISSEMENT ⚠️

Le site web de Txbit a été définitivement fermé le 14 septembre. Ce dépôt est conservé à des fins d'archive et n'est plus fonctionnel avec l'API de Txbit, étant donné que le service n'est plus disponible.

# TxbitAPI

Une bibliothèque Python pour interagir avec l'API de Txbit.

## Caractéristiques

- Interface simple pour les requêtes publiques et privées
- Gestion de la signature HMAC pour l'authentification
- Méthodes pour toutes les principales fonctions de l'API Txbit

## Dépendances

- `requests`
- `hmac`
- `hashlib`
- `time`

## Utilisation

### Initialisation

Pour utiliser l'API, initialisez d'abord l'objet `TxbitAPI` avec votre clé API et votre secret API :

```python
api = TxbitAPI(api_key="YOUR_API_KEY", api_secret="YOUR_API_SECRET")
```

### Méthodes Publiques

- `get_markets()`
- `get_currencies()`
- `get_ticker(market: str)`
- `get_market_summaries()`
- `get_market_summary(market: str)`
- `get_orderbook(market: str, type_: str='both')`
- `get_market_history(market: str)`

### Méthodes Privées

- `buy_limit(market: str, quantity: float, rate: float)`
- `sell_limit(market: str, quantity: float, rate: float)`
- `cancel_order(uuid: str)`
- `get_open_orders(market: Optional[str]=None)`
- `get_balances()`
- `get_balance(currency: str)`

## Exemple

```python
api = TxbitAPI(api_key="YOUR_API_KEY", api_secret="YOUR_API_SECRET")
markets = api.get_markets()
print(markets)
```

## Notes

N'oubliez pas de ne jamais exposer votre clé API et votre secret API dans votre code ou sur des plateformes publiques.
