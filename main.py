import os
import importlib.util

def load_strategies(strategy_folder):
    strategies = []

    for filename in os.listdir(strategy_folder):
        if filename.endswith(".py"):
            module_name = filename[:-3]
            file_path = os.path.join(strategy_folder, filename)

            spec = importlib.util.spec_from_file_location(module_name, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            if hasattr(module, 'Strategy'):
                strategies.append(module.Strategy())

    return strategies

def evaluate_scores(moves):
    scores = {}
    
    for move in moves:
        for player in move:
            if player not in scores:
                scores[player] = 0
        
        player1, player2 = list(move.keys())
        move1, move2 = move[player1], move[player2]
        
        if move1 == 'split' and move2 == 'split':
            scores[player1] += 5
            scores[player2] += 5
        elif move1 == 'split' and move2 == 'steal':
            scores[player2] += 10
        elif move1 == 'steal' and move2 == 'split':
            scores[player1] += 10
        elif move1 == 'steal' and move2 == 'steal':
            scores[player1] += 3
            scores[player2] += 3
    
    return scores

if __name__ == "__main__":
    strategy_folder = 'strategies'
    strategies = load_strategies(strategy_folder)

    for index1, strategy1 in enumerate(strategies):
        for index2 in range(index1+1, len(strategies)):
            strategy2 = strategies[index2]
            name1 = strategy1.name
            name2 = strategy2.name
            
            start1 = strategy1.begin()
            start2 = strategy2.begin()
            history1 = [{ 'opponent': start2, 'you': start1 }]
            history2 = [{ 'opponent': start1, 'you': start2 }]
            
            for i in range(20000):
                move1 = strategy1.turn(history1)
                move2 = strategy2.turn(history2)
                history1.append({ 'opponent': move2, 'you': move1 })
                history2.append({ 'opponent': move1, 'you': move2 })

            compiled = []
    
            for i in history1:
                compiled.append(
                    {
                        name1: i.get('you'),
                        name2: i.get('opponent')
                    }
                )
            print(evaluate_scores(compiled))
            
