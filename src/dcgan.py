import os
import datetime

import torch
import torchvision
import matplotlib.pyplot as plt

# モデル読み込み
use_gpu = True if torch.cuda.is_available() else False
model = torch.hub.load('facebookresearch/pytorch_GAN_zoo:hub', 'DCGAN', pretrained=True, useGPU=use_gpu)

#ノイズ設定
num_images = 1 # <- 自由に変更してね！
noise, _ = model.buildNoiseData(num_images)

# 画像生成
with torch.no_grad():
    generated_images = model.test(noise)

# 保存
save_dir = "../result/dcgan"
os.makedirs(save_dir, exist_ok=True)
plt.imshow(torchvision.utils.make_grid(generated_images).permute(1, 2, 0).cpu().numpy())
plt.savefig(f"{save_dir}/{datetime.datetime.now()}.png")
