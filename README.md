# Geometry Friends environment using OpenAI Gym

The purpose of this project was to develop an OpenAI Gym environment with a simplified version of Geometry Friends game.

### Prerequisites

1) This project was developed using the following: <br/>
    Ubuntu 16 or higher </br>
    python 3.7.5: https://www.python.org/downloads/release/python-375/

2) Install pip for the version of this python. In ubuntu:
    ```
    sudo apt-get install python3-pip
    ```

3) Next, install the other libraries needed for this project:
    ```
    pip3 install keras==2.2.4
    pip3 install keras-rl==0.4.2
    pip3 install tensorflow==1.13.1
    pip3 install gym==0.12.1
    pip3 install h5py==2.9.0
    pip3 install pygame
    ```

4) Install the Spinning Up library following their site instructions:
    https://spinningup.openai.com/en/latest/user/installation.html

5) Finally, make sure that you are in the main directory of the project and run:
    ```
    pip3 install -e .
    ```

6) The trainment for PPO algorithm is already done. To see the algorithm working inside the environment, run:</br>
    ```
    cd ppo
    python3 test.py
    ```

    This is not recommended, but if you want to redo it, run:</br>
    ```
    cd ppo
    rm -rf spinupPpo; python3 train.py  
    ```


## Authors
* **Bruna Kimura up201902504@fe.up.pt** - [brunakimura](https://github.com/BrunaKimura/) 
* **Raphael Costa up201902503@fe.up.pt** - [raphacosta27](https://github.com/raphacosta27)

