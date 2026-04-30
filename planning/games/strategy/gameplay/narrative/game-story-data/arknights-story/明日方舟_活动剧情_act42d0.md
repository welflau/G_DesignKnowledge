# 明日方舟 · 活动剧情 · act42d0（2段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act42d0」完整剧情脚本（2个文件，0行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act42d0
- 脚本文件数：2

### guide_act42d0_effect

```
[HEADER(is_skippable=false, is_tutorial=true)] act42d0增益引导
[Tutorial(waitForSignal="act42d0_effect_view_routed")]
[Tutorial(target="pool_act42d0_buff_list_graphic", animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_sys")] 右侧为战备增益列表，选择后可加载增益，已选增益的对应效果在增益详情中显示。
[Tutorial(focusX=-245, focusY=130, focusWidth=420, focusHeight=114, anchor="BottomRight",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_sys")] 加载增益将降低一定的拟真度。请注意，拟真度的降低情况将会导致拟真等级的下降。
[Tutorial(focusX=192, focusY=-266, focusWidth=352, focusHeight=45, anchor="Left",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_sys")] 首次通过模拟作战将取得试验数据集。拟真等级的下降会导致最终取得的试验数据集减少。详细情况可点击此处查看。
[Tutorial(focusX=-670, focusY=35, focusWidth=362, focusHeight=70, anchor="BottomRight",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_sys")] 点击此处可关闭战备增益，以最高拟真等级还原真实战场。
[Tutorial(focusX=-245, focusY=37, focusWidth=490, focusHeight=72, anchor="BottomRight",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_sys")] 战场实境已构建完毕。博士，请开始模拟作战。
```

### guide_act42d0_map

```
[HEADER(is_skippable=false, is_tutorial=true)] act42d0地图引导
[Tutorial(waitForSignal="act42d0_map_routed")]
[Tutorial(target="pool_act42d0_first_unlock_area", waitForSignal="act42d0_map_area_selected", searchBtnInChildren=true, focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Click", protectTime=0.5, dialogHead="$avatar_sys")] 本次拟构战场中共包含C/B/A/S四片交战区域，区域内模拟作战的强度依次递增。只有完成前一片区域的模拟试验，才能解锁下一片区域。
[Tutorial(focusX=-170, focusY=-10, focusWidth=350, focusHeight=500, anchor="Right",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_sys")] 同一交战区域内存在三处模拟作战，作战难度依次提升，第三处为转折点作战。区域内的模拟作战彼此并无关联，可任意挑战。
[Tutorial(target="pool_act42d0_last_stage_in_current_area", waitForSignal="act42d0_map_stage_selected", searchBtnInChildren=true, focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Click", protectTime=0.5, dialogHead="$avatar_sys")] 随着交战区域的推进，区域内模拟作战的难度也会增加。此处显示的即是难度提升的详情。
[Tutorial(focusX=192, focusY=-230, focusWidth=315, focusHeight=42, anchor="Left",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_sys")] 不启用战备增益，以最高拟真等级完成转折点作战可解锁下一交战区域。
[Tutorial(target="pool_act42d0_btn_start_battle", searchBtnInChildren=true, focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=0.5, dialogHead="$avatar_sys")] 战场实境已构建完毕。博士，请开始模拟作战。
```


## 统计

- 总字符数：2828
- 对话行数：0


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
