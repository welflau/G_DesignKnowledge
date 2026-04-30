# 明日方舟 · 活动剧情 · act2vmulti（18段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act2vmulti」完整剧情脚本（18个文件，0行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act2vmulti
- 脚本文件数：18

### guide_act2vmulti_entry

```
[HEADER(is_skippable=false, is_tutorial=true)] act2vmulti匹配引导
[Tutorial(waitForSignal="act2vmulti_home_routed")]
[PopupDialog(dialogHead="$avatar_amiya")] 博士，您能来参加这次促融共竞活动真是太好了！
[PopupDialog(dialogHead="$avatar_amiya")] 随着越来越多身份各异的干员加入，维系干员关系的工作也变得棘手起来。《干员安全相处指南》越来越厚了，这样下去可不是办法......
[PopupDialog(dialogHead="$avatar_amiya")] 这次促融共竞活动旨在帮助罗德岛全体成员建立融洽的关系，博士也要和一位协作者共同参加比赛才行哦。
[PopupDialog(dialogHead="$avatar_amiya")] 我也拜托后勤部准备了丰厚的比赛奖励，多多完成比赛项目，提升赛事热度，就可以拿到奖励了。
[Tutorial(target="btn_match", searchBtnInChildren=true,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 来看看这次的比赛项目吧！
[Tutorial(waitForSignal="act2vmulti_match_routed")]
[Tutorial(target="match_normal_group_bg", searchBtnInChildren=true,            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 常规项目构成了赛事的主体且分为多个阶段，每个阶段都有特定的目标需要达成。
[Tutorial(target="match_other_group_bg", searchBtnInChildren=true,            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 此外，本次赛事还设置了两个特殊的娱乐项目——堡垒守御和阵地足球，博士有兴趣的话也可以来体验哦。
[Tutorial(target="btn_normal_train", searchBtnInChildren=true,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 选择博士您有意向参与的项目，就可以匹配到参赛意向相近的协作者。
[Tutorial(focusX=-557, focusY=43, focusWidth=362, focusHeight=85, anchor="BottomRight",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 如果在赛场上表现优异，博士也可以选择成为兼任教练，优先匹配到经验尚浅的协作者，帮助他们完成比赛。
[Tutorial(target="btn_match_guide_book", searchBtnInChildren=true,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 现在，来熟悉下进入比赛前的备赛流程吧！
[Tutorial(waitForSignal="guidebook_exit_btn_clicked")]
[Tutorial(target="btn_match_train", searchBtnInChildren=true,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 如果博士已经了解了备赛流程，就进入规则教学，熟悉一下比赛内的规则吧！
```

### guide_act2vmulti_squad

```
[HEADER(is_skippable=false, is_tutorial=true)] act2vmulti队伍引导
[Tutorial(waitForSignal="act2vmulti_home_routed")]
[Tutorial(target="btn_team_config", searchBtnInChildren=true,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 这次促融共竞活动中，为了方便您与协作者搭配出合适的阵容，您可以在赛前配置队伍时设置两种不同的干员类别。
[Tutorial(waitForSignal="act2vmulti_squad_routed")]
[Tutorial(target="squad_high_group_item_view",            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 您可以将您青睐的干员设为高顺位干员。高顺位干员具有优先入队权。
[PopupDialog(dialogHead="$avatar_amiya")]如果您将干员A设置为高顺位干员，协作者将干员A设置为低顺位干员，当您与协作者同时携带干员A时，干员A将直接加入您的队伍。
[Tutorial(target="squad_low_group_item_view",            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 与高顺位干员相对，低顺位干员不具有优先入队权。
[PopupDialog(dialogHead="$avatar_amiya")]如果您与协作者都将干员B设置为低顺位干员，当您与协作者同时携带干员B时，主办方会将干员B随机分配至某一方的队伍中。
[Tutorial(target="btn_buff_desc", searchBtnInChildren=true,            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 最终的上场阵容中，干员的职业分布决定了队伍可以在比赛中获得怎样的专项支持。专项支持的获取规则和加成效果可以在这里查看。
```

### fortress_beginning_camera

```
[HEADER(is_tutorial=true, is_skippable=false)] 要塞镜头演出

[Battle.lockFunction(mask="PAUSE_BUTTON_INTERACT")]
[Battle.lockFunction(mask="CARD_LIST")]
[UIOperation(target="main", enable="false")]

[InputBlocker(blockInput=true)]
[Battle.Delay(time=2)]
[CooperateBattle.CameraFocusTo(offsetX=4, offsetY=8, scale=1.2, time=2)]
[Battle.elay(time=3)]
[CooperateBattle.CameraFocusTo(offsetX=22, offsetY=8, scale=1.2, time=2)]
[Battle.Delay(time=3)]
[CooperateBattle.CameraFocusTo(offsetX=8, offsetY=8, scale=1, time=2)]
[Battle.Delay(time=3)]

[Battle.unlockFunction(mask="PAUSE_BUTTON_INTERACT")]
[Battle.unlockFunction(mask="CARD_LIST")]
[UIOperation(target="main", enable="true")]
```

### training_fortress_a1

```
[HEADER(is_tutorial=true, is_skippable=false)] 要塞教学a1

[Battle.lockFunction(mask="PAUSE_BUTTON_INTERACT")]
[Battle.lockFunction(mask="CARD_LIST")]

[CooperateBattle.CameraFocusTo(offsetX=5, offsetY=4, scale=1.2, time=1.5)]
[Battle.Delay(time=2.5)]
[CooperateBattle.CameraFocusTo(offsetX=16, offsetY=4, scale=1.2, time=1.5)]
[Battle.Delay(time=2.5)]
[CooperateBattle.CameraFocusTo(offsetX=8, offsetY=4, scale=1, time=1.5)]
[Battle.Delay(time=1)]

[Battle.unlockFunction(mask="PAUSE_BUTTON_INTERACT")]
[Battle.unlockFunction(mask="CARD_LIST")]
```

### training_fortress_a2

```
[HEADER(is_tutorial=true, is_skippable=false)] 要塞教学a2

[Battle.lockFunction(mask="PAUSE_BUTTON_INTERACT")]
[Battle.lockFunction(mask="CARD_LIST")]

[Battle.Pause]

[CooperateBattle.CameraFocusTo(offsetX=6, offsetY=4, scale=1, time=1)]
[Delay(time=1)]
[Tutorial(dialogHead="$avatar_melan")]堡垒守御项目的比赛开始了。要守住我身后的目标点才行......
[CooperateBattle.CameraFocusTo(offsetX=8, offsetY=4, scale=1, time=1)]
[Delay(time=1)]

[Battle.unlockFunction(mask="PAUSE_BUTTON_INTERACT")]
[Battle.unlockFunction(mask="CARD_LIST")]
```

### training_fortress_a3

```
[HEADER(is_tutorial=true, is_skippable=false)] 要塞教学a3

[Battle.lockFunction(mask="PAUSE_BUTTON_INTERACT")]

[Battle.Pause]

[CooperateBattle.CameraFocusTo(offsetX=8, offsetY=4, scale=0.8, time=0.5)]
[Tutorial(dialogHead="$avatar_melan")]第一波进攻的敌方选手，我会尽力打倒。
[Tutorial(dialogHead="$avatar_melan")]但后面还会有更猛烈的进攻......

[Battle.Pause(pause=false)]
[Battle.Delay(time=1)]
[Battle.Pause]


[Tutorial(dialogHead="$avatar_adnach")]我来支援！

[CooperateBattle.CameraFocusTo(offsetX=3, offsetY=4, scale=1, time=0.5)]
[Delay(time=0.5)]

[Tutorial(dialogHead="$avatar_adnach")]看起来，场内布置了很多【折叠设施】。

[Battle.Pause(pause=false)]
[Battle.Delay(time=1)]
[Battle.Pause]

[Tutorial(dialogHead="$avatar_stward")]把这些设施利用起来，可以帮助我们防守。
[Tutorial(dialogHead="$avatar_stward")]派遣【折叠设施维护员】能帮忙维护这些设施。


[Battle.Pause(pause=false)]
[Battle.Delay(time=3.5)]
[Battle.Pause]

[CooperateBattle.CameraFocusTo(offsetX=3, offsetY=5.5, scale=0.8, time=0.5)]
[Delay(time=0.5)]
[Tutorial(focusX=0, focusY=0, focusWidth=360, focusHeight=360, anchor="Center", \
          animStyle="Highlight", focusStyle="HighlightRect", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_stward", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
这是【折叠式后勤站】，经过维护就可以展开成为赛场后勤站，提升同时可部署的干员人数，并缩短干员的再部署时间。

[CooperateBattle.CameraFocusTo(offsetX=3, offsetY=3.5, scale=0.8, time=0.5)]
[Delay(time=0.5)]
[Tutorial(focusX=0, focusY=0, focusWidth=360, focusHeight=360, anchor="Center", \
          animStyle="Highlight", focusStyle="HighlightRect", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_stward", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
这是【折叠式维护车】，经过维护就可以展开成为赛场维护车，为我们带来更多的折叠设施维护员。
[CooperateBattle.CameraFocusTo(offsetX=3, offsetY=4, scale=1, time=0.5)]
[Delay(time=0.5)]
[Tutorial(dialogHead="$avatar_stward")]折叠设施维护员工作一段时间后会下班，折叠设施需要经过三次维护才能投入使用。
[Tutorial(dialogHead="$avatar_stward")]不过如果地形合适，也可以派遣多名维护员同时维护。

[Battle.Pause(pause=false)]
[Battle.Delay(time=5)]
[Battle.Pause]

[CooperateBattle.CameraFocusTo(offsetX=3, offsetY=5.5, scale=0.8, time=0.5)]
[Delay(time=0.5)]
[Tutorial(focusX=0, focusY=0, focusWidth=240, focusHeight=240, anchor="Center", \
          animStyle="Highlight", focusStyle="HighlightRect", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_stward", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
后勤站已经展开了，可以投入使用！

[CooperateBattle.CameraFocusTo(offsetX=3, offsetY=3.5, scale=0.8, time=0.5)]
[Delay(time=0.5)]
[Tutorial(focusX=0, focusY=0, focusWidth=240, focusHeight=240, anchor="Center", \
          animStyle="Highlight", focusStyle="HighlightRect", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_adnach", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
这里的维护车刚刚只有两名维护员在维护，还不能投入使用。

[Tutorial(focusX=0, focusY=-120, focusWidth=400, focusHeight=100, anchor="Top", \
          animStyle="Highlight", focusStyle="HighlightRect", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_melan", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
没关系，现在还是两波进攻之间的休整阶段......

[CooperateBattle.CameraFocusTo(offsetX=3, offsetY=3.5, scale=0.8, time=0.5)]
[Delay(time=0.5)]
[CooperateBattle.LockCamera(enable=false)]
[InputBlocker(blockInput=true, cardIndex=0, validWidth=112, validHeight=116)]
[Tutorial(waitForSignal="put_down", dialogHead="$avatar_stward", animStyle="Drag", \
          startX=-300, startY=60, startAnchor="BottomRight", endAnchor="Center", endX=0, endY=0)] \
趁还有休整时间，继续派遣折叠设施维护员吧！
[InputBlocker(blockInput=true)]
[Delay(time=0.5)]
[InputBlocker(blockInput=true, tileX=3, tileY=3, validWidth=600, validHeight=600)]
[Tutorial(waitForSignal="select_direction", dialogHead="$avatar_stward")] \
向<@tu.kw>折叠式维护车</>的方向部署维护员！

[InputBlocker(blockInput=false)]
[Battle.Pause(pause=false)]
[Battle.Delay(time=8)]
[Battle.Pause]
[InputBlocker(blockInput=true)]

[Tutorial(dialogHead="$avatar_stward")]一切顺利，维护车应该可以投入使用了！
[Tutorial(dialogHead="$avatar_stward")]如果操作失误，没有让维护员正确地朝向需要维护的设施，维护员会自主返回待部署区，等待下一次派遣。
[Tutorial(dialogHead="$avatar_adnach")]场上目前还没有高台位，我们该怎么上场？
[Tutorial(dialogHead="$avatar_stward")]抵御住下一波进攻，再次进入休整阶段时，赛场维护车就会为我们带来更多折叠设施维护员。
[Tutorial(dialogHead="$avatar_stward")]到时候就可以派遣他们去维护【折叠式堡垒模块】，展开成为可部署高台干员的【堡垒筑台】，为更多干员创造上场的机会。
[CooperateBattle.CameraFocusTo(offsetX=6, offsetY=4, scale=1, time=1)]
[Delay(time=1)]
[Tutorial(focusX=0, focusY=-180, focusWidth=200, focusHeight=60, anchor="Top", \
          animStyle="Highlight", focusStyle="HighlightRect", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_adnach", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
目前已经没有其他准备工作需要做了，可以迎接下一波进攻了！

[CooperateBattle.LockCamera(enable=true)]

[Battle.unlockFunction(mask="PAUSE_BUTTON_INTERACT")]
```

### training_fortress_b1

```
[HEADER(is_tutorial=true, is_skippable=false)] 要塞教学b1

[Battle.lockFunction(mask="PAUSE_BUTTON_INTERACT")]
[Battle.lockFunction(mask="CARD_LIST")]

[CooperateBattle.CameraFocusTo(offsetX=9, offsetY=4.5, scale=1, time=0.5)]
[Battle.Delay(time=1)]
[Battle.Pause]

[CooperateBattle.CameraFocusTo(offsetX=9, offsetY=4.5, scale=1, time=0.5)]
[Delay(time=0.5)]

[Tutorial(focusX=0, focusY=0, focusWidth=240, focusHeight=480, anchor="Center", \
          animStyle="Highlight", focusStyle="HighlightRect", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_adnach", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
这就是折叠式堡垒模块，经过维护能展开成为堡垒筑台。
[Tutorial(dialogHead="$avatar_stward")]它也需要经过三次维护才能投入使用。
[Tutorial(dialogHead="$avatar_stward")]对了，堡垒筑台不仅能部署高台干员，还可以改变敌方的行进路线。

[CooperateBattle.CameraFocusTo(offsetX=11, offsetY=4.5, scale=1, time=0.5)]
[Delay(time=0.5)]
[Tutorial(focusX=0, focusY=0, focusWidth=240, focusHeight=480, anchor="Center", \
          animStyle="Highlight", focusStyle="HighlightRect", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_adnach", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
前面的设施是......
[Tutorial(dialogHead="$avatar_stward")]【折叠式城防路障】，只需要一次维护就能投入使用。
[Tutorial(dialogHead="$avatar_stward")]维护完成后，它会展开成为【城防路障】，阻挡敌方的脚步。

[Battle.Pause(pause=false)]
[Battle.Delay(time=1.5)]
[Battle.Pause]

[Tutorial(dialogHead="$avatar_stward")]协作者可以共同参与设施维护。
[Tutorial(dialogHead="$avatar_stward")]之前投入使用的维护车带来了更多维护员，剩下的设施维护就交给博士了！
[Tutorial(dialogHead="$avatar_adnach")]休整阶段的主要任务是维护设施，干员们还不需要上场。
[Tutorial(dialogHead="$avatar_adnach")]等到下一波进攻开始，我们就可以登上已经展开的堡垒筑台，准备防守了。

[CooperateBattle.CameraFocusTo(offsetX=10, offsetY=4, scale=1, time=0.5)]
[Delay(time=0.5)]

[Battle.unlockFunction(mask="PAUSE_BUTTON_INTERACT")]
[Battle.unlockFunction(mask="CARD_LIST")]
```

### training_fortress_b2

```
[HEADER(is_tutorial=true, is_skippable=false)] 要塞教学b2

[Battle.lockFunction(mask="PAUSE_BUTTON_INTERACT")]
[Battle.lockFunction(mask="CARD_LIST")]

[CooperateBattle.CameraFocusTo(offsetX=16, offsetY=4, scale=1.2, time=1.5)]
[Battle.Delay(time=4)]

[Battle.pause]
[Tutorial(dialogHead="$avatar_melan")]下一波进攻要来了......大家小心！
[Tutorial(dialogHead="$avatar_stward")]我们的场地设施可以发挥作用了！

[CooperateBattle.CameraFocusTo(offsetX=16, offsetY=4, scale=0.6, time=0.5)]
[Delay(time=0.5)]
[Tutorial(focusX=160, focusY=120, focusWidth=240, focusHeight=240, anchor="Center", \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_adnach", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
等等，这两名敌方选手为什么直奔场地下方的后勤站？
[Tutorial(dialogHead="$avatar_stward")]敌方的【铁头前锋】和【长臂投手】会破坏我们的场地设施。
[Tutorial(dialogHead="$avatar_stward")]看起来，他们的注意力完全被场地下方的后勤站吸引了。
[Tutorial(dialogHead="$avatar_melan")]在之后的堡垒守御比赛中，还是多注意下他们的行动比较好。

[CooperateBattle.CameraFocusTo(offsetX=8, offsetY=4, scale=1, time=1.5)]
[Delay(time=1)]

[Battle.unlockFunction(mask="PAUSE_BUTTON_INTERACT")]
[Battle.unlockFunction(mask="CARD_LIST")]
```

### training_act2vmulti_01_a

```
[HEADER(is_tutorial=true, is_skippable=false)] 联机教学关1a

[Battle.Pause]
[InputBlocker(blockInput=true)]

[PopupDialog(dialogHead="$avatar_amiya")]博士，欢迎来到促融共竞的比赛现场！

[PopupDialog(dialogHead="$avatar_amiya")]促融共竞的所有项目都需要您与<@tu.kw>一位协作者</>共同参与，这次就先让我来当博士的协作者吧！

```

### training_act2vmulti_01_b

```
[HEADER(is_tutorial=true, is_skippable=false)] 联机教学关1b

[Battle.Pause]
[InputBlocker(blockInput=true)]

[PopupDialog(dialogHead="$avatar_amiya")]一场比赛分为两个阶段，每个阶段都有需要完成的目标。

[Tutorial(target="panel_cooperate_normal_status",\
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
本场比赛第一阶段的目标是【生存】，我们需要在限定时间内抵挡敌方的进攻。

[PopupDialog(dialogHead="$avatar_amiya")]虽然在同一片赛场上竞技，但我们各自需要防守不同的目标点。

[Tutorial(focusX=-430, focusY=-70, focusWidth=150, focusHeight=150, \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
博士，您需要防守的是蓝色的目标点。敌方进入蓝色目标点，将会扣减您的目标生命值。

[Tutorial(focusX=430, focusY=-70, focusWidth=150, focusHeight=150, \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
墨绿色的目标点由协作者——也就是我来防守。敌方进入墨绿色目标点，则会扣减我的目标生命值。

[Battle.Pause(pause=false)]
[Delay(time=1)]
[Battle.Pause(pause=true)]

[Tutorial(focusX=350, focusY=100, focusWidth=120, focusHeight=120, \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
对了！协作者部署的干员会用特殊的颜色标记出来，这样您就不会混淆双方的干员了。

[Tutorial(focusX=0, focusY=-70, focusWidth=180, focusHeight=180, \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
最后，高亮的目标点由我们协作防守。敌方进入高亮的目标点，会同时扣减我们两个人的目标生命值。
```

### training_act2vmulti_01_c

```
[HEADER(is_tutorial=true, is_skippable=false)]  联机教学关1c

[Battle.Pause]
[InputBlocker(blockInput=true)]

[PopupDialog(dialogHead="$avatar_amiya")]即使我们之中有一方的目标生命值归零，我们的队伍也不会立刻输掉比赛。

[Battle.Pause(pause=false)]
[Delay(time=2)]
[Battle.Pause(pause=true)]

[Tutorial(focusX=350, focusY=0, focusWidth=150, focusHeight=150, \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
啊，敌方选手很快就要进入我负责防守的目标点了——我的目标生命值就要归零了......

[Battle.Pause(pause=false)]
[Delay(time=3)]
[Battle.Pause(pause=true)]

[Tutorial(focusX=350, focusY=120, focusWidth=150, focusHeight=150, \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
之后，我部署的干员会停止行动。

[Tutorial(focusX=380, focusY=-60, focusWidth=150, focusHeight=150, \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
而进入我的目标点的敌方选手——

[Battle.Pause(pause=false)]
[Delay(time=3)]
[Battle.Pause(pause=true)]

[Tutorial(focusX=-305, focusY=250, focusWidth=150, focusHeight=150, \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
也会沿新的路线向您发起进攻。

[InputBlocker(blockInput=true)]
```

### training_act2vmulti_01_d

```
[HEADER(is_tutorial=true, is_skippable=false)]  联机教学关1d

[Battle.Pause]
[InputBlocker(blockInput=true)]

[Tutorial(target="slider_progress_basic",\
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
赢得比赛最重要的是完成特定目标，不需要击倒所有敌方选手哦。

[Tutorial(focusX=350, focusY=100, focusWidth=120, focusHeight=120, \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
第一阶段结束后，我们的目标生命值都会恢复，我也可以回到场上与博士并肩作战了！

[Battle.Pause(pause=false)]
[Delay(time=7)]
[Battle.Pause(pause=true)]

[Tutorial(focusX=-30, focusY=190, focusWidth=120, focusHeight=120, \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
此时，赛场上还会出现<@tu.kw>补给员</>。

[PopupDialog(dialogHead="$avatar_amiya")]在限定时间内<@tu.kw>击倒补给员</>，就可以抢下补给，获得<@tu.kw>增益效果</>。
```

### training_act2vmulti_01_e

```
[HEADER(is_tutorial=true, is_skippable=false)]  联机教学关1d1

[Battle.Pause]
[InputBlocker(blockInput=true)]
[Battle.Pause(pause=true)]

[PopupDialog(dialogHead="$avatar_amiya")]随后，就来到了中场休整的时间。在场的所有干员都将<@tu.kw>下场</>休息，做好在第二阶段重新登场的准备。
[PopupDialog(dialogHead="$avatar_amiya")]博士休息好了的话，我们就去挑战比赛的第二阶段吧！

[Battle.Pause(pause=false)]
```

### training_act2vmulti_01_f

```
[HEADER(is_tutorial=true, is_skippable=false)] 活动act1sandbox教学关1_b

[Battle.Pause]
[InputBlocker(blockInput=true)]

[Tutorial(target="slider_progress_basic",\
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
本场比赛第二阶段的目标是<@tu.kw>渗透</>，我们需要深入敌阵，击倒特定的敌方选手。击倒三名拾荒者就可以达成目标！

[Tutorial(target="slider_progress_basic",\
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
如果博士还有余力，也可以向着<@tu.kw>进阶目标</>努力！击倒五名拾荒者，就可以在赛后获得额外的<@tu.kw>嘉奖印章</>！


```

### training_act2vmulti_01_g

```
[HEADER(is_tutorial=true, is_skippable=false)] 活动act1sandbox教学关1_b

[Battle.Pause]
[InputBlocker(blockInput=true)]

[PopupDialog(dialogHead="$avatar_amiya")]为了方便协作者之间的交流互动，主办方还设置了两项辅助功能。

[Tutorial(target="cost_handle_panel",\
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
点击右下方的<@tu.kw>请求费用</>，就可以请求协作者向您支援至多15点部署费用。

[Tutorial(focusX=50, focusY=50, focusWidth=200, focusHeight=200, anchor="BottomLeft",  \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
<@tu.kw>按住</>左下方的<@tu.kw>拖动标记</>，并将其<@tu.kw>拖动</>到赛场上，就可以向协作者发送标记信号。

[PopupDialog(dialogHead="$avatar_amiya")]现在，我们一起击倒五名拾荒者，完成进阶目标吧！
```

### training_act2vmulti_02_a

```
[HEADER(is_tutorial=true, is_skippable=false)] 联机教学关1a

[Battle.Pause]
[InputBlocker(blockInput=true)]

[PopupDialog(dialogHead="$avatar_amiya")]博士，这里是娱乐项目——阵地足球的赛场！我们的唯一目标就是合力攻破敌方的球门。

[Tutorial(focusX=0, focusY=45, focusWidth=100, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
这是普通的比赛用球——不用担心！这个造型只是工程部的一个小小的玩笑，它看起来像坚硬的矿石，实际上是用很有弹性的材料制成的哦！

[Battle.Pause(pause=false)]
[Delay(time=3)]
[Battle.Pause(pause=true)]

[Tutorial(focusX=-65, focusY=50, focusWidth=130, focusHeight=130, \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
干员们可以攻击足球，<@tu.kw>累计造成一定伤害</>就能将球<@tu.kw>推动</>。

[Battle.Pause(pause=false)]
[Delay(time=3.8)]
[Battle.Pause(pause=true)]

[Tutorial(focusX=200, focusY=10, focusWidth=260, focusHeight=260, \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
足球最终的<@tu.kw>移动方向</>，完全取决于干员与足球的<@tu.kw>位置关系</>。

[Battle.Pause(pause=false)]
[Delay(time=0.7)]
[Battle.Pause(pause=true)]

[Tutorial(focusX=570, focusY=180, focusWidth=200, focusHeight=200, \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
红色目标点就是<@tu.kw>敌方的球门</>！不论用什么方法，只要足球进入红色目标点，都会被<@tu.kw>记为我方进球</>哦。






```

### training_act2vmulti_02_b

```
[HEADER(is_tutorial=true, is_skippable=false)] 联机教学关1a

[Battle.Pause]
[InputBlocker(blockInput=true)]

[PopupDialog(dialogHead="$avatar_amiya")]下面，来熟悉下防守的操作吧！

[Tutorial(focusX=-600, focusY=30, focusWidth=300, focusHeight=500, anchor="Center",\
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
蓝色目标点是我们的球门，我们需要协力防守球门，防止失球。

[Battle.Pause(pause=false)]
[Delay(time=2.2)]
[Battle.Pause(pause=true)]

[Tutorial(focusX=-70, focusY=50, focusWidth=150, focusHeight=150, \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
这只可爱的小鼷兽是敌方的<@tu.kw>击球手</>，它会试图追上足球，并向我方射门！

[Battle.Pause(pause=false)]
[Delay(time=3.1)]
[Battle.Pause(pause=true)]

[Tutorial(focusX=-480, focusY=40, focusWidth=200, focusHeight=200, \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
这时就需要部署干员防守球门。这些带有特殊标记的地块是<@tu.kw>守门位</>，部署在上面的干员会承担起<@tu.kw>守门员</>的职责。

[Battle.Pause(pause=false)]
[Delay(time=1)]
[Battle.Pause(pause=true)]

[PopupDialog(dialogHead="$avatar_amiya")]守门员可以接住飞来的足球。


[Tutorial(focusX=600, focusY=-250, focusWidth=250, focusHeight=250, \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
被守门员接住的足球会<@tu.kw>进入待部署区</>。


[CooperateBattle.LockCamera(enable=false)]
[InputBlocker(blockInput=true, cardIndex=0, validWidth=112, validHeight=116)]
[Battle.LockFunction(mask="PAUSE_BUTTON_INTERACT")]
[Tutorial(waitForSignal="put_down", dialogHead="$avatar_stward", animStyle="Drag", \
          startX=-50, startY=60, startAnchor="BottomRight", endAnchor="Center", endX=0, endY=100)] \
在5秒内将待部署区的足球<@tu.kw>部署</>在我方半场的任意位置，就可以在此<@tu.kw>重新开球</>。
[Battle.UnlockFunction(mask="PAUSE_BUTTON_INTERACT")]
[InputBlocker(blockInput=true)]

[Battle.Pause(pause=false)]
[Delay(time=3.7)]
[Battle.Pause(pause=true)]

[PopupDialog(dialogHead="$avatar_amiya")]现在，轮到我们反攻了！阵地足球项目有一个突出的特点——不仅可以踢球，还可以<@tu.kw>攻击敌方球员</>。

[Battle.Pause(pause=false)]
[Delay(time=3.7)]
[Battle.Pause(pause=true)]

[Tutorial(focusX=-110, focusY=-60,  focusWidth=150, focusHeight=150, \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
敌方球员<@tu.kw>生命值归零</>时会暂时停止行动，我们可以趁机发动进攻！

[Battle.Pause(pause=false)]
[Delay(time=7.5)]
[Battle.Pause(pause=true)]

[Tutorial(focusX=450, focusY=220, focusWidth=200, focusHeight=200, \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
这些置于球门前的场地设施是<@tu.kw>阵地屏障</>，它会阻碍我们进球。

[Battle.Pause(pause=false)]
[Delay(time=3.5)]
[Battle.Pause(pause=true)]

[Tutorial(focusX=430, focusY=170, focusWidth=200, focusHeight=200, \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
不过，干员的攻击和足球的撞击都可以<@tu.kw>破坏阵地屏障</>，使敌方的球门暴露出来。



```

### training_act2vmulti_02_c

```
[HEADER(is_tutorial=true, is_skippable=false)] 联机教学关1a

[Battle.Pause]
[InputBlocker(blockInput=true)]

[PopupDialog(dialogHead="$avatar_amiya")]不愧是博士！剩下的时间，就交给您了。
[PopupDialog(dialogHead="$avatar_amiya")]破坏阵地屏障、击倒敌方球员，或是找好角度直接射门——设法攻破敌方的球门吧！

```


## 统计

- 总字符数：25577
- 对话行数：0


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
