# print("Hello,Python!我回来了")
import os
import shutil

# 要整理的目录（改成你自己的路径）
source_dir = "/Users/Michael/Downloads"

# 按文件类型分类的规则
file_categories = {
    "图片": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "文档": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".ppt", ".pptx"],
    "视频": [".mp4", ".avi", ".mov", ".mkv"],
    "音频": [".mp3", ".wav", ".flac", ".aac"],
    "压缩包": [".zip", ".rar", ".7z", ".tar", ".gz"],
}

def get_category(filename):
    """根据文件扩展名判断属于哪个分类"""
    ext = os.path.splitext(filename)[1].lower()
    for category, extensions in file_categories.items():
        if ext in extensions:
            return category
    return "其他"

def organize_files(source_dir):
    """扫描目录，把文件按类型移到对应子文件夹"""
    if not os.path.exists(source_dir):
        print(f"目录不存在: {source_dir}")
        return

    # 遍历目录中的所有文件
    for filename in os.listdir(source_dir):
        filepath = os.path.join(source_dir, filename)
        
        # 跳过子目录和隐藏文件
        if os.path.isdir(filepath) or filename.startswith("."):
            continue
        
        # 判断文件类型
        category = get_category(filename)
        
        # 创建目标子文件夹
        target_dir = os.path.join(source_dir, category)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
            print(f"创建文件夹: {category}/")
        
        # 移动文件
        target_path = os.path.join(target_dir, filename)
        shutil.move(filepath, target_path)
        print(f"移动: {filename} -> {category}/")

if __name__ == "__main__":
    organize_files(source_dir)
    print("整理完成!")
