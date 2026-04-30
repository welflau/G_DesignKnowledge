# 明日方舟 · 活动剧情 · act1lock（5段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act1lock」完整剧情脚本（5个文件，120行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act1lock
- 脚本文件数：5

### guide_act1lock_defend

```
[HEADER(is_skippable=false, is_tutorial=true)] 驻守关卡新手引导
[Interlock.EnsureMapStatus]
[PopupDialog(dialogHead="$avatar_doberm")] 恭喜，博士。我听特别甄选代表报告，你们已经完成了【最终试炼场所】的初次挑战。
[PopupDialog(dialogHead="$avatar_doberm")] 你应该还记得规则。想要进行更高效的作战，接下来将可以通过挑战新解锁的【据点】关卡并进行驻守，以此增加【最终试炼场所】中额外的【特殊假想敌】。
[PopupDialog(dialogHead="$avatar_doberm")] 击败这些敌人，将获得更多的收益。
[Tutorial(target="pool_btn_interlock_first_defend", waitForSignal="interlock_stage_first_defend_detail_shown",            animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 首先，选择其中一个【据点】关卡。
[Tutorial(focusX=746, focusY=190, focusWidth=891, focusHeight=161, anchor="BottomLeft",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_doberm")]  在【据点】关卡，可以安排行动干员进行驻守。只有在据点保持驻守时，才会在【最终试炼场所】中出现额外的【特殊假想敌】。
[PopupDialog(dialogHead="$avatar_doberm")] 当我们通关【据点】关卡后，将选择是否让通关的所有行动干员进行【驻守】。只有确认进行驻守，才会有相应的【特殊假想敌】出现在【最终试炼场所】关卡中。
[PopupDialog(dialogHead="$avatar_npc012")] 杜宾教官，我想再确认一下，派去据点进行驻守的干员，不能再参与其它【据点】关卡和【最终试炼场所】关卡的作战了吗？
[PopupDialog(dialogHead="$avatar_doberm")] 没错。任何干员的擅自离开都会为据点驻守造成不确定性。不过根据规则，占领据点并非强制要求。驻守中的干员随时可以撤离，为更加合理的行动人员调配做准备。
[PopupDialog(dialogHead="$avatar_doberm")] 我们的目的，仍将是保留最强大的实力在【最终试炼场所】关卡进行挑战。
[PopupDialog(dialogHead="$avatar_doberm")] 占领越多的据点，意味着参赛小队已经准备好将花费更多的精力，在【最终试炼场所】中面临更危险的挑战。我们尚不知那些额外的敌人会有怎样的实力。
[PopupDialog(dialogHead="$avatar_npc012")] 多说无益。敌人到底有多少实力，交手后自然就知道了。
```

### guide_act1lock_finalstage

```
[HEADER(is_skippable=false, is_tutorial=true)] 最终试炼新手引导
[Interlock.EnsureMapStatus]
[PopupDialog(dialogHead="$avatar_npc012")] 报告，我们已经在第一处【据点】驻守成功。根据观察，在驻守成功后，场地氛围发生了一定改变，之后也可以据此确认驻守是否成功。
[Tutorial(target="pool_btn_interlock_first_final",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_npc012")] 第一个额外的【特殊假想敌】已经进入了【最终试炼场所】了。
[Tutorial(target="pool_btn_interlock_first_final", waitForSignal="interlock_stage_final_detail_shown",           animStyle="Click", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_npc012")] 【最终试炼场所】的情报也已经更新了。
[PopupDialog(dialogHead="$avatar_npc012")] 原来如此……已经确认【特殊假想敌】到达了【最终试炼场所】。这样，在关卡中应该就可以向敌人发起挑战了。
[PopupDialog(dialogHead="$avatar_doberm")] 嗯。要注意，击败【特殊假想敌】可以获取额外奖励。相应地，进入【最终试炼场所】时，理智的消耗也会提升。
[Tutorial(focusX=-539, focusY=71, focusWidth=157, focusHeight=89, anchor="BottomRight",           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_doberm")] 如果【特殊假想敌】进入目标点，不会扣除关卡生命值，且关卡结束后将会退还相应增加的理智。这一点可以在【返还规则】中查看。
[PopupDialog(dialogHead="$avatar_npc012")] 了解。
[PopupDialog(dialogHead="$avatar_doberm")] 我没有什么别的好提醒的了。博士，接下来不论是直接开始挑战，亦或是去更多据点进行驻守。联锁竞赛的中的作战指挥，便全权交给你了。
```

### level_act1lock_entry

```
[HEADER(key="title_test", is_skippable=false, fit_mode="BLACK_MASK")] 固定开头avg
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_rhodescom",screenadapt="coverall")]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[name="？？？"]  ......这样的提案......是出于对我们的信任，亦或是另有所图？
[name="？？？"]  ......我不能够确定，但是，这无疑是一次......机会。
[name="？？？"]  ......那么，就确定这次由“这个人”来......
[dialog]
[Decision(options="（谁的声音？）",values="1")]
[Predicate(references="1")]
[PlaySound(key="$dooropenquite", volume=0.6)]
[delay(time=1)]
[Character(name="char_002_amiya_1",fadetime=1,block=true)]
[Delay(time=1)]
[Character(name="char_002_amiya_1#10")]
[name="阿米娅"]  啊，博士，你来了。
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  博士。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]  来得正好，Dr.{@nickname}。
[dialog]
[Decision(options="我迟到了？",values="1")]
[Predicate(references="1")]
[Character(name="char_003_kalts_1")]
[name="凯尔希"]  看来你对自己的散漫多少有些自知之明。
[dialog]
[Decision(options="......;明明是你没有通知我有事要商量......",values="1;2")]
[Predicate(references="1;2")]
[Character(name="char_002_amiya_1#3")]
[name="阿米娅"]  放心吧，博士，今天十分准时。
[Character(name="char_002_amiya_1")]
[name="阿米娅"]  实际上，我和凯尔希、杜宾教官正在商量的是有关“联锁竞赛”的事情。
[dialog]
[Decision(options="联锁......竞赛？",values="1")]
[Predicate(references="1")]
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  没错，更详细地说，是“联锁安保竞赛”。
[Character(name="char_130_doberm_ex#3")]
[name="杜宾"]  它起源于古时米诺斯。热爱举办各类竞赛进行活动的米诺斯人，为各城邦之间进行和谐的安保演练、切磋而创办了官方安保竞赛。
[name="杜宾"]  放在现代来说，更加类似于“军事演练”。不过，现在的联锁竞赛已经没有官方成分了。
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  自从重新举办以后，它已经成为了非官方组织的商业竞赛。
[name="杜宾"]  参与竞赛的商业安保组织成立了联合赛事委员会，负责与各地区官方组织接洽，以保证联锁安保竞赛能够在各地区定期举办。
[Character(name="char_002_amiya_1#2")]
[name="阿米娅"]  大概是因为合作组织的推荐，这一次，罗德岛也收到了参加联锁竞赛的邀请。
[dialog]
[Decision(options="那就参加吧！;参加竞赛......会有什么好处吗？",values="1;2")]
[Predicate(references="1;2")]
[Character(name="char_002_amiya_1#2")]
[name="阿米娅"]  嗯。至关重要的一点是，赛事方提供的奖金和物资十分丰厚！
[Character(name="char_002_amiya_1#3")]
[name="阿米娅"]  对罗德岛来说，这也是最重要的一点。
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  另外，官方地区和组织认为举办竞赛能够提升当地影响力，以及为当地创造更多的合作机会和商业往来，所以十分乐意提供最先进、完备的训练设施和比赛场所。
[name="杜宾"]  联锁竞赛的比赛机制，将要求参赛队伍有分散小队或合击作战的意识，为获得更高的积分和排名需要在战术上进行细致的规划。
[Character(name="char_130_doberm_ex#3")]
[name="杜宾"]  为了进一步增强罗德岛的干员们的整体实力，参与竞赛的确是不可多得的训练机会。
[dialog]
[Decision(options="那一定要参与啊。",values="1")]
[Predicate(references="1")]
[Character(name="char_002_amiya_1#3", name2="char_003_kalts_1", focus=1)]
[name="阿米娅"]  哼哼，凯尔希，你看，我就说博士一定会答应的。
[Character(name="char_002_amiya_1#3", name2="char_003_kalts_1", focus=2)]
[name="凯尔希"]  好啊，Dr.{@nickname}，这可是你自己揽下的活计，可不能后悔。
[dialog]
[Decision(options="嗯？;......",values="1;2")]
[Predicate(references="1;2")]
[Character(name="char_002_amiya_1")]
[name="阿米娅"]  实际上，博士，联锁竞赛想要取得好的名次和更多报酬，一名强大的指挥官是必不可少的。
[name="阿米娅"]  想要参加竞赛，就必须要由博士您来牵头。
[dialog]
[Decision(options="由我来指挥？;......",values="1;2")]
[Predicate(references="1;2")]
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  是的，博士，在联锁竞赛的比赛过程中，您的指挥和判断是不可缺少的环节。
[dialog]
[Decision(options="好吧，又增加工作量了......;我需要注意些什么？",values="1;2")]
[Predicate(references="1;2")]
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  在联锁安保竞赛中，我们将面对“假想敌”队伍，从假想敌的手中获取赛事奖章和物资。
[name="杜宾"]  想要更高效地在限定时间中获得更多奖章，换取更多的物资和奖金的话，将需要配置不同的小队去往不同的“据点”进行驻守。
[name="杜宾"]  只有经赛事裁判确认驻守成功，才会在最终的挑战中增加更强大的假想敌，击败这些特殊的假想敌将获得更多的赛事奖章。
[name="杜宾"]  不过，对付更加强大的假想敌会耗费博士您更多的精力，如果感到力不从心，可以选择更加稳妥的方式获得奖章。
[Character(name="char_130_doberm_ex#2")]
[name="杜宾"]  具体情况，就需要博士您在现场明智的判断了。
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]  不能专注进行指挥导致失误反倒得不偿失。不过，我相信博士一定能布置最合适的战术！
[dialog]
[Decision(options="我会努力的。",values="1")]
[Predicate(references="1")]
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  除此以外，为了配合联锁竞赛的主题和可能出现的假想敌的状况，罗德岛每次将派遣特别甄选代表，陪伴博士您一同前往参赛。
[Character(name="char_002_amiya_1#3")]
[name="阿米娅"]  请放心，博士，特别甄选代表是我、凯尔希和杜宾教官一起考核并选任的干员，一定会在作战中拥有大展身手的机会！
[dialog]
[Decision(options="你们不一起去吗？",values="1")]
[Predicate(references="1")]
[Character(name="char_002_amiya_1#5")]
[name="阿米娅"]  ......
[Character(name="char_003_kalts_1")]
[name="凯尔希"]  ......
[Character(name="char_130_doberm_ex#4")]
[name="杜宾"]  ......
[Character(name="char_003_kalts_1")]
[name="凯尔希"]  这种事不要来麻烦我。
[Character(name="char_002_amiya_1#5")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="阿米娅"]  实、实际上，我还有好多工作没来得及做完......
[Character(name="char_130_doberm_ex")]
[name="杜宾"]  训练干员是我的任务，但我不能永远盯着他们。干员们如何和指挥互相配合，在作战中怎样才能大显身手，这些是你应当考虑的，博士。
[dialog]
[Decision(options="......好吧。;怎么有种把麻烦事丢给我来做的感觉。",values="1;2")]
[Predicate(references="1;2")]
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]  参加联锁竞赛需要储备多支小队的战力，博士，不如趁现在好好想想该如何指挥干员们的行动，制定一份完备的参赛成员名单......
[PlaySound(key="$doorknockquite", volume=0.6)]
[dialog]
[Character(name="char_002_amiya_1#6")]
[name="阿米娅"]  啊，来得正好！
[Character(name="char_002_amiya_1#2")]
[name="阿米娅"]  博士，本次特别甄选代表已经到了。
[dialog]
[Decision(options="这也太快了吧！;你们是不是早就商量好了？;......",values="1;2;3")]
[Predicate(references="1;2;3")]
[Character(name="char_002_amiya_1#10")]
[name="阿米娅"]  嘿嘿，接下来，就麻烦您和特别甄选代表一起商量一下竞赛相关事宜吧。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]  Dr.{@nickname}，记住。
[dialog]
[Decision(options="记......记住什么？;好。;......",values="1;2;3")]
[Predicate(references="1;2;3")]
[Character(name="char_003_kalts_1")]
[name="凯尔希"]  既然参加了竞赛，就要做到最好。
[name="凯尔希"]  每一任主办方的承办竞赛的需求各不相同，假想敌们的行动方式也千差万别。
[Character(name="char_003_kalts_1#3")]
[name="凯尔希"]  找出他们的弱点。看清他们的目的。不要掉入他们的诡计。
[Character(name="char_003_kalts_1#4")]
[name="凯尔希"]  ——然后，取胜。
[Dialog]
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Image]
```

### level_act1lock_st01

```
[HEADER(key="title_test", is_skippable=false, fit_mode="BLACK_MASK")] 开头avg
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_rhodescom",screenadapt="coverall")]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_003_kalts_1",fadetime=1,block=true)]
[delay(time=1)]
[PlaySound(key="$doorknockquite", volume=0.6)]
[delay(time=0.5)]
[name="凯尔希"]  请进。
[PlaySound(key="$dooropenquite", volume=0.6)]
[dialog]
[Character(name="avg_482_pallas_1",fadetime=1,block=true)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Delay(time=1)]
[name="帕拉斯"]  啊，凯尔希女士。博士，您也在。
[name="帕拉斯"]  我们曾在廊上打过几次招呼，那时候您和我还并未足够熟悉。既然我被传唤而来，想必“盛会的邀约”已经传达到您的耳中了。
[dialog]
[Decision(options="“盛会的邀约”......？",values="1")]
[Predicate(references="1")]
[Character(name="char_003_kalts_1")]
[name="凯尔希"]  本次联锁安保竞赛，是首次在米诺斯举办的安保竞赛。
[name="凯尔希"]  实际上，这次邀请罗德岛参赛，与赛事委员会和米诺斯方面负责人接洽的种种行动，都是由祭司帕拉斯对接完成的。
[Character(name="char_003_kalts_1",name2="avg_482_pallas_1#5",focus=2)]
[name="帕拉斯"]  能够接纳我进行隐蔽的治疗，罗德岛已经给予了我诸多恩惠。
[name="帕拉斯"]  参与不同的盛典、享受节日盛典的喜庆、进行武力的比拼是每一位勇士发自心底的期盼，也是对荣耀的渴望。
[name="帕拉斯"]  对于赐予我恩惠的朋友，我自然热情于将同样令人心情愉快的、互有益处的盛会的情报传递给他们。
[Character(name="char_003_kalts_1",name2="avg_482_pallas_1#5",focus=1)]
[name="凯尔希"]  情况就是这样，Dr.{@nickname}。详细的事情会由本次竞赛活动特别甄选代表——帕拉斯，和你慢慢详说。我还有别的事情要处理。
[Character(name="char_003_kalts_1",name2="avg_482_pallas_1",focus=2)]
[name="帕拉斯"]  也祝您有心情愉快的一天，凯尔希女士。
[dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.4, block=true)]
[Background(image="bg_corridor",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.4, block=true)]
[Character(name="avg_482_pallas_1#13",fadetime=1,block=true)]
[Delay(time=1)]
[name="帕拉斯"]  ......
[dialog]
[Decision(options="......",values="1")]
[Predicate(references="1")]
[Character(name="avg_482_pallas_1")]
[name="帕拉斯"]  哎......不论多少次，和凯尔希女士交谈还是颇感压力。
[name="帕拉斯"]  但愿博士的性格要更加主动一些，交流起来能够更加融洽。
[name="帕拉斯"]  就让我们愉快地赴往盛典，完成一次惊艳的亮相，让众人领受来自罗德岛的优越素质与能力吧！来，博士，现在就......
[PlaySound(key="$rungeneral", volume=0.6)]
[dialog]
[character]
[Character(name="char_empty",fadetime=0.7)]
[characteraction(name="middle", type="move", xpos=-200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="middle", type="move", xpos=200, fadetime=0.6, block=false)]
[Character(name="char_333_sidero_1",fadetime=0.7)]
[delay(time=0.6)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="铸铁"]  哈、哈......在此以前，还请你......站住！
[delay(time=0.6)]
[Character(name="char_333_sidero_1",name2="avg_482_pallas_1#9",focus=2)]
[name="帕拉斯"]  嗯？
[Character(name="char_333_sidero_1",name2="avg_482_pallas_1#6",focus=2)]
[name="帕拉斯"]  啊，来自科林尼亚的战士。你又在我的身前显现了。
[Character(name="char_333_sidero_1",name2="avg_482_pallas_1#5",focus=2)]
[name="帕拉斯"]  自我们离开舰桥前往办公室的途中失去联络后，我还几番寻找过你，为何刚才要离我而去呢？
[Character(name="char_333_sidero_1",name2="avg_482_pallas_1#5",focus=1)]
[name="铸铁"]  不要在博士面前搬弄是非。是你自己一边走路一边到处瞧，自说自话地找人闲聊了一阵子，然后突然就从舰桥上消失了。
[Character(name="char_333_sidero_1",name2="avg_482_pallas_1#6",focus=2)]
[name="帕拉斯"]  自然，不应放弃每一次与勇士相逢的机会！
[name="帕拉斯"]  人生本就是匆匆行进，如若能用言语和他人心灵相通，哪怕只言片语所产生的联系，也比错过后的伤感要美好。
[dialog]
[Decision(options="（帕拉斯在说什么？）;你们好像说的不是一回事。;......",values="1;2;3")]
[Predicate(references="1;2;3")]
[Character(name="char_333_sidero_1",name2="avg_482_pallas_1#6",focus=1)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="铸铁"]  ......总之，虽然你不知道弯弯绕绕去了哪里，既然已经找到了博士，接下来就请好好完成自己的任务。
[name="铸铁"]  咳，要做的事情，第一，和博士详细说明本次联锁竞赛的主题——“荷谟伊智境”的有关情报。
[name="铸铁"]  第二，提出建议参赛的人选并查询近期是否有训练和参赛的时间......
[Character(name="char_333_sidero_1",name2="avg_482_pallas_1#13",focus=2)]
[name="帕拉斯"]  可怜的，实力单薄的祭司帕拉斯啊。从前的你被教条式的生活所禁锢，终日于神庙中循规蹈矩。现如今，命运将再次使你过上这般日子吗？
[Character(name="char_333_sidero_1",name2="avg_482_pallas_1#7",focus=2)]
[name="帕拉斯"]  不，勇敢的帕拉斯。抗拒，要勇于对抗那些最枯燥的条理！
[Character(name="char_333_sidero_1",name2="avg_482_pallas_1#7",focus=1)]
[name="铸铁"]  祭司......大人，正事要紧，还请你说些能够让博士和我能听懂的话。
[Character(name="char_333_sidero_1",name2="avg_482_pallas_1#7",focus=2)]
[name="帕拉斯"]  呜......既然如此，我也只能忍受这般不甘的生活。
[Character(name="avg_482_pallas_1")]
[name="帕拉斯"]  博士，如若对这次竞赛的事宜还有疑惑，还请将疑问悉数告知于我。言语将化作灵羽兽传到您的耳边，使您的智慧不被蒙蔽。
[dialog]
[Decision(options="还是告诉我联锁竞赛的事情吧。;谢谢。",values="1;2")]
[Predicate(references="1;2")]
[Character(name="avg_482_pallas_1")]
[name="帕拉斯"]  嗯，从哪里说起好呢......本次联锁安保竞赛举办地设于米诺斯荷谟伊地区。
[name="帕拉斯"]  毕竟，联锁竞赛的概念起源于米诺斯，这次借着重新修建荷谟伊军事训练基地的机会，非常顺利地准备好了举办竞赛的所有条件。
[name="帕拉斯"]  既有丰厚的奖金和物资，还能在参与过程中提升实力，最重要的是......
[name="帕拉斯"]  这是仅限于商业组织之间的竞赛，不会被别有用心的官方组织忌惮。
[dialog]
[Decision(options="......真的吗？",values="1")]
[Predicate(references="1")]
[Character(name="avg_482_pallas_1")]
[name="帕拉斯"]  放心吧，智慧且谨慎的博士啊。阴谋无法在米诺斯的大地上生存，那是一片被英雄祝福的土地。
[name="帕拉斯"]  只要您前去拜访，便能体会到米诺斯人对竞技精神的推崇，而非那些残忍的利益之争。
[name="帕拉斯"]  对正在重回强大的米诺斯而言，再没有比让这份精神在大地上传播、使在动乱中的平和更加稳固更重要的事情了。
[Character(name="char_333_sidero_1",name2="avg_482_pallas_1",focus=1)]
[name="铸铁"]  除了......科林尼亚。
[Character(name="char_333_sidero_1",name2="avg_482_pallas_1",focus=2)]
[name="帕拉斯"]  当然，总会有向商贸繁盛妥协的人在。
[name="帕拉斯"]  不过，已经毅然离开科林尼亚的战士啊，你所怀有的赤子之心，现在不是已然在罗德岛上更好地展现了吗？
[Character(name="char_333_sidero_1",name2="avg_482_pallas_1",focus=1)]
[name="铸铁"]  ......嗯。
[Character(name="avg_482_pallas_1")]
[name="帕拉斯"]  事不宜迟。行动起来吧，博士，我们还有许多事务要准备。
[name="帕拉斯"]  不论是人员和战术的安排和准备，亦或是装备的维护与配备，都是在出发前必须确定的。
[dialog]
[Decision(options="帕拉斯，你觉得罗德岛有多大的胜算？",values="1")]
[Predicate(references="1")]
[Character(name="avg_482_pallas_1#14")]
[name="帕拉斯"]  无需担忧，博士。
[name="帕拉斯"]  站在你身前的，是祭司帕拉斯。受到英雄的指引，我来到罗德岛，代表罗德岛参赛——
[name="帕拉斯"]  我知晓罗德岛的实力。我们，罗德岛的勇士们，将会前去取得我们想要的一切。
[name="帕拉斯"]  胜算......博士，那些虚无缥缈的数字和统计毫无意义。
[name="帕拉斯"]  若说胜算，为取得胜利，那么最为关键的秘宝，便将是我们本身。
[Dialog]
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Image]
```

### level_act1lock_st02

```
[HEADER(key="title_test", is_skippable=false, fit_mode="BLACK_MASK")] 结尾avg
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
“胜利的号角已经吹响——”
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
“英雄的意志，将由每一个英勇的灵魂传承下去！”
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_bridge",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.4)]
[Character(name="char_333_sidero_1",name2="avg_482_pallas_1#7",focus=1)]
[name="铸铁"]  ......外面正热闹地在庆祝呢，帕拉斯。
[name="铸铁"]  你摆出这副愁眉苦脸的样子，像是我们输得很惨似的。罗德岛这次可是获得了胜利组的奖章的。
[Character(name="char_333_sidero_1",name2="avg_482_pallas_1#7",focus=2)]
[name="帕拉斯"]  科林尼亚的战士......呜......我并非为自己感到悲伤。
[Character(name="char_333_sidero_1",name2="avg_482_pallas_1#7",focus=1)]
[name="铸铁"]  ......我知道。现在的你还不能到公众面前亮相。
[dialog]
[Character(name="char_333_sidero_1",name2="avg_482_pallas_1#13",focus=2)]
帕拉斯的手蜷紧了些。迟疑之后，她叹了口气，点头承认。
[dialog]
[Character(name="char_333_sidero_1",name2="avg_482_pallas_1#13",focus=1)]
[name="铸铁"]  老实说，一开始接到任务要求的时候我不太理解。
[name="铸铁"]  为什么给我的指令要随时注意你的动向，避免你的身边有“意外”发生，甚至......提防由你自己制造出些“意外”。
[Character(name="char_333_sidero_1",name2="avg_482_pallas_1",focus=2)]
[name="帕拉斯"]  铸铁战士啊，想必你已经知晓了其中的深意。
[Character(name="char_333_sidero_1",name2="avg_482_pallas_1",focus=1)]
[name="铸铁"]  嗯。因为罗德岛的参赛干员中......有许多的“感染者”。
[name="铸铁"]  在所有的参赛组织当中，只有我们是雇佣感染者作为正式干员的组织。
[name="铸铁"]  不仅出行受到了极大的限制，几乎全部生活都被安排在了比赛场地中。
[name="铸铁"]  对于第一次来到米诺斯的感染者干员们来说，这也是他们能够活动的最大范围了。
[Character(name="char_333_sidero_1",name2="avg_482_pallas_1#13",focus=2)]
[name="帕拉斯"]  是啊......无法改变的铁律与人心的偏见，这是多么令人痛心的隔阂。
[Character(name="char_333_sidero_1",name2="avg_482_pallas_1#13",focus=1)]
[name="铸铁"]  所以，你努力地让罗德岛参与进竞赛中来，也是为了......改变？
[Character(name="char_333_sidero_1",name2="avg_482_pallas_1#8",focus=2)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="帕拉斯"]  呜。
[name="帕拉斯"]  战士啊，虽然大小场面我都曾亲身参与，有些言语要从嘴中说出还是难免催生一种羞愧的心理......
[Character(name="char_333_sidero_1",name2="avg_482_pallas_1#8",focus=1)]
[name="铸铁"]  这有什么好害羞的。
[Character(name="char_333_sidero_1",name2="avg_482_pallas_1#8",focus=2)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="帕拉斯"]  你、你也知道，尽管怀揣着万分期待重回故土，我也难免有深情而惆怅的时刻。
[name="帕拉斯"]  不论是米诺斯还是罗德岛的视线，都不会容许我做过多出格的事情。
[Character(name="char_333_sidero_1",name2="avg_482_pallas_1#7",focus=2)]
[name="帕拉斯"]  所以......正如你所说，我的心中早已了然，这一次的旅途，于我来说已经走到米诺斯能容许我进入的最深处了。
[name="帕拉斯"]  哪怕只是在边远地区的荷谟伊，这座山上也栖息着神话中英雄们的魂魄和意志，能够在此豪爽地酣战一番，于我也意义非凡。
[Character(name="char_333_sidero_1",name2="avg_482_pallas_1#7",focus=1)]
[name="铸铁"]  ......真的一点办法也没有吗？
[Character(name="char_333_sidero_1",name2="avg_482_pallas_1",focus=2)]
[name="帕拉斯"]  正如你从科林尼亚铸造的商业美梦中醒来，现在回看米诺斯的我，又何尝不是仿佛凝视着美好却又稍显荒唐的梦境呢。
[name="帕拉斯"]  这场竞赛的过程，你是否乐在其中？
[Character(name="char_333_sidero_1",name2="avg_482_pallas_1",focus=1)]
[name="铸铁"]  当然。再怎么说我也是米诺斯人，胜负心是无法被磨灭的。
[Character(name="char_333_sidero_1",name2="avg_482_pallas_1#14",focus=2)]
[name="帕拉斯"]  哈哈......英勇的战士啊，对我来说，再没有比这更欣慰的感言了。
[Dialog]
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Image]
```


## 统计

- 总字符数：17700
- 对话行数：120


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
