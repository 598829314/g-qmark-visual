# G_QMark Visual

<p align="center">
  <img src="./assets/identity/gqmark-primary.svg" width="360" alt="G_QMark sleepy G_Q identity mark">
</p>

`g-qmark-visual` 是一套面向个人视频、技术解释和数字内容制作的视觉规范。它从 [`oil-oil/oil-visual`](https://github.com/oil-oil/oil-visual) Fork 而来，保留原项目把角色、构图、颜色和生成流程固化为 Agent Skill 的方法，并改造成属于 G_QMark 的视觉资产系统。

它不是单独的一种“画风”，而是一套可以持续扩展的个人视觉语言：固定标识、人物、吉祥物、色彩、图形规则，以及适合解释图和透明视频素材的生产方式。

## 视觉方向

整体风格：**明亮、安静、略困、圆润、克制地可爱、带一点技术内容。**

- 使用暖米白背景和大面积留白，不依赖深色科技背景。
- 以深灰线稿和柔和扁平色块构成画面，避免强渐变、霓虹和复杂 3D。
- 信息结构保持规整，允许箭头、标签、窗口和设备带轻微手绘感。
- 可爱来自小火柴人的短比例、金毛幼犬的动作和少量细节，不使用夸张萌化或表情包式表演。
- 技术感通过真实设备、Agent 节点、文件、模型、流程关系和数据表达，而不是依赖赛博朋克装饰。

## 固定身份资产

### `G_QMark` / `G_Q` / `G?`

- `G_QMark` 是正式项目与视觉系统名称。
- `G_Q` 是核心人格化短标：它像一个正在轻轻揉惺忪睡眼的极简表情，安静、有点困，但已经开始工作。
- `G?` 是 favicon、微型图标和衍生动效可用的次级抽象符号，不是唯一主标识。

The core short mark is `G_Q`, treated as a sleepy, calm emoticon-like identity rather than a purely abstract logo.

v1 已提供主标、反白、正式字标和一次性揉眼动效 SVG，见 [`assets/identity/`](./assets/identity/)。固定黄色仍是整套视觉系统的重复记号，可用于章节编号、流程节点、光标、状态提示和小型强调元素。

### Wenhao

Wenhao 是矮小的简笔线条火柴人，用于代表“我”或内容讲述者。

- 圆头、短身体和短四肢，总高约 2.5–3 个头
- 几笔黑色短发、极简眼镜和微困表情
- 小块深色上衣，不佩戴项链或吊坠
- 不画成高挑火柴人，也不画成完整卡通人物

### Golden Pup

Golden Pup 是圆乎乎的金毛幼犬，用于表示陪伴、好奇、等待、观察和轻量状态反馈。

- 头身连成低矮豆子形，几乎没有脖子
- 宽软的半圆垂耳、极短手脚和小卷尾巴
- 点状五官、奶油色小嘴部和暖金黄色身体
- 一条没有吊牌和铃铛的细暖红色项圈
- 与小火柴人相同的粗圆极简深灰线条
- 可以趴在设备、窗口、进度条和文件夹旁，但不抢占主体信息

## 基础配色

| 用途 | 色值 |
| --- | --- |
| 暖米白背景 | `#FFFDF7` |
| 卡片白 | `#FFFFFF` |
| 主文字 / 线稿 | `#30343B` |
| 次级线稿 | `#60656F` |
| 标识黄 | `#F2C94C` |
| 天空蓝 | `#8EC5E8` |
| 鼠尾草绿 | `#A9C8A5` |
| 淡橙 | `#F2A66F` |
| 淡紫 | `#B9A7D8` |

详细规则见 [`DESIGN.md`](./DESIGN.md)。

## 输出模式

### Mode A：完整解释图

用于概念、机制、流程、对比和数据关系。图片本身应能在约 10 秒内表达主要关系，可以包含少量准确标签。

### Mode B：透明视频素材

用于小火柴人、Golden Pup、设备和小场景。先在纯色键控背景生成，再使用原项目保留的 `scripts/cutout.py` 输出透明 PNG，方便放进视频、网页、卡片或其他版式。

## 安装

```bash
git clone https://github.com/598829314/g-qmark-visual.git ~/.codex/skills/g-qmark-visual
```

重启 Codex 后可以直接点名使用：

```text
Use $g-qmark-visual to explain why a sparse local model can generate faster than a dense model.
Use short, exact Chinese labels and the bright G_QMark visual language.
```

```text
Use $g-qmark-visual to create a transparent Golden Pup illustration for a video overlay.
The golden retriever puppy is resting beside a progress bar while an Agent is working.
```

完整生成规则、提示词结构和交付检查见 [`SKILL.md`](./SKILL.md)。

## 仓库结构

```text
assets/
  identity/            G_Q 核心短标、G_QMark 正式字标与次级 G? 符号
  characters/wenhao/  Wenhao 小火柴人资产
  mascot/golden-pup/   金毛幼犬资产
  icons/               设备、Agent、模型和工作流图标
  readme/              README 相关素材
examples/              示例；当前仍保留部分上游示例作为参考
prompts/               可复用生成提示词和场景模板
scripts/               通用处理脚本
```

当前 v1 已完成确定性的 `G_Q` SVG 身份资产。Wenhao 小火柴人、Golden Pup 和图标仍先以母版规则约束，待各自视觉方案确认后再加入正式图片。旧 `oil-visual` 示例素材暂时保留作为上游参考，后续再逐步替换。

## Upstream

本项目 Fork 自 [`oil-oil/oil-visual`](https://github.com/oil-oil/oil-visual)。原项目由 Zhihuang Lin 创建，并以 MIT License 发布。

## License

[MIT](./LICENSE)
