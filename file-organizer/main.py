import os
import shutil
import argparse


# 按文件类型分类的规则
file_categories = {
    "图片": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".heic"],
    "文档": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".xls", ".ppt", ".pptx", ".csv", ".md"],
    "视频": [".mp4", ".avi", ".mov", ".mkv", ".flv", ".wmv"],
    "音频": [".mp3", ".wav", ".flac", ".aac", ".m4a"],
    "压缩包": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
    "代码": [".py", ".js", ".ts", ".html", ".css", ".java", ".cpp", ".c", ".go", ".rs"],
}


def get_category(filename):
    """根据文件扩展名判断属于哪个分类"""
    ext = os.path.splitext(filename)[1].lower()
    for category, extensions in file_categories.items():
        if ext in extensions:
            return category
    return "其他"


def organize_files(source_dir, dry_run=False):
    """
    扫描目录，把文件按类型移到对应子文件夹

    参数:
        source_dir: 要整理的目录路径
        dry_run: 如果为 True，只打印会做什么，不实际移动文件（预览模式）
    """
    if not os.path.exists(source_dir):
        print(f"目录不存在: {source_dir}")
        return

    moved_count = 0
    skipped_count = 0

    for filename in os.listdir(source_dir):
        filepath = os.path.join(source_dir, filename)

        # 跳过子目录和隐藏文件
        if os.path.isdir(filepath) or filename.startswith("."):
            skipped_count += 1
            continue

        category = get_category(filename)

        # 创建目标子文件夹
        target_dir = os.path.join(source_dir, category)
        if not os.path.exists(target_dir):
            if dry_run:
                print(f"[预览] 会创建文件夹: {category}/")
            else:
                os.makedirs(target_dir)
                print(f"创建文件夹: {category}/")

        # 移动文件
        target_path = os.path.join(target_dir, filename)
        if dry_run:
            print(f"[预览] {filename} -> {category}/")
        else:
            shutil.move(filepath, target_path)
            print(f"移动: {filename} -> {category}/")
        moved_count += 1

    print(f"\n整理完成! 移动 {moved_count} 个文件, 跳过 {skipped_count} 个")


def main():
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(
        description="文件整理机器人 - 按文件类型自动归类",
        epilog="示例:\n  python3 main.py ~/Desktop/test-folder\n  python3 main.py ~/Downloads --dry-run",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    # 位置参数：要整理的目录（必填）
    parser.add_argument(
        "source",
        help="要整理的目录路径",
    )

    # 可选参数：预览模式
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="预览模式：只显示会做什么，不实际移动文件",
    )

    # 解析命令行参数
    args = parser.parse_args()

    # 执行整理
    organize_files(args.source, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
