import torch
from emotion_model import EmotionNet
from dataset_fer import get_loaders

_, _, _, classes = get_loaders()

model = EmotionNet(num_classes=len(classes))
model.load_state_dict(torch.load("models/emotion.pt", map_location="cpu"))
model.eval()

dummy = torch.randn(1,1,48,48)
torch.onnx.export(model, dummy, "models/emotion.onnx",
                  input_names=["input"],
                  output_names=["output"],
                  opset_version=12)

print("Exported ONNX!")
