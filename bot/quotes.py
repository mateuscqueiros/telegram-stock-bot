from dataclasses import dataclass

import httpx

from bot.config import BRAPI_TOKEN

BRAPI_BASE_URL = "https://brapi.dev/api/quote"


@dataclass
class Quote:
    ticker: str
    name: str
    price: float
    change_percent: float


class QuoteError(Exception):
    pass


def _headers() -> dict[str, str]:
    if BRAPI_TOKEN:
        return {"Authorization": f"Bearer {BRAPI_TOKEN}"}
    return {}


async def get_quote(ticker: str) -> Quote:
    normalized = ticker.strip().upper()
    if not normalized:
        raise QuoteError("Informe um ticker. Exemplo: /cotacao PETR4")

    url = f"{BRAPI_BASE_URL}/{normalized}"

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(url, headers=_headers())
    except httpx.RequestError as exc:
        raise QuoteError("Não foi possível consultar a API. Tente novamente.") from exc

    if response.status_code == 401:
        raise QuoteError(
            f"Ticker '{normalized}' exige token da brapi.dev. "
            "Adicione BRAPI_TOKEN no .env (cadastro gratuito em brapi.dev). "
            "Sem token, use: PETR4, VALE3, MGLU3 ou ITUB4."
        )

    if response.status_code == 404:
        raise QuoteError(f"Ticker '{normalized}' não encontrado na B3.")

    if response.status_code != 200:
        raise QuoteError("A API retornou um erro. Tente novamente em instantes.")

    data = response.json()
    results = data.get("results") or []
    if not results:
        raise QuoteError(f"Ticker '{normalized}' não encontrado na B3.")

    item = results[0]
    price = item.get("regularMarketPrice")
    if price is None:
        raise QuoteError(f"Cotação indisponível para '{normalized}'.")

    return Quote(
        ticker=normalized,
        name=item.get("shortName") or normalized,
        price=float(price),
        change_percent=float(item.get("regularMarketChangePercent") or 0.0),
    )


def format_price(value: float) -> str:
    return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def format_change_percent(value: float) -> str:
    sign = "+" if value >= 0 else ""
    return f"{sign}{value:.2f}%".replace(".", ",")
