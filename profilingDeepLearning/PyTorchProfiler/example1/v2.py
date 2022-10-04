# This example is adapted from
# https://pytorch.org/tutorials/recipes/recipes/profiler_recipe.html

import torch
import torchvision.models as models
import torch.autograd.profiler as profiler

torch.set_default_tensor_type(torch.DoubleTensor)
model = models.resnet18()
inputs = torch.randn(128, 3, 224, 224)

with profiler.profile(profile_memory=True, record_shapes=True) as prof:
    model(inputs)
print(prof.key_averages().table(sort_by="self_cpu_memory_usage", row_limit=10))
