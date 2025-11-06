from torch.utils.data import DataLoader
from torchvision import datasets, transforms

def get_loaders(batch=128):
    transform = transforms.Compose([
        transforms.Grayscale(),
        transforms.Resize((48,48)),
        transforms.ToTensor()
    ])

    train = datasets.ImageFolder("data/fer2013/train", transform=transform)
    val   = datasets.ImageFolder("data/fer2013/val", transform=transform)
    test  = datasets.ImageFolder("data/fer2013/test", transform=transform)

    classes = train.classes  # angry, happy, etc.

    train_dl = DataLoader(train, batch_size=batch, shuffle=True)
    val_dl   = DataLoader(val, batch_size=batch)
    test_dl  = DataLoader(test, batch_size=batch)

    return train_dl, val_dl, test_dl, classes
