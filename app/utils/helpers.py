import torch



def create_torch_generator(seed):

    if seed is None:

        return None


    seed=int(seed)


    if torch.cuda.is_available():

        return torch.Generator(
            device="cuda"
        ).manual_seed(seed)


    return torch.Generator(
        device="cpu"
    ).manual_seed(seed)