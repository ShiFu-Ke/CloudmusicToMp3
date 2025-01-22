# CloudmusicToMp3

## 软件功能

网易云音乐下载**无损**格式的`ncm`或`flac`文件，转换为`mp3`格式。

## 使用方法

1. 安装第三方库。
   ```python
   pip install -r requirements.txt
   ```

2. 执行脚本。
   ```python
   python CloudmusicToMp3.py
   ```

3. 选择`ncm`或`flac`文件，可以多选。

4. 执行完成后，会在原目录生成`mp3`文件。

## 转换失败原因

1. 网易云音乐下载格式不是**无损**格式。
2. 网易云更新加密算法。