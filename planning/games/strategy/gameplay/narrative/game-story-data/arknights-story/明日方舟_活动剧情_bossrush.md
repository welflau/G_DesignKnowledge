# 明日方舟 · 活动剧情 · bossrush（5段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「bossrush」完整剧情脚本（5个文件，0行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/bossrush
- 脚本文件数：5

### bossrush_a

```
[HEADER(is_skippable=true, is_autoable=false)] 活动17side教学关_a

[PopupDialog(dialogHead="$avatar_doberm")] WAVE 1（第1/3波）
[Tutorial(focusX=110, focusY=-80, focusWidth=80, focusHeight=80, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_snakek", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
成功挑战本波BOSS之后，存档点解锁；再次进入关卡时可以开启，使我方单位在本波次中属性大幅提升


```

### bossrush_b

```
[HEADER(is_skippable=true, is_autoable=false)] 活动17side教学关_a

[PopupDialog(dialogHead="$avatar_doberm")] 危险区域即将出现，已经将部署于危险区域上的干员强制撤离并刷新再部署时间！
[PopupDialog(dialogHead="$avatar_doberm")] 接下来该区域中出现的敌人不会扣减关卡生命，击杀可以获得奖励，但再次部署于危险区域的干员，会在波次结束时强制撤离且再部署时间翻倍
```

### bossrush_c

```
[HEADER(is_skippable=true, is_autoable=false)] 活动17side教学关_a

[PopupDialog(dialogHead="$avatar_doberm")] 第一波次结束,下一波次即将开始!危险区域上的干员将被强制撤离！


```

### bossrush_d

```
[HEADER(is_skippable=true, is_autoable=false)] 活动17side教学关_a

[PopupDialog(dialogHead="$avatar_doberm")] WAVE 2 （第2/3波）


```

### bossrush_e

```
[HEADER(is_skippable=true, is_autoable=false)] 活动17side教学关_a

[PopupDialog(dialogHead="$avatar_doberm")] 最终WAVE （第3/3波）


```


## 统计

- 总字符数：1075
- 对话行数：0


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
