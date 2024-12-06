import sys
import os
from pathlib import Path
import shutil
from transformers import pipeline, WhisperForConditionalGeneration, WhisperProcessor
import concurrent.futures
from tqdm import tqdm

# 设置Hugging Face模型缓存目录
cache_dir = 'E:/speech_to_text_project/model_cache'
if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)
os.environ['HUGGINGFACE_HUB_CACHE'] = cache_dir

# 指定ffmpeg的路径
os.environ['PATH'] = 'E:/ffmpeg-2024-12-04-git-2f95bc3cb3-essentials_build/bin;' + os.environ['PATH']

def transcribe_media(file_path, transcriber):
    """
    将视频或音频文件转换为文字
    :param file_path: 媒体文件路径
    :param transcriber: 已加载的转写器
    :return: 转写的文本
    """
    try:
        # 检查文件是否存在
        if not os.path.exists(file_path):
            print(f"错误：文件 {file_path} 不存在")
            return

        print(f"开始转写 {file_path}")
        # 执行转写
        result = transcriber(file_path)
        text = result["text"]

        return text

    except Exception as e:
        print(f"发生错误：{str(e)}")
        return None

def transcribe_all_files(input_dir, output_text_dir, processed_dir):
    """
    转写input_dir目录中的所有音频和视频文件，将文本输出到output_text_dir，并将处理后的文件移动到processed_dir。
    """
    if not os.path.exists(output_text_dir):
        os.makedirs(output_text_dir)
    if not os.path.exists(processed_dir):
        os.makedirs(processed_dir)

    # 在主线程中加载模型和处理器
    print("正在加载模型...")
    model = WhisperForConditionalGeneration.from_pretrained(
        "openai/whisper-large",
        cache_dir=cache_dir
    )
    processor = WhisperProcessor.from_pretrained(
        "openai/whisper-large",
        cache_dir=cache_dir
    )
    transcriber = pipeline("automatic-speech-recognition", model=model, tokenizer=processor.tokenizer, feature_extractor=processor.feature_extractor, chunk_length_s=30)

    # 使用多线程进行转写
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(transcribe_media, os.path.join(input_dir, file_name), transcriber): file_name for file_name in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, file_name))}
        for future in tqdm(concurrent.futures.as_completed(futures), total=len(futures), desc="Transcribing", unit="file"):
            file_name = futures[future]
            try:
                text = future.result()
                if text:
                    output_file = os.path.join(output_text_dir, Path(file_name).stem + "_transcript.txt")
                    with open(output_file, "w", encoding="utf-8") as f:
                        f.write(text)
                    print(f"文本已保存到 {output_file}")

                    # 移动已处理文件
                    shutil.move(os.path.join(input_dir, file_name), os.path.join(processed_dir, file_name))
                    print(f"已移动文件: {file_name} 到 {processed_dir}")
            except Exception as e:
                print(f"处理文件 {file_name} 时发生错误：{e}")

if __name__ == "__main__":
    input_directory = "E:/aidataaudios/audios"
    output_text_directory = "E:/aidataaudios/text"
    processed_directory = "E:/aidataaudios/okaudios"
    transcribe_all_files(input_directory, output_text_directory, processed_directory)
