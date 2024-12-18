import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# Define Image Parameters
img_height, img_width = 128, 128
batch_size = 32

# Data Augmentation and Preprocessing
transform = transforms.Compose([
    transforms.Resize((img_height, img_width)),
    transforms.RandomRotation(10),  # to simulate tilt in label
    transforms.ToTensor(),
    transforms.Normalize([0.5], [0.5])
])

train_dataset = datasets.ImageFolder(root='D:/GitHub/0000WorkSpace/test', transform=transform)
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

# Define CNN Model in PyTorch
class LabelInspectionCNN(nn.Module):
    def __init__(self):
        super(LabelInspectionCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1)
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.fc1 = nn.Linear(128 * 16 * 16, 128)  # Adjust based on input size
        self.fc2 = nn.Linear(128, 1)  # Binary classification

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = self.pool(torch.relu(self.conv2(x)))
        x = self.pool(torch.relu(self.conv3(x)))
        x = x.view(-1, 128 * 16 * 16)  # Flatten
        x = torch.relu(self.fc1(x))
        x = torch.sigmoid(self.fc2(x))
        return x

# Instantiate the Model
model = LabelInspectionCNN()

# Define Loss Function and Optimizer
criterion = nn.BCELoss()  # Binary Cross Entropy Loss
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training the Model
epochs = 10
for epoch in range(epochs):
    running_loss = 0.0
    for inputs, labels in train_loader:
        # Move to GPU if available
        inputs, labels = inputs.cuda(), labels.float().cuda()
        
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs.squeeze(), labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
    print(f'Epoch {epoch+1}, Loss: {running_loss/len(train_loader)}')

# Save the model for later use
torch.save(model.state_dict(), 'label_inspection_model_pytorch.pth')

# Inference: Check if the new image is Pass or NG
from PIL import Image

def classify_image_pytorch(img_path):
    img = Image.open(img_path)
    img = transform(img).unsqueeze(0)  # Add batch dimension
    img = img.cuda()  # Move to GPU if available
    
    model.eval()  # Switch to evaluation mode
    with torch.no_grad():
        output = model(img)
    if output.item() > 0.5:
        print("Pass")
    else:
        print("NG")

# Example inference
classify_image_pytorch('path_to_new_image.png')