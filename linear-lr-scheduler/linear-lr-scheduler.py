def linear_lr(step, total_steps, initial_lr, final_lr=0.0, warmup_steps=0) -> float:
    """
    Linear warmup (0→initial_lr) then linear decay (initial_lr→final_lr).
    Steps are 0-based; clamp at final_lr after total_steps.
    """
    # Write code here\
    t=step
    if(t<warmup_steps and warmup_steps>0):
        lr=(t*initial_lr)/warmup_steps
    elif(warmup_steps<=t and t<total_steps and total_steps!=warmup_steps):
        lr= final_lr+(initial_lr-final_lr)*((total_steps-t)/(total_steps-warmup_steps))
    elif(t>=total_steps):
        lr= final_lr
    else:
        lr=initial_lr
    return float(lr)
    pass