def step(self, action):
    try:
        # Take action of player and move him with something like move_player_to(x, y, vel(?), vel(?))
        self.GeoFriend2.make_move(x, y, vel(?), vel(?))

    except AssertionError:
        # The algorthim tried to move to somewhere not in the map, return reward -1 
        return self.tictactoe.board_state.flatten(), -1, True, {}

    reward = 0
    done = False

    # To determine our winner we have to have a list of objects (maybe) called rewards. Also, we want to have the
    # distance between the player and the rewards for this step and for the last step. Then, if its distance to 
    # the rewards in this step is fewer than the last step, we give it posite reward (maybe based on how much 
    # he came closer and then we normalize the vector of the distance differences). If he takes a reward we 
    # remove this reward from the list rewards_still_alive.   

    if len(rewards_still_alive) > 0:
        done = False
        reward = get_step_reward() 
    else:
        done = True
    
    return self.game, reward, done, {}
    # return self.tictactoe.board_state.flatten(), reward, done, {}


    our agent:
    Observation: 
        Type: Box(2)
        Num	Observation                 Min                  Max
        0	Circle Position             Left side            Right side
        1	Circle Velocity             -Inf                 Inf
        
    Action:
        Type: Discrete(4)
        Num	Action
        0	Push Circle to the left
        1	Push Circle to the right
        2	Push Circle to the top
        3	Push Circle to the bottom


FAZER A LOGICAS DO MAPA, MOVER PLAYER, ETC, NO GeoFriend2 E NAO NO GeoFriend2Env, que nem no tictactoe. A gente
nao precisa do PLAYER, nosso player é uma rede neural. A logica de definir o mapa e renderizar o mapa, o player, 
os pontos, etc, todas ficam no GeoFriend2. Ver tictactoe e cartpole.
Vamo comecar com o basico, com o mapa Basic, fazer ele pegar os pontos sem nenhum obstaculo, testar e depois 
implementar o obstaculo!

Ver como o action_space vai definir uma acao (exemplo, se ele definir que quer ir pra cima (2), a gente
tem que move pra cima) ver implementacao do amiguinho la
Talvez a gente nao queria o spin, so queremos que ela se mova na direcao escolhida

Decide ação ----> anda com o player ---> checa se pegou alguma reward
                                                |             |
                                                |             |
                                                |             | 
                                        Se pegou, r = 1     Se nao, r = 0