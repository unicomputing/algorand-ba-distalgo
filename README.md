# Implementing Algorand Byzantine agreement BA* in DistAlgo
<https://sites.google.com/a/stonybrook.edu/sbcs535/projects/algorand-ba-distalgo>

# Prerequisites
* Python 3.5 or Python 3.6
* Mac/Windows or Linux environment

### Installing all the required python packages
Install all the dependencies using pip:

    pip install -r requirements.txt
# Usage
    python3 -m da algorand.da [-h] [-u NUSERS] [-tr NTRAITORS] [-st STAKE_TRAITORS]
                   [-lb LAMBDA_BLOCK] [-ls LAMBDA_STEP] [-Tf T_FINAL]
                   [-Ts T_STEP] [-ts TAU_STEP] [-tp TAU_PROPOSER]
                   [-tf TAU_FINAL] [-ms MAX_STEPS] [-bp] [-pbp]
                   [-bl BLOCK_SIZE] [-cl CL] [-ll]
                    
  `-h, --help`  Show the help message and exit \
  `-u , --users`   Number of users the algorand runs with, `default = 10`\
  `-tr , --traitors`   Number of traitors that algorand runs with, `default = 0`\
  `-st , --stake-traitors`  Sum of fractions of stake held by all traitors `default = 0.33`\
  `-lb , --lambda-block`   Timeout for receiving a block `default = 4`secs\
  `-ls , --lambda-step `  Timeout for BA* step `default = 4`secs\
  `-Tf , --t_final` h reshold of tau final for BA* `default = 0.74`\
  `-Ts , --t_step`
                        Threshold of tau step for BA* `default = 0.685`\
  `-ts , --tau_step`
                        Expected # of committee members `default =  5`\
  `-tp , --tau_proposer`
                        Expected # of block proposers `default = 2`\
  `-tf , --tau_final`
                        Expected # of final committee members `default = 6`\
  `-ms , --max_steps`
                        Maximum number of steps in BinaryBA* `default = 50`\
  `-bp, --byzantine-proposer`
                        Force highest-priority proposer to be malicious
                        regardless of stake-traitors `default = False`\
  `-pbp, --prevent-byzantine-proposer`
                        Prevent any proposer from being malicious (overrides
                        byzantine-proposer) `default = False `
  `-bl , --block-size`
                        Size of a block in Bytes (bl <= 3) `default = 0`\
  `-cl , --chain-length`
                        Length of Chain to generate, cl = number of final
                        blocks. If -1, continue indefinitely. `default = 5`\
 ` -ll, --log_enable`     Print Log Outputs for all processes `default = False`
  
  
### Sample algorand run for 1 round and 10 users

    python -m da algorand.da -u 10 -cl 1

### Sample algorand run for 3 rounds (i.e blockchain of 3 blocks)

    python -m da algorand.da -cl 3

### Sample algroand run with 5 traitors and 20 user

    python -m da algorand.da -u 20 -tr 5

### Sample algorand run forcing the highest priority proposer to be the traitor 

    python -m da algorand.da -u 10 -bp

### Sample algorand run with 5 traitors but preventing the highest priority proposer from being a traitor

    python -m da algorand.da -tr 5 -pbp
    (Note: pbp takes precedence over bp) 

### Sample algorand run with all the traitor stakes ccombined to be 0.5

    python -m da algorand.da -tr 5 -st 0.5
    
    
# Correctness and Performance Testing
Monitor.da runs correctness and performance tests to check Safety, Liveness and Validity on the algorand.da in the following cases
* Checks correctness with various number of users.
* Checks correctness with various number of traitors.
* Checks correctness with various stakes of traitors.
* Checks correctness with various timeout parameters.

The Monitor runs the tests for combination of following set of parameters
* No.of Users range 20-50
* No.of traitors range 0-17
* Traitor stakes range 0-0.36
* No.of committee members in step range from 5-20
* Block size range from approximately 0-3Kb

Run the test as below

    python3 -m da Monitor.da
    
The results of the tests will be saved in correctness.csv and performance.csv respectively.





 
