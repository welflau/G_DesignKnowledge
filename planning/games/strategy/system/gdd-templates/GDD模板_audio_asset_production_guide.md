# GDD模板 · audio asset production guide

> 来源：wanghaisheng/openagenticgame-gdd
> 原始链接：https://github.com/wanghaisheng/openagenticgame-gdd/blob/master/templates/guides/audio_asset_production_guide.md
> 分类：system
> 标签：GDD, 系统设计, 模板

## 概述
工业化GDD模板章节：audio_asset_production_guide

## 正文
# 音频资产生产指南（BGM/SFX/VO）

## 能力与约束
- 载体：audio（WAV/OGG/MP3/Opus），BGM/SFX/VO。
- 目标：统一采样率/比特率/声道；循环点与淡入淡出规范。

## 输入规范
- 采样：48kHz（推荐），24bit 或 16bit；立体声/单声道按用途。
- 格式：BGM OGG/MP3、SFX WAV/OGG、VO WAV/OGG。
- 命名：MX_theme_loop.ogg、SX_footstep_gravel_01.wav、VO_hero_intro_zh.wav。

## 制作要点
- 音量与响度：目标 -16 ~ -20 LUFS（移动端可稍高）；峰值不剪裁。
- 循环与过渡：无缝循环点；淡入淡出时长与曲线统一。
- 频段与混音：关键事件时压低环境音；对白与提示优先。

## 多语言与本地化
- 语言包：文本/字典、语音文件、发音规范与审核。
- 字体/字符集：与 UI 同步，避免不支持字符。

## 校验与交付
- 校验：无噪点/爆音/失真；循环无跳点。
- 交付：母带（可选）、导出文件、循环点/淡入淡出标注、元数据（format=audio）。


## 策划参考价值
可直接套用的GDD框架，含15章完整体系。
