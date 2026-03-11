from PIL import Image
import os

folder = "사진"
max_width = 1920  # 웹 최대 너비
quality = 82      # JPEG 품질 (0~100)

for filename in os.listdir(folder):
    if not filename.lower().endswith(('.jpg', '.jpeg', '.png')): 
        continue

    path = os.path.join(folder, filename)
    original_size = os.path.getsize(path) / (1024 * 1024)

    img = Image.open(path)
    img = img.convert("RGB")  # PNG도 JPEG로 저장 가능하게

    # 너비가 max_width 초과시 리사이즈
    if img.width > max_width:
        ratio = max_width / img.width
        new_size = (max_width, int(img.height * ratio))
        img = img.resize(new_size, Image.LANCZOS)

    # 저장 (원본 덮어쓰기, PNG도 JPG로 변환)
    if filename.lower().endswith('.png'):
        save_path = os.path.join(folder, filename)  # 확장자 유지
        img.save(save_path, "PNG", optimize=True)
    else:
        img.save(path, "JPEG", quality=quality, optimize=True)

    new_size_mb = os.path.getsize(path) / (1024 * 1024)
    print(f"{filename}: {original_size:.1f}MB → {new_size_mb:.1f}MB")

print("\n압축 완료!")