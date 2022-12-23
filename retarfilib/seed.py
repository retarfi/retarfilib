def fix_seed(seed: int) -> None:
    try:
        import numpy as np

        np.random.seed(seed)
        np.random.RandomState(seed)
    except ModuleNotFoundError:
        pass
    try:
        import torch

        torch.manual_seed(seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
    except ModuleNotFoundError:
        pass
    try:
        import transformers

        transformers.trainer_utils.set_seed(seed=seed)
    except ModuleNotFoundError:
        pass
