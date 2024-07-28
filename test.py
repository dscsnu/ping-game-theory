import os
import time
import random
import importlib.util
from pathlib import Path
from typing import List, Tuple, Any
from tqdm import tqdm

from utils.types import Move, Strategy, History, HistoryEntry

def load_strategy(filename: str) -> Any:
    strategies_path = Path("./strategies")
    file_path = strategies_path / filename
    spec = importlib.util.spec_from_file_location(filename[:-3], file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if hasattr(module, "Strategy"):
        return getattr(module, "Strategy")
    raise AttributeError("Strategy class not found in the module")

class RandomStrategy(Strategy):
    def __init__(self) -> None:
        self.name = "RandomStrategy"

    def begin(self) -> Move:
        return random.choice(list(Move))

    def turn(self, history: History) -> Move:
        return random.choice(list(Move))

def run_dilemma(strategy1: Strategy, strategy2: Strategy, num_rounds: int) -> Tuple[int, int]:
    history1: List[HistoryEntry] = []
    history2: List[HistoryEntry] = []
    score1: int = 0
    score2: int = 0

    start_time = time.time()

    with tqdm(total=num_rounds, desc="Running dilemma", unit="round", bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} [{rate_fmt}{postfix}]') as pbar:
        for i in range(num_rounds):
            if i == 0:
                move1 = strategy1.begin()
                move2 = strategy2.begin()
            else:
                move1 = strategy1.turn(tuple(history1))
                move2 = strategy2.turn(tuple(history2))

            if not isinstance(move1, Move) or not isinstance(move2, Move):
                raise TypeError(f"Invalid move type. Expected Move, got {type(move1)}")

            history1.append(HistoryEntry(opponent=move2, you=move1))
            history2.append(HistoryEntry(opponent=move1, you=move2))

            pbar.update(1)
            elapsed_time = time.time() - start_time
            pbar.set_postfix({'Time': f'{elapsed_time:.2f}s'})

    return score1, score2

def main() -> None:
    num_rounds: int = 50000
    timeout: int = 60

    try:
        strategy_file = next(file for file in os.listdir("./strategies") if file.endswith(".py") and file != "__init__.py")
        StrategyClass = load_strategy(strategy_file)
        
        test_strategy = StrategyClass()
        random_strategy = RandomStrategy()

        start_time = time.time()
        
        run_dilemma(test_strategy, random_strategy, num_rounds)
        
        end_time = time.time()
        total_time = end_time - start_time

        if total_time > timeout:
            print(f"\nTest failed: Execution time ({total_time:.2f} seconds) exceeded the 30-minute limit.")
        else:
            print(f"\nTest passed: Execution completed in {total_time:.2f} seconds.")

    except Exception as e:
        print(f"\nError occurred during test execution: {str(e)}")

if __name__ == "__main__":
    main()