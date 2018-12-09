# Implementing Algorand Byzantine agreement BA* in DistAlgo
<https://sites.google.com/a/stonybrook.edu/sbcs535/projects/algorand-ba-distalgo>

# Prerequisites
* Python 3.5 and above
* Mac/Windows or Linux environment

### Installing all the required python packages
Install all the dependencies using pip:

    cd algorand/src
    pip3 install -r requirements.txt
# Usage
    python3 -m da algorand.da [-h] [-u NUSERS] [-tr NTRAITORS] [-st STAKE_TRAITORS]
                   [-lb LAMBDA_BLOCK] [-ls LAMBDA_STEP] [-Tf T_FINAL]
                   [-Ts T_STEP] [-ts TAU_STEP] [-tp TAU_PROPOSER]
                   [-tf TAU_FINAL] [-ms MAX_STEPS] [-bp] [-pbp]
                   [-bl BLOCK_SIZE] [-cl CL] [-ll]
                    </b>
  -h, --help            show the help message and exit \
  -u NUSERS, --users NUSERS
                        Number of users the algorand runs with, default = 10\
  -tr NTRAITORS, --traitors NTRAITORS
                        Number of traitors that algorand runs with, default = 0\
  -st STAKE_TRAITORS, --stake-traitors STAKE_TRAITORS
                        Sum of fractions of stake held by all traitors default = 0.33\
  -lb LAMBDA_BLOCK, --lambda-block LAMBDA_BLOCK
                        Timeout for receiving a block default = 4secs\
  -ls LAMBDA_STEP, --lambda-step LAMBDA_STEP
                        Timeout for BA* step default = 4 secs\
  -Tf T_FINAL, --t_final T_FINAL
                        threshold of tau final for BA* default = 0.74\
  -Ts T_STEP, --t_step T_STEP
                        Threshold of tau step for BA* default = 0.685\
  -ts TAU_STEP, --tau_step TAU_STEP
                        Expected # of committee members default =  5\
  -tp TAU_PROPOSER, --tau_proposer TAU_PROPOSER
                        expected # of block proposers default = 2\
  -tf TAU_FINAL, --tau_final TAU_FINAL
                        expected # of final committee members default = 6\
  -ms MAX_STEPS, --max_steps MAX_STEPS
                        maximum number of steps in BinaryBA* default = 50\
  -bp, --byzantine-proposer
                        Force highest-priority proposer to be malicious
                        regardless of stake-traitors default = False\
  -pbp, --prevent-byzantine-proposer
                        Prevent any proposer from being malicious (overrides
                        byzantine-proposer) default = False \  
  -bl BLOCK_SIZE, --block-size BLOCK_SIZE
                        Size of a block in Bytes (bl <= 3) default = 0\
  -cl CL, --chain-length CL
                        Length of Chain to generate, cl = number of final
                        blocks. If -1, continue indefinitely. default = 5\
  -ll, --log_enable     Print Log Outputs for all processes default = False
  
  
### Sample algorand run for 1 round and 10 users

    python3 -m da algorand.da -u 10 -cl 1</b>

### Sample algorand run for 3 rounds (i.e blockchain of 3 blocks)

    python3 -m da algorand.da -cl 3

### Sample algroand run with 5 traitors and 20 user

    python3 -m da algorand.da -u 20 -tr 5</b>

### Sample algorand run forcing the highest priority proposer to be the traitor 

    python3 -m da algorand.da -u 10 -bp</b>

### Sample algorand run with 5 traitors but preventing the highest priority proposer from being a traitor

    python3 -m da algorand.da -tr 5 -pbp</b> \
    (Note: pbp takes precedence over bp) 

### Sample algorand run with all the traitor stakes ccombined to be 0.5

    python3 -m da algorand.da -tr 5 -st 0.5</b>





 
