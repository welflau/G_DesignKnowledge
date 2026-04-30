# 明日方舟 · 活动剧情 · multiv3（21段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「multiv3」完整剧情脚本（21个文件，0行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/multiv3
- 脚本文件数：21

### guide_multi_v3_entry

```
[HEADER(is_skippable=false, is_tutorial=true)] ActMultiV3匹配引导
[Tutorial(waitForSignal="act_multi_v3_home_routed")]
[PopupDialog(dialogHead="$avatar_amiya")] 博士，欢迎您来到罗德岛促融共竞。这次促融共竞活动旨在帮助罗德岛全体成员建立融洽的关系，博士要和一位协作者共同参加比赛哦。
[PopupDialog(dialogHead="$avatar_amiya")] 在赛季手册里可以看到后勤部准备的丰厚奖励~
[Tutorial(target="pool_btn_team_up", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 【组队参加】可以创建备赛休息室，您可以在备赛休息室内独自练习，或与其他玩家共同参赛。
[Tutorial(target="pool_btn_quick_match", waitForSignal="act_multi_v3_quick_match_routed", searchBtnInChildren=true,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 【快速匹配】则可以快速匹配到与您参赛意向相近的协作者。
[Tutorial(focusX=152, focusY=192, focusWidth=306, focusHeight=320, anchor="Bottom",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 来看看这次的比赛项目吧！首先是常规项目，它们构成了这次赛事的主体。
[Tutorial(focusX=152, focusY=192, focusWidth=306, focusHeight=320, anchor="Bottom",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 常规项目有多个阶段，每个阶段都有特定的目标需要达成。
[Tutorial(focusX=-316, focusY=192, focusWidth=620, focusHeight=320, anchor="Bottom",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 此外，本次赛事还设置了两个特殊的娱乐项目——堡垒守御和障碍漂航，博士有兴趣的话也可以来体验哦。
[Tutorial(target="pool_btn_match_pos", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 博士在这里可选择游玩时的身份。
[Tutorial(target="pool_btn_match_pos", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 如果博士想要帮助更多经验尚浅的朋友，可以选择“教练”身份；反之，如果需要帮助，也可以选择“学员”身份。
[Tutorial(target="pool_btn_guidebook", searchBtnInChildren=true,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 现在，让我们来熟悉一下这次的参赛流程吧。
[Tutorial(waitForSignal="guidebook_exit_btn_clicked")]
[Tutorial(target="pool_btn_start_guide_match", searchBtnInChildren=true,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 先来体验下常规项目，完成训练赛才可以解锁更多比赛项目哦。
```

### guide_multi_v3_squad

```
[HEADER(is_skippable=false, is_tutorial=true)] ActMultiV3编队引导
[Tutorial(waitForSignal="act_multi_v3_home_routed")]
[Tutorial(target="pool_btn_squad", waitForSignal="act_multi_v3_squad_routed", searchBtnInChildren=true,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 本次促融共竞活动中，您可以提前配置队伍。
[Tutorial(focusX=455, focusY=-5, focusWidth=720, focusHeight=570, anchor="Left",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 您可以将您青睐的干员设为高顺位干员。高顺位干员具有优先入队权。 如果您与协作者携带了相同的干员，该干员是您的高顺位干员，是对方的低顺位干员，那么这位干员就可以加入您的队伍。
[Tutorial(focusX=1486, focusY=-5, focusWidth=1330, focusHeight=570, anchor="Left",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 与高顺位干员相对，低顺位干员不具有优先入队权。 如果您与协作者携带了相同的低顺位干员，主办方会将这位干员随机分配至一方的队伍。
[Tutorial(focusX=0, focusY=35, focusWidth=1000, focusHeight=70, anchor="Bottom",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 针对不同类型的项目，您可以配置不同的队伍。
[Tutorial(target="pool_btn_squad_effect", waitForSignal="act_multi_v3_squad_effect_routed", searchBtnInChildren=true,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 另外，您还可以指定每一支队伍的比赛风格。
[Tutorial(focusX=-300, focusY=289, focusWidth=600, focusHeight=142, anchor="Right",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 随着参加的比赛越来越多，您将有机会解锁更多比赛风格。您可以自由选择要解锁的比赛风格。
```

### guide_multi_v3_team

```
[HEADER(is_skippable=false, is_tutorial=true)] ActMultiV3房间引导
[Tutorial(waitForSignal="act_multi_v3_team_view_routed")]
[Tutorial(target="pool_btn_create_room", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 您可以在这里创建备赛休息室，只要分享编号，就可以邀请其他的协作者。
[Tutorial(target="pool_btn_join_room", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 同理，您也可以通过输入编号加入其他协作者的房间哦。
[Tutorial(target="pool_btn_training", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 在与人共竞之前，您如果想先熟悉下项目与赛场，也完全可以进行单人训练。不过请注意，训练赛中无法获得奖励。
[Tutorial(target="pool_btn_create_room", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 此外，您也可以通过直接点击空闲位置的方式邀请好友参与比赛。
[Tutorial(target="pool_btn_invite", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 通过此处和主界面按钮可以查看来自好友的邀请，请记得及时回应！
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

[Tutorial(dialogHead="$avatar_adnach")]看起来，场内布置了很多<@tu.kw>原料箱</>。

[Battle.Pause(pause=false)]
[Battle.Delay(time=1)]
[Battle.Pause]

[Tutorial(dialogHead="$avatar_stward")]原料箱可以被建造成各种场地设施，帮助我们防守。
[Tutorial(dialogHead="$avatar_stward")]专业的事就让专业的人来做吧！派遣<@tu.kw>设施建筑工</>来建造这些设施。


[Battle.Pause(pause=false)]
[Battle.Delay(time=3.5)]
[Battle.Pause]

[CooperateBattle.CameraFocusTo(offsetX=3, offsetY=5.5, scale=0.8, time=0.5)]
[Delay(time=0.5)]
[Tutorial(focusX=0, focusY=0, focusWidth=240, focusHeight=240, anchor="Center", \
          animStyle="Highlight", focusStyle="HighlightRect", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_stward", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
这是<@tu.kw>临时休息舱</>，提升同时可部署的干员人数。

[CooperateBattle.CameraFocusTo(offsetX=3, offsetY=4, scale=1, time=0.5)]
[Delay(time=0.5)]

[CooperateBattle.CameraFocusTo(offsetX=2.5, offsetY=5.5, scale=0.8, time=0.5)]
[Delay(time=0.5)]
[Tutorial(focusX=-80, focusY=0, focusWidth=240, focusHeight=240, anchor="Center", \
          animStyle="Highlight", focusStyle="HighlightRect", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_stward", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
这是<@tu.kw>便携健身架</>，会提高双方干员的生命值。


[CooperateBattle.CameraFocusTo(offsetX=3, offsetY=4, scale=1, time=0.5)]
[Delay(time=0.5)]

[CooperateBattle.CameraFocusTo(offsetX=3, offsetY=3.5, scale=0.8, time=0.5)]
[Delay(time=0.5)]
[Tutorial(focusX=0, focusY=0, focusWidth=280, focusHeight=280, anchor="Center", \
          animStyle="Highlight", focusStyle="HighlightRect", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_stward", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
这是<@tu.kw>建筑工具间</>，为我们带来更多的<@tu.kw>设施建筑工</>。
[CooperateBattle.CameraFocusTo(offsetX=3, offsetY=4, scale=1, time=0.5)]
[Delay(time=0.5)]



[Tutorial(dialogHead="$avatar_stward")]原料箱需要经过数次建造才能投入使用，每个设施建筑工建造了一段时间就会休息。
[Tutorial(dialogHead="$avatar_stward")]如果地形合适，也可以派遣多名建筑工同时建造，加快建造进度。

[InputBlocker(blockInput=true)]
[Battle.Pause(pause=false)]
[Battle.Delay(time=8)]
[Battle.Pause]

[CooperateBattle.CameraFocusTo(offsetX=3, offsetY=5.5, scale=0.8, time=0.5)]
[Delay(time=0.5)]
[Tutorial(focusX=0, focusY=0, focusWidth=240, focusHeight=240, anchor="Center", \
          animStyle="Highlight", focusStyle="HighlightRect", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_stward", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
休息舱已经建造完成了，可以投入使用！

[CooperateBattle.CameraFocusTo(offsetX=3, offsetY=3.5, scale=0.8, time=0.5)]
[Delay(time=0.5)]
[Tutorial(focusX=0, focusY=0, focusWidth=240, focusHeight=240, anchor="Center", \
          animStyle="Highlight", focusStyle="HighlightRect", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_adnach", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
这里的工具间刚刚只有一名建筑工在建造，还不能投入使用。

[Tutorial(focusX=0, focusY=-100, focusWidth=200, focusHeight=100, anchor="Top", \
          animStyle="Highlight", focusStyle="HighlightRect", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_stward", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
没关系，现在还是两波进攻之间的休整阶段......

[CooperateBattle.CameraFocusTo(offsetX=3, offsetY=3.5, scale=0.8, time=0.5)]
[Delay(time=0.5)]
[CooperateBattle.LockCamera(enable=false)]
[InputBlocker(blockInput=true, cardIndex=0, validWidth=112, validHeight=116)]
[Tutorial(waitForSignal="put_down", dialogHead="$avatar_stward", animStyle="Drag", \
          startX=-300, startY=60, startAnchor="BottomRight", endAnchor="Center", endX=0, endY=0)] \
趁还有休整时间，继续部署建筑工吧！
[InputBlocker(blockInput=true)]
[Delay(time=0.5)]
[InputBlocker(blockInput=true, tileX=3, tileY=3, validWidth=600, validHeight=600)]
[Tutorial(waitForSignal="select_direction", dialogHead="$avatar_stward")] \
向<@tu.kw>建筑工具间</>的方向部署建筑工！

[InputBlocker(blockInput=true)]
[Battle.Pause(pause=false)]
[Battle.Delay(time=7)]
[Battle.Pause]


[Tutorial(dialogHead="$avatar_stward")]一切顺利，工具间应该可以投入使用了！
[Tutorial(dialogHead="$avatar_stward")]如果操作失误，没有让建筑工正确地朝向需要建造的原料箱，建筑工会自主返回待部署区，等待下一次派遣。
[CooperateBattle.CameraFocusTo(offsetX=6, offsetY=4, scale=1, time=1)]
[Delay(time=1)]
[Tutorial(focusX=0, focusY=-180, focusWidth=200, focusHeight=60, anchor="Top", \
          animStyle="Highlight", focusStyle="HighlightRect", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_adnach", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
目前已经没有其他准备工作需要做了，可以迎接下一波进攻了！

[CooperateBattle.LockCamera(enable=true)]

[Battle.unlockFunction(mask="PAUSE_BUTTON_INTERACT")]
```

### training_fortress_b0

```
[HEADER(is_tutorial=true, is_skippable=false)] 要塞教学a2

[Battle.lockFunction(mask="PAUSE_BUTTON_INTERACT")]
[Battle.lockFunction(mask="CARD_LIST")]

[Battle.Pause]

[Tutorial(focusX=750, focusY=0,  focusWidth=200,  focusHeight=200, anchor="Center", \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_stward", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
屏幕边缘的红色箭头会提示敌方增援的位置，点击箭头可以将镜头移动到敌方所在位置。

[Battle.unlockFunction(mask="PAUSE_BUTTON_INTERACT")]
[Battle.unlockFunction(mask="CARD_LIST")]


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
这就是<@tu.kw>高台原料箱</>，经过维护能展开成为<@tu.kw>液压式高台</>。
[Tutorial(dialogHead="$avatar_stward")]它需要经过两次建造才能投入使用。
[Tutorial(dialogHead="$avatar_stward")]对了，<@tu.kw>液压式高台</>不仅能部署远程干员，还可以改变敌方的行进路线。

[CooperateBattle.CameraFocusTo(offsetX=11, offsetY=4.5, scale=1, time=0.5)]
[Delay(time=0.5)]
[Tutorial(focusX=0, focusY=0, focusWidth=240, focusHeight=480, anchor="Center", \
          animStyle="Highlight", focusStyle="HighlightRect", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_adnach", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
前面的设施是......
[Tutorial(dialogHead="$avatar_stward")]<@tu.kw>路障原料箱</>，只需要一次建造就能投入使用。
[Tutorial(dialogHead="$avatar_stward")]维护完成后，它会展开成为<@tu.kw>混凝土路障</>，阻挡敌方的脚步。

[Battle.Pause(pause=false)]
[Battle.Delay(time=0.5)]
[Battle.Pause]

[Tutorial(dialogHead="$avatar_stward")]协作者可以共同参与设施建造。
[Tutorial(dialogHead="$avatar_stward")]之前投入使用的工具间带来了更多建筑工，剩下的设施建造就交给博士了！

[CooperateBattle.CameraFocusTo(offsetX=10, offsetY=4, scale=1, time=0.5)]
[Delay(time=0.5)]

[Battle.unlockFunction(mask="PAUSE_BUTTON_INTERACT")]
[Battle.unlockFunction(mask="CARD_LIST")]
```

### training_fortress_c1

```
[HEADER(is_tutorial=true, is_skippable=false)] 要塞教学c1

[Battle.lockFunction(mask="PAUSE_BUTTON_INTERACT")]

[Battle.Pause]
[CooperateBattle.CameraFocusTo(offsetX=16, offsetY=5, scale=1.2, time=1.5)]
[Delay(time=1)]




[Tutorial(focusX=160, focusY=185, focusWidth=210, focusHeight=210, anchor="Center", \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_stward", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
除普通的建筑工之外，每个波次开始时可能会出现被困在瓦砾堆中等待解救的<@tu.kw>高级设施建筑工</>

[Battle.Pause(pause=false)]
[Battle.Delay(time=4)]
[Battle.Pause]


[Tutorial(dialogHead="$avatar_stward")]击倒周围负责看守的敌人，可以解救被困的高级建筑工。

[Battle.Pause(pause=false)]
[Battle.Delay(time=2)]
[Battle.Pause]

[CooperateBattle.CameraFocusTo(offsetX=2.5, offsetY=5.5, scale=0.8, time=0.5)]
[Delay(time=1)]

[CooperateBattle.LockCamera(enable=false)]
[Tutorial(dialogHead="$avatar_stward")]部署高级建筑工继续建设<@tu.kw>I级</>设施，可以使其<@tu.kw>升级</>提供更强的效果。
[Tutorial(dialogHead="$avatar_stward")]比如<@tu.kw>便携健身架</>升至III级后，可以提升双方干员的攻击力和技力回复速度。


[CooperateBattle.CameraFocusTo(offsetX=6, offsetY=4, scale=1, time=1)]
[Delay(time=1)]

[Tutorial(dialogHead="$avatar_stward")]让我们迎接敌人的最后一波进攻吧！
[CooperateBattle.LockCamera(enable=true)]
[Battle.unlockFunction(mask="PAUSE_BUTTON_INTERACT")]
```

### training_fortress_d1

```
[HEADER(is_tutorial=true, is_skippable=false)] 要塞教学b2

[Battle.lockFunction(mask="PAUSE_BUTTON_INTERACT")]
[Battle.lockFunction(mask="CARD_LIST")]




[CooperateBattle.CameraFocusTo(offsetX=16, offsetY=4, scale=1.2, time=1.5)]
[Battle.Delay(time=0.5)]

[Battle.pause]


[CooperateBattle.CameraFocusTo(offsetX=16, offsetY=4, scale=0.6, time=0.5)]
[Delay(time=0.5)]
[Tutorial(focusX=160, focusY=120, focusWidth=240, focusHeight=240, anchor="Center", \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_adnach", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
当完成了所有波次之后，场上会出现一个强大的敌人<@tu.kw>试炼丰碑</>！
[Tutorial(dialogHead="$avatar_stward")]您对它造成的伤害将记入最终的比赛成绩。
[Tutorial(dialogHead="$avatar_stward")]请在限时内尽可能地对它造成更高伤害，完成本次训练。
[CooperateBattle.CameraFocusTo(offsetX=8, offsetY=4, scale=1, time=1.5)]
[Delay(time=1)]

[Battle.unlockFunction(mask="PAUSE_BUTTON_INTERACT")]
[Battle.unlockFunction(mask="CARD_LIST")]
```

### training_multi_v3_01-01_a

```
[HEADER(is_tutorial=true, is_skippable=false)] 联机教学关1a

[Battle.Pause]
[InputBlocker(blockInput=true)]

[PopupDialog(dialogHead="$avatar_amiya")]博士，许久不见！欢迎再次来到促融共竞的比赛现场！

[PopupDialog(dialogHead="$avatar_amiya")]与之前一样，促融共竞的所有项目都需要您与<@tu.kw>一位协作者</>共同参与，这次就还是让我来当博士的协作者吧！

```

### training_multi_v3_01-01_b

```
[HEADER(is_tutorial=true, is_skippable=false)] 联机教学关1b

[Battle.Pause]
[InputBlocker(blockInput=true)]

[PopupDialog(dialogHead="$avatar_amiya")]与之前一样，每场比赛分为两个阶段，每个阶段都有需要完成的目标。

[Tutorial(target="panel_cooperate_normal_and_fortress_status",\
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
本场比赛第一阶段的目标是<@tu.kw>生存</>，我们需要在限定时间内抵挡敌方的进攻。

[PopupDialog(dialogHead="$avatar_amiya")]虽然在同一片赛场上竞技，但我们各自需要防守不同的目标点。

[Tutorial(focusX=-50, focusY=-70, focusWidth=130, focusHeight=130, \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
博士，您需要防守的是蓝色的目标点。敌方进入蓝色目标点，将会扣减您的目标生命值。

[Tutorial(focusX=60, focusY=-70, focusWidth=130, focusHeight=130, \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
墨绿色的目标点由协作者——也就是我来防守。敌方进入墨绿色目标点，则会扣减我的目标生命值。

[Battle.Pause(pause=false)]
[Delay(time=1)]
[Battle.Pause(pause=true)]

[Tutorial(focusX=55, focusY=85, focusWidth=100, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
对了！协作者部署的干员会用特殊的颜色标记出来，这样您就不会混淆双方的干员了。

[Tutorial(focusX=-50, focusY=170, focusWidth=120, focusHeight=120, \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
与上一届赛事不同的是，本届赛事会存在<@tu.kw>共同敌手</>。

[Tutorial(focusX=-15, focusY=200, focusWidth=120, focusHeight=120, \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
当带有这个标记的<@tu.kw>共同敌手</>进入任意一方的目标点时，我们双方都会扣减关卡生命。
```

### training_multi_v3_01-01_c

```
[HEADER(is_tutorial=true, is_skippable=false)]  联机教学关1c

[Battle.Pause]


[PopupDialog(dialogHead="$avatar_amiya")]即使我们之中有一方的目标生命值归零，我们的队伍也不会立刻输掉比赛。


[Battle.Pause(pause=false)]

[Delay(time=2)]
[Battle.Pause(pause=true)]

[Tutorial(focusX=40, focusY=-30, focusWidth=150, focusHeight=150, \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
啊，敌方选手很快就要进入我负责防守的目标点了——我的目标生命值就要归零了......

[Battle.Pause(pause=false)]
[Delay(time=3)]
[Battle.Pause(pause=true)]

[Tutorial(focusX=55, focusY=85, focusWidth=100, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
之后，我部署的干员会停止行动。

[Tutorial(focusX=40, focusY=-70, focusWidth=150, focusHeight=150, \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
但此时，只要您坚守一段时间，阻止敌人继续进入我的目标点——

[Battle.Pause(pause=false)]
[Delay(time=9.2)]
[Battle.Pause(pause=true)]

[Tutorial(focusX=55, focusY=85, focusWidth=100, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
——我就会再度回到赛场，与博士您并肩作战！

[InputBlocker(blockInput=false)]
```

### training_multi_v3_01-01_d

```
[HEADER(is_tutorial=true, is_skippable=false)]  联机教学关1d

[Battle.Pause]
[InputBlocker(blockInput=true)]

[PopupDialog(dialogHead="$avatar_amiya")]为了方便协作者之间的交流互动，主办方还设置了两项辅助功能。

[Tutorial(focusX=-73, focusY=293, focusWidth=144, focusHeight=75, \
          animStyle="Highlight", focusStyle="HighlightRect", black=0.5, anchor="BottomRight", \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
点击右下方的<@tu.kw>请求费用</>，就可以请求协作者向您支援至多15点部署费用。

[Tutorial(target="btn_display_mark",\
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
<@tu.kw>按住</>左下方的<@tu.kw>拖动标记</>，并将其<@tu.kw>拖动</>到赛场上，就可以向协作者发送标记信号。
```

### training_multi_v3_01-01_e

```
[HEADER(is_tutorial=true, is_skippable=false)]  联机教学关1d1

[Battle.Pause]
[InputBlocker(blockInput=true)]
[Battle.Pause(pause=true)]

[PopupDialog(dialogHead="$avatar_amiya")]随后，就来到了中场休整的时间。在场的所有干员都将<@tu.kw>下场</>休息，做好在第二阶段重新登场的准备。
[PopupDialog(dialogHead="$avatar_amiya")]博士休息好了的话，我们就去挑战比赛的第二阶段吧！

[Battle.Pause(pause=false)]
```

### training_multi_v3_01-01_f

```
[HEADER(is_tutorial=true, is_skippable=false)] 活动act1sandbox教学关1_b

[Battle.Pause]
[InputBlocker(blockInput=true)]

[Tutorial(target="bg_timer_slider",\
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
本场比赛第二阶段的目标是<@tu.kw>渗透</>，我们需要深入敌阵，击倒特定的敌方选手。击倒三名拾荒者就可以达成目标！

[Tutorial(target="bg_timer_slider",\
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
如果博士还有余力，也可以向着<@tu.kw>进阶目标</>努力！击倒五名拾荒者，就可以在赛后获得额外的<@tu.kw>嘉奖印章</>！


```

### training_multi_v3_01-01_g

```
[HEADER(is_tutorial=true, is_skippable=false)] 活动act1sandbox教学关1_b

[Battle.Pause]
[InputBlocker(blockInput=true)]

[Tutorial(focusX=600, focusY=-300, focusWidth=250, focusHeight=250, \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
实战中，您需要从多种专项中选择一个进入比赛。每个专项都会提供一种支援装置，让您在战斗中部署！

[InputBlocker(blockInput=true, cardIndex=0, validWidth=112, validHeight=116)]
[Battle.LockFunction(mask="PAUSE_BUTTON_INTERACT")]
[Tutorial(waitForSignal="put_down", dialogHead="$avatar_amiya", animStyle="Drag", \
          startX=-130, startY=60, startAnchor="BottomRight", endAnchor="Center", endX=0, endY=100)] \
这是基础专项的支援装置<@tu.kw>赛场啦啦队</>，部署后可以使协作双方干员的<@tu.kw>攻击力提升</>！
[Battle.UnlockFunction(mask="PAUSE_BUTTON_INTERACT")]
[InputBlocker(blockInput=true)]

[PopupDialog(dialogHead="$avatar_amiya")]现在，我们一起击倒五名拾荒者，完成进阶目标吧！
```

### training_multi_v3_01-02_a

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

### training_multi_v3_01-02_b

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

[PopupDialog(dialogHead="$avatar_amiya")]守门员不仅<@tu.kw>不占用部署人数</>，可以接住飞来的足球。


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

### training_multi_v3_01-02_c

```
[HEADER(is_tutorial=true, is_skippable=false)] 联机教学关1a

[Battle.Pause]
[InputBlocker(blockInput=true)]

[PopupDialog(dialogHead="$avatar_amiya")]不愧是博士！剩下的时间，就交给您了。
[PopupDialog(dialogHead="$avatar_amiya")]破坏阵地屏障、击倒敌方球员，或是找好角度直接射门——设法攻破敌方的球门吧！

```


## 统计

- 总字符数：29584
- 对话行数：0


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
