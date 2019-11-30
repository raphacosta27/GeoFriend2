
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

Para aprender a pegar a reward, a reward deveria estar no obeservation_space tb, nao?