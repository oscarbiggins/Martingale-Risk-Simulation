import matplotlib.pyplot as plt
import random


class Gambler:
    
    def __init__(self, starting_wealth,goal):
        self.GOAL = goal
        self.BET_INCREMENT = 0
        self.STARTING_WEALTH = starting_wealth
        self.WIN_CHANCE = 0.5
        self.reset()
    
    def reset(self):
        self.money = self.STARTING_WEALTH
        self.bet_increase = self.BET_INCREMENT
        self.history = [self.money]
        self.bets = []
        
    def Betting_Simulation(self):
        while 0 < self.money < self.GOAL:
            self.current_bet = 2**self.bet_increase
            if self.current_bet > self.money:
                self.money = 0
                break
            if random.uniform(0,1) < 0.5 :
                self.money -= self.current_bet
                self.bet_increase += 1
            else:
                self.money += self.current_bet
                self.bet_increase = 0
            self.history.append(self.money)
            self.bets.append(self.current_bet)
        self.history.append(self.money)
        return self.history, self.bets
if __name__ == "__main__":
    STARTING_WEALTH = 100
    GOAL = 200
    TRIALS = 3
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=False)
    for _ in range(TRIALS):
        sim = Gambler(STARTING_WEALTH,GOAL)
        history, bets = sim.Betting_Simulation()
        
        ax1.plot(history, alpha = 0.7)
        ax2.plot(bets, alpha=0.7)
    ax1.set_title("Martingale Path:Total Money Over Time")
    ax1.axhline(y=0, color='r', linestyle='--')
    ax1.axhline(y=GOAL, color='g', linestyle='--')
    ax1.set_ylabel("Wealth (£)")

    ax2.set_title("Martingale Path:Bet Size Over Time")
    ax2.axhline(y=0, color='r', linestyle='--')
    ax2.set_ylabel("Bet Size (£)")
    ax2.set_xlabel("Round Number")
    ax2.set_yscale("log")
    plt.tight_layout()
    plt.show()
