import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torchvision
import torchvision.datasets as datasets
import torchvision.models as models
import torchvision.transforms as transforms
from torch.autograd import Variable


from collections import Counter
import os
from PIL import Image


# Load
PATH = "best_model_tank_v1.pth"
classes = 4
device = 'cpu'

model = models.alexnet(pretrained=True)
model.classifier[6] = torch.nn.Linear(model.classifier[6].in_features, classes)

checkpoint = torch.load(PATH)
model.load_state_dict(torch.load(PATH))
model.eval()

preprocess = transforms.Compose([
        transforms.ColorJitter(0.1, 0.1, 0.1, 0.1),
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

classes_map = {0: 'forward',
               1: 'reverse',
               2: 'turn_left',
               3: 'turn_right'}



def predict_image(image):
    
    image_tensor = preprocess(image).float()
    image_tensor = image_tensor.unsqueeze_(0)
    input = Variable(image_tensor)
    input = input.to(device)
    output = model(input)
    index = output.data.cpu().numpy().argmax()
    return index



def next_move(img):

    return classes_map[predict_image(img)]

    

    
