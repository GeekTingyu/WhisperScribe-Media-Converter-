# 语音/视频转文字工具

## 项目简介
这是一个基于Python的工具，使用OpenAI的Whisper AI模型将音频和视频文件转录为文本。该工具支持多种音频和视频格式，并提供了简单的使用界面。

## 功能特点
- 支持多种音频格式（mp3, wav, m4a等）
- 支持多种视频格式（mp4, avi等）
- 自动将转写文本保存为txt文件
- 自动管理已处理的文件
- 显示转写进度条
- 支持中文和英文转写

## 项目结构
```
speech_to_text_project/
├── transcribe.py      # 主程序脚本
├── run_transcribe.bat # 运行脚本的批处理文件
├── requirements.txt   # 项目依赖
└── README.md         # 项目文档
```

## 环境要求
- Python 3.11
- FFmpeg
- 足够的磁盘空间（用于模型缓存）

## 安装步骤
1. **安装Python依赖**
   ```bash
   pip install -r requirements.txt
   ```

2. **安装FFmpeg**
   - 下载FFmpeg并解压到指定目录
   - 确保FFmpeg路径已在脚本中正确配置

## 使用方法
1. **准备音频/视频文件**
   - 将需要转写的文件放入输入目录：`E:/aidataaudios/audios/`

2. **运行程序**
   - 双击运行`run_transcribe.bat`
   - 或在命令行中运行：
     ```bash
     python transcribe.py
     ```

3. **查看结果**
   - 转写结果将保存在：`E:/aidataaudios/text/`
   - 已处理的文件将移动到：`E:/aidataaudios/okaudios/`

## 目录说明
- **输入目录**：`E:/aidataaudios/audios/`
  - 存放待转写的音频和视频文件
- **输出目录**：`E:/aidataaudios/text/`
  - 存放转写生成的文本文件
- **已处理目录**：`E:/aidataaudios/okaudios/`
  - 存放已完成转写的原始文件

## 注意事项
1. **文件格式**
   - 确保输入文件为支持的音频或视频格式
   - 文件名不要包含特殊字符

2. **系统资源**
   - 转写过程可能较慢，请耐心等待
   - 确保系统有足够的磁盘空间和内存

3. **网络要求**
   - 首次运行需要下载模型，请确保网络连接正常
   - 模型下载完成后可离线使用

## 故障排除
1. **模型下载失败**
   - 检查网络连接
   - 确认模型缓存目录权限正确

2. **转写失败**
   - 检查FFmpeg是否正确安装
   - 确认输入文件格式是否支持
   - 查看错误信息进行相应处理

## 技术支持
如遇到问题，请检查：
1. Python环境是否正确配置
2. 所有依赖是否正确安装
3. FFmpeg是否正确配置
4. 文件路径是否正确设置
