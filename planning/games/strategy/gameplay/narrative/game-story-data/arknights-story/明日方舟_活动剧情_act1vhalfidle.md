# 明日方舟 · 活动剧情 · act1vhalfidle（5段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act1vhalfidle」完整剧情脚本（5个文件，0行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act1vhalfidle
- 脚本文件数：5

### guide_act1vhalfidle_first

```
[HEADER(is_skippable=false, is_tutorial=true)] 首次进入玩法
[Activity.ResetToEntry]
[Tutorial(waitForSignal="template_act_entry_routed")]
[PopupDialog(dialogHead="char_007_closre_1")] 博士，别对着那一大堆表格挠头啦！为罗德岛的重建工作调度各类资源当然是重中之重，但我也有秘密武器哦——看这里！在终端上像玩电子游戏一样操作，就可以统筹所有的工作哦！
[Tutorial(target="pool_act1vhalfidle_entry_stage_btn", waitForSignal="act1vhalfidle_zone_map_routed", searchBtnInChildren=true,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="char_007_closre_1")] 为了给罗德岛新地块的建造提供充足的资源，我们需要安排人手去往荒地建立生产基地——咳咳，用更专业的说法，就是“前哨支点”。点击这里试试吧！
[Tutorial(target="pool_act1vhalfidle_zone_map_tr_stage", waitForSignal="act1vhalfidle_zone_map_stage_bar_show", searchBtnInChildren=true,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="char_007_closre_1")] 所有的地点都在这里啦，怎么样，是不是一目了然？作为示例，我已经挑好了一处前哨支点，在这里。
[Tutorial(target="pool_act1vhalfidle_zone_map_stage_production", waitForSignal="act1vhalfidle_stage_income_dialog_show", searchBtnInChildren=true,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="char_007_closre_1")] 另外，我帮博士将各个前哨支点的资源产出效率整理在实时更新的面板里了，点击这里就可以查看。
[PopupDialog(dialogHead="char_007_closre_1")] 毕竟是在荒地里，仓储和物流条件都很差，每个前哨支点的资源产出都有上限。另外，每个前哨支点都有自己固定产出的资源类型哦。
[Tutorial(target="pool_act1vhalfidle_stage_income_dialog_close", waitForSignal="act1vhalfidle_stage_income_dialog_hide", searchBtnInChildren=true,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="char_007_closre_1")] 好了好了，我也不想太啰嗦的，可这套系统毕竟是我的得意之作嘛。现在我们就去建设第一座前哨支点吧！
[Tutorial(target="pool_act1vhalfidle_zone_map_stage_start_battle", waitForSignal="common_squad_home_state_show", searchBtnInChildren=true,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="char_007_closre_1")] 下达指令吧，博士！
[Tutorial(target="pool_act1vhalfidle_char_squad_btn_next", waitForSignal="act1vhalfidle_stage_plot_squad_state_show", searchBtnInChildren=true,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="char_007_closre_1")] 我们已经预先将一支先遣队从罗德岛总部调派到荒地了。
[Tutorial(target="pool_act1vhalfidle_plot_squad_plot_list", searchBtnInChildren=true,            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="char_007_closre_1")] 哇哦，终于说到这个了！博士只需要将生产模块部署在场地内，就可以改造地形、规划建筑、产出更多资源，是不是很方便？
[Tutorial(target="pool_act1vhalfidle_plot_squad_group_landscape", searchBtnInChildren=true,            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="char_007_closre_1")] 这些是地形类的生产模块，需要部署在高台位置。
[Tutorial(target="pool_act1vhalfidle_plot_squad_group_roadside", searchBtnInChildren=true,            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="char_007_closre_1")] 这些是设备类的生产模块，需要部署在周围4格范围内存在低地的高台位置。
[Tutorial(target="pool_act1vhalfidle_plot_squad_group_road", searchBtnInChildren=true,            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="char_007_closre_1")] 这些是建筑类的生产模块，可以部署在任意低地位置。
[Tutorial(target="pool_act1vhalfidle_plot_squad_group_special", searchBtnInChildren=true,            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="char_007_closre_1")] 这些是特殊类的生产模块，部署位置需要视情况而定。
[Tutorial(target="pool_act1vhalfidle_plot_squad_group_item_btn_add", waitForSignal="act1vhalfidle_stage_plot_select_state_show", searchBtnInChildren=true,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="char_007_closre_1")] 具体选择哪些生产模块就由博士来决定啦。
[Tutorial(target="pool_act1vhalfidle_plot_select_tip", searchBtnInChildren=true,            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="char_007_closre_1", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 需要注意的是，编入队伍的每种类型的生产模块都要符合数量要求。
[Tutorial(target="pool_act1vhalfidle_plot_squad_group_item", searchBtnInChildren=true,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="char_007_closre_1", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 这个很好用的，就选它吧，嘿嘿！
[Tutorial(target="pool_act1vhalfidle_plot_btn_confirm", waitForSignal="act1vhalfidle_stage_plot_select_state_hide", searchBtnInChildren=true,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="char_007_closre_1")] 点击这里可以将生产模块编入队伍。
[Tutorial(target="pool_act1vhalfidle_plot_squad_tip", searchBtnInChildren=true,            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="char_007_closre_1", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 啊哦，刚刚好像忘记讲了，选择生产模块后，需要先击败场地上的敌人才有可能获得它们哦。
[Tutorial(target="pool_act1vhalfidle_plot_squad_start_battle", searchBtnInChildren=true,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="char_007_closre_1")] 罗德岛的重建工作刻不容缓，博士赶快下达指令吧！
```

### guide_act1vhalfidle_pack

```
[HEADER(is_skippable=false, is_tutorial=true)] 首次进入仓库
[Tutorial(waitForSignal="act1vhalfidle_depot_page_routed")]
[Tutorial(target="pool_act1vhalfidle_depot_recruit_btn", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black=0.5,           protectTime=1.5, dialogHead="char_007_closre_1")] 博士可以通过干员任命，从罗德岛总部调派更多干员来参与前哨支点的建设和资源采集。
[Tutorial(target="pool_act1vhalfidle_depot_char_buff_btn", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black=0.5,           protectTime=1.5, dialogHead="char_007_closre_1", dialogY="$f_lower_dialog_pos_y")] 干员之间会互相协助，博士调派过去的相同职业的干员越多，协作增益就越高。
[Tutorial(target="pool_act1vhalfidle_depot_char_assist_btn", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black=0.5,           protectTime=1.5, dialogHead="char_007_closre_1", dialogY="$f_lower_dialog_pos_y")] 只有被列入战备的干员才能在前哨支点中出战。当然，博士也可以向好友申请协助，将助战干员列入战备。
[Tutorial(target="pool_act1vhalfidle_depot_char_list_first_item", waitForSignal="common_char_select_state_show", searchBtnInChildren=true,           animStyle="Click", focusStyle="HighlightRect", black=0.5,           protectTime=1.5, dialogHead="char_007_closre_1", dialogY="$f_lower_dialog_pos_y")] 博士发现了吗？这里的干员等级发生了变化。
[Tutorial(target="pool_act1vhalfidle_char_select_detail_btn", waitForSignal="act1vhalfidle_char_upgrade_page_routed", searchBtnInChildren=true,           animStyle="Click", focusStyle="HighlightRect", black=0.5,           protectTime=1.5, dialogHead="char_007_closre_1", dialogY="$f_lower_dialog_pos_y")] 平时的战斗训练和生产建设可以说是两码事，所以干员们来到这里之后，都需要重新接受培训，请博士点击这里看看。
[Tutorial(target="pool_act1vhalfidle_char_upgrade_pnl_level_upgrade", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black=0.5,           protectTime=1.5, dialogHead="char_007_closre_1", dialogY="$f_lower_dialog_pos_y")] 在这里，可以给干员进行生产培训，提升干员的培训等级。
[Tutorial(target="pool_act1vhalfidle_char_upgrade_level_upgrade_discount_desc", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black=0.5,           protectTime=1.5, dialogHead="char_007_closre_1", dialogY="$f_lower_dialog_pos_y")] 如果干员在来到这里之前，已经有了较高的精英化等级，那么生产培训需要消耗的材料将相应减少。
[Tutorial(target="pool_act1vhalfidle_char_upgrade_pnl_upgrade_reward", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black=0.5,           protectTime=1.5, dialogHead="char_007_closre_1", dialogY="$f_lower_dialog_pos_y")] 我还为博士准备了一些特别的激励——每次为干员进行精英职称晋升都能获得奖励！
[Tutorial(target="pool_act1vhalfidle_char_upgrade_pnl_skill_upgrade", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black=0.5,           protectTime=1.5, dialogHead="char_007_closre_1")] 在这里，干员各项技能的等级被合并，等级提升后效果将同步到该干员的所有技能上。
[Tutorial(target="pool_act1vhalfidle_char_upgrade_skill_upgrade_discount_desc", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black=0.5,           protectTime=1.5, dialogHead="char_007_closre_1")] 和培训等级一样，干员原本的技能等级越高，在这里提升所消耗的材料就越少。
[PopupDialog(dialogHead="char_007_closre_1")] 需要注意的差不多就这些了，博士快试试吧！
```

### guide_act1vhalfidle_trstage_end

```
[HEADER(is_skippable=false, is_tutorial=true)] 通关教学关后，首次返回关卡界面
[Activity.ResetToEntry]
[Tutorial(waitForSignal="template_act_entry_routed")]
[PopupDialog(dialogHead="char_007_closre_1")] 怎么样，博士，我这套系统用起来还挺顺手的吧？看你适应得不错，可以给你开放新功能了。
[Tutorial(target="pool_act1vhalfidle_entry_depot_btn", searchBtnInChildren=true,            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="char_007_closre_1")] 这是战备入口，派驻到前哨支点的干员信息都在这里了，也可以在这里任命更多干员哦。
[Tutorial(target="pool_act1vhalfidle_entry_tech_tree_btn", searchBtnInChildren=true,            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="char_007_closre_1")] 还记得你桌上那张密密麻麻写满字的生产计划表吗？我把它放到这里了，这样似乎更有动力了，对不对？
[Tutorial(target="pool_act1vhalfidle_entry_harvest_btn", waitForSignal="act1vhalfidle_harvest_page_routed", searchBtnInChildren=true,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="char_007_closre_1")] 想要了解资源产出的情况，就点击这里吧！
[PopupDialog(dialogHead="char_007_closre_1")] 一旦生产效率达标，前哨支点就会稳定运转，按照博士的规划产出我们所需的资源。
[Tutorial(target="pool_act1vhalfidle_harvest_btn", searchBtnInChildren=true,            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="char_007_closre_1")] 资源会临时存放在各个前哨支点内。博士需要在限定时间内下达转运指令，否则前哨支点被堆满，就没办法继续生产了。
[Tutorial(target="pool_act1vhalfidle_harvest_report_btn", waitForSignal="act1vhalfidle_stage_income_dialog_show", searchBtnInChildren=true,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="char_007_closre_1")] 时间紧任务重，生产效率可是最重要的指标呀！博士可以点击这里，随时查看资源产出的效率。
[PopupDialog(dialogHead="char_007_closre_1")] 努力提高生产效率吧，博士！我在罗德岛地块的建设工地上，等着你将资源送来的好消息哦~
```

### level_act1vhalfidle_entry

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK",is_video_only=true)] 
[stopmusic]
[Background(image="bg_black",screenadapt="coverall")]
[playMusic(intro="$empty",key="$empty")]
[Video(res="video/act38side/PV01.mp4")]
```

### training_act1vhalfidle_01_a

```
[HEADER(is_tutorial=true, is_skippable=true)] 次生预案教学关1_a

[InputBlocker(blockInput=true)]
[Delay(time=1.5)]
[Battle.Pause]
[InputBlocker(blockInput=true, black=0.4)]

[PopupDialog(dialogHead="$avatar_closure")]喂，阿米娅，听得到吗？通讯信号已经建立，和大家打个招呼吧，博士。

[PopupDialog(dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]博士，还有可露希尔！先遣队都到齐了，听候博士指挥。

[PopupDialog(dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]只是......目前的后勤物资比较紧张，我们只能就地取材开展建设了。

[Battle.UnlockFunction(mask="CHARACTER_INFO")]
[Battle.UnlockFunction(mask="CHARACTER_MENU")]

[Battle.Pause(pause=false)]
[InputBlocker(blockInput=true, black=0)]
[Delay(time=0.5)]
[Battle.Pause(pause=true)]

[InputBlocker(blockInput=true, cardIndex=1, rightStart=true, validWidth=112, validHeight=116)]

[Tutorial(waitForSignal="put_down", charId="char_002_amiya",posX=1,posY=3, \
          dialogHead="$avatar_closure", animStyle="Drag", \
          startCardIndex=1, startRightStart=true, endTileX=1, endTileY=3)] \
博士，快部署阿米娅，试着先击败那只源石虫吧。

[Delay(time=0.5)]

[InputBlocker(blockInput=true, tileX=2,tileY=3, validWidth=160, validHeight=160)]

[Tutorial(waitForSignal="select_direction", dialogHead="$avatar_amiya", animStyle="Drag", \
          startTileX=2, startTileY=3, endTileX=3, endTileY=3, dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \

[Battle.Pause(pause=false)]
[InputBlocker(blockInput=true)]
[Battle.Delay(time=6)]
[Battle.Pause(pause=true)]
[InputBlocker(blockInput=true, black=0)]

[Tutorial(dialogHead="$avatar_amiya",dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]已击败目标！我好像又积攒了一些新的<@tu.kw>作战经验</>，<@tu.kw>培训等级</>也提升了。

[Tutorial(dialogHead="$avatar_closure")]不止那些，现在我们可以开始对<@tu.kw>环境进行改造</>了。

[Tutorial(focusWidth=100, focusHeight=100, \
          dialogHead="$avatar_closure", animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          cardIndex=0, rightStart=true)] \
          博士应该看到刚刚出现的<@tu.kw>生产模块</>了吧？

[InputBlocker(blockInput=true, cardIndex=0, rightStart=true, validWidth=112, validHeight=116)]

[Tutorial(waitForSignal="char_info",focusWidth=100, focusHeight=100, \
          dialogHead="$avatar_closure", animStyle="Click", focusStyle="HighlightCircle", black="$f_tut_black", \
          cardIndex=0, rightStart=true)] \
          没错，我给复杂的生产系统都换了个相对简单易懂的形式。

[InputBlocker(blockInput=false)]
[Battle.LockFunction(mask="SYSTEM_MENU")]

[Tutorial(waitForSignal="put_down",charId="trap_1500_lhgras", posX=4, posY=3, focusWidth=100, focusHeight=100, \
          dialogHead="$avatar_closure", animStyle="Click", focusStyle="HighlightCircle", \
          tileX=4, tileY=3, black=0)] \
          现在试着部署那片<@tu.kw>草丛</>吧，直接<@tu.kw>点击</>或者拖动操作都可以哦。

[Battle.Pause(pause=false)]
[InputBlocker(blockInput=true)]
[Battle.Delay(time=0.5)]
[Battle.Pause(pause=true)]
[InputBlocker(blockInput=true, black=0)]

[Tutorial(dialogHead="$avatar_amiya",dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]指令已收到......地形改造完成。

[Battle.UnlockFunction(mask="SYSTEM_MENU")]

[Tutorial(focusX=40, focusY=130, focusWidth=100, focusHeight=100, anchor="Left", \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_closure", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]\
          看，<@tu.kw>部署草丛</>会为我们提供一些<@tu.kw>培训手册</>。

[Tutorial(focusX=130,focusY=20, focusWidth=200, focusHeight=200, anchor="Left", \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_closure", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]\
          击败不同的敌人，会获得不同的资源。
          
[Tutorial(dialogHead="$avatar_closure", protectTime=0.5)]同样，妥善利用我准备的这些<@tu.kw>生产装置</>，也能产出许多资源。

[InputBlocker(blockInput=true, black=0)]
[Battle.Pause(pause=false)]
[Battle.Delay(time=6)]
[Battle.Pause(pause=true)]
[InputBlocker(blockInput=true)]

[Tutorial(dialogHead="$avatar_amiya",dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y", black=0, protectTime=0.5)]小心，更多敌人出现了！不过，我还没有观察到目标点的位置。

[Tutorial(dialogHead="$avatar_closure", black=0, protectTime=0.5)]这是因为在前哨支点的战斗中，我们<@tu.kw>不再需要守护目标点</>了。

[Tutorial(dialogHead="$avatar_closure", black=0, protectTime=0.5)]敌人会按照固定路线在场地中行进。

[Tutorial(focusX=-100,focusY=0, focusWidth=120, focusHeight=120, anchor="Top", \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_closure", protectTime=0.5)]\
          如果场地内<@tu.kw>同时存在过多的敌人</>，我们的生产建设就会受到影响，<@tu.kw>目标生命值也会不断流失</>。
[Tutorial(focusX=-100,focusY=0, focusWidth=120, focusHeight=120, anchor="Top", \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y", protectTime=0.5)]\
          也就是说，我们需要及时将这些敌人清除掉，减少敌人的数量。

[InputBlocker(blockInput=true)]
[Battle.Pause(pause=false)]
[Tutorial(waitForSignal="act1vhalfidle_battle_gain_equip")]
[Battle.Pause(pause=true)]
[InputBlocker(blockInput=true)]

[Tutorial(focusX=-35,focusY=110,  focusWidth=90, focusHeight=90, anchor="Right",  \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]\
          欸，这是什么？好像是某种可以提供<@tu.kw>增益</>的物件。

[Tutorial(target="pool_act1vhalfidle_equip_thumbnail_btn", \
          waitForSignal="act1vhalfidle_battle_open_equip_panel", \
          animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_closure")]\
          在博士的指挥界面里，这些可以提供临时增益的物件被我统称为<@tu.kw>“战术插件”</>。

[Delay(time=0.3)]
[Tutorial(target="pool_act1vhalfidle_equip_in_bag_btn", \
          animStyle="Click", focusStyle="Highlight

... (全文8205字符)
```


## 统计

- 总字符数：18870
- 对话行数：0


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
