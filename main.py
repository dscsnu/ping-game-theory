import os
import importlib.util
from pathlib import Path
from typing import List, Tuple
import pandas as pd
from itertools import combinations_with_replacement
import matplotlib.pyplot as plt

from utils.types import Strategy, HistoryEntry, Move


def load_strategies() -> List[Strategy]:
    strategies: List[Strategy] = []
    strategies_path = Path("./strategies")

    for filename in os.listdir(strategies_path):
        if filename.endswith(".py"):
            module_name = filename[:-3]
            file_path = strategies_path / filename

            spec = importlib.util.spec_from_file_location(module_name, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            if hasattr(module, "Strategy"):
                strategy_class: type = getattr(module, "Strategy")
                strategies.append(strategy_class())

    return strategies


def evaluate_score(move1: Move, move2: Move) -> Tuple[int, int]:
    if move1 == Move.SPLIT and move2 == Move.SPLIT:
        return (5, 5)
    elif move1 == Move.SPLIT and move2 == Move.STEAL:
        return (0, 10)
    elif move1 == Move.STEAL and move2 == Move.SPLIT:
        return (10, 0)
    else:
        return (3, 3)


def dillema(
    strategy1: Strategy, strategy2: Strategy, num_rounds: int = 100
) -> Tuple[int, int]:
    history1: List[HistoryEntry] = []
    history2: List[HistoryEntry] = []
    score1: int = 0
    score2: int = 0

    for _ in range(num_rounds):
        if _ == 0:
            move1 = strategy1.begin()
            move2 = strategy2.begin()
        else:
            move1 = strategy1.turn(tuple(history1))
            move2 = strategy2.turn(tuple(history2))

        history1.append(HistoryEntry(opponent=move2, you=move1))
        history2.append(HistoryEntry(opponent=move1, you=move2))

        round_score1, round_score2 = evaluate_score(move1, move2)
        score1 += round_score1
        score2 += round_score2

    return (score1, score2)


if __name__ == "__main__":
    num_rounds = 10000
    strategies = load_strategies()

    df = pd.DataFrame(
        index=[s.name for s in strategies], columns=[s.name for s in strategies]
    )

    for strategy1, strategy2 in combinations_with_replacement(strategies, 2):
        score1, score2 = dillema(strategy1, strategy2, num_rounds)
        df.at[strategy1.name, strategy2.name] = score1
        df.at[strategy2.name, strategy1.name] = score2

    for strategy in strategies:
        score1, _ = dillema(strategy, strategy, num_rounds)
        df.at[strategy.name, strategy.name] = score1

    print(f"Number of rounds: {num_rounds}")

    total_scores = df.sum(axis=1)
    df["Total"] = total_scores

    print(df)
    print("\nTotal scores:")
    print(total_scores.sort_values(ascending=False))

    fig, ax = plt.subplots(figsize=(12, 10))

    ax.axis("off")

    table = ax.table(
        cellText=df.values,
        rowLabels=df.index,
        colLabels=df.columns,
        cellLoc="center",
        loc="center",
    )

    table.auto_set_font_size(False)
    table.set_fontsize(9)

    table.scale(1, 1.5)

    plt.title(f"Dilema Results (Number of rounds: {num_rounds})")
    plt.tight_layout()
    plt.savefig("results.png", dpi=300, bbox_inches="tight")
    plt.close()
