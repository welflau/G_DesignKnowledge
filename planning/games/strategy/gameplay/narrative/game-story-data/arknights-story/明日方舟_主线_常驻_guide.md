# 明日方舟 · 主线/常驻 · guide（111段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 主线/常驻, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟主线/常驻「guide」完整剧情脚本（111个文件，201行对话）

## 正文
## 章节信息

- 分类：主线/常驻
- 目录：obt/guide
- 脚本文件数：111

### building_intro_new

```
[HEADER(is_skippable=false, is_tutorial=true)] 基建扩建老玩家引导
[PopupDialog(dialogHead="$avatar_closure")] 博士，欢迎回到罗德岛！
[PopupDialog(dialogHead="$avatar_closure")] 这段时间，后勤部派遣工程队对舰船的部分区域进行了升级，下面由我来作详细介绍。
[Building.FocusBRoom(roomId="slot_47", needSelect = false)]
[Delay(time="$f_delay_focus_building_broom")]
[Tutorial(target="building_right_part_all",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 可以看到，基建右侧区域进行了扩建及改造。
[Tutorial(target="build_right_part_new_room",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 功能房间右侧开辟出了<@tu.kw>新的区域</>，扩建后博士可以自由探索。
[Building.FocusBRoom(roomId="slot_36", needSelect = false)]
[Delay(time="$f_delay_focus_building_broom")]
[Tutorial(target="broom_tutorial_btn",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 与此同时，翻新后的<@tu.kw>会客室</>也提供了更大的面积，能更好地支持新功能。
```

### control_intro

```
[HEADER(is_skippable=false, is_tutorial=true)] 基建副手引导
[PopupDialog(dialogHead="$avatar_closure")] 这里就是<@tu.kw>基建控制中心</>了。除了我的小黑屋以外，这里也能算基建的中枢部分了。
[PopupDialog(dialogHead="$avatar_closure")] 在控制中心你可以管理基建的各项事宜，并为罗德岛的基建配置<@tu.kw>副手</>。
[PopupDialog(dialogHead="$avatar_closure")] 副手会担任各种管理工作，也能提高信赖度获取量，这是和干员们拉近关系建立信任的好方式哦。
[Tutorial(target="btn_assist", waitForSignal="building_assist_report_resumed",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 点击打开副手界面
[PopupDialog(dialogHead="$avatar_closure")] 副手是你管理基建的左膀右臂，他们将分别为你管理基建的各个楼层，并提交每日报告。
[PopupDialog(dialogHead="$avatar_closure")] 因为能与你有更多交流，所以副手们在基建中的<@tu.kw>信赖度</>获取量会得到大幅度提升，并且每天可以获取的次数提升至两次。
[Tutorial(target="pool_btn_building_assist_report_first_slot", searchBtnInChildren=true, waitForSignal="squadselect_resumed",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 首先点击设置总副手
[Delay(time="$f_delay_single_frame")]
[Tutorial(target="pool_btn_squad_select_first_item", searchBtnInChildren=true, waitForSignal="squadselect_charcard_selected",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 点击选中干员
[Tutorial(target="panel_hotspot", waitForSignal="building_assist_report_resumed",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black", importantClick=true,           protectTime=0.5, dialogHead="$avatar_closure")] 点击确认设置为副手
[Tutorial(target="pool_btn_building_assist_report_first_slot", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 基建的总副手为你管理整个基建的运作，能够获得最高的信赖度加速。
[Tutorial(target="pool_btn_building_assist_report_second_slot", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 各个楼层的副手则为你管理的各个基建楼层的运作，能够根据相应楼层的宿舍情况获得信赖度加速。
[PopupDialog(dialogHead="$avatar_closure")] 和前面说的一样————建议博士你将当前最想要增进交流的干员设置为基建副手。
[PopupDialog(dialogHead="$avatar_closure")] 大致就是这些了。如果有不明白的，回头看一下提示就行了。
```

### dorm_intro

```
[HEADER(is_skippable=false, is_tutorial=true)] 基建宿舍引导
[PopupDialog(dialogHead="$avatar_closure")] 欢迎来到罗德岛的<@tu.kw>宿舍</>。
[PopupDialog(dialogHead="$avatar_closure")] 宿舍是干员们在工作繁忙之余休息的地方，在这里可以让他们放松，回复心情值。
[Tutorial(target="bg_dorm_leftbtm",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 这里标识了该宿舍的<@tu.kw>氛围值</>和相应的<@tu.kw>心情值</>回复量。
[Tutorial(target="bg_dorm_leftbtm",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 氛围值越高，心情值回复的速度就越快。你可以在装扮商店中购置新的家具来提高宿舍的氛围值，同时也让宿舍更美观。
[Tutorial(target="btn_diy_shop",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 装扮商店可以从此处快速进入。
[PopupDialog(dialogHead="$avatar_closure")] 在<@tu.kw>装扮商店</>中购买到的家具还需要摆放在宿舍中才能生效。
[Tutorial(target="btn_diy_entry",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 可以从此进入装扮模式来放置家具。
[PopupDialog(dialogHead="$avatar_closure")] 啊，差点忘了。家具并不是只能从<@tu.kw>装扮商店</>中获得的。
[PopupDialog(dialogHead="$avatar_closure")] 如果运气特别好的话，在部分<@tu.kw>作战行动</>完成时，说不定也能获得的家具哦！
[PopupDialog(dialogHead="$avatar_closure")] 总之，干员们的工作状态对罗德岛基建的稳定运行有着很大的影响。
[PopupDialog(dialogHead="$avatar_closure")] 希望博士也能时常关注干员们的身体情况，合理调配干员的休息时间。博士也是哦。
[PopupDialog(dialogHead="$avatar_closure")] 我？啊啊......博士不用担心我。其实本来我就是适合在夜间活动的。
[PopupDialog(dialogHead="$avatar_closure")] “夜晚，就是用来通宵的。”
[PopupDialog(dialogHead="$avatar_closure")] 其实对我的族群来说，“通宵”应该是指早上不睡觉。
```

### drone_accel

```
[HEADER(is_skippable=false, is_tutorial=true)] 无人机加速引导
[PopupDialog(dialogHead="$avatar_sys")] 无人机加速制造功能已解锁。
[Tutorial(target="btn_labor_accel", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 好极了！谢谢你PRTS。现在制造产品时可以派遣无人机进行辅助，消耗一定的空闲无人机数量可以大大加速产品制造。
```

### drone_exchange

```
[HEADER(is_skippable=false, is_tutorial=true)] 理智兑换无人机
[PopupDialog(dialogHead="$avatar_sys")] 理智恢复无人机功能已解锁。
[Tutorial(target="btn_labor_detail", searchBtnInChildren=true,           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 好，点击打开无人机功能面板吧
[PopupDialog(dialogHead="$avatar_closure", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 现在消耗理智可以立即使一部分无人机成为可以工作的状态。这一定能帮博士加速基建的发展。
```

### hr_intro

```
[HEADER(is_skippable=false, is_tutorial=true)] 基建人力办公室引导
[PopupDialog(dialogHead="$avatar_closure")] 欢迎来到人力办公室。
[PopupDialog(dialogHead="$avatar_closure")] 人力办公室负责帮助罗德岛在公开招募中招募到更优质的干员。
[PopupDialog(dialogHead="$avatar_closure")] 为此，博士你需要为人力办公室配置相应的工作人员。
[Tutorial(target="panel_hiring",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 此处可以为人力办公室进驻干员，提高效率
[Tutorial(target="panel_hiring",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 干员在进驻了以后，会为你自动搜寻<@tu.kw>人脉</>。当人脉提示条显示为满时，你便可以在<@tu.kw>公开招募</>中额外获得一次刷新标签的机会。
```

### meeting_intro

```
[HEADER(is_skippable=false, is_tutorial=true)] 基建会议室引导
[PopupDialog(dialogHead="$avatar_closure")] 欢迎来到<@tu.kw>会客室</>！
[PopupDialog(dialogHead="$avatar_closure")] 会客室是你和好友相互交流的场所，下面我将为你做一个简单的介绍。
[Tutorial(target="panel_meeting", searchBtnInChildren=true, waitForSignal="building_meeting_routed",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 点击打开线索界面
[PopupDialog(dialogHead="$avatar_sys")] 在线索界面你可以与好友互相交换线索，这些情报来自各个地方，并通过搜集线索获得<@tu.kw>信用点数</>。
[Tutorial(target="station_char", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 这里可以为会客室进驻角色。进驻的角色会为你自动搜集线索。
[Tutorial(target="product_button", searchBtnInChildren=true, waitForSignal="building_meeting_clue_product_toggled",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 点击此处查看线索的生成情况
[Tutorial(focusX=-152, focusY=-9, focusWidth=321, focusHeight=482,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 左边部分代表了进驻干员的线索搜集进度，在线索库存达到上限之前会一直进行。
[Tutorial(focusX=166, focusY=-14, focusWidth=316, focusHeight=482,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 右边部分是会客室自动的线索生成进度，领取后会在每天固定时刻刷新。
[Tutorial(target="close_btn_hotspot", waitForSignal="building_meeting_clue_product_toggled",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 点击退出线索生成页面
[PopupDialog(dialogHead="$avatar_closure")] 除了能够自己搜集线索以外，还能够从好友处接受线索。
[PopupDialog(dialogHead="$avatar_closure")] 不过从好友处获得的线索是有时间限制的，请在获取后尽快使用。
[Tutorial(target="recv_button", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 从此处查看好友传递来的线索
[PopupDialog(dialogHead="$avatar_closure")] 你也可以把自己多余的线索传递给好友。这样不仅可以帮助好友搜集线索，也可以立即获得一定<@tu.kw>信用点数</>。
[Tutorial(target="send_button", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 从此处给好友传递线索
[Tutorial(focusX=53, focusY=1, focusWidth=782, focusHeight=497,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 当你搜集到了所有七种线索以后，就可以将它们解锁。
[Tutorial(focusX=53, focusY=1, focusWidth=782, focusHeight=497,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 线索被解锁以后会在一段时间后获得大量的信用点数，并且这段时间内访问你基建的好友可以额外获得<@tu.kw>信用点数</>。
[Tutorial(target="unlock_button",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 点击此处解锁所有线索
```

### meeting_intro_v2_np

```
[HEADER(is_skippable=false, is_tutorial=true)] 会议室新引导
[PopupDialog(dialogHead="$avatar_closure")] 欢迎来到<@tu.kw>会客室</>！
[PopupDialog(dialogHead="$avatar_closure")] 会客室是你和好友相互交流的场所，一起来看看吧！
[Tutorial(target="panel_furn_btn_tutorial",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 点击<@tu.kw>家具互动按钮</>，能够高亮所有可交互家具和功能家具。功能家具会出现对应按钮，点击即可打开相应界面。
[Tutorial(target="btn_diy_entry",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 点击<@tu.kw>装扮模式按钮</>能对会客室家具进行调整布置。
[Tutorial(target="panel_meeting", searchBtnInChildren=true, waitForSignal="building_meeting_routed",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 点击打开<@tu.kw>线索界面</>。
[PopupDialog(dialogHead="$avatar_sys")] 在线索界面你可以与好友互相传递线索，这些情报来自不同组织，通过搜集线索可获得<@tu.kw>信用点数</>。
[Tutorial(target="station_char", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 这里可以为会客室进驻角色。进驻的角色会为你自动搜集线索。
[Tutorial(target="product_button", searchBtnInChildren=true, waitForSignal="building_meeting_clue_product_toggled",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 点击此处查看线索的生成情况。
[Tutorial(focusX=-152, focusY=-9, focusWidth=321, focusHeight=482,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 左边部分代表了进驻干员的线索搜集进度，在线索库存达到上限之前会一直进行。
[Tutorial(focusX=166, focusY=-14, focusWidth=316, focusHeight=482,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 右边部分是会客室自动的线索生成进度，领取后会在每天固定时刻刷新。
[Tutorial(target="close_btn_hotspot", waitForSignal="building_meeting_clue_product_toggled",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 点击退出线索生成页面。
[PopupDialog(dialogHead="$avatar_closure")] 除了能够自己搜集线索以外，还能够从好友处接受线索。
[PopupDialog(dialogHead="$avatar_closure")] 不过从好友处获得的线索是有时间限制的，请在获取后尽快使用。
[Tutorial(target="recv_button", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 从此处查看好友传递来的线索。
[PopupDialog(dialogHead="$avatar_closure")] 你也可以把自己多余的线索传递给好友。这样不仅可以帮助好友搜集线索，也可以立即获得一定<@tu.kw>信用点数</>。
[Tutorial(target="send_button", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 从此处给好友传递线索。
[Tutorial(focusX=53, focusY=1, focusWidth=782, focusHeight=497,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 当你搜集到了所有七种线索以后，就可以将它们解锁。
[Tutorial(focusX=53, focusY=1, focusWidth=782, focusHeight=497,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 线索被解锁以后会在一段时间后获得大量的信用点数，并且这段时间内访问你基建的好友可以额外获得<@tu.kw>信用点数</>。
[Tutorial(target="unlock_button",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 点击此处解锁所有线索。
```

### meeting_intro_v2_op

```
[HEADER(is_skippable=false, is_tutorial=true)] 会议室新引导老玩家补充
[PopupDialog(dialogHead="$avatar_closure")] 欢迎来到<@tu.kw>会客室</>！
[PopupDialog(dialogHead="$avatar_closure")] 这段时间，工程队翻新了会客室，扩大了整个房间的面积。如今，会客室也可以进行<@tu.kw>装扮</>了！
[Tutorial(target="panel_furn_btn_tutorial",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 点击<@tu.kw>家具互动按钮</>，能够高亮所有可交互家具和功能家具。功能家具会出现对应按钮，点击即可打开相应界面。
[Tutorial(target="btn_diy_entry",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 点击<@tu.kw>装扮模式按钮</>能对会客室家具进行调整布置。
```

### private_intro

```
[HEADER(is_skippable=false, is_tutorial=true)] 个人房间引导
[PopupDialog(dialogHead="$avatar_closure")] 欢迎来到<@tu.kw>活动室</>！
[PopupDialog(dialogHead="$avatar_closure")] 活动室是新扩建的房间，让我们看看它有什么特别之处吧！
[Tutorial(target="btn_diy_entry",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 与宿舍相似，为活动室<@tu.kw>布置家具</>，可以提高房间的<@tu.kw>氛围值</>，让干员拥有一个更加舒适的活动空间。
[Tutorial(target="panel_info_private_select_char_hotspot",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 房间的整体氛围值标注在左下角。
[Tutorial(target="panel_info_private_select_char_hotspot", searchBtnInChildren=true, waitForSignal="any",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 邀请干员使用活动室后，可以提升干员<@tu.kw>信赖</>，并能够开启行动模式<@tu.kw>引导干员行动</>。
[Tutorial(target="private_char_no_drawing_tut", searchBtnInChildren=true,waitForSignal="any",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 点击<@tu.kw>邀请</>干员使用活动室。
```

### private_owner

```
[HEADER(is_skippable=false, is_tutorial=true)] 个人房间行动模式引导
[Tutorial(target="private_char_no_drawing_tut", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 每名干员最多使用<@tu.kw>一间</>活动室，正在使用活动室的干员仍能担任基建副手或进驻其他设施。
[Tutorial(target="private_no_drawing_call_back", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 当使用者不在活动室内时，可以点击<@tu.kw>召回</>按钮呼唤其回到活动室。
[Building.Privatereturn()]
[PopupDialog(dialogHead="$avatar_closure")] 请尝试<@tu.kw>选中干员</>。
```

### private_owner_controller

```
[HEADER(is_skippable=false, is_tutorial=true)] 个人房间行动模式引导
[Building.Focusonprivateowner()]
[PopupDialog(dialogHead="$avatar_closure")]选中正在使用活动室的干员，会弹出行动引导按钮。
[Tutorial(target="panel_char_private_op_btn_hotspot", searchBtnInChildren=true ,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 点击进入<@tu.kw>行动模式</>。
[PopupDialog(dialogHead="$avatar_closure")] 在行动模式下，可以通过<@tu.kw>滑动屏幕</>引导干员，在全基建范围内进行跨房间移动。
[Tutorial(target="panel_touch",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 靠近座椅、床等家具时，可以点击交互按钮与<@tu.kw>家具</>进行互动；靠近电梯时，也可以点击按钮<@tu.kw>乘坐电梯</>。
[Tutorial(target="panel_back",searchBtnInChildren=true ,            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 如果想离开行动模式，可以在此处点击<@tu.kw>退出按钮</>，回到常规模式。
```

### trade_lv3

```
[HEADER(is_skippable=false, is_tutorial=true)] 贸易站3级
[PopupDialog(dialogHead="$avatar_sys")] <@tu.kw>谈判策略</>功能已解锁
[Tutorial(target="btn_switch_strategy", waitForSignal="building_trading_negotiation_resumed",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 点击查看谈判策略
[PopupDialog(dialogHead="$avatar_closure")] 贸易站会<@tu.kw>完全依据谈判策略</>来获取相应的订单，博士请根据实际情况进行选择。
[PopupDialog(dialogHead="$avatar_closure")] 选择<@tu.kw>龙门商法</>策略会让贸易站生成龙门币订单，而选择<@tu.kw>开采协力</>策略则会让贸易站只生成合成玉订单。
```

### workshop_op

```
[HEADER(is_skippable=false, is_tutorial=true)] 控制中枢3级 Part5
[PopupDialog(dialogHead="$avatar_closure")] 加工站主要用于材料的<@tu.kw>合成</>和<@tu.kw>分解</>。
[PopupDialog(dialogHead="$avatar_closure")] 由于技术的改进，材料的合成和分解几乎可以在短时间内由机器自动完成，节约了宝贵的时间。
[Tutorial(target="character_station",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 虽然加工过程是全自动的，但加工站中同样可以进驻干员。
[Tutorial(target="character_station",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 在进驻角色的状态下进行加工的话，除了通常的产出外，有时会出现加工副产物，给你带来意外惊喜。
[Tutorial(target="character_station",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 不过相应地，每次加工时也会一定程度消耗干员的心情值，如何取舍就看博士你的安排了。
[PopupDialog(dialogHead="$avatar_closure")] 最后来尝试进行一次加工吧。
[Tutorial(target="formula_frame", searchBtnInChildren=true, waitForSignal="building_workshop_formula_resumed",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 点击选择加工配方
[Tutorial(target="panel_tab_build", searchBtnInChildren=true, waitForSignal="building_workshop_formula_filter_toggled",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 选择基建材料分类
[Delay(time="$f_delay_single_frame")]
[Tutorial(target="pool_btn_building_workshop_formula_first_item", searchBtnInChildren=true, waitForSignal="building_workshop_home_resumed",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 点击选中配方
[Tutorial(target="start_work_btn", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 点击这里就可以开始加工了
```

### 0_welcome_to_guide

```
[HEADER(is_tutorial=true, is_skippable=true, is_autoable=true, fit_mode="BLACK_MASK", deny_auto_switch_scene=true)] 初始引导
[PlayMusic(key="$babel_loop", volume=0.8, delay=0.2)]
[name=""]   哦，是你。
[Dialog]
[Image(image="bg_0_babel", fadetime=1, block=true)]
[ImageTween(image="bg_0_babel", tiled=true, xScaleTo=1.05, yScaleTo=1.05, duration=3, block=false)]
[ImageTween(image="bg_0_babel", tiled=true, xScaleTo=1.5, yScaleTo=1.5, duration=75, block=false)]
[name=""]   离我们上一次见面，已经过去了很久。
[name=""]   这段时间里......你一直徘徊在悬崖的边缘。
[Dialog]
[Delay(time=1.3)]
[name=""]   你可能已经忘记了你的身份，但你还记得那个名字，这就够了。
[Dialog]
[name=""]   ——好了，别在这里逗留太久。
[name=""]   毕竟，你既不是我的客人，也不应该出现在这里。
[name=""]   她需要你。
[Dialog]
[Delay(time=1)]
[name=""]   12月23日。
[name=""]   你可能记不清这一天对你来说，究竟意味着什么。
[name=""]   这会让你陷入十分危险的处境。
[name=""]   ......
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Image]
[name=""]   不。
[name=""]   你必须想起来。
[Dialog]
[PlayMusic(intro="$ekg_loop", key="$ekg_loop", volume=0.8, delay=0)]
[Blocker(a=1, r=255, g=255, b=255, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=1)]
[Image(image="bg_0_am", tiled=true, fadetime=0, block=false)]
[Blocker(a=0, fadetime=0.3, block=true)]
[CameraEffect(effect="Grayscale", fadetime=18, amount=0, block=false)]
[Delay(time=2)]
[name="模糊的声音"]   ......知觉......
[name="模糊的声音"]   开始循环............阻升主......停跳液注入完成......
[Dialog]
[Delay(time=2)]
[CameraEffect(effect="Grayscale", fadetime=8, amount=1, block=false)]
[name="模糊的声音"]   ......体温过低............海克塞米松20cc，静推。
[Dialog]
[CameraEffect(effect="Grayscale", fadetime=8, amount=0, block=false)]
[Delay(time=1)]
[name="模糊的声音"]   止血钳！
[name="模糊的声音"]   ......状态正常......开始切除......注意室颤......
[Dialog]
[Delay(time=1)]
[name="模糊的声音"]   ......抱歉......
[name="模糊的声音"]   又让你受苦了。
[Delay(time=0.5)]
[StopMusic(fadetime=1)]
[Background(fadetime=1, block=false)]
[PlaySound(key="$flashback", volume=0.3)]
[PlaySound(key="$e_atk_arrow_h", volume=0.2, Delay=0.4)]
[PlaySound(key="$flashback", volume=0.1, Delay=0.3)]
[PlaySound(key="$flashback", volume=0.2, Delay=0.7)]
[Blocker(a=1, r=255, g=255, b=255, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=1, r=159, g=254, b=255, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0.8, r=255, g=96, b=15, afrom=1, rfrom=14, gfrom=0, bfrom=15, fadetime=0.2, block=true)]
[Blocker(a=0.8, r=0, g=0, b=0, afrom=0.8, rfrom=255, gfrom=96, bfrom=15, fadetime=0.3, block=true)]
[delay=0.5]
[Blocker(a=1, r=0, g=0, b=0, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.3, block=true)]
[delay=1]
[Blocker(a=1, r=225, g=225, b=225, afrom=1, rfrom=0, gfrom=0, bfrom=0, fadetime=2, block=true)]
[Image(fadetime=0)]
[Image(image="avg_0_2",x=-100, y=-50,xScale=1.3, yScale=1.3, fadetime=0)]
[name="？？？"]   ......
[name="？？？"]   博士......
[Blocker(a=0, fadetime=10, block=false)]
[name="？？？"]   .......手！
[name="？？？"]   抓......紧！
[name="？？？"]   抓紧我的手！！
[Dialog(time=1)]
[Delay(time=1)]
[Blocker(a=0, fadetime=2, block=false)]
[Delay(time=3)]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.8, crossfade=1, delay=0.5)]
[Image(image="avg_0_1",x=-100, y=-50,xScale=1.3, yScale=1.3, fadetime=2)]
[ImageTween(xFrom=-100, yFrom=-50, xTo=0, yTo=0, xScaleFrom=1.3, yScaleFrom=1.3, xScaleTo=1, yScaleTo=1, duration=35, block=false)]
[name="？？？"]   ......
[name="？？？"]   紧急......
[name="？？？"]   ......救......
[name="？？？"]   ......束了......！
[Dialog]
[Image(fadetime=2)]
[Delay(time=2)]
[Delay(time=1)]
[Dialog]
[Character(name="char_002_amiya_1#1")]
[name="？？？"]   博士，博士！
[Delay(time=1)]
[Dialog]
[name="？？？"]   医生，博士他还好吗？
[name="？？？"]   刚才，刚才博士......明明已经拉住我的手了。
[name="？？？"]   但是到现在，博士都没有清醒......怎么办......
[Character(name="char_016_medic")]
[name="医疗干员"]   阿米娅！别那么着急，稍微冷静点！
[Character(name="char_016_medic",name2="char_002_amiya_1#4",focus=2)]
[name="阿米娅"]   啊......抱，抱歉。
[Character(name="char_016_medic",name2="char_002_amiya_1#4",focus=1)]
[name="医疗干员"]   一遇到和博士有关的事情，你就变得慌慌张张的。
[name="医疗干员"]   只不过，阿米娅，如果博士还是.....你该怎么办？
[Character(name="char_016_medic",name2="char_002_amiya_1#4",focus=2)]
[name="阿米娅"]   ——我做好心理准备了。就像我们之前说的那样做。
[Character(name="char_016_medic",name2="char_002_amiya_1#4",focus=1)]
[name="医疗干员"]   ......我知道了。就按你说的做。
[Character(name="char_016_medic",name2="char_002_amiya_1#1",focus=2)]
[name="阿米娅"]   那就......拜托你了。
[Character(name="char_016_medic",name2="char_002_amiya_1#4",focus=2)]
[name="阿米娅"]   那博士......
[Character(name="char_016_medic",name2="char_002_amiya_1#4",focus=1)]
[name="医疗干员"]   放心吧阿米娅，博士的状况已经稳定了。
[name="医疗干员"]   我再检查一次好了，包在我身上。
[Character(name="char_016_medic",name2="char_002_amiya_1#4",focus=2)]
[name="阿米娅"]   那就......拜托你了！
[Delay(time=1)]
[Dialog]
[Character(name="char_016_medic")]
[name="医疗干员"]   嗯。呼吸比较微弱，血压正常。应该不要紧的。
[Blocker(a=0.6, r=255, g=150, b=13, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_atk_blunt_n")]
[CameraShake(duration=0.5, xstrength=3, ystrength=4, vibrato=30, randomness=90, block=true)]
[Blocker(a=0, fadetime=0.2, block=true)]
[Background(image="bg_indoor_1", width=1, height=1, fadetime=0.5, block=true)]
[Character(name="char_002_amiya_1#6")]
[name="阿米娅"]   ——！
[Character(name="char_016_medic")]
[name="医疗干员"]   ......
[name="医疗干员"]   你醒了？
[name="医疗干员"]   阿米娅，成功了，博士清醒了！
[Character(name="char_002_amiya_1#3")]
[name="阿米娅"]   博士......？
[name="阿米娅"]   太好了，太好了......博士......
[Character(name="char_016_medic")]
[name="医疗干员"]   啊，小心！你现在还不能......
[Blocker(a=0.5, r=1, g=0.5, b=0.5, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0,fadetime=0.1, block=true)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=15, randomness=90, fadeout=true, block=false)]
[Character(name="char_016_medic")]
[name="医疗干员"]   先别动，你的身体还没有完全适应。
[Character(name="char_002_amiya_1#4")]
[name="阿米娅"]   博士......？
[Delay(time=1)]
[Dialog]
[Character(name="char_002_amiya_1#3", focus=-1)]
[Decision(options="你们......是谁？", values="1")]
[Predicate

... (全文13607字符)
```

### 1a_guide_1to2

```
[HEADER(is_tutorial=true, is_skippable=true, fit_mode="BLACK_MASK", deny_auto_switch_scene=true)] 引导1到引导2(a)
[Character(name="$ill_amiya_normal")]
[Blocker(afrom=1, a=0, fadetime=1, block=true)]
[name="阿米娅"]   博士，小心另一个方向！
[SkipToThis]
[StartBattle(stageId="guide_02")]
[Tutorial(waitForSignal="battle_start")]
```

### 1b_guide_1to2

```
[HEADER(is_tutorial=true, is_skippable=true, fit_mode="BLACK_MASK", deny_auto_switch_scene=true)] 引导1到引导2(b)
[Character(name="$ill_amiya_normal")]
[Blocker(afrom=1, a=0, fadetime=1, block=true)]
[name="阿米娅"]   刚才发生了什么？博士一句话没说，仿佛整个时间都停止了......
[Character(name="$ill_amiya_normal", focus=-1)]
[name="？？？"]   记录显示Dr.{@nickname}切换了当前执行的应用程序。
[Character(name="$ill_amiya_normal", focus=0)]
[name="阿米娅"]   原来如此，那就让博士回到刚才的环境里吧。战斗还在继续。
[SkipToThis]
[StartBattle(stageId="guide_02")]
[Tutorial(waitForSignal="battle_start")]
```

### 2_guide_to_home

```
[HEADER(is_tutorial=true, is_skippable=true, is_autoable=true, fit_mode="BLACK_MASK", deny_auto_switch_scene=true)] 引导2到主界面
[stopmusic(fadetime=1)]
[Background(image="bg_indoor_1", width=1, height=1, fadetime=1)]
[Delay(time=1)]
[Character(name="char_013_riop")]
[name="近卫干员"]   最后一个！
[CameraShake(duration=1.5, xstrength=7, ystrength=5, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="char_1002_nsabr_2")]
[Blocker(a=1, r=255, g=255, b=255, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, fadetime=1.5, block=false)]
[name="整合运动成员"]   呃啊！
[Character(name="char_013_riop")]
[Dialog]
[Character(fadetime=0)]
[Delay(time=0.5)]
[PlayMusic(intro="$escape_intro", key="$escape_loop", volume=0.8, crossfade=1.5)]
[Character(name="char_013_riop")]
[name="近卫干员"]   剩余目标已清除。敌方小队溃退了！
[name="近卫干员"]   ......Dr.{@nickname}的指挥确实和阿米娅说的一样，让人放心。
[Character(name="char_002_amiya_1#10")]
[name="阿米娅"]   是吧，轻轻松松吧？
[name="阿米娅"]   博士曾经经历的，可不只是这种程度的战斗。
[Character(fatetime=0.5, block=true)]
[delay=1]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.8, block=true)]
[Character(name="char_1002_nsabr_2")]
[name="整合运动成员"]   咳......怎么会出现......乌萨斯人以外的阻碍......
[name="整合运动成员"]   不会......让你们阻挠我们的事业！
[dialog]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$p_imp_whip_h")]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[CameraShake(duration=0.6, xstrength=5, ystrength=8, vibrato=30, randomness=90, block=true)]
[Character(name="char_1002_nsabr_2")]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="char_130_doberm_ex")]
[name="？？？"]   别想得逞！
[Character(name="char_013_riop")]
[name="近卫干员"]   杜，杜宾教官！
[Character(name="char_013_riop", name2="char_130_doberm_ex", focus=2)]
[name="杜宾"]   你在发什么呆！差一点，你就要被打成筛子了！
[Character(name="char_013_riop", name2="char_130_doberm_ex", focus=1)]
[name="近卫干员"]   对，对不起！
[Character(name="char_013_riop", name2="char_130_doberm_ex", focus=2)]
[name="杜宾"]   快！重整队形！
[Character(name="char_013_riop", name2="char_130_doberm_ex", focus=1)]
[name="近卫干员"]   是！
[Character(name="char_002_amiya_1#2")]
[name="阿米娅"]   杜宾！你来了！
[Character(name="char_002_amiya_1#2", name2="char_130_doberm_ex", focus=2)]
[name="杜宾"]   情况紧急。我的小组也遭到了攻击，敌人同样是整合运动。
[name="杜宾"]   所以我才立刻赶过来跟你们汇合。
[Character(name="char_002_amiya_1#2", name2="char_130_doberm_ex", focus=1)]
[name="阿米娅"]   整合运动为什么会攻击我们......？
[Character(name="char_002_amiya_1#2", name2="char_130_doberm_ex", focus=2)]
[name="杜宾"]   一个感染者权益组织......本来我觉得他们只是有点盲目激进————
[name="杜宾"]   ————现在居然开始使用暴力，还是在乌萨斯的城市？真是自寻死路。
[name="杜宾"]   接下来，这里只会变得更加混乱。
[name="杜宾"]   阿米娅，我们必须立刻撤离切尔诺伯格。
[Character(name="char_002_amiya_1#1", name2="char_130_doberm_ex", focus=1)]
[name="阿米娅"]   好的。我们已经成功救出博士，之后按照计划撤退就可以了。
[Delay(time=0.5)]
[Character(name="char_130_doberm_ex")]
[name="杜宾"]    ——这位就是Dr.{@nickname}？
[Character(name="char_002_amiya_1")]
[name="阿米娅"]   是，是的。
[Character(name="char_130_doberm_ex")]
[name="杜宾"]    Dr.{@nickname}，你可能不认识我，但你认识阿米娅，为了你的安全着想——
[Character(name="char_002_amiya_1", name2="char_130_doberm_ex", focus=1)]
[name="阿米娅"]   不不......
[name="阿米娅"]   唔，杜宾，博士目前的状态并不是很好。
[name="阿米娅"]   简单地说，博士......失忆了。
[Character(name="char_002_amiya_1", name2="char_130_doberm_ex", focus=2)]
[name="杜宾"]    失忆？
[name="杜宾"]    ......这怎么办？你还准备将指挥权交给这个......
[Character(name="char_002_amiya_1", name2="char_130_doberm_ex", focus=1)]
[name="阿米娅"]   博士依然有能力指挥小队。
[name="阿米娅"]   ......至少，在刚才的战斗中，我已经确认了。
[Character(name="char_002_amiya_1", name2="char_130_doberm_ex", focus=2)]
[name="杜宾"]   ......
[name="杜宾"]   我还是不能这么简单就相信一个陌生人。
[name="杜宾"]   但我相信你，阿米娅。
[Character(name="char_002_amiya_1", name2="char_130_doberm_ex", focus=1)]
[name="阿米娅"]   ......我知道了。
[Character(name="char_130_doberm_ex")]
[name="杜宾"]   Dr.{@nickname}， 我是行动组E1组长，杜宾。
[name="杜宾"]   我们将把你从这座乌萨斯的城市——切尔诺伯格，护送到罗德岛。
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[image(image="avg_map_1")]
[ImageTween(image="avg_map_1", tiled=true, xScaleTo=1.3, yScaleTo=1.3, xTo=-200, duration=75, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.8, block=true)]
[name="杜宾"]   身处切尔诺伯格城的核心区废弃设施，现在的我们理应向西撤退。
[Character(name="char_002_amiya_1", name2="char_130_doberm_ex", focus=1)]
[ImageTween(image="avg_map_1", tiled=true, xScaleTo=1.8, yScaleTo=1.8, xTo=-200, duration=75, block=false)]
[name="阿米娅"]   但......和凯尔希医生通讯中断时，我和杜宾教官都需要先带领着各自的小组，去西边的集结地汇合然后确认撤出信号。
[name="阿米娅"]   按照计划，原本是这样的......
[name="杜宾"]    如果能这么顺利就好了。
[name="杜宾"]    今天是我们从石棺救走你的最后机会，Dr.{@nickname}。
[name="杜宾"]    只是......我总有种不祥的预感。
[character]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[image]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.8, block=true)]
[Character(name="char_016_medic", name2="char_002_amiya_1", focus=1)]
[name="医疗干员"]   阿，阿米娅！
[Character(name="char_016_medic", name2="char_002_amiya_1#6", focus=2)]
[name="阿米娅"]   怎么了?
[Character(name="char_016_medic", name2="char_002_amiya_1#6", focus=1)]
[name="医疗干员"]   是......是来自罗德岛的对话请求！
[Character(name="char_002_amiya_1#6", focus=-1)]
[name="阿米娅"]   通讯接上了吗！难道说，是凯尔希医......
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Character(name="char_002_amiya_1#6", focus=-1)]
[name="？？？"]   很抱歉，并不是。
[image(image="bg_2_call")]
[PlaySound(key="$d_gen_transmissionget",volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.8, block=true)]
[Character(name="char_002_amiya_1#1", focus=1)]
[name="阿米娅"]   PRTS......？
[Character(name="char_002_amiya_1#1", focus=-1)]
[name="PRTS"]   应急神经连接请求被意外触发了。
[name="PRTS"]   罗德岛号方面也受到干扰，只有神经连接可以勉强进行。
[name="PRTS"]   无法用电波通讯联系到尚未回到罗德岛的凯尔希。
[name="PRTS"]   已经确认过阿米娅您的安全，那么我的任务就已经完成了。
[Character(name="char_130_doberm_ex")]
[name="杜宾"]   这东西......
[name="杜宾"]   现在真的是时候吗？
[Character(name="char_002_amiya_1#1", focus=-1)]
[name="PRTS"]   不需要使用您的神经连接操作罗德岛的话，我将在稍后断开连接。
[name="PRTS"]   如果打扰到了您的派对，万分抱歉。
[Character(name="char_002_amiya_1#5", focus=1)]
[name="阿米娅"]   不不！别挂断......我需要你帮个忙。
[name="阿米娅"]   杜宾，博士需要这些帮助。
[Character(name="char_13

... (全文7325字符)
```

### guide_bossrush_relic

```
[HEADER(is_skippable=false, is_tutorial=true)] BossRush遗物使用引导
[PopupDialog(dialogHead="$avatar_sys", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 博士，使用<@tu.kw>遏制单元</>能够调整试炼的模拟参数，帮助您更轻松地通过试炼。
[Tutorial(target="btn_relic", searchBtnInChildren=true, waitForSignal="boss_rush_relic_routed",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_sys", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 点击这里，可以装配和切换遏制单元。
[PopupDialog(dialogHead="$avatar_sys",dialogX=-533, dialogY=230)] 遏制单元可以直接接入引航者试炼的模拟系统，对作战参数进行有针对性的修改。
[PopupDialog(dialogHead="$avatar_sys",dialogX=-533, dialogY=230)] 在试炼过程中，您可以收集<@tu.kw>数据黑盒</>。数据黑盒能够对遏制单元进行<@tu.kw>数据迭代</>，从而提升其性能。
[PopupDialog(dialogHead="$avatar_sys",dialogX=-533, dialogY=230)] 解锁条件达成后，您可以解锁新的遏制单元，不同遏制单元具备的效果也不相同。但在试炼时<@tu.kw>最多只能启用一个遏制单元</>。
```

### camp_sweep

```
[HEADER(is_skippable=false, is_tutorial=true)] 剿灭扫荡引导
[PopupDialog(dialogHead="$avatar_sys")] 您好，博士，已为您加载新增功能：剿灭作战<@tu.kw>全权委托代理指挥</>。简而言之，就是由我为您完成剿灭作战流程。
[PopupDialog(dialogHead="$avatar_sys")] 您在日常任务中获取的<@tu.kw>【PRTS剿灭代理卡】</>可以在剿灭作战中使用，来激活全权委托代理指挥功能。
[Tutorial(target="pool_btn_use_agent",            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_sys")] 已经可以使用代理卡了，请点击<@tu.kw>高亮区域</>。
[Tutorial(target="pool_btn_agent_battle",            animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_sys")] 现在，全权委托代理指挥功能被激活了。
[Tutorial(target="pool_btn_agent_start_battle",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_sys")] 点击<@tu.kw>开始行动</>后，系统将分配资源完成任务。
[PopupDialog(dialogHead="$avatar_sys")] 全权委托代理指挥直接以该剿灭无助战时的<@tu.kw>最高歼灭数</>来计算您获得的报酬，即使完全不关注作战过程，您的战术仍可得到<@tu.kw>完美复现</>。
[PopupDialog(dialogHead="$avatar_sys")] 新增功能说明环节到此结束。
```

### guide_crisis_v2_intro

```
[HEADER(is_skippable=false, is_tutorial=true)] 危机合约入口
[Tutorial(waitForSignal="crisis_v2_entry_routed")]
[PopupDialog(dialogHead="$avatar_amiya")] 与博士已知的一样，危机合约仍是罗德岛重要的合作伙伴，我们曾通过完成危机合约获取足以支撑罗德岛运转的各种物资。
[CrisisV2.ResetToEntry()]
[Tutorial(target="crisis_v2_shop_btn", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black=0.5,           protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 【结晶圣所】会伴随每期合约上架各类可兑换的物资。完成作战任务可获得【晶体合约赏金】，用于在【结晶圣所】中兑换物资。
[Tutorial(target="crisis_v2_achieve_btn", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black=0.5,           protectTime=0.5, dialogHead="$avatar_amiya")] 这里是【作战回顾】，会记录博士在今后的危机合约中取得的蚀刻章、圣所评喻，以及在作战中的各项表现。
[Tutorial(target="crisis_v2_daily_btn", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black=0.5,           protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 从这可进入【轮换测试地】，活动期间会逐步开放四个地块，在限定时间内完成对应任务可领取限时奖励。完成轮换测试地中的所有任务时，【主测试地】会同时开放新的指标以供挑战，博士不要忘记哦。
[Tutorial(target="crisis_v2_main_map_btn", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black=0.5,           protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 这里是【主测试地】，是本期危机合约的主要作战区域，我们一起进去看看吧。
```

### guide_crisis_v2_map

```
[HEADER(is_skippable=false, is_tutorial=true)] 危机合约主图
[Tutorial(waitForSignal="crisis_v2_map_routed")]
[PopupDialog(dialogHead="$avatar_amiya")] 每期危机合约针对具体任务内容，会提供许多非强制性的【指标】和【指标集】。在这里，博士可以查看本期合约的主要指标。
[CrisisV2.SwitchMap(mapType="BAG_VIEW")]
[CrisisV2.FocusSlot(slotType="BAG_VIEW_BAG")]
[Tutorial(target="crisis_v2_bag_view_bag", searchBtnInChildren=true, focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Click", protectTime=0.5, dialogHead="$avatar_amiya",dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 【指标集】是按照效果将多个【指标】归为一组，博士可以选择单个【指标】或者【指标集】，点击【指标集】将默认以最高分一次性勾选其中对应指标。
[Tutorial(target="crisis_v2_bag_title", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black=0.5,           protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 完成【指标】可获得对应的奖励分数；在满足【指标集】最高分要求的情况下，部分指标集可提供额外奖励分数。
[Tutorial(target="crisis_v2_rune_desc", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black=0.5,           protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 选中的【指标集】效果可在此处查看。
[Tutorial(target="crisis_v2_bag_detail_btn", searchBtnInChildren=true,           animStyle="Click", focusStyle="HighlightRect", black=0.5,           protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 博士也可以进入【指标集】，对单个【指标】的选择情况做出具体调整。
[CrisisV2.SwitchMap(mapType="NODE_VIEW")]
[CrisisV2.FocusSlot(slotType="SLOT_VIEW_BAG")]
[Tutorial(target="crisis_v2_slot_view_bag", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black=0.5,           protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 调整【指标】后可在右侧查看当前的总效果，以【指标集】的最高分完成一次作战即视为完成当前【指标集】。
[CrisisV2.FocusSlot(slotType="RUNE")]
[Tutorial(target="crisis_v2_rune_item_desc", searchBtnInChildren=true, focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Click", protectTime=0.5, dialogHead="$avatar_amiya",           dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 现在可以通过点击右侧列表中的具体效果，直接显示对应的【指标】。
[Tutorial(target="crisis_v2_rune_item", searchBtnInChildren=true, focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=0.5, dialogHead="$avatar_amiya",           dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 这里亮起的就是博士选中的【指标】。
[CrisisV2.FocusSlot(slotType="TREASURE")]
[Tutorial(target="crisis_v2_treasure_item", searchBtnInChildren=true, focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Click", protectTime=0.5, dialogHead="$avatar_amiya",          dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 这里是本期作战的【晶块陈列室】，部分【结晶瑰宝】会在作战结束后上架常设兑换所，但没有现在获取这么实惠了哦，博士可要注意了。
[Tutorial(target="crisis_v2_slot_desc", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black=0.5,           protectTime=0.5, dialogHead="$avatar_amiya")] 只需完成与之相连的【指标集】即可获得其中的【结晶瑰宝】，点击右下方【指标集】图标可以帮博士快速选择对应的【指标集】。
[CrisisV2.FocusSlot(slotType="KEYPOINT")]
[Tutorial(target="crisis_v2_keypoint_item", searchBtnInChildren=true, focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Click", protectTime=0.5, dialogHead="$avatar_amiya",           dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 这是未完成的【关键节点】，点击一下试试吧。
[Tutorial(target="crisis_v2_slot_desc", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black=0.5,           protectTime=0.5, dialogHead="$avatar_amiya")] 每个【关键节点】都需要完成特定的任务才能被激活，激活后以它为起点可以点亮别的【指标】。
[CrisisV2.HidePreview]
[Tutorial(target="crisis_v2_start_battle_btn", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black=0.5,           protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 好了，博士，让我们开始一次作战吧！
```

### uniequip_intro

```
[HEADER(is_skippable=false, is_tutorial=true)] 专属装备解锁引导
[PopupDialog(dialogHead="$avatar_amiya")] 博士，干员们的<@tu.kw>模组</>系统已经可以访问了，请随我来，先确认一下该系统的基本状态吧。
[PopupDialog(dialogHead="$avatar_amiya")] 一般来说，如果干员还没满足PRTS设置的<@tu.kw>模组</>系统解锁条件，对应的系统入口是不会对博士您开放的。
[GotoCharInfo]
[Tutorial(waitForSignal="charinfo_routed")]
[Tutorial(target="hide_desc_view",animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 在这里，我们可以点击除模组以外的部分展开分支与天赋详情，浏览干员的分支职业特性信息。如果干员拥有模组，也可以在此进行模组的快速切换。
[Tutorial(target="hide_desc_view", animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 但模组系统需要先进行解锁哦，要干员满足至少可以获取一件的条件后，才可以获得模组系统的访问权限。
[Tutorial(target="uniequip_hot_spot", waitForSignal="equip_edit_show", animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 点击这里，就可以为干员编辑模组了。
[Tutorial(focusX=235, focusY=-450, focusWidth=460, focusHeight=750, anchor="TopLeft",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya", dialogX=-210, dialogY=180)] 在左侧可查看干员启用模组后的各项数据变化。
[Tutorial(target="pool_btn_equip_select", waitForSignal="equip_item_selected",            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 点击此处可以查看模组带来的效果。
[Tutorial(target="pool_btn_equip_detail", waitForSignal="equip_unlock_show",            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 点击此处可以解锁模组。
[PopupDialog(dialogHead="$avatar_amiya")] 完成各项模组的<@tu.kw>指定任务</>后，再消耗一定素材后才可以解锁模组，博士要加油哦。
[Tutorial(focusX=239, focusY=101, focusWidth=161, focusHeight=177, anchor="BottomLeft",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 对了，博士，这是预先准备好的几个<@tu.kw>模组数据块</>，这是解锁模组的关键材料，本次教学结束后就可以获得了。
```

### uniequip_upgrade

```
[HEADER(is_skippable=false, is_tutorial=true)] 专属装备升级引导
[PopupDialog(dialogHead="$avatar_amiya")] 博士，已解锁的模组可以继续升级，干员的作战能力将进一步提升。
[GotoCharInfo]
[Tutorial(waitForSignal="charinfo_routed")]
[Tutorial(target="uniequip_hot_spot",animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 点击这里为干员编辑模组。
[Tutorial(waitForSignal="equip_show")]
[Tutorial(target="lvlup_hotspot_avail", animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 点击已解锁的干员专属模组。
[PopupDialog(dialogHead="$avatar_amiya")] 模组解锁后为1级，可以在此进行升级。
[Tutorial(target="panel_uniequip_require_item_focus", animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 博士，完成保全派驻的作战任务可以获得模组升级所需的稀有材料，快去试试吧。
[Tutorial(target="panel_uniequip_require_item_focus", animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 工程部已经为博士提供了一些升级所需的材料。
```

### 0_home_ui

```
[HEADER(is_skippable=false, is_tutorial=true)] 主UI新手引导
[PopupDialog(dialogHead="$avatar_sys", protectTime=1)] 虽然你的身体还留在切尔诺伯格，但还是————欢迎回到罗德岛。
[PopupDialog(dialogHead="$avatar_sys")] 暂时你还没有熟悉罗德岛的全部功能，看来这也是需要复习的部分了。虽然部分功能区域还在修复中，不过至少核心功能已经可以使用了。
[Tutorial(target="btn_battle",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_sys")] 通过<@tu.kw>终端</>，你可以推进主要行动或者进行训练关卡。
[Tutorial(target="btn_character_repo",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_sys")] 这里是<@tu.kw>干员管理</>界面，在这里你可以管理和训练你的干员。
[Tutorial(target="btn_squad",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_sys")] 这里是<@tu.kw>编队</>入口，在这里可以管理小队的编成和干员技能的选择。
[Tutorial(target="btn_recruit",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_sys")] 不要忘了招募干员，在这里你可以招募新的干员，以扩大罗德岛的成员规模。
[Tutorial(target="btn_inventory",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_sys")] 最后是仓库界面，在这里你可以整理获得的物品。
```

### 1_recruit_adv

```
[HEADER(is_skippable=false, is_tutorial=true)] 高级干员招募引导
[PopupDialog(dialogHead="$avatar_sys")] 未被损坏的记忆部分可能比想象的少。
[PopupDialog(dialogHead="$avatar_sys")] 不过你已经懂得了基本的生存技巧，没有白费阿米娅对你的一片期待，以及她为了救你而准备的这些干员。
[PopupDialog(dialogHead="$avatar_amiya")] 无论如何，整合运动造成的影响和破坏都超过了预期。博士，我们需要坚持下去。
[PopupDialog(dialogHead="$avatar_sys")] 如果想要生存下去的话，需要扩充下罗德岛的成员配置。
[PopupDialog(dialogHead="$avatar_amiya")] 博士，堆积着的档案已经很多了，当中一定有能够成为我们新的伙伴的人，从中招募些有可能加入我们的人吧。
[GotoPage(dest="HOME", waitForSignal="home_routed")]
[Tutorial(target="btn_advanced_recruit",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 博士，点击干员寻访按钮。
[GotoPage(dest="recruit_advanced", waitForSignal="recruit_advanced_routed")]
[PopupDialog(dialogHead="$avatar_sys")] 在这里你可以使用<@tu.kw>合成玉</>进行<@tu.kw>干员寻访</>。
[Tutorial(target="panel_diamond_shard",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_sys", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 合成玉是一种十分珍贵的资源，但同时也是干员寻访的必须品。使用前请务必仔细思考。
[Tutorial(target="btn_gacha", waitForSignal="recruit_gacha_drawn",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black", importantClick=true,           protectTime=0.5, dialogHead="$avatar_sys")] 点击此处以招募干员。
[InputBlocker(blockInput=false)]
[Tutorial(waitForSignal="recruit_gachaeffect_shown")]
[InputBlocker(blockInput=true)]
```

### 2_make_squad

```
[HEADER(is_skippable=false, is_tutorial=true, char_sort_type="BY_RARITY_DOWN")] 编辑小队引导
[PopupDialog(dialogHead="$avatar_amiya")] 博士，光靠之前参与了行动的大家，可能还不足以面对之后的所有威胁。
[PopupDialog(dialogHead="$avatar_amiya")] 也许我们需要派遣一些新招募的成员参与行动。
[PopupDialog(dialogHead="$avatar_amiya")] 接下来PRTS会教您如何做。
[GotoPage(dest="HOME", waitForSignal="home_routed")]
[Tutorial(target="btn_squad",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_sys")] 点击进入编队界面
[GotoPage(dest="squad", waitForSignal="squad_routed")]
[Tutorial(target="pool_btn_squad_first_empty_slot", searchBtnInChildren="true", waitForSignal="squadselect_resumed",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_sys")] 点击这里在小队中添加干员
[Tutorial(target="pool_btn_squad_select_first_item", searchBtnInChildren="true", waitForSignal="squadselect_charcard_selected",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_sys")] 点击选中干员
[InputBlocker(blockInput=true)]
[Tutorial(target="panel_hotspot", waitForSignal="squadhome_resumed",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_sys")] 点击确认编队
[Tutorial(target="btn_topmenu_home", waitForSignal="topmenu_shown",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_sys", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 干员已经成功加入出击小队，点击导航栏返回
[Tutorial(target="btn_home", waitForSignal="squad_saved", importantClick=true,           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_sys", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 点击首页按钮回到中央大厅
```

### 3_battle_ui

```
[HEADER(is_skippable=false, is_tutorial=true)] 战斗关卡引导
[PopupDialog(dialogHead="$avatar_sys")] 记住，现在你们还身处作战环境中。如果你忘记了如何回到行动现场，接下来我会告诉你怎么做。
[GotoPage(dest="HOME", waitForSignal="home_routed")]
[Tutorial(target="btn_battle",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_sys")] 点击进入<@tu.kw>终端</>界面
[GotoPage(dest="stage", waitForSignal="stage_routed")]
[Tutorial(target="mix_story_layout", waitForSignal="stage_mix_story_zonetype_selected",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_sys")] 选中曲谱标签
[Tutorial(target="pool_btn_first_zone", waitForSignal="stage_mix_story_retro_routed",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_sys")] 乐章的旋律由此开始......在您苏醒之后首先要面对的，是在切尔诺伯格市内进行破坏活动的整合运动。
[Tutorial(target="panel_mix_story_retro_entrance", waitForSignal="zone_switched_or_resumed",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_sys")] 点击进入对应主题曲地图
[Tutorial(target="pool_btn_first_zonestage", waitForSignal="stagepreview_resumed",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_sys", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 选择行动地点。
[Tutorial(target="btn_start_battle", waitForSignal="squadhome_resumed",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_sys")] 点击按钮进入战前编队页面。
[Delay(time="$f_delay_start_battle_btn")]
[Tutorial(target="hotspot_startbtn", waitForSignal="battle_start", importantClick=true,           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_sys")] 点击按钮开始执行此次作战。
```

### 0_mission_main

```
[HEADER(is_skippable=false, is_tutorial=true)] 主线任务引导
[PopupDialog(dialogHead="$avatar_amiya")] 其实，罗德岛除了有一些日常的内部维护工作，还会收到来自外部的各种委托请求。
[PopupDialog(dialogHead="$avatar_sys")] 为了能更有序地管理这些事宜，你需要学习如何处理现在手中的<@tu.kw>任务</>。
[GotoPage(dest="HOME", waitForSignal="home_routed")]
[Tutorial(target="btn_mission",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 博士，从这里可以进入<@tu.kw>任务</>管理界面。
[GotoPage(dest="mission", waitForSignal="mission_routed", initMissionPage="MAINMISSION")]
[PopupDialog(dialogHead="$avatar_amiya")] 这个界面会罗列出所有您需要处理的<@tu.kw>任务</>。
[Tutorial(target="tab_hotspot_mainmission",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 请看<@tu.kw>这里</>。这一部分记录了正在面临的最主要任务。
[Tutorial(target="hotspot_draw", waitForSignal="mission_confirmed_mission", importantClick=true,           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 点击领取这次任务完成的补给。
[Tutorial(waitForSignal="gainitem_routed")]
[Tutorial(target="confirm_button", waitForSignal="gainitem_confirmed",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 在这种非常时期，我们需要利用一切我们可以利用的资源。
[PopupDialog(dialogHead="$avatar_sys")] 稍后你可以回到这里继续整理手上的任务。
[PopupDialog(dialogHead="$avatar_sys")] 现在，你需要了解另外一件重要事项。
```

### 1_training_level

```
[HEADER(is_skippable=false, is_tutorial=true)] 训练关卡引导
[PopupDialog(dialogHead="$avatar_amiya")] 博士，罗德岛的档案库中存放着杜宾老师指导的<@tu.kw>作战演习</>。
[PopupDialog(dialogHead="$avatar_amiya")] 这些演习中包含了基础的作战技巧，相信掌握之后对博士一定大有帮助。
[PopupDialog(dialogHead="$avatar_amiya")] 因为杜宾正在参加营救，所以她不能同时在训练场进行指导。
[PopupDialog(dialogHead="$avatar_amiya")] 这边会回放她之前和接受过黑钢训练的干员杰西卡先进行的模拟训练。
[GotoPage(dest="home", waitForSignal="home_routed")]
[Tutorial(target="btn_battle",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 点击进入<@tu.kw>终端</>
[GotoPage(dest="STAGE", waitForSignal="stage_routed", zoneId="main_1", stageId="tr_01")]
[Delay(time="$f_delay_scroll_stage_on_map")]
[Tutorial(target="pool_btn_train_substage#tr_01",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 进行<@tu.kw>作战演习</>的关卡并<@tu.kw>不会消耗理智</>，可以随时进行反复尝试。
[Tutorial(target="btn_start_battle", waitForSignal="squadhome_resumed",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 点击按钮进入战前编队页面。
[Delay(time="$f_delay_start_battle_btn")]
[PopupDialog(focusX=-10, focusY=34, focusWidth=388, focusHeight=65, anchor="Bottom",              animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",             dialogHead="$avatar_amiya")] 博士，所有演习关卡的阵容都<@tu.kw>不可改变</>。如果遇到无法通过演习的情况，请多尝试不同的战术和部署位置。
[Tutorial(target="hotspot_startbtn", waitForSignal="battle_start", importantClick=true,           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 点击按钮开始<@tu.kw>演习</>项目。
```


> 本章节共111个脚本文件，此处展示前30个。

## 统计

- 总字符数：61636
- 对话行数：201


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
