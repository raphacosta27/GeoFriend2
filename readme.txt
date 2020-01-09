Bruna Kimura and Raphael Costa1
Universidade do Porto, Porto, Portugal. 
Up201802504@fe.up.pt, Up201802503@fe.up.pt

1) This project was developed using the following:
    Ubuntu 16 or higher
    python 3.7.5: https://www.python.org/downloads/release/python-375/

2) Install pip for the version of this python. In ubuntu:
    sudo apt-get install python3-pip

3) Next, install the other libraries needed for this project:
    pip3 install keras==2.2.4
    pip3 install keras-rl==0.4.2
    pip3 install tensorflow==1.13.1
    pip3 install gym==0.12.1
    pip3 install h5py==2.9.0
    pip3 install pygame

4) Install the Spinning Up library following their site instructions:
    https://spinningup.openai.com/en/latest/user/installation.html

5) Finally, make sure that you are in the main directory of the project and run:
    pip3 install -e .

6) The trainment for PPO algorithm is already done. To see the algorithm working inside the environment, run:
    cd ppo
    python3 test.py

    This is not recommended, but if you want to redo it, run:
    cd ppo
    rm -rf spinupPpo; python3 train.py  