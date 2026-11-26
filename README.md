# 说英语 · 本地英语陪练

**一个完全跑在你自己电脑上的英语口语学习软件。**

大模型用本机 [Ollama](https://ollama.com/)，语音识别用 [faster-whisper](https://github.com/SYSTRAN/faster-whisper) 在本地完成，
你的录音、对话、学习记录**都不会上传到任何服务器**。断网也能用（除了语音合成会回落到系统语音）。

面向「能看懂简单句，但说不出口」的中文母语者：中文辅助、句子短、语速慢，每轮只纠一个最重要的错误。

![今日学习](assets/preview-home.png)

---

## 它和背单词 App 有什么不同

大部分工具帮你「认识」英语，这个工具逼你「说出来」：

- **每轮只纠一个错**：一次改三个错误人会崩溃，改一个才记得住。
- **说错就进错题本**：被纠正的句子自动入库，等你重写一遍才算巩固。
- **用今天的词开口**：新学的词不会停在卡片上，第二天就会被拉进对话里逼你用。
- **评分会区分「发音错」和「用词错」**：`think` 读成 `sink` 是口型问题，`think` 说成 `like` 是用词问题，
  系统用词库音标判断两者的远近，不会一律说你「读错词」。
- **做得不好的地方直接讲**：下面「已知限制」里写清楚了它抓不到什么。

---

## 功能一览（14 个页面）

| 分组 | 页面 | 做什么 |
|---|---|---|
| 学习 | **今日学习** | 每日计划、周报、连续天数、词汇量参考 |
| 学习 | **情景对话** | 30 个真实场景，AI 扮演店员/医生/面试官，每轮只挑一个错 |
| 学习 | **自由聊** | 不设角色随手聊；可挑「今天新学的词」，让语伴用起来再引导你说 |
| 学习 | **发音纠音** | 逐词五色标记（读对/发音不太准/词不对/漏读/没听清）+ 口型建议；40 组最小对立对 |
| 训练 | **背单词** | 间隔重复（SRS）+ 三种测验；4400 词分级词库 |
| 训练 | **地道口语** | 91 条「课本说法 → 母语者说法」、12 组功能句型、20 条连读弱读、影子跟读 |
| 训练 | **面试口试** | 11 类面试与考试，含 20 张雅思 Part 2 话题卡，四维评分 |
| 训练 | **精读听写** | 22 篇分级短文 + 可粘任意英文；逐句讲解 + 听写对比 |
| 资料 | **分级词库** | 4400 词按档位和考试标签筛选，批量加入复习 |
| 资料 | **精读文库** | 8 篇精选文章（原创 + 公版经典），可导出 Word / Markdown 分享 |
| 资料 | **错题本** | 自动收录被纠正的句子，按类型复练 |
| 资料 | **历史记录** | 回看每次对话、面试报告、跟读成绩曲线 |
| 系统 | **设置 / 使用说明** | 模型、音色、语速、水平、每日目标 |

<table>
<tr>
<td><img src="assets/preview-freetalk.png" alt="自由聊"></td>
<td><img src="assets/preview-library.png" alt="精读文库"></td>
</tr>
<tr>
<td align="center">自由聊：挑今天的词，逼你开口</td>
<td align="center">精读文库：可导出 Word 分享</td>
</tr>
<tr>
<td><img src="assets/preview-conversation.png" alt="情景对话"></td>
<td><img src="assets/preview-vocabulary.png" alt="背单词"></td>
</tr>
<tr>
<td align="center">情景对话：AI 演对方，每轮只纠一个错</td>
<td align="center">背单词：间隔重复 + 真实例句</td>
</tr>
<tr>
<td><img src="assets/preview-history.png" alt="历史记录"></td>
<td align="center"><i>练过的东西都在历史里，随时回看</i></td>
</tr>
</table>

---

## 快速开始

### 0. 前置条件：一个本地大模型

这个软件**本身不含模型**，推理交给 [Ollama](https://ollama.com/download)。

```bash
# 1) 安装 Ollama 后启动它（Windows 装完会自动常驻托盘）
# 2) 拉一个模型（约 4.7GB）
ollama pull qwen2.5:7b-instruct
```

显存 8GB 左右跑得很顺。显存小可以换：

```bash
ollama pull qwen2.5:3b-instruct   # 更小更快，质量差一些
ollama pull llama3.2              # 备选
```

> 换模型后，到软件「设置」里把模型名改成对应的值。

### 1. Windows（最简单）

1. 装 [Python 3.10+](https://www.python.org/downloads/)，安装时勾选 **Add Python to PATH**。
2. 双击 **`install.bat`** —— 自动建虚拟环境、装依赖（第一次 2–5 分钟）。
3. 双击 **`start.bat`** —— 浏览器自动打开 <http://127.0.0.1:8501>。

### 2. macOS / Linux

```bash
git clone https://github.com/<你的用户名>/<仓库名>.git
cd <仓库名>

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

streamlit run streamlit_app.py
```

### 3. 手动启动（任何系统）

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py --server.port 8501
```

### 第一次运行会发生什么

| 时机 | 现象 |
|---|---|
| 启动时 | 首次导入 4400 词到本地数据库，约 1 秒 |
| 第一次对话 | 要等 **20–30 秒**——那是模型加载进显存，之后每句 1–3 秒 |
| 第一次录音 | 自动下载语音识别模型（`small`，约 480MB），下完就不用了 |
| 第一次点「播放」 | 走 edge-tts 在线合成；断网会回落到系统语音 |

---

## 环境要求

| 项目 | 要求 | 说明 |
|---|---|---|
| Python | **3.10+** | 用到了 `X \| Y` 类型语法 |
| Ollama | 任意较新版本 | 需要至少一个模型；默认 `qwen2.5:7b-instruct` |
| 显存 | 6GB+ 体验较好 | 3–4GB 可换 3B 模型 |
| 磁盘 | 约 3GB | 依赖 ~1.5GB + 识别模型 480MB + 词库 |
| 浏览器 | Chrome / Edge / Firefox 新版 | 录音需要 `localhost` 或 HTTPS |
| ffmpeg | **可选** | 只用于显示音频时长，没有会自动跳过 |

> **录音的两个坑**：① 浏览器只在 `localhost` 或 `https` 下允许麦克风，用局域网 IP 打开会静默失效；
> ② 手机浏览器同理。这两种情况都可以在页面上切到「上传音频文件」。

---

## 内容规模

| 内容 | 规模 | 来源 |
|---|---|---|
| 分级词库 | **4400 词**（A1 878 / A2 1483 / B1 1080 / B2 959），每词都有音标、释义、例句 | ECDICT + Tatoeba |
| 跟读句库 | 192 句，9 类发音重点 | 手写 + 模型生成后校验 |
| 最小对立对 | 40 组（ship/sheep、bad/bed…） | 手写 |
| 情景对话 | 30 个场景 | 手写 |
| 面试口试 | 11 类 + 20 张话题卡 | 手写 |
| 地道表达 | 91 条替换 + 12 组功能句型 + 20 条连读弱读 + 12 句影子跟读 | 手写 |
| 精读文章 | 22 篇分级短文 | 模型生成 + 校验 |
| 精读文库 | 8 篇（4 篇原创 + 4 篇公版经典） | 原创 + 公有领域 |

内容都在 `content/*.json` 里，**加内容不用改代码**。

---

## 目录结构

```
说英语/
├── start.bat / install.bat      # Windows 双击启动 / 安装
├── streamlit_app.py             # 入口：侧边栏导航
├── app_pages/                   # 14 个页面（只负责渲染）
├── core/                        # 业务逻辑
│   ├── config.py   llm.py       #   设置、Ollama 客户端
│   ├── coach.py    prompts.py   #   教学动作与提示词
│   ├── asr.py      tts.py       #   语音识别 / 合成
│   ├── scoring.py  phonetics.py #   发音评分、逐词对齐、音近判断
│   ├── planner.py  db.py        #   今日计划、周报、SQLite
│   ├── export.py   content.py   #   文档导出、内容加载
│   └── ui.py       seed.py      #   通用组件、首次导入
├── content/                     # 全部学习内容（JSON）
├── assets/                      # 图标与预览图
├── tools/                       # 内容管线与自检脚本
└── data/                        # 运行时生成（不进仓库）
    ├── app.db                   #   你的学习数据
    ├── audio_cache/             #   合成语音缓存
    └── models/whisper/          #   识别模型
```

---

## 数据来源与许可

**代码以 [MIT](LICENSE) 发布**，但词库和例句来自开放数据，各有各的许可，
二次分发请保留 [ATTRIBUTION.md](ATTRIBUTION.md)：

- 词库音标/释义/词频/考试标签：**ECDICT**（MIT）
- 真实语料例句：**Tatoeba** cmn-eng（CC BY 2.0）
- 精读文库中的经典片段：**公有领域**（O. Henry / Lewis Carroll / Conan Doyle / Aesop）
- 部分例句和释义由 **Qwen2.5**（Apache-2.0）在本地生成

---

## 常见问题

**左侧显示「模型离线」**
Ollama 没启动。开始菜单里打开它，等托盘出现图标，再点设置里的「刷新模型列表」。

**对话很慢**
7B 模型在 8GB 显卡上每句 1–3 秒。更慢的话：设置里把上下文长度调到 3072、换 3B 模型、或关掉其他占显存的程序。

**录音没反应 / 麦克风用不了**
① 浏览器没给麦克风权限；② 通过局域网 IP 访问（浏览器只在 localhost/https 下允许录音）；
③ 电脑没有麦克风。**三种情况都可以把录音控件切到「上传音频文件」**，wav/mp3/m4a/ogg/webm 都支持。

**识别不准**
设置里把识别模型从 `small` 换成 `medium`（更准更慢），或反过来换 `base`（更快）。

**能局域网给手机用吗**
可以，但录音用不了（非 https），只能打字或用上传：
```bash
streamlit run streamlit_app.py --server.address 0.0.0.0 --server.port 8501
```

---

## 开发

### 跑测试

```bash
python tools/selftest.py --no-model   # 内容完整性、数据库、SRS、评分、计划（不需要模型）
python tools/selftest.py              # 加上模型、语音合成、语音识别
python tools/smoke_pages.py           # 15 个页面能不能渲染
python tools/smoke_flows.py           # 有状态的界面流程
python tools/check_icons.py           # 校验 Material 图标名（写错会整页崩）
```

### 重建内容

```bash
pip install -r requirements-dev.txt

python tools/build_wordbank.py       # 从 ECDICT + Tatoeba 重建 4400 词（自动下载原始数据）
python tools/fill_examples.py        # 给没有例句的词补例句
python tools/fix_meanings.py         # 重排高频词释义（词典首义常常是错的义项）
python tools/gen_content.py          # 生成精读文章和跟读句
```

### 加内容不用改代码

`content/` 下的 JSON 都是「加一条就生效」：

```jsonc
// content/scenes.json
{
  "id": "new_scene",
  "name": "场景名",
  "icon": "store",
  "role": "你扮演的角色（如：店员）",
  "learner": "学员扮演的角色（如：顾客）",
  "brief": "给模型看的场景说明",
  "desc_cn": "给学员看的一句话",
  "phrases": ["店员会说的句子"],
  "starters": ["开场白"]
}
```

---

## 已知限制

写在这里，是因为它们真的存在：

1. **发音评分基于转写文本，不是音素级比对。**
   识别模型会自动「纠正」一些模糊发音（实测把读错的 `sink` 直接听成 `think`，置信度 0.99），
   所以**极细微的口音差别抓不到**。它能稳定抓到的是：读成了别的词、漏读、语速、停顿。
   想测音素级发音，需要换 wav2vec2 + GOP 那一套（本项目没做）。
2. **约 1300 条例句是模型生成的**，其中少数语感一般。带 `example_source: "ai"` 标记，可自行筛查。
3. **7B 模型的点评偶尔会过度纠正**（把完全正确的句子改得更啰嗦）。提示词里已经在约束，但无法根除。
4. **语音合成依赖微软在线接口**（edge-tts），这是本项目唯一的联网点。断网会自动回落系统语音。
5. **只有单用户**，没有账号、没有云同步——这是刻意的，数据就该留在自己电脑里。

---

## 许可

代码 [MIT](LICENSE) · 内容与第三方数据见 [ATTRIBUTION.md](ATTRIBUTION.md)

如果这个项目帮到你，欢迎 star ⭐ 或提 issue 告诉我哪里不好用。