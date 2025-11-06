import torch, torch.optim as optim, torch.nn as nn
from emotion_model import EmotionNet
from tqdm import tqdm
from dataset_fer import get_loaders

device = "cuda" if torch.cuda.is_available() else "cpu"

train_dl, val_dl, test_dl, classes = get_loaders()

model = EmotionNet(num_classes=len(classes)).to(device)
opt   = optim.Adam(model.parameters(), lr=1e-3)
lossv = nn.CrossEntropyLoss()

for epoch in range(5):
    model.train()
    loop = tqdm(train_dl, total=len(train_dl))
    for x,y in loop:
        x,y = x.to(device), y.to(device)
        opt.zero_grad()
        pred = model(x)
        loss = lossv(pred,y)
        loss.backward()
        opt.step()
        loop.set_description(f"Epoch {epoch}")
        loop.set_postfix(loss=loss.item())


    model.eval()
    correct = 0
    total   = 0
    with torch.no_grad():
        for x,y in val_dl:
            x,y = x.to(device), y.to(device)
            pred = model(x).argmax(1)
            correct += (pred == y).sum().item()
            total   += len(y)

    print(f"Epoch {epoch} Acc: {correct/total:.2f}")

torch.save(model.state_dict(),"models/emotion.pt")
print("Saved!")
