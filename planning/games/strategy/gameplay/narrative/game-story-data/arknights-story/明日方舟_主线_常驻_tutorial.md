# 明日方舟 · 主线/常驻 · tutorial（240段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 主线/常驻, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟主线/常驻「tutorial」完整剧情脚本（240个文件，0行对话）

## 正文
## 章节信息

- 分类：主线/常驻
- 目录：obt/tutorial
- 脚本文件数：240

### guide_01_a

```
[HEADER(is_tutorial=true)] 引导关卡1_a

[Battle.Pause]

[PopupDialog(dialogHead="$avatar_amiya")] 博士，时间虽然很紧迫，不过不要担心，我会让你在离开这里前恢复基本的行动力……

[Tutorial(focusX=520, focusY=-56, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amiya")] \
敌人<@tu.kw>会从这里出现</>。

[Tutorial(focusX=-520, focusY=-56, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amiya")] \
我们不能让他靠近你，因此<@tu.kw>不要让他们靠近这个位置</>。

[PopupDialog(dialogHead="$avatar_amiya")] 他们接近了，准备好。

```

### guide_01_b

```
[HEADER(is_tutorial=true)] 引导关卡1_b

[Battle.Pause]

// 介绍：敌人
[Tutorial(focusX=390, focusY=-50, focusWidth=100, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amiya")] \
这是需要消灭的<@tu.kw>敌人</>。
[Tutorial(focusX=390, focusY=-50, focusWidth=100, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amiya")] \
他是“整合运动”的破坏分子。不击溃他的话会有大麻烦......
// 介绍：角色卡片
[Battle.UnlockFunction(mask="CARD_LIST")]
[Tutorial(focusX=-120, focusY=70, focusWidth=250, focusHeight=140, anchor="BottomRight", \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amiya")] \
而下方展示了待命中的罗德岛<@tu.kw>干员列表</>。

[Tutorial(focusX=-120, focusY=70, focusWidth=250, focusHeight=140, anchor="BottomRight", \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amiya")] \
只要将他们部署到场上，就可以参与作战行动。
// 介绍：费用
[Battle.UnlockFunction(mask="COST_PANEL")]
[Tutorial(target="panel_cost", \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amiya")] \
列表上方的数字代表着目前的<@tu.kw>部署费用</>。

[Tutorial(target="panel_cost", \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amiya")] \
只有当部署费用足够的情况下，才可以在战场中部署干员。

[Tutorial(focusX=-178, focusY=110, focusWidth=50, focusHeight=50, anchor="BottomRight", \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amiya")] \
大家头顶的数字代表了部署<@tu.kw>需要消耗的费用</>。
[PopupDialog(dialogHead="$avatar_amiya", black="$f_tut_black", protectTime=0.5)] \
通常情况下，能力越强的干员，所花费的费用也越高。
[PopupDialog(dialogHead="$avatar_amiya", black="$f_tut_black", protectTime=0.5)] \
不过不用担心，部署费用会<@tu.kw>随着游戏时间逐渐增加</>。

[PopupDialog(dialogHead="$avatar_amiya")] 现在，博士的手指应该已经恢复知觉了。
[PopupDialog(dialogHead="$avatar_amiya")] 把注意力集中到手指上试试吧，任何一根。
[InputBlocker(blockInput=false)]
[Battle.EnsureMinCost(cost=11)]
[Tutorial(waitForSignal="put_down", dialogHead="$avatar_amiya", animStyle="Drag", \
          startX=-180, startY=60, startAnchor="BottomRight", endX=-60, endY=-65)] \
博士看到我标注的位置了吗？把干员的标签<@tu.kw>拖到那里</>。
[Tutorial(waitForSignal="select_direction", dialogHead="$avatar_amiya", animStyle="Drag", \
          startX=-60, startY=-45, endX=240, endY=-45)] \
然后将中央的方向指示块<@tu.kw>拖向这个方向</>。
[InputBlocker(blockInput=true)]

[Battle.Pause(pause=false)]
[Delay(time=1)]
[Battle.Pause(pause=true)]

[PopupDialog(dialogHead="$avatar_amiya")] 好了，德克萨斯干员已经完成了部署。她能帮助你清除大部分的威胁。

```

### guide_01_c

```
[HEADER(is_tutorial=true)] 引导关卡1_c

[Battle.Pause(pause=false)]
[Delay(time=1)]
[Battle.Pause(pause=true)]

[PopupDialog(dialogHead="$avatar_amiya")] 啊小心，有新的敌人。

[Battle.EnsureMinCost(cost=14)]

[InputBlocker(blockInput=false)]
[Tutorial(waitForSignal="put_down", dialogHead="$avatar_amiya", animStyle="Drag", \
          startX=-63, startY=60, startAnchor="BottomRight", endX=55, endY=65)] \
为了确保安全，现在需要放置一个<@tu.kw>远程单位</>到场地当中。
[Tutorial(waitForSignal="select_direction", dialogHead="$avatar_amiya", animStyle="Drag", \
          startX=55, startY=65, endX=355, endY=65)] \
能天使是一名狙击干员，她可以在远处攻击敌方单位，来帮助德克萨斯稳固阵线。目前来看门外的那些人已经无法进入了。
[InputBlocker(blockInput=true)]

[Battle.Pause(pause=false)]
[Delay(time=1)]
[Battle.Pause(pause=true)]

[PopupDialog(dialogHead="$avatar_amiya")] 好了，现在博士需要静观其变，冷静等待战场的下一步变化。
[PopupDialog(dialogHead="$avatar_amiya")] 虽然博士的身体还不适合战斗，但通过这样的合理指挥就能够保护大家。

```

### guide_01_d

```
[HEADER(is_tutorial=true)] 引导关卡1_d

[Battle.Pause]

[PopupDialog(dialogHead="$avatar_amiya")] 啊对了，博士你应该还有不少疑问。
[PopupDialog(dialogHead="$avatar_amiya")] 这里还有一些最基本的界面信息。

[Battle.UnlockFunction(mask="PAUSE_BUTTON")]
[Tutorial(focusX=-83, focusY=-57, focusWidth=113, focusHeight=106, anchor="TopRight", \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
右上方是暂停按钮，点击可以<@tu.kw>暂停或继续</>。

[Battle.UnlockFunction(mask="SPEED_SWITCHER_BUTTON")]
[Tutorial(target="btn_speed_level", \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
暂停按钮左方是变速按钮，可以<@tu.kw>调整当前的速度</>。

[Battle.UnlockFunction(mask="BATTLE_STATUS")]
[Tutorial(focusX=87, focusY=-31, focusWidth=105, focusHeight=45, anchor="Top", \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
屏幕上方是战斗基本信息，<@tu.kw>总生命值</>代表了蓝色目标点最多承受的敌人数量。

[Tutorial(focusX=-98, focusY=-30, focusWidth=124, focusHeight=52, anchor="Top", \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
<@tu.kw>敌方信息</>代表敌人的总数和已击败的敌人数量。

[PopupDialog(dialogHead="$avatar_amiya")] 了解清楚这些，应该能对博士更有帮助。

```

### guide_02_a

```
[HEADER(is_tutorial=true)] 引导关卡2_a

[Battle.Pause]

[PopupDialog(dialogHead="$avatar_amiya")] 大家原本以为“整合运动”只是一个无纪律的感染者团体。
[PopupDialog(dialogHead="$avatar_amiya")] 但是他们现在已经在组织有序的进攻了。
[PopupDialog(dialogHead="$avatar_amiya")] 准备好，迎击敌人的下一步进攻。

```

### guide_02_b

```
[HEADER(is_tutorial=true)] 引导关卡2_b

[Battle.Pause]

[Battle.EnsureMinSp(charId="char_102_texas", sp=100)]
[Tutorial(focusX=-152, focusY=62, focusWidth=100, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amiya")] \
德克萨斯能够同时使用更多的武器对周围的敌人造成伤害。

[Tutorial(focusX=-152, focusY=62, focusWidth=100, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amiya")] \
不过同时启动这么多的武器并不是一件容易的事情，博士需要告诉她正确的时机。

[Battle.UnlockFunction(mask="CHARACTER_INFO")]
[Battle.UnlockFunction(mask="CHARACTER_MENU")]

[PopupDialog(dialogHead="$avatar_amiya")] 当有足够多的敌人靠近她时，点击她的位置，选择她的<@tu.kw>技能</>标签以提醒她使用技能。

[Tutorial(focusX=-152, focusY=62, focusWidth=100, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amiya")] \
还有，在这个时候你也可以查看她的信息来了解她的数据。

[InputBlocker(blockInput=true, validX=-166, validY=45, validWidth=100, validHeight=80)]
[Tutorial(waitForSignal="char_info", focusX=-152, focusY=62, focusWidth=100, focusHeight=100, \
          animStyle="Click", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amiya")] \
教官曾告诉过我，每知道大家的一项指标就能够多为自己延长11.45秒的生存时间，虽然不知道是不是真的。
[InputBlocker(blockInput=true)]

[Tutorial(focusX=42, focusY=50, focusWidth=60, focusHeight=20, anchor="Left", \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amiya")] \
<@tu.kw>阻挡</>代表了该单位最多所能阻拦的敌人数量。

[Tutorial(target="btn_withdraw", \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amiya")] \
<@tu.kw>撤退</>按钮则会召回干员，该干员会回到待命列表中，一定时间后可以再度部署。

[Tutorial(target="btn_withdraw", \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amiya")] \
撤退的同时会<@tu.kw>返还一定的部署点数</>。不过如果干员被击败则无法返还。

[Tutorial(target="btn_skill",  waitForSignal="use_skill", \
          animStyle="Click", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amiya")] \
是时候使用<@tu.kw>技能</>了。

[InputBlocker(blockInput=true)]
[Battle.Pause(pause=false)]

[Delay(time=3)]
[Battle.Pause]

[PopupDialog(dialogHead="$avatar_amiya")] 太好了。
[PopupDialog(dialogHead="$avatar_amiya")] 就像刚才这样，在合适的时机对干员作出指示是指挥作战行动的关键。
[PopupDialog(dialogHead="$avatar_amiya")] 但是还不可放松警惕。如果博士在这里就倒下的话，我们就前功尽弃了。

```

### guide_02_c

```
[HEADER(is_tutorial=true)] 引导关卡2_c

[PopupDialog(dialogHead="$avatar_doberm", animStyle="NoWait")] 阿米娅，这边也有敌人。
[PopupDialog(dialogHead="$avatar_amiya", animStyle="NoWait")] 啊！杜宾教官，你来了！
[Delay(time=4)]

```

### guide_02_d

```
[HEADER(is_tutorial=true)] 引导关卡2_d

[Battle.Pause]

[PopupDialog(dialogHead="$avatar_amiya")] 啊不好......杜宾教官正在陷入苦战。

[Tutorial(focusX=103, focusY=-32, focusWidth=160, focusHeight=167, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amiya")] \
整合运动的重装防御者身着防护盔甲，普通的物理攻击难以对其造成伤害。

```

### guide_02_e

```
[HEADER(is_tutorial=true)] 引导关卡2_e

[Battle.Pause]


[PopupDialog(dialogHead="$avatar_amiya")] 博士，请把他交给我来对付！

[PopupDialog(dialogHead="$avatar_amiya")] 我是术师，能使用法术穿透敌人的防御。
[PopupDialog(dialogHead="$avatar_amiya")] 针对敌方的重甲单位是再好不过了。


[Battle.EnsureMinSp(charId="char_002_amiya", sp=100)]

```

### guide_02_f

```
[HEADER(is_tutorial=true)] 引导关卡2_f

[Battle.Pause]

[PopupDialog(dialogHead="$avatar_amiya")] 对！就是这样，将大家部署至适合她们的位置也是战术的重要一环。
[PopupDialog(dialogHead="$avatar_amiya")] …………
[PopupDialog(dialogHead="$avatar_amiya")] 博士，注意，更难对付的敌人正在靠近。

```

### guide_02_g

```
[HEADER(is_tutorial=true)] 引导关卡2_g

[Battle.Pause]

[PopupDialog(dialogHead="$avatar_amiya")] 小心。从后方来的是敌人的装备精良的单位，拥有不可小觑的破坏力。
[PopupDialog(dialogHead="$avatar_amiya")] 立即部署重装干员就能阻挡这些难缠的敌人。

```

### guide_02_h

```
[HEADER(is_tutorial=true)] 引导关卡2_g

[Battle.Pause]

[PopupDialog(dialogHead="$avatar_amiya")] 额外的罗德岛干员已经部署完毕，建议立即下达进攻指令。

[Battle.EnsureMinSp(charId="char_107_liskam", sp=100)]
[Battle.EnsureMinSp(charId="char_103_angel", sp=100)]

```

### guide_02_i

```
[HEADER(is_tutorial=true)] 引导关卡2_g

[Battle.Pause]

[PopupDialog(dialogHead="$avatar_amiya")] 太好了。
[PopupDialog(dialogHead="$avatar_amiya")] 虽然博士现在刚恢复，但如此短的时间就能够掌握这一切......
[PopupDialog(dialogHead="$avatar_amiya")] 休息一下吧，接下来......还有更重要的事情等着我们。


```

### legion_tr01_a

```
[HEADER(is_tutorial=true)] 爬塔教学关卡01_a

[Battle.LockFunction(mask="SYSTEM_MENU_INTERACT")]
[Battle.Pause]

[PopupDialog(dialogHead="$avatar_jesica")] 我无法击破敌人的装甲！请求火力支援！
[PopupDialog(dialogHead="$avatar_doberm")] 杰西卡，干得不错。经历了这么多次模拟作战，还是有所成长的。
[PopupDialog(dialogHead="$avatar_jesica")] 唉!？
[PopupDialog(dialogHead="$avatar_doberm")] 呼叫守林人，T032<@tu.kw>待部署区域</>请求支援，请立即前往。
[PopupDialog(dialogHead="$avatar_milu")] 收到。

[Battle.Pause(pause=false)]
[Delay(time=2)]
[Battle.Pause(pause=true)]

[PopupDialog(dialogHead="$avatar_milu")] 呼叫杜宾教官，守林人已达到指定位置。
[PopupDialog(dialogHead="$avatar_doberm")] 注意，本次作战条件较为苛刻，只能部署两名干员。不过，你可以与杰西卡进行“<@tu.kw>接力</>”，直接部署在她的位置上。
[PopupDialog(dialogHead="$avatar_jesica")] “<@tu.kw>接力</>”？与以往的作战部署相比，有什么不一样吗？
[PopupDialog(dialogHead="$avatar_doberm")] 这是一种全新的战术。杰西卡注意，当守林人部署在你的位置时，你需要马上撤退。
[Tutorial(focusX=35, focusY=63, focusWidth=69, focusHeight=125, anchor="BottomLeft", \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_jesica")] \
是直接撤往<@tu.kw>休整区</>吗？
[PopupDialog(dialogHead="$avatar_doberm")] 没错，记得抓紧时间好好调整状态。预备区人手不足时，休整区待命的干员需要全部补充进来。
[PopupDialog(dialogHead="$avatar_jesica")] 明白了！
[PopupDialog(dialogHead="$avatar_doberm")] 另外，PRTS为大家配备了一种全新的“<@tu.kw>战术装备</>”。它可以使接力的干员继承被接力者的部分能力，从而获得<@tu.kw>增强</>。

[Battle.LockFunction(mask="CHARACTER_MENU")]
[InputBlocker(blockInput=false)]
[Tutorial(waitForSignal="put_down", dialogHead="$avatar_doberm", animStyle="Drag", \
          startX=-122, startY=60, startAnchor="BottomRight", endX=-185, endY=-40)] \
博士，现在请将守林人部署在杰西卡的位置。
[Tutorial(waitForSignal="select_direction", dialogHead="$avatar_doberm", animStyle="Drag", \
          startX=-70, startY=-50, endX=250, endY=-50)] \
就是这样，<@tu.kw>选择方向</>。
[InputBlocker(blockInput=true)]
[Battle.UnlockFunction(mask="CHARACTER_MENU")]
[Battle.Pause(pause=false)]
[Delay(time=6)]
[Battle.Pause(pause=true)]
[PopupDialog(dialogHead="$avatar_milu")] 我的攻击速度好像变快了，是因为杰西卡留给我的<@tu.kw>战术装备</>吗？
[Tutorial(focusX=-180, focusY=-37, focusWidth=150, focusHeight=150, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm")] \
是的，你身上的战术装备已经激活了，仔细看围绕在你身边的<@tu.kw>深色装备</>。
[PopupDialog(dialogHead="$avatar_milu")] 原来如此。
[Battle.LockFunction(mask="CHARACTER_MENU")]
[InputBlocker(blockInput=false)]
[Battle.UnlockFunction(mask="CHARACTER_MENU")]
[Tutorial(waitForSignal="char_info", focusX=-180, focusY=-37, focusWidth=150, focusHeight=150, \
          animStyle="Click", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_doberm")] \
另外，博士，请你聚焦守林人。
[InputBlocker(blockInput=true)]
[Battle.UnlockFunction(mask="SYSTEM_MENU_INTERACT")]
[Battle.LockFunction(mask="CHARACTER_MENU")]

[Tutorial(focusX=242, focusY=-111, focusWidth=480, focusHeight=235, \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",anchor="Left", \
          protectTime=0.5, dialogHead="$avatar_doberm")] \
很好，这里详细显示了守林人当前继承的战术装备的具体效果。
[Tutorial(focusX=242, focusY=-111, focusWidth=480, focusHeight=235, \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",anchor="Left", \
          protectTime=0.5, dialogHead="$avatar_doberm")] \
撤退干员的职业不同，接力干员所继承的战术装备也不同。比如杰西卡是<@tu.kw>狙击</>干员，守林人便获得了一件<@tu.kw>狙击装备</>。
[Tutorial(focusX=242, focusY=-111, focusWidth=480, focusHeight=235, \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",anchor="Left", \
          protectTime=0.5, dialogHead="$avatar_doberm")] \
但请注意，每位干员最多只能继承<@tu.kw>五件</>战术装备。
[PopupDialog(dialogHead="$avatar_milu")] 所以之后有其他干员继续来接力时，他也将<@tu.kw>继承</>杰西卡和我留下的战术装备。
[PopupDialog(dialogHead="$avatar_doberm")] 正是如此。


[Blocker(fadetime=0.3, block=true, a=0)]

```

### legion_tr01_b

```
[HEADER(is_tutorial=true)] 爬塔教学关卡01_b
[Battle.LockFunction(mask="SYSTEM_MENU_INTERACT")]
[Battle.Pause]

[PopupDialog(dialogHead="$avatar_milu")] 呼叫杜宾教官，前方出现重装敌人。
[Battle.Pause(pause=false)]
[Delay(time=3)]
[Battle.Pause(pause=true)]
[PopupDialog(dialogHead="$avatar_doberm")] 无需紧张。博士，我们可以消耗<@tu.kw>调用凭证</>，从预备区调度一名干员前来支援。
[InputBlocker(blockInput=false)]
[Tutorial(target="btn_draw_next_card", waitForSignal="draw_card", \
          animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",searchBtnInChildren=true, \
          protectTime=0.5, dialogHead="$avatar_doberm")] \
博士，点击这里呼叫支援。

[InputBlocker(blockInput=true)]
[PopupDialog(dialogHead="$avatar_gnosis")] 博士，杜宾教官，灵知前来支援。
[InputBlocker(blockInput=false)]

[Tutorial(waitForSignal="put_down", dialogHead="$avatar_gnosis", animStyle="Drag", \
          startX=-150, startY=60, startAnchor="BottomRight", endX=-185, endY=-40)] \
建议让我来<@tu.kw>接力</>守林人。
[Tutorial(waitForSignal="select_direction", dialogHead="$avatar_gnosis", animStyle="Drag", \
          startX=-60, startY=-45, endX=240, endY=-45)] \
就是这样。
[InputBlocker(blockInput=true)]
[Battle.UnlockFunction(mask="CHARACTER_MENU")]
[Battle.UnlockFunction(mask="SYSTEM_MENU_INTERACT")]
[Battle.Pause(pause=false)]
[Delay(time=2)]
[Battle.Pause(pause=true)]
[PopupDialog(dialogHead="$avatar_doberm")] 对了博士，部分职业的战术装备，并非继承效果，比如<@tu.kw>辅助</>的装备效果将在<@tu.kw>部署时</>立即触发。
[Tutorial(focusX=-48, focusY=292, focusWidth=92, focusHeight=124, anchor="BottomRight", \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_gnosis")] \
没错。作为辅助干员，我在部署后可立即带来一些调用凭证。
[PopupDialog(dialogHead="$avatar_gnosis")] 博士，开始战斗吧。

[Blocker(fadetime=0.3, block=true, a=0)]

```

### legion_tr02_a

```
[HEADER(is_tutorial=true)] 爬塔教学关卡02_a
[Battle.LockFunction(mask="SYSTEM_MENU_INTERACT")]
[Battle.Pause]

[PopupDialog(dialogHead="$avatar_scave")] 呼叫杜宾教官，正在遭受不明人士攻击！
[PopupDialog(dialogHead="$avatar_doberm")] 我马上呼叫支援！
[PopupDialog(dialogHead="$avatar_doberm")] 这里是T0326“待部署区域”，清道夫受到攻击，请求支援！
[PopupDialog(dialogHead="$avatar_grani")] 收到。
[Battle.Pause(pause=false)]
[Delay(time=1)]
[Battle.Pause(pause=true)]

[Tutorial(focusX=-170, focusY=-51, focusWidth=135, focusHeight=144,  \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_grani")] \
格拉尼到达指定区域，已经找到清道夫了......她现在很虚弱。

[Tutorial(focusX=-170, focusY=-51, focusWidth=135, focusHeight=144,  \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_grani")] \
我该怎么办？

[PopupDialog(dialogHead="$avatar_doberm")] <@tu.kw>接力</>清道夫。这样即使她被击倒，她身上的战术装备也可以被全部继承下来。
[InputBlocker(blockInput=false)]
[Battle.EnsureMinCost(cost=11)]
[Tutorial(waitForSignal="put_down", dialogHead="$avatar_grani", animStyle="Drag", \
          startX=-150, startY=60, startAnchor="BottomRight", endX=-185, endY=-40)] \
博士，请立刻将我部署到清道夫的位置！
[Tutorial(waitForSignal="select_direction", dialogHead="$avatar_grani", animStyle="Drag", \
          startX=-70, startY=-50, endX=250, endY=-50)] \
好！就这样！
[InputBlocker(blockInput=true)]
[Battle.UnlockFunction(mask="SYSTEM_MENU_INTERACT")]

[Battle.Pause(pause=false)]
[Delay(time=2)]
[Battle.Pause(pause=true)]

[PopupDialog(dialogHead="$avatar_scave")] 可恶......小心点，格拉尼，那个戴着头盔的人，很危险。
[PopupDialog(dialogHead="$avatar_grani")] 放心吧。

[Battle.Pause(pause=false)]
[Delay(time=5)]
[Battle.Pause(pause=true)]

[PopupDialog(dialogHead="$avatar_grani", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 哈......这副打扮还真像大鲍勃！
[PopupDialog(dialogHead="$avatar_grani", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 呼叫杜宾教官，前方发现重装敌人，需要支援！
[Tutorial(focusX=-48, focusY=292, focusWidth=92, focusHeight=124, anchor="BottomRight", \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm")] \
这里还有少量<@tu.kw>调用凭证</>。
[PopupDialog(dialogHead="$avatar_grani")] 呜......只能请求三次支援。
[PopupDialog(dialogHead="$avatar_doberm")] 目前人手紧张，等坚持过敌人的一轮进攻后，在<@tu.kw>休息阶段</>将会重新发放调用凭证。所以，格拉尼，一定要坚持住！
[PopupDialog(dialogHead="$avatar_skadi")] 格拉尼，听得到吗？我来前往支援。

[Blocker(fadetime=0.3, block=true, a=0)]

```

### legion_tr02_b

```
[HEADER(is_tutorial=true)] 爬塔教学关卡02_b

[Battle.Pause]

[PopupDialog(dialogHead="$avatar_skadi")] 原来击败这个敌人后，还会获得<@tu.kw>调用凭证</>。
[PopupDialog(dialogHead="$avatar_grani")] 呼叫杜宾教官，我们已经击败了敌人。
[PopupDialog(dialogHead="$avatar_doberm")] 收到。现在有<@tu.kw>短暂</>的休息时间，我们会抓紧时间为各位投放补给。
[PopupDialog(dialogHead="$avatar_grani")] 收到。
[PopupDialog(dialogHead="$avatar_skadi")] 这次的敌人，似乎有些不对劲......
[PopupDialog(dialogHead="$avatar_mudrok")] 和之前相比，好像<@tu.kw>变强</>了。
[PopupDialog(dialogHead="$avatar_doberm")] 是因为增幅装置。
[PopupDialog(dialogHead="$avatar_grani")] 增幅装置？
[Tutorial(focusX=-181, focusY=-29, focusWidth=202, focusHeight=44, anchor="Top", \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
在这里，敌人也同样配置了能<@tu.kw>变强</>的装备。注意，他们的<@tu.kw>危险等级</>会随着战斗时间的延长而提升。
[Tutorial(focusX=-181, focusY=-29, focusWidth=202, focusHeight=44, anchor="Top", \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
每次危险等级的提升，都会使敌人变得更强。在本次作战中，危险等级的提升会使敌人的<@tu.kw>生命值</>大幅提升、<@tu.kw>攻击力</>与<@tu.kw>防御力</>提升，并且这种提升是永久生效的。
[Tutorial(focusX=-181, focusY=-29, focusWidth=202, focusHeight=44, anchor="Top", \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_grani", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
也就是说，战斗拖得<@tu.kw>越久越危险</>？
[Tutorial(focusX=-181, focusY=-29, focusWidth=202, focusHeight=44, anchor="Top", \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
没错，要速战速决。
[Tutorial(focusX=35, focusY=63, focusWidth=69, focusHeight=125, anchor="BottomLeft", \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_scave")] \
呼叫杜宾教官，清道夫已经休整完毕。
[Tutorial(focusX=-36, focusY=67, focusWidth=71, focusHeight=121, anchor="BottomRight", \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_scave")] \
预备区的干员全部投入战斗后，我会随休整区的各位一起前往<@tu.kw>预备区</>待命，随时支援作战。

[Blocker(fadetime=0.3, block=true, a=0)]

```

### legion_tr03

```
[HEADER(is_tutorial=true)] 爬塔教学关卡03

[Battle.Pause]

[PopupDialog(dialogHead="$avatar_doberm")] 博士，接下来便是正式的作战任务了。
[PopupDialog(dialogHead="$avatar_doberm")] 在此之前，我向你介绍两种全新的战术规则。

[Tutorial(focusX=1, focusY=63, focusWidth=1154, focusHeight=126, anchor="Bottom",  \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm")] \
任务开始前，我们将<@tu.kw>随机</>调派数名干员前来支援作战。

[Tutorial(focusX=112, focusY=64, focusWidth=470, focusHeight=122, anchor="Bottom",  \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm")] \
此时，博士可以选择<@tu.kw>最多四名</>干员<@tu.kw>返回预备区</>，另选四名干员来<@tu.kw>重组</>初始作战阵容。
[PopupDialog(dialogHead="$avatar_doberm")] 并且，我们也为博士准备了部分<@tu.kw>调用凭证</>，由您自行调配。
[Tutorial(focusX=112, focusY=64, focusWidth=470, focusHeight=122, anchor="Bottom",  \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm")] \
不过还有一点需要注意：待部署区域能容纳的<@tu.kw>人数有限</>，当<@tu.kw>满员</>时，其他干员将<@tu.kw>无法加入</>，只能前往休整区。
[Tutorial(focusX=-115, focusY=160, focusWidth=229, focusHeight=39, anchor="BottomRight", \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm")] \
最后还有一点，保全派驻作战中的可部署数<@tu.kw>十分有限</>。
[Tutorial(focusX=-115, focusY=160, focusWidth=229, focusHeight=39, anchor="BottomRight",  \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm")] \
所以博士你需要针对这种情况做出策略调整。
[PopupDialog(dialogHead="$avatar_doberm")] 博士，准备好了吗？

[Blocker(fadetime=0.3, block=true, a=0)]

```

### main_00-01

```
[HEADER(is_skippable=true, is_autoable=false)] 主线00-01关卡内剧情
[PopupDialog(dialogHead="$avatar_doberm")] 敌人从右边组织了进攻，请小心。
[Blocker(fadetime=0.3, block=true, a=0)]
```

### main_00-02

```
[HEADER(is_skippable=true, is_autoable=false)] 主线00-02关卡内剧情
[PopupDialog(dialogHead="$avatar_doberm")] 更多整合运动接近中，请注意防守！
[Blocker(fadetime=0.3, block=true, a=0)]
```

### main_00-03

```
[HEADER(is_skippable=true, is_autoable=false)] 主线00-03关卡内剧情
[PopupDialog(dialogHead="$avatar_doberm")] 这里更接近敌人的聚集区域。
[PopupDialog(dialogHead="$avatar_doberm")] 左侧侦察到了敌方的无人机，请部署狙击干员防守！
[Blocker(fadetime=0.3, block=true, a=0)]
```

### main_00-04

```
[HEADER(is_skippable=true, is_autoable=false)] 主线00-04关卡内剧情
[PopupDialog(dialogHead="$avatar_ace")] 有更多无人机接近中，基本可以确定是敌方的术师无人机。
[PopupDialog(dialogHead="$avatar_doberm")] 看得出是从切城的军备库里缴获后改造的......简单的暴乱可是用不了这么多的无人机。
[PopupDialog(dialogHead="$avatar_doberm")] 他们是有备而来的。注意部署狙击干员防守无人机！
[Blocker(fadetime=0.3, block=true, a=0)]
```

### main_00-05

```
[HEADER(is_skippable=true, is_autoable=false)] 主线00-05关卡内剧情
[PopupDialog(dialogHead="$avatar_amiya")] 那些是......野兽？不对......它们好像被控制了一样。
[PopupDialog(dialogHead="$avatar_doberm")] 整合运动的术师还控制了这么多源石虫和无人机，他们打算靠数量取胜。
[PopupDialog(dialogHead="$avatar_doberm")] 前方会有高速的敌方单位袭来，建议优先部署<@tu.kw>先锋</>干员。
[Blocker(fadetime=0.3, block=true, a=0)]
```

### main_00-06

```
[HEADER(is_skippable=true, is_autoable=false)] 主线00-06教学
[Tutorial(focusX=-546, focusY=-165, focusWidth=156, focusHeight=154,          animStyle="Highlight", focusStyle="HighlightCircle", black=0.6,           protectTime=0.5, dialogHead="$avatar_doberm")] 啧，他们还在组织进攻。真是难缠。
[Tutorial(focusX=-546, focusY=-165, focusWidth=156, focusHeight=154,          animStyle="Highlight", focusStyle="HighlightCircle", black=0.6,           protectTime=0.5, dialogHead="$avatar_amiya")] 博士，战场下方的道路已经被打开。请注意在上下方各部署一名<@tu.kw>先锋</>干员来防守突袭而来的敌方猎犬。
[Blocker(fadetime=0.3, block=true, a=0)]
```

### main_00-07

```
[HEADER(is_skippable=true, is_autoable=false)] 主线00-07教学
[Tutorial(focusX=-468, focusY=-118, focusWidth=109, focusHeight=119,          animStyle="Highlight", focusStyle="HighlightCircle", black=0.6,           protectTime=0.5, dialogHead="$avatar_amiya")] 博士，敌方持盾的单位拥有<@tu.kw>较高防御</>，普通攻击对他们很难产生效果。最好能派遣<@tu.kw>术师</>干员进行针对。
[Blocker(fadetime=0.3, block=true, a=0)]
```

### main_00-08

```
[HEADER(is_skippable=true, is_autoable=false)] 主线00-08关卡内剧情
[PopupDialog(dialogHead="$avatar_ace")] 虽然并不是没有胜算，但是情况不容乐观。
[PopupDialog(dialogHead="$avatar_amiya")] 嗯，我明白我该怎么做......
[PopupDialog(dialogHead="$avatar_doberm")] 前方有大量敌人部队接近，建议部署带有<@tu.kw>群体伤害效果</>的术师。
[Blocker(fadetime=0.3, block=true, a=0)]
```

### main_00-09

```
[HEADER(is_skippable=true, is_autoable=false)] 主线00-09关卡内剧情
[PopupDialog(dialogHead="$avatar_doberm")] 真是没完没了......还有大量敌人没有被消灭。不要放松警惕！
[Blocker(fadetime=0.3, block=true, a=0)]
```

### main_00-10

```
[HEADER(is_skippable=true, is_autoable=false)] 主线00-10关卡内剧情
[PopupDialog(dialogHead="$avatar_amiya")] 敌方单位“拾荒者”的攻击力很强......我们需要小心应对。
[PopupDialog(dialogHead="$avatar_doberm")] 博士，建议部署重装干员防守。
[PopupDialog(dialogHead="$avatar_ace")] 只有击溃他，我们才能有更大的发挥空间！
[Blocker(fadetime=0.3, block=true, a=0)]
```

### main_00-11

```
[HEADER(is_skippable=true, is_autoable=false)] 主线00-11关卡内剧情
[PopupDialog(dialogHead="$avatar_doberm")] 别管整合运动的指挥官了，至少他没有进一步的指挥动作了。
[PopupDialog(dialogHead="$avatar_doberm")] 是敌人的混合部队！小心应对。
[Blocker(fadetime=0.3, block=true, a=0)]
```

### main_01-01

```
[HEADER(is_skippable=false, is_autoable=false, is_tutorial=true)] 主线01-01关卡内剧情
[Battle.LockFunction(mask="SYSTEM_MENU_INTERACT")]
[InputBlocker(blockInput=false)]
[PopupDialog(dialogHead="$avatar_amiya", animStyle="NoWait",     dialogX="$f_lower_dialog_pos_x", dialogY=-200)] 博士请注意，敌人派出了更强的猎狗部队。请确保我方<@tu.kw>先锋</>干员能够在第一时间内阻挡其行动。
[Delay(time=3.5)]
[Battle.unlockFunction(mask="SYSTEM_MENU_INTERACT")]
```


> 本章节共240个脚本文件，此处展示前30个。

## 统计

- 总字符数：26521
- 对话行数：0


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
