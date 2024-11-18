import torch
import torch.nn.functional as F
from torchvision import models, transforms
from PIL import Image
import numpy as np
import os

# Thiết lập đường dẫn
base_path = os.path.expanduser("~/Documents/SOC/CTF/LMS/Introduction to Attacks on Artificial Intelligence Systems/MobileNetV2")
image_path = os.path.join(base_path, "284.png")  # Đường dẫn file ảnh đầu vào
output_path = os.path.join(base_path, "adversarial_red_fox.png")  # Đường dẫn lưu ảnh sau tấn công
perturbation_path = os.path.join(base_path, "perturbation.png")  # Đường dẫn lưu nhiễu

# Kiểm tra file ảnh
if not os.path.exists(image_path):
    raise FileNotFoundError(f"File ảnh không tồn tại: {image_path}")

# Bước 1: Tải mô hình MobileNetV2
model = models.mobilenet_v2(weights=models.MobileNet_V2_Weights.IMAGENET1K_V1)
model.eval()

# Lớp mục tiêu (red fox)
target_class = 277  # Bạn có thể thay đổi lớp mục tiêu, ví dụ: 283 (Persian cat)

# Tiền xử lý ảnh
preprocess = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Đọc và tiền xử lý ảnh
image = Image.open(image_path).convert("RGB")
input_tensor = preprocess(image).unsqueeze(0)  # Thêm chiều batch
input_tensor.requires_grad = True

# Tham số tấn công PGD
epsilon = 0.1  # Tổng mức nhiễu cho phép
num_iterations = 20  # Số bước lặp
alpha = epsilon / num_iterations  # Mức nhiễu mỗi bước

# Sao chép input tensor ban đầu
perturbed_tensor = input_tensor.clone()

# PGD: Tấn công đa bước
for i in range(num_iterations):
    # Khởi tạo lại tensor leaf
    perturbed_tensor = perturbed_tensor.detach().clone()
    perturbed_tensor.requires_grad = True

    # Dự đoán và tính loss
    output = model(perturbed_tensor)
    loss = F.cross_entropy(output, torch.tensor([target_class]))
    
    # Tính gradient
    model.zero_grad()
    loss.backward()

    # Thêm nhiễu
    perturbation = alpha * perturbed_tensor.grad.sign()
    perturbed_tensor = perturbed_tensor + perturbation
    
    # Giới hạn tổng nhiễu trong phạm vi epsilon
    total_perturbation = torch.clamp(perturbed_tensor - input_tensor, -epsilon, epsilon)
    perturbed_tensor = torch.clamp(input_tensor + total_perturbation, 0, 1)

    # Kiểm tra lớp dự đoán
    predicted_class = torch.argmax(model(perturbed_tensor), 1).item()
    print(f"Iteration {i+1}/{num_iterations}: Predicted class = {predicted_class}")

    # Nếu thành công, dừng lại
    if predicted_class == target_class:
        print(f"Tấn công thành công tại bước {i+1}!")
        break

# Lưu ảnh tấn công cuối cùng
inv_normalize = transforms.Normalize(
    mean=[-0.485 / 0.229, -0.456 / 0.224, -0.406 / 0.225],
    std=[1 / 0.229, 1 / 0.224, 1 / 0.225]
)
adversarial_image = inv_normalize(perturbed_tensor.squeeze(0)).detach().numpy()
adversarial_image = np.transpose(adversarial_image, (1, 2, 0))
adversarial_image = np.clip(adversarial_image, 0, 1) * 255
adversarial_image = Image.fromarray(adversarial_image.astype("uint8"))
adversarial_image.save(output_path)

# Lưu nhiễu
perturbation_image = (total_perturbation.squeeze(0).detach().cpu().numpy().transpose(1, 2, 0) * 255).astype("uint8")
perturbation_image = np.clip(perturbation_image, 0, 255)
Image.fromarray(perturbation_image).save(perturbation_path)

# Kết quả
print(f"Ảnh tấn công FGSM đã được lưu tại: {output_path}")
print(f"Nhiễu đã được lưu tại: {perturbation_path}")

# Kiểm tra lớp dự đoán cuối cùng
final_output = model(perturbed_tensor)
final_predicted_class = torch.argmax(final_output, 1).item()
if final_predicted_class == target_class:
    print(f"Thành công! Mô hình nhận dạng hình ảnh là 'red fox' (class {target_class}).")
else:
    print(f"Thất bại! Mô hình vẫn nhận dạng hình ảnh là class {final_predicted_class}.")

