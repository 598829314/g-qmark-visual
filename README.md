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
- 可爱来自人物比例、Q Cat 的动作和小细节，不使用夸张萌化或表情包式表演。
- 技术感通过真实设备、Agent 节点、文件、模型、流程关系和数据表达，而不是依赖赛博朋克装饰。

## 固定身份资产

### `G_QMark` / `G_Q` / `G?`

- `G_QMark` 是正式项目与视觉系统名称。
- `G_Q` 是核心人格化短标：它像一个正在轻轻揉惺忪睡眼的极简表情，安静、有点困，但已经开始工作。
- `G?` 是 favicon、微型图标和衍生动效可用的次级抽象符号，不是唯一主标识。

The core short mark is `G_Q`, treated as a sleepy, calm emoticon-like identity rather than a purely abstract logo.

v1 已提供主标、反白、正式字标和一次性揉眼动效 SVG，见 [`assets/identity/`](./assets/identity/)。固定黄色仍是整套视觉系统的重复记号，可用于章节编号、流程节点、光标、状态提示和小型强调元素。

### Wenhao

简化人物角色，用于代表“我”或内容讲述者。固定识别特征：

- 黑色短发
- 简洁眼镜
- 深灰或黑色上衣
- 小型金黄色吊坠
- 约 1:3.5–1:4 的轻度卡通比例
- 表情克制，保持编辑插画感

### Q Cat

Q Cat 是奶灰色小猫，用于表示问题、AI、Agent、好奇心和处理状态。

- 奶灰身体、暖白肚皮
- 极简深灰线稿
- 尾巴自然卷成 `?`
- 黄色小圆牌或小色块作为固定识别点
- 可以趴在设备、窗口、进度条和文件夹上，但不抢占主体信息

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

用于人物、Q Cat、设备和小场景。先在纯色键控背景生成，再使用原项目保留的 `scripts/cutout.py` 输出透明 PNG，方便放进视频、网页、卡片或其他版式。

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
Use $g-qmark-visual to create a transparent Q Cat illustration for a video overlay.
The cat is resting on a progress bar while an Agent is working.
```

完整生成规则、提示词结构和交付检查见 [`SKILL.md`](./SKILL.md)。

## 仓库结构

```text
assets/
  identity/            G_Q 核心短标、G_QMark 正式字标与次级 G? 符号
  characters/wenhao/  Wenhao 人物资产
  mascot/q-cat/        Q Cat 资产
  icons/               设备、Agent、模型和工作流图标
  readme/              README 相关素材
examples/              示例；当前仍保留部分上游示例作为参考
prompts/               可复用生成提示词和场景模板
scripts/               通用处理脚本
```

当前 v1 已完成确定性的 `G_Q` SVG 身份资产。Wenhao、Q Cat 和图标仍先以母版规则约束，待各自视觉方案确认后再加入正式图片。旧 `oil-visual` 示例素材暂时保留作为上游参考，后续再逐步替换。

## Upstream

本项目 Fork 自 [`oil-oil/oil-visual`](https://github.com/oil-oil/oil-visual)。原项目由 Zhihuang Lin 创建，并以 MIT License 发布。

## License

[MIT](./LICENSE)
