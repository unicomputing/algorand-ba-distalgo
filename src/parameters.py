class Parameters:
    """
    The following parameters are parameters.

    lambda_block = Timeout for receiving a block
    lambda_step = Timeout for BA* step
    T_final = Threshold of tau final for BA*
    T_step = Threshold of tau step for BA*
    tau_step = Expected # of committee members
    tau_proposer = Expected # of block proposers
    tau_final = Expected # of final committee members
    max_steps = Maximum number of steps in BinaryBA*
    logger_level = The logging level of the whole program.
    loss_rate = The loss rate of the messages.
    msg_delay = Delay inreceiving the message

    """
    lambda_block = 10
    lambda_step = 10
    T_final = 0.74
    T_step = 0.685
    tau_step = 5
    tau_proposer = 2
    tau_final = 6
    max_steps = 50
    logger_level = 10
    loss_rate = 0
    msg_delay = 0
