# 第三方数据与素材的来源与许可

本项目的**代码**以 MIT 许可发布（见 [LICENSE](LICENSE)）。
但这不等于本仓库里的一切都由我原创 —— 词库、例句、经典文本分别来自不同的来源，
下面逐项说明。如果你要二次分发，请把这份说明一起带上。

---

## 1. 词库 `content/wordbank.json`（4400 词）

音标、中文释义、词性、词频、柯林斯星级、牛津核心标记、考试标签（中考/高考/四级/六级/考研/雅思/托福）
来自 **ECDICT**：

- 项目：<https://github.com/skywind3000/ECDICT>
- 许可：**MIT**
- 我们做的处理：重新排序/规范化音标、按词频分档（A1-B2）、用模型重写高频词的中文释义（474 条）

> 释义被重写的词保留了 `meaning_original` 字段，原始释义仍可追溯。

## 2. 单词例句

### 2.1 真实语料例句

来自 **Tatoeba** 的中英句对（ManyThings 整理的 `cmn-eng.zip`）：

- 项目：<https://tatoeba.org/> · <https://www.manythings.org/anki/>
- 许可：**CC BY 2.0 FR**（署名）
- 我们做的处理：为每个词挑一句最短最自然的句子、繁体转简体

### 2.2 模型生成的例句

其余单词的例句由本地大模型生成（`tools/fill_examples.py`），属于机器生成内容，
已做基本校验（含该词、长度、纯英文、有中文翻译），但**不保证全部符合母语者语感**。
这类词条带有 `"example_source": "ai"` 字段，可以据此筛选。

## 3. 精读文库中的经典片段 `content/readings.json`

以下文本已进入**公有领域**（
美国：1930 年前出版；作者逝世超过 70 年的司法辖区同样适用）：

| 篇目 | 作者 | 首次出版 |
|---|---|---|
| The Gift of the Magi | O. Henry（1862–1910） | 1905 |
| Alice's Adventures in Wonderland | Lewis Carroll（1832–1898） | 1865 |
| A Scandal in Bohemia | Arthur Conan Doyle（1859–1930） | 1891 |
| The Tortoise and the Hare（伊索寓言，英文改写） | Aesop（古希腊） | — |

其余 4 篇（The Two-Minute Rule / Why Small Talk Matters /
How to Say No Without Being Rude / Learning to Be Bad at Things）为本项目原创，
中文翻译与讲解同样是原创。

## 4. 内容由模型辅助生成的部分

`tools/gen_content.py`、`tools/fill_examples.py`、`tools/fix_meanings.py`
使用本地部署的 **Qwen2.5-7B-Instruct** 生成或改写文本：

- 模型：<https://huggingface.co/Qwen/Qwen2.5-7B-Instruct>
- 许可：**Apache-2.0**

## 5. 运行时依赖（不由本仓库分发）

| 组件 | 用途 | 许可 |
|---|---|---|
| [Streamlit](https://streamlit.io/) | 界面框架 | Apache-2.0 |
| [Ollama](https://ollama.com/) + 本地大模型 | 对话与点评推理 | MIT / 各模型自己的许可 |
| [faster-whisper](https://github.com/SYSTRAN/faster-whisper) · CTranslate2 | 本地语音识别 | MIT |
| [edge-tts](https://github.com/rany2/edge-tts) | 语音合成（调用微软在线接口） | GPL-3.0（本项目仅调用，不修改） |
| [python-docx](https://python-docx.readthedocs.io/) | 导出的 Word 文档 | MIT |
| [pydub](https://github.com/jiaaro/pydub) | 音频时长 | MIT |
| [Material Symbols](https://fonts.google.com/icons) | 界面图标 | Apache-2.0 |
| [Whisper small](https://huggingface.co/Systran/faster-whisper-small) | 识别模型权重（首次运行自动下载） | MIT |

## 6. 语音合成与隐私

- **语音识别**（faster-whisper）完全在本机完成，音频不出本地。
- **语音合成**（edge-tts）会把你输入/生成的英文句子发到微软的在线接口。
  断网或接口不可用时，程序会自动回落到 Windows 自带的 SAPI 语音。
  如果你需要完全离线，可以在 `data/settings.json` 里关掉在线语音
  （或自己接一套本地 TTS）。

---

如果你认为本仓库的某处内容侵犯了你的权利，请开 issue 说明，我会尽快处理。