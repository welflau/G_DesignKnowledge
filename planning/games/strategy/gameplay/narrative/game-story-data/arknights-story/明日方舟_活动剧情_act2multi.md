# 明日方舟 · 活动剧情 · act2multi（3段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act2multi」完整剧情脚本（3个文件，0行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act2multi
- 脚本文件数：3

### training_raft_end_a

```
[header(is_skippable=false, is_tutorial=true)]
[inputblocker(blockInput=true)]
[battle.delay(time=2)]
[battle.pause(pause=true)]
[popupdialog(dialogHead="$avatar_amiya", black="$f_tut_black", protectTime=0.5)]看，这样我们就到达了新的赛段~
[tutorial(focusX=52, focusY=-37, focusWidth=228, focusHeight=42, animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y", anchor="Top")]每次到达新的赛段，我们就能获得大量<@tu.kw>分数</>奖励，还可以<@tu.kw>延长比赛时间</>！
[popupdialog(dialogHead="$avatar_amiya", black="$f_tut_black", protectTime=1)]另外，最后一个赛段会出现<@tu.kw>终点信标塔</>，漂流艇只要触碰到信标塔，比赛就会立即结束，博士将获得大量分数奖励。
[popupdialog(dialogHead="$avatar_amiya", black="$f_tut_black", protectTime=1)]接下来，就请博士航向终点完成这次训练吧！
[battle.pause(pause=false)]
```

### training_raft_start_a

```
[header(is_skippable=false, is_tutorial=true)]
[inputblocker(blockInput=true)]
[battle.delay(time=2)]
[battle.pause(pause=true)]
[inputblocker(blockInput=true)]
[popupdialog(dialogHead="$avatar_amiya", black="$f_tut_black", protectTime=0.5)]博士，这里就是障碍漂航的赛道。
[popupdialog(dialogHead="$avatar_amiya", protectTime=0.5)]与其他项目一样，博士需要和<@tu.kw>一位协作者</>共同参与，这次就让我来当博士的协作者吧！
[tutorial(focusX=0, focusY=-70, focusWidth=132, focusHeight=37, animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", protectTime=1, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y", anchor="Top")]在漂航比赛中，我们的目标是在<@tu.kw>倒计时</>结束之前完成所有赛段，到达<@tu.kw>终点</>！
[tutorial(focusX=-70, focusY=8, focusWidth=100, focusHeight=100, animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y", anchor="Right")]这里的标记指向通往下一个赛段或终点的方向。
[tutorial(black="$f_tut_black", protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]那么，要如何让漂流艇<@tu.kw>开始航行</>呢？
[tutorial(focusX=235, focusY=-37, focusWidth=137, focusHeight=49, animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y", anchor="Top")]在比赛过程中，每隔一段时间，赛道中的水流流速就会<@tu.kw>变快</>，推动漂流艇航向下一赛段。
[tutorial(focusWidth=100, focusHeight=100, animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y", tileY=18, tileX=17)]博士也可以通过攻击<@tu.kw>全手动推进器</>为漂流艇增加动力。
[tutorial(focusWidth=100, focusHeight=100, animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", protectTime=1, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y", tileY=18, tileX=17)]但全手动推进器只能被其<@tu.kw>周围4格</>的单位攻击，所以选择适合的干员“掌舵”也是达成比赛目标的关键！
[popupdialog(dialogHead="$avatar_amiya", black="$f_tut_black", protectTime=0.5)]现在，我们出发吧！
[battle.pause(pause=false)]
```

### training_raft_start_b

```
[header(is_skippable=false, is_tutorial=true)]
[inputblocker(blockInput=true)]
[battle.pause(pause=true)]
[tutorial(focusWidth=100, focusHeight=100, animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y", tileY=23, tileX=21)]比赛时，我们可以通过各种方式来获得分数，<@tu.kw>击落</>这些“宝石飞翼”无人机就能获得<@tu.kw>分数</>奖励。
[battle.pause(pause=false)]
[battle.delay(time=2.5)]
[inputblocker(blockInput=true)]
[battle.pause(pause=true)]
[tutorial(focusX=52, focusY=-37, focusWidth=228, focusHeight=42, animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y", anchor="Top")]这样我们就<@tu.kw>得到分数</>了！
[battle.pause(pause=false)]
[battle.delay(time=3)]
[battle.pause(pause=true)]
[tutorial(focusWidth=180, focusHeight=180, animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", protectTime=0.5, dialogHead="$avatar_amiya", tileY=17, tileX=20)]同时也要小心，赛道中会出现很多意想不到的敌人，对比赛造成干扰。
[tutorial(focusWidth=180, focusHeight=180, animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", protectTime=0.5, dialogHead="$avatar_amiya", tileY=17, tileX=20)]敌人的目标是漂流艇上的<@tu.kw>全手动推进器</>，推进器一旦受损，一定时间内就<@tu.kw>无法继续输出动力</>。
[popupdialog(dialogHead="$avatar_amiya", black="$f_tut_black", protectTime=0.5)]不过不用担心，博士，我来帮你解决这个麻烦！
[battle.pause(pause=false)]
```


## 统计

- 总字符数：4460
- 对话行数：0


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
