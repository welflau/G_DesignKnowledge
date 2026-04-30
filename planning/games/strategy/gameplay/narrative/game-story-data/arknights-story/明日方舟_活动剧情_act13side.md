# 明日方舟 · 活动剧情 · act13side（40段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act13side」完整剧情脚本（40个文件，6646行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act13side
- 脚本文件数：40

### guide_act13side_mission_1

```
[HEADER(is_skippable=false, is_tutorial=true)] 博士的办公室引导1
[Activity.ResetToEntry]
[Tutorial(waitForSignal="activity_entry_routed")]
[PopupDialog(dialogHead="$avatar_amiya")] 博士，罗德岛和卡西米尔相关组织的联络渠道已经建立完毕了，请让我带您先熟悉一下流程吧。
[Tutorial(target="mission_btn", searchBtnInChildren=true,            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 请点击屏幕上的图标进入您的办公桌。
```

### guide_act13side_mission_2

```
[HEADER(is_skippable=false, is_tutorial=true)] 博士的办公室引导2
[PopupDialog(dialogHead="$avatar_amiya")] 在卡西米尔，多个组织向罗德岛发布了合作意向，他们的委托在到达罗德岛后被归类为对应阵营的长期事务与每日事务。
[Tutorial(target="down_back_img",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 长期事务中每个条目均为唯一，完成后就可以获得相应报酬。
[Tutorial(target="top_select_img",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 每日事务有多种类型，您可以挑选合乎心意的条目完成，完成后能获得不菲的报酬呢。
[Tutorial(focusX=-132, focusY=-53, focusWidth=226, focusHeight=28, anchor="TopRight",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 您可以每日获取3份议程提案，累积的话，最多，嗯......15份吧。您处理这些已经很辛苦了，如果有多余的提案，我会想办法应付的。
[Tutorial(target="pool_first_daily_slot", searchBtnInChildren=true, waitForSignal="act13side_mission_pool_routed",            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya")] 请尝试接取一下新的事务吧。
[Tutorial(focusX=191, focusY=0, focusWidth=350, focusHeight=535, anchor="Left",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya", dialogX=-315, dialogY="$f_lower_dialog_pos_y")] 左侧会列出所有可接取的事务条目，接取事务后，就会消耗相应数量的议程提案。如果接取事务后发现任务无法完成，也可以选择驳回，消耗的议程提案会全数返还。
[Tutorial(focusX=191, focusY=0, focusWidth=350, focusHeight=535, anchor="Left",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya", dialogX=-315, dialogY="$f_lower_dialog_pos_y")] 但如果选择驳回，这项事务就不会回到当日待选事务列表中了，一定要注意呀。
[Tutorial(target="btn_search", searchBtnInChildren=true, waitForSignal="act13side_mission_search_routed",            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_amiya", dialogX=-315, dialogY="$f_lower_dialog_pos_y")] 每天开始工作的时候，我会先帮博士梳理一遍每日事务，如果博士有需求和倾向的话，我们可以通过重新搜索来对列表进行更新。
[PopupDialog(dialogHead="$avatar_amiya")] 每日事务列表更新前，博士可以选择想要接触的企业及想要获取的报酬材料，选择完毕后点击重新搜索，列表就能依照您的需求进行更新了。
[PopupDialog(dialogHead="$avatar_amiya")] 虽说可以更新，但还是有次数限制的，不然更新太频繁，各个组织的联系人会有意见的。
[PopupDialog(dialogHead="$avatar_amiya")] 以上就是与卡西米尔各组织合作的相关注意事项了，在卡西米尔驻留期间您的工作可能会比较繁忙，一定要注意劳逸结合呀
```

### level_act13side_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔2 1-1
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_23_G03",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[dialog]
[Character(name="avg_npc_212_1")]
[name="发言人麦基"]  辛苦了，德罗斯特女士......您在看什么？
[Character(name="avg_npc_215_1#3", name2="avg_npc_212_1", focus=1)]
[name="烛骑士"]  不入流的诗集，麦基先生。
[Character(name="avg_npc_215_1#3", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  啊......您一直很喜欢这些。
[name="发言人麦基"]  还记得我第一次见到您，在那处满是血腥与铁锈气味的竞技场里，您也是捧着这样一本书，好像与周围格格不入。
[Character(name="avg_npc_215_1#3", name2="avg_npc_212_1", focus=1)]
[name="烛骑士"]  您对这些细节，似乎记得很清楚......？
[Character(name="avg_npc_215_1#1", name2="avg_npc_212_1#6", focus=2)]
[name="发言人麦基"]  啊......哈哈，惭愧，我也是您的粉丝之一。如果有空，可要您为我签个名。
[Character(name="avg_npc_215_1#1", name2="avg_npc_212_1#6", focus=1)]
[name="烛骑士"]  荣幸之至。
[dialog]
[character]
[PlaySound(key="$doorknockquite", volume=0.6)]
[delay(time=1)]
[Character(name="avg_npc_222",fadetime=1,block=true)]
[delay(time=1)]
[name="企业员工"]  麦基先生，打扰了。
[name="企业员工"]  您要的酒就放在这里。
[Character(name="avg_npc_222", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  多谢，代我向其他工作人员问好。
[Character(name="avg_npc_215_1#1", name2="avg_npc_212_1#6", focus=2)]
[name="发言人麦基"]  让我们庆祝一下吧，德罗斯特女士。
[Character(name="avg_npc_215_1#1", name2="avg_npc_212_1#6", focus=1)]
[name="烛骑士"]  乐意至极。
[Character(name="avg_npc_215_1#1", name2="avg_npc_212_1#6", focus=2)]
[name="发言人麦基"]  干杯！
[Character(name="avg_npc_215_1#1", name2="avg_npc_212_1#6", focus=1)]
[name="烛骑士"]  干杯。
[dialog]
[Character(name="avg_npc_215_1#2", name2="avg_npc_212_1#6", focus=0)]
[PlaySound(key="$clink", volume=0.6)]
[delay(time=2)]
[Character(name="avg_npc_215_1#2", name2="avg_npc_212_1#6", focus=2)]
[name="发言人麦基"]  哈，确实是好酒，价格惊人的高卢藏品，配得上今天这样的日子......
[name="发言人麦基"]  还有您这样的骑士。
[Character(name="avg_npc_215_1#1", name2="avg_npc_212_1#6", focus=1)]
[name="烛骑士"]  您过奖，我只是个幸运儿罢了。
[Character(name="avg_npc_215_1#1", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  这本诗集......
[Character(name="avg_npc_215_1#1", name2="avg_npc_212_1", focus=1)]
[name="烛骑士"]  是我家乡的一位无名诗人，我很喜欢他的句子。
[Character(name="avg_npc_215_1#1", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  啊，莱塔尼亚的诗集......是叫《两个月亮与金盏花》？
[Character(name="avg_npc_215_1#1", name2="avg_npc_212_1", focus=1)]
[name="烛骑士"]  您的莱塔尼亚语一向很好。
[Character(name="avg_npc_215_1#1", name2="avg_npc_212_1#6", focus=2)]
[name="发言人麦基"]  哈哈，只是必要的外交学习。我猜您喜欢金盏花？今天的卡西米尔已经很少有人懂得欣赏诗歌了。
[Character(name="avg_npc_215_1#1", name2="avg_npc_212_1#6", focus=1)]
[name="烛骑士"]  ......字符终归脱离不了想象，这些都只是想象的符号。
[name="烛骑士"]  对当代人而言，诗歌不过是毫无美感的文字迷宫，自作多情，矫揉造作。
[name="烛骑士"]  也许卡西米尔人已经习惯于别样的消费，而诗歌总是与这类消费无缘，这很正常。
[Character(name="avg_npc_215_1#1", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  ......您似乎别有所指？
[Character(name="avg_npc_215_1#2", name2="avg_npc_212_1", focus=1)]
[name="烛骑士"]  只是谈论诗歌，麦基先生。
[Character(name="avg_npc_215_1#2", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  您应该还有些话要对我们说吧，女士？
[Character(name="avg_npc_215_1#1", name2="avg_npc_212_1", focus=1)]
[name="烛骑士"]  唔......是什么呢。
[name="烛骑士"]  啊，您的新眼镜很适合您，麦基先生。
[Character(name="avg_npc_215_1#1", name2="avg_npc_212_1#3", focus=2)]
[name="发言人麦基"]  哈哈......您、您居然能注意到这种事，真让人意外，哈哈......
[Character(name="avg_npc_215_1#1", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  咳，不过，您该说的不是这个，先前在城际网络和纸媒上出现的一些谣言......
[Character(name="avg_npc_215_1#3", name2="avg_npc_212_1", focus=1)]
[name="烛骑士"]  啊......红酒浴池？
[Character(name="avg_npc_215_1#3", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  是的，那是对您声誉的诋毁......
[Character(name="avg_npc_215_1#1", name2="avg_npc_212_1", focus=1)]
[name="烛骑士"]  真的会有人用红酒泡澡吗？不会黏哒哒的吗？
[Character(name="avg_npc_215_1#1", name2="avg_npc_212_1#3", focus=2)]
[name="发言人麦基"]  呃？大概......我不知道。
[Character(name="avg_npc_215_1#1", name2="avg_npc_212_1#3", focus=1)]
[name="烛骑士"]  呵......这种新闻又有谁会信呢？
[Character(name="avg_npc_215_1#1", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  有人会信的，德罗斯特女士......会有很多人信的。哪怕他们知道真相未必如此，他们也愿意掺和这些事情。
[Character(name="avg_npc_215_1#1", name2="avg_npc_212_1", focus=1)]
[name="烛骑士"]  事后澄清一下不就行了？
[Character(name="avg_npc_215_1#1", name2="avg_npc_212_1#2", focus=2)]
[name="发言人麦基"]  唉，女士，您总是把骑士之外的事情想得太简单了......
[Character(name="avg_npc_215_1#1", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  我已经联络了玫瑰新闻报业的总部，这是某家娱乐报刊的编辑私人所为。
[name="发言人麦基"]  似乎在发现的时候已经引起了不小的反响，出于各种考量没有立刻撤回......
[Character(name="avg_npc_215_1#1", name2="avg_npc_212_1", focus=1)]
[name="烛骑士"]  这是他们的工作方式，我不怪他们。
[Character(name="avg_npc_215_1#1", name2="avg_npc_212_1#2", focus=2)]
[name="发言人麦基"]  您很宽容，但这更让我为您感到委屈。
[name="发言人麦基"]  您把几乎所有私人收入都捐赠给了莱塔尼亚的贫困地区，为家乡修建学校，建设移动平台。
[Character(name="avg_npc_215_1#1", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  但就算现在辟谣，经历过狂欢的群众也不会去在意真相如何。
[name="发言人麦基"]  伤害和诋毁是很简单的，他们会把这些谣言和噱头握在手上，奔走相告。
[name="发言人麦基"]  可您几时见过，真相揭露以后，这些曾经伤害过您的人会去帮您洗清冤屈，澄清事实的？
[Character(name="avg_npc_215_1#2", name2="avg_npc_212_1", focus=1)]
[name="烛骑士"]  这些八卦能让人们感到新鲜刺激，澄清事实却是一件无聊的事情，这也是理所当然的。
[Character(name="avg_npc_215_1#2", name2="avg_npc_212_1#2", focus=2)]
[name="发言人麦基"]  唉，您怎么这么无所谓呢！
[name="发言人麦基"]  您这样清正廉直的骑士应该成为其他人的榜样！这本该让您有更好的名声，而且——
[Character(name="avg_npc_215_1#6", name2="avg_npc_212_1#2", focus=1)]
[name="烛骑士"]  麦基。
[Character(name="avg_npc_215_1#6", name2="avg_npc_212_1#3", focus=2)]
[name="发言人麦基"]  呃......
[Character(name="avg_npc_215_1#1", name2="avg_npc_212_1#3", focus=1)]
[name="烛骑士"]  我很感动。
[name="烛骑士"]  您是个多愁善感的人......也是个温柔的人。
[Character(name="avg_npc_215_1#1", name2="avg_npc_212_1#2", focus=2)]
[name="发言人麦基"]  ......
[Character(name="avg_npc_215_1#1", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  ......作为联合会发言人，保证各位骑士不受场外因素干扰，也是我应该做的。
[name="发言人麦基"]  只是，请您多在乎一下自己的生活。
[Character(name="avg_npc_215_1#1", name2="avg_npc_212_1", focus=1)]
[name="烛骑士"]  啊......对了。
[name="烛骑士"]  决斗赛的赛程表什么时候发布？
[Character(name="avg_npc_215_1#1", name2="avg_npc_212_1", focu

... (全文19389字符)
```

### level_act13side_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔2 1-2
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_23_G03",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(name="avg_npc_212_1")]
[name="发言人麦基"]  留步，马克维茨先生。
[dialog]
[Character(name="avg_npc_211_1#4",fadetime=1,block=true)]
[delay(time=1)]
[name="发言人马克维茨"]  是您啊，麦基先生，您......您有事找我？
[Character(name="avg_npc_211_1#4", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  又见面了，你收到联合会的信件了吗？
[name="发言人麦基"]  特锦赛期间负责赛事监督的发言人只有我们俩......这可是个苦差事，但也备受瞩目。
[name="发言人麦基"]  如果想要在摘掉“发言人”三个字之后还能继续平步青云，眼下这可是最好的机会了。
[Character(name="avg_npc_211_1#5", name2="avg_npc_212_1", focus=1)]
[name="发言人马克维茨"]  哈哈......不怕您笑话，我宁可不被这么瞩目，去负责场地活动的策划一类......
[Character(name="avg_npc_211_1#5", name2="avg_npc_212_1#3", focus=2)]
[name="发言人麦基"]  您擅长这些？
[Character(name="avg_npc_211_1#7", name2="avg_npc_212_1#3", focus=1)]
[name="发言人马克维茨"]  可没什么擅长不擅长的，我只是......
[Character(name="avg_npc_211_1#7", name2="avg_npc_212_1#6", focus=2)]
[name="发言人麦基"]  您又谦虚了，您适应得比那些老员工都快。
[Character(name="avg_npc_211_1#7", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  ——不过今天找您，是有一些别的事情我想提前知会您一声。
[name="发言人麦基"]  咱们找一间休息室聊吧？
[Character(name="avg_npc_211_1#3", name2="avg_npc_212_1", focus=1)]
[name="发言人马克维茨"]  啊，听您的......
[dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Background(image="bg_23_G09",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Character(name="avg_npc_211_1", name2="avg_npc_212_1", focus=1)]
[name="发言人马克维茨"]  什么事需要这么谨慎？
[Character(name="avg_npc_211_1", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  其实这些，本不该我来和您说，但是恰尔内先生走得匆忙。
[name="发言人麦基"]  卡瓦莱利亚基除了核心的大骑士领本土，每届会从商业发展最迅速的城市中选出三座，合并成为如今的大骑士领。
[name="发言人麦基"]  在特锦赛结束之后的几个月内，除了大骑士领外的移动城市，会根据航线工程师的设计，在一个月内回到原本的航线之中。
[Character(name="avg_npc_211_1", name2="avg_npc_212_1#2", focus=2)]
[name="发言人麦基"]  每次四城合并都是一次机遇。可观的人流量，无缝通商，以及......处理一些问题的机会。
[name="发言人麦基"]  说实在的，要不是四城联合的规模实在过于庞大，无法有效移动，躲避天灾，也难处理物资分配和开采问题。
[name="发言人麦基"]  我真希望四城联合永不解散。
[Character(name="avg_npc_211_1", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  不过今天要说的是一个......嗯......潜规则。
[Character(name="avg_npc_211_1#3", name2="avg_npc_212_1", focus=1)]
[name="发言人马克维茨"]  是关于......？
[Character(name="avg_npc_211_1#3", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  ......感染者。
[name="发言人麦基"]  梅什科工业集团今年为大骑士领提供了七个移动平台，相当于其他国家一座城区的规模......当然，这是台面上的部分。
[Character(name="avg_npc_211_1#5", name2="avg_npc_212_1", focus=1)]
[name="发言人马克维茨"]  这些，我都从同事那里听闻过。
[Character(name="avg_npc_211_1#5", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  现在我们应当关注的重点是零号地块。它不在梅什科工业交付的合法名单上。
[name="发言人麦基"]  这个地块性质特殊，它是一个规模很小的移动平台，现在连接在西南边角，十七号城区之外。
[Character(name="avg_npc_211_1#3", name2="avg_npc_212_1", focus=1)]
[name="发言人马克维茨"]  那里是......
[Character(name="avg_npc_211_1#3", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  是的，那里就在感染者收容治疗中心旁边。
[Character(name="avg_npc_211_1#3", name2="avg_npc_212_1#2", focus=2)]
[name="发言人麦基"]  原谅我的无礼，马克维茨先生，接下来我们交谈的每一句话，都要录像记录。
[Character(name="avg_npc_211_1#3", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  这是规定......发言人之中不允许有任何背叛联合会的行为。
[Character(name="avg_npc_211_1#3", name2="avg_npc_212_1", focus=1)]
[name="发言人马克维茨"]  ......
[Character(name="avg_npc_211_1#5", name2="avg_npc_212_1", focus=1)]
[name="发言人马克维茨"]  ......我明白了。
[dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[Background(image="bg_23_G03",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Character(name="avg_npc_211_1#5", name2="avg_npc_212_1", focus=1)]
[name="发言人马克维茨"]  ......
[Character(name="avg_npc_211_1#5", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  您的脸色很难看......我知道，我一开始听说的时候，也是您这样。
[Character(name="avg_npc_211_1#7", name2="avg_npc_212_1", focus=1)]
[name="发言人马克维茨"]  可这也太不人道了......
[Character(name="avg_npc_211_1#7", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  ......您现在是董事会的执行人，商业联合会的发言人，马克维茨兄。
[Character(name="avg_npc_211_1#7", name2="avg_npc_212_1#6", focus=2)]
[name="发言人麦基"]  ......我只是提醒您这一点，当然，不是警告或是威胁什么的——哈哈，恰尔内先生总会给人这样的感觉对吧？
[Character(name="avg_npc_211_1#7", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  尽在把握，了如指掌。你不听他的可不行。
[Character(name="avg_npc_211_1#5", name2="avg_npc_212_1", focus=1)]
[name="发言人马克维茨"]  ......
[Character(name="avg_npc_211_1#5", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  我可没那个意思，马克维茨兄，我们得相互扶持。
[name="发言人麦基"]  您该好好想想我的话，我接下来还要去和几个骑士团确认行程。
[name="发言人麦基"]  回头见。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_nearllivingroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_064_weapon_1#5")]
[name="佐菲娅"]  ......玛恩纳？
[name="佐菲娅"]  你在吗？玛——
[Character(name="avg_npc_064_weapon_1", focus=-1)]
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[delay(time=0.5)]
[Character(name="char_148_nearl_ns_1#4",fadetime=1,block=true)]
[delay(time=1)]
[name="玛嘉烈"]  ......佐菲娅姑母？
[Character(name="char_148_nearl_ns_1#4", name2="avg_npc_064_weapon_1", focus=2)]
[name="佐菲娅"]  啊......玛嘉烈，你怎么还在家里？
[name="佐菲娅"]  玛莉娅那孩子不是说你去骑士协会了吗？
[Character(name="char_148_nearl_ns_1#6", name2="avg_npc_064_weapon_1", focus=1)]
[name="玛嘉烈"]  一些程序上的琐事罢了，花不了多少功夫。
[Character(name="char_148_nearl_ns_1#6", name2="avg_npc_064_weapon_1", focus=2)]
[name="佐菲娅"]  ......呵呵，你真的变了。
[name="佐菲娅"]  是因为那个叫“罗德岛”的地方？你以前可根本不擅长那些文书工作。
[name="佐菲娅"]  还记得你刚报名成为骑士的时候吗？独立骑士玛嘉烈·临光，总是把各种证件和手续搞混......
[Character(name="char_148_nearl_ns_1#6", name2="avg_npc_064_weapon_1", focus=1)]
[name="玛嘉烈"]  嗯......那时候多亏了有你，姑母。
[Character(name="char_148_nearl_ns_1#6", name2="avg_npc_064_weapon_1#6", focus=2)]
[name="佐菲娅"]  唉......玛莉娅那丫头也就算了，你年纪不是和我差不多吗？
[name="佐菲娅"]  以前花了那么大力气让你习惯直呼其名，怎么几年没见，又变回去了？
[name="佐菲娅"]  难道我们生疏了？嗯？
[Character(name="char_148_nearl_ns_1#6", name2="avg_npc_064_we

... (全文12594字符)
```

### level_act13side_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔2 2-1
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_23_G01",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Character(name="avg_npc_220")]
[name="感染者骑士"]  喝啊！
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.2, block=false)]
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[dialog]
[Character(name="avg_npc_219")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="参赛骑士"]  你这感染者——竟敢——
[Character(name="avg_npc_220")]
[name="感染者骑士"]  退场吧，这里不适合你。
[Character(name="avg_npc_219")]
[name="参赛骑士"]  啧！至少要把你拉出得分圈！
[dialog]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral")] 
[Character(name="avg_npc_220")]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="感染者骑士"]  ——！唔！
[name="感染者骑士"]  还好，分数还在——
[dialog]
[Character(name="avg_npc_104")]
[name="锈铜骑士"]  是吗？矿石病垃圾？
[Character(name="avg_npc_220")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="感染者骑士"]  唔！？
[dialog]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_23_G08",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
[Character(name="avg_496_wdmane_1#9")]
[name="艾沃娜"]  啧，英格拉......
[Character(name="avg_npc_033")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="激动的观众"]  好样的！锈铜！就这样！把他逼出得分圈！
[name="激动的观众"]  打烂他的手！就这样！别让这个感染者得手！
[Character(name="avg_npc_033", name2="avg_npc_032", focus=2)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="谨慎的观众"]  嘘！小点声！你看那边的观众席......
[Character(name="avg_npc_033", name2="avg_npc_032", focus=1)]
[name="激动地观众"]  啊啊？那块怎么就坐着她一个人......“感染者骑士席位”？
[Character(name="avg_496_wdmane_1#9")]
[name="艾沃娜"]  ......
[Character(name="avg_npc_033", name2="avg_npc_032", focus=2)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="谨慎的观众"]  小声点，她往这边看过来了。
[Character(name="avg_npc_033", name2="avg_npc_032", focus=1)]
[name="激动的观众"]  哈，座位之间不是有隔离墙吗？她什么都听不见吧？再说，难道感染者还敢翻过来打我不成？
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_23_G01",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Dialog]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.4, block=false)]
[Character]
[CameraShake(duration=0.4, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.4, block=false)]
[Character(name="avg_npc_104")]
[CameraShake(duration=0.4, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_npc_220")]
[name="感染者骑士"]  这才叫骑士剑术，英格拉，你那直来直往的动作真让人看不下去。
[Character(name="avg_npc_104")]
[name="锈铜骑士"]  啐......感染者杂碎......也敢教训我？等我把你剥皮拆骨......你会后悔的。
[Character(name="avg_npc_220")]
[name="感染者骑士"]  （果然是个一点就着的莽夫......就这样等着他失去理智......）
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="感染者骑士"]  （唔，来了......！）
[Dialog]
[Character(name="avg_npc_104")]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.2, block=false)]
[Character(name="avg_npc_220")]
[CameraShake(duration=0.2

... (全文51014字符)
```

### level_act13side_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔2 2-2
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_23_G10",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.4)]
[Character(name="avg_496_wdmane_1#9",fadetime=1,block=true)]
[delay(time=1)]
[name="艾沃娜"]  ......
[Character(name="avg_430_fartth_1", name2="avg_496_wdmane_1#9", focus=1)]
[name="查丝汀娜"]  ......艾沃娜，你回来了。
[Character(name="avg_430_fartth_1#3", name2="avg_496_wdmane_1#9", focus=1)]
[name="查丝汀娜"]  你脸色很差......
[Character(name="avg_430_fartth_1#3", name2="avg_496_wdmane_1#8", focus=2)]
[name="艾沃娜"]  ......当然的吧。
[Character(name="avg_430_fartth_1#3", name2="avg_496_wdmane_1#9", focus=2)]
[name="艾沃娜"]  没能把那些该死的骑士的甲胄全部打烂......啧。
[Character(name="avg_430_fartth_1", name2="avg_496_wdmane_1#9", focus=1)]
[name="查丝汀娜"]  ......不是你的错。
[name="查丝汀娜"]  他没有把身体情况告诉我们任何人。
[Character(name="avg_430_fartth_1", name2="avg_npc_122#2", focus=2)]
[name="索娜"]  如果是这种程度的感染，几个月前他就不该再继续活动了——
[name="索娜"]  他该想办法离开卡西米尔，按自己的想法，安排好自己最后的时日。
[Character(name="avg_npc_123#2", name2="avg_430_fartth_1", focus=1)]
[name="格蕾纳蒂"]  奥尔默·英格拉......这就是卡瓦莱利亚基的骑士贵族，暴虐、无知、草菅人命。
[Character(name="avg_npc_123#3", name2="avg_430_fartth_1", focus=1)]
[name="格蕾纳蒂"]  我就应该在赛场上打断他的四肢......
[Character(name="avg_npc_123#3", name2="avg_430_fartth_1", focus=2)]
[name="查丝汀娜"]  ......也不是你的错，灰毫。
[Character(name="avg_496_wdmane_1#8")]
[name="艾沃娜"]  嘁，明明有我跟着......
[Character(name="avg_npc_122#2", name2="avg_496_wdmane_1#8", focus=1)]
[name="索娜"]  ......他最后......说了什么吗？
[Character(name="avg_npc_122#2", name2="avg_496_wdmane_1#9", focus=2)]
[name="艾沃娜"]  你不会想知道的。
[Character(name="avg_npc_122#2", name2="avg_496_wdmane_1#9", focus=1)]
[name="索娜"]  我希望知道。
[Character(name="avg_npc_122#2", name2="avg_496_wdmane_1#9", focus=2)]
[name="艾沃娜"]  ......好吧。
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Background(image="bg_23_G10",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Character(name="avg_npc_122#2")]
[name="索娜"]  ......
[Character(name="avg_npc_123#6")]
[name="格蕾纳蒂"]  感染者死不瞑目......并不是一件稀罕事。
[name="格蕾纳蒂"]  我们会记住他的愤怒。
[Character(name="avg_npc_122#2")]
[name="索娜"]  ......
[Character(name="avg_npc_123", name2="avg_npc_122#2", focus=1)]
[name="格蕾纳蒂"]  索娜？
[Character(name="avg_npc_123", name2="avg_npc_122#2", focus=2)]
[name="索娜"]  ......他叫杰米。是先成为竞技骑士，再因为意外变成感染者的。
[name="索娜"]  离过婚，有个可爱的小女儿。瞒报病情多半是为了能继续作为骑士参赛吧......他需要钱。
[Character(name="avg_430_fartth_1#2", name2="avg_npc_122#2", focus=1)]
[name="查丝汀娜"]  但为了瞒报病情......他要给骑士协会更多的钱。
[Character(name="avg_430_fartth_1", name2="avg_npc_122#2", focus=1)]
[name="查丝汀娜"]  我在他的房间里发现了他与协会成员的信件，那是个无底洞。
[Character(name="avg_430_fartth_1", name2="avg_npc_122#2", focus=2)]
[name="索娜"]  他是个很乐观的人，乐观到我们甚至察觉不到他在背负这样的事情。
[name="索娜"]  就算是感染了矿石病，和妻子孩子都分道扬镳，他也在帮助别人......
[name="索娜"]  你们还记得吗？他每个清晨都会去帮忙照顾那些孩子。
[Character(name="avg_430_fartth_1", name2="avg_npc_122#8", focus=2)]
[name="索娜"]  他不该这么毫无尊严地死去，这和我们建立骑士团的初衷相悖，可是......
[Character(name="avg_npc_122#8")]
[name="索娜"]  可是我在想......
[name="索娜"]  这样一个对生活满怀热情的人，在最后的最后袒露的是刻骨铭心的仇恨。
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="索娜"]  如果是这样——
[Character(name="avg_npc_123#2", name2="avg_npc_122#8", focus=1)]
[name="格蕾纳蒂"]  ......索娜。
[Character(name="avg_npc_123", name2="avg_npc_122#8", focus=1)]
[name="格蕾纳蒂"]  你最近想的事情太多了，别这么一根筋。
[Character(name="avg_430_fartth_1#2", name2="avg_npc_122#8", focus=1)]
[name="查丝汀娜"]  ......唔......
[Character(name="avg_496_wdmane_1#2")]
[name="艾沃娜"]  ......这些弯弯绕绕的思考工作就交给你们了。
[Character(name="avg_496_wdmane_1#8")]
[name="艾沃娜"]  我要变得更强，强到可以捏碎那些道貌岸然的家伙，强到可以靠自己开辟出一条路来。
[name="艾沃娜"]  血骑士是个不错的榜样，既然卡西米尔如今还愿意认同“骑士”......我们就该这么走下去。
[Character(name="avg_npc_122#8", name2="avg_496_wdmane_1#10", focus=2)]
[name="艾沃娜"]  别想太多，索娜，那只会让你的速度变慢。
[Character(name="avg_430_fartth_1", name2="avg_npc_122#8", focus=1)]
[name="查丝汀娜"]  ......索娜！
[Character(name="avg_430_fartth_1", name2="avg_npc_122", focus=2)]
[name="索娜"]  好啦好啦，我知道，我们得加紧和瑟奇亚克确定——
[dialog]
[Character(name="char_empty")]
[characteraction(name="middle", type="move", xpos=200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="middle", type="move", xpos=-200, fadetime=0.5, block=false)]
[Character(name="avg_430_fartth_1#6",fadetime=0.7)]
[delay(time=1)]
[name="查丝汀娜"]  风......风的响动有变化，虽然只是一瞬间......
[name="查丝汀娜"]  有什么人在盯着这里，而且......
[Character(name="avg_430_fartth_1#6", name2="avg_npc_122#8", focus=2)]
[name="索娜"]  ......无胄盟？
[Character(name="avg_430_fartth_1#6", name2="avg_npc_122", focus=1)]
[name="查丝汀娜"]  气息隐藏得很好......但如果是敌人的话早就该袭击我们了......
[Character(name="avg_496_wdmane_1#8")]
[name="艾沃娜"]  ——出来。
[Character(name="avg_496_wdmane_1#9")]
[name="艾沃娜"]  这里是感染者的地盘，普通人可不会随便跑到这里。
[Character(name="avg_496_wdmane_1#8")]
[name="艾沃娜"]  否则的话——
[dialog]
[character]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(name="avg_npc_213_1",fadetime=1,block=true)]
[delay(time=2)]
[name="托兰"]  好，好，好，别那么大声，唉。
[name="托兰"]  感染者骑士，真是没想过的一道风景。十几年没有靠近过卡瓦莱利亚基，骑士老爷和商人们也真是异想天开......
[Character(name="avg_npc_123")]
[name="格蕾纳蒂"]  ......你是谁？
[Character(name="avg_npc_213_1")]
[name="托兰"]  别误会，我只是找某些人，凑巧路过这里，不过嘛，相逢即是缘......
[name="托兰"]  ......我想我们应该有些共同话题，各位感染者，例如......无胄盟。
[Character(name="avg_npc_122#5")]
[name="索娜"]  很遗憾，今天我们遭遇了一些不幸的事情，如果真想聊天的话，改日再说吧。
[Character(name="avg_npc_213_1#3")]
[name="托兰"]  是吗？这还真是不凑巧，令人遗憾。
[Character(name="avg_npc_213_1")]
[name="托兰"]  那我只好去别的地方再试试运气啦，毕竟难得来一趟大骑士领。
[name="托兰"]  那么就不打扰各位啦......但也许我们很快就会再见的。
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_23_G07",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_23_G05",screenadapt="co

... (全文34447字符)
```

### level_act13side_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔2 3-1
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_23_G03",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Character(name="avg_npc_211_1#5",fadetime=1,block=true)]
[delay(time=1)]
[name="发言人马克维茨"]  ......
[Character(name="avg_npc_211_1#5", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  我听说，你向国民院检举了奥尔默·英格拉？
[Character(name="avg_npc_211_1#6", name2="avg_npc_212_1", focus=1)]
[name="发言人马克维茨"]  ......是的。
[name="发言人马克维茨"]  在特锦赛上闹出人命，如果这还不用受到制裁，那法律究竟......
[Character(name="avg_npc_211_1#6", name2="avg_npc_212_1#2", focus=2)]
[name="发言人麦基"]  我们都很清楚国民院的行事作风，马克维茨兄。你过去创业的时候，和他们打交道还少吗？
[Character(name="avg_npc_211_1#6", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  别纠结太久了，稍后你得去一趟感染者收容治疗地区，安排一下那里的几个医疗企业与骑士协会的对接。
[name="发言人麦基"]  往好处想，这份工作也是在救人，不是吗？
[Character(name="avg_npc_211_1#5", name2="avg_npc_212_1", focus=1)]
[name="发言人马克维茨"]  ......
[Character(name="avg_npc_211_1#5", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  别太累......你这样会累垮自己的，我先去开会了。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[characteraction(name="right", type="move", xpos=300, fadetime=2,block=false)]
[character(name="avg_npc_211_1",name2="char_empty",fadetime=0.5)]
[delay(time=2)]
[Character(name="avg_npc_211_1#7")]
[name="发言人马克维茨"]  ......唉。
[dialog]
[PlaySound(key="$phone",volume=0.6)]
[CameraShake(duration=1, xstrength=5, ystrength=3, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_npc_211_1#3")]
[name="发言人马克维茨"]  ......！
[PlaySound(key="$d_gen_transmissionget",volume=0.6)]
[delay(time=0.5)]
[Character(name="avg_npc_211_1#5")]
[name="发言人马克维茨"]  喂，您好......
[Character(name="avg_npc_211_1#5", focus=-1)]
[name="电话那头的声音"]  发言人马克维茨阁下，您好。
[name="电话那头的声音"]  我是国民院副审官，我们收到了发言人的诉讼。
[Character(name="avg_npc_211_1#3")]
[name="发言人马克维茨"]  啊......
[Character(name="avg_npc_211_1#4")]
[name="发言人马克维茨"]  ......你们打算怎么处理？
[Character(name="avg_npc_211_1#4", focus=-1)]
[name="电话那头的声音"]  检举不符合联合会规定的骑士，是发言人的义务，正因如此，您对于锈铜骑士的一些......意见，我们也会优先考虑。
[name="电话那头的声音"]  但关于锈铜骑士奥尔默·英格拉，事情有一些复杂。
[name="电话那头的声音"]  您应该知道，不久前，英格拉的保释申请刚刚得到国民院的批准，现在再对他进行审判，恐怕有损国民院的权威......
[name="电话那头的声音"]  当然了......发言人的诉求就是董事会的诉求，我们只能这么理解，我们不会拒绝您。
[Character(name="avg_npc_211_1#8")]
[name="发言人马克维茨"]  ......所以才有了这通电话，我明白，国民院的条件是？
[Character(name="avg_npc_211_1#8", focus=-1)]
[name="电话那头的声音"]  哦......条件？您可别这么说，我希望您理解成这是工作上的沟通。
[name="电话那头的声音"]  恰尔内先生遭到了流程之外的流放，这件事出乎许多人预料。即使是我们，也不认为恰尔内先生的失误有如此糟糕。
[name="电话那头的声音"]  但无论如何，事情已经发生。恰尔内离开了大骑士领，失去了发言人的地位。
[name="电话那头的声音"]  但是也因为这次流放的突然，我们没能配合各方，做好善后工作。
[Character(name="avg_npc_211_1#8")]
[name="发言人马克维茨"]  ......你......
[Character(name="avg_npc_211_1#8", focus=-1)]
[name="电话那头的声音"]  玫瑰新闻联合报业为锈铜骑士支付的献金，正是通过恰尔内先生之手。
[name="电话那头的声音"]  恰尔内先生知道太多事情了......马克维茨先生，您明白吗？
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.6, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="我能听到自己的心跳。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.6, block=true)]
[Background(image="bg_23_G03",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.6, block=true)]
[Character(name="avg_npc_211_1#7")]
[name="发言人马克维茨"]  我......不明白......
[Character(name="avg_npc_211_1#7", focus=-1)]
[name="电话那头的声音"]  如果您保证恰尔内先生永远不会成为我们之间的问题......那么我们一定会将锈铜骑士绳之于法。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.6, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="我从未想过这种事情会发生在我身上。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="或者，其实我想过。只是我不觉得我是有决定权的这一方。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_23_G03",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Character(name="avg_npc_211_1#4")]
[name="发言人马克维茨"]  ......
[name="发言人马克维茨"]  您......的意思是......
[Character(name="avg_npc_211_1#4", focus=-1)]
[name="电话那头的声音"]  我能理解特锦赛事务繁忙，不急于当下。只要您答应我，会让恰尔内先生体面地消失，我立刻就去操办此事。
[name="电话那头的声音"]  当然，我们也会随着恰尔内先生的消失而......建立起深厚的信赖关系。
[Character(name="avg_npc_211_1#2")]
[name="发言人马克维茨"]  ......
[name="发言人马克维茨"]  ......抱歉，恐怕我现在还不能给您答复......
[Character(name="avg_npc_211_1#2", focus=-1)]
[name="电话那头的声音"]  ......那很遗憾。希望您尽早下定决心，锈铜骑士阁下的禁赛期并不算长。
[name="电话那头的声音"]  随时欢迎您的来电，马克维茨先生。祝您有美好的一天。
[PlaySound(key="$transmission",volume=0.6)]
[Character(name="avg_npc_211_1#5")]
[name="发言人马克维茨"]  ......
[dialog]
[PlaySound(key="$doorknockquite", volume=0.6)]
[delay(time=1)]
[Character(name="avg_npc_211_1#3")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="发言人马克维茨"]  ......啊！
[delay(time=1)]
[Character(name="avg_npc_211_1#3", focus=-1)]
[name="门外的人"]  马克维茨先生？ 您在吗？
[Character(name="avg_npc_211_1#4")]
[name="发言人马克维茨"]  请、请进......
[PlaySound(key="$dooropenquite", volume=0.6)]
[Dialog]
[Character(name="avg_npc_121#2",fadetime=1,block=true)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[delay(time=1)]
[name="大嘴莫布"]  啊......马克维茨先生......很抱歉打扰您了。
[name="大嘴莫布"]  事实上，呃，我最

... (全文21230字符)
```

### level_act13side_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔2 3-2
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_23_G10",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Character(name="avg_npc_220", name2="avg_npc_221", focus=1)]
[name="感染者骑士"]  打倒联合会！打倒贵族！处死奥尔默·英格拉！
[Character(name="avg_npc_220", name2="avg_npc_221", focus=2)]
[name="感染者骑士"]  打倒联合会！打倒贵族！处死奥尔默·英格拉！
[Character(name="avg_430_fartth_1#6")]
[name="查丝汀娜"]  ......
[Character(name="avg_430_fartth_1#2")]
[name="查丝汀娜"]  ......愤怒在我们之间蔓延。
[Character(name="avg_430_fartth_1")]
[name="查丝汀娜"]  我能理解，但是......
[Character(name="avg_430_fartth_1", name2="avg_npc_122#2", focus=2)]
[name="索娜"]  ......愤怒，我们已经习惯了这种情绪。
[Character(name="avg_430_fartth_1", name2="avg_npc_122", focus=2)]
[name="索娜"]  但是愤怒会让人短视，我们已经吃过了苦头。
[Character(name="avg_npc_122", name2="avg_496_wdmane_1", focus=2)]
[name="艾沃娜"]  哈，保持冷静可不是我的风格。
[Character(name="avg_npc_122", name2="avg_496_wdmane_1", focus=1)]
[name="索娜"]  你冷静地向前冲就行了嘛。
[Character(name="avg_npc_122", name2="avg_496_wdmane_1", focus=2)]
[name="艾沃娜"]  ......也行，那麻烦的事情就交给你们啦，干架，交给我。
[Character(name="avg_npc_122", name2="avg_496_wdmane_1#9", focus=2)]
[name="艾沃娜"]  我憋了很久了，索娜。
[Character(name="avg_npc_122#2", name2="avg_496_wdmane_1#9", focus=1)]
[name="索娜"]  我知道。
[name="索娜"]  在瑟奇亚克和小灰回来之前，我们必须找到当时的参与人......记者也好，目击者也罢，越多越好。
[Character(name="avg_430_fartth_1", name2="avg_npc_122#2", focus=1)]
[name="查丝汀娜"]  ......四城大隔断。
[name="查丝汀娜"]  对外报道是莱塔尼亚激进分子的破坏导致的工程事故，为了破坏特锦赛的顺利举行。
[Character(name="avg_430_fartth_1", name2="avg_npc_122", focus=2)]
[name="索娜"]  城市哪有这么脆弱，多半是互相掣肘的结果吧。
[name="索娜"]  但是，那场骚动确实让人看到了卡瓦莱利亚基......这座“伟大之城”的腐败之处，究竟在哪里。
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_23_G07",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Character(name="avg_npc_123#3")]
[name="格蕾纳蒂"]  ......
[Character(name="avg_npc_123")]
[name="格蕾纳蒂"]  我就算了，你也算是小有名气的骑士吧，就这么大摇大摆，不怕被人认出来？
[Character(name="avg_npc_123", name2="avg_npc_103nc_1#6", focus=2)]
[name="塑料骑士"]  ......特锦赛期间，谁会在意我这种小人物呢。
[Character(name="avg_npc_123", name2="avg_npc_103nc_1", focus=2)]
[name="塑料骑士"]  为什么是你和我同行？我以为会是那个狙击手，她更适合做这类事。
[Character(name="avg_npc_123#3", name2="avg_npc_103nc_1", focus=1)]
[name="格蕾纳蒂"]  查丝汀娜吗，她其实比我更容易暴露，更别提，她还是冒着风险把你救出来的那个人。
[Character(name="avg_npc_123#2", name2="avg_npc_103nc_1", focus=1)]
[name="格蕾纳蒂"]  没必要让危险因素聚在一起，你们都是弓弩骑士，如果真的在街巷里遭到袭击，不好对付。
[Character(name="avg_npc_123#2", name2="avg_npc_103nc_1", focus=2)]
[name="塑料骑士"]  说得好听，你只是想来盯着我而已吧？
[Character(name="avg_npc_123#2", name2="avg_npc_103nc_1", focus=1)]
[name="格蕾纳蒂"]  ......哼。
[name="格蕾纳蒂"]  一个骑士贵族，就算因为和无胄盟发生冲突，也不可能消除和感染者的隔阂。你觉得我真会对你放下戒备？
[Character(name="avg_npc_123#2", name2="avg_npc_103nc_1#4", focus=2)]
[name="塑料骑士"]  废话。我害怕被感染，也害怕家人被感染，这能有什么问题？
[Character(name="avg_npc_123#2", name2="avg_npc_103nc_1#5", focus=2)]
[name="塑料骑士"]  不要以为只有你不信任我，灰毫骑士。
[Character(name="avg_npc_123", name2="avg_npc_103nc_1#5", focus=1)]
[name="格蕾纳蒂"]  是吗，那现在好像是你逃走的最好时机，塑料骑士。
[name="格蕾纳蒂"]  前提是——
[Character(name="avg_npc_123", name2="avg_npc_103nc_1#5", focus=2)]
[name="塑料骑士"]  ——少说废话，小屁孩。
[Character(name="avg_npc_123#2", name2="avg_npc_103nc_1#5", focus=1)]
[name="格蕾纳蒂"]  ......
[Character(name="avg_npc_123#2", name2="avg_npc_103nc_1#2", focus=2)]
[name="塑料骑士"]  我不是来陪你们玩弱者抱团游戏的，我完全不关心你们的诉求，以及你们之间是不是真的需要相互信任——
[name="塑料骑士"]  ——我只是来找胆大包天的混蛋，无胄盟不会轻易放过我，更不会放过我的家人，那么我就要先下手为强。
[Character(name="avg_npc_123#2", name2="avg_npc_103nc_1#5", focus=2)]
[name="塑料骑士"]  所以我现在站在这里，只是为了我的妻子和孩子，真的，和你们可笑的事业没有半点关系。
[Character(name="avg_npc_123#2", name2="avg_npc_103nc_1", focus=2)]
[name="塑料骑士"]  别太自以为是，感染者，你觉得这座城市里只有“你们的敌人”和“你们的朋友”？典型的被害妄想......
[name="塑料骑士"]  告诉你吧，在卡西米尔，在这个社会，大部分人，“和你们根本没有关系”。
[stopmusic(fadetime=1)]
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_23_G04",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Character(name="avg_npc_123", name2="avg_npc_103nc_1", focus=1)]
[name="格蕾纳蒂"]  ......这附近很安静。
[Character(name="avg_npc_123", name2="avg_npc_103nc_1", focus=2)]
[name="塑料骑士"]  这里是联合会大楼的底层。再往下的构造区，只有移动城市的工程师和维修人员才能进入，我们得在这里止步了。
[Character(name="avg_npc_123", name2="avg_npc_103nc_1#6", focus=2)]
[name="塑料骑士"]  呵。
[Character(name="avg_npc_123", name2="avg_npc_103nc_1#6", focus=1)]
[name="格蕾纳蒂"]  ......
[Character(name="avg_npc_123", name2="avg_npc_103nc_1", focus=2)]
[name="塑料骑士"]  别担心，不用那么谨慎，这附近没有摄像头。
[Character(name="avg_npc_123", name2="avg_npc_103nc_1", focus=1)]
[name="格蕾纳蒂"]  那你能保证没有无胄盟吗？
[Character(name="avg_npc_123", name2="avg_npc_103nc_1#6", focus=2)]
[name="塑料骑士"]  说个笑话，无胄盟不会在公开场合——特别是这些社会精英汇聚的地方大开杀戒。
[name="塑料骑士"]  这样会给监正会太多把柄，这就是他们的局限性，我们要巧妙地利用这些局限性。
[Character(name="avg_npc_123", name2="avg_npc_103nc_1", focus=2)]
[name="塑料骑士"]  说实在的，卡西米尔有多少骑士？他们只会用身份识别卡之类的手段来判断身份......伪装很容易。
[Character(name="avg_npc_123", name2="avg_npc_103nc_1", focus=1)]
[name="格蕾纳蒂"]  ......那你的家人怎么办？
[Character(name="avg_npc_123", name2="avg_npc_103nc_1", focus=2)]
[name="塑料骑士"]  除了我失踪的妻儿，其他人已经被送去大骑士领外了。
[Character(name="avg_npc_123", name2="avg_npc_103nc_1", focus=1)]
[name="格蕾纳蒂"]  无胄盟可不止在大骑士领有眼线。
[Character(name="avg_npc_123", name2="avg_npc_103nc_1#2", focus=2)]
[name="塑料骑士"]  ......我知道。
[name="塑料骑士"]  也许再给我一次机会，我不会那么冲动，至少等到我的孩子长大，能够照顾自己。
[Character(name="avg_npc_123", name2="avg_npc_103nc_1#6", focus=2)]
[name="塑料骑士"]  但商业联合会也不卖后悔药，事已至此，感染者，我们还是不要这么怨天尤人了。
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_23_G09",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Character(name="avg_npc_223")]
[name="企业员工"]  ......唔......该死，超市和餐馆都关门了，为什么要定这个时间开会......
[name="企业员工"]  唉......凌晨改稿子的话，明天也许能在审稿会上少挨几句骂——
[name="企业员工"]  ——唔？
[delay(time=1)

... (全文38891字符)
```

### level_act13side_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔2 3-2
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_courtyard",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.4)]
[Character(name="avg_npc_064_weapon_1#5")]
[name="佐菲娅"]  薇薇安娜·德罗斯特，第一次参加骑士竞技就赢得封号，“微光”薇薇安娜，三年后首次参加特锦赛，成为大骑士受封“烛骑士”。
[name="佐菲娅"]  论天资，她是史上最年轻的十位大骑士之一，论实力，她至今仍在稳步提升，不可小觑。
[delay(time=1)]
[Character(name="avg_npc_064_weapon_1#6")]
[name="佐菲娅"]  ......玛嘉烈，你在听吗？
[Character(name="avg_npc_064_weapon_1#6", name2="avg_1014_nearl2_1#6$1", focus=2)]
[name="玛嘉烈"]  ......嗯，只是有些怀念。
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1#6", focus=1)]
[name="玛莉娅"]  以前，姑母和姐姐也是这样......迎战特锦赛的吗？
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1", focus=2)]
[name="佐菲娅"]  那个时候啊......呵呵。
[name="佐菲娅"]  某些人比赛结束之后就不见人影，要么躲在房间里钻研下一个对手的特点，要么自己偷偷去找玛恩纳锻炼剑术......
[name="佐菲娅"]  还记得玛嘉烈第一次获胜的时候，说好了咱们在这儿办个庆功宴，结果这家伙自己忘记了。
[name="佐菲娅"]  我们找到她的时候，她正拖着受伤的身子，在院子里尝试自己的源石技艺......
[name="佐菲娅"]  我当时就想问了，你不疼吗？
[Character(name="avg_npc_064_weapon_1", name2="avg_1014_nearl2_1#1$1", focus=2)]
[name="玛嘉烈"]  ......因为我的源石技艺也是可以缓解伤痛的，所以......
[Character(name="avg_npc_064_weapon_1", name2="avg_1014_nearl2_1#1$1", focus=1)]
[name="佐菲娅"]  那终究不是真正的治疗，不然现代医学还有什么价值？
[Character(name="avg_npc_064_weapon_1", name2="avg_1014_nearl2_1#6$1", focus=2)]
[name="玛嘉烈"]  呵呵......我不否认。
[name="玛嘉烈"]  我可认识许多令人惊叹的医生，多亏了他们难能可贵的技术，拯救他人不再是一个遥不可及的想法。
[Character(name="avg_npc_064_weapon_1", name2="avg_1014_nearl2_1#6$1", focus=1)]
[name="佐菲娅"]  ......罗德岛制药？还是那两位萨卡兹小姐？
[Character(name="avg_npc_064_weapon_1", name2="avg_1014_nearl2_1#1$1", focus=2)]
[name="玛嘉烈"]  都是。他们都是与苦难斗争的人们。
[Character(name="avg_npc_061#2", name2="avg_1014_nearl2_1#1$1", focus=1)]
[name="玛莉娅"]  说起来，闪灵小姐和夜莺小姐，都去和罗德岛的朋友们会合了吧？
[name="玛莉娅"]  不知道他们现在怎么样......
[Character(name="avg_npc_061#2", name2="avg_1014_nearl2_1#1$1", focus=2)]
[name="玛嘉烈"]  哪怕在这座大骑士领内，他们依旧在尽其所能地帮助感染者，我相信他们。
[Character(name="avg_npc_061#2", name2="avg_1014_nearl2_1#2$1", focus=2)]
[name="玛嘉烈"]  ......但我自己要做的事情和罗德岛的意志无关。我不能把这份责任强加在他们身上。
[Character(name="avg_npc_061#2", name2="avg_1014_nearl2_1#1$1", focus=2)]
[name="玛嘉烈"]  所以我脱离了罗德岛。
[Character(name="avg_npc_061#7", name2="avg_1014_nearl2_1#1$1", focus=1)]
[name="玛莉娅"]  姐姐......偶尔也稍微照顾一下自己啊。
[Character(name="avg_npc_061#7", name2="avg_npc_064_weapon_1", focus=2)]
[name="佐菲娅"]  这话轮不到你来说，论乱来的程度，玛莉娅你有过之而无不及。
[Character(name="avg_npc_061", name2="avg_npc_064_weapon_1", focus=1)]
[CameraShake(duration=0.3, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="玛莉娅"]  ......哈哈......
[Character(name="avg_npc_064_weapon_1#5", name2="avg_1014_nearl2_1#1$1", focus=1)]
[name="佐菲娅"]  好了——总之。
[name="佐菲娅"]  现在要怎么做？虽然我觉得对现在的你而言，训练已经没有什么意义了......
[name="佐菲娅"]  但这是你时隔多年再一次对上一位大骑士，要不要适当运动一下，回到最佳状态？
[Character(name="avg_npc_064_weapon_1#5", name2="avg_1014_nearl2_1#6$1", focus=2)]
[name="玛嘉烈"]  麻烦了，佐菲娅。
[Character(name="avg_npc_064_weapon_1#5", name2="avg_1014_nearl2_1#6$1", focus=1)]
[name="佐菲娅"]  好。
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1", focus=2)]
[name="佐菲娅"]  玛莉娅，来。
[Character(name="avg_npc_061#4", name2="avg_npc_064_weapon_1", focus=1)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="玛莉娅"]  欸、欸？我不是在旁边看着就行吗？
[Character(name="avg_npc_061#4", name2="avg_npc_064_weapon_1#4", focus=2)]
[name="佐菲娅"]  看着就行？那我让你带装备来做什么？上次的结果你没看见吗？还想让我一个人对付耀骑士吗？
[Character(name="avg_npc_061#3", name2="avg_npc_064_weapon_1#4", focus=1)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="玛莉娅"]  呜......
[Character(name="avg_npc_064_weapon_1", name2="avg_1014_nearl2_1#4$1", focus=2)]
[name="玛嘉烈"]  佐菲娅，要是她不愿意的话......
[Character(name="avg_npc_064_weapon_1#5", name2="avg_1014_nearl2_1#4$1", focus=1)]
[name="佐菲娅"]  你也别总惯着她！
[Character(name="avg_npc_064_weapon_1#5", name2="avg_1014_nearl2_1#5$1", focus=2)]
[name="玛嘉烈"]  ......好。
[Character(name="avg_npc_061#6", name2="avg_npc_064_weapon_1#5", focus=1)]
[CameraShake(duration=0.3, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="玛莉娅"]  要、要和姐姐对练吗？我还从来没有过......
[Character(name="avg_npc_061#6", name2="avg_npc_064_weapon_1#5", focus=2)]
[name="佐菲娅"]  玛嘉烈参赛的时候，你还只是个孩子嘛。虽然现在也是。
[name="佐菲娅"]  玛莉娅。
[Character(name="avg_npc_061#5", name2="avg_npc_064_weapon_1#5", focus=1)]
[name="玛莉娅"]  在、在！
[Character(name="avg_npc_061#5", name2="avg_npc_064_weapon_1#5", focus=2)]
[name="佐菲娅"]  让咱们的耀骑士见识一下，独立骑士玛莉娅·临光，是怎么战胜左手骑士的。
[Character(name="avg_npc_061#5", name2="avg_npc_064_weapon_1#5", focus=1)]
[name="玛莉娅"]  ......是！
[Character(name="avg_npc_061#5")]
[name="玛莉娅"]  姐姐......请多指教！
[Character(name="avg_1014_nearl2_1#2$1")]
[name="玛嘉烈"]  ......
[Character(name="avg_1014_nearl2_1#7$1")]
[name="玛嘉烈"]  ......好。
[dialog]
[delay(time=0.5)]
看着玛莉娅的眼神，耀骑士突然回忆起了某个人的某句话。
[delay(time=0.5)]
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="她放弃了......骑士之路吗？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="是我，令她放弃了吗？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.6)]
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2.5, block=true)]
[Background(image="bg_nearllivingroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b

... (全文41772字符)
```

### level_act13side_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔2 4-2
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="薇薇安娜·德罗斯特，这是你的名字。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="你是家族的耻辱......如果被其他贵族知道，你会成为别人攻击你父亲的道具。", x=200, y=370, alignment="center", size=24, delay=0.04, width=900)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="你应当被秘密流放，或是干脆被处死。高塔不该听闻你的啼哭。", x=200, y=370, alignment="center", size=24, delay=0.04, width=900)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="但，你被带来了卡西米尔，你被委托给了一位卡西米尔的征战骑士抚养。", x=200, y=370, alignment="center", size=24, delay=0.04, width=900)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="甚至没有人隐瞒你的身份，你这本应讳莫如深的身份。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="就好像他们所有人都希望你能坦荡地活着一样。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="多么可敬又可悲......你的贵族父亲，你那不知名的母亲，他们竟然都爱着你。", x=200, y=370, alignment="center", size=24, delay=0.04, width=900)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[stopmusic(fadetime=1.5)]
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[Background(image="bg_23_G01",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[playsound(key="$e_atk_magic_n", volume=0.4)]
[CameraShake(duration=0.3, xstrength=4, ystrength=4, vibrato=20, randomness=30, fadeout=true)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.3, block=false)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.3, block=false)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[playsound(key="$e_atk_magic_n", volume=0.4)]
[CameraShake(duration=0.3, xstrength=4, ystrength=4, vibrato=20, randomness=30, fadeout=true)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.6, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$swordtsing1", volume=0.9)]
[Blocker(a=0, fadetime=1.3, block=false)]
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$swordtsing2", volume=0.9)]
[Blocker(a=0, fadetime=1.3, block=false)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_1014_nearl2_1#4$1",fadetime=1,block=true)]
[delay(time=1)]
[name="玛嘉烈"]  ......唔。
[Character(name="avg_1014_nearl2_1#1$1")]
[name="玛嘉烈"]  烛火和......阴影。
[Character(name="avg_npc_215_1#1", name2="avg_1014_nearl2_1#1$1", focus=1)]
[name="烛骑士"]  真令人惊奇......你似乎很懂得如何对法术现象进行归纳......
[name="烛骑士"]  当房间里点燃一支蜡烛时，最吸引你目光的是那点烛光，而真正将你包裹的，是周遭所有器物的影子。
[Character(name="avg_npc_215_1#1", name2="avg_1014_nearl2_1#2$1", focus=2)]
[name="玛嘉烈"]  令人赞叹的技艺，薇薇安娜......我的光甚至无法......照亮你。
[Character(name="avg_npc_215_1#5", name2="avg_1014_nearl2_1#2$1", focus=1)]
[name="烛骑士"]  ......抱歉。
[Character(name="avg_npc_215_1#5", name2="avg_1014_nearl2_1#4$1", focus=2)]
[name="玛嘉烈"]  ......什么？
[Character(name="avg_npc_215_1#2", name2="avg_1014_nearl2_1#4$1", focus=1)]
[name="烛骑士"]  我想，按礼节来说，我也应该称呼您的名字，玛嘉烈小姐。
[stopmusic(fadetime=1)]
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_23_G08",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
[Character(name="avg_npc_121#2")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomnes

... (全文53133字符)
```

### level_act13side_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔2 5-1
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_warehouse",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Character(name="avg_npc_102")]
[CameraShake(duration=0.8, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="凋零骑士"]  咕——咕啊啊——
[delay(time=1)]
[Character(name="avg_npc_102_2")]
[name="腐败骑士"]  ......
[dialog]
[character]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$bottlebroken")]
[delay(time=1)]
[Character(name="avg_npc_102")]
[CameraShake(duration=0.8, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="凋零骑士"]  啊——啊啊啊——
[Character(name="avg_npc_216")]
[name="无胄盟成员"]  ......报告，凋零骑士服药后产生了明显的排斥反应。
[delay(time=0.5)]
[name="无胄盟成员"]  不......在其他骑士身上并没有发现类似的反应，在场的药师推测是萨卡兹的过敏反应......
[name="无胄盟成员"]  什么？可......可这很浪费......
[name="无胄盟成员"]  浓度比例......已经接近常规的凝胶修复液了，这玩意是用来修盔甲的啊，继续注射会对人脑造成不可逆的损伤......
[name="无胄盟成员"]  ......
[delay(time=0.5)]
[name="无胄盟成员"]  好吧，我明白，他们是萨卡兹，不是人类......
[name="无胄盟成员"]  唉，你们也听见了，再增加百分之零点三......测试一下萨卡兹的极限。
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_23_G05",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_225",fadetime=1,block=true)]
[delay(time=1)]
[name="逐魇骑士"]  ......
[name="逐魇骑士"]  你们，是什么东西？
[Character(name="avg_npc_102", name2="avg_npc_102_2", focus=1)]
[name="凋零骑士"]  嘎啊......嘎啊......
[Character(name="avg_npc_102", name2="avg_npc_102_2", focus=2)]
[name="腐败骑士"]  ......你......梦魇......死......
[dialog]
[Character(name="avg_npc_225")]
年轻的梦魇长叹一口气。他仰头望去，熟悉的黑夜被灯光驱散。
这也是文明兴起的象征吗？卡西米尔在用霓虹灯征服黑夜吗？
他突然有些感伤。
[stopmusic(fadetime=2.5)]
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[Background(image="bg_sportsbar",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[PlaySound(key="$dooropenquite", volume=0.6)]
[playMusic(intro="$bar_intro", key="$bar_loop", volume=0.4)]
[PlaySound(key="$rungeneral", volume=0.6)]
[delay(time=1)]
[Character(name="avg_npc_061#2",fadetime=1,block=true)]
[delay(time=1)]
[name="玛莉娅"]  各位！
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1#3", focus=2)]
[name="佐菲娅"]  玛莉娅！
[characteraction(name="right", type="move", xpos=-180, fadetime=1,block=false)]
[delay(time=1)]
[name="佐菲娅"]  你没事......你没事真是太好了！
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1#3", focus=1)]
[name="玛莉娅"]  哎、哎，佐菲娅姐姐？别、别哭啊......
[Character(name="avg_npc_107", name2="avg_npc_061#2", focus=1)]
[name="光头马丁"]  你没事就好，玛莉娅。
[dialog]
[character]
[Character(name="avg_npc_120#4", name2="avg_npc_061#2", focus=1)]
[name="老骑士"]  要是你出了什么事情，我们可没脸去见临光老爷。
[Character(name="avg_npc_061#2", name2="avg_npc_101", focus=2)]
[name="老工匠"]  虽然现在也没脸去见就是了。
[Character(name="avg_npc_061#2")]
[name="玛莉娅"]  啊哈哈......各位还很长寿呢，胡说什么呢，咳咳。
[dialog]
[character]
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1#3", focus=1)]
[characteraction(name="right", type="move", xpos=-180, fadetime=0.01,block=false)]
[name="玛莉娅"]  那个......佐菲娅姐姐？差不多可以放手了吧......？
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1#3", focus=2)]
[name="佐菲娅"]  ......
[characteraction(name="right", type="move", xpos=180, fadetime=3,block=false)]
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1#3", focus=2)]
[name="佐菲娅"]  ......嗯。
[delay(time=1)]
[Character(name="avg_npc_213_1")]
[name="托兰"]  打扰这一幅姐妹情深的情景实在让人于心不忍......不过玛嘉烈似乎不在这里？
[Character(name="avg_npc_064_weapon_1#6", name2="avg_npc_213_1", focus=1)]
[name="佐菲娅"]  ......呃，你什么时候......
[Character(name="avg_npc_064_weapon_1#6", name2="avg_npc_213_1#6", focus=2)]
[name="托兰"]  从你带着哭腔抱上去开始。
[Character(name="avg_npc_064_weapon_1#6", name2="avg_npc_213_1#6", focus=1)]
[name="佐菲娅"]  呀......你是谁？
[Character(name="avg_npc_061#2", name2="avg_npc_213_1#6", focus=1)]
[name="玛莉娅"]  啊，他是刚才帮我——
[Character(name="avg_npc_120#2", name2="avg_npc_213_1#6", focus=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="老骑士"]  你......！你、你是......
[Character(name="avg_npc_120#2", name2="avg_npc_213_1", focus=2)]
[name="托兰"]  你认错人了，老骑士先生。
[Character(name="avg_npc_120#3", name2="avg_npc_213_1", focus=1)]
[name="老骑士"]  ......
[Character(name="avg_npc_213_1")]
[name="托兰"]  所以，玛嘉烈呢？
[name="托兰"]  出了这么大事，我们神经大条的耀骑士难道还在勇闯特锦赛吗？
[Character(name="avg_npc_061#7", name2="avg_npc_213_1", focus=1)]
[name="玛莉娅"]  ......我......我不知道该不该告诉姐姐......
[Character(name="avg_npc_061#7", name2="avg_npc_213_1#3", focus=2)]
[name="托兰"]  嚯。
[Character(name="avg_npc_061#5", name2="avg_npc_213_1#3", focus=1)]
[name="玛莉娅"]  无胄盟不会善罢甘休的吧......他们迟早会再攻击过来的，大家都会有危险！
[Character(name="avg_npc_061#7", name2="avg_npc_213_1#3", focus=1)]
[name="玛莉娅"]  但是......但是如果告诉了姐姐......才是正中他们的下怀......
[Character(name="avg_npc_061#7", name2="avg_npc_213_1#2", focus=2)]
[name="托兰"]  在这座大骑士领，你们无处可逃，他们迟早都会来的。
[name="托兰"]  今时不同往日，哪怕是下一秒和现在比起来，商业联合会都在壮大自身。
[Character(name="avg_npc_061#7", name2="avg_npc_064_weapon_1#5", focus=2)]
[name="佐菲娅"]  ......为了你的安全，玛莉娅，你姐姐必须知道这件事。
[Character(name="avg_npc_061#7", name2="avg_npc_064_weapon_1#5", focus=1)]
[name="玛莉娅"]  姐姐知道了，就能解决吗？
[Character(name="avg_npc_061#7")]
[name="玛莉娅"]  姐姐放弃了特锦赛，他们真的就会就此罢休吗？
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="在这座城市坚持的骑士们，真的还有出路吗？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[Character(name="avg_npc_061#6")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="玛莉娅"]  ......！
[name="玛莉

... (全文19247字符)
```

### level_act13side_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔2 5-2
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_23_G05",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Character(name="avg_npc_209_1", name2="avg_npc_208_1", focus=2)]
[name="莫妮克"]  ......之前我还奇怪，为什么你们要带着那个路都走不了的萨卡兹。
[name="莫妮克"]  原来如此。
[Character(name="avg_npc_209_1#4", name2="avg_npc_208_1", focus=1)]
[name="罗伊"]  呃......莫妮克阁下，我怎么什么都没感觉到......
[Character(name="avg_npc_209_1#4", name2="avg_npc_208_1#5", focus=2)]
[name="莫妮克"]  ......那就少说话，少丢脸。
[dialog]
[Character(name="avg_1014_nearl2_1#1$1",fadetime=1,block=true)]
[delay(time=1)]
[name="玛嘉烈"]  ......无胄盟吗，有何贵干？
[Character(name="avg_npc_209_1", name2="avg_1014_nearl2_1#1$1", focus=1)]
[name="罗伊"]  首先，请允许我向耀骑士道歉。
[name="罗伊"]  关于今天无胄盟绑架了玛莉娅一事——
[Character(name="avg_npc_209_1", name2="avg_1014_nearl2_1#7$1", focus=2)]
[name="玛嘉烈"]  ——
[Character(name="avg_npc_209_1#3", name2="avg_1014_nearl2_1#7$1", focus=1)]
[name="罗伊"]  ——喔，别冲动，再说也不是我干的啊。
[Character(name="avg_npc_209_1#3", name2="avg_1014_nearl2_1#7$1", focus=2)]
[name="玛嘉烈"]  ......你们......卑劣的刽子手！
[Character(name="avg_npc_209_1", name2="avg_1014_nearl2_1#1$1", focus=1)]
[name="罗伊"]  玛莉娅此时应该已经安全回家了，放心，没有后续针对你们的行动，就算有，也会尽量做得......不那么完美。
[name="罗伊"]  无胄盟也只是收钱办事，就算我们不想，毕竟上面的人也盯着，你说对吧？
[Character(name="char_147_shining_1", name2="avg_npc_209_1", focus=1)]
[name="闪灵"]  ......你们在袭击感染者。
[Character(name="char_147_shining_1", name2="avg_npc_209_1", focus=2)]
[name="罗伊"]  这也是上面的安排，别怪我们啊。
[Character(name="avg_npc_209_1", name2="avg_1014_nearl2_1#7$1", focus=2)]
[name="玛嘉烈"]  恶行不因为其缘由而洗刷罪孽。
[Character(name="avg_npc_209_1", name2="avg_1014_nearl2_1#7$1", focus=1)]
[name="罗伊"]  ......说的也是。
[name="罗伊"]  所以，我们今天这不是来打声招呼吗......
[Character(name="avg_npc_209_1", name2="avg_1014_nearl2_1#7$1", focus=2)]
[name="玛嘉烈"]  我们没什么好聊的，要动手的话，随时奉陪。
[Character(name="avg_npc_209_1", name2="avg_1014_nearl2_1#7$1", focus=1)]
[name="罗伊"]  真是咄咄逼人，直说了吧，我们想摆脱商业联合会的控制。
[Character(name="avg_npc_209_1", name2="avg_1014_nearl2_1#4$1", focus=2)]
[name="玛嘉烈"]  ......什么？
[Character(name="avg_npc_209_1", name2="avg_1014_nearl2_1#4$1", focus=1)]
[name="罗伊"]  今天来，我就是想把这话挑明的。我们是对立的立场，毕竟现在我们还是联合会的人......
[name="罗伊"]  但我们是否可以私下签订一份和平协议呢？
[Character(name="avg_npc_209_1", name2="avg_1014_nearl2_1#5$1", focus=2)]
[name="耀骑士"]  ......
[Character(name="avg_npc_209_1", name2="avg_1014_nearl2_1#5$1", focus=1)]
[name="罗伊"]  你，耀骑士，临光家族和那些附庸，以及“罗德岛”。我们希望你们不要影响到我们的计划。
[name="罗伊"]  相对的，无胄盟不会妨碍你的夺冠，更不会对和耀骑士相关的人物出手。
[Character(name="char_179_cgbird_1", name2="avg_npc_209_1", focus=1)]
[name="夜莺"]  ......那些感染者呢？
[Character(name="char_179_cgbird_1", name2="avg_npc_209_1#2", focus=2)]
[name="罗伊"]  ......遗憾，我们也不能做到所有事情。
[Character(name="char_179_cgbird_1", name2="avg_npc_209_1", focus=2)]
[name="罗伊"]  感染者对我们而言也算是个威胁，但是请放心，现在的我们也需要那些感染者骑士——
[Character(name="avg_npc_209_1", name2="avg_1014_nearl2_1#4$1", focus=2)]
[name="玛嘉烈"]  当你们的替罪者？
[Character(name="avg_npc_209_1#2", name2="avg_1014_nearl2_1#4$1", focus=1)]
[name="罗伊"]  ......
[Character(name="avg_npc_209_1#2", name2="avg_1014_nearl2_1#7$1", focus=2)]
[name="玛嘉烈"]  这不是我索求的东西，无胄盟。
[Character(name="avg_npc_209_1#2", name2="avg_1014_nearl2_1#7$1", focus=1)]
[name="罗伊"]  ——无胄盟是什么？
[name="罗伊"]  古时候，为了对抗荒淫无道的骑士贵族，当地的农民和扈从们串通，雇佣了一批身经百战的杀手。
[name="罗伊"]  但是他们——全都失手了。
[name="罗伊"]  骑士把叛徒通通吊死，悬挂在城堡之上，以儆效尤。领地内的村民怒不敢言，只能忍气吞声，放弃抵抗。
[name="罗伊"]  不过后来，有一位弓手主动请缨，当时人们普遍认为弓箭手无法应对库兰塔骑士的速度，并不抱期望......
[name="罗伊"]  然而翌日清晨，那位暴虐骑士的家人们醒来后，却看见那位骑士保持着冲锋的姿势，仰面朝天，被一杆长枪钉在了广场地面——
[name="罗伊"]  等到人们靠近细看，才发现那并不是一杆长枪，而是一支利箭，由玄铁铸造而成的利箭。
[Character(name="avg_npc_209_1", name2="avg_1014_nearl2_1#7$1", focus=1)]
[name="罗伊"]  “玄铁”，是历史上第一位无胄盟。
[Character(name="avg_npc_209_1#6", name2="avg_1014_nearl2_1#7$1", focus=1)]
[name="罗伊"]  虽然我对于我们只是被雇来的杀手这点还是有自觉的，不过呢......
[name="罗伊"]  有些传说，可不是空穴来风。
[stopmusic]
[Character(name="char_147_shining_1", name2="avg_1014_nearl2_1#7$1", focus=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="闪灵"]  ——临光！上面！
[dialog]
[character]
耀骑士抬起头。
路灯暗淡，今夜星光璀璨。
而其中一颗流星，闪烁了数下之后，偏离了群星的轨道。
直坠大地。
[dialog]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_avg_arrowshot")]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[CameraShake(duration=0.6, xstrength=5, ystrength=8, vibrato=30, randomness=90, block=true)]
[playMusic(intro="$normal02_intro", key="$normal02_loop", volume=0.4)]
[Character(name="avg_1014_nearl2_1#4$1")]
[name="玛嘉烈"]  ——箭！？
[Character(name="char_147_shining_1", name2="avg_1014_nearl2_1#4$1", focus=1)]
[name="闪灵"]  斩断它！
[Character(name="char_147_shining_1", name2="avg_1014_nearl2_1#7$1", focus=2)]
[name="玛嘉烈"]  明白——！
[dialog]
[Character(name="char_147_shining_1", name2="avg_1014_nearl2_1#7$1", focus=0)]
[PlaySound(key="$b_char_defboost", volume=0.6)]
[Blocker(a=0.8, r=1, g=1, b=1, fadetime=1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$d_avg_arrow")]
[Background(image="bg_23_G05",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[delay(time=1)]
[Character(name="char_179_cgbird_1")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="夜莺"]  咿呀——！？
[Character(nam

... (全文21121字符)
```

### level_act13side_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔2 6-1
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_23_G05",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Character(name="avg_npc_209_1#5", name2="avg_npc_208_1", focus=1)]
[name="罗伊"]  开始了。感染者的行动。
[Character(name="avg_npc_209_1#5", name2="avg_npc_208_1", focus=2)]
[name="莫妮克"]  ......他们真的会主动撞枪口上来？
[Character(name="avg_npc_209_1", name2="avg_npc_208_1", focus=1)]
[name="罗伊"]  他们最好会。我们把动静闹大一点，董事会抓不住我们的把柄。
[name="罗伊"]  动力炉那边......？
[Character(name="avg_npc_209_1", name2="avg_npc_208_1#4", focus=2)]
[name="莫妮克"]  你是在质疑我？
[Character(name="avg_npc_209_1#4", name2="avg_npc_208_1#4", focus=1)]
[name="罗伊"]  不，不敢。
[Character(name="avg_npc_209_1#4", name2="avg_npc_208_1", focus=2)]
[name="莫妮克"]  可以杀掉野鬃吗？
[Character(name="avg_npc_209_1", name2="avg_npc_208_1", focus=1)]
[name="罗伊"]  ......当然，事已至此。
[name="罗伊"]  有几个猎物的话，饲主也不会大发雷霆了吧。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="left", type="move", xpos=-300, fadetime=2,block=false)]
[character(name="char_empty",name2="avg_npc_208_1",fadetime=0.5)]
[delay(time=2)]
[Character(name="avg_npc_208_1#4")]
[name="莫妮克"]  ......
[name="莫妮克"]  本来，就是从我手底下逃走的猎物......我只是取回我早该得到的东西。
[Character(name="avg_npc_208_1")]
[name="莫妮克"]  通知第三小队，收队，跟我走。
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_23_G05",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_216")]
[name="无胄盟成员"]  发现野鬃！发现——
[dialog]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_496_wdmane_1#8")]
[name="艾沃娜"]  太慢了，无胄盟！
[dialog]
[Character(name="avg_npc_216")]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$fightgeneral", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$fightgeneral", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_npc_216")]
[name="无胄盟成员"]  呃！？
[CameraShake(duration=0.5, xstrength=3, ystrength=3, vibrato=10, randomness=90, fadeout=true, block=false)]
[Character(fadetime=1)]
[PlaySound(key="$bodyfalldown1", volume=0.6)]
[Dialog]
[Delay(time=1)]
[Character(name="avg_496_wdmane_1#9")]
[name="艾沃娜"]  躲在暗处耍阴招，你们已经忘了该怎么对付骑士了吗！？
[Character(name="avg_npc_216")]
[name="无胄盟成员"]  该死的感染者！
[Character(name="avg_496_wdmane_1#8")]
[name="艾沃娜"]  为了杰米，和那些死在你们手里的无辜者！
[dialog]
[Character(name="avg_npc_216")]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$fightgeneral", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_npc_216")]
[name="无胄盟成员"]  咿——
[CameraShake(duration=0.5, xstrength=3, ystrength=3, vibrato=10, randomness=90, fadeout=true, block=false)]
[Character(fadetime=1)]
[PlaySound(key="$bodyfalldown1", volume=0.6)]
[Dialog]
[Delay(time=1)]
[Character(name="avg_npc_221", name2="avg_496_wdmane_1#8", focus=1)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="感染者骑士"]  ——艾沃娜！别忘了索娜说的，不要随意下杀手......至少，在杀他们的时候，做好觉悟。
[Character(name="avg_496_wdmane_1#9")]
[name="艾沃娜"]  ......无胄盟，你杀过多少人？
[Character(name="avg_npc_216")]
[name="无胄盟成员"]  ......哈。
[name="无胄盟成员"]  道貌岸然才能让你们自诩正义吗？小鬼头？我在黄金草原当赏金猎人的时候，可从来没想过这个问题！
[name="无胄盟成员"]  忘了城市之外的地方，卡西米尔人是怎么活着的了吗？很简单的道理！最强大的求生者全是冷酷的混账！
[Character(name="avg_496_wdmane_1#9")]
[name="艾沃娜"]  ——随你怎么说，无胄盟，但现在，是我赢了。
[name="艾沃娜"]  输了，死了，说什么都是徒劳。
[Character(name="avg_npc_216")]
[name="无胄盟成员"]  你——
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[dialog]
[Character(fadetime=1)]
[PlaySound(key="$bodyfalldown1", volume=0.6)]
[Dialog]
[Delay(time=1)]
[Character(name="avg_496_wdmane_1#2")]
[name="艾沃娜"]  ......他刚才应该已经发出了求救信号。
[name="艾沃娜"]  希望能把无胄盟吸引过来，不要干扰到格蕾纳蒂的行动。
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_23_G07",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_430_fartth_1")]
[name="查丝汀娜"]  ......
[dialog]
[PlaySound(key="$d_gen_transmissionget", volume=0.6)]
[delay(time=1)]
[Character(name="avg_430_fartth_1",focus=-1)]
[name="瑟奇亚克"]  远牙，你那边发现无胄盟了吗？
[Character(name="avg_430_fartth_1")]
[name="查丝汀娜"]  没有。
[name="查丝汀娜"]  你那边呢？
[Character(name="avg_430_fartth_1",focus=-1)]
[name="瑟奇亚克"]  格蕾纳蒂已经就位了，只等我们的信号。
[name="瑟奇亚克"]  但是，无胄盟的反应速度不会这么慢......他们真的有被野鬃吸引过去吗？
[Character(name="avg_430_fartth_1")]
[name="查丝汀娜"]  应该......
[Character(name="avg_430_fartth_1#3")]
[name="查丝汀娜"]  ......！
[Character(name="avg_430_fartth_1#6")]
[name="查丝汀娜"]  发现无胄盟小队，他们从四号大街的小巷进入了你的包围网，艾沃娜！
[PlaySound(key="$transmission", volume=0.6)]
[Character(name="avg_430_fartth_1#4")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="查丝汀娜"]  ......艾沃娜？听得见吗？艾沃娜？
[name="查丝汀娜"]  喂！？瑟奇亚克？艾沃娜！？
[Character(name="avg_430_fartth_1#5")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="查丝汀娜"]  ......通讯......被......截断了

... (全文31007字符)
```

### level_act13side_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔2 6-2
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$dignified_intro", key="$dignified_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="四周变暗了。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="格蕾纳蒂成功了吗？索娜是不是已经成功潜入了？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="成功之后，我们，就能顺利生活在卡西米尔了吗？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.5)]
[Character(name="avg_npc_220", name2="avg_496_wdmane_1#9", focus=1)]
[name="杰米"]  别骗自己。
[Character(name="avg_npc_220", name2="avg_496_wdmane_1#6", focus=2)]
[name="艾沃娜"]  ......！
[Character(name="avg_npc_220", name2="avg_496_wdmane_1#6", focus=1)]
[name="杰米"]  想想我们的遭遇。
[name="杰米"]  在地下竞技场和野兽厮杀，和同伴厮杀，每一场比赛留下的都是实打实的伤痛。
[name="杰米"]  主办方要看到更多的鲜血和刺激，假赛，场外的阴谋诡计。
[name="杰米"]  这一切都是因为什么？
[name="杰米"]  再看看那些卡瓦莱利亚基之外的地方吧，感染者有何处可去？
[Character(name="avg_npc_220", name2="avg_496_wdmane_1#9", focus=2)]
[name="艾沃娜"]  ......何处可去。
[Character(name="avg_npc_220", name2="avg_496_wdmane_1#9", focus=1)]
[name="杰米"]  我们身患矿石病，绝症，我们迟早会死，我们的死还会给周围带来灾难。
[name="杰米"]  我们是不祥的，是不可控的，是被排斥的异类。
[name="杰米"]  监正会真的会允许感染者建立正规骑士团吗？
[name="杰米"]  卡西米尔......不，这片大地真的还有感染者存续的空间吗？
[name="杰米"]  就算有......
[name="杰米"]  ......又与你何干呢？
[stopmusic(fadetime=2.5)]
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[Background(image="bg_23_G05",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Character(name="avg_npc_216", name2="avg_npc_216", focus=1)]
[name="无胄盟成员A"]  这家伙，已经一动不动了啊......死了吗？
[Character(name="avg_npc_216", name2="avg_npc_216", focus=2)]
[name="无胄盟成员B"]  但愿吧，我是真的不想和感染者厮杀，要是我也被感染了怎么办......
[name="无胄盟成员B"]  你去确认一下吧，如果真的死了，就让善后小组来处理。
[dialog]
[Character(name="avg_496_wdmane_1#8",blackstart=0.4,blackend=0.9,fadetime=1,block=true)]
[delay(time=1)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="艾沃娜"]  ......咳。
[name="艾沃娜"]  说谁，死了呢？
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="艾沃娜"]  ......来啊！
[name="艾沃娜"]  该死的......无胄盟！我要......打败你们所有人！
[name="艾沃娜"]  残害......感染者的......凶手！
[Character(name="avg_npc_216", name2="avg_npc_216", focus=1)]
[name="无胄盟成员A"]  ......她还有力气动？
[name="无胄盟成员A"]  浑身是血，站都站不稳，何必勉强呢。
[Character(name="avg_496_wdmane_1#8",blackstart=0.4,blackend=0.9)]
[name="艾沃娜"]  来......来！
[name="艾沃娜"]  谁也别......想走......咳！
[CameraShake(duration=0.5, xstrength=3, ystrength=3, vibrato=10, randomness=90, fadeout=true, block=false)]
[Character(fadetime=1)]
[PlaySound(key="$bodyfalldown1", volume=0.6)]
[Dialog]
[Delay(time=1)]
[Character(name="avg_npc_216", name2="avg_npc_216", focus=2)]
[name="无胄盟成员B"]  ......也算挺有骨气的，给她个痛快吧。
[name="无胄盟成员B"]  反正再这样下去，过个几分钟她就要失血而死了，啧啧，莫妮克的手法还真娴熟。
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="如果，我更强的话，更快的话......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="是不是可以......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="逃离这个时代？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="逃？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, b

... (全文23314字符)
```

### level_act13side_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔2 7-1
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="“骑士最后的敌人，是这片大地。”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="“那些本该安分地等待在地上的城市，以人民的血汗为食，竟然开始蠕行前进。”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="“城市是生活的怪物，去号召他们对抗每一座城，去将最纯真的美好归还给他们！”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="“让草原重新成为草原，让天空仍是天空，让人性再次坚定，让荣光永垂不朽！”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="“我即是最后的骑士！”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.5)]
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[Background(image="bg_23_G03",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Character(name="avg_npc_211_1#8", name2="avg_npc_212_1", focus=1)]
[name="发言人马克维茨"]  怎么样了，征战骑士的目的地是哪里？监正院吗？
[Character(name="avg_npc_211_1#8", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  不......
[name="发言人麦基"]  ......他们去了，冠军墙展厅，历代冠军挂像与颁奖之地。
[Character(name="avg_npc_211_1#3", name2="avg_npc_212_1", focus=1)]
[name="发言人马克维茨"]  ......为什么？他们不应该立刻去政府那边吗？
[Character(name="avg_npc_211_1#3", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  董事会正在讨论此事。在我看来，这是监正会试图挽回颜面的一步棋。
[Character(name="avg_npc_211_1#3", name2="avg_npc_212_1#2", focus=2)]
[name="发言人麦基"]  也许下一步......也许下一步，他们会尝试让驻军成为常态。
[Character(name="avg_npc_211_1#5", name2="avg_npc_212_1#2", focus=1)]
[name="发言人马克维茨"]  ......
[Character(name="avg_npc_211_1#5", name2="avg_npc_212_1#5", focus=2)]
[name="发言人麦基"]  但现在的卡西米尔，可不是他们把刀架在别人脖子上就说了算的......愚昧的骑士还没能意识到这一点。
[name="发言人麦基"]  暴力的时代早就过去了。
[Character(name="avg_npc_211_1#5", name2="avg_npc_212_1#5", focus=1)]
[name="发言人马克维茨"]  ......嗯......
[Character(name="avg_npc_211_1#5", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  辛苦你另外走一趟零号地块了，断电对感染者收容治疗中心的影响很大。
[name="发言人麦基"]  去看一看那里有没有出什么岔子。
[Character(name="avg_npc_211_1#8", name2="avg_npc_212_1", focus=1)]
[name="发言人马克维茨"]  好。
[Character(name="avg_npc_211_1#8", name2="avg_npc_223", focus=2)]
[name="企业员工"]  报告，发言人阁下，电力系统......基本恢复了！正在准备重启！
[stopmusic(fadetime=1)]
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Background(image="bg_23_G06",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.4)]
黑暗中的银光一路行过。
嘈杂的观众围绕着这一场奢华的登场。
路灯扑闪，随即，霓虹色彩回到了这座小睡片刻的城市。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_23_G07",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
银枪的天马在广告灯光的簇拥下显得格格不入。
但是，在场的每一个人，凑热闹的路人、慌张的骑士、兴奋的游客......
他们都产生了错觉，他们都认为，是天马带来了光。
是城市在他们的身后，逐步恢复活力。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_23_G02",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_224")]
[name="“银枪的天马”"]  ......见过伊奥莱塔宗师。
[dialog]
[Character(name="avg_npc_210_1",fadetime=1,block=true)]
[delay(time=1)]
[name="伊奥莱塔·罗素"]  许久不见，莱姆。
[name="伊奥莱塔·罗素"]  长途跋涉辛苦了，但可惜，我们似乎没有什么时间休息。
[Character(name="avg_npc_224", name2="avg_npc_210_1", focus=1)]
[name="“银枪的天马”"]  我们不需要休息，为卡西米尔扫清污秽才是当务之急。
[Character(name="avg_npc_224", name2="avg_npc_210_1", focus=2)]
[name="伊奥莱塔·罗素"]  呵呵......你还是老样子，这么性急。
[name="伊奥莱塔·罗素"]  想去见一见这场宴会的主角吗？
[Character(name="avg_npc_224", name2="avg_npc_210_1", focus=1)]
[name="“银枪的天马”"]  ......玛嘉烈·临光？
[name="“银枪的天马”"]  当年她就不应该拒绝宗师的邀请，她本会是我们中最优秀的一批，而不用沦落至此。
[name="“银枪的天马”"]  可是，她再次回到卡西米尔，却重新站上了那种虚伪的擂台......莫非流放让玛嘉烈改变了想法？
[Character(name="avg_npc_224", name2="avg_npc_210_1#5", focus=2)]
[name="伊奥莱塔·罗素"]  你也是和玛嘉烈决斗过的，你觉得她是那样的孩子吗？
[Character(name="avg_npc_224", name2="avg_npc_210_1#5", focus=1)]
[name="“银枪的天马”"]  唔......但时间能改变一切，玛嘉烈如今......
[Character(name="avg_npc_224", name2="avg_npc_210_1#5", focus=2)]
[name="伊奥莱塔·罗素"]  看看这面墙，莱姆，特锦赛的历代冠军们。
[name="伊奥莱塔·罗素"]  为什么从这个逐渐崩溃的时代中脱颖而出的骑士，他们依旧能蕴含光芒？
[Character(name="avg_npc_224", name2="avg_npc_210_1#5", focus=1)]
[name="“银枪的天马”"]  ......只出现一两位优秀的骑士，并不能说明什么，宗师。
[name="“银枪的天马”"]  骑士竞技依旧只是纯粹的亵渎，是卡西米尔的祸根。
[name="“银枪的天马”"]  每一次回到大骑士领，我都更加悲哀愤懑，我们的人民正在丧失敬畏，高尚的品德反倒成了迂腐的笑话。
[Character(name="avg_npc_224", name2="avg_npc_210_1#2", focus=2)]
[name="伊奥莱塔·罗素"]  ......也许吧，自从征战骑士离开大骑士领后，就一直如此。
[name="伊奥莱塔·罗素"]  可惜时代在年轻人手上，我们得出的答案，已经无关紧要了。
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_23_G09",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="char_147_shining_1", fadetime=1,block=true)]
[delay(time=1)]
[name="闪灵"]  ......原来博士你已经察觉到了。
[name="闪灵"]  不愧是你。
[dialog]
[Decision(options="我们不能在卡西米尔的中心做得太过火。;阿米娅和各位干员的安全才是第一考量。;我想各位都不会同意我们轻举妄动。

... (全文32455字符)
```

### level_act13side_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔2 7-2
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_23_G10",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Character(name="avg_npc_122")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="索娜"]  ......小灰！
[Character(name="avg_npc_123#7", name2="avg_npc_122", focus=1)]
[name="格蕾纳蒂"]  ......索娜，你没事！太好了！
[Character(name="avg_npc_123#7", name2="avg_npc_122", focus=2)]
[name="索娜"]  你骗过了罗伊？不错的演技嘛，怎么做到的？
[Character(name="avg_npc_123#4", name2="avg_npc_122", focus=1)]
[name="格蕾纳蒂"]  ......只是想象了一下我如果真的失去你，会是什么感受。
[Character(name="avg_npc_123#4", name2="avg_npc_122#4", focus=2)]
[name="索娜"]  哇哦，体验派......
[Character(name="avg_npc_123#4", name2="avg_npc_122", focus=2)]
[name="索娜"]  其他人呢？
[Character(name="avg_npc_123#2", name2="avg_npc_122", focus=1)]
[name="格蕾纳蒂"]  ......艾沃娜受伤很重......但好在没有大碍。
[Character(name="avg_npc_123#2", name2="avg_npc_122#2", focus=2)]
[name="索娜"]  ......艾沃娜她......
[Character(name="avg_4000_jnight_1#2")]
[name="“正义骑士号”"]  （低沉的滴滴声）
[Character(name="avg_npc_123#3", name2="avg_npc_122#2", focus=1)]
[name="格蕾纳蒂"]  她是我们中最像个战士的......她站到了最后。
[Character(name="avg_npc_123", name2="avg_npc_122#2", focus=1)]
[name="格蕾纳蒂"]  查丝汀娜和塑料骑士去对付白金大位了......我们得去帮他们！
[dialog]
[Character(name="avg_npc_103nc_1#2",fadetime=1,block=true)]
[delay(time=1)]
[name="塑料骑士"]  ......不必了，白金已经撤退了。
[Character(name="avg_npc_103nc_1")]
[name="塑料骑士"]  我们还没有沦落到两个人都打不退她的地步，她没那么强。
[Character(name="avg_npc_123", name2="avg_npc_103nc_1", focus=1)]
[name="格蕾纳蒂"]  ......查丝汀娜呢？
[Character(name="avg_npc_123", name2="avg_npc_103nc_1#2", focus=2)]
[name="塑料骑士"]  ......
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_23_G03",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_222", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  今天的赛事必须正常进行，没问题吧。
[Character(name="avg_npc_222", name2="avg_npc_212_1", focus=1)]
[name="企业员工"]  我们已经确认好特锦赛赛场万无一失。
[Character(name="avg_npc_222", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  好。安抚观众的情绪，今晚的比赛必须完美无缺。
[name="发言人麦基"]  记住，不光是观众......经历了之前的骚动后，几位常务董事也对今晚的比赛分外关注。
[Character(name="avg_npc_222", name2="avg_npc_212_1#2", focus=2)]
[name="发言人麦基"]  表现好的话，我们都会得到嘉奖，否则......
[Character(name="avg_npc_222", name2="avg_npc_212_1#2", focus=1)]
[name="企业员工"]  明白！
[Character(name="avg_npc_212_1")]
[name="发言人麦基"]  唉，辛苦你了，莫布。
[Character(name="avg_npc_121#2", name2="avg_npc_212_1", focus=1)]
[name="大嘴莫布"]  不！能负责今晚的解说，是我的荣幸——
[Character(name="avg_npc_121#2", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  不用说你应该也知道，就当昨晚的事情没发生过。
[name="发言人麦基"]  今晚的四场比赛里，最受关注的，无疑是耀骑士和逐魇骑士的对决。
[Character(name="avg_npc_121#2", name2="avg_npc_212_1#4", focus=2)]
[name="发言人麦基"]  但是......在感染者引发了这种规模的异常事件后，董事会不太希望耀骑士继续获胜了。
[Character(name="avg_npc_121#2", name2="avg_npc_212_1#4", focus=1)]
[name="大嘴莫布"]  ......是想让裁判席吹黑哨吗？
[Character(name="avg_npc_121#2", name2="avg_npc_212_1#2", focus=2)]
[name="发言人麦基"]  这一点，我们会根据赛况自行判断，但是，你需要在裁判席作出判决后，向观众“传达”其合理性。
[Character(name="avg_npc_121#2", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  血骑士那边，已经有人去赤盏骑士团做思想工作，应该很快就能得出结论。
[name="发言人麦基"]  而这一边......耀骑士和逐魇骑士......只是两个疯子罢了。
[Character(name="avg_npc_121#2", name2="avg_npc_212_1", focus=1)]
[name="大嘴莫布"]  明白！我这就去做赛前准备！
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[characteraction(name="left", type="move", xpos=-300, fadetime=2,block=false)]
[character(name="char_empty",name2="avg_npc_212_1",fadetime=0.5)]
[delay(time=2)]
[Character(name="avg_npc_212_1#5")]
[name="发言人麦基"]  ......
[Character(name="avg_npc_211_1#4", name2="avg_npc_212_1#5", focus=1)]
[name="发言人马克维茨"]  怎么了？你的脸色很苍白。
[Character(name="avg_npc_211_1#4", name2="avg_npc_212_1#2", focus=2)]
[name="发言人麦基"]  ......玄铁在大停电之后就消失了。三个人，都消失了。
[Character(name="avg_npc_211_1#4", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  虽然秘而不发，但是有数位联合会高管在大停电期间遭到了刺杀......
[name="发言人麦基"]  现场很仓促，线索指向了感染者，但是......我不这么认为，感染者有这么大能耐吗？
[Character(name="avg_npc_211_1#4", name2="avg_npc_212_1#4", focus=2)]
[name="发言人麦基"]  现在，有一件很恐怖的事情在悄然发生。
[Character(name="avg_npc_211_1#3", name2="avg_npc_212_1#4", focus=1)]
[name="发言人马克维茨"]  难道说......？
[Character(name="avg_npc_211_1#3", name2="avg_npc_212_1#3", focus=2)]
[name="发言人麦基"]  ......是的。
[Character(name="avg_npc_211_1#3", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  无胄盟背叛了。
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_kxstreet",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_225", name2="avg_npc_120", focus=1)]
[name="逐魇骑士"]  ......巴特巴雅尔，你平时无事可做吗？
[Character(name="avg_npc_225", name2="avg_npc_120#2", focus=2)]
[name="老骑士"]  你问我这话吗！？
[Character(name="avg_npc_225", name2="avg_npc_120#3", focus=2)]
[name="老骑士"]  ......你啊，是进入了特锦赛的骑士吧？没有训练场地，甚至都无家可归，每天就在大骑士领当流浪汉吗！？
[Character(name="avg_npc_225", name2="avg_npc_120#3", focus=1)]
[name="逐魇骑士"]  ......当一个猎人，在森林里迷失方向的时候，他会自行生活，搭建木棚。
[Character(name="avg_npc_225", name2="avg_npc_120", focus=2)]
[name="老骑士"]  你可是在一座大地上屈指可数的大城市里......
[Character(name="avg_npc_225", name2="avg_npc_120", focus=1)]
[CameraShake(duration=0.8, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="逐魇骑士"]  ——城市！
[delay(time=0.5)]
[dialog]
[Character(name="avg_npc_225", name2="avg_npc_120#3", focus=-1)]
异样的咆哮声令老骑士一时无言。
周遭的目光聚集在两人身上，仿佛他们才是森林里的野兽。
[dialog]
[Character(name="avg_npc_225", name2="avg_npc_120#3", focus=1)]
[name="逐魇骑士"]  城市......是懦弱的象征。
[name="逐魇骑士"]  被称作文明的东西在征服蛮荒之后，建立起了自己的高楼。
[name="逐魇骑士"]  在这座高楼里，不再需要人性做门票。
[Character(name="avg_npc_225", name2="avg_npc_120#3", focus=2)]
[name="老骑士"]  ......你在说什么？
[Character(name="avg_npc_225", name2="avg_npc_120#3", focus=1)]
[name="逐魇骑士"]  ......卡瓦莱利亚基有值得一

... (全文36547字符)
```

### level_act13side_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔2 8-1
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_23_G10",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[PlaySound(key="$radio")]
[name="广播里的声音"]  突然出现的冠军，以雷霆之势阻止一触即发的二人！
[name="广播里的声音"]  昨晚的比赛由于逐魇骑士的法术涉嫌违规而遭到终止，而阻止了事态进一步恶化的人，正是“英雄”血骑士！
[name="广播里的声音"]  而逐魇骑士与耀骑士也以平手告终，逐魇骑士接下来将直接与因对手投降而轮空的血骑士交战——
[Character(name="avg_npc_123#5")]
[name="格蕾纳蒂"]  平手......？逐魇犯规，难道不该让耀骑士晋级吗？
[Character(name="avg_npc_123#5", name2="avg_npc_122#2", focus=2)]
[name="索娜"]  ......他们不希望感染者顺利晋级，当然。
[Character(name="avg_npc_122#5")]
[name="索娜"]  瑟奇亚克人呢？
[Character(name="avg_430_fartth_1", name2="avg_npc_122#5", focus=1)]
[name="查丝汀娜"]  他刚和家人见面，给他一点时间。
[Character(name="avg_npc_123#3", name2="avg_npc_122#5", focus=1)]
[name="格蕾纳蒂"]  ......说真的，我对他本来没什么好感。
[Character(name="avg_npc_123#3", name2="avg_npc_122", focus=2)]
[name="索娜"]  都看得出来。
[Character(name="avg_npc_123#3", name2="avg_430_fartth_1", focus=2)]
[name="查丝汀娜"]  确实，原来你没打算表现得那么露骨？
[Character(name="avg_npc_123#6", name2="avg_430_fartth_1", focus=1)]
[name="格蕾纳蒂"]  ......
[Character(name="avg_npc_122")]
[name="索娜"]  但他也是个有血有肉的人，对吧？
[name="索娜"]  这座城市经常让我们忘了这点......我们都是活着的人。
[name="索娜"]  我们应该有自己的选择，有自己的生活，而不是......在无尽的浪潮中，迷失自我。
[dialog]
[PlaySound(key="$radio")]
[character]
[name="广播里的声音"]  血骑士与逐魇骑士的旷世之战，将在明晚打响！
[name="广播里的声音"]  请各位观众，锁定骑士之夜频道，明晚八点，为您带来绝佳的观战体验！
[dialog]
[Character(name="avg_496_wdmane_1",fadetime=1,block=true)]
[delay(time=2)]
[Character(name="avg_496_wdmane_1", name2="avg_4000_jnight_1#4", focus=2)]
[delay(time=0.5)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="“正义骑士号”"]  （响亮的滴滴声）
[Character(name="avg_496_wdmane_1", name2="avg_4000_jnight_1#4", focus=1)]
[name="艾沃娜"]  哈......正义号！你没事！
[Character(name="avg_npc_122#6", name2="avg_496_wdmane_1", focus=1)]
[name="索娜"]  艾沃娜！你还不能随便下床......
[Character(name="avg_npc_123#2", name2="avg_496_wdmane_1", focus=1)]
[name="格蕾纳蒂"]  来，扶着我。
[Character(name="avg_npc_123", name2="avg_496_wdmane_1#4", focus=2)]
[name="艾沃娜"]  嘿......谢啦，小灰。
[Character(name="avg_npc_122#5", name2="avg_496_wdmane_1#4", focus=1)]
[name="索娜"]  小灰是我独享的绰号吧？
[Character(name="avg_npc_122#5", name2="avg_496_wdmane_1", focus=2)]
[name="艾沃娜"]  哈哈，借来一用......
[Character(name="avg_npc_122", name2="avg_496_wdmane_1", focus=1)]
[name="索娜"]  要付版权费的喔。
[Character(name="avg_npc_122#2", name2="avg_496_wdmane_1", focus=1)]
[name="索娜"]  ......艾沃娜，那天......
[Character(name="avg_npc_122#2", name2="avg_496_wdmane_1#9", focus=2)]
[name="艾沃娜"]  是，我看到了血骑士的影子。
[Character(name="avg_430_fartth_1", name2="avg_496_wdmane_1#9", focus=1)]
[name="查丝汀娜"]  ......现场有鲜血法术的痕迹。
[Character(name="avg_430_fartth_1#2", name2="avg_496_wdmane_1#9", focus=1)]
[name="查丝汀娜"]  那是种......很糟糕的法术。现在，单纯的施法都会让我感到疼痛，难以想象操纵那种法术，血骑士要遭受多大的痛苦。
[Character(name="avg_430_fartth_1#2", name2="avg_496_wdmane_1#9", focus=2)]
[name="艾沃娜"]  ......血骑士......他很强。
[Character(name="avg_npc_122#2", name2="avg_496_wdmane_1#9", focus=1)]
[name="索娜"]  我们都知道。
[name="索娜"]  有血骑士，才有了感染者骑士的参赛机制。
[Character(name="avg_npc_123", name2="avg_npc_122#2", focus=1)]
[name="格蕾纳蒂"]  ......成为联合会的玩物......失去尊严和自由......但是，我们活着。
[Character(name="avg_npc_123", name2="avg_496_wdmane_1#10", focus=2)]
[name="艾沃娜"]  活着才有机会奔跑。
[Character(name="avg_430_fartth_1", name2="avg_496_wdmane_1#10", focus=1)]
[name="查丝汀娜"]  ......耀骑士和血骑士，你们更支持哪一方？
[Character(name="avg_430_fartth_1", name2="avg_496_wdmane_1", focus=2)]
[name="艾沃娜"]  ......血骑士。毫无疑问，他才是真正为感染者开辟了未来的人。
[Character(name="avg_npc_123#3", name2="avg_430_fartth_1", focus=1)]
[name="格蕾纳蒂"]  但我们需要的是不懈的斗争，而不是安于现状......我选择耀骑士。
[Character(name="avg_npc_123", name2="avg_430_fartth_1", focus=1)]
[name="格蕾纳蒂"]  你呢？
[Character(name="avg_npc_123", name2="avg_430_fartth_1#2", focus=2)]
[name="查丝汀娜"]  ......我选索娜。
[Character(name="avg_430_fartth_1#2", name2="avg_496_wdmane_1#6", focus=2)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="艾沃娜"]  还能这样啊！？
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_23_G03",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="char_204na_platnm_1",fadetime=1,block=true)]
[delay(time=1)]
[name="白金"]  ......您找我？
[Character(name="avg_npc_211_1#5")]
[name="发言人马克维茨"]  ......
[Character(name="char_204na_platnm_1", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  ......董事会已经决定......对零号地块实施清理。
[name="发言人麦基"]  现阶段的感染者策略是错误的。
[Character(name="char_204na_platnm_1#3", name2="avg_npc_212_1", focus=1)]
[name="白金"]  错误呢......
[Character(name="char_204na_platnm_1#3", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  而且，罗德岛的领导人对零号地块的调查有些深入了。这也是无胄盟的失误。
[Character(name="char_204na_platnm_1#3", name2="avg_npc_212_1", focus=1)]
[name="白金"]  ......
[Character(name="char_204na_platnm_1#3", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  几位常务董事强烈要求无胄盟斩草除根。不能让罗德岛的医疗小队安然离开卡西米尔。
[name="发言人麦基"]  没问题吧？
[Character(name="avg_npc_211_1#5")]
[name="发言人马克维茨"]  ......
[Character(name="char_204na_platnm_1", name2="avg_npc_212_1", focus=1)]
[name="白金"]  ......我明白了。但是，不是董事会全体的命令，而是“几位常务董事”？
[Character(name="char_204na_platnm_1", name2="avg_npc_212_1#2", focus=2)]
[name="发言人麦基"]  ......这你不需要过问。你的指挥权在我们手上。
[Character(name="char_204na_platnm_1#6", name2="avg_npc_212_1#2", focus=1)]
[name="白金"]  准确来说，是在那边那位马克维茨先生的手里。
[Character(name="avg_npc_211_1#5", name2="avg_npc_212_1#4", focus=2)]
[name="发言人麦基"]  马克维茨......你知道该怎么办。
[Character(name="avg_npc_211_1#5")]
[name="发言人马克维茨"]  ......
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_courtyard",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_064_weapon_1#6", name2="avg_1014_nearl2_1#1$1", focus=1)]
[n

... (全文22666字符)
```

### level_act13side_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔2 8-2
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_23_G05",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$tense_intro", key="$tense_loop", volume=0.4)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.4, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_npc_061#6")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="玛莉娅"]  呀！
[Character(name="avg_npc_061#6",name2="avg_npc_120#2",focus=2)]
[characteraction(name="right", type="move", xpos=-190, fadetime=0.8, block=true)]
[name="老骑士"]  孩子！
[name="老骑士"]  别勉强自己了——
[Character(name="avg_npc_061#6",name2="avg_npc_120#2",focus=1)]
[name="玛莉娅"]  ......不，弗格瓦尔德师傅......你的手也......
[Character(name="avg_npc_061#6",name2="avg_npc_120#2",focus=2)]
[characteraction(name="right", type="move", xpos=190, fadetime=1.5, block=true)]
[Character(name="avg_npc_061#6",name2="avg_npc_120#3",focus=2)]
[name="老骑士"]  也不是第一次了，习惯了。
[dialog]
[Character(name="avg_npc_225",fadetime=1,block=true)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[delay(time=1)]
[name="逐魇骑士"]  ......胜负已分。你们的实力已在意料之外，勉强能平息我的怒意......
[name="逐魇骑士"]  看在末裔的份上，我不会取你性命。但现在，从我的道路上滚开。
[Character(name="avg_npc_120#2")]
[name="老骑士"]  ......你是铁了心要和玛嘉烈私斗了，哈？
[Character(name="avg_npc_225")]
[name="逐魇骑士"]  ......错了，只是继续一场被中断的决斗。
[Character(name="avg_npc_120#3")]
[name="老骑士"]  图什么？
[name="老骑士"]  你这么偏执，这么......疯狂，你到底为了寻找什么？你想要得到什么？
[Character(name="avg_npc_225")]
[name="逐魇骑士"]  你不明白......
[Character(name="avg_npc_120#3")]
[name="老骑士"]  鬼明白。为了那个所谓的传统，你放弃了生活和眼前的一切！你做的事都毫无意义！
[Character(name="avg_npc_225")]
[name="逐魇骑士"]  我生命的意义，需要你来赋予吗？
[Character(name="avg_npc_120#3")]
[name="老骑士"]  我只是不想看着你这样疯狂下去，“天途”只是极少数部族的成年礼传统吧，那你也只是个孩子！
[Character(name="avg_npc_225")]
[name="逐魇骑士"]  ......！少废话，让开。
[Character(name="avg_npc_120#2")]
[name="老骑士"]  那就把我打趴下再说吧。
[Character(name="avg_npc_225")]
[name="逐魇骑士"]  ——别后悔，老家伙！
[dialog]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_npc_120#2")]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_npc_061#5")]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$swordtsing5", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_npc_225")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="逐魇骑士"]  ——！
[delay(time=0.5)]
[Character(name="avg_npc_061#5",name2="avg_npc_120#2",focus=2)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="老骑士"]  玛莉娅，你做什么！你本来就受伤——
[Character(name="avg_npc_061#5")]
[name="玛莉娅"]  ......这还是，第一次看见你有这么大情绪波动啊，梦魇。
[Character(name="avg_npc_225")]
[name="逐魇骑士"]  ......
[Character(name="avg_npc_061#5")]
[name="玛莉娅"]  骑士的盾，应当保护他人，这是姐姐告诉我的。
[Character(name="avg_npc_061#4")]
[name="玛莉娅"]  ......你说我的信念是借来的，我无话可说。
[Character(name="avg_npc_061#5")]
[name="玛莉娅"]  可如果行那些被照亮的道路也算怯懦，那骑士就根本毫无意义！
[Character(name="avg_npc_225")]
[name="逐魇骑士"]  你妄言骑士——
[Character(name="avg_npc_061#5")]
[name="玛莉娅"]  ——不好意思，我现在根本不是骑士，我只单纯地想保护姐姐——
[name="玛莉娅"]  不想让你这种说不通道理的疯子阻碍姐姐的道路！
[dialog]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.3, block=true)]
[PlaySound(key="$b_char_defboost", volume=0.6)]
[Blocker(a=0, fadetime=1.5, block=false)]
[character]
[delay(time=1)]
[Character(name="avg_npc_225")]
[name="逐魇骑士"]  ......法术？这又算得了......嗯？
[dialog]
[Character(name="avg_npc_061#5")]
玛莉娅脸上的血液被光芒照亮。
脆弱，微小，是的，如果全力以赴，梦魇有十足的把握杀死这匹天马。
他十分确信。
但为何......此刻少女脸颊上的鲜血，如同黄金？
[dialog]
[character]
[Character(name="avg_npc_225")]
[name="逐魇骑士"]  ......法术的光芒让血液看上去好像变成了金色？
[name="逐魇骑士"]  可已经值得被载入史册的天马，又怎么会是这么弱小的......偶然吗。
[Character(name="avg_npc_061#5",name2="avg_npc_120#3",focus=1)]
[name="玛莉娅"]  弗格瓦尔德师傅，你先回去......这里有我。
[Character(name="avg_npc_061#5",name2="avg_npc_120#2",focus=2)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="老骑士"]  别逞强了，他真的会杀了你的——！
[Character(name="avg_npc_061#5",name2="avg_npc_120#2",focus=1)]
[name="玛莉娅"]  没关系。
[name="玛莉娅"]  我会挡住他！
[Character(name="avg_npc_225")]
[name="逐魇骑士"]  ......
[delay(time=0.5)]
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.9)]
[Character(fadetime=1,block=true)]
[Delay(time=2)]
[Character(name="avg_npc_061#5")]
[name="玛莉娅"]  ......呃？你转身是什么意思......
[Character(name="avg_npc_225")]
[name="逐魇骑士"]  ......天马。
[name="逐魇骑士"]  你只靠他人信念，是无法强大的，除非你真正坚信那个信念。
[name="逐魇骑士"]  但你，并不相信。
[Character(name="avg_npc_061#7")]
[name="玛莉娅"]  ......
[Character(name="avg_npc_225")]
[name="逐魇骑士"]  奉献，牺牲。
[name="逐魇骑士"]  你先天地......有着这种近乎自毁的美德。不失为给我的一次教训，天马，末裔。
[name="逐魇骑士"]  也许......
[name="逐魇骑士"]  ......不，没什么。
[name="逐魇骑士"]

... (全文24605字符)
```

### level_act13side_09_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔2-9-1
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_23_G09",screenadapt="coverall")]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[character(name="avg_237_gravel_1",fadetime=1)]
[delay(time=1)]
[name="砾"]  ......好消息，博士。
[name="砾"]  监正会同意罗德岛各位的外出申请了，“让重要的合作伙伴游览城市也是必要的”。
[name="砾"]  本来，如果没有这一系列事件发生的话，您可以在大骑士领更自由一些的。
[dialog]
[character]
[PlaySound(key="$dooropenquite", volume=0.6)]
[delay(time=1)]
[playsound(key="$d_gen_walk_n")]
[character(name="char_002_amiya_1",name2="char_120_hibisc_1", fadetime=1.5)]
[delay(time=2)]
[character(name="char_002_amiya_1#6",name2="char_120_hibisc_1", focus=1)]
[name="阿米娅"]  博士？您找我们吗？
[character(name="char_002_amiya_1#6",name2="char_120_hibisc_1", focus=2)]
[name="芙蓉"]  啊！骑士姐姐！正好我还有剩下的健康餐，你打包带回家吗？
[character(name="avg_237_gravel_1#5")]
[name="砾"]  ......
[Character(name="char_179_cgbird_1")]
[name="夜莺"]  ......您好，砾小姐，博士。
[Dialog]
[Decision(options="难得有机会去卡西米尔的其他地方参观。;想不想出去逛逛？;休——假——时——间——", values="1;2;3")]
[Predicate(references="1;2;3")]
[stopmusic(fadetime=1)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Background(image="bg_23_G01",screenadapt="coverall")]
[playMusic(intro="$m_bat_game02_intro", key="$m_bat_game02_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[character(name="avg_npc_121",fadetime=1.5)]
[delay(time=1.5)]
[name="大嘴莫布"]  激烈的战斗！让人不敢相信自己的眼睛！
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=80, fadeout=true, block=false)]
[name="大嘴莫布"]  不对！应该说，一位名不见经传的梦魇！首次闯入特锦赛，竟然就能与冠军分庭抗礼！
[name="大嘴莫布"]  鲜红的铠甲在赛场上碰撞，让今夜的月光也黯然失色！
[character(name="avg_npc_121#3")]
[name="大嘴莫布"]  不用说，我想观众也感受到了，拓拉！“草原之恐”逐魇骑士！他那疯狂的意志令人为之着迷沉醉！
[name="大嘴莫布"]  经历了与耀骑士的那场决斗之后，人气居高不下的逐魇骑士！究竟能不能为他成为大骑士的故事中，再添一笔！？
[name="大嘴莫布"]  顺带一提，古代人娱乐公司正在举行“骑士封号有奖竞猜”！凡是能猜中骑士封号的观众，都能获得精美礼品一份！
[dialog]
[character]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=0.1, block=false)]
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$sheildimpact",volume=1)] 
[Blocker(a=0, fadetime=0.1, block=false)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=0.1, block=false)]
[CameraShake(duration=0.4, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[delay(time=1)]
[character(name="avg_npc_214_1#2$1",fadetime=1)]
[delay(time=1)]
[name="血骑士"]  你的气势哪里去了？梦魇？
[character(name="avg_npc_225")]
[name="逐魇骑士"]  ......唔。
[name="逐魇骑士"]  米诺斯人......在我的同胞鞭笞往日的时代，你们的英雄已经沦为了诗人口中的典故......
[Dialog]
[Character(name="avg_npc_225", name2="char_empty")]
[characteraction(name="right", type="move", xpos=200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="right", type="move", xpos=-300, power=5, fadetime=0.3, block=false)]
[characteraction(name="left", type="jump", xpos=100, power=5, fadetime=0.3, block=false)]
[Character(name="avg_npc_225", name2="avg_npc_214_1#2$1",fadetime=0.51)]
[delay(time=0.51)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.1, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$sheildimpact",volume=1)] 
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.1, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[CameraShake(xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=2)]
[Dialog]
[Character(name="avg_npc_225", name2="avg_npc_214_1#2$1",focus=2)]
[name="血骑士"]  废话啰嗦。
[name="血骑士"]  那你的可汗如今在哪儿？你那些引以为豪的同胞活在大地何处？
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[PlaySound(key="$sheildimpact",volume=1)] 
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[characteraction(name="right", type="jump", xpos=100, power=5, fadetime=0.5,block=true)]
[characteraction(name="left", type="jump", xpos=-100, power=5, fadetime=0.5,block=true)]
[dialog]
[delay(time=1)]
[character(name="avg_npc_225")]
[name="逐魇骑士"]  ......
[character(name="avg_npc_214_1#2$1")]
[name="血骑士"]  一个活在过去的梦魇，一个可怜人罢了。
[character(name="avg_npc_225")]
[name="逐魇骑士"]  ......米诺斯人，感染者，你为什么而战？
[character(name="avg_npc_214_1#2$1")]
[name="血骑士"]  生存。
[name="血骑士"]  他们把我奉为感染者的英雄......把我当做历史的标杆，但我的初衷，仅仅是活着。
[character(name="avg_npc_225")]
[name="逐魇骑士"]  ......感染者的英雄？
[name="逐魇骑士"]  原来如此......你也在为你的同胞而战吗？
[character(name="avg_npc_214_1#2$1")]
[name="血骑士"]  同胞......？不，我们并无血缘，也没有相同的故乡，我们只是不幸患上了同一种疾病而已。
[name="血骑士"]  他们的遭遇令我感到悲悯，所以我去拯救他们，为所有人寻觅出路。
[character(name="avg_npc_225")]
[name="逐魇骑士"]  不是同胞......你却还要，拯救他们。
[name="逐魇骑士"]  ......可笑。
[name="逐魇骑士"]  你的确强大......但是，卡西米尔的草原难道已经被感染者和异国人瓜分了吗？
[name="逐魇骑士"]  卡西米尔人，库兰塔，他们在哪儿！？
[name="逐魇骑士"]  难道我千里迢迢来到骑士之国，是为了和感染者、米诺斯人和自己的同族决斗的吗！？
[name="逐魇骑士"]  ——奇耻大辱！
[dialog]
[Character]
[Character(name="avg_npc_225", name2="avg_npc_214_1#2$1",fa

... (全文35032字符)
```

### level_act13side_09_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔2-9-2
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_23_G10",screenadapt="coverall")]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[name="新闻里的声音"]  血骑士成功闯入决赛，成为卡西米尔特锦赛历史上第二位有望连任冠军的大骑士。
[name="新闻里的声音"]  不过，血骑士的感染者身份依旧带来了许多非议。联合会发言人表示，“不会因为血骑士的感染者身份而区别对待”——
[name="新闻里的声音"]  但部分骑士家族并不认可这一说法，断电事件与大隔断再演给民众带来的压力不可估量，下面有请骑士协会负责人发言——
[dialog]
[Character(name="avg_npc_123", name2="avg_496_wdmane_1#5", fadetime=1.5)]
[delay(time=2)]
[Character(name="avg_npc_123", name2="avg_496_wdmane_1#5", focus=2)]
[name="艾沃娜"]  ......狄开俄波利斯！血骑士！
[Character(name="avg_npc_123", name2="avg_496_wdmane_1", focus=2)]
[name="艾沃娜"]  哈哈！我就说，这才是感染者骑士该有的样子！
[Character(name="avg_npc_123#2", name2="avg_496_wdmane_1", focus=1)]
[name="格蕾纳蒂"]  ......如果耀骑士赢了风骑士，那么......
[Character(name="avg_430_fartth_1#7")]
[name="查丝汀娜"]  ......两个感染者。
[name="查丝汀娜"]  本届特锦赛冠军，会在，两个感染者之中决出......
[Character(name="avg_npc_123#2", name2="avg_496_wdmane_1", focus=2)]
[name="艾沃娜"]  哈哈！这不是一件好事吗！
[name="艾沃娜"]  我们让那群家伙知道，他们引以为豪的城市并不是无懈可击的，然后，血骑士和耀骑士会揭开他们的遮羞布——
[CameraShake(duration=0.3, xstrength=20, ystrength=20, vibrato=20, randomness=80, fadeout=true, block=false)]
[name="艾沃娜"]  感染者大获全胜！
[Character(name="avg_npc_123#2", name2="avg_496_wdmane_1", focus=1)]
[name="格蕾纳蒂"]  ......真有这么简单就好了。
[Character(name="avg_npc_123#3", name2="avg_496_wdmane_1", focus=1)]
[name="格蕾纳蒂"]  于是，我们呢，接下来怎么办？
[dialog]
[character]
[playsound(key="$d_gen_walk_n")]
[Character(name="avg_npc_122#3", fadetime=1.5)]
[delay(time=1)]
[name="索娜"]  ......啊哈哈......反正大骑士领是待不下去了嘛。
[Character(name="avg_npc_122")]
[name="索娜"]  但是我们可以得到一些合法证明，然后找个村子，找个地方，安安稳稳地过日子。
[character(name="avg_npc_123")]
[name="格蕾纳蒂"]  ......这和我们一开始想的不一样。
[Character(name="avg_496_wdmane_1#9")]
[name="艾沃娜"]  还没到解甲归田的时候呢，索娜！
[name="艾沃娜"]  我们不是为了让更多感染矿石病的人能被合理对待吗！
[name="艾沃娜"]  把商业联合会在零号地块的所作所为告知监正会，不是为了救下更多的感染者吗！？
[name="艾沃娜"]  还没到离开的时候！
[Character(name="avg_430_fartth_1")]
[name="查丝汀娜"]  ......
[character(name="avg_npc_123#2")]
[name="格蕾纳蒂"]  ......我很难反驳，索娜。
[name="格蕾纳蒂"]  我们现在离开，就像是半途而废一样。
[Character(name="avg_npc_122#2")]
[name="索娜"]  ......
[Character(name="avg_496_wdmane_1#5")]
[name="艾沃娜"]  索娜？
[Character(name="avg_npc_122#6")]
[name="索娜"]  ......为什么大部分感染者会被抛弃？
[Character(name="avg_npc_122#7")]
[name="索娜"]  不，这个问题不大对，我想想啊......为什么，感染者总是些......不被重视的人？
[character(name="avg_npc_123#2")]
[name="格蕾纳蒂"]  暴露在高危环境中的工人，没法有效躲避天灾的农民，城市之外无家可归的流浪者，这些人，是最容易染上矿石病的。
[Character(name="avg_430_fartth_1#6")]
[name="查丝汀娜"]  ......被精加工后的宝石制品。
[name="查丝汀娜"]  也许是富有的骑士贵族和社会上层，这辈子唯一见过的源石吧。
[name="查丝汀娜"]  他们当然和矿石病无缘。
[character(name="avg_npc_123#5")]
[name="格蕾纳蒂"]  ......为什么问这个？
[Character(name="avg_npc_122#2")]
[name="索娜"]  ......没什么。
[Character(name="avg_npc_122#6")]
[name="索娜"]  瑟奇亚克和我们一起走吗？
[dialog]
[Character]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_npc_103nc_1#3",fadetime=1.5)]
[delay(time=1.5)]
[name="瑟奇亚克"]  ......你在说什么蠢话。
[Character(name="avg_npc_122#5")]
[name="索娜"]  啊，原来你在啊。
[Character(name="avg_430_fartth_1")]
[name="查丝汀娜"]  你的妻子和孩子还好吗？
[character(name="avg_npc_103nc_1#2")]
[name="瑟奇亚克"]  嗯，所以我是来道谢的，只要能救出他们，怎么样都好。
[character(name="avg_npc_103nc_1#3")]
[name="瑟奇亚克"]  不过，我可不是感染者。明面上，我甚至还保留有合法的骑士身份。
[name="瑟奇亚克"]  我不打算待在大骑士领，我会用前些年积累下来的财富购置一处地产，换一座城市生活吧。
[Character(name="avg_npc_122#5")]
[name="索娜"]  不考虑在移动城市之外的地方定居吗？那样比较容易避人耳目吧。
[character(name="avg_npc_103nc_1#3")]
[name="瑟奇亚克"]  ......那就不是“生活”了，是“生存”。
[name="瑟奇亚克"]  我是来道别的，特锦赛还没结束，人流量很大，这是悄悄离开大骑士领的好机会。
[Character(name="avg_npc_122#5")]
[name="索娜"]  ......新的城市吗。
[character(name="avg_npc_103nc_1")]
[name="瑟奇亚克"]  ......红松骑士团，我得对你们说句实话。
[name="瑟奇亚克"]  监正会取得了关于无胄盟和感染者收容治疗中心的信息，也不代表，他们能立刻把联合会赶下台——
[name="瑟奇亚克"]  ——不，我现在甚至开始觉得，他们根本威胁不到商业联合会。
[Character(name="avg_npc_122#2")]
[name="索娜"]  ......
[character(name="avg_npc_103nc_1")]
[name="瑟奇亚克"]  你也察觉到一点什么了，对吧？
[name="瑟奇亚克"]  可别说我绝情，但这都和现在的我没关系了。
[character(name="avg_npc_103nc_1#2")]
[name="瑟奇亚克"]  念在我们共同战斗过一小段时日的份上......好自为之吧，别和城市作对，焰尾。
[dialog]
[playsound(key="$d_gen_walk_n")]
[character(fadetime=1.5)]
[delay(time=2)]
[Character(name="avg_npc_123", name2="avg_496_wdmane_1#7", focus=2)]
[name="艾沃娜"]  ......什么啊，只是过来说泄气话的吗？
[Character(name="avg_npc_123", name2="avg_496_wdmane_1#7", focus=1)]
[name="格蕾纳蒂"]  所以我才讨厌骑士家族。
[stopmusic(fadetime=1)]
[Character(name="avg_npc_122#7")]
[name="索娜"]  ......和城市，作对。
[name="索娜"]  听着有些像滑稽的骑士小说啊......
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Background(image="bg_23_G09",screenadapt="coverall")]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[character(name="avg_237_gravel_1#6",fadetime=1)]
[delay(time=1)]
[name="砾"]  博士。
[name="砾"]  我被命令成为您的护卫，也有一段时间了，您对我......是怎么想的呢？
[name="砾"]  不瞒您说，我现在，只是和您共处一室就有些心跳加速了喔？
[Dialog]
[Decision(options="要叫医生吗？;......;私人问题请恕我暂时回避。", values="1;2;3")]
[Predicate(references="1")]
[name="砾"]  哎呀......真是让人遗憾。
[name="砾"]  但我觉得，您是在装作听不懂？
[Predicate(references="2")]
[name="砾"]  偶尔的沉默也很令人着迷，不过，如果博士您太过沉溺在工作中，也是会累坏身子的。
[Predicate(references="3")]
[name="砾"]  这可事关监正会和罗德岛的合作......您对我的评价可是很重要的。
[Predicate(references="1;2;3")]
[Dialog]
[character]
[PlaySound(key="$dooropenquite", volume=0.6)]
[delay(time=1)]
[playsound(key="$d_gen_walk_n")]
[Character(name="char_002_amiya_1#2", fadetime=1)]
[delay(time=1)]
[name="阿米娅"]  博士！临光小姐顺利进入决赛了！
[name="阿米娅"]  “风骑士赛前弃权，耀骑士不战而胜”，今天的报纸上是这么写的！
[Character(name="avg_237_gravel_1#4")]
[name="砾"]  ......风骑士离隐退只有一步之遥，大概不愿意在这个时候败给耀骑士吧。
[Character(name="avg_237_gravel_1")]
[name="砾"]  真是有些嫉妒耀骑士了，能让博士这么关心。
[Character(name="char_002_amiya_1#6")]
[CameraShake(duration=0.3, xstrength=15, ystrength=15, vibrato=20, randomness=50, fadeout=true, block=false)]
[name="阿米娅"]  砾、砾小姐？
[Character(name="avg_237_gravel_1#6")]
[name="砾"]  不，没别的意思。
[name="砾"]  ......暂时。
[Character(name="char_002_amiya_1#5")]
[name="阿米娅"]  啊......哈哈......
[name="阿米娅"]

... (全文16177字符)
```

### level_act13side_10_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔2 10-1
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_courtyard",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=0.1, block=false)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=0.1, block=false)]
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=0.1, block=false)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[delay(time=1)]
[Character(name="avg_npc_064_weapon_1", name2="avg_1014_nearl2_1#1$1", focus=1,fadetime=1)]
[delay(time=1)]
[name="佐菲娅"]  ——好！到此为止！
[name="佐菲娅"]  还有疼痛感吗？
[Character(name="avg_npc_064_weapon_1", name2="avg_1014_nearl2_1#6$1", focus=2)]
[name="玛嘉烈"]  不，状态完美。
[Character(name="avg_npc_064_weapon_1", name2="avg_1014_nearl2_1#6$1", focus=1)]
[name="佐菲娅"]  看来手臂已经完全恢复了，风骑士突然弃赛真是帮了大忙。
[dialog]
[Character]
[character(name="avg_npc_061#2",fadetime=1)]
[delay(time=1)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="玛莉娅"]  姐姐！剑枪的强化完成了！
[name="玛莉娅"]  试着采用了米诺斯的工艺技术，一面保证良好的源石技艺传导，一面试着用特殊聚合剂涂层来加强集中——
[name="玛莉娅"]  总之，这把武器会让姐姐的光芒更锋利的！
[Character(name="avg_npc_061#2", name2="avg_npc_101#3", focus=2)]
[name="老工匠"]  哈，我可把库存的老底全用上啦。
[name="老工匠"]  放心吧，这绝对是有史以来最好的剑——枪，对，剑枪。
[name="老工匠"]  你夺冠时拿的那把剑是第二好的。你带走的战锤是第三好的。
[Character(name="avg_1014_nearl2_1#6$1")]
[name="玛嘉烈"]  ......谢谢。
[Character(name="avg_npc_107", name2="avg_npc_101#2", focus=2)]
[name="老工匠"]  哈，这有啥。
[Character(name="avg_npc_107#3", name2="avg_npc_101", focus=1)]
[name="光头马丁"]  ......佐菲娅，这是我能找到的，血骑士的所有比赛记录了。
[Character(name="avg_npc_064_weapon_1", name2="avg_1014_nearl2_1#1$1", focus=1)]
[name="佐菲娅"]  好，时间紧迫。
[name="佐菲娅"]  玛嘉烈，我们要做好万全的准备。玛嘉烈？
[Character(name="avg_npc_064_weapon_1", name2="avg_1014_nearl2_1#6$1", focus=2)]
[name="玛嘉烈"]  ......
[name="玛嘉烈"]  ......谢谢，谢谢你们在我身边。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_23_G07",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_209_1#2",fadetime=1,block=true)]
[Delay(time=1)]
[name="罗伊"]  ......这也许是我们的最后一次任务了，莫妮克阁下。
[Character(name="avg_npc_209_1#2", name2="avg_npc_208_1#2", focus=2)]
[name="莫妮克"]  当然，我知道。
[name="莫妮克"]  我们当真要对耀骑士下手？
[Character(name="avg_npc_209_1#2", name2="avg_npc_208_1#2", focus=1)]
[name="罗伊"]  董事会的判断不一致。最麻烦的部分，就让白金去做就好。
[Character(name="avg_npc_209_1#2", name2="avg_npc_208_1#3", focus=2)]
[name="莫妮克"]  ......玄铁同意我们对耀骑士下手？为什么？在这之后，我们和耀骑士还会有瓜葛吗？
[Character(name="avg_npc_209_1#2", name2="avg_npc_208_1#3", focus=1)]
[name="罗伊"]  我不知道。也许玄铁从耀骑士和她身上看到了什么威胁......既然董事会有这个意思，那么正好。
[name="罗伊"]  董事会已经开始提防我们了，在玄铁给我们信号之前，我们最好暂时不要轻举妄动。
[name="罗伊"]  总之，现在还是祈祷血骑士能打败耀骑士吧，这样的话，我们能省多少事情。
[Character(name="avg_npc_209_1#2", name2="avg_npc_208_1", focus=2)]
[name="莫妮克"]  ......以你的眼光看，谁胜算比较大？
[Character(name="avg_npc_209_1#2", name2="avg_npc_208_1", focus=1)]
[name="罗伊"]  ......不好说呢......
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_23_G03",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[character(name="avg_npc_121#2",fadetime=1.5)]
[delay(time=1.5)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="大嘴莫布"]  我、我担任特锦赛决赛解说！？
[Character(name="avg_npc_211_1")]
[name="发言人马克维茨"]  这是数据的作用，莫布。你现在在骑士竞技解说之中，也名列前茅，恭喜。
[name="发言人马克维茨"]  再加上，从玛莉娅开始，临光姐妹一路走来你都参与其中，董事会认为这本身也是一个卖点，更想要委你重任。
[name="发言人马克维茨"]  你有看最近的《竞技新闻报》吗？你已经被称作“与光芒同行的声音”，现在名声大噪了。
[character(name="avg_npc_121#2")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="大嘴莫布"]  真、真、真的！！？
[Character(name="avg_npc_211_1")]
[name="发言人马克维茨"]  关于你的奖金......会在明天打到你的账户上。决赛结束之后，你还会有一笔收入。
[character(name="avg_npc_121")]
[name="大嘴莫布"]  那我是不是总算可以把父母接来大骑士领住啦？
[Character(name="avg_npc_211_1")]
[name="发言人马克维茨"]  当然，完全可以买下一栋大别墅了。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Background(image="bg_23_G09",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[character(name="char_002_amiya_1#6",fadetime=1.5)]
[delay(time=1.5)]
[name="阿米娅"]  ......决赛的......门票？
[Character(name="avg_npc_210_1")]
[name="伊奥莱塔·罗素"]  罗德岛为今年的卡西米尔特锦赛提供了许多帮助，关于应对矿石病的先进方案，卡西米尔从罗德岛身上学到了许多。
[name="伊奥莱塔·罗素"]  今年特锦赛的胜者，是由耀骑士和血骑士——是由两位感染者决出的。
[name="伊奥莱塔·罗素"]  既然如此，我认为罗德岛应该观看这一场前所未有的决战。
[Character(name="avg_npc_210_1#6")]
[name="伊奥莱塔·罗素"]  而且......那边那两位萨卡兹小姐，应该是玛嘉烈的熟识是吧？
[Character(name="char_147_shining_1", name2="char_179_cgbird_1", focus=1)]
[name="闪灵"]  ......谢谢您的好意。
[Character(name="char_147_shining_1", name2="char_179_cgbird_1", focus=2)]
[name="夜莺"]  临光......她会赢吧？
[Character(name="avg_npc_210_1#6")]
[name="伊奥莱塔·罗素"]  这就要你自己去现场观战啦，孩子。
[character(name="char_002_amiya_1")]
[name="阿米娅"]  门票有四张呢......
[Dialog]
[Decision(options="阿米娅一定要去的吧。;罗德岛的领导人可不能缺席。", values="1;2")]
[Predicate(references="1;2")]
[character(name="char_002_amiya_1#10")]
[name="阿米娅"]  那博士也要和我一起去！
[Character(name="char_002_amiya_1#10",name2="avg_237_gravel_1#3",focus=2)]
[name="砾"]  当然，如果博士去的话，我也一定会护卫好博士的安全。
[Character(name="char_002_amiya_1",name2="avg_237_gravel_1#3",focus=1)

... (全文39482字符)
```

### level_act13side_10_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔2 10-2
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_23_G02",screenadapt="coverall")]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[character(name="avg_npc_210_1#5",fadetime=1.5)]
[delay(time=1.5)]
[name="伊奥莱塔·罗素"]  ......“不畏苦暗”。
[name="伊奥莱塔·罗素"]  这些优秀的苗子，却要在这个遍布腐毒的土壤里长大......
[name="伊奥莱塔·罗素"]  也许我们做了一个错误的决定，临光......
[character(name="avg_npc_224")]
[name="“银枪的天马”"]  ......宗师。
[character(name="avg_npc_210_1#5")]
[name="伊奥莱塔·罗素"]  商业联合会最终也没猜到我们的目的。
[name="伊奥莱塔·罗素"]  当然......他们一定以为，你们来到这里，是为了借机敲打他们，是给监正会巩固权力的一环。
[name="伊奥莱塔·罗素"]  当然啦，我们肯定有这个目的就是了。监正会已经接替监管了零号地块，商业联合会必定为此付出代价。
[name="伊奥莱塔·罗素"]  但商人们一定不会明白，我们能为玛嘉烈那个孩子做到哪一步。
[name="伊奥莱塔·罗素"]  “不畏苦暗”，是临光家的祖训。
[name="伊奥莱塔·罗素"]  但是这句话，却被刻在了近三十名银枪天马骑士团成员的盾牌、枪与剑上。
[name="伊奥莱塔·罗素"]  在那场战争之中，在那场看不到希望的战役里，漆黑的沼泽正中，西里尔·临光发誓要救下每一个被围困的骑士。
[name="伊奥莱塔·罗素"]  没有补给，没有通讯，集团军的炮兵师和机动部队正在搜捕他们。
[name="伊奥莱塔·罗素"]  被临光说服参与救援行动的，只有七位骑士。在出发之前，他们每一个人都在自己盾牌上刻下了“不畏苦暗”。
[name="伊奥莱塔·罗素"]  ......七位骑士出发，回来的却有四十一人。
[name="伊奥莱塔·罗素"]  但是，那开始的七位骑士，只有西里尔和我回来了。
[character(name="avg_npc_224")]
[name="“银枪的天马”"]  ......但您和他救回了三十多个同胞。
[name="“银枪的天马”"]  也带回了......所有人的盾牌。
[character(name="avg_npc_210_1#5")]
[name="伊奥莱塔·罗素"]  “不畏苦暗”。在那晚过后，四十一个人的身上，都铭刻着这一段铭文。剑上、盔甲上、法杖上、盾上。
[name="伊奥莱塔·罗素"]  之后，我们向东突围。
[character(name="avg_npc_224")]
[name="“银枪的天马”"]  ......在与骑士团本部会合时，骑士再度只剩七人。
[character(name="avg_npc_210_1#5")]
[name="伊奥莱塔·罗素"]  宛如天意。
[character(name="avg_npc_224")]
[name="“银枪的天马”"]  但，歼敌三千，四十六面印有各自家族纹章的骑士盾牌，全部回到了卡西米尔的土地，没有一面被丢下。
[name="“银枪的天马”"]  黄金平原的黎明，这场战役，每一个征战骑士都耳熟能详，宗师。
[name="“银枪的天马”"]  向您致敬！
[character(name="avg_npc_210_1#4")]
[name="伊奥莱塔·罗素"]  ......无胄盟想要伤害临光家的孩子？
[name="伊奥莱塔·罗素"]  呵呵，他们的兵力储备如何？
[stopmusic(fadetime=1)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_23_G01",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[playMusic(intro="$m_bat_game02_intro", key="$m_bat_game02_loop", volume=0.4)]
[character(name="avg_npc_121#2",fadetime=1.5)]
[delay(time=1.5)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="大嘴莫布"]  ——爆、爆炸！二人包裹着源石技艺的一次交锋！竟然引发了爆炸！
[name="大嘴莫布"]  烟雾中率先出现的——是血骑士，血骑士被击退了！他换了一只手握斧——不是惯用手！是因为手臂被震麻了吗！？
[name="大嘴莫布"]  而另一面——玛嘉烈用她奇异的剑枪拄着地面！毫无疑问，这一次交锋，是保持住了身形的血骑士占了上风——
[character(name="avg_npc_214_1#2$1")]
[CameraShake(duration=0.5, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=0.5)]
[name="血骑士"]  呵——！
[character(name="avg_npc_121")]
[name="大嘴莫布"]  ——血骑士再度发起冲锋！耀骑士来得及重整态势吗！？
[Dialog]
[Character(name="char_empty", name2="avg_1014_nearl2_1#1$1")]
[PlaySound(key="$rungeneral", volume=1)]
[characteraction(name="left", type="move", xpos=-200, fadetime=0.2, block=true)]
[delay(time=0.51)]
[characteraction(name="left", type="move", xpos=300, power=5, fadetime=0.41, block=false)]
[Character(name="avg_npc_214_1#2$1", name2="avg_1014_nearl2_1#1$1",fadetime=0.5)]
[delay(time=0.51)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[PlaySound(key="$sheildimpact", volume=1)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.1, block=true)]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[characteraction(name="left", type="jump", xpos=-200, power=5, fadetime=0.2, times=0.5, block=false)]
[characteraction(name="right", type="move", xpos=100, power=5, fadetime=0.2, times=0.5, block=false)]
[delay(time=1)]
[Character(name="avg_1014_nearl2_1#1$1")]
[CameraShake(duration=0.3, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="玛嘉烈"]  ——！
[character(name="avg_npc_214_1#2$1")]
[name="血骑士"]  竟然......！
[Character(name="avg_1014_nearl2_1#1$1")]
[name="玛嘉烈"]  很遗憾，你慢了一步。
[Dialog]
[Character(name="avg_npc_214_1#2$1",name2="avg_1014_nearl2_1#1$1")]
[delay(time=0.51)]
[characteraction(name="right", type="move",xpos=100, power=5, fadetime=0.2, times=0.2, block=true)]
[characteraction(name="left", type="move", xpos=-100, power=5, fadetime=0.2, times=0.2, block=true)]
[delay(time=0.51)]
[characteraction(name="right", type="move",xpos=-200, power=5, fadetime=0.2, times=0.2, block=true)]
[characteraction(name="left", type="move", xpos=200, power=5, fadetime=0.2, times=0.2, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[PlaySound(key="$e_skill_skulsrsword",volume=1)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.3, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[characteraction(name="right", type="jump",xpos=100, power=5, fadetime=0.2, times=0.2, block=true)]
[characteraction(name="left", type="jump", xpos=-100, power=5, fadetime=0.2, times=0.2, block=true)]
[delay(time=0.51)]
[characteraction(name="right", type="move",xpos=-100, power=5, fadetime=0.2, times=0.2, block=true)]
[characteraction(name="left", type="move", xpos=100, power=5, fadetime=0.2, times=0.2, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[PlaySound(key="$e_skill_skulsrsword",volume=1)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.3, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[CameraShake(duration=0.4, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=fal

... (全文75408字符)
```

### level_act13side_hidden_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 隐藏AVG1 逃离
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_208_1",fadetime=1.5,block=true)]
[delay(time=1)]
[name="莫妮克"]  ......
[dialog]
[PlaySound(key="$d_gen_soldiersrun", volume=0.6)]
[Character(name="avg_npc_216", name2="avg_npc_208_1", focus=1)]
[delay(time=1)]
[name="第三小队队员"]  莫妮克阁下。
[Character(name="avg_npc_216", name2="avg_npc_208_1", focus=2)]
[name="莫妮克"]  第三小队所有人跟我一起行动。
[name="莫妮克"]  欣特莱雅想去哪里，她说了不算。
[name="莫妮克"]  ......留住她，无论生死。
[Character(name="avg_npc_216", name2="avg_npc_208_1", focus=1)]
[name="第三小队队员"]  是！
[Character(name="avg_npc_216", name2="avg_npc_208_1#3", focus=2)]
[name="莫妮克"]  绝对不要让......无关人员察觉到这件事。
[Character(name="avg_npc_216", name2="avg_npc_208_1", focus=2)]
[name="莫妮克"]  行动开始。
[dialog]
[PlaySound(key="$d_gen_soldiersrun", volume=0.6)]
[characteraction(name="left", type="move", xpos=-300, fadetime=2,block=false)]
[character(name="char_empty",name2="avg_npc_208_1",fadetime=0.5)]
[delay(time=2)]
[Character(name="avg_npc_208_1#2")]
[name="莫妮克"]  ......
[name="莫妮克"]  这是你自己的选择。
[name="莫妮克"]  欣特莱雅。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_23_G10",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2.5, block=true)]
[Character(name="char_empty")]
[PlaySound(key="$rungeneral", volume=0.5)]
[characteraction(name="middle", type="move", xpos=200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="middle", type="move", xpos=-200, fadetime=1, block=false)]
[Character(name="char_204_platnm_1#2",fadetime=0.7)]
[delay(time=2)]
[name="白金"]  呼......
[Character(name="char_204_platnm_1")]
[name="白金"]  如果罗伊阁下在的话，我怕是半点机会都没吧......
[name="白金"]  两位青金少一位，只是逃走的话，还算是......有些把握......
[Character(name="char_204_platnm_1#3")]
[name="白金"]  呵......
[name="白金"]  谁能想到无胄盟的白金大位，有一天会躲在监正会控制下的零号地块里呢......
[dialog]
[Character(name="char_204_platnm_1#4", focus=-1)]
[PlaySound(key="$leaveshake", volume=0.5)]
[delay(time=0.6)]
[Character(name="char_204_platnm_1")]
[name="白金"]  ......
[name="白金"]  休息时间到了......
[Dialog]
[delay(time=0.7)]
[PlaySound(key="$rungeneral", volume=0.6)]
[characteraction(name="middle", type="move", xpos=-300, fadetime=2,block=false)]
[Character(fadetime=0.5)]
[delay(time=2)]
[Character(name="avg_npc_216", name2="avg_npc_216", fadetime=1,block=true)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[delay(time=2)]
[Character(name="avg_npc_216", name2="avg_npc_216", focus=1)]
[name="第三小队队员A"]  她真的会逃到这里来吗？
[Character(name="avg_npc_216", name2="avg_npc_216", focus=2)]
[name="第三小队队员B"]  其它地方都搜查过了。
[Character(name="avg_npc_216", name2="avg_npc_216", focus=1)]
[name="第三小队队员A"]  也是......
[Character(name="avg_npc_216", name2="avg_npc_216", focus=2)]
[name="第三小队队员B"]  你脚步轻一点，别惊动那些巡逻的征战骑士。这个地方现在太敏感了......
[Character(name="avg_npc_216", name2="avg_npc_216", focus=1)]
[name="第三小队队员A"]  好、好！
[Character(name="char_204_platnm_1")]
[name="白金"]  （这里离最近港口还有一段距离......）
[name="白金"]  （从零号地块穿过工业区，然后可以选择从居住区或者商业区到达港口区......）
[name="白金"]  （太远了......）
[name="白金"]  （但只要能逃出工业区，就还能挣扎一下......）
[Character(name="avg_npc_216")]
[name="第三小队队员A"]  那边是不是有人？
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="第三小队队员A"]  别躲躲藏藏的，快出来！
[Character(name="char_204_platnm_1")]
[name="白金"]  ......
[Character(name="avg_npc_216")]
[name="第三小队队员A"]  （举起短弩）
[name="第三小队队员A"]  ......
[Character(name="char_204_platnm_1")]
[name="白金"]  ......
[Character(name="avg_npc_216")]
[name="第三小队队员A"]  是感染者吗，还是其他什么东西？
[Character(name="char_204_platnm_1#6")]
[name="白金"]  （再过来一点......）
[Character(name="avg_npc_216", name2="avg_npc_216", focus=2)]
[name="第三小队队员B"]  （小声）怎么样，有发现吗。
[Character(name="avg_npc_216", name2="avg_npc_216", focus=1)]
[name="第三小队队员A"]  （小声）那边转角好像有什么东西。
[Character(name="avg_npc_216", name2="avg_npc_216", focus=2)]
[name="第三小队队员B"]  （小声）我掩护你。
[Character(name="avg_npc_216", name2="avg_npc_216", focus=1)]
[name="第三小队队员A"]  （小声）好。
[dialog]
[Character(name="avg_npc_216", name2="avg_npc_216", focus=0)]
[PlaySound(key="$d_gen_soldiersrun", volume=0.5)]
[characteraction(name="right", type="move", xpos=800, fadetime=2.5,block=false)]
[character(name="avg_npc_216",name2="char_empty",fadetime=0.5)]
[characteraction(name="left", type="move", xpos=600, fadetime=2.5,block=false)]
[character(name="char_empty",name2="avg_npc_216",fadetime=0.5)]
[delay(time=1.55)]
[character]
[Character(name="char_empty")]
[PlaySound(key="$d_gen_walk_n", volume=0.5)]
[characteraction(name="middle", type="move", xpos=-200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="middle", type="move", xpos=200, fadetime=1, block=false)]
[Character(name="char_204_platnm_1",fadetime=0.7)]
[delay(time=2)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.6, block=true)]
[Background(image="bg_23_G10",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.6, block=true)]
[Character(name="avg_npc_216", name2="avg_npc_216", focus=2)]
[name="第三小队队员B"]  这是......
[Character(name="avg_npc_216", name2="avg_npc_216", focus=1)]
[name="第三小队队员A"]  白金的箭筒，她肯定就在附近。
[dialog]
[Character(name="avg_npc_216", name2="avg_npc_216", focus=-1)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$e_atk_arrow_h")]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[CameraShake(duration=0.6, xstrength=5, ystrength=8, vibrato=30, randomness=90, block=true)]
[characteraction(name="right", type="move", ypos=-800, fadetime=1.5, block=true)]
[delay(time=1.5)]
[Character(name="char_204_platnm_1#6")]
[name="白金"]  别动！
[Character(name="avg_npc_216")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="第三

... (全文36798字符)
```

### level_act13side_hidden_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 隐藏AVG2 选择
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Background(image="bg_23_G10",screenadapt="coverall")]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_220", name2="avg_npc_122", focus=1)]
[name="感染者骑士"]  呃，所以我们都要去那个什么罗德岛接受治疗吗？
[Character(name="avg_npc_220", name2="avg_npc_122", focus=2)]
[name="索娜"]  不是“都要去”，是“可以去”，别因为习惯了就太小看矿石病啊！
[name="索娜"]  就算我们有再多想做的事情，如果最先垮掉的是我们的身体，岂不是都无从谈起了？
[Character(name="avg_npc_220", name2="avg_npc_122", focus=1)]
[name="感染者骑士"]  呃、说的也是......
[Character(name="avg_npc_220", name2="avg_npc_122", focus=2)]
[name="索娜"]  嗯。都照顾好自己，我们已经很久没有接受正儿八经的矿石病治疗了。
[name="索娜"]  感染者骑士们姑且不论，队伍里还有那么多普通的工人、农户和市民......我们不能逼着他们遭受矿石病折磨。
[name="索娜"]  不能让杰米的惨剧再发生一次。
[Character(name="avg_npc_220", name2="avg_npc_122", focus=1)]
[name="感染者骑士"]  ......嗯。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="left", type="move", xpos=-300, fadetime=2,block=false)]
[character(name="char_empty",name2="avg_npc_122",fadetime=0.5)]
[delay(time=2)]
[Character(name="avg_npc_122#2")]
[name="索娜"]  呼......
[dialog]
[character]
[Character(name="avg_npc_123#2",fadetime=1,block=true)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[delay(time=1)]
[name="格蕾纳蒂"]  索娜。
[Character(name="avg_npc_123#2", name2="avg_npc_122", focus=2)]
[name="索娜"]  是小灰啊，怎么了？
[Character(name="avg_npc_123#3", name2="avg_npc_122", focus=1)]
[name="格蕾纳蒂"]  我们和那个叫芙蓉的萨卡兹医生联系过了，罗德岛下午就得离开大骑士领。
[name="格蕾纳蒂"]  我们人数很多，要早做准备。
[Character(name="avg_npc_123#3", name2="avg_npc_122", focus=2)]
[name="索娜"]  嗯，查丝汀娜和艾沃娜应该已经在联系还能联系到的感染者了。
[Character(name="avg_npc_123", name2="avg_npc_122", focus=1)]
[name="格蕾纳蒂"]  无胄盟和商业联合会就这么善罢甘休了？
[Character(name="avg_npc_123", name2="avg_npc_122#2", focus=2)]
[name="索娜"]  ......如果我们得知的事情是真的，那他们现在只会自顾不暇。
[name="索娜"]  何况罗德岛还有监正会这张护身符，暂时......是安全的。
[Character(name="avg_npc_123#7", name2="avg_npc_122#2", focus=1)]
[name="格蕾纳蒂"]  ......
[Character(name="avg_npc_123#7", name2="avg_npc_122#4", focus=2)]
[name="索娜"]  嗯？干嘛盯着我？
[Character(name="avg_npc_123#7", name2="avg_npc_122#4", focus=1)]
[name="格蕾纳蒂"]  托兰对你说了些什么？
[Character(name="avg_npc_123#7", name2="avg_npc_122#5", focus=2)]
[name="索娜"]  呃......怎么突然提这个？
[Character(name="avg_npc_123#7", name2="avg_npc_122#5", focus=1)]
[name="格蕾纳蒂"]  自从你和他去了趟大骑士领外的村庄之后，你的神色就变了。
[Character(name="avg_npc_123#7", name2="avg_npc_122#4", focus=2)]
[name="索娜"]  ......
[Character(name="avg_npc_123#3", name2="avg_npc_122#4", focus=1)]
[name="格蕾纳蒂"]  大骑士领附近的村庄是这些年依附于四城联合建立起来的，那里应该只有些普通的农户而已。
[Character(name="avg_npc_123#2", name2="avg_npc_122#4", focus=1)]
[name="格蕾纳蒂"]  赏金猎人可不该在那里有一席之地，他一定有什么目的。
[Character(name="avg_npc_123#2", name2="avg_npc_122", focus=2)]
[name="索娜"]  ......他委托给了我们一件事。
[name="索娜"]  关于卡西米尔，关于这个国家，感染者和我们所有人。
[Character(name="avg_npc_123", name2="avg_npc_122", focus=1)]
[name="格蕾纳蒂"]  那为什么不告诉我？
[Character(name="avg_npc_123", name2="avg_npc_122#3", focus=2)]
[name="索娜"]  啊哈哈......其实我心底里也没谱，最近一直在想这件事，本来打算想通了再告诉其他人......
[Character(name="avg_npc_123#3", name2="avg_npc_122#3", focus=1)]
[name="格蕾纳蒂"]  哼嗯......
[Character(name="avg_npc_123#3", name2="avg_npc_122#3", focus=2)]
[name="索娜"]  ......生、生气了？
[dialog]
[Character(name="avg_430_fartth_1", name2="avg_496_wdmane_1", fadetime=1,block=true)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[delay(time=2)]
[Character(name="avg_430_fartth_1")]
[name="查丝汀娜"]  那就更该把话说明白。
[name="查丝汀娜"]  这不是索娜你告诉过我的吗？
[Character(name="avg_430_fartth_1", name2="avg_496_wdmane_1", focus=2)]
[name="艾沃娜"]  哈哈，你是不知道格蕾纳蒂这几天有多坐立难安，我都告诉她没事了。
[Character(name="avg_npc_123", name2="avg_496_wdmane_1", focus=1)]
[name="格蕾纳蒂"]  咳。谁让索娜总是一个人把很多事情扛下来......
[Character(name="avg_npc_122#4")]
[name="索娜"]  ......抱歉。
[Character(name="avg_430_fartth_1")]
[name="查丝汀娜"]  所以，你在纠结什么？
[Character(name="avg_npc_122#2")]
[name="索娜"]  ......
[delay(time=0.5)]
[Character(name="avg_npc_122#8")]
[name="索娜"]  如果我们接下来要做的事情，与一开始大家成立红松骑士团的目的并不完全一致......你们会怎么办？
[Character(name="avg_npc_123")]
[name="格蕾纳蒂"]  ......什么意思？
[Character(name="avg_npc_122#8")]
[name="索娜"]  如果我们不止为了对抗腐朽的骑士，为了对抗商业联合会，也不只是为了博取感染者的利益而战——
[name="索娜"]  为此我们要忍受他人对感染者歧视，要与过去的敌人重新交好，要聪明地选择抗争的方式，我们会被迫改变自己——
[Character(name="avg_npc_122#2")]
[name="索娜"]  ——最后会把我们原本近在眼前的宁静生活再一次无限延期，我们得再投身到另一个漩涡中去......你们会怎么选？
[Character(name="avg_430_fartth_1#2")]
[name="查丝汀娜"]  ......
[Character(name="avg_npc_123#2")]
[name="格蕾纳蒂"]  ......
[Character(name="avg_496_wdmane_1#7", name2="avg_npc_122#2", focus=1)]
[name="艾沃娜"]  欸，突然问这种问题......我不擅长想这些啊。有区别吗？
[Character(name="avg_npc_123", name2="avg_npc_122#2", focus=1)]
[name="格蕾纳蒂"]  ......那你自己是怎么想的？
[Character(name="avg_npc_123", name2="avg_npc_122#2", focus=2)]
[name="索娜"]  身为感染者，身为一名骑士，我认为......我们应该试着去做更多的事情。尽管我现在......还不清楚。
[Character(name="avg_npc_123", name2="avg_npc_122", focus=2)]
[name="索娜"]  但是作为“索娜”，我并不想这么简单地离开大家......更不想逼迫各位走一条原本不在视野里的路。
[name="索娜"]  何况这条出路究竟通向何方，现在谁也不知道。
[Character(name="avg_npc_123#7", name2="avg_npc_122", focus=1)]
[name="格蕾纳蒂"]  ......索娜。
[Character(name="avg_npc_123#7", name2="avg_npc_122", focus=2)]
[name="索娜"]  ......嗯。
[Character(name="avg_npc_123#3", name2="avg_npc_122", focus=1)]
[name="格蕾纳蒂"]  最近你经常想得很多，这让我们都很不安，但我希望......我希望你明白一件事。
[name="格蕾纳蒂"]  “红松骑士团”虽然许以骑士团之名，但我们都清楚，我们既是骑士，也不是骑士。
[name="格蕾纳蒂"]  骑士也好，感染者也好，札拉克也好，哪怕最后你只打算作为“索娜”做些什么，都可以和我们商量。
[Character(name="avg_npc_123#3", name2="avg_npc_122#4", focus=2)]
[name="索娜"]  小灰......
[Character(name="avg_npc_123#7", name2="avg_npc_122#4", focus=1)]
[name="格蕾纳蒂"]  然后你得到的答案也是肯定的。
[name="格蕾纳蒂"]  我们不会分开。
[Character(name="avg_430_fartth_1")]
[name="查丝汀娜"]  说实在，在经历了这一切以后，我想骑士团内也不会有太多感染者只把自己当做寻常骑士了吧。
[name="查丝汀娜"]  当然，有意向离去的，寻找普通生活的，我们会帮助他们......
[Character(name="avg_430_fartth_1#8")]
[name="查丝汀娜"]  但不会是我们。不会是我们四个。
[Character(name="avg_430_fartth_1#8", name2="avg_496_wdmane_1#10", focus=2)]
[name="艾沃娜"]  当然！要是就这么向那群家伙妥协了，我这么些年不是白等了嘛！
[Character(name="avg_npc_123", name2="avg_496_wdmane

... (全文20324字符)
```

### level_act13side_hidden_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 隐藏AVG3 路漫漫
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Background(image="bg_kxstreet",screenadapt="coverall")]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_215_1#1")]
[name="烛骑士"]  现在我也，稍微有点耐不下性子看书了——
[name="烛骑士"]  ——玛嘉烈。
[dialog]
[character]
[Character(name="avg_1014_nearl2_1#1$1",fadetime=1,block=true)]
[delay(time=1.5)]
[name="玛嘉烈"]  ......薇薇安娜。什么时候的事？
[Character(name="avg_npc_215_1#1", name2="avg_1014_nearl2_1#1$1", focus=1)]
[name="烛骑士"]  不知道呢。
[name="烛骑士"]  非要说的话，也许是我明明没有做好觉悟就闯进特锦赛的那一刻吧。
[Character(name="avg_npc_215_1#1", name2="avg_1014_nearl2_1#1$1", focus=2)]
[name="玛嘉烈"]  你可以留下的。
[Character(name="avg_npc_215_1#1", name2="avg_1014_nearl2_1#1$1", focus=1)]
[name="烛骑士"]  我确实想过留在这里，毕竟这座大骑士领，还有你这样的骑士。
[Character(name="avg_npc_215_1#2", name2="avg_1014_nearl2_1#1$1", focus=1)]
[name="烛骑士"]  ......但这也是我做出的选择。
[Character(name="avg_npc_215_1#2", name2="avg_1014_nearl2_1#4$1", focus=2)]
[name="玛嘉烈"]  选择？
[Character(name="avg_npc_215_1#6", name2="avg_1014_nearl2_1#4$1", focus=1)]
[name="烛骑士"]  你知道吗，为了你和血骑士那场荒唐的冒险而决心拔剑的时候，我其实......挺兴奋的。
[Character(name="avg_npc_215_1#6", name2="avg_1014_nearl2_1#2$1", focus=2)]
[name="玛嘉烈"]  ......
[Character(name="avg_npc_215_1#1", name2="avg_1014_nearl2_1#2$1", focus=1)]
[name="烛骑士"]  别沉默呀，都让我不好意思了......
[name="烛骑士"]  那是很难得的体验。为他人，为某个信念，为一件看似不合理的事情而战斗。
[name="烛骑士"]  也许离开莱塔尼亚之后，我从未真正以骑士身份生活过。
[Character(name="avg_npc_215_1#1", name2="avg_1014_nearl2_1#1$1", focus=2)]
[name="玛嘉烈"]  你真不留下？如果你走了，只是正中他们的下怀。
[Character(name="avg_npc_215_1#1", name2="avg_1014_nearl2_1#1$1", focus=1)]
[name="烛骑士"]  换个说法吧，玛嘉烈，不要让我留下，请祈求我回来。我一定会回来的。
[Character(name="avg_npc_215_1#2", name2="avg_1014_nearl2_1#1$1", focus=1)]
[name="烛骑士"]  不过现在，就让我服从散华骑士团的“安排”......去偏远的城市待上一段时间吧。
[Character(name="avg_npc_215_1#1", name2="avg_1014_nearl2_1#1$1", focus=1)]
[name="烛骑士"]  也算一次不错的冒险。
[Character(name="avg_npc_215_1#1", name2="avg_1014_nearl2_1#1$1", focus=2)]
[name="玛嘉烈"]  你的骑士同伴们呢？
[Character(name="avg_npc_215_1#1", name2="avg_1014_nearl2_1#1$1", focus=1)]
[name="烛骑士"]  我为数不多的同伴，不是都已经到齐了吗。
[Character(name="avg_npc_215_1#1", name2="avg_1014_nearl2_1#3$1", focus=2)]
[name="玛嘉烈"]  .....深感荣幸。
[Character(name="avg_npc_215_1#1", name2="avg_1014_nearl2_1#6$1", focus=2)]
[name="玛嘉烈"]  那至少，让我为你送行吧。
[Character(name="avg_npc_215_1#1", name2="avg_1014_nearl2_1#6$1", focus=1)]
[name="烛骑士"]  好啊。让两届冠军为我送行，我也荣幸之至。
[name="烛骑士"]  对了。收拾行李的时候忘了这本书，正好，就送你吧。
[Character(name="avg_npc_215_1#1", name2="avg_1014_nearl2_1#4$1", focus=2)]
[name="玛嘉烈"]  诗集？
[Character(name="avg_npc_215_1#1", name2="avg_1014_nearl2_1#4$1", focus=1)]
[name="烛骑士"]  《两个月亮与金盏花》。
[Character(name="avg_npc_215_1#1", name2="avg_1014_nearl2_1#5$1", focus=2)]
[name="玛嘉烈"]  唔。我不是很懂莱塔尼亚的诗歌艺术......
[Character(name="avg_npc_215_1#2", name2="avg_1014_nearl2_1#5$1", focus=1)]
[name="烛骑士"]  符号和隐喻的魅力就在于，不强迫你得出一个具体的，有逻辑的答案。
[name="烛骑士"]  就像耀骑士和她的行为一样。
[Character(name="avg_npc_215_1#1", name2="avg_1014_nearl2_1#5$1", focus=1)]
[name="烛骑士"]  ......车要到了。看见了吗？
[Character(name="avg_npc_215_1#1", name2="avg_1014_nearl2_1#1$1", focus=2)]
[name="玛嘉烈"]  嗯。
[Character(name="avg_npc_215_1#1", name2="avg_1014_nearl2_1#1$1", focus=1)]
[name="烛骑士"]  下次再见，大骑士领会变个模样吗？
[Character(name="avg_npc_215_1#1", name2="avg_1014_nearl2_1#2$1", focus=2)]
[name="玛嘉烈"]  ......你知道的，这个国度没那么轻易改变。
[Character(name="avg_npc_215_1#1", name2="avg_1014_nearl2_1#1$1", focus=2)]
[name="玛嘉烈"]  但至少，我想让骑士们能够重新被称作骑士。
[Character(name="avg_npc_215_1#1", name2="avg_1014_nearl2_1#1$1", focus=1)]
[name="烛骑士"]  好。记住你的承诺，玛嘉烈。
[dialog]
[character]
[Character(name="avg_npc_217",fadetime=1.5,block=true)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[delay(time=1.5)]
[name="来接应的骑士"]  烛骑士阁下，久等了，上车吧。
[Character(name="avg_npc_217", name2="avg_1014_nearl2_1#1$1", focus=1)]
[name="来接应的骑士"]  哦......真意外，您也好，耀骑士阁下。
[Character(name="avg_npc_217", name2="avg_1014_nearl2_1#1$1", focus=2)]
[name="耀骑士"]  您好。
[Character(name="avg_npc_215_1#1", name2="avg_npc_217", focus=1)]
[name="烛骑士"]  我要立刻启程吗？
[Character(name="avg_npc_215_1#1", name2="avg_npc_217", focus=2)]
[name="来接应的骑士"]  啊，是的......您已经是最后一位乘客啦。天灾信使也已经准备好了。
[Character(name="avg_npc_215_1#1", name2="avg_npc_217", focus=1)]
[name="烛骑士"]  ......好。但愿那是一座美丽的城市吧。
[Character(name="avg_npc_215_1#1", name2="avg_1014_nearl2_1#1$1", focus=1)]
[name="烛骑士"]  后会有期。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[characteraction(name="left", type="move", xpos=-300, fadetime=2,block=false)]
[character(name="char_empty",name2="avg_1014_nearl2_1#1$1",fadetime=0.5)]
[delay(time=2)]
[Character(name="avg_1014_nearl2_1#6$1")]
[name="玛嘉烈"]  ......后会有期，薇薇安娜。
[dialog]
[delay(time=1.5)]
[Character(name="avg_1014_nearl2_1#1$1")]
[name="玛嘉烈"]  ......
[name="玛嘉烈"]  她已经走了，你不上前来吗？
[dialog]
[character]
[Character(name="avg_npc_212_1#1",fadetime=1,block=true)]
[delay(time=1)]
[name="发言人麦基"]  ......
[Character(name="avg_1014_nearl2_1#4$1")]
[name="玛嘉烈"]  我记得你是......
[Character(name="avg_npc_212_1#1")]
[name="发言人麦基"]  商业联合会发言人，麦基......不过特锦赛已经结束，我的发言人职务也会很快终止。
[Character(name="avg_1014_nearl2_1#1$1")]
[name="玛嘉烈"]  也许你该鼓起勇气。
[Character(name="avg_npc_212_1#1")]
[name="发言人麦基"]  德罗斯特小姐和散华骑士团的相关事务一直是我负责的。
[Character(name="avg_npc_212_1#2")]
[name="发言人麦基"]  我只是尽到最后的义务，不过看起来，我并没有赶上，很遗憾。
[Character(name="avg_1014_nearl2_1#2$1")]
[name="玛嘉烈"]  你......好吧。
[Character(name="avg_npc_212_1#1")]
[name="发言人麦基"]  德罗斯特女士遭到这样的对待，与您分不开关系。
[name="发言人麦基"]  耀骑士阁下，考虑到您在特锦赛上做的事情，现在，我们是敌人。
[Character(name="avg_1014_nearl2_1#1$1")]
[name="玛嘉烈"]  这不准确，发言人阁下。
[Character(name="avg_1014_nearl2_1#7$1")]
[name="玛嘉烈"]  我们只是各自投身于自己的信念，为自己的理想和正义而奋斗。
[name="玛嘉烈"]  倘若......联合会真的还有所谓理想，而不是靠倾轧他人来中饱私囊的话。
[Character(name="avg_npc_212_1#3")]
[name="发言人麦基"]  ......我倒是没想到您如此伶牙俐齿。
[Character(name="avg_1014_nearl2_1#1$1")]
[name="玛嘉烈"]  只是实事求是。
[Character(name="avg_npc_212_1#2")]
[name="发言人麦基"]  ......好吧。
[Character(name="avg

... (全文22366字符)
```

### level_act13side_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔2 纯1
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
“城市是一只怪物，它把人吞噬殆尽，我们却还要感恩戴德地待在它的肠胃里。”
“等着生活把我们消化，等着白骨和血肉被排出，留下的会成为养分，供城市前行。”
“即是文明欣欣向荣。”
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_23_G01",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$batmeeting_intro", key="$batmeeting_loop", volume=0.4)]
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
[Character(name="avg_npc_121#3",fadetime=1,block=true)]
[delay(time=1)]
[name="大嘴莫布"]  欢迎来到卡西米尔国立竞技场！欢迎来到，卡西米尔特别锦标赛！我是各位的老朋友——大嘴莫布！
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
[Character(name="avg_npc_121")]
[name="大嘴莫布"]  经过了漫长的预选阶段，全卡西米尔翘首以盼的卡西米尔骑士特别锦标赛正赛阶段，将于今日迎来首场对决！
[name="大嘴莫布"]  决斗、竞速、花样竞技，三大类别、八大项目、四十三小项，荣誉、财富，无数骑士团和骑士们对奖牌势在必得！
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
[dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_23_G08",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_217")]
[name="观众席上的骑士"]  ......莫布怎么成了特锦赛解说？他是不是背地里给哪个发言人塞钱了？
[Character(name="avg_npc_217", name2="avg_npc_218", focus=2)]
[name="捧着爆米花的骑士"]  塞钱？真要靠塞钱，这得塞多少钱？
[Character(name="avg_npc_217", name2="avg_npc_218", focus=1)]
[name="观众席上的骑士"]  莫布平时就喜欢口无遮拦，到这种大场合上，万一他一时嘴瓢？
[Character(name="avg_npc_217", name2="avg_npc_218", focus=2)]
[name="捧着爆米花的骑士"]  哈，你知道吗，之前那个名嘴大胡子凯奇，就是因为在特锦赛上“调侃”了某位大骑士......
[name="捧着爆米花的骑士"]  然后第二天就消失啦，要爆米花不？
[Character(name="avg_npc_217", name2="avg_npc_218", focus=1)]
[name="观众席上的骑士"]  嗨，引咎辞职嘛，常见的伎俩。
[Character(name="avg_npc_217", name2="avg_npc_218", focus=2)]
[name="捧着爆米花的骑士"]  （咀嚼声）我说的是消失（咀嚼声）不是辞职。你懂吧。
[Character(name="avg_npc_217", name2="avg_npc_218", focus=1)]
[delay(time=0.2)]
[CameraShake(duration=0.2, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[delay(time=0.2)]
[name="观众席上的骑士"]  呃......真的？
[dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
[Background(image="bg_23_G01",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_121")]
[name="大嘴莫布"]  八支大骑士团，六十四支骑士团，以及两位特立独行的独立骑士，于今日齐聚特锦赛现场！
[name="大嘴莫布"]  卡西米尔骑士特别锦标赛，将向整片泰拉大地，彰显骑士之美，彰显骑士之风！
[name="大嘴莫布"]  本日的第一场比赛，将是来自锋盔骑士团与云雾骑士团的对决！来自双方的十位骑士，究竟能为骑士团斩获几个比分！？
[Character(name="avg_npc_121#3")]
[name="大嘴莫布"]  巨额的奖金池哪怕此时此刻也在增加，来自卡西米尔各竞技场的每一点消费，都将按照骑士份额转化为特锦赛奖金！
[Character(name="avg_npc_121")]
[name="大嘴莫布"]  究竟哪个骑士团能获得最多的奖杯？又会是哪位骑士从决斗赛中脱颖而出，成为本届特锦赛的冠军骑士？
[Character(name="avg_npc_121#3")]
[PlaySound(key="$livecrowd", volume=0.5, loop=false, channel="people")]
[name="大嘴莫布"]  让我们——拭目以待——！
[stopmusic(fadetime=2.3)]
[dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2.5, block=true)]
[Background(image="bg_23_G02",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
5:43 P.M.  天气/晴     
大骑士领卡瓦莱利亚基，冠军墙展厅
[dialog]
[Character(name="avg_npc_212_1")]
[name="发言人麦基"]  合身吗？马克维茨先生？
[dialog]
[character]
[Character(name="avg_npc_211_1",fadetime=1,block=true)]
[delay(time=1)]
[name="发言人马克维茨"]  ......托您的福。
[Character(name="avg_npc_211_1", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  别这么说，一身定制的合乎礼仪的服装，是我们必备的门面。
[name="发言人麦基"]  您有留下那位裁缝的联络方式吗？我相信您还会用得到他的。
[Character(name="avg_npc_211_1#5", name2="avg_npc_212_1", focus=1)]
[name="发言人马克维茨"]  ......
[Character(name="avg_npc_212_1")]
[name="发言人麦基"]  先生，麻烦给我一杯葡萄酒，谢谢。
[Character(name="avg_npc_211_1#5", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  您在想什么？
[Character(name="avg_npc_211_1#3", name2="avg_npc_212_1", focus=1)]
[name="发言人马克维茨"]  不，没什么......
[Character(name="avg_npc_211_1#4", name2="avg_npc_212_1", focus=1)]
[name="发言人马克维茨"]  也许我只是在感叹，这场宴会多么盛大......
[Character(name="avg_npc_211_1#4", name2="avg_npc_212_1#6", focus=2)]
[name="发言人麦基"]  啊......“也许”。
[name="发言人麦基"]  也许你只是还没缓过神来，恰尔内先生的事情我们都很遗憾。
[Character(name="avg_npc_211_1#7", name2="avg_npc_212_1#6", focus=1)]
[CameraShake(duration=0.5, xstrength=10, ystrength=10, vibrato=15, randomness=60, fadeout=true, block=false)]
[name="发言人马克维茨"]  ......！
[Character(name="avg_npc_211_1#3", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  他是个兢兢业业的人，无论是作为公司员工，还是作为联合会发言人，他都尽力了。
[Character(name="avg_npc_211_1#3", name2="avg_npc_212_1#2", focus=2)]
[name="发言人麦基"]  其实我在成为发言人之后才认识他，对于特锦赛的工作而言，我是新手，他才是前辈。
[Character(name="avg_npc_211_1#3", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  他对待赏识的人一向不差，对吧？
[Character(name="avg_npc_211_1#5", name2="avg_npc_212_1", focus=1)]
[name="发言人马克维茨"]  也许......
[Character(name="avg_npc_211_1#5", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  别也许了，摆出个笑脸来吧。
[name="发言人麦基"]  今天才是开幕式的第二天，冠军墙对外开放的大好日子，驻场管理摆着一副臭脸可不行。
[Character(name="avg_npc_211_1#3", name2="avg_npc_212_1", focus=1)]
[name="发言人马克维茨"]  您、您说得对，很抱歉......
[Character(name="avg_npc_211_1#3", name2="avg_npc_212_1#6", focus=2)]
[name="发言人麦基"]  别总这么低声下气，马克维茨，咱们之间也别用“您”了，太过死板，不利于沟通。
[dialog]
[Character(name="avg_npc_211_1#3", name2="avg_npc_212_1#6", focus=2)]
[PlaySound(key="$livecrowd", volume=0.25, loop=false, channel="people")]
[delay(time=0.5)]
[Character(name="avg_npc_211_1#3", name2="avg_npc_212_1#6", focus=1)]
[name="发言人马克维茨"]  怎么了？是不是有什么动静？
[Character(name="avg_npc_211_1#3", name2="avg_npc_212_1#3", focus=2)]
[name="发言人麦基"]  唔。
[Character(name="avg_npc_211_1#3", name2="avg_npc_212_1", focus=2)]
[name="发言人麦基"]  是特邀骑士嘉宾，我看看时间......你看，她一向很守时，真希望各位骑士都向她学习。
[name="发言人麦基"]  容我失陪一下，还有，请适应您可以免费取用酒水的权利，好好喝一杯吧。
[Character(name="avg_npc_211_1#4", name2="avg_npc_212_1", focus=1)]
[name="发言人马克维茨"]  哦，好的......
[Character(name="avg_npc_212_1")]
[name="发言人麦基"]  甜美的微醺，你该享受它。
[Dial

... (全文28124字符)
```

### level_act13side_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_23_G09",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_237_gravel_1#4",fadetime=1,block=true)]
[delay(time=1)]
[name="砾"]......博士？
[name="砾"]您从餐厅回来之后，就一直紧锁着眉头哦？
[Character(name="avg_237_gravel_1#3")]
[name="砾"]如果感到疲惫的话，我可以——
[dialog]
[Decision(options="你怎么看待今天这场晚宴？;你觉得，马克维茨是个怎样的人？", values="1;2")]
[Predicate(references="1")]
[Character(name="avg_237_gravel_1")]
[name="砾"]很得体，博士。看来您已经习惯这类交际了？
[name="砾"]看得出，虽然常务董事没有亲自露面，但那些企业高管都对您青睐有加......
[dialog]
[Predicate(references="2")]
[name="砾"]......如我之前对您说的，因为耀骑士的事件，有一位发言人引咎辞职。
[name="砾"]马克维茨是临时顶上这个位置的，在此之前，他只是一个默默无闻的小角色......
[name="砾"]虽然他的身上还保留有一些未经洗礼的人情味......不过在现在这个环境，能持续多久可说不太好。
[Predicate(references="1;2")]
[Dialog]
[Decision(options="你认为罗德岛的计划，有可行性吗？", values="1")]
[Predicate(references="1")]
[Character(name="avg_237_gravel_1#2")]
[name="砾"]......
[Character(name="avg_237_gravel_1#6")]
[name="砾"]先不提这个......您真的信任我吗？
[name="砾"]联合会的渗透并非某种组织形式上的渗透......在金钱和确实发生改变的社会面前，即使联合会什么也不做，骑士也会倒向资本。
[Character(name="avg_237_gravel_1#3")]
[name="砾"]监正会对罗德岛礼遇的原因几乎和耀骑士密不可分。即使如此，您这样缜密的人......如果不小心对待监正会，是会吃亏的。
[Dialog]
[Decision(options="感谢你的提醒。;这我当然知道。", values="1;2")]
[Predicate(references="1;2")]
[Decision(options="那么，能告诉我你的意见吗？;所以你的意见是？", values="1;2")]
[Predicate(references="1;2")]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Character(name="avg_npc_211_1#3",fadetime=1,block=true)]
[delay(time=1)]
[name="发言人马克维茨"]......锈铜骑士......又，复赛了？
[Character(name="avg_npc_211_1#3",name2="avg_npc_222",focus=2)]
[name="企业员工"]是的......毕竟骑士协会根据录像和其他骑士的证词，向国民院证明那位感染者不过是自己过度施法导致的疾病恶化。
[name="企业员工"]死因也是“矿石病”，锈铜骑士并没有直接责任，所以......
[Character(name="avg_npc_211_1#5",name2="avg_npc_222",focus=1)]
[name="发言人马克维茨"]......就算这是真的......那难道我们就该......
[Character(name="avg_npc_211_1",name2="avg_npc_222",focus=1)]
[name="发言人马克维茨"]你先出去吧。
[Character(name="avg_npc_211_1",name2="avg_npc_222",focus=2)]
[name="企业员工"]好的。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[characteraction(name="right", type="move", xpos=300, fadetime=2,block=false)]
[character(name="avg_npc_211_1#4",name2="char_empty",fadetime=0.5)]
[delay(time=2)]
[Character(name="avg_npc_211_1#4")]
[name="发言人马克维茨"]......
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[CameraEffect(effect="Grayscale",keep=true, initamount=0, amount=1, block=true)]
[Background(image="bg_23_G10",screenadapt="coverall")]
[Character(name="avg_npc_221")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[name="感染者骑士"]......
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[CameraEffect(effect="Grayscale", amount=0, block=true)]
[Background(image="bg_23_G09",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_211_1#5")]
[name="发言人马克维茨"]......拨通国民院副审官的......私人电话。
[Dialog]
[PlaySound(key="$d_avg_telephonebusy",channel="bgs", volume=0.6, loop=true, block=false, volume=0.6)]
[delay(time=0.6)]
[soundvolume(channel="bgs",volume=0,fadetime=5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="电话忙音响了两声。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="马克维茨突然回想起了自己童年的时候，父亲的书房桌上，摆着一台黄铜色的电话。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[PlaySound(key="$d_gen_transmissionget", volume=0.6)]
[Character(name="avg_npc_211_1#5",focus=-1)]
[name="电话那头的声音"]......发言人阁下，您想出结果了？
[Character(name="avg_npc_211_1#4")]
[name="发言人马克维茨"]只要恰尔内先生不再掌握证据，就可以了，对吧？
[Character(name="avg_npc_211_1#4",focus=-1)]
[name="电话那头的声音"]当然......可是我得提醒您，如果事后暴露了，你我都难辞其咎。
[name="电话那头的声音"]所以，杀死他，是最安全的。
[Character(name="avg_npc_211_1#5")]
[name="发言人马克维茨"]我向您保证。
[name="发言人马克维茨"]保证我确实......可以堵住恰尔内先生的嘴。
[Character(name="avg_npc_211_1#2")]
[name="发言人马克维茨"]具体手段，您就不要过问了。
[Character(name="avg_npc_211_1#2",focus=-1)]
[name="电话那头的声音"]好吧......如果您能拿出诚意的话。
[name="电话那头的声音"]明天我就会着手重审奥尔默·英格拉的案件，在七天之内，只要您能给我一个足够有诚意的答案......
[name="电话那头的声音"]奥尔默·英格拉就会从此消失在骑士竞技之中。
[Character(name="avg_npc_211_1#5")]
[name="发言人马克维茨"]......诚意。
[Character(name="avg_npc_211_1#5",focus=-1)]
[name="电话那头的声音"]是的。至少，您得向我证明恰尔内先生“确实永远不会背叛”。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="马克维茨记得，记得那台黄铜色的电话。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="那时的电话还没有如今普及，电缆绕过了酒吧、旅社与轰鸣的工地。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="铃声响起后，悲欢喜怒也会悄然降临。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="这就是卡西米尔的生活......现代生活。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Character(name="avg_npc_211_1#8")]
[name="发言人马克维茨"]......我想您应该明白一件事情......
[name="发言人马克维茨"]您是在挑衅一位发言人。
[Character(name="avg_npc_211_1#8",focus=-1)]
[name="电话那头的声音"]......
[Character(name="avg_npc_211_1#5")]
[name="发言人马克维茨"]您和我心里都明白，我只是临危受命，我在董事会里并没有靠山。
[name="发言人马克维茨"]但这不代表，我会任您宰割。
[Character(name="avg_npc_211_1#2")]
[name="发言人马克维茨"]无胄盟的指挥权......曾在恰尔内先生手里。那么现在......
[Character(name="avg_npc_211_1#2",focus=-1)]
[name="电话那头的声音"]......
[name="电话那头的声音"]......请您不要误会，我并不是在挑战您的权力。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="权力。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Character(name="avg_npc_211_1#2",focus=-1)]
[name="电话那头的声音"]我只是提醒您，确保我们

... (全文21510字符)
```

### level_act13side_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔 纯剧情3
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
确认卡瓦莱利亚基陷入紧急情况。
确认讯号代码正确。确认部队识别码正确。
全队听令。
撤下伪装，进城。
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_23_G09",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_237_gravel_1")]
[name="砾"]  ......距离电力完全恢复，还需要一点时间。
[name="砾"]  罗德岛的各位已经在指引下回到了房间休息，如果二位想要确认的话......
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]  ......博士，我想去看看各位。
[name="阿米娅"]  事发突然，也许会有一些干员弄不清状况，这些天对感染者的抗议，也让干员们积攒了不少压力。
[dialog]
[Decision(options="那就有劳阿米娅了。;......;真的不需要我帮忙吗？",values="1;2;3")]
[Predicate(references="1")]
[Character(name="char_002_amiya_1#6")]
[name="阿米娅"]  啊，没关系的，博士。
[Character(name="char_002_amiya_1#4")]
[name="阿米娅"]  这些天一直是博士在应付各种商业洽谈和社交活动，其实我还挺过意不去的。
[Character(name="char_002_amiya_1#3")]
[name="阿米娅"]  趁着这个机会，赶紧休息一下吧。
[Predicate(references="2")]
[Character(name="char_002_amiya_1#3")]
[name="阿米娅"]  ......啊哈哈，博士已经很累了吧。
[name="阿米娅"]  毕竟从昨天开始就一直在应付那些企业家，嗓子都哑了吧？
[Predicate(references="3")]
[Character(name="char_002_amiya_1#3")]
[name="阿米娅"]  没关系，有芙蓉小姐在，应该不会出什么差错。
[name="阿米娅"]  我也只是去确认一下各位的情况，很快就会回来的。
[Predicate(references="1;2;3")]
[Character(name="avg_237_gravel_1", name2="char_002_amiya_1", focus=1)]
[name="砾"]  请阿米娅小姐放心吧，您不在的时间里，我会照顾好博士的。
[Character(name="avg_237_gravel_1", name2="char_002_amiya_1#2", focus=2)]
[name="阿米娅"]  啊......嗯。
[Character(name="avg_237_gravel_1", name2="char_002_amiya_1#3", focus=2)]
[name="阿米娅"]  那么我先下去啦。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[characteraction(name="right", type="move", xpos=300, fadetime=2,block=false)]
[character(name="avg_237_gravel_1",name2="char_empty",fadetime=0.5)]
[delay(time=2)]
[Character(name="avg_237_gravel_1")]
[name="砾"]  ......{@nickname}博士。
[name="砾"]  最近商业联合会有一些动向，恐怕会对罗德岛不利。
[name="砾"]  加上现在的停电事件，恐怕下一步会是更加明目张胆的阴谋。
[name="砾"]  最近......请千万不要离开我的视线。当然，您要是自愿留在我的身边，那是再好不过。
[dialog]
[Decision(options="想出去逛逛吗？",values="1")]
[Predicate(references="1")]
[Character(name="avg_237_gravel_1#3")]
[name="砾"]  ......嘻嘻，您突然这么解风情，倒是让我有些吃惊。
[name="砾"]  怎么了？难道发生了什么好事吗？
[dialog]
[Decision(options="砾小姐，您是怎么看待商业联合会的？",values="1")]
[Predicate(references="1")]
[Character(name="avg_237_gravel_1#4")]
[name="砾"]  ......您不是问过类似的问题了吗？怎么，是想多听一听我的声音吗？可以哦。
[Character(name="avg_237_gravel_1#2")]
[name="砾"]  他们是卡西米尔的蛀虫。
[name="砾"]  商人们联合起来，腐蚀骑士和城市，最终达成他们自己的目的。
[dialog]
[Decision(options="不。",values="1")]
[Predicate(references="1")]
[Decision(options="商业联合会，如其名，只是“联合”罢了。",values="1")]
[Predicate(references="1")]
[Decision(options="利益是连系他们的纽带，他们当然可被分割。",values="1")]
[Predicate(references="1")]
[Decision(options="不过是与骑士们的对抗，让他们看起来，像一个整体。",values="1")]
[Predicate(references="1")]
[Character(name="avg_237_gravel_1#4")]
[name="砾"]  ......
[name="砾"]  ......您做了什么？
[dialog]
[Decision(options="商业联合会的常务董事大致有四类人。",values="1")]
[Predicate(references="1")]
[Character(name="avg_237_gravel_1")]
[name="砾"]  嘻......愿闻其详。
[dialog]
[Decision(options="急于推进时代，取缔骑士阶层的激进分子。",values="1")]
[Predicate(references="1")]
[Decision(options="守旧却扎实，一步一脚印的稳健派。",values="1")]
[Predicate(references="1")]
[Decision(options="没有任何立场，只要有利益就趋之若鹜的逐利者。",values="1")]
[Predicate(references="1")]
[Character(name="avg_237_gravel_1#4")]
[name="砾"]  ......最后一种呢？
[dialog]
[Decision(options="对于如今的罗德岛而言，还为时尚早。",values="1")]
[Predicate(references="1")]
[Decision(options="贸然接触，反而危险。",values="1")]
[Predicate(references="1")]
[Character(name="avg_237_gravel_1#4")]
[name="砾"]  ......您的意思是，联合会内部有分歧？而您......已经抓住了那些分歧？
[dialog]
[Decision(options="很难说是分歧。;他们根本就不可能存在“团结”。;皆为利来，皆为利往。",values="1;2;3")]
[Predicate(references="1;2;3")]
[Character(name="avg_237_gravel_1#5")]
[name="砾"]  ......但您不过初来乍到，只是通过发言人的渠道，结识了一部分常务董事......
[name="砾"]  您怎么敢如此断言？一旦您选错了信任对象，其后果绝非监正会可以承担......
[dialog]
[Decision(options="罗德岛从未考虑过依赖他人牺牲来达成自己的目的。;您总不能认为，我是真的毫无牺牲觉悟去参加那些宴会的吧？",values="1;2")]
[Predicate(references="1;2")]
[Character(name="avg_237_gravel_1")]
[name="砾"]  ......不。
[Character(name="avg_237_gravel_1#6")]
[name="砾"]  您当然不。
[stopmusic(fadetime=1.5)]
[dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_23_G04",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$normal01_intro", key="$normal01_loop", volume=0.4)]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$swordtsing3", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_npc_209_1")]
[name="罗伊"]  你们还有时间可以浪费吗？
[name="罗伊"]  关于感染者的通缉令已经发出，等到大隔断的影响过去，你们无路可逃。
[Character(name="avg_npc_209

... (全文40591字符)
```

### level_act13side_st04

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="“让所有人都站起来。”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="“让这一切归于寂静。”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="“如果觉得浪涛吵闹，就去令大海平静。”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="“文明欣欣向荣，城市轰鸣前进，能消灭他们的只有他们自己。”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="“不要交给时间，他们连时间都能打败。要把握住，要托付给自己。”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="“托付给每一个人。”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_sportsbar",screenadapt="coverall")]
[playMusic(intro="$bar_intro", key="$bar_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[name="电视里的声音"]  特锦赛出现特殊情况——两位冠军共赴冠军墙，这是前所未有的事情！
[name="电视里的声音"]  不仅如此，冠军耀骑士——拒绝了来自骑士协会的颁奖，独自离开！
[name="电视里的声音"]  这毫无疑问是一种亵渎。
[Dialog]
[Character(name="avg_npc_120#2", name2="avg_npc_101", focus=1)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="老骑士"]  疼疼疼......
[Character(name="avg_npc_120#2", name2="avg_npc_101#2", focus=2)]
[name="老工匠"]  老家伙，不能打就不要强出头，交给玛莉娅和佐菲娅不就好了吗！
[Character(name="avg_npc_120#2", name2="avg_npc_101#2", focus=1)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="老骑士"]  你有脸说我！？啊——疼疼——
[Dialog]
[Character]
[Character(name="avg_npc_107#2",fadetime=1,block=true)]
[delay(time=1)]
[name="光头马丁"]  ......
[Character(name="avg_npc_107#2", name2="avg_npc_101#3", focus=2)]
[name="老工匠"]  干嘛老盯着你那把锤子，马丁，一晚上的热身运动，让你怀念起过去了？
[Character(name="avg_npc_107#2", name2="avg_npc_101#3", focus=1)]
[name="光头马丁"]  ......有点吧。
[name="光头马丁"]  也不知道临光家那边怎么样了......
[stopmusic(fadetime=1)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_nearllivingroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[playMusic(intro="$distressed_intro", key="$distressed_loop", volume=0.4)]
[delay=2]
[character(name="avg_npc_061#7",fadetime=1.5)]
[delay(time=1.5)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="玛莉娅"]  欸？
[Character(name="avg_npc_108", name2="avg_npc_061#7", focus=2)]
[name="玛莉娅"]  ......叔叔......要暂时离开大骑士领？
[Character(name="avg_npc_108", name2="avg_npc_061#7", focus=1)]
[name="玛恩纳"]  你们到底是姓临光的，别总是待在佐菲娅家里，不成体统。
[Character(name="avg_npc_108#2")]
[name="玛恩纳"]  ......我会离开一段时间，在这期间......玛嘉烈。
[name="玛恩纳"]  ......你真的决定留在卡西米尔？
[Character(name="avg_1014_nearl2_1#1$1")]
[name="玛嘉烈"]  是的。
[Character(name="avg_npc_108")]
[name="玛恩纳"]  ......你应该知道自己会面对什么。
[name="玛恩纳"]  你不会被理解。
[Character(name="avg_1014_nearl2_1#1$1")]
[name="玛嘉烈"]  ......当然，我一开始就知道。
[Character(name="avg_npc_108")]
[name="玛恩纳"]  ......
[name="玛恩纳"]  那就这样吧，我们没有其他话可说了。
[Dialog]
[playsound(key="$d_gen_walk_n")]
[character(fadetime=1.5)]
[delay(time=2)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_kxstreet",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_108", name2="avg_npc_213_1", focus=2)]
[name="托兰"]  ......怎么突然改性了？
[Character(name="avg_npc_108", name2="avg_npc_213_1", focus=1)]
[name="玛恩纳"]  ......托兰......
[Character(name="avg_npc_108", name2="avg_npc_213_1", focus=2)]
[name="托兰"]  突然想要离开大骑士领，哼？为了什么？
[Character(name="avg_npc_108", name2="avg_npc_213_1", focus=1)]
[name="玛恩纳"]  ......在你眼里，我现在是什么模样？
[Character(name="avg_npc_108", name2="avg_npc_213_1", focus=2)]
[name="托兰"]  能什么模样。你自己还不清楚吗？
[name="托兰"]  ——但是说真的，你让我们所有人都失望了。
[name="托兰"]  你可以不是监正会的高层，可以不是改变国民院的那个人，但是，你至少该是我们的英雄，我们的临光。
[name="托兰"]  我不知道你离开城市是要去哪儿，但我得说——除了我以外，他们大都失望了。再让他们见到你，他们会巴不得杀了你的。
[Character(name="avg_npc_108", name2="avg_npc_213_1", focus=1)]
[name="玛恩纳"]  那他们打得过我吗？
[Character(name="avg_npc_108", name2="avg_npc_213_1", focus=2)]
[name="托兰"]  啧。
[Character(name="avg_npc_108#3", name2="avg_npc_213_1", focus=1)]
[name="玛恩纳"]  我放弃了很多东西，托兰。
[name="玛恩纳"]  ......只是，我还是经常怀抱着一个不切实际的想法。
[name="玛恩纳"]  他们应该还在某处。
[Character(name="avg_npc_108#3", name2="avg_npc_213_1#2", focus=2)]
[name="托兰"]  ......
[Character(name="avg_npc_108", name2="avg_npc_213_1#2", focus=1)]
[name="玛恩纳"]  他是战争英雄的长子，他是我玛恩纳的兄弟，是家族最强大的骑士。
[name="玛恩纳"]  而她......是卡西米尔最美的人，优雅，端庄，如同一颗宝石......
[name="玛恩纳"]  他们曾是我眼中的天之骄子，他们不该就这么......了无音讯。
[Character(name="avg_npc_108#3", name2="avg_npc_213_1#2", focus=1)]
[name="玛恩纳"]  十多年了。
[name="玛恩纳"]  我一直在想这件事。
[Character(name="avg_npc_108#3", name2="avg_npc_213_1#2", focus=2)]
[name="托兰"]  已经十五年了。当时花了那么久苦寻无果，现在又想——
[Character(name="avg_npc_108#2", name2="avg_npc_213_1#2", focus=1)]
[name="玛恩纳"]  ......只是......带薪旅行而已。
[Character(name="avg_npc_108#2", name2="avg_npc_213_1#3", focus=2)]
[name="托兰"]  你一个人？
[Character(name="avg_npc_108#2", name2="avg_npc_213_1#3", focus=1)]
[name="玛恩纳"]  一趟未必有希望的旅程，一个人还不够吗？
[Character(name="avg_npc_108#2", name2="avg_npc_213_1", focus=2)]
[name="托兰"]  你不是一个会......被耀骑士带来的情绪感染的人，我就先不问你为什么突然作出决定了——
[name="托兰"]  你知道怎么找到我......“我们”。
[Character(name="avg_npc_108#3", name2="avg_npc_213_1", focus=1)]
[name="玛恩纳"]  ......我要找到的，是我自己。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_23_G10",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1.5)]
[Character(name="avg_npc_122#2", name2="avg_1014_nearl2_1#1$1", focus=1)]
[name="索娜"]  ......罗德岛吗。
[Character(name="avg_npc_122#2", name2="avg_1014_nearl2_1#1$1", focus=2)]
[name="玛嘉烈"]  那里能为你们提供治疗，而且，也不会强迫你们做些什么。
[Character(name=

... (全文22743字符)
```

### ref_act13side

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔2 Ref

[Image(image="23_kv",screenadapt="coverall", fadetime=0)]
```


> 本章节共40个脚本文件，此处展示前30个。

## 统计

- 总字符数：845011
- 对话行数：6646


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
