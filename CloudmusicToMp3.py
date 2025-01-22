import os

# 添加 FFmpeg 的 bin 目录到 PATH 环境变量中
original_path = os.environ.get('PATH', '')
ffmpeg_bin_dir = f"{os.path.dirname(__file__)}\\ffmpeg\\bin"
os.environ['PATH'] = f"{ffmpeg_bin_dir};{original_path}"

from pydub import AudioSegment
from win32con import OFN_ALLOWMULTISELECT, IDOK, OFN_FILEMUSTEXIST, MB_ICONMASK, MB_OKCANCEL
from win32ui import CreateFileDialog


def open_files_dialog():
    """
    文件选择窗口
    """
    # 定义文件类型过滤器
    lps_filter = "cloudmusic Files|*.ncm;*.flac"

    # 创建打开文件对话框对象并启用多选
    dlg = CreateFileDialog(True, None, None,
                           OFN_FILEMUSTEXIST | OFN_ALLOWMULTISELECT,
                           lps_filter)
    if dlg.DoModal() == IDOK:  # 检查是否点击了“打开”
        return dlg.GetPathNames()  # 获取选择的文件名称列表
    return []


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
    list_flac = open_files_dialog()

    # 执行转换
    length = len(list_flac)
    if length == 0:
        print("未选择文件！")
        exit(1)
    times = 0
    print("开始转换...\n")
    for i in list_flac:
        if i[-3:] == "ncm":
            os.system(f'ncm_to_mp3.exe "{i}" > nul 2>&1')
            flac_to_mp3(i[:i.rfind(".") + 1] + "flac", i[:i.rfind(".") + 1] + "mp3")
            os.remove(i[:i.rfind(".") + 1] + "flac")
        else:
            flac_to_mp3(i[:i.rfind(".") + 1] + "flac", i[:i.rfind(".") + 1] + "mp3")
        times += 1
        print(f"已完成({times}/{length})：{i[i.rfind("\\") + 1:i.rfind(".") + 1]}mp3")
    print("\n转换完成！")
