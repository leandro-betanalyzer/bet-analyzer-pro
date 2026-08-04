from statistics import mean


def _parse_numbers(text: str) -> list[float]:
    values = []
    for item in text.replace(";", ",").split(","):
        item = item.strip()
        if not item:
            continue
        try:
            values.append(float(item.replace(",", ".")))
        except ValueError as exc:
            raise ValueError(f'Valor inválido: "{item}"') from exc
    if not values:
        raise ValueError("Informe ao menos um valor.")
    return values


def _rate(values: list[float], threshold: float) -> float:
    return sum(v > threshold for v in values) / len(values) * 100


def football_analysis(goals_text, corners_text, cards_text, ht_text):
    goals = _parse_numbers(goals_text)
    corners = _parse_numbers(corners_text)
    cards = _parse_numbers(cards_text)
    ht = _parse_numbers(ht_text)

    markets = {
        "Over 1.5 gols": _rate(goals, 1.5),
        "Over 2.5 gols": _rate(goals, 2.5),
        "Gol no 1º tempo": _rate(ht, 0.5),
        "Over 8.5 escanteios": _rate(corners, 8.5),
        "Over 3.5 cartões": _rate(cards, 3.5),
    }

    best_market = max(markets, key=markets.get)
    best_rate = markets[best_market]

    return {
        "over_15": markets["Over 1.5 gols"],
        "over_25": markets["Over 2.5 gols"],
        "over_05_ht": markets["Gol no 1º tempo"],
        "over_85_corners": markets["Over 8.5 escanteios"],
        "avg_goals": mean(goals),
        "avg_corners": mean(corners),
        "avg_cards": mean(cards),
        "best_market": f"{best_market} — frequência de {best_rate:.0f}%",
        "explanation": (
            f'Na amostra informada, o mercado "{best_market}" foi o mais frequente. '
            f'A média foi de {mean(goals):.2f} gols, {mean(corners):.2f} escanteios '
            f'e {mean(cards):.2f} cartões por partida. Confira contexto, escalações '
            f'e odd antes de decidir.'
        ),
    }


def basketball_analysis(values_text: str, line: float, odd: float):
    values = _parse_numbers(values_text)
    over_rate = _rate(values, line)
    under_rate = 100 - over_rate

    recommendation = "OVER" if over_rate >= under_rate else "UNDER"
    selected_probability = max(over_rate, under_rate) / 100
    fair_odd = 1 / selected_probability if selected_probability > 0 else 99
    implied_probability = 1 / odd
    edge = (selected_probability - implied_probability) * 100

    return {
        "average": mean(values),
        "over_rate": over_rate,
        "fair_odd": fair_odd,
        "edge": edge,
        "recommendation": recommendation,
        "explanation": (
            f'O jogador teve média de {mean(values):.2f} na amostra. '
            f'Ele ficou acima da linha em {over_rate:.0f}% dos jogos. '
            f'A odd informada implica aproximadamente {implied_probability*100:.1f}% '
            f'de probabilidade. O valor estimado é apenas matemático e depende da '
            f'qualidade da amostra.'
        ),
    }
