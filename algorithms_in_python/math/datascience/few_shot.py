import torch
import torch.nn as nn


def cosine_similarity():
    input1 = torch.randn(100, 128)
    input2 = torch.randn(100, 128)
    cos = nn.CosineSimilarity(dim=1, eps=1e-6)
    output = cos(input1, input2)
    print(output)


def triplet_loss():
    triplet_loss = nn.TripletMarginLoss(margin=1.0, p=2)
    anchor = torch.randn(100, 128, requires_grad=True)
    positive = torch.randn(100, 128, requires_grad=True)
    negative = torch.randn(100, 128, requires_grad=True)
    output = triplet_loss(anchor, positive, negative)
    output.backward()

e = 2.7182818284590452353602874713527
def sin_h(x):
    return (e ** x) - (e ** -x) /2

def sinh(x):
    return (1 - (e ** (-2 * x))) / (2 * (e ** -x))

if __name__ == "__main__":
    print(sinh(30))
    print(sin_h(30))
