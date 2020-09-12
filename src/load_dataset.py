import torch
import torchvision.transforms as transforms
from .custom_dataset import CustomDataSet

im_size = 32


transform = transforms.Compose([
    transforms.Resize((im_size, im_size), interpolation=2),
    transforms.ToTensor(),
    transforms.Normalize((.5, .5, .5), (.5, .5, .5))])


def load_dataset(data_path):
    dataset = CustomDataSet(data_path, transform=transform)
    loader = torch.utils.data.DataLoader(
        dataset,
        batch_size=64,
        shuffle=False,
        num_workers=2
    )
    return loader, dataset.total_imgs
