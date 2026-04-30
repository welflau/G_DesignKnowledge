# 明日方舟 · 活动剧情 · act44side（35段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act44side」完整剧情脚本（35个文件，3437行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act44side
- 脚本文件数：35

### guide_informant_choice_end_01

```
[HEADER(is_skippable=false, is_tutorial=true, dont_clear_gameobjectpool_onstart=true)] 东国夏活情报室-choice_end触发第一段
[Tutorial(waitForSignal="informant_choice_end_entry_anim_displayed")]
[Tutorial(target="choice_end_btn_next_round", searchBtnInChildren=true,           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=1.5, dialogHead="$avatar_makiri")] 不错的选择！客人的“<color=#FF476A>信任</color>”和“<color=#62B815>兴味</color>”在这次谈话中发生了一定的变化，现在就趁热打铁，继续刚才的话题吧！
```

### guide_informant_choice_end_02

```
[HEADER(is_skippable=false, is_tutorial=true, dont_clear_gameobjectpool_onstart=true)] 东国夏活情报室-choice_end触发第二段
[Tutorial(waitForSignal="informant_choice_end_entry_anim_displayed")]
[Tutorial(target="choice_end_btn_settle", searchBtnInChildren=true,          animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=1.5, dialogHead="$avatar_makiri")] 哎呀！客人“<color=#FFA800>耐心</color>”耗尽，并不想继续再聊下去了，这种情况下只能选择结单，结束这笔交易了。
```

### guide_informant_entry

```
[HEADER(is_skippable=false, is_tutorial=true)] 东国夏活情报室-entry触发
[Tutorial(waitForSignal="informant_entry_anim_displayed")]
[Tutorial(target="entry_panel_customer_bar",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_makiri", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 哦？立刻就有客人上门了。作为一个合格的情报商人，让我们先从仔细观察客人，确认客人的信息开始吧。
[Tutorial(target="entry_panel_tutorial_customer_info",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_makiri", dialogX="$f_lower_dialog_pos_x")] 这里可以观察到客人的性格与交易偏好。我们可以通过客人的穿着打扮将其分为不同的类型，但需注意的是，即使是同类型的客人也会有不同的性格差异，应对的方式也要有所区别哦。
[Tutorial(target="entry_panel_milestone_point",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_makiri", dialogX="$f_lower_dialog_pos_x")] 这里会统计本次交易客人的定金——基础宝物袋，我们的目的是在这个基础上获得进一步的收益！
[Tutorial(target="entry_start_btn", searchBtnInChildren=true,           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=1.5, dialogHead="$avatar_makiri")] 那么让我们正式开始本次的试营业。
```

### guide_informant_home

```
[HEADER(is_skippable=false, is_tutorial=true)] 东国夏活情报室-活动页触发
[Tutorial(waitForSignal="informant_home_entry_anim_displayed")]
[PopupDialog(dialogHead="$avatar_makiri")] 在御机生活也是很不容易的，大家各有各的难处，各有各的需要。像我们这种靠情报吃饭的人，这时候就能派上用场啦。
[Tutorial(target="home_btn_enter", searchBtnInChildren=true,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_makiri")] 让我们开始营业，迎接今天的客人吧！
```

### guide_informant_result

```
[HEADER(is_skippable=false, is_tutorial=true)] 东国夏活情报室-result触发
[PopupDialog(dialogHead="$avatar_makiri")] 在这里我们可以看到整个营业日内接待过的所有客人，和每次交易的详细状况。
[PopupDialog(dialogHead="$avatar_makiri")] 虽然今天只来了一名客人，之后的客人数量会更多，类型也会更丰富。
[PopupDialog(dialogHead="$avatar_makiri")] 之后遇到不同客人时，要记得留心观察。虽然御机形形色色的客人多得数不过来，但大家有各自的特点。
[PopupDialog(dialogHead="$avatar_makiri")] 他们对“<color=#FFA800>耐心</color>”、“<color=#FF476A>信任</color>”、“<color=#62B815>兴味</color>”的需求各不相同，既然走上了这条情报之路，相信你绝对可以做到总结客人的需求，然后针对他们的特点来做针对性的交流。这对你来说并不难，对吧？
[PopupDialog(dialogHead="$avatar_makiri")] 那么试营业就到此为止。真是期待，之后走进这家小店的会是什么样的客人呢。
```

### guide_informant_select_choice_01

```
[HEADER(is_skippable=false, is_tutorial=true)] 东国夏活情报室-select_choice触发第一段
[Tutorial(waitForSignal="informant_select_choice_entry_anim_displayed")]
[Tutorial(target="select_choice_trust",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_makiri", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 这里会显示客人目前的“<color=#FF476A>信任</color>”情况，可以观察这里来判断客人对情报的信任程度。
[Tutorial(target="select_choice_trust",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_makiri", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 当“<color=#FF476A>信任</color>”程度够高时，本次交易结算时就有机会<color=#FF476A>一本万利</color>！
[Tutorial(target="select_choice_attention",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_makiri", dialogX="$f_lower_dialog_pos_x")] 这里会显示客人目前的“<color=#62B815>兴味</color>”情况，可以观察这里来判断客人对情报的感兴趣程度。
[Tutorial(target="select_choice_attention",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_makiri", dialogX="$f_lower_dialog_pos_x")] 客人对情报的“<color=#62B815>兴味</color>”越高，单次交易的<color=#62B815>收益</color>也会越高。
[Tutorial(target="select_choice_button_item_1", searchBtnInChildren=true,           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=1.5, dialogHead="$avatar_makiri")] 好，现在让我们来回应客人吧。选择一种回应风格。
[Tutorial(target="select_choice_button_item_1", searchBtnInChildren=true,           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=1.5, dialogHead="$avatar_makiri")] 向客人推销我们的宝贵情报吧。
```

### guide_informant_select_choice_02

```
[HEADER(is_skippable=false, is_tutorial=true, dont_clear_gameobjectpool_onstart=true)] 东国夏活情报室-select_choice触发第二段
[Tutorial(waitForSignal="informant_select_choice_patience_anim_displayed")]
[Tutorial(target="select_choice_patience",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_makiri", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 嗯？客人的情绪发生了变化！这里可以看到客人已经开始<color=#FFA800>烦躁</color>了，如果接下来的对话还说不到重点，可能会导致客人<color=#FFA800>直接离开</color>。
[Tutorial(target="select_choice_use_insight_btn", searchBtnInChildren=true,           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=1.5, dialogHead="$avatar_makiri")] 这种情况下就要谨慎选择交谈的方法......遇到这种难以判断的情况时，不妨试试我的独家秘笈，“望气”！
[Tutorial(target="select_choice_insight_tutorial_detail",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_makiri", dialogX="$f_lower_dialog_pos_x")] 使用“望气”后可以发现，客人目前对情报的“<color=#62B815>兴味</color>”已经足够，但“<color=#FF476A>信任</color>”似乎还有继续提升的空间。先点击收起“望气”。
[Tutorial(target="select_choice_button_item_1", searchBtnInChildren=true,           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=1.5, dialogHead="$avatar_makiri")] 虽然有些冒险，但为了远大的利益，我们再试试好啦！
[Tutorial(target="select_choice_button_item_1", searchBtnInChildren=true,           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=1.5, dialogHead="$avatar_makiri")] 换一种方式再向客人推销我们的情报！
```

### guide_informant_single_result

```
[HEADER(is_skippable=false, is_tutorial=true)] 东国夏活情报室-single_result触发
[Tutorial(waitForSignal="informant_single_result_second_anim_displayed")]
[PopupDialog(dialogHead="$avatar_makiri")] 此时由于客人<color=#FFA800>耐心</color>耗尽，“<color=#FF476A>信任</color>”也就失去了作用，直接以“小赚一笔”的状态完成了这笔交易。
[PopupDialog(dialogHead="$avatar_makiri")] 好在客人对情报还有一定的“<color=#62B815>兴味</color>”，我们依然可以获得一些额外的<color=#62B815>小费</color>。
[PopupDialog(dialogHead="$avatar_makiri")] 放轻松啦，虽然这次只是小赚了一笔，但等到正式营业时，客人会有更充足的<color=#FFA800>耐心</color>来进行交流，到时候我们再接再厉就好啦。
[PopupDialog(dialogHead="$avatar_makiri")] 还有一个独家秘诀，在这里分享给你吧。正式营业时，通常在客人“<color=#FFA800>走神</color>”的时候就可以考虑主动拍板，来提前结束交易。
[PopupDialog(dialogHead="$avatar_makiri")] 这样还有机会根据“<color=#62B815>兴味</color>”获取一笔额外的奖金。
```

### level_act44side_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=2)]
[playMusic(intro="$darkness01_intro",key="$darkness01_loop", volume=0.6)]
[name="值班警察"]刑警，炸肉排饭到了。
[name="刑警"]辛苦。你先回去吧。
[name="值班警察"]是！
[dialog]
[PlaySound(key="$dooropenquite", volume=1)]
[Delay(time=1.5)]
[name="星熊"]......
[name="刑警"]已经半夜了，你从下午进入御机就在躲我们的人，一口吃的也没混到，肯定饿了吧。
[name="星熊"]（点头）
[name="刑警"]那先吃饭吧。东国的炸肉排饭。
[PlaySound(key="$d_avg_plateplace", volume=1)]
刑警特意强调了“东国”两个字，把餐盘推给星熊。
[PlaySound(key="$d_avg_pickupchopsticks", volume=1)]
星熊一言不发地拿起深碗，抓起筷子，开始大口扒饭。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Image(image="64_i01",screenadapt="coverall",x=150)]
[ImageTween( xScaleFrom=1.3, yScaleFrom=1.3, xScaleTo=1, yScaleTo=1, duration=60,xTo=0)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[name="刑警"]怎么样，龙门有这东西吗？
[PlaySound(key="$d_avg_dishes", volume=1)]
[name="星熊"]（闷头扒饭）
[name="刑警"]看你这副样子，到底有多长时间没吃过家乡菜了？
[name="星熊"]（往嘴里塞肉排）
[name="刑警"]......算了，你先吃。
[PlaySound(key="$d_avg_humaneat", volume=1)]
[name="星熊"]（咯吱咯吱地嚼卷心菜）
[PlaySound(key="$d_avg_drinkswllw", volume=1)] 
[name="星熊"]（喝水）
[PlaySound(key="$d_avg_dishes", volume=1)]
[name="星熊"]（把整个深碗端起来仰头往嘴里扒）
[Dialog]
[Delay(time=1.5)]
[CameraShake(duration=0.2, xstrength=2, ystrength=5, vibrato=10, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_plateplace", volume=1)]
[name="星熊"]（放下空空如也的深碗）
[name="星熊"]呼。
[name="刑警"]怎么样，怀念吗？
[name="星熊"]报告刑警，不是怀念，我就是饿了。
[name="刑警"]你——
[name="星熊"]其实我从龙门出发前就吃的炸肉排饭。下次能请我吃点别的吗？比如你们把我抓走那地方的关东煮？闻起来那么香，汤我都没喝上一口。
[name="星熊"]还有，顺带一提，我在龙门自掏腰包请嫌疑人吃饭的时候都是吃肠粉的。
[name="刑警"]态度放端正点，星熊嫌疑人。
[name="星熊"]嫌疑人？我才来御机不到二十四小时，我的嫌疑是什么？
[name="刑警"]二十年前的嫌疑人就不是嫌疑人了吗？
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Image]
[Background(image="bg_offce",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "left", name = "avg_136_hsguma_1#2$1",duration = 1)]
[charslot(slot = "right", name = "avg_npc_1898_1#1$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "left", name = "avg_136_hsguma_1#2$1",focus="l")]
[name="星熊"]......刑警先生。
[charslot(slot = "right", name = "avg_npc_1898_1#1$1",focus="r")]
[name="刑警"]我姓惟任。
[charslot(slot = "left", name = "avg_136_hsguma_1#2$1",focus="l")]
[name="星熊"]惟任刑警。
[charslot(slot = "right", name = "avg_npc_1898_1#1$1",focus="r")]
[name="惟任刑警"]说。
[charslot(slot = "left", name = "avg_136_hsguma_1#2$1",focus="l")]
[name="星熊"]二十年，我的追诉期已经过了。
[name="星熊"]再说，我在龙门的督察证现在也应该确认得差不多了吧。
[charslot(slot = "right", name = "avg_npc_1898_1#1$1",focus="r")]
[name="惟任刑警"]结果还没出。
[charslot(slot = "right", name = "avg_npc_1898_1#7$1",focus="r")]
[name="惟任刑警"]就当你说的是真的好了，那到底是什么风，能把一位龙门警察吹回来？
[name="惟任刑警"]你失业了？你有仇家要对付？
[charslot(slot = "right", name = "avg_npc_1898_1#2$1",focus="r")]
[name="惟任刑警"]龙门有什么人派你来的？
[name="惟任刑警"]还是说，你跟最近城里在传的北院间谍有关系？
[charslot(slot = "left", name = "avg_136_hsguma_1#9$1",focus="l")]
[name="星熊"]停停停，你再这么猜下去，事情就大条了。
[charslot(slot = "left", name = "avg_136_hsguma_1#2$1",focus="l")]
[name="星熊"]刑警，看看这封信吧。
[charslot(slot = "right", name = "avg_npc_1898_1#6$1",focus="r")]
[name="惟任刑警"]刚刚已经搜过一遍，你身上居然还藏着东西？
[charslot(slot = "left", name = "avg_136_hsguma_1#11$1",focus="l")]
[name="星熊"]警察最懂警察。
[charslot(slot = "right", name = "avg_npc_1898_1#1$1",focus="r")]
[name="惟任刑警"]......
[stopmusic(fadetime=2)]
[playsound(key="$d_avg_paper2")]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.7, block=true)]
[Background(image="bg_lungmenbridge",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$motorbikestart", volume=0.6)]
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=35, randomness=45, fadeout=true, block=false)]
[PlaySound(key="$drift", volume=0.6)]
[CameraShake(duration=3, xstrength=10, ystrength=12, vibrato=25, randomness=45, fadeout=true, block=false)]
[Delay(time=3)]
[playMusic(intro="$tech_intro",key="$tech_loop", volume=0.6)]
[charslot(slot = "m", name = "avg_136_hsguma_1#2$1",duration=0.5)]
[Delay(time=1)]
[name="星熊"]呼。
[name="星熊"]再跑一圈，怎么样，伙计，还撑得住吗？
[dialog]
[CameraShake(duration=1, xstrength=5, ystrength=5, vibrato=35, randomness=45, fadeout=true, block=false)]
[playsound(key="$motorbikestart", loop=true, channel="bgs")]
[Delay(time=1.5)]
[StopSound(channel="bgs", fadetime=0.5)]
[charslot(slot = "m", name = "avg_136_hsguma_1#11$1")]
[name="星熊"]看来还成。那就走吧。
[dialog]
[charslot(duration=0.5)]
[PlaySound(key="$motorbikestart")]
[Delay(time=2)]
[playsound(key="$d_avg_enginerun", loop=true, channel="bgs", volume=0.4)]
[Delay(time=2)]
[charslot(slot = "m", name = "avg_136_hsguma_1#5$1",duration=0.5)]
[Delay(time=1)]
[name="星熊"]（是夫人的车？）
[dialog]
[charslot(slot = "m", name = "avg_136_hsguma_1#2$1")]
[PlaySound(key="$motorbikestart")]
[charslot(duration=0.5)]
[CameraShake(duration=-1, xstrength=5, ystrength=5, vibrato=30, randomness=90, fadeout=true, block=false)]
独角的鬼把整个身体伏在车上，看准了直道结束的位置，笔直地朝前冲去。
咆哮的风几乎让她看不清追赶者的距离——
[dialog]
[CameraShake(duration=1, xstrength=15, ystrength=15, vibrato=30, randomness=90, fadeout=true, block=false)]
[StopSound(channel="bgs", fadetime=1)]
[PlaySound(key="$drift", volume=0.6)]
[Delay(time=1.5)]
[charslot(slot = "left", name = "avg_136_hsguma_1#2$1",duration = 1)]
[delay(time=1.5)]
[charslot(slot = "left", name = "avg_136_hsguma_1#2$1",focus="l")]
[name="星熊"]夫人怎么停车了？
[dialog]
[charslot(slot = "right", name = "avg_npc_1645_1#4$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "right", name = "avg_npc_1645_1#4$1",focus="r")]
[name="文月"]来凑个热闹而已，没打算一决高下。
[name="文月"]听彦吾说，出发去新汐斯塔前，诗怀雅将局内事务打理得井井有条，免得给你们这些留守的增添压力。
[charslot(slot = "left", name = "avg_136_hsguma_1#2$1",focus="l")]
[name="星熊"]是啊。要不是Missy临走前把事情处理得干净利落，没给我留什么负担，我怎么能抽出时间来这儿呢。
[charslot(slot = "right", name = "avg_npc_1645_1#4$1",focus="r")]
[name="文月"]也是。那还有什么事能让星熊督察烦心？

... (全文17644字符)
```

### level_act44side_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="64_g1_jindastreet_d",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[playMusic(key="$normal_loop", volume=0.6)]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_1918_1#3$1",duration=1)]
[delay(time=2)]
[charslot(slot="m",name="avg_npc_1918_1#4$1")]
[name="萌萌香"]（打哈欠）
[charslot(slot="m",name="avg_npc_1918_1#3$1")]
[name="萌萌香"]新口味煎饼，“高级网纹蜜瓜配叙拉古风情红酱”，还有“甄选浓厚瘤奶配本酿造酱油”......
[charslot(slot="m",name="avg_npc_1918_1#23$1")]
[name="萌萌香"]看起来好好吃啊。
[charslot(slot="m",name="avg_npc_1918_1#13$1")]
[name="萌萌香"]不行，热量，时刻谨记热量！
[dialog]
[charslot(slot = "m", focus = "n")]
[playsound(key="$phonevibration")]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1918_1#3$1")]
[name="萌萌香"]嗯？澪小姐？
[name="萌萌香"]嗯，我马上就到事务所了。有急事？
[stopmusic(fadetime=1)]
[charslot(slot="m",name="avg_npc_1918_1#8$1")]
[name="萌萌香"]什么？
[CameraShake(duration=-1, xstrength=5, ystrength=5, vibrato=15, randomness=90, fadeout=true, block=false)]
[playsound(key="$rungeneral")]
[charslot(slot="m",name="avg_npc_1918_1#18$1")]
[name="萌萌香"]我马上过去——跑着过去！
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[CameraShake(duration=0, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Background(image="62_g13_directorstudio",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[playMusic(intro="$sjoyasorrow_intro",key="$sjoyasorrow_loop", volume=0.6)]
[charslot(slot="m",name="avg_npc_1918_1#10$1")]
[name="萌萌香"]“把粉丝当傻瓜，鼻孔朝天”......
[name="萌萌香"]“再也不粉这个人了，演唱会搞得乱七八糟”......
[name="萌萌香"]“想炒热点想疯了，假装害怕不尬吗”......
[charslot(slot="m",name="avg_npc_1918_1#8$1")]
[name="萌萌香"]这......这怎么回事？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1901_1#13$1",duration=1.5)]
[delay(time=2)]
[name="澪"]舆论攻击。时间上，昨天凌晨开始。应该是竞争对手所为。
[Dialog]
[charslot]
[playsound(key="$dooropenquite")]
[charslot(slot="m",name="avg_npc_1257_1#1$1",duration=1)]
[delay(time=2)]
[charslot(slot="m",name="avg_npc_1901_1#13$1")]
[name="澪"]所长。
[charslot(slot="m",name="avg_npc_1918_1#18$1")]
[name="萌萌香"]所长，您亲自来了！
[charslot(slot="m",name="avg_npc_1257_1#1$1")]
[name="事务所所长"]情况怎么样了？
[charslot(slot="m",name="avg_npc_1901_1#13$1")]
[name="澪"]事发突然，公关还在查。
[charslot(slot="m",name="avg_npc_1257_1#1$1")]
[name="事务所所长"]不光是公关。
[charslot(slot="m",name="avg_npc_1901_1#1$1")]
[name="澪"]您的意思是？
[charslot(slot="m",name="avg_npc_1257_1#1$1")]
[name="事务所所长"]那个“独角的鬼”，可不是我们的人安排上去的，对不对？
[name="事务所所长"]澪，萌萌香的人身安全毕竟也是你负责，拜托你查清这件事了。
[charslot(slot="m",name="avg_npc_1901_1#1$1")]
[name="澪"]是。
[charslot(slot="m",name="avg_npc_1257_1#1$1")]
[name="事务所所长"]萌萌香，比起昨天舞台上的失态，“上面”更不满意的是另一件事。
[charslot(slot="m",name="avg_npc_1918_1#20$1")]
[name="萌萌香"]另一件事......？
[charslot(slot="m",name="avg_npc_1257_1#1$1")]
[name="事务所所长"]你最近的言行越来越不像是偶像该有的样子，事后竟然直接消失不见——
[charslot(slot="m",name="avg_npc_1918_1#20$1")]
[name="萌萌香"]当时粉丝好像并没有特别负面的反应，返场的时候我也额外多唱了一首，大家的反应还挺好的......
[name="萌萌香"]散场之后，我又累又饿，而且又害怕，就去了一趟常去的那个关东煮摊子。
[charslot(slot="m",name="avg_npc_1257_1#1$1")]
[name="事务所所长"]那你对演唱会上的不当发言又作何解释？
[charslot(slot="m",name="avg_npc_1918_1#10$1")]
[name="萌萌香"]不当发言？！我、我说错什么话了吗？
[charslot(slot="m",name="avg_npc_1901_1#1$1")]
[name="澪"]关于锻冶町的发言。
[charslot(slot="m",name="avg_npc_1918_1#10$1")]
[name="萌萌香"]锻冶町？哦，你是说那个粉丝——
[charslot(slot="m",name="avg_npc_1257_1#1$1")]
[name="事务所所长"]我们事务所的运营全靠金石集团的支持，现在锻冶町和集团关系紧张，你贸然表达自己的立场只会让我们所有人难办。
[charslot(slot="m",name="avg_npc_1918_1#1$1")]
[name="萌萌香"]我不了解其中的缘由......我原本只想着自己第一部电影是在那里拍的......
[name="萌萌香"]我还记得我最开始来到这的时候，你说是铁斋社长看中了我的能力......
[charslot(slot="m",name="avg_npc_1257_1#1$1")]
[name="事务所所长"]以前是以前，现在是现在。情况已经不一样了。
[name="事务所所长"]再说，我们一直告诉你，不要说越界的话，老老实实按照写好的台本念。人们想看的是萌萌香，不是乱说话的你。
[charslot(slot="m",name="avg_npc_1918_1#1$1")]
[name="萌萌香"]我......我明白了。
[charslot(slot="m",name="avg_npc_1901_1#3$1")]
[name="澪"]......
[charslot(slot="m",name="avg_npc_1257_1#1$1")]
[name="事务所所长"]你明白就好。
[charslot(slot="m",name="avg_npc_1918_1#1$1")]
[name="萌萌香"]所长......我们什么时候去录音棚？今天的日程挺满的，我得再努力一点。
[charslot(slot="m",name="avg_npc_1257_1#1$1")]
[name="事务所所长"]唉，算了。你要不还是先休息几天吧。
[charslot(slot="m",name="avg_npc_1918_1#10$1")]
[name="萌萌香"]欸？欸？！
[name="萌萌香"]所、所长，我没问题的！我已经调整好了！我知道最近工期很紧，现在休息的话，之后好几天的安排都会受影响！
[charslot(slot="m",name="avg_npc_1257_1#1$1")]
[name="事务所所长"]说不定你昨天白天少做点事，晚上还能镇定一点。
[charslot(slot="m",name="avg_npc_1918_1#1$1")]
[name="萌萌香"]抱歉！但是——
[charslot(slot="m",name="avg_npc_1257_1#1$1")]
[name="事务所所长"]萌萌香，你要是真愿意将功补过，这里有个现成的紧急工作交给你。
[charslot(slot="m",name="avg_npc_1918_1#10$1")]
[name="萌萌香"]我愿意的！
[charslot(slot="m",name="avg_npc_1257_1#1$1")]
[name="事务所所长"]这是电视台刚发来的节目邀请，你看看吧。
[charslot(slot="m",name="avg_npc_1918_1#18$1")]
[playsound(key="$d_avg_paper2")]
[name="萌萌香"]锻冶町......鬼屋探访？！怎么又是这样的节目！
[charslot(slot="m",name="avg_npc_1918_1#20$1")]
[name="萌萌香"]而且为什么偏偏要在这个时间节点，制作这种对锻冶町不利的节目......
[charslot(slot="m",name="avg_npc_1257_1#1$1")]
[name="事务所所长"]那你是想休息？
[charslot(slot="m",name="avg_npc_1918_1#1$1")]
[name="萌萌香"]不是！可......
[charslot(slot="m",name="avg_npc_1257_1#1$1")]
[name="事务所所长"]萌萌香，你应该明白，不听我们的，对你影响更大。
[stopmusic(fadetime=1)]
[charslot(slot="m",name="avg_npc_1918_1#21$1")]
[name="萌萌香"]我......
[charslot(slot="m",name="avg_npc_1257_1#1$1")]
[name="事务所所长"]萌萌香！
[dialog]
[charslot(slot="m",name="avg_npc_1918_1#21$1")]
[Delay(time=1.5)]
[playMusic(intro="$farce_intro",key="$farce_loop", volume=0.6)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_npc_1918_1#22$1")]
[name="萌萌香"]所长，我不想死啊！
[name="萌萌香"]我早就知道那是鬼屋，里面好像连着死过好几个人......
[name="萌萌香"]那个鬼屋据说还和“无名之鬼”有关系，昨天舞台上那个就是她......
[charslot(slot="m",name="avg_npc_1257_1#1$1")]
[name="事务所所长"]......
[charslot(slot="m",name="avg_npc_1901_1#13$1")]
[name="澪"]......
[charslot(slot="m",name="avg_npc_1257_1#1$1")]
[name="事务所所长"]呃，萌萌香，我们会给你做好安保措施的。
[name="事务所所长"]（小声）澪，你也表示一下。
[cha

... (全文27369字符)
```

### level_act44side_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="64_g5_kajistreet_d",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$m_dia_street_intro",key="$m_dia_street_loop", volume=0.6)]
[Delay(time=2)]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_1899_1#1$2",duration=1.5)]
[delay(time=2)]
[name="衣着洒脱的青年"]那边那位女士，我好像没在锻冶町见过你。你是哪位？
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[name="星熊"]有事吗？我家刚被一个陌生人折腾了一通，我要收拾一下。
[charslot(slot="m",name="avg_npc_1899_1#1$2")]
[name="衣着洒脱的青年"]你没听最近的新闻吗？北方有人偷越边境，好像进了御机。
[name="衣着洒脱的青年"]我叫反町哲也，是金石会的人。麻烦告诉我你是谁。锻冶町的人我都熟悉，可从来没见过你这么一号人物。
[charslot(slot="m",name="avg_136_hsguma_1#5$1")]
[name="星熊"]哲也？难道......
[name="星熊"]不，一定是我想多了。
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[name="星熊"]......
[name="星熊"]哲也，我是要回家。
[charslot(slot="m",name="avg_npc_1899_1#5$2")]
[name="哲也"]你家？别开玩笑了。知道这座凶宅什么来头吗？
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[name="星熊"]金石会一代目会长的家，也是他的诊疗所。他是金石会最好的医生，救过许多人的命。
[name="星熊"]他后来死了，这里就成了他女儿的家。
[charslot(slot="m",name="avg_npc_1899_1#1$2")]
[name="哲也"]难道你要冒充他女儿？
[charslot(slot="m",name="avg_npc_1899_1#7$2")]
[name="哲也"]等等......独角，这么高，这样的头发......你真的是星熊姐？
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[name="星熊"]星熊“姐”？哲也，你——
[charslot(slot="m",name="avg_npc_1899_1#5$2")]
[name="哲也"]——凶宅的怪谈真的和你有关？
[charslot(slot="m",name="avg_136_hsguma_1#7$1")]
[name="星熊"]我没有死，没有失踪，没有变成怪谈，我只是去了龙门。
[charslot(slot="m",name="avg_npc_1899_1#4$2")]
[name="哲也"]谁能证明你说的话？
[charslot(slot="m",name="avg_136_hsguma_1#7$1")]
[name="星熊"]去问铁斋叔。
[charslot(slot="m",name="avg_npc_1899_1#4$2")]
[name="哲也"]我和他没什么好说的。
[charslot(slot="m",name="avg_136_hsguma_1#7$1")]
[name="星熊"]哦，你是金兵卫那边的？那就去问他。别缠着我，我要回家祭奠父亲。
[charslot(slot="m",name="avg_npc_1899_1#4$2")]
[name="哲也"]跟我一起去见三船先生，解释清楚之后你就可以回来了。
[charslot(slot="m",name="avg_136_hsguma_1#7$1")]
[name="星熊"]恕不奉陪。
[charslot]
[PlaySound(key="$d_avg_scabbard")]
眼前的年轻人抽出腰间挂着的木刀，对星熊摆好了架势。
见年轻人举起的不过是木刀，星熊重重地叹了口气，把般若放下，徒手对着眼前的年轻人。
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[name="星熊"]我们以前见过？
[charslot(slot="m",name="avg_npc_1899_1#1$2")]
[name="哲也"]没有。
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[name="星熊"]还是说，你觉得靠一把木刀就能打赢我？
[charslot(slot="m",name="avg_npc_1899_1#1$2")]
[name="哲也"]......我听说过“金石会的青鬼”的故事。
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[name="星熊"]那你？
[dialog]
[charslot]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_1897_1#10$1",duration=1)]
[delay(time=1.5)]
[name="？？？"]哲也？你怎么又和人打起来了？上次你把人给惹了，差点闹到动真刀，你还没长教训？
[charslot(slot="m",name="avg_npc_1899_1#4$2")]
[name="哲也"]吉星，你别管。三船先生吩咐我的，让我最近留心陌生人。我得带这个人去三船先生那里。
[charslot(slot="m",name="avg_npc_1897_1#10$1")]
[name="吉星"]对面一看就不好惹，你怎么——
[dialog]
[charslot]
[charslot(slot="m",name="avg_136_hsguma_1#2$1",duration=0.5)]
[delay(time=1.5)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_npc_1897_1#6$1")]
[name="吉星"]你怎么连幽灵也要打呀！
[charslot(slot="m",name="avg_npc_1899_1#1$2")]
[name="哲也"]......
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[name="星熊"]......
[charslot(slot="m",name="avg_npc_1899_1#1$2")]
[name="哲也"]你认识她？
[charslot(slot="m",name="avg_npc_1897_1#4$1")]
[name="吉星"]昨晚萌萌香的演唱会上她突然出现，把萌萌香吓得半死。
[charslot(slot="m",name="avg_npc_1899_1#6$2")]
[name="哲也"]她真是幽灵？
[charslot(slot="m",name="avg_npc_1897_1#10$1")]
[name="吉星"]那倒不至于，哪有幽灵逃到最后被警察给逮捕的......难道说你越狱了？还是警察根本关不住你？
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[name="星熊"]我是被放出来的，谢谢！
[charslot(slot="m",name="avg_npc_1897_1#4$1")]
[name="吉星"]嗐，没劲。
[name="吉星"]哲也，你也冷静点，别再拿着三船那家伙的羽兽毛当令箭了。
[name="吉星"]我知道你讨厌你爸，你也不想住回那座大宅子，可你至少得有个姿态，免得锻冶町的大家见了你就像见了什么疫病神一样——
[charslot(slot="m",name="avg_npc_1899_1#5$2")]
[name="哲也"]吉星！
[charslot(slot="m",name="avg_npc_1897_1#3$1")]
[name="吉星"]......
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[name="星熊"]所以铁斋叔......续弦了？还给你取了和他以前的孩子同样的名字？
[name="星熊"]他......对你和你妈不好？
[charslot(slot="m",name="avg_npc_1899_1#5$2")]
[name="哲也"]以前我们俩还能吵起来的时候，我就问过他，为什么要娶妈。
[name="哲也"]他原来的老婆孩子和你亲爸一起被害了，他当成女儿来培养的你也不见了，他命里合该孤独终老，为什么还要来祸害我妈，祸害我？
[charslot]
星熊瞪着年轻人脸上也瞪着自己的面具，发觉他对着自己，不像是对一个强敌......
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[name="星熊"]唉。
[charslot(slot="m",name="avg_npc_1899_1#4$2")]
[name="哲也"]你叹什么气？
[charslot(slot="m",name="avg_136_hsguma_1#5$1")]
[name="星熊"]没什么，只是有点累了。
[charslot(slot="m",name="avg_npc_1899_1#5$2")]
[name="哲也"]少虚张声势了！
[dialog]
[charslot(slot = "m", posfrom = "0,0", posto = "50,0",duration = 1)]
[delay(time=1.5)]
[charslot(slot = "m", focus = "n")]
年轻人摆出标准的上段架势，试图从一个刁钻的角度欺近星熊。
[charslot(slot = "m", posfrom = "50,0", posto = "-300,0",duration = 0.6)]
[Dialog]
[PlaySound(key="$d_avg_clothmovementsp", volume=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.5)]
[charslot]
[Effect(name="$e_fist_01",x=240,y=-50,rox=-250,roy=150,roz=-240,layer = 2)]
[PlaySound(key="$d_avg_punchsp2",volume=0.7)]
[delay(time=0.3)]
[Effect(name="$e_fist_01",x=240,y=0,rox=50,roy=50,roz=-240,layer = 2)]
[PlaySound(key="$d_avg_punchsp5",volume=0.7)]
[delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[charslot(slot="m",name="avg_npc_1899_1#7$2",duration=0.1)]
[PlaySound(key="$bodyfalldown3", volume=1)]
[charslot(slot = "m", posfrom = "-250,0", posto = "0,-30",duration = 0.4)]
[delay(time=0.2)]
[CameraShake(duration=0.3, xstrength=15, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(duration=0.2)]
[name="哲也"]呃！
[dialog]
[delay(time=0.5)]
[charslot(slot="m",name="avg_npc_1899_1#7$2",duration=0.3)]
[charslot(slot ="m", action="shake", power=7, times=30, duration=0.5)]
[charslot(slot = "m",posfrom = "0,-60", posto = "0,0",duration = 1)]
[delay(time=1.5)]
[name="哲也"]这是什么......无刀取？！
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[name="星熊"]少看点漫画吧，这是最最基本的擒拿术。
[name="星熊"]冷静下来了吗？
[charslot(slot="m",name="avg_npc_1899_1#1$2",focus="n")]
年轻人没说话

... (全文19056字符)
```

### level_act44side_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="bg_oldwarehouse_n",screenadapt="coverall")]
[PlaySound(key="$d_avg_catfootstep", volume=1)]
[Delay(time=1.5)]
[name="星熊"]唔......
[Dialog]
[PlaySound(key="$d_avg_pawfootstep_3", volume=1)]
[Delay(time=1.5)]
[name="星熊"]谁？谁在这里？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[PlaySound(key="$d_avg_monocycle_bell", volume=0.5)]
[delay(time=2)]
[playMusic(key="$comedy_loop", volume=0.6)]
[charslot(slot="m",name="avg_136_hsguma_1#2$1",duration=1)]
[delay(time=2)]
[name="星熊"]车铃声？
[name="星熊"]（揉眼睛）这是梦？我还没醒？
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1904_1#1$3",duration=1.5)]
[delay(time=2.5)]
[charslot(slot = "m", focus = "n")]
明亮的月光下，杂物早已被收拾干净的地上，分明停着一辆小小的独轮车。
这东西就那么立在地上，没靠着任何东西，甚至都没处在平衡状态，是往一边歪着的。
[charslot(slot="m",name="avg_136_hsguma_1#10$1")]
[name="星熊"]怎么搞的......我喝多了？半瓶米酒，怎么可能？
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1904_1#1$3")]
[delay(time=1.5)]
[charslot(slot = "m", focus = "n")]
更诡异的是，假如真有什么看不见的东西骑在独轮车上，那么，这东西头上还戴着一顶比例完全合适的，小小的独轮车头盔。
但没人知道独轮车上面到底有没有“什么”，所以，在星熊看来，那顶头盔毫无疑问，正浮在半空中。
[charslot(slot="m",name="avg_136_hsguma_1#5$1")]
[name="星熊"]警察的窃听装置？金兵卫的把戏？铁斋叔？某种源石技艺？
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.7, block=true)]
[Background(image="64_g5_kajistreet_d",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[name="油滑的记者"]很多观众都认为青鬼的怪谈与轮入道的怪谈有关！许多青鬼的受害者都是在目睹轮入道之后遭遇不测，我想——
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[CameraEffect(effect="Grayscale", fadetime=0, amount=0, block=true)]
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[Background(image="bg_oldwarehouse_n",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[name="星熊"]......轮入道？怪谈是真的？
[name="星熊"]总之先拿起来看看吧——
[dialog]
[charslot]
[playsound(key="$d_avg_monocycle_fast_lp", loop=true, channel="bgs")]
[CameraShake(duration=1, xstrength=1, ystrength=0, vibrato=30, randomness=50, fadeout=true, block=false)]
[charslot(slot = "m", name = "avg_npc_1904_1#1$3",posfrom = "0,0", posto = "350,0",duration = 1,afrom=1,ato=0)]
[delay(time=0.5)]
[StopSound(channel="bgs", fadetime=0.5)]
[delay(time=1)]
和星熊弯腰同时，独轮车的脚蹬飞转起来，整辆车连同头盔嗖的一声窜了出去。
[charslot]
[charslot(slot="m",name="avg_136_hsguma_1#9$1")]
[name="星熊"]等等——站住！
[playsound(key="$rungeneral")]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot]
[Delay(time=1)]
[Background(image="64_g18_kajistreet_n",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Delay(time=0.5)]
[CameraShake(duration=-1, xstrength=1, ystrength=0, vibrato=20, randomness=50, fadeout=false, block=false)]
[playsound(key="$d_avg_monocycle_fast_lp", loop=true, channel="bgs",volume=0.5)]
[charslot(slot = "m", name = "avg_npc_1904_1#1$3",duration = 0.3)]
[charslot(slot = "m",posfrom = "0,0", posto = "-100,0",duration = 0.5)]
[Delay(time=1)]
[charslot(slot = "m",posfrom = "-100,0", posto = "150,0",duration = 0.7)]
[Delay(time=1)]
[charslot(slot = "m", focus = "n")]
独轮车在前面飞驰，星熊跟在后面穷追不舍。
她清清楚楚地看见，脚蹬带动车轮，上面的小头盔有规律地一上一下......
怎么看都像是有个看不见的东西在骑车。拐弯时独轮车的脚蹬在地上蹭了一下，甚至还溅起几星火花。
[StopSound(channel="bgs", fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[CameraShake(duration=0, xstrength=1, ystrength=1, vibrato=30, randomness=90, fadeout=false, block=false)]
[Delay(time=2)]
[Background(image="64_g15_higashiroom",screenadapt="coverall")]
[playsound(key="$d_avg_doorknob")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playsound(key="$d_avg_sit_tatami")]
[CameraShake(duration=0.3, xstrength=5, ystrength=10, vibrato=5, randomness=90, fadeout=true, block=false)]
萌萌香整个身子一软，倒在榻榻米上。
[charslot(slot="m",name="avg_npc_1918_1#1$1")]
[name="萌萌香"]......根本睡不着。
[charslot(slot="m",name="avg_npc_1918_1#3$1")]
[name="萌萌香"]明天早上要不去一趟事务所吧......
[name="萌萌香"]先好好认个错，态度诚恳一点......实在不行就再多接一点工作，澪小姐会原谅我——
[charslot]
[dialog]
[playsound(key="$d_avg_largebell",volume=0.5)]
[Delay(time=1)]
[CameraShake(duration=0.2, xstrength=20, ystrength=20, vibrato=20, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_npc_1918_1#10$1")]
[name="萌萌香"]噫！
[charslot(slot="m",name="avg_npc_1918_1#9$1")]
[name="萌萌香"]是、是钟声啊......
[charslot(slot="m",name="avg_npc_1918_1#7$1")]
[name="萌萌香"]还是开着灯和电视睡吧......
[charslot]
[playsound(key="$d_avg_oldtvelectricity")]
萌萌香膝行到电视前面，按下开关。
吵闹、夸张、做作，然而就像御机本身一样令人安心的广告声响了起来。
[charslot(slot="m",name="avg_npc_1918_1#4$1")]
[name="萌萌香"]今晚就先......睡吧。
[stopmusic(fadetime=2)]
[dialog]
[playsound(key="$d_avg_clothmovement")]
[charslot(duration=1)]
[Delay(time=2)]
[playsound(key="$d_avg_oldtvelectricity", loop=true, channel="bgs",volume=1)]
[name="电视里的声音"]......安心与安定的，御机联合人寿。
[name="电视里的声音"]（音乐声）
[name="电视里的声音"]观众朋友们大家好，欢迎收看金石台的午夜新闻，现在是凌晨一点三十分......
[name="萌萌香"]快到丑时三刻了......幽灵最活跃的时间段......呜......
[name="电视里的声音"]......与北院联合制定的计划受阻......
[name="电视里的声音"]......暴雨袭击谏崎城，农业地块受灾情况可控......
[name="电视里的声音"]......接下来让我们关注受人瞩目的御机娱乐产业......
[dialog]
[StopSound(channel="bgs", fadetime=1)]
[Delay(time=1)]
[playsound(key="$d_avg_airdefensealert", loop=true, channel="a",volume=0)]
[SoundVolume(volume=0.4, channel="a",fadetime=2)]
[name="电视里的声音"]（刺耳的警报声）
[dialog]
[playMusic(intro="$suspenseful_intro",key="$suspenseful_loop", volume=0.6)]
[playsound(key="$d_avg_clothmovement")]
[charslot(slot="m",name="avg_npc_1918_1#18$1",posfrom = "0,-80", posto = "0,0",duration = 0.5)]
[Delay(time=1)]
[name="萌萌香"]怎、怎么了？出什么事了？地震？天灾？！
[charslot(slot = "m", focus = "n")]
[dialog]
[StopSound(channel="a", fadetime=1)]
[Delay(time=1)]
[playsound(key="$transmission")]
[name="电视里的声音"]（信号干扰声）
[name="电视里的声音"]——况速报，紧急情况速报。这不是演习，这不是演习。
[name="电视里的声音"]......目前正遭到北院军队的全面攻击——遭到北院军队的全面攻击——
[name="电视里的声音"]为了您的人身安全，请遵守以下指示——
[name="电视里的声音"]（刺耳的不明声音）
[charslot(slot="m",name="avg_

... (全文16280字符)
```

### level_act44side_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="64_g11_odenstall",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playMusic(key="$calm_loop", volume=0.6)]
[charslot(slot="m",name="avg_136_hsguma_1#2$1",duration=0.5)]
[Delay(time=1)]
[name="星熊"]神明？
[charslot(slot="m",name="avg_4199_makiri_1#1$1")]
[name="森内"]没错。在我看来，御机大大小小的怪谈，都可以用“神明大人作祟”解释。而我要找的，就是无数神明中的一位。
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[name="星熊"]......
[charslot(slot="m",name="avg_4199_makiri_1#1$1")]
[name="森内"]看来你是不相信的了。
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[name="星熊"]鬼族多少还是和寺院更亲近些。
[name="星熊"]再说，我也很难想象哪位神明大人有那么闲，骑着独轮车诅咒我家房子。
[charslot(slot="m",name="avg_4199_makiri_1#1$1")]
[name="森内"]哈哈，大多数鬼族都像你这么想。
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[name="星熊"]你为什么要找“神明大人”？觉得自己被某位神明作祟了？
[charslot(slot="m",name="avg_4199_makiri_1#1$1")]
[multiline(name="森内")]恰恰相反，祂帮过我很大的忙。
[charslot(slot="m",name="avg_4199_makiri_1#2$1")]
[multiline(name="森内")]可不知从哪一天开始，祂不见了。
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[name="星熊"]就是刚刚那个“轮入道”？
[charslot(slot="m",name="avg_4199_makiri_1#2$1")]
[name="森内"]有可能，但我没法确定，毕竟我也看不见那辆独轮车上坐着的神明究竟长什么样。
[name="森内"]所以能不能请你帮我个忙？
[name="森内"]假如你追上了祂，甚至......有幸目睹祂的身姿，麻烦帮我确认一下，祂的长相是否与此类似。
[playsound(key="$d_avg_key")]
[charslot(slot = "m", focus = "n")]
森内从口袋里掏出一串钥匙，上面挂着一枚小小的钥匙扣。
[charslot]
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[name="星熊"]招财猫？这不就是东国菲林照着兽亲的样子刻画出来的吉祥物吗？
[charslot(slot="m",name="avg_4199_makiri_1#1$1")]
[name="森内"]我遇见的神明，除了大小，几乎和它别无二致。
[name="森内"]星熊小姐，既然你不是幽灵，那你追逐轮入道，想必也是想知道自己的老宅里究竟发生了什么，对不对？
[charslot(slot="m",name="avg_136_hsguma_1#7$1")]
[name="星熊"]......
[name="星熊"]森内老板，我可没对你做过自我介绍。
[name="星熊"]你是金石会的人？
[charslot(slot="m",name="avg_4199_makiri_1#1$1")]
[name="森内"]（摇头）不是。金石会的人怎么会跑到这里来摆摊呢。
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[name="星熊"]警方的线人？
[charslot(slot="m",name="avg_4199_makiri_1#10$1")]
[name="森内"]（摇头）那我真是不要命了。
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[name="星熊"]情报贩子。
[charslot(slot="m",name="avg_4199_makiri_1#1$1")]
[name="森内"]（不点头也不摇头）
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[name="星熊"]哈，也是，哪个情报贩子会承认自己是干这行的呢。
[name="星熊"]既然是生意，拜托我帮你做事，却只字不提回报，这可不太好吧？
[charslot(slot="m",name="avg_4199_makiri_1#1$1")]
[name="森内"]哈哈，那星熊小姐究竟要什么回报？如果是情报，我可以知无不言。
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[name="星熊"]不忙，等我知道自己需要什么情报的时候再说。
[name="星熊"]有什么说了会惹来杀身之祸的东西吗？这种东西最好提前跟我打好招呼，临时现讲，我可不会答应。
[charslot(slot="m",name="avg_4199_makiri_1#4$1")]
[name="森内"]......
[name="森内"]不，如果你真能帮我找到有用的线索，我没什么不能说的。
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[name="星熊"]一言为定？
[charslot(slot="m",name="avg_4199_makiri_1#2$1")]
[name="森内"]一言为定。
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[name="星熊"]好了，接下来我该去哪找那位轮入道？神社？
[name="星熊"]可别忘了，我们脚下这座城市就叫“南院行在御机大社”，总不至于让我把这里所有的神社都跑一遍吧？
[charslot(slot="m",name="avg_4199_makiri_1#1$1")]
[name="森内"]怎么会呢。知道俗称“结缘的神社”的那一间吗？
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[name="星熊"]略有耳闻。
[name="星熊"]不过，既然你知道得这么清楚，为什么不自己去？
[charslot(slot="m",name="avg_4199_makiri_1#1$1")]
[name="森内"]神明是很随心所欲的。祂们愿意在一些人面前现身，在另一些人面前却无论如何都不愿被看到。
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[name="星熊"]原来你是“另一类人”？
[charslot(slot="m",name="avg_4199_makiri_1#3$1")]
[name="森内"]自从那位神明离我而去之后，我就一直是了。
[dialog]
[charslot]
[playsound(key="$rungeneral", loop=true, channel="bgs")]
[delay(time=1)]
[StopSound(channel="bgs", fadetime=1)]
[charslot(slot="m",name="avg_npc_1918_1#18$1",duration=0.5)]
[delay(time=1)]
[name="萌萌香"]老板！我的电动车坏了，你快帮我修一下，有人在追我！
[dialog]
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[delay(time=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_npc_1918_1#10$1")]
[name="萌萌香"]噫！怎么是你？
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[name="星熊"]......还在把我当幽灵？
[charslot(slot="m",name="avg_npc_1918_1#7$1")]
[name="萌萌香"]原来你、你不是幽灵吗......
[charslot(slot="m",name="avg_136_hsguma_1#4$1")]
[name="星熊"]唉。
[charslot(slot="m",name="avg_4199_makiri_1#8$1")]
[name="森内"]萌萌香？怎么慌成这样？
[charslot(slot="m",name="avg_npc_1918_1#10$1")]
[name="萌萌香"]有人在追我！我骑着电动车好容易甩掉他们，可骑到这附近车就出故障了，麻烦你帮我修一修！
[charslot(slot="m",name="avg_4199_makiri_1#8$1")]
[name="森内"]谁在追你？
[charslot(slot="m",name="avg_npc_1918_1#20$1")]
[name="萌萌香"]是、是澪小姐......
[charslot(slot="m",name="avg_4199_makiri_1#1$1")]
[name="森内"]澪？那我劝你乖乖跟她回去。热量又超标了？
[charslot(slot="m",name="avg_npc_1918_1#18$1")]
[name="萌萌香"]不是，她是要......要处理我！
[name="萌萌香"]我家电视晚上突然坏了，放了很多可怕的东西！
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="萌萌香"]还有她和三船先生聊天！他们说——不是处理，就是矿石病！帮帮我！
[charslot]
萌萌香语无伦次起来。
森内还没动作，星熊已经走到电动车旁边。
[charslot(slot="m",name="avg_136_hsguma_1#7$1")]
[name="星熊"]处理？矿石病？萌萌香小姐，你惹到他们了？
[charslot(slot="m",name="avg_npc_1918_1#18$1")]
[name="萌萌香"]我只是发了个帖子，我没想做什么，也不是什么勾结铁斋！
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[name="星熊"]勾结铁斋？
[charslot(slot="m",name="avg_136_hsguma_1#5$1")]
[name="星熊"]......
[name="星熊"]我看看这车怎么修。
[charslot(slot="m",name="avg_4199_makiri_1#1$1")]
[name="森内"]你要不还是先追轮入道去？
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[name="星熊"]还要装听不懂吗，情报贩子先生？
[name="星熊"]再说我已经两次吓到这位萌萌香小姐了。现在她有麻烦，我也该做点力所能及的事，就当是还人情了。
[name="星熊"]萌萌香小姐，我可以保证，只要有我在，你就不会有事。
[charslot(slot="m",name="avg_npc_1918_1#1$1")]
[name="萌萌香"]谢谢......
[dialog]
[stopmusic(fadetime=2)]
[charslot(slot="m",name="avg_npc_1918_1#10$1")]
[Delay(time=1)]
[name="萌萌香"]——仁田街那边是不是有人跑过来了！他们是来追我的吗？
[charslot(slot="m",name="avg_4199_makiri_1#2$1")]
[name="森内"]金石会的打扮......看样子还真是。
[charslot(slot="m",name="avg_npc_1918_1#10$1")]
[name="萌萌香"]老板！幽灵小姐！救我！
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[name="星熊"]幽灵小姐？我？
[charslot(slot="m",name="avg_npc_1918_1#20$1")]
[name="萌萌香"]抱歉，可我也不知道你叫什么......
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[name="星熊"]不管怎么说，你的车修好了。
[name="星熊"]你骑车，其余的事情交给我。
[charslot(slot="m",name="avg_np

... (全文24085字符)
```

### level_act44side_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[curtain(direction = 0,fillfrom = 0.1,fillto = 0.15, fadetime=0.1)]
[bgeffect(name = "$eb_speedline" ,layer = 1)]
[focusout(duration=1, type="bg", from=0, to=0.8, block=true)]
[curtain(direction = 4,fillfrom = 0.1,fillto = 0.15, fadetime=0.1)]
[playsound(key="$d_avg_electricbicycle_fast", loop=true, channel="bgs",volume=0.2)]
[CameraShake(duration=-1, xstrength=0.5, ystrength=0.5, vibrato=20, randomness=50, fadeout=false, block=false)]
[Background(image="64_g2_jindastreet_n",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playMusic(key="$darkness_03_loop", volume=0.6)]
[name="星熊"]刚刚的新闻是怎么回事？
[name="萌萌香"]我——我不知道！
[name="星熊"]金兵卫以前也主持节目吗？
[name="萌萌香"]金兵卫？
[name="星熊"]就是三船。
[name="萌萌香"]那是我很小的时候的事了，我也记不太清。
[name="萌萌香"]听所长说，当年金石台草创阶段，什么节目都得三船顶着，新闻播报，综艺节目......有时候连天气预报都要他客串去播。
[name="萌萌香"]这么说来，我还帮金石台报过好长时间的天气预报呢。
[name="萌萌香"]再后来，金石台越做越大，他就只播重要新闻，再后来连新闻也不播，整个人都退居幕后了。
[name="星熊"]那他现在究竟是要——
[StopSound(channel="bgs", fadetime=1.5)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot]
[curtain]
[focusout(duration=0.1, type="bg", from=0.8, to=0, block=true)]
[bgeffect(layer = 1)]
[Delay(time=0.25)]
[CameraShake(duration=0, xstrength=0.5, ystrength=0.5, vibrato=20, randomness=50, fadeout=false, block=false)]
[charslot(slot = "left", name = "avg_npc_1911_1#1$1")]
[charslot(slot = "right", name = "avg_npc_1912_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Delay(time=0.5)]
[charslot(slot = "left",focus="l")]
[name="眼尖的路人"]你看那边的摩托车上！
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "left",focus="r")]
[name="浮躁的路人"]青鬼？！
[name="浮躁的路人"]青鬼真的和萌萌香在一起！
[name="浮躁的路人"]怎么说，把她们拦下来？
[charslot(slot = "left",focus="l")]
[name="眼尖的路人"]你不要命了！发消息，联系电视台的人啊！
[name="眼尖的路人"]你看她哭成那个样子，肯定是被青鬼给挟持了......说不定是被精神控制了！
[charslot(slot = "left",focus="r")]
[name="浮躁的路人"]你联系电视台，我去报警。
[charslot(slot = "left",focus="l")]
[name="眼尖的路人"]警察不是发了好几回公告，说不要把警察局当灵务局，怪谈相关的事别找他们了吗？
[charslot(slot = "left",focus="r")]
[name="浮躁的路人"]倒也是。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot]
[bgeffect(name = "$eb_speedline" ,layer = 1)]
[focusout(duration=1, type="bg", from=0, to=0.8, block=true)]
[curtain(direction = 0,fillfrom = 0.1,fillto = 0.15, fadetime=0.1)]
[curtain(direction = 4,fillfrom = 0.1,fillto = 0.15, fadetime=0.1)]
[playsound(key="$d_avg_electricbicycle_fast", loop=true, channel="bgs",volume=0.2)]
[CameraShake(duration=-1, xstrength=0.5, ystrength=0.5, vibrato=20, randomness=50, fadeout=false, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[name="星熊"]啧，我们该加速了。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[Background(image="bg_wild_a",screenadapt="coverall")]
[playsound(key="$d_avg_electricbicycle_speedup")]
萌萌香已经开得尽可能快，星熊却仍觉得眼前的景色不过是某种巨大的循环。
霓虹灯，路人，高楼大厦，十字路口。霓虹灯，路人，高楼大厦，十字路口——
[dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0.3, r=0, g=0, b=0, fadetime=2, block=true)]
某个瞬间过后，这样的循环忽然中断，她的视线里开始出现像锻冶町那样古旧的街区，而后连建筑的数量都变得稀少。
再后来，她们开过成片的荒地，有的有开工的痕迹，有的干脆就只是荒废的地块。
天色渐明。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2,block=true)]
[name="萌萌香"]星熊小姐，目的地就在前面了。
[name="星熊"]好的——等下，该减速了——要冲进去了！
[name="萌萌香"]欸？！
萌萌香猛地踩下刹车踏板，然而已经来不及了——
[Dialog]
[StopSound(channel="bgs", fadetime=0.5)]
[PlaySound(key="$drift", volume=1)]
[CameraShake(duration=1.5, xstrength=6, ystrength=3, vibrato=20, randomness=90, fadeout=false, block=false)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot]
[curtain]
[focusout(duration=0.1, type="bg", from=0.8, to=0, block=true)]
[bgeffect(layer = 1)]
[Delay(time=2)]
[Background(image="64_g7_jinja_indoor",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Delay(time=1)]
[playMusic(key="$ouat_loop", volume=0.6)]
摩托车风驰电掣地开进神社，一直开到庭园中央才停下来。多亏萌萌香的平衡保持得不错，两个人才没有摔车。
[Dialog]
[charslot(slot = "left", name = "avg_136_hsguma_1#2$1",duration = 1)]
[charslot(slot = "right", name = "avg_npc_1918_1#1$1",duration = 1)]
[delay(time=1.5)]
[charslot(slot = "right", name = "avg_npc_1918_1#1$1",focus="r")]
[name="萌萌香"]糟了，我们这算不算对神社不敬啊......
[dialog]
[charslot]
[playsound(key="$rungeneral", loop=true, channel="bgs",volume=0.5)]
[delay(time=1)]
[StopSound(channel="bgs", fadetime=1.5)]
[name="女性神职的声音"]宫司大人，宫司大人！又有女人杀进来了！这次还骑在摩托车上！
[name="男性神职的声音"]又来？！
[name="女性神职的声音"]这次不知道为什么没人拦着，她们一路畅通无阻就进来了，一直开到庭园正中央！
[name="沉稳的声音"]“她们”？
[name="沉稳的声音"]你确定车上是沃尔珀？
[name="女性神职的声音"]呃......
[name="男性神职的声音"]宫司大人，哪是什么沃尔珀，是一个阿戈尔和一个鬼。
[name="女性神职的声音"]这次的场景和上次实在有点像，我太慌张，没看清人，抱歉......
[name="沉稳的声音"]关心则乱，这不怪你。
[name="沉稳的声音"]不管来客究竟是谁，我去接待就好。你们放心做自己的事。
[dialog]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_1902_1#2$1",duration=1.5)]
[delay(time=2.5)]
[charslot(slot = "m", name = "avg_npc_1918_1#1$1")]
[name="萌萌香"]宫司大人对不起！我不是故意的！我真的就是太紧张了忘记踩刹车——
[charslot(slot="m",name="avg_npc_1902_1#1$1")]
[name="沉稳的神职"]我还当是谁呢，这不是萌萌香小姐吗？
[charslot(slot = "m", name = "avg_npc_1918_1#1$1")]
[name="萌萌香"]宫、宫司大人......
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[name="星熊"]呃，你们认识？
[charslot(slot="m",name="avg_npc_1902_1#1$1")]
[name="沉稳的神职"]萌萌香小姐以前是常来这里的。五年前她来了最后一次之后就不再光顾，可能是愿望都已满足，生活已经非常幸福了吧。
[charslot(slot = "m", name = "avg_npc_1918_1#1$1")]
[name="萌萌香"]其实也没有啦......只是从那个时候开始，我越来越忙，忙到连来神社的时间都没有了。
[charslot(slot="m",name="avg_npc_1902_1#12$1")]
[name="沉稳的神职"]不必消沉。这里本来就是结缘的神社，萌萌香小姐事业有成，想必不会缺少人与人之间的缘分与纽带。
[charslot(slot = "m", name = "avg_npc_1918_1#1$1")]
[name="萌萌香"]呜......
[charslot(slot="m",name="avg_npc_1902_1#1$1")]
[name="沉稳的神职"]萌萌香小姐身边这位，不知该如何称呼？
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[name="星熊"]我叫星熊，来找一个人。
[charslot(slot="m",name="avg_npc_1902_1#1$1")]
[name="沉稳的神职"]不知您找哪位？在本社任职的神职并不太多。
[charslot(slot="m",name="avg_136_hsguma_1#7$1")]
[name="星熊"]我不是来找神职的，我是替人前来，寻找一位“神明大人”。
[name="星熊"]更确切地说，我来找的是一辆看不见驾驶人的独轮车，据说御机有不

... (全文22297字符)
```

### level_act44side_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="64_g6_gokudouoffice",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playMusic(intro="$loading_intro",key="$loading_loop", volume=0.6)]
[charslot(slot = "left", name = "avg_npc_1896_1#1$1",duration = 1)]
[charslot(slot = "right", name = "avg_npc_1901_1#13$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "right", name = "avg_npc_1901_1#13$1",focus="r")]
[name="澪"]三船先生。
[charslot(slot = "left", name = "avg_npc_1896_1#1$1",focus="l")]
[name="三船"]交待你办的事怎么样了？
[charslot(slot = "right", name = "avg_npc_1901_1#13$1",focus="r")]
[name="澪"]议员大人终于首肯金石集团和金石会的剥离了。
[name="澪"]只要您现在接过会长的位置，金石会就可以和金石集团彻底分离。
[charslot(slot = "left", name = "avg_npc_1896_1#1$1",focus="l")]
[name="三船"]呵，那不如就把继位仪式和明晚的花火大会同时办了，你觉得怎么样？
[charslot(slot = "right", name = "avg_npc_1901_1#1$1",focus="r")]
[name="澪"]铁斋那边的态度没变，现在甚至多了星熊作为助力，我们真的能在一天之内......
[charslot(slot = "left", name = "avg_npc_1896_1#1$1",focus="l")]
[name="三船"]能。
[name="三船"]你眉头微微跳了一下。我知道你在想什么。你知道我不在这种事上开玩笑，又对我没信心。归根结底......
[charslot(slot = "left", name = "avg_npc_1896_1#1$1",focus="l")]
[name="三船"]觉得我没必要让你仿老东西的笔迹，把星熊叫回来徒增麻烦，是不是？
[charslot(slot = "right", name = "avg_npc_1901_1#3$1",focus="r")]
[name="澪"]......
[charslot(slot = "left", name = "avg_npc_1896_1#2$1",focus="l")]
[name="三船"]二十多年前，星熊手里那面盾引发了不少血雨腥风。毕竟是老东西的最后一作......澪，你去过他家吗？
[charslot(slot = "right", name = "avg_npc_1901_1#13$1",focus="r")]
[name="澪"]好多年前了。
[charslot(slot = "left", name = "avg_npc_1896_1#1$1",focus="l")]
[name="三船"]他家最多的是什么？
[charslot(slot = "right", name = "avg_npc_1901_1#13$1",focus="r")]
[name="澪"]电视。
[charslot(slot = "left", name = "avg_npc_1896_1#1$1",focus="l")]
[name="三船"]对，电视。
[name="三船"]老家伙迂腐不假，但他的嗅觉偶尔也很灵敏。
[name="三船"]他知道金石会如果永远那么打打杀杀下去，总有一天会彻底完蛋。所以，他盯上了源石晶体元件。
[name="三船"]触类旁通，他家打金属的工坊很快变成了制作晶体元件的作坊，然后一炮打响。这下老家伙没工夫打他最喜欢的神兵利器了。
[name="三船"]就在晶体产业蒸蒸日上的时候，老家伙忽然从光元一系的破落公家那里淘到了铸盾的材料和工艺。
[name="三船"]据说为了那些材料和工艺，他用了组里当时将近一半的流动资金。
[charslot(slot = "left", name = "avg_npc_1896_1#6$1",focus="l")]
[name="三船"]你觉得，对当时的金石会来说，一面这么大来头，而且几乎可以肯定是他最后一作的盾，意味着什么？
[charslot(slot = "right", name = "avg_npc_1901_1#13$1",focus="r")]
[name="澪"]......传位。
[charslot(slot = "left", name = "avg_npc_1896_1#1$1",focus="l")]
[name="三船"]连你都知道的事，老家伙却给搁下了。他就那么拖着，拖着，一直拖到南院的第一届议会都要开选了。
[name="三船"]对你们这辈人来说，你们早都习惯议会这东西了。可对当时的我们来说，没人知道那是什么。
[name="三船"]一开始我们以为他们是要改官制，但那是他们几年后才做的事。
[name="三船"]我们那时只听说，“议员”是要从平民中选的。这下整个南院都轰动了起来......然后，那个姓惟任的倒霉蛋就跳了出来。
[charslot(slot = "right", name = "avg_npc_1901_1#13$1",focus="r")]
[name="澪"]......那位议员候选人？
[charslot(slot = "left", name = "avg_npc_1896_1#1$1",focus="l")]
[name="三船"]是啊。他当时的政见一大堆，核心却是要把我们金石会从锻冶町赶出去。
[name="三船"]他甚至纠结了一帮乌合之众，每天在我们锻冶町外面吵吵嚷嚷，让我们做不成生意。
[charslot(slot = "left", name = "avg_npc_1896_1#3$1",focus="l")]
[name="三船"]老东西——不，不光老东西，整个金石会一开始没把他当回事，直到他的人越来越多，越来越多。
[charslot(slot = "right", name = "avg_npc_1901_1#1$1",focus="r")]
[name="澪"]所以......您决定除掉他。
[charslot(slot = "left", name = "avg_npc_1896_1#1$1",focus="l")]
[name="三船"]是啊。后面的事，你也都知道了。那个议员候选人死了之后，金石会才领教了什么叫做民意汹汹。
[name="三船"]也是在那之后，我才明白，尽管在四大家族面前，议员只是拿来装点门面的花瓶......
[name="三船"]但对我们这些人而言，议员的一句话，一点头，往往就能决定我们的生和死。
[charslot(slot = "right", name = "avg_npc_1901_1#1$1",focus="r")]
[name="澪"]......恕我直言，您其实可以直接告诉我，如果铁斋会长不从，您在继位仪式上需要般若。
[charslot(slot = "left", name = "avg_npc_1896_1#9$1",focus="l")]
[name="三船"]我真得说，你有时候还挺像铁斋的。
[name="三船"]当然，铁斋骑在我头上是一回事，像你这样忠心耿耿、知无不言，那又是另一回事。
[charslot(slot = "left", name = "avg_npc_1896_1#1$1",focus="l")]
[name="三船"]说真的，金石集团和金石会剥离之后，我自然不能再当这个金石会的会长。除了你，会里还有第二个能接我班的人吗？
[charslot(slot = "right", name = "avg_npc_1901_1#13$1",focus="r")]
[name="澪"]......
[charslot(slot = "left", name = "avg_npc_1896_1#9$1",focus="l")]
[name="三船"]等我进入政界，有了自己的一方势力的那一天，自然也不会亏待你和你的金石会的。
[charslot(slot = "m", focus = "n")]
三船自顾自地大笑起来。
而他眼前的女性仍然面无表情，不知道她究竟是习惯了如此，是不敢相信自己听见了什么，还是对远大的未来无动于衷。
[charslot(slot = "left", name = "avg_npc_1896_1#1$1",focus="l")]
[name="三船"]至于现在，我们的第一要务，仍然是萌萌香。
[name="三船"]她实在知道太多东西了，而且还和那个情报贩子搭上了线。
[charslot(slot = "left", name = "avg_npc_1896_1#6$1",focus="l")]
[name="三船"]她为了把佐野口的断刀留在身上，甚至不惜跳窗逃跑，这意味着什么，你还不明白吗？
[charslot(slot = "right", name = "avg_npc_1901_1#10$1",focus="r")]
[name="澪"]三船先生——
[charslot(slot = "left", name = "avg_npc_1896_1#1$1",focus="l")]
[name="三船"]你不忍心，而且愿意对我说，这很好。我也可以答应你，让她得矿石病的事可以再考虑考虑。
[charslot(slot = "left", name = "avg_npc_1896_1#6$1",focus="l")]
[name="三船"]但是，首先，你得把她给我抓回来。
[name="三船"]她手里的断刀，上面的刀镡无论如何都要回收。
[name="三船"]其次，她这个艺人无论如何不可能再当下去。她未来必须处在我们的严密掌控之下。
[name="三船"]这样你满意了吗？
[charslot(slot = "right", name = "avg_npc_1901_1#2$1",focus="r")]
[name="澪"]多谢您的宽宏大量。
[charslot(slot = "left", name = "avg_npc_1896_1#1$1",focus="l")]
[name="三船"]等你把她抓来，还是让她谢谢你吧。
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[Background(image="64_g7_jinja_indoor",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[playMusic(key="$normal_loop", volume=0.6)]
太阳缓缓爬上头顶。
尽管没有其他访客，但庭园中有了四个人和一个神明的身影，也就不再显得那么空旷安静。
吉星拿出身上能写字的一切让萌萌香签名，萌萌香被猛烈的攻势吓了一跳，但签名的手速一点也不慢。
庭院另一边，宫司怀里抱着刚刚那位左冲右突的神明，正和星熊说着什么。
[dialog]
[charslot(slot="m",name="avg_npc_1902_1#1$1",duration=1)]
[delay(time=2)]
[name="沉稳的神职"]刚刚毕竟也是神明大人要与人游戏，我作为神职，自然也只能旁观，不好插手，还请星熊小姐见谅。
[dialog]
[charslot]
[playsound(key="$d_avg_monocycle_bell")]
[charslot(slot="m",name="avg_npc_1904_1#1$2",duration=1)]
[delay(time=1.5)]
[name="好事的神明"]你自己不也看得挺开心？
[charslot(slot="m",name="avg_npc_1902_1#1$1")]
[name="沉稳的神职"]有吗？
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[name="星熊"]我觉得有。
[charslot(slot="m",name="avg_npc_1902_1#12$1")]
[name="沉稳的神职"]诚心诚意侍奉神明，自然会让人心情愉悦。星熊小姐和萌萌香小姐刚刚不也一样？
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[name="星熊"]我还是更关心祂为什么半夜闯入我家。
[charslot(slot="m",name="avg_npc_1904_1#1$2")]
[name="好事的神明"]什么叫“半夜闯入”，说得我好像什么危险分子似的。突然有人在凶宅里收垃圾倒垃圾，还躺在那里睡觉，换做是你，不会觉得奇怪吗？
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[name="星熊"

... (全文17554字符)
```

### level_act44side_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="64_g11_odenstall",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playMusic(key="$calm_loop", volume=0.6)]
[PlaySound(key="$d_avg_electricbicycle_speedup", volume=0.6)]
[charslot(slot = "left", name = "avg_136_hsguma_1#2$1",duration = 1)]
[charslot(slot = "right", name = "avg_npc_1918_1#1$1",duration = 1)]
[delay(time=2.5)]
[charslot]
[charslot(slot="m",name="avg_4199_makiri_1#1$1",duration=1)]
[delay(time=1.5)]
[name="森内"]星熊小姐，还有萌萌香？
[name="森内"]先吃点东西垫垫肚子？还是说我拜托二位的事情这么快就有结果了？
[charslot(slot="m",name="avg_npc_1918_1#1$1")]
[name="萌萌香"]吃、吃东西就不必了......一路骑到这里，我觉得自己喝了好多风......
[charslot(slot="m",name="avg_4199_makiri_1#11$1")]
[name="森内"]金石会的人还在追你们？
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[name="星熊"]多亏神明大人点拨，再加上我们特意挑了人迹罕至的路线，回来的路还算顺畅。
[charslot(slot="m",name="avg_4199_makiri_1#8$1")]
[name="森内"]神明大人......难道说？！
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[name="星熊"]别高兴太早。虽然的确是神明大人，可并不是你要找的那位。
[charslot(slot="m",name="avg_4199_makiri_1#1$1")]
[name="森内"]......没关系，没关系！
[dialog]
[charslot]
[playsound(key="$d_avg_monocycle_bell")]
[charslot(slot="m",name="avg_npc_1904_1#1$2",duration=1)]
[delay(time=2)]
[name="好事的神明"]真没关系？
[charslot(slot="m",name="avg_4199_makiri_1#8$1")]
[name="森内"]您、您是......？
[charslot(slot="m",name="avg_npc_1904_1#1$2")]
[name="好事的神明"]看，我就说嘛。
[charslot(slot="m",name="avg_4199_makiri_1#8$1")]
[multiline(name="森内")]不，不不！小店没什么能招待您的，您看要不要......来点关东煮汤暖暖身子——
[charslot(slot="m",name="avg_4199_makiri_1#13$1")]
[multiline(name="森内")]不对，所有的关东煮随您挑！
[charslot(slot="m",name="avg_npc_1904_1#1$2")]
[name="好事的神明"]我可不像某些家伙，对你做的关东煮那么上心。
[charslot(slot="m",name="avg_4199_makiri_1#1$1")]
[name="森内"]神明大人，不知您——
[charslot(slot="m",name="avg_npc_1904_1#1$2")]
[name="好事的神明"]不知什么？不知我有没有见过你口中的招财猫，对不对？你要找的根本就不是我，而是他。
[charslot(slot="m",name="avg_4199_makiri_1#1$1")]
[name="森内"]不敢！能见到一位神明，对我来说已经是天大的喜事，我哪敢挑挑拣拣？
[charslot(slot="m",name="avg_npc_1904_1#1$2")]
[name="好事的神明"]可你的眼睛分明就不是这么说的。
[name="好事的神明"]以前我和那家伙还能聊得上天的时候，他口中的你可没这么做作。你那时就是个小孩子，小孩子怎么对朋友，你就怎么对他。
[charslot(slot="m",name="avg_4199_makiri_1#4$1")]
[name="森内"]......祂就是因为这个离我而去的吗？
[charslot(slot="m",name="avg_npc_1904_1#1$2")]
[name="好事的神明"]我哪知道。他记得你，但你也不过是他打过交道的无数人中的一个。他才不会费心告诉我为什么“离你而去”。
[charslot(slot="m",name="avg_4199_makiri_1#9$1")]
[name="森内"]这......
[stopmusic(fadetime=2)]
[charslot(slot="m",name="avg_npc_1904_1#1$2")]
[name="好事的神明"]我来找你有别的理由。
[charslot(slot="m",name="avg_4199_makiri_1#1$1")]
[name="森内"]没问题！您想从我这儿得到什么？金钱？还是信息？
[playMusic(key="$formal_loop", volume=0.6)]
[charslot(slot="m",name="avg_npc_1904_1#1$2")]
[name="好事的神明"]当然是信息。有关怪谈的信息。
[name="好事的神明"]你以为御机的怪谈都是我们这样的神明做的，但我可以明确告诉你，基本上全都不是。
[charslot(slot="m",name="avg_4199_makiri_1#8$1")]
[name="森内"]您不正是怪谈“轮入道”的本体吗？
[charslot(slot="m",name="avg_npc_1904_1#1$2")]
[name="好事的神明"]我不否认自己每天骑着独轮车风风火火地在街上跑，可除此之外呢？
[charslot(slot="m",name="avg_4199_makiri_1#2$1")]
[name="森内"]都厅街的那个警察署背后的旧楼。“不存在的电梯”。
[name="森内"]只有十五层的楼里居然有显示十六层的按钮，多出来的一层便是“地狱”，那里发生过失踪事件。
[name="森内"]而且前台的招财猫摆件和十六层出现的时机息息相关。那个固定在台面上的招财猫偶尔会消失，第二天又重新出现在台面上。
[name="森内"]这样的事情不仅发生在那栋旧楼，还有很多人都跟我说过类似的事情，“招财猫饰品莫名其妙丢失又出现”之类的。
[name="森内"]具体到那栋旧楼，每次“误入地狱”事件发生的时候，招财猫的摆件都不见了。
[charslot(slot="m",name="avg_npc_1904_1#1$2")]
[name="好事的神明"]你知道得倒是细，可我偏偏能够断定，那栋楼的招财猫摆件和你想找的“神明”，除了长得像之外半点关系都没有。
[charslot(slot="m",name="avg_4199_makiri_1#11$1")]
[name="森内"]您的证据呢？
[charslot(slot="m",name="avg_npc_1904_1#1$2")]
[name="好事的神明"]我哪需要证据？我就是神明，分辨一样东西和神明有没有关系，那还不轻而易举？
[charslot(slot="m",name="avg_4199_makiri_1#6$1")]
[name="森内"]这只能算空口无凭——
[charslot(slot="m",name="avg_npc_1904_1#1$2")]
[name="好事的神明"]你刚才那股恭顺劲儿呢？
[charslot(slot="m",name="avg_4199_makiri_1#9$1")]
[name="森内"]我......
[charslot(slot="m",name="avg_npc_1904_1#1$2")]
[name="好事的神明"]我可不是要责难你。像现在这样有什么说什么，比刚才那副样子好多了。
[name="好事的神明"]再说，我也是仔仔细细探查过那栋旧楼的。
[name="好事的神明"]第一，那根本就不是什么隐藏按钮。十六层的按钮是嵌在十五层按钮上边的，被钢板挡住了。
[name="好事的神明"]那肯定不是神明做的，你们人类也不可能掀动那东西。
[charslot(slot="m",name="avg_4199_makiri_1#11$1")]
[name="森内"]十六层的按钮一直都在那里......只是被钢板挡住了？！
[charslot(slot = "m", focus = "n")]
森内的脸色忽然变得有些难看。
[charslot]
[charslot(slot="m",name="avg_npc_1904_1#1$2")]
[name="好事的神明"]看，你也觉得自己有点傻了，是不是？
[name="好事的神明"]第二，那个招财猫是能按动的。使劲按，按下去，能把整个摆件按到台面下面去。
[charslot(slot="m",name="avg_4199_makiri_1#11$1")]
[name="森内"]您......按了？
[charslot(slot="m",name="avg_npc_1904_1#1$2")]
[name="好事的神明"]按了啊，按了也什么都没发生。前台回来的时候随便鼓捣鼓捣，那个摆件就又冒出来了。
[name="好事的神明"]然后那个前台就开始接电话，接了一长串，一直在道歉什么的。就这样。
[name="好事的神明"]看，你不过是把真正的怪谈和那个前台的怪癖联系在了一起而已。
[charslot(slot="m",name="avg_4199_makiri_1#9$1")]
[name="森内"]那......怎么可能是怪癖呢？
[charslot(slot="m",name="avg_npc_1904_1#1$2")]
[name="好事的神明"]那还能是什么？把招财猫摆件压到台面里去，难道是他和你正相反，跟那家伙有什么仇怨？
[charslot(slot="m",name="avg_npc_1918_1#3$1")]
[name="萌萌香"]那个......
[charslot(slot="m",name="avg_npc_1904_1#1$2")]
[name="好事的神明"]小姑娘？怎么了，你去那做过节目？
[charslot(slot="m",name="avg_npc_1918_1#3$1")]
[name="萌萌香"]没有，但之前综艺节目取材的时候，一个同事曾经提过这个点子，然后被事务所所长骂了一顿。
[charslot(slot="m",name="avg_4199_makiri_1#11$1")]
[name="森内"]骂了一顿？
[charslot(slot="m",name="avg_npc_1918_1#6$1")]
[name="萌萌香"]所长说了很多我不是很能听懂的话，说是里面有个“铁火场”是金石会的产业什么的。大概是饭店，怕做节目影响生意吧。
[dialog]
[charslot(slot="m",name="avg_136_hsguma_1#5$1")]
[name="星熊"]铁火场？
[charslot(slot="m",name="avg_4199_makiri_1#8$1")]
[name="森内"]铁火场？！
[charslot(slot="m",name="avg_npc_1918_1#3$1")]
[name="萌萌香"]是啊，怎么了？“铁火”是一种鳞兽料理的名字，那铁火场不就是卖铁火的饭店吗？
[charslot(slot="m",name="avg_136_hsguma_1#2$1")]
[name="星熊"]......“铁火场”是赌场的暗语。
[name="星熊"]看来“地狱”不过是金石会的赌场，有人误入那里后被封口了。
[name="星熊"]十六层的按钮得通过某种机关调出来，多半对应了某个夹层，或者地下室也说不定。
[name="星熊"]那个招财猫摆件大概是发信装置，按下去就会发信，所以“神明大人”按了之后才会有人打电话，那个前台才会道歉。
[charslot]
萌萌香感叹了一声，不知是替森内惋惜，还是得知怪谈并非超自然力量后松了口气。
好事的神明略微有些烦躁地用爪子搔了搔小脑袋，显然没料到怪谈竟然如此收场。
[stopmusic(fadetime=2)]
而森内的脸色越来越青，越来越青，直到汗水都从他的额头上流了下来。
[playMusic(intro="$loneliness_intro",key="$loneliness_loop", volume=0.6)]
[charslot(slot="m",name="avg_4199_makiri_1#11$1")]
[name="森内"]这一定只是巧合......只是巧合。
[charslot(slot="m",name="avg_4199_makiri_1

... (全文18795字符)
```

### level_act44side_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="64_g15_higashiroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[PlaySound(key="$d_avg_key")]
[Delay(time=1.2)]
[name="萌萌香"]放我下来吧，我自己能走了。
[name="星熊"]好。
[dialog]
[PlaySound(key="$dooropenquite")]
[charslot(slot="m",name="avg_npc_1918_1#10$1",duration=1)]
[delay(time=1.5)]
[playMusic(intro="$distressed_intro",key="$distressed_loop", volume=0.6)]
[name="萌萌香"]这......这是怎么了？！
[name="萌萌香"]我家怎么乱成这样......金兵卫的人真的已经来过了？
[charslot(slot = "m", name = "avg_136_hsguma_1#7$1")]
[name="星熊"]小心，可能还有人埋伏在里面——
[charslot]
[playsound(key="$d_avg_walkfast")]
萌萌香全然不顾星熊的叮嘱，三步并作两步往窗边跑。
[charslot(slot="m",name="avg_npc_1918_1#20$1")]
[name="萌萌香"]我的叶......
[name="萌萌香"]......助？
[charslot(slot="m",name="avg_npc_1918_1#21$1")]
[name="萌萌香"]等等，这不可能......这......怎么会这样......
[name="萌萌香"]谁把我的叶助给......剪了？
[charslot(slot = "m", name = "avg_136_hsguma_1#2$1")]
[name="星熊"]剪了？
[charslot(duration=0.5)]
星熊跟着萌萌香一路跑到窗边，看见在那里摆着的一整排东西，还有......
一个花盆。
里面还立着半截植物的梗，上半截显然被谁给剪了。
星熊转头看向垃圾桶，植物蔫头耷脑的上半截正躺在里面。
[charslot(slot = "m", name = "avg_136_hsguma_1#2$1")]
[name="星熊"]叶助是棵树？
[charslot(slot="m",name="avg_npc_1918_1#21$1")]
[name="萌萌香"]它只是一棵树苗！因为我照料不周，一棵根本没怎么长的小树！
[charslot(slot="m",name="avg_npc_1918_1#22$1")]
[name="萌萌香"]它凭什么像现在这样断成两截？！凭什么？凭什么？
[charslot(slot = "m", name = "avg_136_hsguma_1#2$1")]
[name="星熊"]萌萌香，你稍微缓一缓——
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_npc_1918_1#15$1")]
[name="萌萌香"]你别拦我，我要替叶助报仇！
[charslot(slot = "m", focus = "n")]
不知为什么，星熊每和萌萌香说一句话，萌萌香身上的火气就更盛一层。
几句话过后，她已经怒目圆睁，浑身颤抖，喘着粗气，完全是一副拼命的架势了。
星熊下意识地往后退了一步，甚至罕见地生出想咽口水的冲动。倒不是说她会对自己怎么样，只是......
杀意。自己感受到了杀意。
星熊又往后退了一步，忽然摸到个水壶，于是反手倒了杯水，交在萌萌香手里。
[charslot(slot = "m", name = "avg_136_hsguma_1#2$1")]
[name="星熊"]消消气，先喝口水吧。
[charslot]
[playsound(key="$d_avg_drinkswllw")]
萌萌香不答，只是恶狠狠地把一整杯水灌下肚。星熊隐约看见纸杯子的边缘都被她咬出了牙印。
但是不管怎么说，喝了杯水之后，她终于稍微冷静了一点。只是稍微。
[charslot(slot="m",name="avg_npc_1918_1#14$1")]
[name="萌萌香"]星熊，叶助只可能是金兵卫的手下害死的，是不是？
[charslot(slot = "m", name = "avg_136_hsguma_1#2$1")]
[name="星熊"]......很有可能。
[charslot(slot="m",name="avg_npc_1918_1#1$1")]
[name="萌萌香"]可是......为什么啊？
[name="萌萌香"]就因为我不在家，就把叶助剪掉泄愤吗？那个人怎么能这么做？
[charslot(slot = "m", name = "avg_136_hsguma_1#2$1")]
[name="星熊"]从垃圾桶里的状况来看，叶助的状况本来也不怎么好——
[dialog]
[charslot]
[playsound(key="$d_avg_footsteps_tatami", loop=true, channel="bgs")]
[CameraShake(duration=0.2, xstrength=15, ystrength=15, vibrato=20, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_npc_1918_1#13$1",duration=0.5)]
[delay(time=0.5)]
[StopSound(channel="bgs", fadetime=0)]
[delay(time=1)]
[charslot(slot = "m", focus = "n")]
萌萌香往星熊面前跨了一大步。星熊想躲，差点把刚刚放在身后的水壶撞倒了。
[charslot(slot="m",name="avg_npc_1918_1#15$1")]
[name="萌萌香"]叶助的状况当然不好！我整个人的时间全都扑在艺人的工作上了，叶助怎么可能好？！
[charslot(slot = "m", name = "avg_136_hsguma_1#2$1")]
[name="星熊"]欸？
[charslot(slot="m",name="avg_npc_1918_1#15$1")]
[name="萌萌香"]我当然希望叶助健健康康地长高长大，然后我就给它换盆，一直换，一直换，一直到我家都装不下！
[charslot(slot="m",name="avg_npc_1918_1#16$1")]
[name="萌萌香"]可事务所让我加班，我就必须得加班，到家三四点钟，很多时候根本记不住上次是什么时候浇的水。
[charslot(slot="m",name="avg_npc_1918_1#17$1")]
[name="萌萌香"]但是没关系，我可以在本子上记好，我可以算水量。
[charslot(slot="m",name="avg_npc_1918_1#15$1")]
[name="萌萌香"]可事务所让我出差的时候，我说我要带上叶助，他们只会像看傻瓜一样笑话我！
[name="萌萌香"]我像城际网络上那些博主教的一样，往土里插眼药水小瓶，可是没有用，每次我出差，叶助都黄得厉害，好几次差点干死！
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="萌萌香"]每次我都拼命把它救回来，它一直在生死线上来来回回，怎么可能长高？！
[charslot(slot = "m", name = "avg_136_hsguma_1#2$1")]
[name="星熊"]你这么重视它，它是......
[charslot(slot = "m", focus = "n")]
第一个涌到嘴边的当然是“很名贵的品种”，但星熊立刻意识到，不是这样的。
[charslot(slot = "m", name = "avg_136_hsguma_1#2$1")]
[name="星熊"]它是......对你很重要的人送给你的？
[charslot(slot="m",name="avg_npc_1918_1#21$1")]
[name="萌萌香"]......不。它是我在路边捡的。
[charslot(slot = "m", name = "avg_136_hsguma_1#2$1")]
[name="星熊"]捡的？
[charslot(slot="m",name="avg_npc_1918_1#21$1")]
[name="萌萌香"]从老家来御机的时候，我一直带着在老家养的云兽“花丸”。
[name="萌萌香"]可工作越来越忙，我实在没有时间照顾她，只能把她连兽带爬架送给别人，自己买了个相似的爬架做纪念。
[name="萌萌香"]我知道自己没时间养小动物，就想着，那我养些花花草草，是不是就可以了呢？
[charslot(slot = "m", name = "avg_136_hsguma_1#2$1")]
[name="星熊"]所以就有了叶助？
[charslot(slot="m",name="avg_npc_1918_1#1$1")]
[name="萌萌香"]不，我一开始养的是“阿兰”......
[name="萌萌香"]我努力抽出时间照顾它，一板一眼地按照书上说的照顾它，结果没几个月，阿兰莫名其妙地......
[charslot]
星熊看了一眼云兽爬架旁边的花盆。
[charslot(slot="m",name="avg_npc_1918_1#1$1")]
[name="萌萌香"]但阿兰的盆里又长了一棵小小的苗，我问了花店的老板，他说那是某种莓果的苗，建议我换个盆养，于是就有了小莓。
[name="萌萌香"]结果有一天御机刮大风，把我家窗玻璃刮坏了，我回家的时候，小莓已经......
[charslot(slot="m",name="avg_npc_1918_1#22$1")]
[name="萌萌香"]阿兰、小莓、松丸、刺殿......我养的植物总会以各种莫名其妙的方式死掉，刺殿甚至是因为楼上跑水被泡死的！
[name="萌萌香"]我开始怀疑自己是不是天生和植物处不来，动物却无论如何也不敢养，毕竟不知什么时候就要出差。
[name="萌萌香"]可每天下班回到家，家里空空荡荡，别说是人，连棵能卸下面具说话的草都没有，我......受不了，于是就有了拓麻三郎。
[charslot(slot = "m", name = "avg_136_hsguma_1#2$1")]
[name="星熊"]呃，这个电子宠物？那拓麻三郎他......
[charslot(slot="m",name="avg_npc_1918_1#1$1")]
[name="萌萌香"]我去找修理铺的老板，老板说我这台机器出厂时主板就有问题。
[charslot(slot = "m", name = "avg_136_hsguma_1#5$1")]
[name="星熊"]......
[charslot(slot="m",name="avg_npc_1918_1#1$1")]
[name="萌萌香"]叶助......是我从修理铺回来的路上连花盆一起从垃圾箱旁边捡到的。
[name="萌萌香"]我捡到叶助的时候下定决心，要是连叶助也被我养死了，那......我就断了养植物的心。
[charslot]
[playsound(key="$d_avg_zipper_normal",delay=1.5)]
泪眼婆娑的萌萌香沿着窗台一个一个介绍过去，星熊哭笑不得，直到萌萌香拉开最后那个运动包。
那不再是小动物或者植物的纪念，而是两个人的牌位，“紫野和彦”和“紫野久美子”。
[charslot(slot = "m", name = "avg_136_hsguma_1#2$1")]
[name="星熊"]......这是？
[charslot(slot="m",name="avg_npc_1918_1#1$1")]
[name="萌萌香"]我爸爸和我妈妈。
[charslot(slot = "m", name = "avg_136_hsguma_1#9$1")]
[name="星熊"]难道？！
[charslot(slot="m",name="avg_npc_1918_1#1$1")]
[name="萌萌香"]不。不是你想的那样。
[name="萌萌香"]我老家，在南部边境的后川城。
[name="萌萌香"]那是一座没什么名气的移动城市，金城家的地盘。不大，也没什么特产，非要说的话，最有名的东西是塑料，还有化工厂。
[stopmusic(fadetime=2)]
[charslot(slot = "m", name = "avg_136_hsguma_1#2$1")]
[name="星熊"]......
[dialog]
[charslot(slot="m",name="avg_npc_1918_1#5$1")]
[delay(time=1.5)]
[Dialog]
[Blocker(a=1, r=0, g

... (全文29212字符)
```

### level_act44side_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="64_g14_mifuneoffice",screenadapt="coverall")]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[charslot(slot = "l", name = "avg_npc_1896_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_clog_fts", volume=1)]
[charslot(slot = "r", name = "avg_npc_1901_1#5$1", duration=1.5)]
[Delay(time=2)]
[charslot(slot = "r", name = "avg_npc_1901_1#5$1", focus="r")]
[name="澪"]三船先生，您真的要亲自去锻冶町吗？
[charslot(slot = "l", name = "avg_npc_1896_1#1$1", focus="l")]
[name="三船"]这是我和铁斋、和星熊之间的事，只有我亲自了结，这事才算办得漂亮。
[charslot(slot = "r", name = "avg_npc_1901_1#5$1", focus="r")]
[name="澪"]按照您现在的谋划，说实话，就算没有般若，铁斋也会就范。
[charslot(slot = "l", name = "avg_npc_1896_1#1$1", focus="l")]
[name="三船"]你就这么不愿意让星熊回来？
[charslot(slot = "r", name = "avg_npc_1901_1#2$1", focus="r")]
[name="澪"]只是觉得没必要。
[charslot(slot = "l", name = "avg_npc_1896_1#1$1", focus="l")]
[name="三船"]也是，她一回来，你的工作量多了不少。看在你要接我班的分上，我可以给你讲得明白一点。
[dialog]
[delay(time=1.5)]
[charslot(slot = "l", name = "avg_npc_1896_1#6$1", focus="l")]
[name="三船"]澪，你觉得想在御机活得好，什么最重要？
[charslot(slot = "r", name = "avg_npc_1901_1#1$1", focus="r")]
[name="澪"]团结？
[charslot(slot = "l", name = "avg_npc_1896_1#6$1", focus="l")]
[name="三船"]不，最重要的是......“漂亮”。
[name="三船"]外表上的华丽美观可以一举扭转世人心中的成见，你、我，我们都得益于此。
[name="三船"]如果一直是当年那副小混混的打扮，我怕不是第一次上电视就要被人轰下去，更别说把金石台办到今天这步。
[charslot(slot = "l", name = "avg_npc_1896_1#2$1", focus="l")]
[name="三船"]而做事，同样讲究漂亮，讲究美。
[charslot(slot = "l", name = "avg_npc_1896_1#1$1", focus="l")]
[name="三船"]乌萨斯有个我记不起名字的作家说过一句话，如果第一幕出现了一把铳......
[name="三船"]那么，最迟到第三幕，这把铳一定要被一个拉特兰人握在手中。
[charslot(slot = "r", name = "avg_npc_1901_1#5$1", focus="r")]
[name="澪"]三船先生，据说哥伦比亚有一群叫黑钢的人也会用铳。
[charslot(slot = "l", name = "avg_npc_1896_1#9$1", focus="l")]
[name="三船"]哈哈，你明白我意思就好。
[charslot(slot = "l", name = "avg_npc_1896_1#1$1", focus="l")]
[name="三船"]御机太大，发展得也太快，我们很多时候没办法确定自己做的事究竟是否正确......
[name="三船"]那就只能把事情做得有始有终，让每个人都去他们该去的地方，让每一把铳都在最后扣响，这也是漂亮，这也是美。
[charslot(slot = "r", name = "avg_npc_1901_1#3$1", focus="r")]
[name="澪"]听起来更像......把事情做绝。
[charslot(slot = "l", name = "avg_npc_1896_1#1$1", focus="l")]
[name="三船"]你愿意怎么想都随你去。等你成了金石会的四代目会长，你大可以试一试我说的话。
[name="三船"]不过现在，你还是专心休息，等着对付星熊吧。
[charslot(slot = "r", name = "avg_npc_1901_1#5$1", focus="r")]
[name="澪"]......星熊是强敌。
[charslot(slot = "l", name = "avg_npc_1896_1#6$1", focus="l")]
[name="三船"]但她是鬼，而且是已经失控过一次的鬼。
[charslot(slot = "l", name = "avg_npc_1896_1#1$1", focus="l")]
[name="三船"]听说过一个叫奎隆的人吗？
[charslot(slot = "r", name = "avg_npc_1901_1#5$1", focus="r")]
[name="澪"]据说是个很久很久以前的人，和鬼族以及僧院有关，再多就不知道了。
[charslot(slot = "l", name = "avg_npc_1896_1#1$1", focus="l")]
[name="三船"]铁斋以前除了那些老掉牙的武家故事，就喜欢讲这个人的传说。
[name="三船"]那些传说真假难辨，有的还自相矛盾，比如关于奎隆的死，铁斋至少讲过三种不同的版本。
[charslot(slot = "l", name = "avg_npc_1896_1#2$1", focus="l")]
[name="三船"]但其中我最喜欢的一种，就很残忍，也很......美。
[name="三船"]在真正取得涅槃，遁入阇那之前，奎隆听见了最后一支鬼族被迫成为苇原之民时骨肉分离的哭声。
[name="三船"]但那时的奎隆已经形销骨立，无力从无忧树下离开，无力仗剑拯救同族，甚至无力控制自己青色的怒火——
[charslot(slot = "l", name = "avg_npc_1896_1#1$1", focus="l")]
[name="三船"]于是，怒火占据了奎隆的心神，让他彻底失却了神智，让他以垂死之躯消灭了一整支军队，可他要保护的同族也全数死在他的剑下。
[name="三船"]至于这个故事里的奎隆是力尽而死，还是死于自戕，抑或是无情到即便如此仍然能心安理得地涅槃，就不得而知了。
[charslot(slot = "r", name = "avg_npc_1901_1#1$1", focus="r")]
[name="澪"]......我不懂您讲这位奎隆的传说有什么用意。
[charslot(slot = "l", name = "avg_npc_1896_1#9$1", focus="l")]
[name="三船"]当一个鬼意识到自己无能为力的那一刻，总是其最脆弱的时候。至于是一蹶不振，还是陷入疯狂......
[name="三船"]我们要对付的这一位，可是有过先例的。
[charslot(slot = "r", name = "avg_npc_1901_1#5$1", focus="r")]
[name="澪"]......
[charslot(slot = "l", name = "avg_npc_1896_1#9$1", focus="l")]
[name="三船"]好了，快去休息吧。我也该见见我们的客人了。
[dialog]
[PlaySound(key="$d_avg_clog_fts", volume=1)]
[charslot(slot = "r", afrom=1, ato=0, duration=1.5)]
[delay(time=2.5)]
[charslot(duration=1, isblock=true)]
[delay(time=0.5)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_4199_makiri_1#2$1", posfrom="200,0", posto="0,0", duration = 1.5)]
[delay(time=2)]
[name="森内"]三船先生......您贵安？
[charslot(slot = "m", name = "avg_npc_1896_1#9$1")]
[name="三船"]怎么样，没伤着吧？
[charslot(slot = "m", name = "avg_4199_makiri_1#13$1")]
[name="森内"]没有，没有！倒不如说这是我最近睡得最香的一觉！
[charslot(slot = "m", name = "avg_npc_1896_1#9$1")]
[multiline(name="三船")]对嘛，干你们这一行的，就该像你这样，风趣幽默，笑面迎人......
[charslot(slot = "m", name = "avg_npc_1896_1#1$1")]
[multiline(name="三船",end=true)]还喜欢东挨西问。
[charslot(slot = "m", name = "avg_4199_makiri_1#5$1")]
[name="森内"]......！
[charslot(slot = "m", name = "avg_npc_1896_1#1$1")]
[name="三船"]去给星熊打个电话，就说......我找她有事相商。
[charslot(slot = "m", name = "avg_4199_makiri_1#13$1")]
[name="森内"]这个......三船先生，您看，星熊她毕竟帮了我不少......
[charslot(slot = "m", name = "avg_npc_1896_1#4$1")]
[name="三船"]帮你查明了“轮入道”的真相？
[charslot(slot = "m", name = "avg_4199_makiri_1#13$1")]
[name="森内"]是啊——
[charslot(slot = "m", name = "avg_npc_1896_1#4$1")]
[name="三船"]不止如此吧？
[name="三船"]你站在摊前怅然若失的时候，到底在想什么呢？这么多年追逐怪谈的努力都白费了，是不是？
[charslot(slot = "m", name = "avg_4199_makiri_1#6$1")]
[name="森内"]......
[charslot(slot = "m", name = "avg_npc_1896_1#9$1")]
[name="三船"]现在你知道了，一切都是虚妄。你好像被我和我构筑的这些怪谈给骗了。
[charslot(slot = "m", name = "avg_4199_makiri_1#6$1")]
[name="森内"]您......为什么要这么做？
[charslot(slot = "m", name = "avg_npc_1896_1#1$1")]
[name="三船"]这和你无关。你就当自己太倒霉吧。但反正生活是要继续的，所以，如果你愿意，可以把一些更实在的东西抓在手里。
[charslot(slot = "m", name = "avg_4199_makiri_1#6$1")]
[name="森内"]您在利诱我？
[charslot(slot = "m", name = "avg_npc_1896_1#6$1")]
[name="三船"]利诱？打电话，你以后继续做你的情报商。不打，你知道金石会对敌人会怎么做。
[charslot(slot = "m", name = "avg_4199_makiri_1#8$1")]
[name="森内"]三船先生——
[charslot(slot = "m", name = "avg_npc_1896_1#6$1")]
[name="三船"]你要是想不起来，我很愿意提醒你一下，记得你的右眼是怎么丢的吗？
[charslot(slot = "m", name = "avg_4199_makiri_1#9$1")]
[name="森内"]......记得。当时是我为了追逐一桩怪谈，冲撞了三船先生和人谈事的场合......
[charslot(slot = "m", name = "avg_npc_1896_1#6$1")]
[name="三船"]我废你一只眼，是因为你当初看了不该看的东西。而我留你另一只眼，是珍惜你的才能，也是对你的警告。
[charslot(slot = "m",

... (全文28103字符)
```

### level_act44side_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.1, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_punch",volume=1)]
[Effect(name="$e_fist_hit_02",x=-180,layer = 1)]
[delay(time=0.2)]
[PlaySound(key="$d_avg_punch02",volume=1)]
[Effect(name="$e_fist_hit_02",x=180,layer = 2)]
[delay(time=0.5)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.1, block=true)]
[charslot]
[charslot(slot = "r", name = "avg_npc_1916_1#1$1")]
[charslot(slot = "l", name = "avg_npc_1917_1#1$1")]
[Background(image="64_g4_kajistreet_dusk",screenadapt="coverall")]
[delay(time=0.1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[StopSound(channel="a", fadetime=2)]
[CameraShake(duration=0.8, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$bodyfalldown2")]
[charslot(slot = "l", posfrom="0,0", posto="0,-100", afrom=1, ato=0, duration=0.5)]
[delay(time=0.2)]
[playsound(key="$bodyfalldown3")]
[charslot(slot = "r", posfrom="0,0", posto="0,-100", afrom=1, ato=0, duration=0.5)]
[delay(time=1)]
[charslot]
[PlayMusic(intro="$normal02_intro", key="$normal02_loop", volume=0.6)]
[charslot(slot = "l", name = "avg_npc_1914_1#1$1", duration=1, isblock=true)]
[name="疲惫的警察"]......
[dialog]
[PlaySound(key="$rungeneral", volume=1, loop=true, channel="r")]
[StopSound(channel="r", fadetime=1)]
[charslot(slot = "r", name = "avg_npc_1915_1#1$1", posfrom="300,0", posto="0,0", duration=1)]
[delay(time=1.5)]
[charslot(slot = "r", name = "avg_npc_1915_1#1$1", focus="r")]
[name="泄气的警察"]别傻站着，这帮亡命徒还没嫌疑人有分寸！
[charslot(slot = "l", name = "avg_npc_1914_1#1$1", focus="l")]
[name="疲惫的警察"]......我累了。
[charslot(slot = "r", name = "avg_npc_1915_1#1$1", focus="r")]
[name="泄气的警察"]谁不累？
[charslot(slot = "l", name = "avg_npc_1914_1#1$1", focus="l")]
[name="疲惫的警察"]我是说，我真的累了。
[name="疲惫的警察"]跟一帮社会渣滓一起，一群人抓一个人，还*东国粗口*抓不到。
[name="疲惫的警察"]她连我们的一根头发都不愿意碰，倒在她那刀鞘下的才是真正的渣滓，每个人屁股上都不缺案底。
[name="疲惫的警察"]她把他们一个个打趴下，我们却和社会渣滓一起对付她......
[name="疲惫的警察"]可恶......该死！
[name="疲惫的警察"]惟任那家伙只知道一句“会好的”，我从入职到现在已经干了快十年，肩上的章也快换了，真的好了吗？好个——
[charslot(slot = "r", focus="n")]
[name="张狂的忍者"]条子，躲开！
[dialog]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$d_avg_punch02",volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[delay(time=0.5)]
[charslot(slot = "l", posfrom="0,0", posto="0,-50", afrom=1, ato=0, duration=0.5)]
[playsound(key="$bodyfalldown2")]
[delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1915_1#1$1", focus="r")]
[name="泄气的警察"]将吾！
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="泄气的警察"]混蛋，你敢袭警？！
[charslot]
[charslot(slot = "m", name = "avg_npc_1916_1#1$1")]
[name="张狂的忍者"]我刚刚叫你们躲了——
[dialog]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$d_avg_punch02",volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[delay(time=0.5)]
[CameraShake(duration=0.3, xstrength=10, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "m", posfrom="0,0", posto="0,-50", afrom=1, ato=0, duration=0.5)]
[playsound(key="$bodyfalldown2")]
[delay(time=1)]
[charslot]
[PlaySound(key="$d_avg_higheldshosfts", volume=1)]
[charslot(slot = "m", name = "avg_1044_hsgma2_1#2$1", duration=1.5)]
[Delay(time=2)]
[charslot(slot = "m", focus="n")]
[name="泄气的警察"]你——
二人面面相觑。
[charslot(slot = "m", name = "avg_1044_hsgma2_1#2$1")]
[name="星熊"]警官，让条路好吗？
[name="星熊"]不然，我身上的罪名可能会多一条袭警。也许是杀人。我现在不是特别在乎。
[charslot]
警察叹了口气，把空空如也的手从口袋里掏出来，放在星熊能看见的地方，微微侧了侧身。
[charslot(slot = "m", name = "avg_npc_1915_1#1$1")]
[name="泄气的警察"]多谢你替将吾出了口气。
[dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="64_g1_jindastreet_d",screenadapt="coverall")]
[PlaySound(key="$d_avg_crwddiscuss_outside", volume=0, loop=true, channel="cr")]
[SoundVolume(volume=0.6, channel="cr",fadetime=2)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.6)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_avg_broadcast_third", volume=1)]
[Delay(time=1)]
[name="重复播放的广播"]铃、铃、铃，林贡斯，林贡斯百货♪
[name="重复播放的广播"]古今东西，无所不包，林贡斯百货♪
[charslot(slot = "m", name = "avg_npc_1908_1#1$1")]
[name="拉客的店员"]时候还早，进来喝一杯吧！像您这样豪爽的鬼族，最适合本店新进的精酿黑啤——
[name="拉客的店员"]如果您是古典派，我们也有珍藏的芋烧酒......
[dialog]
[charslot]
[StopSound(channel="cr", fadetime=2)]
[PlaySound(key="$d_avg_carpet_normal_fts", volume=1)]
[charslot(slot = "m", name = "avg_1044_hsgma2_1#2$1", posfrom="300,0", posto="0,0", duration=1.5)]
[Delay(time=1.5)]
[charslot(slot = "m", focus="n")]
[name="打扮入时的男人"]女士，请收好。
[charslot(slot = "m", name = "avg_1044_hsgma2_1#7$1")]
[name="星熊"]滚开。
[charslot(slot = "m", focus="n")]
[name="打扮入时的男人"]何必这么急躁呢？难道您也在寻找这片大地唯一珍贵之物——“幸福”的敲门砖——
[dialog]
[Delay(time=0.5)]
[charslot(slot = "m", focus="n")]
[name="打扮入时的男人"]等等，您是“金石会的青鬼”？
[charslot(slot = "m", name = "avg_1044_hsgma2_1#4$1")]
[name="星熊"]......
[charslot(slot = "m", focus="n")]
[name="打扮入时的男人"]我能问下萌萌香小姐去哪里了吗？
[charslot(slot = "m", name = "avg_1044_hsgma2_1#7$1")]
[name="星熊"]你是她的粉丝？还是想带着她去找三船领赏？
[charslot(slot = "m", focus="n")]
[name="打扮入时的男人"]都不是，我是想请您帮个忙。
[name="打扮入时的男人"]能不能请您也让我像这几天的萌萌香小姐一样失踪一次？这样，我是不是也能像她一样彻彻底底火一把？
[dialog]
[charslot]
[PlaySound(key="$rungeneral", volume=1)]
[chars

... (全文25167字符)
```

### level_act44side_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_towerinside",screenadapt="coverall")]
[PlayMusic(key="$formal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$transmission", volume=1)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1918_1#8$1", duration=0.5, isblock=true)]
[name="萌萌香"]星熊！星熊！！能听见我说话吗？
[name="萌萌香"]能听见我——
[dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_npc_1906_1#1$1", posfrom="200,0", posto="0,0", duration=1.5)]
[delay(time=0.5)]
[name="懈怠的黑道"]号什么丧呢！
[charslot(slot = "m", name = "avg_npc_1918_1#14$1")]
[name="萌萌香"]星——
[charslot(slot = "m", name = "avg_npc_1906_1#1$1")]
[name="懈怠的黑道"]你就叫吧，看看星熊那傻瓜什么时候来自投罗网！
[charslot(slot = "m", name = "avg_npc_1918_1#13$1")]
[name="萌萌香"]......金兵卫到底想拿我怎么样？
[charslot(slot = "m", name = "avg_npc_1906_1#1$1")]
[name="懈怠的黑道"]金兵卫？那是谁？
[charslot(slot = "m", name = "avg_npc_1918_1#12$1")]
[name="萌萌香"]......我说三船。
[charslot(slot = "m", name = "avg_npc_1906_1#1$1")]
[name="懈怠的黑道"]我怎么知道？不过，毕竟你多少也算个偶像，说不定会长拿你还有什么别的用处，也说不定他就打算做掉你拉倒。
[name="懈怠的黑道"]你也是的，白长了这么一张漂亮脸蛋，怎么就不知道跟他服个软？
[dialog]
[PlaySound(key="$d_gen_transmissionget", volume=1)]
[delay(time=1.5)]
[name="懈怠的黑道"]*东国粗口*，明知道我被临时拉来当看守，又是哪个混球给我发信息寻开心——
[name="懈怠的黑道"]啥？又搞来一个倒霉蛋跟我换班？
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="懈怠的黑道"]呀——嚯！
[dialog]
[PlaySound(key="$rungeneral", volume=1, loop=true, channel="r")]
[StopSound(channel="r", fadetime=1)]
[charslot(slot = "m", name = "avg_npc_1906_1#1$1", posfrom="0,0", posto="200,0", afrom=1, ato=0, duration=0.5, isblock=true)]
[delay(time=1)]
[charslot]
[charslot(slot = "m", name = "avg_npc_1918_1#7$1")]
[name="萌萌香"]......走远了。
[charslot(slot = "m", name = "avg_npc_1918_1#6$1")]
[name="萌萌香"]刚刚到底是怎么回事？为什么能听见人的声音，甚至......好像还和星熊说上了话？
[name="萌萌香"]难道出幻觉了？
[charslot(slot = "m", focus="n")]
[name="？？？"]在——你——的——背——后——
[charslot]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "l", name = "avg_npc_1918_1#10$1", posfrom="200,0", posto="0,0", afrom=1, ato=1, duration=0.5)]
[name="萌萌香"]呀！！
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "r", name = "avg_npc_1900_1#10$1", posfrom="200,0", posto="0,0", duration=1.5, isblock=true)]
[delay(time=0.5)]
[charslot(slot = "r", name = "avg_npc_1900_1#10$1", focus="r")]
[name="？？？"]噗！
[charslot(slot = "r", name = "avg_npc_1900_1#9$1", focus="r")]
[name="？？？"]原来你节目里那些反应真不是演的啊。之前吉星告诉我的时候我还不信呢。
[charslot(slot = "l", name = "avg_npc_1918_1#10$1", focus="l")]
[name="萌萌香"]你认识吉星？吉星她怎么样了？
[charslot(slot = "r", name = "avg_npc_1900_1#9$1", focus="r")]
[name="？？？"]她和你差不多，也被关了起来。暂时应该不会吃什么苦头。
[charslot(slot = "l", name = "avg_npc_1918_1#3$1", focus="l")]
[name="萌萌香"]你、你到底是......
[charslot(slot = "r", name = "avg_npc_1900_1#9$1", focus="r")]
[name="？？？"]叫我更纱吧，算是你的粉丝，名义上也算是三船的雇员。不过，我的真实身份其实是隐藏的忍客！
[charslot(slot = "l", name = "avg_npc_1918_1#7$1", focus="l")]
[name="萌萌香"]忍客？忍者？
[charslot(slot = "r", name = "avg_npc_1900_1#4$1", focus="r")]
[name="更纱"]别瞎说，忍者不过是拿钱办事的杀人犯，忍客可是城际网络的漫游者！
[charslot(slot = "l", name = "avg_npc_1918_1#3$1", focus="l")]
[name="萌萌香"]可我记得忍客一开始不也是财阀养来攻击竞争对手的忍者，只是精通城际网络相关的技术吗？
[charslot(slot = "r", name = "avg_npc_1900_1#3$1", focus="r")]
[name="更纱"]啧，那就流浪忍客，流浪忍客好吧！
[charslot(slot = "l", name = "avg_npc_1918_1#7$1", focus="l")]
[name="萌萌香"]可我还是不知道你从哪来，也不知道你为什么会帮我——
[charslot(slot = "r", name = "avg_npc_1900_1#9$1", focus="r")]
[name="更纱"]你在家看到的那段录像，就是三船和澪商量怎么让你感染矿石病的那段，那是我放出来提醒你的！这样够不够让你相信我？
[charslot(slot = "l", name = "avg_npc_1918_1#11$1", focus="l")]
[name="萌萌香"]就是你大半夜把我吓得睡不着觉？！
[charslot(slot = "r", name = "avg_npc_1900_1#4$1", focus="r")]
[name="更纱"]这这这，毕竟那也是我头一次处理御机——不是，金石台的信号系统，稍微出了点错，不是故意的，真的不是故意的！
[charslot(slot = "l", name = "avg_npc_1918_1#1$1", focus="l")]
[name="萌萌香"]嗯......嗯。不管怎么说，如果不是你，我可能已经......
[charslot(slot = "r", name = "avg_npc_1900_1#11$1", focus="r")]
[name="更纱"]说实话，我一开始只是听说金石台是御机首屈一指的大电视台，就来随便递份简历养活自己罢了。
[charslot(slot = "r", name = "avg_npc_1900_1#5$1", focus="r")]
[name="更纱"]但越是在这儿待着，越觉得他们其实有点不像话，只有你这个当家花旦还挺可爱的......结果他们居然连你也不放过！
[name="更纱"]尤其是那个三船，他要是个更像样点的家伙，我倒也不是不知道拿钱办事的道理。
[name="更纱"]可这家伙......帮这种人做事，还不如让我跳海自尽呢。
[charslot(slot = "l", name = "avg_npc_1918_1#23$1", focus="l")]
[name="萌萌香"]......哈哈。
[charslot(slot = "r", name = "avg_npc_1900_1#1$1", focus="r")]
[name="更纱"]刚才我从三船的监控网里定位到了星熊的位置，就稍微帮你们连上了一会儿。
[charslot(slot = "l", name = "avg_npc_1918_1#3$1", focus="l")]
[name="萌萌香"]欸？这也能连上？上次直播的时候，电视台的技术总监连事先设置好的连接都鼓捣了大半天......
[charslot(slot = "r", name = "avg_npc_1900_1#9$1", focus="r")]
[name="更纱"]那他水平也不怎么样嘛。
[name="更纱"]总而言之，现在你听我的指示，一会儿我再让你和星熊联络一次，让她在外面接应。
[charslot(slot = "r", name = "avg_npc_1900_1#10$1", focus="r")]
[name="更纱"]我们一会儿带上吉星一起走，听我的，保证那些笨蛋黑道连你们的影子都摸不到。
[charslot(slot = "l", name = "avg_npc_1918_1#7$1", focus="l")]
[name="萌萌香"]......不，我不能走。
[charslot(slot = "r", name = "avg_npc_1900_1#5$1", focus="r")]
[name="更纱"]你在说什么蠢话？不走，就在这儿等着三船拿你开刀？
[charslot(slot = "l", name = "avg_npc_1918_1#1$1", focus="l")]
[name="萌萌香"]我走了之后......又能去哪儿呢？
[charslot(slot = "r", name = "avg_npc_1900_1#5$1", focus="r")]
[name="更纱"]南院的地盘这么大，你想去哪就去哪啊。
[charslot(slot = "l", name = "avg_npc_1918_1#6$1", focus="l")]
[name="萌萌香"]去改名换姓，当一个永远不知道什么时候会被人追上的逃亡者？我不干。
[charslot(slot = "l", name = "avg_npc_1918_1#3$1", focus="l")]
[name="萌萌香"]羽生萌萌香这个名字不是我自己选的，但事到如今，才告诉我，要我把这个名字从自己身上剥下去......
[name="萌萌香"]那我和死了又有什么区别？
[charslot(slot = "r", name = "avg_npc_1900_1#5$1", focus="r")]
[name="更纱"]你认真的？我听你这话，怎么听怎么都像是准备赴死哦？你不怕死？
[charslot(slot = "l", name = "avg_npc_1918_1#3$1", focus="l")]
[name="萌萌香"]我不知道，我只知道自己已经没有别的活法了。
[charslot(slot = "r", name = "avg_npc_1900_1#9$1", focus="r")]
[name="更纱"]行，不愧是我喜欢的明星。你刚刚那段话还挺酷的，感觉像是电影里的台词。
[name="更纱"]那你打算怎么把这个明星当下去？金兵卫不让你当怎么办？
[charslot(slot = "l", 

... (全文18883字符)
```

### level_act44side_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="64_g14_mifuneoffice",screenadapt="coverall")]
[PlayMusic(intro="$loading_intro", key="$loading_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$fireworks", volume=0.5)]
[Delay(time=1)]
从电视台的顶层俯瞰，夜空中烟花零星升起，又缓缓下坠，一直落到脚下不可见的地方。
花火大会尚未正式开始，这不过是预热之前的预热。
斐迪亚凝视着玻璃幕墙里的自己，和自己身后重铸后的般若。
[dialog]
[charslot(slot = "m", name = "avg_npc_1896_1#4$1", duration=1, isblock=true)]
[name="三船"]......般若。
[name="三船"]二十年过去，你终于到了我的手里......可惜，太迟了。
[name="三船"]除了代替铁斋，被打扮成这次仪式的承认者以外，你又能为我做些什么呢？
[charslot]
斐迪亚玩味地看着重铸后的般若，忽然注意到内面的把手上明显粘着胶痕，大概是被什么绑带箍了很长时间。
[charslot(slot = "l", name = "avg_npc_1896_1#1$1")]
[name="三船"]内面没动过，是吗？
[charslot(slot = "l", name = "avg_npc_1896_1#2$1")]
[name="三船"]......真是面好盾，但也就这样了。
[charslot(slot = "l", name = "avg_npc_1896_1#2$1")]
[name="三船"]澪！
[dialog]
[PlaySound(key="$d_avg_clog_fts", volume=1, loop=true, channel="c")]
[StopSound(channel="c", fadetime=1.5)]
[charslot(slot = "r", name = "avg_npc_1901_1#1$1", posfrom="200,0", posto="50,0", duration=1.5)]
[Delay(time=2)]
[charslot(slot = "l", name = "avg_npc_1896_1#1$1", focus="l")]
[name="三船"]距离典礼正式开始还有多长时间？
[charslot(slot = "r", name = "avg_npc_1901_1#1$1", focus="r")]
[name="澪"]一个小时左右。
[charslot(slot = "l", name = "avg_npc_1896_1#1$1", focus="l")]
[name="三船"]行。我下楼透口气。
[charslot(slot = "r", name = "avg_npc_1901_1#5$1", focus="r")]
[name="澪"]三船先生，星熊很可能突袭会场。
[charslot(slot = "l", name = "avg_npc_1896_1#9$1", focus="l")]
[name="三船"]我正等着她来呢。
[charslot(slot = "r", name = "avg_npc_1901_1#1$1", focus="r")]
[name="澪"]您是说？
[charslot(slot = "l", name = "avg_npc_1896_1#9$1", focus="l")]
[name="三船"]她来无非两种情况。要么已经被逼疯，要么居然还能在铁斋死后保持冷静。
[name="三船"]但不管她什么样，在我的地盘上，在我的镜头下，电视上的她，也不过是个疯狂的杀人鬼。
[name="三船"]到时候，这个疯女人就只会是这次继位仪式的注脚，陷入疯狂的失败者。就算我敌不过她，也会有上面的人来替我收拾她的。
[charslot(slot = "r", name = "avg_npc_1901_1#3$1", focus="r")]
[name="澪"]萌萌香她......
[charslot(slot = "l", name = "avg_npc_1896_1#9$1", focus="l")]
[name="三船"]不忍心了？
[name="三船"]也罢，那就再留她一阵子，把她彻底榨干。我们有的是手段让她就范——
[charslot(slot = "l", name = "avg_npc_1896_1#1$1", focus="l")]
[name="三船"]等等，这样也得留那个叫吉星的一条命，免得彻底让萌萌香绝望。你还没处理她呢吧？
[charslot(slot = "r", name = "avg_npc_1901_1#3$1", focus="r")]
[name="澪"]没有。
[charslot(slot = "l", name = "avg_npc_1896_1#9$1", focus="l")]
[name="三船"]那就好。
[name="三船"]对了，哲也呢？
[charslot(slot = "r", name = "avg_npc_1901_1#3$1", focus="r")]
[name="澪"]......
[charslot(slot = "l", name = "avg_npc_1896_1#1$1", focus="l")]
[name="三船"]澪？
[charslot(slot = "r", name = "avg_npc_1901_1#2$1", focus="r")]
[name="澪"]......我没能看住他。
[charslot(slot = "l", name = "avg_npc_1896_1#7$1", focus="l")]
[name="三船"]你？没能看住他？
[charslot(slot = "l", focus="n")]
三船的声音陡然阴狠起来。
[charslot(slot = "l", name = "avg_npc_1896_1#6$1", focus="l")]
[name="三船"]说实话。
[charslot(slot = "r", name = "avg_npc_1901_1#2$1", focus="r")]
[name="澪"]......我放跑了他。
[charslot(slot = "l", name = "avg_npc_1896_1#6$1", focus="l")]
[name="三船"]还是恻隐之心？
[charslot(slot = "r", name = "avg_npc_1901_1#2$1", focus="r")]
[name="澪"]是。
[charslot(slot = "l", name = "avg_npc_1896_1#6$1", focus="l")]
[name="三船"]仅此而已？
[charslot(slot = "r", name = "avg_npc_1901_1#5$1", focus="r")]
[name="澪"]仅此而已。
[charslot(slot = "l", name = "avg_npc_1896_1#2$1", focus="l")]
[name="三船"]我对你很失望。
[charslot(slot = "r", name = "avg_npc_1901_1#5$1", focus="r")]
[name="澪"]愿受惩罚。
[charslot(slot = "l", name = "avg_npc_1896_1#1$1", focus="l")]
[name="三船"]算了。现在正是用人之际，我先不跟你计较。不过，你的任务该变一变了。
[name="三船"]假如星熊真打了过来，你去对她。
[charslot(slot = "r", name = "avg_npc_1901_1#5$1", focus="r")]
[name="澪"]这是我分内之事。
[charslot(slot = "l", name = "avg_npc_1896_1#6$1", focus="l")]
[name="三船"]别急着答应。
[name="三船"]如果她活着走到了我面前，你该知道自己的下场是什么。
[charslot(slot = "r", name = "avg_npc_1901_1#5$1", focus="r")]
[name="澪"]......
[charslot(slot = "r", name = "avg_npc_1901_1#2$1", focus="r")]
[name="澪"]......是。
[charslot(slot = "l", name = "avg_npc_1896_1#6$1", focus="l")]
[name="三船"]从现在开始，时刻会有两名忍者盯住你。别想耍什么花招。
[name="三船"]我出去透口气。告诉所有人，做好应对一切突发情况的准备。
[dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="64_g2_jindastreet_n",screenadapt="coverall")]
[Delay(time=1)]
[PlaySound(key="$d_avg_firework_amb", volume=0, loop=true, channel="f")]
[SoundVolume(volume=0.3, channel="f",fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[SoundVolume(volume=0.2, channel="f",fadetime=2)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "l", name = "avg_npc_1909_1#1$1", posfrom="300,0", posto="0,0", duration=1)]
[Delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1912_1#1$1", posfrom="200,0", posto="-50,0", duration=1.5)]
[Delay(time=2)]
[charslot(slot = "l", name = "avg_npc_1909_1#1$1", focus="l")]
[name="欣喜的路人"]花火大会还有一会儿，现在只是预热。我们继续在这边逛一会儿吧。
[charslot(slot = "r", name = "avg_npc_1912_1#1$1", focus="r")]
[name="冷静的路人"]别，亲爱的，我们就该直接去河对面的花火大会会场。城际网络上好多人在说，这片区域现在不安全。
[name="冷静的路人"]有小道消息说金石会的会长死了。怪谈中的那个青鬼砍死了他。
[charslot(slot = "l", name = "avg_npc_1909_1#1$1", focus="l")]
[name="欣喜的路人"]欸——是那个传媒大亨，金什么来着？
[charslot(slot = "r", name = "avg_npc_1912_1#1$1", focus="r")]
[name="冷静的路人"]不是不是，那个是三船。死掉的是铁斋。
[charslot(slot = "l", name = "avg_npc_1909_1#1$1", focus="l")]
[name="欣喜的路人"]欸——我看平时都是三船出现，还以为是他死了呢。
[charslot(slot = "r", name = "avg_npc_1912_1#1$1", focus="r")]
[name="冷静的路人"]锻冶町那边好像也有些不好的消息，加上最近一直在传的北院间谍......总之，还是先去河对岸吧。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "r", posfrom="-50,0", posto="-200,0", afrom=1, ato=0, duration=1.5)]
[charslot(slot = "l", posfrom="0,0", posto="-200,0", afrom=1, ato=0, duration=1.5)]
[Delay(time=2.5)]
[charslot(slot = "m", name = "avg_npc_1896_1#1$1", duration=1.5)]
[Delay(time=2.5)]
[SoundVolume(volume=0.2, channel="f",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blo

... (全文18285字符)
```

### level_act44side_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_warehouse_2",screenadapt="coverall")]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1918_1#10$1", duration=1, isblock=true)]
[name="萌萌香"]电视台的所有人全都乱成一团了......
[charslot(slot = "m", name = "avg_npc_1897_1#10$1")]
[name="吉星"]天啊......
[name="吉星"]奶奶以前跟我讲过，她年轻的时候，真的有北院的渗透部队进入过御机......
[name="吉星"]我听的时候不觉得有什么，可现在看来，我们面前的场面只是小意思，万一......
[dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_npc_1900_1#10$1", duration=1.5, isblock=true)]
[delay(time=0.5)]
[name="更纱"]怎么样？我送给金兵卫的这份大礼怎么样？
[charslot(slot = "m", name = "avg_npc_1897_1#10$1")]
[name="吉星"]效果可能有点......好过头了。
[charslot(slot = "m", name = "avg_npc_1900_1#9$1")]
[name="更纱"]还是专心想我们自己的事吧。森内老板已经混进了电视台，我们也该趁机到继位仪式现场去了。
[name="更纱"]那里这时应该没什么人。如果还有抵抗，吉星，你也得搭把手。
[charslot(slot = "m", name = "avg_npc_1897_1#1$1")]
[name="吉星"]明白。
[charslot(slot = "m", name = "avg_npc_1900_1#9$1")]
[name="更纱"]那现在就只剩开拔了！我来给你们带路！从这个排风口爬上去！
[dialog]
[PlaySound(key="$d_avg_metalpipe", volume=1)]
[charslot(slot = "m", posfrom="0,0", posto="50,0", afrom=1, ato=0, duration=1, isblock=true)]
[delay(time=0.5)]
[name="更纱"]你们也快上来啊！
[charslot]
[charslot(slot = "m", name = "avg_npc_1918_1#10$1")]
[name="萌萌香"]来、来了！
[dialog]
[PlaySound(key="$rungeneral", volume=1)]
[charslot(duration=0.5, isblock=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background]
[PlaySound(key="$d_avg_lightsurge", volume=0, loop=true, channel="l")]
[SoundVolume(volume=0.5, channel="l",fadetime=2)]
[Image(image="64_i15", screenadapt="coverall", xScale=1.05, yScale=1.05, fadetime=0)]
[ImageTween(xScaleFrom=1.05, yScaleFrom=1.05, xScaleTo=1, yScaleTo=1, duration=20, block=false)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[name="萌萌香"]好、好高......
[name="更纱"]别怕，萌萌香，我这里有灯。手给我，我牵着你走。
[StopSound(channel="l", fadetime=2)]
萌萌香努力控制自己不要往下看，但她的身体依然止不住地颤抖摇晃。
此刻，她们在密密麻麻的钢筋结构之间缓缓移动，头顶一片昏暗，脚下亮如白昼。
电视台的员工、黑道、忍者，乱成一团的人们就在她们正下方来来去去。
[name="更纱"]吉星，你怎么样？
[name="吉星"]还、还好。
[name="更纱"]那就好啦。
[name="更纱"]你们不常在这种地方走吗？
[name="吉星"]谁会每天在这种地方跑来跑去啦，你难道是什么叛逃的忍者吗？
[name="更纱"]那倒不是。我都是为了躲忍者，才习惯在这种地方走路的。
[name="萌萌香"]躲忍者？
[name="更纱"]嗐，那不重要——我们到了！
[name="更纱"]啧，下面还有几个人看着......
[name="更纱"]萌萌香，从这边的空隙跳过去，顺着那边的管道下到舞台上，那边是他们的视线盲区。
[name="萌萌香"]这么长的距离？！
[name="萌萌香"]我、我试试......
[dialog]
[StopSound(channel="l", fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Image]
萌萌香紧握双拳，目光直勾勾地盯着正前方，左脚往后蹬地——
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.1, block=true)]
[PlaySound(key="$d_avg_woodgear", volume=1)]
[PlaySound(key="$d_avg_erthshkng", volume=0.4, loop=true, channel="e")]
[CameraShake(duration=4, xstrength=10, ystrength=10, vibrato=90, randomness=90, fadeout=true, block=false)]
[StopSound(channel="e", fadetime=6)]
原本静止的钢筋结构突然开始运转起来，萌萌香脚下的平台也不规则地震动着。
[dialog]
[charslot(slot = "m", name = "avg_npc_1900_1#8$1")]
[name="更纱"]......怎么突然就动起来了？！
[charslot(slot = "m", action="shake", afrom=1 , ato=1, power=3, times=30, duration=0.5)]
[charslot(slot = "m", name = "avg_npc_1918_1#8$1")]
[name="萌萌香"]我、我好像要滑下去了！
[charslot(slot = "m", name = "avg_npc_1897_1#6$1")]
[name="吉星"]小心头顶！
[charslot(slot = "m", name = "avg_npc_1918_1#1$1")]
[multiline(name="萌萌香")]怎么回事......
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[charslot(slot = "m", name = "avg_npc_1918_1#8$1", posfrom="0,0", posto="0,-50", afrom=1, ato=0, duration=0.5, isblock=true)]
[multiline(name="萌萌香",end=true)]哇！
[charslot]
[charslot(slot = "m", name = "avg_npc_1897_1#2$1")]
[name="吉星"]掉下去了？！
[charslot(slot = "m", name = "avg_npc_1897_1#1$1")]
[name="吉星"]不管那么多了，更纱，我们也下去！
[dialog]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[charslot(slot = "m", name = "avg_npc_1897_1#5$1", posfrom="0,0", posto="-200,30", afrom=1, ato=0, duration=0.5)]
[name="吉星"]呀——嚯！
[dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="64_g12_stage",screenadapt="coverall")]
[charslot(slot = "r", name = "avg_npc_1907_1#1$1")]
[charslot(slot = "l", name = "avg_npc_1906_1#1$1")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[CameraShake(duration=1, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_explo_n")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[playsound(key="$bodyfalldown2")]
[charslot(slot = "l", posfrom="0,0", posto="0,-50", afrom=1, ato=0, duration=0.3)]
[Delay(time=0.1)]
[charslot(slot = "r", posfrom="0,0", posto="0,-50", afrom=1, ato=0, duration=0.3)]
[Delay(time=1)]
[charslot]
[PlaySound(key="$rungeneral", volume=1, loop=true, channel="r")]
[StopSound(channel="r", fadetime=0.5)]
[charslot(slot = "m", name = "avg_npc_1900_1#1$1", posfrom="-200,0", posto="0,0", duration=0.5, isblock=true)]
[Delay(time=0.5)]
[name="更纱"]萌萌香，你怎么样？
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_1918_1#20$1", posfrom="0,-20", posto="0,0", duration=1)]
[Delay(time=0.5)]
[name="萌萌香"]还好！我还撑得住！
[charslot(slot = "m", name = "avg_npc_1900_1#1$1")]
[name="更纱"]好，你快上舞台，我去操作台控制线路！灯光一亮你就开始！
[dialog]
[charslot]
[CameraShake(duration=1, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_explo_n", volume=0.5)]
[Delay(time=2)]
[name="吉星"]等不及要听萌萌香开嗓了——
[dialog]
[Pla

... (全文37022字符)
```

### level_act44side_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlayMusic(intro="$suspenseful_intro", key="$suspenseful_loop", volume=0.6)]
[Background(image="64_g14_mifuneoffice",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1896_1#4$1", duration=1, isblock=true)]
[name="三船"]对，是我！我刚从议员大人那里回来！
[name="三船"]星熊现在在哪里？
[charslot(slot = "m", name = "avg_npc_1896_1#7$1")]
[name="三船"]会场？！
[name="三船"]澪呢？澪控制住他们了吗？
[charslot(slot = "m", name = "avg_npc_1896_1#7$1")]
[name="三船"]没有？！她自己离开了？！
[name="三船"]叛徒！
[name="三船"]线路呢？里面的事录下来了吗？星熊的状态怎么样？
[charslot(slot = "m", name = "avg_npc_1896_1#6$1")]
[name="三船"]......该死！赶快让后期处理一下，把她和澪对打的场景处理成她已经彻底疯狂的证据——
[name="三船"]什么叫来不及？！忍客入侵？！线路劫持？！处理不了？！
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "m", name = "avg_npc_1896_1#7$1")]
[name="三船"]......废物！处理不了就赶快切断信号传输，还有供电系统！今晚已经只剩道歉声明要播了，信号掐了又能怎么样？
[name="三船"]关键是决不能让人在我的电视台不受控制地胡说八道——
[dialog]
[charslot(slot = "m", focus="n")]
[PlaySound(key="$transmission", volume=1)]
[Delay(time=1.5)]
[charslot(slot = "m", name = "avg_npc_1896_1#7$1")]
[name="三船"]喂？喂？！
[name="三船"]*东国粗口*，断线了？
[name="三船"]该死的议员，什么“要你当面解释”，我去解释，不就是给敌人乘虚而入的机会吗？！
[name="三船"]这下好了，我跟他说废话的时候，一切都乱了套，连般若都......
[charslot(slot = "m", name = "avg_npc_1896_1#6$1")]
[name="三船"]......
[charslot(slot = "m", name = "avg_npc_1896_1#2$1")]
[name="三船"]（深呼吸）
[name="三船"]冷静。
[charslot(slot = "m", name = "avg_npc_1896_1#1$1")]
[name="三船"]不就是收拾残局从头再来嘛，没事，这又不是第一次了。
[name="三船"]先去会场阻止那群混蛋，星熊的事，议员已经点了头，只要能在舆论上处理干净......
[dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_npc_1899_1#5$1", posfrom="200,0", posto="0,0", duration=1.5, isblock=true)]
[Delay(time=0.5)]
[name="哲也"]......
[charslot(slot = "m", name = "avg_npc_1896_1#9$1")]
[name="三船"]哈，跟你的星熊姐一起来捣乱了，是吗？
[charslot(slot = "m", name = "avg_npc_1899_1#5$1")]
[name="哲也"]星熊？
[charslot(slot = "m", name = "avg_npc_1896_1#10$1")]
[name="三船"]天啊，我该说你勇气可嘉呢，还是傻得可爱呢？
[charslot(slot = "m", name = "avg_npc_1896_1#9$1")]
[name="三船"]看看你这一身伤。看来我的手下还不知道你已经没用了，还在陪你过家家呢。
[name="三船"]你手里的真刀是从哪位大哥手里抢来的？告诉我，我把它还回去，不然人家会生气的。
[charslot(slot = "m", name = "avg_npc_1899_1#8$1")]
[name="哲也"]金兵卫......你......
[charslot(slot = "m", name = "avg_npc_1896_1#9$1")]
[name="三船"]我？
[charslot(slot = "m", name = "avg_npc_1896_1#1$1")]
[name="三船"]我现在没时间陪你玩，哲也君。
[name="三船"]你父亲从小教你的那几下刀法，作为基础固然不错，但要用它上阵杀敌，你还差得远，差得太远。
[name="三船"]毕竟是一对能被面具挑拨了关系的父子，他教你的刀法，你又能领会几分？
[charslot(slot = "m", name = "avg_npc_1899_1#5$1")]
[name="哲也"]挑拨？！
[charslot(slot = "m", name = "avg_npc_1899_1#6$1")] 
[name="哲也"]挑拨，是啊......挑拨......
[charslot(slot = "m", name = "avg_npc_1896_1#6$1")]
[name="三船"]该说的我都说完了。现在就给我滚，不然，我也不介意再把主意改回来，直接送你去见铁斋。
[charslot(slot = "m", name = "avg_npc_1899_1#9$1")]
[name="哲也"]该滚去见我父亲的人......是你！
[dialog]
[stopmusic(fadetime=1)]
[PlaySound(key="$d_avg_clothmovementsp", volume=1)]
[charslot(slot = "m", action="zoom", poszoom = "0.5,0.5", scale=1.05, duration = 0.2)]
[charslot(duration=0.2)]
[PlaySound(key="$e_skill_skulsrsword", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[charslot]
[Background(image="64_g12_stage",screenadapt="coverall")]
[Delay(time=2)]
[avgdisplay(id = "2", style = "bg", name = "bg_black", afrom = 1 ,ato = 0.5, duration = 2, slot = "bgover", layer = 2)]
[Blocker(a=0.1, r=0, g=0, b=0, fadetime=0, block=true)]
[Delay(time=1)]
[avgdisplay(id = "1", style = "bgeffect", name = "$eb_spotlight_02", slot = "bgover", layer = 1)]
[PlaySound(key="$d_avg_spotlight",volume=0.7)]
[delay(time=1)]
[Subtitle(text="深呼吸。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="我知道，现在有无数人都在看着我。我必须开口，告诉大家真相。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="但......这真的有用吗？", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="大家喜欢羽生萌萌香，喜欢这个怪谈缠身的偶像惊慌失措的样子。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="大家喜欢害怕的我，而不是从我口中说出的什么真相，更不是真正的我......", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="是啊，我连这个都在害怕。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="我是个胆小的人。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="害怕着什么，也许这就是紫野遥和羽生萌萌香，最大的共同点。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[PlaySound(key="$d_avg_mictest", volume=1)]
[delay(time=1)]
[PlayMusic(intro="$storyendjp_intro", key="$storyendjp_loop", volume=0.6)]
[PlaySound(key="$d_avg_higheldshosfts", volume=1)]
[charslot(slot = "m", name = "avg_4202_haruka_1#9$1", duration=1.5, isblock=true)]
[delay(time=0.5)]
[name="萌萌香"]各位观众......晚上......好。
[name="萌萌香"]这里是羽生、羽生......萌萌香。害怕怪谈，却又被怪谈缠身的羽生萌萌香。
[charslot(slot = "m", name = "avg_4202_haruka_1#22$1")]
[name="萌萌香"]非常抱歉，在刚刚发生过那么大的放送事故之后，再来打扰大家......
[dialog]
[avgdisplay(id = "1")]
[charslot]
[Blocker(a=1, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=2, block=true)]
[avgdisplay(id = "2")]
[Background(image="64_g2_jindastreet_n",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=2, block=true)]
[charslot(slot = "l", name = "avg_npc_1909_1#1$1", focus="l")]
[charslot(slot = "r", name = "avg_npc_1911_1#1$1", focus="n")]
[name="惊讶的粉丝"]萌萌亲？！
[charslot(slot = "r", name = "avg_npc_1911_1#1$1", focus="r")]
[name="疑惑的粉丝"]萌萌亲不是失踪了吗，怎么突然又冒出来了？
[charslot(slot = "l", name = "avg_npc_1909_1#1$1", focus="l")]
[name="惊讶的粉丝"]难道刚才的警报真的是怪谈？
[charslot(slot = "r", name = "avg_npc_1911_1#1$1", focus="r")]
[name="疑惑的粉丝"]那现在是......她正在怪谈中......向我们所有人求助？！
[dialog]
[Blocker(a=1, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=2, block=true)]
[chars

... (全文30032字符)
```

### level_act44side_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[CameraEffect(effect="Grayscale", amount=1, keep=true)]
[PlayMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[Background(image="64_g17_jindaalley_n",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1906_1#1$1", duration=1, isblock=true)]
[name="悲痛的黑道"]鬼姐，我最后跟你说一次，不能再往前走了！
[charslot(slot = "m", focus="n")]
[name="星熊"]我必须去救下那个人。
[charslot(slot = "m", name = "avg_npc_1906_1#1$1")]
[name="悲痛的黑道"]鬼姐！！
[charslot(slot = "m", focus="n")]
[name="星熊"]没时间了。我最后说一次，让开。
[charslot(slot = "m", name = "avg_npc_1906_1#1$1")]
[name="悲痛的黑道"]你真的还是鬼姐吗？你身上还有一点人味儿吗？
[charslot(slot = "m", focus="n")]
[name="星熊"]我......为什么不是鬼姐？
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "m", name = "avg_npc_1906_1#1$1")]
[name="悲痛的黑道"]修司已经死了，死在你的刀下！
[charslot(slot = "m", focus="n")]
[name="星熊"]修司......他......？
[charslot(slot = "m", name = "avg_npc_1906_1#1$1")]
[name="悲痛的黑道"]你不再是原来那个鬼姐了......你是鬼，你是恶鬼......
[name="悲痛的黑道"]哪怕是一同喝酒的家人，但凡挡在你的面前，你就会像砍陌生人一样，毫无顾忌地砍死......
[name="悲痛的黑道"]恶鬼！现在我挡在你的面前，你还要杀了我吗？
[charslot(slot = "m", focus="n")]
[name="星熊"]高太郎......让开。
[name="星熊"]我不能就这么回去。我得阻止金兵卫，我无论如何都得阻止金兵卫！
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "m", name = "avg_npc_1906_1#1$1")]
[name="悲痛的黑道"]恶鬼！！
[dialog]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[charslot(slot = "m", action="zoom", poszoom = "0.5,0.5", scale=1.05, duration = 0.2)]
[charslot(duration=0.2)]
[Delay(time=0.2)]
自己下意识地举起刀，只是摆了一个刀刃向前的架势。
而眼前的人举着刀朝自己猛冲过来，甚至像是主动撞上来一样，把胸膛送到了自己的刀尖之上。
是主动撞上来的，还是自己拨开了他的刀，然后......？
[name="悲痛的黑道"]恶......鬼......
[name="悲痛的黑道"]下......地狱去吧......
[name="星熊"]恶鬼？
[name="星熊"]我......恶鬼？
[name="星熊"]鬼？
[dialog]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255,g=255, b=255, fadetime=0.03, block=true)]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_swordchop_xshield", volume=1)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0.5, block=true)]
[Delay(time=1)]
[playsound(key="$d_avg_broadswordblood")]
[charslot(duration=0.2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[charslot]
[Background]
[Image(image="64_i11", screenadapt="coverall")]
[ImageTween(xScaleFrom=1.1, yScaleFrom=1.1, xScaleTo=1, yScaleTo=1, duration=20, block=false)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=4, block=true)]
[Delay(time=1)]
[CameraEffect(effect="Grayscale", fadetime=10, keep=true, initamount=1, amount=0, block=false)]
鲜血。满目的鲜血。血迷了她的眼。
有人朝自己冲过来，那就斩断。
有武器朝自己挥过来，那就反击。
更多的哭声，喊声，武器划破夜幕的风声，杂乱的声音在她胸中搅成无首无尾的一团，和心脏一同搏动，搏动，搏动——
直到那团声音彻底与她的心跳声共振，盖过了耳边响起的所有声音。
几乎失了神智的恶鬼就这样一路走，一路斩，一路留下鲜血与尸骸，一路走到那间破旧的房前，一脚把门踢开。
那里没有声音。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[image]
[CameraEffect(effect="Grayscale", amount=1, keep=true)]
[Background(image="64_g17_jindaalley_n",screenadapt="coverall")]
[focusout(type="bg", id="64_g17_jindaalley_n", from=0, to=1, duration=0.1, block=false)]
[bgeffect(name="$eb_bloodfalling",layer=1)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
于是，恶鬼就这样站在门口，侧着头，仿佛在谛听从地狱传来的，常人根本无法听见的声音。
直到一个颤抖着的声音响起。
[name="三船"]......死了。
谁死了？
[name="三船"]议员候选人......死了。
议员候选人死了？
哭声远去，喊声远去，武器的破空声远去，心跳也远去，一切声音都离她而去。
只有那些从地狱传来的声音，比任何时候都清晰地回响在她耳边。
鬼。
恶鬼。
下地狱去吧。
......
[dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[bgeffect]
[Background(image="64_g16_jindadike",screenadapt="coverall")]
[CameraEffect(effect="Grayscale", amount=0, keep=true)]
[focusout(type="bg", id="bg_ibindoor", from=1, to=0, duration=0.1, block=false)]
[PlaySound(key="$d_avg_firework_amb", volume=0, loop=true, channel="f")]
[SoundVolume(volume=0.3, channel="f",fadetime=2)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_hidehaystack", volume=1)]
[charslot(slot = "m", name = "avg_npc_1896_1#1$1", duration=1.5, isblock=true)]
[Delay(time=0.5)]
[PlayMusic(key="$m_avg_darkduel_loop", volume=0.6)]
[name="三船"]就在这里。
[name="三船"]我没把位置选在刚刚那一路的废墟里，特意挑了这块河边上的荒地，免得你触景生情。不用感谢我。
[dialog]
[delay(time=1.5)]
[charslot(slot = "m", name = "avg_npc_1896_1#9$1")]
[name="三船"]我们来得真是时候。花火大会还没结束。
[charslot(slot = "m", name = "avg_1044_hsgma2_1#4$2")]
[name="星熊"]......
[charslot(slot = "m", name = "avg_npc_1896_1#9$1")]
[name="三船"]怎么，临要动手，反而又迟疑了？
[charslot(slot = "m", name = "avg_1044_hsgma2_1#5$2")]
[name="星熊"]不。
[name="星熊"]我只是想在动手之前，把一切都问清楚。
[charslot(slot = "m", name = "avg_npc_1896_1#1$1")]
[name="三船"]还有什么事不清楚？
[charslot(slot = "m", name = "avg_1044_hsgma2_1#2$2")]
[name="星熊"]只有一件事。
[charslot(slot = "m", name = "avg_1044_hsgma2_1#7$2")]
[name="星熊"]你的恨，从何而来？
[name="星熊"]我在电视台遇见哲也了。我听他说了铁斋叔死时的事。你本可以不那么残忍。
[name="星熊"]我不知道铁斋叔这些年是怎么对你的，但你能走到架空他的这一步，他至少应该没有把你当成假想敌。
[name="星熊"]而我，我自认为对你仁至义尽。甚至在我刚回御机的时候，我想的不过是，希望自己的牺牲不要毫无意义——
[charslot(slot = "m", name = "avg_npc_1896_1#9$1")]
[name="三船"]牺牲？
[charslot(slot = "m", name = "avg_npc_1896_1#6$1")]
[name="三船"]对，这就是你，还有铁斋，你们最让我作呕的地方。
[name="三船"]你是个傻瓜，他比你更傻。哪怕真是你误杀了议员候选人，他难道不知道用当时也在房间里的我顶罪吗？
[name="三船"]他偏爱你，所以我一直在等，等他哪天让我去把杀人的罪责“顶下来”。
[name="三船"]至少在当时，这是对他最好的结果，他保了自己偏爱的你，拔除了敢背着他擅自行动的我。
[name="三船"]至于所谓“杀了兄弟的人”，那重要吗？般若在你手里，他的支持在你背后，谁敢嚼这种不要命的舌头？！
[charslot(slot = "m", name = "avg_1044_hsgma2_1#7$2")]
[name="星熊"]......
[charslot(slot = "m", name = "avg_npc_1896_1#2$1")]
[name="三船"]结果，他却选了大义灭亲，选了“任侠”......简直让人想吐。
[charslot(slot = "m", name = "avg_npc_1896_1#1$1")]
[name="

... (全文22734字符)
```

### level_act44side_entry

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK",is_video_only=true)] 
[stopmusic]
[Background(image="bg_black",screenadapt="coverall")]
[playMusic(intro="$empty",key="$empty")]
[Video(res="video/act44side/AT01.mp4")]
```

### level_act44side_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[bgeffect(name="$eb_tvnoise",layer=3)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.7, block=true)]
[Background(image="64_g2_jindastreet_n",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Delay(time=1)]
[playMusic(intro="$nervous_intro",key="$nervous_loop", volume=0.6)]
[charslot(slot="m",name="avg_npc_1906_1#1$1",duration=1)]
[delay(time=2)]
[name="次郎"]鬼姐，我最后跟你说一次，不能再往前走了！
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1919_1#1$1",duration=1.5)]
[delay(time=2)]
[name="“鬼”"]我必须去杀了那个人。
[charslot(slot="m",name="avg_npc_1906_1#1$1")]
[name="次郎"]老大亲口说的，不能让你靠近了！
[charslot(slot="m",name="avg_npc_1919_1#1$1")]
[name="“鬼”"]......没时间了。次郎，我最后说一次，让开。
[charslot(slot="m",name="avg_npc_1906_1#1$1")]
[name="次郎"]鬼姐！！
[charslot(slot="m",name="avg_npc_1919_1#1$1")]
[name="“鬼”"]次郎，连你也要拦我？
[charslot(slot="m",name="avg_npc_1906_1#1$1")]
[name="次郎"]我拦不住你，只想和你再喝一次酒，行吗？
[name="次郎"]不是拖延，就......再喝一次酒。喝完，我们就决生死。
[charslot(slot = "m", focus = "n")]
[PlaySound(key="$pourwater", volume=1)]
被称为“鬼姐”的女性默默地看着。黑道从怀里掏出酒，给两边各倒了一杯。
[charslot(slot="m",name="avg_npc_1906_1#1$1")]
[name="次郎"]喝吧。
[charslot]
[PlaySound(key="$d_avg_drinkswllw", volume=1)]
“鬼姐”仰头，米酒落入腹中，却火辣得像是刀绞。
[dialog]
[charslot(slot="m",name="avg_npc_1919_1#1$1")]
[charslot(slot ="m", action="shake", power=6, times=30, duration=0.3)]
[delay(time=0.5)]
[name="“鬼”"]次郎，你？！
[charslot(slot="m",name="avg_npc_1906_1#1$1")]
[name="次郎"]那个人，我无论如何都要保。
[name="次郎"]他是你的仇人，但他也是我的恩人。
[name="次郎"]如果他死在这里，他只是我一个人的恩人。如果他活了下来，总有一天，他会成为整个御机的恩人。对不起，鬼姐。
[CameraShake(duration=0.6, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[bgeffect(name="$eb_blackfire",layer=1)]
[PlaySound(key="$firestorm", volume=0.7)]
[charslot(slot="m",name="avg_npc_1919_1#1$1")]
[name="“鬼”"]呜哦哦哦哦哦哦！！！
[charslot(slot = "m", focus = "n")]
腹中的绞痛化作烈火，与脑海中的怒火一同在胸口炸裂。
与整个时代逆向而行的高尚者，恩怨分明、义烈任侠的极道，此刻沦为失却了一切理智的、只知杀人的恶鬼。
她手中的般若此刻已经与经书中的大智慧毫无干涉，只余比狂怒的般若之面更炽烈的，毫不顾念往日情分的，疯狂的愤怒。
[CameraShake(duration=0.3, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=false, block=false)]
[charslot(slot="m",name="avg_npc_1919_1#1$1")]
[name="“鬼”"]喝啊！
[dialog]
[bgeffect(layer=1)]
[charslot(slot="m",name="avg_npc_1906_1#1$1")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255,g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=1)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0.5, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[avgdisplay(id = "1", style = "bgeffect", name = "$eb_bloodfalling", slot = "bgover", layer = 1)]
[delay(time=0.8)]
[charslot(slot = "m",posfrom = "0,0", posto = "0,-60",duration = 0.4)]
[charslot(duration=0.3)]
[CameraShake(duration=0.2, xstrength=15, ystrength=15, vibrato=20, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$bodyfalldown2", volume=1)]
[delay(time=2)]
[charslot]
[charslot(slot="m",name="avg_npc_1907_1#1$1")]
[name="黑道A"]鬼姐？！
[dialog]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255,g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=1)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0.5, block=true)]
[name="黑道A"]咕！
[dialog]
[charslot(slot = "m",posfrom = "0,0", posto = "0,-60",duration = 0.4)]
[charslot(duration=0.3)]
[CameraShake(duration=0.2, xstrength=15, ystrength=15, vibrato=20, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$bodyfalldown2", volume=1)]
[delay(time=1.5)]
[charslot]
[charslot(slot="m",name="avg_npc_1906_1#1$1")]
[name="黑道B"]阻止她——
[dialog]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255,g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=1)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0.5, block=true)]
[name="黑道B"]呃啊！
[dialog]
[charslot(slot = "m",posfrom = "0,0", posto = "0,-60",duration = 0.4)]
[charslot(duration=0.3)]
[CameraShake(duration=0.2, xstrength=15, ystrength=15, vibrato=20, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$bodyfalldown2", volume=1)]
[delay(time=1.5)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[charslot(slot="m",name="avg_npc_1907_1#1$1")]
[Background(image="64_g17_jindaalley_n",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[name="黑道C"]鬼姐、鬼姐她彻底疯了——
[dialog]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255,g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=1)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0.5, block=false)]
[charslot(duration=0.3)]
[CameraShake(duration=0.2, xstrength=15, ystrength=15, vibrato=20, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$bodyfalldown1", volume=1,delay=0.5)]
[delay(time=1.5)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="m",name="avg_npc_1919_1#1$1",duration=1)]
[delay(time=2)]
[name="“鬼”"]挡我者......死。
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1908_1#1$1",duration=1)]
[delay(time=2)]
[name="议员候选人"]......
[name="议员候选人"]时代，变革，福祉......
[name="议员候选人"]对你而言，这些词汇都已经太空洞，说再多，也无法救赎你了......
[name="议员候选人"]恶鬼。
[charslot(slot="m",name="avg_npc_1919_1#1$1")]
[name="“鬼”"]聒噪......
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=fals

... (全文29859字符)
```

### level_act44side_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="64_g8_tessaihome",screenadapt="coverall")]
[PlayMusic(intro="$ponder_intro", key="$ponder_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1897_1#1$1", duration=1.5)]
[charslot(slot = "l", name = "avg_npc_1918_1#1$1", duration=1.5)]
[Delay(time=2)]
[charslot(slot = "l", name = "avg_npc_1918_1#1$1", focus="l")]
[name="萌萌香"]铁斋先生在内室待了这么长时间，有点让人担心......
[charslot(slot = "r", name = "avg_npc_1897_1#1$1", focus="r")]
[name="吉星"]担心他干什么。老爷子做起铁匠活就跟你唱歌、星熊打架、我打小钢珠差不多。
[charslot(slot = "l", name = "avg_npc_1918_1#3$1", focus="l")]
[name="萌萌香"]你打小钢珠也很厉害吗？
[charslot(slot = "r", name = "avg_npc_1897_1#5$1", focus="r")]
[name="吉星"]这个——啊哈哈......
[charslot]
为了转移话题，吉星从面前的点心盘上拿起一枚饼干塞进嘴里。
[charslot(slot = "r", name = "avg_npc_1897_1#10$1", focus="r")]
[charslot(slot = "l", name = "avg_npc_1918_1#1$1", focus="n")]
[name="吉星"]糟糕，饼干都快被我吃完了。
[charslot(slot = "l", name = "avg_npc_1918_1#1$1", focus="l")]
[name="萌萌香"]为什么铁斋先生家的饼干全都是二之宫牌经典瘤奶味？他喜欢这个口味？
[charslot(slot = "r", name = "avg_npc_1897_1#2$1", focus="r")]
[name="吉星"]还不是哲也以前喜欢这个味的。
[charslot(slot = "l", name = "avg_npc_1918_1#20$1", focus="l")]
[name="萌萌香"]要是哲也能认清金兵卫的面目......
[charslot(slot = "r", name = "avg_npc_1897_1#2$1", focus="r")]
[name="吉星"]他要是能认清，早就认清了。
[name="吉星"]而且我也得说句公道话，哲也跟着金兵卫瞎混是果，真正的因，还是在铁斋老爷子身上——
[dialog]
[stopmusic(fadetime=2)]
[PlaySound(key="$d_avg_trnpndor", volume=1)]
[Delay(time=1.5)]
[charslot(slot = "r", focus="n")]
[name="？？？"]铁斋要是有你一半见识就好了，吉星小姐。
[dialog]
[charslot]
[PlayMusic(intro="$plot_intro", key="$plot_loop", volume=0.6)]
[PlaySound(key="$d_avg_woodfloor_fts", volume=1)]
[charslot(slot = "m", name = "avg_npc_1896_1#9$1", duration=1.5)]
[Delay(time=2)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "m", name = "avg_npc_1897_1#8$1")]
[name="吉星"]金兵卫？！
[charslot(slot = "m", name = "avg_npc_1897_1#7$1")]
[name="吉星"]萌萌香，你进内室，我来拖住这家伙！
[charslot(slot = "m", name = "avg_npc_1896_1#9$1")]
[name="三船"]别急着开打，年轻人。
[dialog]
[charslot]
[PlaySound(key="$d_avg_footsteps_tatami", volume=1)]
[charslot(slot = "m", name = "avg_npc_1895_1#1$1", duration=1.5)]
[Delay(time=2)]
[name="铁斋"]......
[charslot(slot = "m", name = "avg_npc_1896_1#10$1")]
[name="三船"]哦哦，失敬。会长大人亲自在家里迎接，真让人不胜感激。
[charslot(slot = "m", name = "avg_npc_1895_1#1$1")]
[name="铁斋"]星熊呢？
[charslot(slot = "m", name = "avg_npc_1896_1#9$1")]
[name="三船"]我的人正好好招待她呢，不会让她来帮你们的。
[charslot(slot = "m", name = "avg_npc_1897_1#7$1")]
[name="吉星"]乘虚而入，卑鄙！
[charslot(slot = "m", name = "avg_npc_1896_1#9$1")]
[name="三船"]还不如说是你们自己棋错一着。我还想着怎么用森内把她钓出来，没想到她自己就上了钩。
[name="三船"]不过呢，我也不想动不动打打杀杀的。早不是那个时代了，诸位。
[name="三船"]我是来诚挚邀请铁斋会长，参加我的继位仪式的。
[charslot(slot = "m", name = "avg_npc_1918_1#13$1")]
[name="萌萌香"]继位仪式？
[charslot(slot = "m", name = "avg_npc_1896_1#9$1")]
[name="三船"]是啊。
[name="三船"]既然老爷子无论如何都不愿意把锻冶町让出来，我也只好略略冒犯一下，接过金石会会长这个有名无实的位置。
[name="三船"]会长，你要是觉得丢面子，不愿出席，也可以把般若交到我手里，有它在，仪式同样办得下去。
[charslot(slot = "m", name = "avg_npc_1895_1#6$1")]
[name="铁斋"]般若不是什么继承人的信物，以前不是，现在也不是！
[charslot(slot = "m", name = "avg_npc_1896_1#9$1")]
[name="三船"]只要所有人都相信，它就会是。
[charslot(slot = "m", name = "avg_npc_1896_1#1$1")]
[name="三船"]而你，你太偏爱星熊，你甚至都没有意识到这一点，是不是？
[name="三船"]还是说，你为了羞辱我，这才在星熊远走龙门之前把般若给了她？我究竟哪里做得不好，让你这么厌恶我？
[charslot(slot = "m", name = "avg_npc_1895_1#6$1")]
[name="铁斋"]......你太把自己当回事了。
[charslot(slot = "m", name = "avg_npc_1896_1#9$1")]
[name="三船"]对，太对了，我就是想听这个！
[name="三船"]可惜啊，老东西，不是我把自己当回事，是你，除了你看得上眼的星熊之外，没有把任何人当回事！
[charslot]
三船一个人站在门口放声大笑。
萌萌香和吉星缓缓退到铁斋身后。
[charslot(slot = "m", name = "avg_npc_1896_1#9$1")]
[name="三船"]我早点告诉你这一点，说不定你儿子也不至于和你反目成仇。
[charslot(slot = "m", name = "avg_npc_1895_1#7$1")]
[name="铁斋"]提哲也干什么？别以为我是为了传位给那混小子才和你过不去。他根本就没有统领整个金石会的器量。
[charslot(slot = "m", name = "avg_npc_1896_1#9$1")]
[name="三船"]知道，他也是你看不上眼的人之一。
[charslot(slot = "m", name = "avg_npc_1895_1#6$1")]
[name="铁斋"]别废话了。我也许打不赢你，不过和你耗下去，耗到星熊回来，不是什么难事。这可是我家。
[name="铁斋"]正好也拿你试试新铸的般若。
[charslot(slot = "m", name = "avg_npc_1896_1#9$1")]
[name="三船"]试斩？好啊。
[name="三船"]不过在那之前，你要不要先看看这个？
[charslot]
三船把手伸入怀中。
铁斋紧盯着他的动作，那只手却只是从怀中掏出几张轻飘飘的照片，随随便便扔在地上。
其中一张正面朝上的照片恰好落在铁斋面前，被他的余光扫到——
[charslot(slot = "m", name = "avg_npc_1895_1#5$1")]
[name="铁斋"]哲也？！
[charslot(slot = "m", name = "avg_npc_1896_1#9$1")]
[name="三船"]哲也。
[name="三船"]真是个好孩子，我吩咐的事情，不管在不在能力范围之内，他都尽心竭力去办。
[charslot(slot = "m", name = "avg_npc_1896_1#10$1")]
[name="三船"]就像现在，这个北院来的间谍还真被他找到了......虽然他找到的好像是他自己。
[charslot(slot = "m", name = "avg_npc_1895_1#6$1")]
[name="铁斋"]你——你？！
[charslot(slot = "m", name = "avg_npc_1896_1#1$1")]
[name="三船"]刚开始看到这些照片的时候，我也很意外，但转念一想，倒也合理。
[name="三船"]哲也的母亲当年只是思念北方亲人，尽管对面的人确实有将她发展成间谍的意思，她却严词拒绝。
[name="三船"]可我们金石会暗中采购的那些武器，上面却实打实地印着帆足家的家徽。
[charslot(slot = "m", name = "avg_npc_1896_1#2$1")]
[name="三船"]也怪我，当时金石会下属的电视台还没像今天这样举足轻重，消息一传出去，那些想让金石会倒霉的人就都涌了上来。
[name="三船"]最后我帮你给那些武器找了个好去处，可善后还得你自己来。你不得不把哲也的母亲推出去，就像当年把星熊推出去一样。
[charslot(slot = "m", name = "avg_npc_1896_1#6$1")]
[name="三船"]在你心中，金石会就是将棋棋盘上的“王将”。
[name="三船"]为了它能存续下去，不管是星熊这样的“金将”，还是我这种你永远看不上的“成金”，该舍的时候，你从来不会犹豫。
[name="三船"]所以我其实很好奇......哲也在你心中，又算什么？
[name="三船"]“飞车”？“角行”？还是说，这孩子实在有些废物，无非是个舍了也毫不心疼的“步兵”？
[charslot(slot = "m", name = "avg_npc_1896_1#9$1")]
[name="三船"]要真是那样，我们今天真的还得打上一架了。但你不会的，对不对？
[name="三船"]他的确是个废物，但他可不是你棋盘上的棋子，他是你这个棋手的好大儿，绝对不能放在棋盘上比较的东西——
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "m", name = "avg_npc_1895_1#6$1")]
[name="铁斋"]闭嘴！
[charslot]
老人浑身紧绷，下一秒马上就要举盾冲向三船。
但三船看得见，般若正在他手中微微颤抖。
[charslot(slot = "m", name = "avg_npc_1896_1#4$1")]
[name="三船"]孩子的母亲已经永远都不可能洗清了，如果连你仅剩的这么一个孩子也落得同等下场......
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "m", name = "avg_npc_1895_1#7$1")]
[

... (全文29521字符)
```

### level_act44side_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlayMusic(key="$normal_loop", volume=0.6)]
[Background(image="bg_park",screenadapt="coverall")]
[PlaySound(key="$d_avg_livelystreet", volume=0, loop=true, channel="li")]
[SoundVolume(volume=1, channel="li",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[StopSound(channel="li", fadetime=2)]
[charslot(slot = "r", name = "avg_1033_swire2_1#8$1", duration=1.5)]
[charslot(slot = "l", name = "avg_4080_lin_1#1$1", duration=1.5)]
[Delay(time=2)]
[charslot(slot = "l", name = "avg_4080_lin_1#1$1", focus="l")]
[name="林雨霞"]她真就写了这么一句话？
[charslot(slot = "r", name = "avg_1033_swire2_1#5$1", focus="r")]
[name="诗怀雅"]我有必要骗你吗？她的信还在我这儿呢。要看吗？
[dialog]
[playsound(key="$d_avg_paper1",volume=1)]
[delay(time=0.5)]
[playsound(key="$d_avg_paper2",volume=1)]
[delay(time=1)]
[charslot(slot = "l", name = "avg_4080_lin_1#2$1", focus="l")]
[name="林雨霞"]（清嗓子）
[charslot(slot = "l", name = "avg_4080_lin_1#9$1", focus="l")]
[name="林雨霞"]*龙门粗口*，我听说你爷爷被你气走了？！
[name="林雨霞"]......没有落款，全信完。
[charslot(slot = "l", name = "avg_4080_lin_1#3$1", focus="l")]
[name="林雨霞"]噗。
[charslot(slot = "r", name = "avg_1033_swire2_1#5$1", focus="r")]
[name="诗怀雅"]这你也笑得出来？
[charslot(slot = "l", name = "avg_4080_lin_1#10$1", focus="l")]
[name="林雨霞"]第一，我不知道她字写快了居然有点像狂草。
[name="林雨霞"]第二，不是在她亲自把这封信拍在你脸上之后，事情就解释清楚了吗，“诗怀雅局长”？
[charslot(slot = "r", name = "avg_1033_swire2_1#5$1", focus="r")]
[name="诗怀雅"]臭老鼠！要不是那家伙还别别扭扭的，你看我找不找你！
[charslot(slot = "l", name = "avg_4080_lin_1#1$1", focus="l")]
[name="林雨霞"]我本来也不用你找。我们见面越少越好。
[CameraShake(duration=0.3, xstrength=15, ystrength=15, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "r", name = "avg_1033_swire2_1#11$1", focus="r")]
[name="诗怀雅"]你！
[name="诗怀雅"]我宣布，你碗里最后一颗鳞丸归我了。
[charslot(slot = "l", name = "avg_4080_lin_1#10$1", focus="l")]
[name="林雨霞"]请便，就当是错怪你的赔罪了。
[charslot(slot = "r", name = "avg_1033_swire2_1#10$1", focus="r")]
[name="诗怀雅"]你可真轻描淡写啊，臭老鼠。
[charslot(slot = "l", name = "avg_4080_lin_1#10$1", focus="l")]
[name="林雨霞"]那你还想怎样？在新汐斯塔和你爷爷对着干，至少这事不能算我错怪你吧？
[charslot(slot = "r", name = "avg_1033_swire2_1#5$1", focus="r")]
[name="诗怀雅"]哼。
[charslot(slot = "r", name = "avg_1033_swire2_1#8$1", focus="r")]
[name="诗怀雅"]不过你说......我是不是也该找星熊聊聊？
[charslot(slot = "l", name = "avg_4080_lin_1#1$1", focus="l")]
[name="林雨霞"]应该，但是不合适。
[charslot(slot = "r", name = "avg_1033_swire2_1#4$1", focus="r")]
[name="诗怀雅"]是啊，我知道她最近要么躲着我，要么就一本正经地叫我官职，但其实我能看出来，我们俩并没有变生分。
[name="诗怀雅"]毕竟发生了这么多事，她得避嫌，她错怪了我不好意思，还有，毕竟她那边也算是长辈去世......
[charslot(slot = "l", name = "avg_4080_lin_1#10$1", focus="l")]
[name="林雨霞"]她没那么敏感。
[charslot(slot = "r", name = "avg_1033_swire2_1#10$1", focus="r")]
[name="诗怀雅"]是吗？我觉得她偶尔也有点多愁善感......也不能这么说，嗯，我想想，怎么描述她那种状态呢......
[charslot(slot = "l", name = "avg_4080_lin_1#10$1", focus="l")]
[name="林雨霞"]等陈晖洁回来，说不定可以帮你一起想。
[charslot(slot = "l", name = "avg_4080_lin_1#3$1", focus="l")]
[name="林雨霞"]但我的意思是说，她现在那副样子，可能根本就不是因为她想了那么多，只是单纯想拿你寻开心而已。
[CameraShake(duration=0.3, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[charslot(slot = "r", name = "avg_1033_swire2_1#11$1", focus="r")]
[name="诗怀雅"]臭！老！鼠！
[name="诗怀雅"]星熊我知根知底，她才不像你，一百个心眼，老奸巨猾！
[charslot(slot = "l", name = "avg_4080_lin_1#3$1", focus="l")]
[name="林雨霞"]承蒙夸奖。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_lungmenbridge",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "r", name = "avg_1044_hsgma2_1#2$1", focus="n")]
[charslot(slot = "l", name = "avg_npc_1645_1#4$1", focus="l")]
[name="文月"]多谢星熊督察帮我带的伴手礼。
[charslot(slot = "r", name = "avg_1044_hsgma2_1#1$1", focus="r")]
[name="星熊"]您客气。
[charslot(slot = "l", name = "avg_npc_1645_1#3$1", focus="l")]
[name="文月"]星熊督察去东国的这段时日，不知怎的，我竟然没少光顾那家姜齐煎饼店，吃到后来，竟然也觉得葱段味道很美。
[charslot(slot = "l", name = "avg_npc_1645_1#4$1", focus="l")]
[name="文月"]不过，据说星熊督察在御机也遭逢不少变故，还能想着替我带东西，这份心意实在是弥足珍贵。
[charslot(slot = "r", name = "avg_1044_hsgma2_1#1$1", focus="r")]
[name="星熊"]都是我应该做的。
[name="星熊"]再说我在御机也惹了不少麻烦，万幸没闹到惊动夫人，惊动魏先生，让龙门难办那一步。
[charslot(slot = "l", name = "avg_npc_1645_1#4$1", focus="l")]
[name="文月"]没有的事。我听说的都是你智勇双全，不仅洗脱自己的冤屈，还替情同义父的铁斋先生报仇的佳话。
[name="文月"]那个金兵卫本来也不是善类，被捕受审是理所当然。星熊督察心存善念，没有下重手，这才是便宜了他。
[charslot(slot = "r", name = "avg_1044_hsgma2_1#2$1", focus="r")]
[name="星熊"]......夫人，我还有一件事想问。
[charslot(slot = "l", name = "avg_npc_1645_1#4$1", focus="l")]
[name="文月"]不必拘泥，问就是了。上次我在街上开快了一点，你别停我的时候也没这么扭扭捏捏的。
[charslot(slot = "r", name = "avg_1044_hsgma2_1#5$1", focus="r")]
[name="星熊"]我从御机回来之后，其实一直在想......
[name="星熊"]龙门和御机......究竟有何不同？
[name="星熊"]为什么我已经可以心安理得地说自己是龙门人，可御机对我而言，却无论如何也没法再当成一个家？
[charslot(slot = "r", name = "avg_1044_hsgma2_1#4$1", focus="r")]
[name="星熊"]因为林先生对黑道管理有方？因为龙门没有所谓神明？不，原因不该是这些。
[charslot(slot = "l", name = "avg_npc_1645_1#4$1", focus="l")]
[name="文月"]......
[charslot(slot = "l", name = "avg_npc_1645_1#2$1", focus="l")]
[name="文月"]星熊，一座城市里最重要的，只有人，一个一个的，生活在城市里的，活生生的人。
[name="文月"]是人就会做梦，而一座城里的人在做什么样的梦，这座城市就会传颂什么样的故事。
[charslot(slot = "r", name = "avg_1044_hsgma2_1#2$1", focus="r")]
[name="星熊"]夫人是说......？
[charslot(slot = "l", name = "avg_npc_1645_1#4$1", focus="l")]
[name="文月"]御机在做的梦，龙门早已醒了。
[charslot(slot = "r", name = "avg_1044_hsgma2_1#2$1", focus="r")]
[name="星熊"]......
[charslot(slot = "l", name = "avg_npc_1645_1#4$1", focus="l")]
[name="文月"]好在你仍然在那边交了一些好朋友。
[charslot(slot = "r", name = "avg_1044_hsgma2_1#1$1", focus="r")]
[name="星熊"]大概是我这趟回御机最大的收获。
[charslot(slot = "l", name = "avg_npc_1645_1#4$1", focus="l")]
[name="文月"]有收获，那不就很好嘛。
[name="文月"]正好我也有件奇闻要跟督察分享。
[charslot(slot = "r", name = "avg_1044_hsgma2_1#1$1", focus="r")]
[name="星熊"]什么事？
[charslot(slot = "l", name = "avg_npc_1645_1#3$1", focus="l")]
[name="文月"]说是和御机邻近的姬户城，最近出现了一名少年英侠。
[name="文

... (全文22179字符)
```

### training_act44side_01_a

```
[HEADER(is_tutorial=true, is_autoable=false, is_skippable=false)]

[Battle.LockFunction(mask="SYSTEM_MENU_INTERACT")]
[Battle.SwitchToDefaultUIState]
[Delay(time=0.5)]
[Battle.Pause]
[Battle.EnsureMinSp(charId="trap_252_pckstp", sp=30)]
[Battle.UnlockFunction(mask="CHARACTER_MENU")]
[InputBlocker(blockInput=true, tileX=1, tileY=7, validWidth=85, validHeight=85)]
[Tutorial(tileX=1, tileY=7, focusWidth=85, focusHeight=85, waitForSignal="char_info", \
          animStyle="Click", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_hsguma", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 我老家有些人管这个发射器叫“天命来袭”，顾名思义，用了这个，总有一刻能逆天改命。
[InputBlocker(blockInput=true)]

[Delay(time=0.3)]
[Tutorial(target="btn_skill", waitForSignal="use_skill", \
          animStyle="Click", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_hsguma")] 博士要试试吗？打开它就能释放出“某种天命”。
[InputBlocker(blockInput=true)]
[Battle.lockFunction(mask="CHARACTER_MENU")]
```

### training_act44side_01_b

```
[HEADER(is_tutorial=true, is_autoable=false, is_skippable=false)]

[Battle.LockFunction(mask="SYSTEM_MENU_INTERACT")]
[Battle.Pause]
[Tutorial(tileX=5, tileY=2, focusWidth=85, focusHeight=85, animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_hsguma", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 这是幸运宝座，只要站上去就能吸收“某种天命”获得“眷顾”。阻挡数越高获得的“眷顾”就越高。
[Battle.EnsureMinSp(charId="trap_252_pckstp", sp=0)]
[Battle.UnlockFunction(mask="SYSTEM_MENU_INTERACT")]
[Battle.Pause(pause=false)]
[InputBlocker(blockInput=true)]
[Delay(time=2.5)]

[Battle.LockFunction(mask="SYSTEM_MENU_INTERACT")]
[Battle.Pause]

[Tutorial(focusX=8, focusY=-95, focusWidth=500, focusHeight=18.5, anchor="Top", \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_hsguma", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 等到“眷顾”攒够了，那些“天命来袭”就都会被激活，大家都管这种状态叫“强运”。

[Battle.EnsureMinSp(charId="trap_252_pckstp#2", sp=30)]
[Battle.UnlockFunction(mask="CHARACTER_MENU")]
[InputBlocker(blockInput=true, tileX=1, tileY=1, validWidth=85, validHeight=85)]
[Tutorial(tileX=1, tileY=1, focusWidth=85, focusHeight=85, waitForSignal="char_info", \
          animStyle="Click", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_hsguma")] 但平时的话，您一次只能操作一台“天命来袭”，其他的机器会自动关机。
[InputBlocker(blockInput=true)]

[Delay(time=0.3)]
[Tutorial(target="btn_skill", waitForSignal="use_skill", \
          animStyle="Click", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_hsguma")] 我们试试这台吧。
[InputBlocker(blockInput=true)]
[Battle.UnlockFunction(mask="SYSTEM_MENU_INTERACT")]
```


> 本章节共35个脚本文件，此处展示前30个。

## 统计

- 总字符数：464469
- 对话行数：3437


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
