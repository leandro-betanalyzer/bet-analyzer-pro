import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "data" / "bets.db"


def _connection():
    DB_PATH.parent.mkdir(exist_ok=True)
    return sqlite3.connect(DB_PATH)


def init_db():
    with _connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS bets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sport TEXT NOT NULL,
                bookmaker TEXT NOT NULL,
                event TEXT NOT NULL,
                market TEXT NOT NULL,
                odd REAL NOT NULL,
                stake REAL NOT NULL,
                result TEXT NOT NULL DEFAULT 'Pendente',
                profit REAL NOT NULL DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )


def add_bet(sport, bookmaker, event, market, odd, stake):
    with _connection() as conn:
        conn.execute(
            """
            INSERT INTO bets (sport, bookmaker, event, market, odd, stake)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (sport, bookmaker, event, market, float(odd), float(stake)),
        )


def get_bets():
    with _connection() as conn:
        rows = conn.execute(
            """
            SELECT id, sport, bookmaker, event, market, odd, stake, result, profit, created_at
            FROM bets ORDER BY id DESC
            """
        ).fetchall()

    return [
        {
            "ID": r[0],
            "Esporte": r[1],
            "Casa": r[2],
            "Evento": r[3],
            "Mercado": r[4],
            "Odd": r[5],
            "Valor": r[6],
            "Resultado": r[7],
            "Lucro/Prejuízo": r[8],
            "Data": r[9],
        }
        for r in rows
    ]


def settle_bet(bet_id: int, result: str):
    with _connection() as conn:
        odd, stake = conn.execute(
            "SELECT odd, stake FROM bets WHERE id = ?", (bet_id,)
        ).fetchone()

        if result == "Ganhou":
            profit = stake * (odd - 1)
        elif result == "Perdeu":
            profit = -stake
        else:
            profit = 0

        conn.execute(
            "UPDATE bets SET result = ?, profit = ? WHERE id = ?",
            (result, profit, bet_id),
        )


def get_dashboard_metrics():
    init_db()
    with _connection() as conn:
        total, settled, won, total_stake, profit = conn.execute(
            """
            SELECT
                COUNT(*),
                SUM(CASE WHEN result != 'Pendente' THEN 1 ELSE 0 END),
                SUM(CASE WHEN result = 'Ganhou' THEN 1 ELSE 0 END),
                SUM(CASE WHEN result != 'Pendente' THEN stake ELSE 0 END),
                SUM(profit)
            FROM bets
            """
        ).fetchone()

    total = total or 0
    settled = settled or 0
    won = won or 0
    total_stake = total_stake or 0
    profit = profit or 0

    return {
        "total": total,
        "hit_rate": (won / settled * 100) if settled else 0,
        "profit": profit,
        "roi": (profit / total_stake * 100) if total_stake else 0,
    }
