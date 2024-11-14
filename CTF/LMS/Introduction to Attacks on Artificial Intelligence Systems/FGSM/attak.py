def fgsm_attack(image, epsilon, gradient):
    # Lấy dấu của gradient
    sign_gradient = gradient.sign()
    # Tạo ảnh bị tấn công bằng cách thêm nhiễu vào ảnh gốc
    perturbed_image = image + epsilon * sign_gradient
    # Cắt giá trị để giữ chúng trong khoảng [0,1]
    perturbed_image = torch.clamp(perturbed_image, 0, 1)
    return perturbed_image

# Kiểm tra tấn công FGSM trên một mẫu
dataiter = iter(trainloader)
images, labels = dataiter.next()
images, labels = images.to(device), labels.to(device)

# Thiết lập mức epsilon
epsilon = 0.1

# Đặt gradient của model là True
images.requires_grad = True

# Tính dự đoán và hàm mất mát
outputs = model(images)
loss = criterion(outputs, labels)

# Tính gradient
model.zero_grad()
loss.backward()

# Thực hiện tấn công FGSM
data_grad = images.grad.data
perturbed_data = fgsm_attack(images, epsilon, data_grad)

# Dự đoán lại với ảnh đã bị tấn công
output = model(perturbed_data)
final_pred = output.max(1, keepdim=True)[1]

# So sánh dự đoán trước và sau tấn công
print("Dự đoán ban đầu:", labels)
print("Dự đoán sau tấn công:", final_pred.view_as(labels))
