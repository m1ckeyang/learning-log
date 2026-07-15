# 文件整理机器人

## 功能
自动把指定目录里的文件按扩展名分类，移动到对应的子文件夹中。

## 适合场景
- 整理学校共享文件夹里的课件、通知、图片
- 整理桌面堆积的临时文件
- 整理下载目录

## 用法

```bash
# 基本用法：整理指定目录
python3 main.py ~/Desktop/test-folder

# 预览模式：只看会做什么，不实际移动文件
python3 main.py ~/Downloads --dry-run

# 查看帮助
python3 main.py --help
```

## 分类规则
| 分类 | 扩展名 |
|------|--------|
| 图片 | .jpg .jpeg .png .gif .bmp .svg .webp .heic |
| 文档 | .pdf .doc .docx .txt .xlsx .xls .ppt .pptx .csv .md |
| 视频 | .mp4 .avi .mov .mkv .flv .wmv |
| 音频 | .mp3 .wav .flac .aac .m4a |
| 压缩包 | .zip .rar .7z .tar .gz .bz2 |
| 代码 | .py .js .ts .html .css .java .cpp .c .go .rs |
| 其他 | 不在以上列表中的文件 |

## 版本历史
- **v0.2**：添加命令行参数（argparse），不用改代码就能指定目录；新增预览模式（--dry-run）
- **v0.1**：基础分类，按文件类型自动归类

## 后续计划
- v0.3：支持按日期再分类，比如 `文档/2026-07/通知.pdf`
- v0.4：支持日志文件，记录每次整理移动了哪些文件
