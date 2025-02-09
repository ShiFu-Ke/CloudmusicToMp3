import os

# 添加 FFmpeg 的 bin 目录到 PATH 环境变量中
original_path = os.environ.get('PATH', '')
ffmpeg_bin_dir = f"{os.path.dirname(__file__)}\\bin\\ffmpeg\\bin"
os.environ['PATH'] = f"{ffmpeg_bin_dir};{original_path}"

from pydub import AudioSegment
import tkinter as tk
from tkinter import filedialog, messagebox


def open_files_dialog():
    """
    文件选择窗口
    """
    root = tk.Tk()
    root.withdraw()
    filetypes = [('音乐文件', '*.ncm *.flac')]
    file_paths = filedialog.askopenfilenames(parent=root, title='选择文件', filetypes=filetypes)
    return list(file_paths)


def ask_messagebox(title: str, msg: str):
    """
    提示窗口
    """
    root = tk.Tk()
    root.withdraw()
    answer = messagebox.askyesno(title, msg)
    root.destroy()
    return answer


def flac_to_mp3(flac_file_path, mp3_file_path):
    """
    将指定路径的 FLAC 文件转换为 MP3 文件。
    :param flac_file_path: 输入的 FLAC 文件路径
    :param mp3_file_path: 输出的 MP3 文件路径
    """
    # 加载 FLAC 文件
    audio = AudioSegment.from_file(flac_file_path, format="flac")
    # 导出为 MP3 文件
    audio.export(mp3_file_path, format="mp3")


if __name__ == "__main__":
    # 选中文件列表
    list_flac = open_files_dialog()

    # 执行转换
    length = len(list_flac)
    if length == 0:
        print("未选择文件！")
        exit(1)
    times = 0
    delete = ask_messagebox("提示","是否删除原文件？")
    print("开始转换...\n")
    for i in list_flac:
        index = i.rfind(".")
        if i[-3:] == "ncm":
            os.system(f'bin\\ncm_to_flac.exe "{i}" > nul 2>&1')
            if os.path.isfile(i[:index + 1] + "flac"):
                flac_to_mp3(i[:index + 1] + "flac", i[:index + 1] + "mp3")
                os.remove(i[:index + 1] + "flac")
        else:
            flac_to_mp3(i[:index + 1] + "flac", i[:index + 1] + "mp3")
        if delete:
            os.remove(i)
        times += 1
        print(f"已完成({times}/{length})：{i[i.rfind("\\") + 1:index + 1]}mp3")
    print("\n转换完成！")
