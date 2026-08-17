# Prompt Library

这里用于存放已经验证过、可重复使用的生成提示词，不把一次性对话提示词直接当作正式模板。

## 当前母资产探索模板

- [`identity-logo.md`](./identity-logo.md) — `G_Q` 选定骨架微调
- [`wenhao-character.md`](./wenhao-character.md) — Wenhao 小火柴人母版与姿态表
- [`golden-pup-character.md`](./golden-pup-character.md) — 金毛幼犬母版与场景姿态

这些模板都处于“探索”阶段。生成结果必须经过人工确认，才能进入 `assets/` 成为正式母资产。

## 后续模板

后续再按用途补充：

```text
explainer-scene.md
transparent-asset.md
video-overlay.md
motion-scene.md
```

正式模板应引用 `SKILL.md`、`DESIGN.md` 和对应 `assets/**/MASTER.md` 的固定规则，只描述本次场景的变量，避免每个提示词重复维护整套视觉规范。
