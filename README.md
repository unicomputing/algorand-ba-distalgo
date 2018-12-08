# Implementing Algorand Byzantine agreement BA* in DistAlgo
<https://sites.google.com/a/stonybrook.edu/sbcs535/projects/algorand-ba-distalgo>

1. Usage
 python -m da algorand.da [-h] [-u NUSERS] [-tr NTRAITORS] [-st STAKE_TRAITORS]
                   [-lb LAMBDA_BLOCK] [-ls LAMBDA_STEP] [-Tf T_FINAL]
                   [-Ts T_STEP] [-ts TAU_STEP] [-tp TAU_PROPOSER]
                   [-tf TAU_FINAL] [-ms MAX_STEPS] [-bp] [-pbp]
                   [-bl BLOCK_SIZE] [-cl CL] [-ll]
                   
  -h, --help            show this help message and exit
  -u NUSERS, --users NUSERS
                        Number of users the algorand runs with
  -tr NTRAITORS, --traitors NTRAITORS
                        Number of traitors that algorand runs with
  -st STAKE_TRAITORS, --stake-traitors STAKE_TRAITORS
                        Sum of fractions of stake held by all traitors
  -lb LAMBDA_BLOCK, --lambda-block LAMBDA_BLOCK
                        Timeout for receiving a block
  -ls LAMBDA_STEP, --lambda-step LAMBDA_STEP
                        Timeout for BA* step
  -Tf T_FINAL, --t_final T_FINAL
                        threshold of tau final for BA*
  -Ts T_STEP, --t_step T_STEP
                        Threshold of tau step for BA*
  -ts TAU_STEP, --tau_step TAU_STEP
                        Expected # of committee members
  -tp TAU_PROPOSER, --tau_proposer TAU_PROPOSER
                        expected # of block proposers
  -tf TAU_FINAL, --tau_final TAU_FINAL
                        expected # of final committee members
  -ms MAX_STEPS, --max_steps MAX_STEPS
                        maximum number of steps in BinaryBA*
  -bp, --byzantine-proposer
                        Force highest-priority proposer to be malicious
                        regardless of stake-traitors
  -pbp, --prevent-byzantine-proposer
                        Prevent any proposer from being malicious (overrides
                        byzantine-proposer)
                        
  -bl BLOCK_SIZE, --block-size BLOCK_SIZE
                        Size of a block in Bytes (bl <= 3)
  -cl CL, --chain-length CL
                        Length of Chain to generate, cl = number of final
                        blocks. If -1, continue indefinitely.
  -ll, --log_enable     Print Log Outputs for all processes
