<p align="center">
  <img src="src/logo-no-background.svg" width='100%'>
</p>


<!-- 图标 -->
<p align="center">
  <a href="https://github.com/tiansztiansz/tiansztiansz/blob/main/wechat_alipay.png">
    <img alt="捐赠" src="src/捐赠.svg" />
  </a>&nbsp; &nbsp; 
  <!-- <a href="https://github.com/tiansztiansz/voice-assistant/blob/main/LICENSE">
    <img alt="License" src="src/license.svg" />
  </a>&nbsp; &nbsp;  -->
  <a href="https://space.bilibili.com/28606893?spm_id_from=333.1007.0.0">
    <img alt="bilibili图标" src="src/BILIBILI_LOGO.svg" />
  </a>&nbsp; &nbsp; 
  <a href="https://www.cnblogs.com/tiansz/">
    <img alt="博客园" src="src/博客园.jpg" />
  </a>&nbsp; &nbsp;
  <a href="https://www.douyin.com/user/MS4wLjABAAAAqkpp6UyrANDXFStAMWuRPp7FU4zHfyq0_OYPoC75_qQ">
    <img alt="抖音" src="src/抖音.svg" />
  </a>&nbsp; &nbsp;
  <a href="https://www.kaggle.com/tiansztianszs">
    <img alt="kaggle" src="src/kaggle.svg" />
  </a>
</p>

<p align="center">A lightweight dialogue system based on local knowledge base and ChatYuan</p>


<br>

## how to run
First download this repository:
```bash
git clone https://github.com/tiansztiansz/langchain-chatyuan.git
```
Then switch to the project directory:
```bash
cd langchain-chatyuan
```
Installation dependencies:
```bash
pip install -r requirements.txt
```
Please note that this project also requires the punkt package of [nltk_data](http://www.nltk.org/nltk_data/), please download and unzip it to `\\wsl.localhost\Ubuntu\home\tiansz\nltk_data\tokenizers\punkt` similar path.

Run the main program:
```bash
python3 main.py
```
The program will look for the 【Answer】 and 【Source】 of the question `Can this project run in colab` from the local `docs/FAQ.md` file



<br>

## example
question:
```
本项目能否在colab中运行
```
answer:
```
可以尝试使用 chatglm-6b-int4 模型在 colab 中运行。需要注意的是，如需在 colab 中运行 Web UI，需将webui.py中demo.queue(concurrency_count=3).launch(server_name='0.0.0.0', share=False, inbrowser=False)中参数share设置为True。

[Document(page_content="Q5: 本项目可否在 colab 中运行？ A5: 可以尝试使用 chatglm-6b-int4 模型在colab 中运行，需要注意的是，如需在 colab 中运行 Web UI，需将webui.py中demo.queue(concurrency_count=3).launch(\n    server_name='0.0.0.0', share=False, inbrowser=False)中参数share设置为True。", metadata={'source': './docs/FAQ.md', 'filename': 'FAQ.md', 'file_directory': './docs', 'filetype': 'text/markdown', 'page_number': 1, 'category': 'Title', 'score': 198})]
```

<br>

## references
[langchain-ChatGLM](https://github.com/imClumsyPanda/langchain-ChatGLM)
