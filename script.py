import torch
from src.net import Net
import json
import argparse
from src.load_dataset import load_dataset

PATH = './model.pth'
class_map = {
    0: 'female',
    1: 'male',
}

parser = argparse.ArgumentParser()
parser.add_argument('path', type=str)
args = parser.parse_args()

net = Net()
net.load_state_dict(torch.load(PATH))

loader, names = load_dataset(args.path)
predicted_general = []
for images in loader:
    outputs = net(images)
    _, predicted = torch.max(outputs, 1)
    predicted_general += predicted.tolist()

data = {
    names[i]: class_map[predicted_general[i]] for i in range(len(names))
}

with open('process_results.json', 'w') as outfile:
    json.dump(data, outfile)
