# 明日方舟 · 活动剧情 · act17d7（4段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act17d7」完整剧情脚本（4个文件，95行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act17d7
- 脚本文件数：4

### act17d7_01a

```
[HEADER(is_skippable=false, is_autoable=false, is_tutorial=true)] 大帝关卡内剧情a

[PopupDialog(dialogHead="$avatar_emperor", animStyle="NoWait")] 是我的低调让你坐地起价
[Delay(time=2)]
[PopupDialog(dialogHead="$avatar_emperor", animStyle="NoWait")] 好好想想谁才是说唱赢家
[Delay(time=2)]
[PopupDialog(dialogHead="$avatar_emperor", animStyle="NoWait")] 我劝您老还是趁早点回家
[Delay(time=2)]
[PopupDialog(dialogHead="$avatar_emperor", animStyle="NoWait")] 免得腰板酸痛把拐杖落下
[Delay(time=2)]
[PopupDialog(dialogHead="$avatar_mousek", animStyle="NoWait", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
你顶着十九冠头衔却只会叫嚷
[Delay(time=2)]
[PopupDialog(dialogHead="$avatar_mousek", animStyle="NoWait", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
还不如回去当你的那快递校长
[Delay(time=2)]
[PopupDialog(dialogHead="$avatar_mousek", animStyle="NoWait", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
让Mc.舸瑞把你收拾个直截了当
[Delay(time=2)]
[PopupDialog(dialogHead="$avatar_mousek", animStyle="NoWait", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
看你下次来公园还敢不敢嚣张
[Delay(time=2)]
[PopupDialog(dialogHead="$avatar_emperor", animStyle="NoWait")] 你该让6060那家伙教你flow
[Delay(time=2)]
[PopupDialog(dialogHead="$avatar_emperor", animStyle="NoWait")] 还能再花180万给你当枪手
[Delay(time=2)]
[PopupDialog(dialogHead="$avatar_emperor", animStyle="NoWait")] 别怪我开<@tu.kw>技能</>把你风头都抢走
[Delay(time=2)]
[PopupDialog(dialogHead="$avatar_emperor", animStyle="NoWait")] <@tu.kw>灯光</>亮起来，让你们好好享受！
[Delay(time=2)]
```

### act17d7_01b

```
[HEADER(is_skippable=false, is_autoable=false, is_tutorial=true)] 大帝关卡内剧情b


[PopupDialog(dialogHead="$avatar_mousek", animStyle="NoWait", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
看来你还真有两把刷
[Delay(time=2)]
[PopupDialog(dialogHead="$avatar_mousek", animStyle="NoWait", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
现在轮到老朽来出马
[Delay(time=2)]

```

### level_act17d7_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[Character]
[Dialog]
[ImageTween(xScaleTo=1.1, yScaleTo=1.1, duration=6)]
[PlayMusic(intro="$fesmetal_intro", key="$fesmetal_loop", volume=0.6, crossfade=1.5)]
[Delay(time=2)]
[Background(image="bg_Festival_2", fadetime=3)]
[Character]
[Character(name="char_130_doberm_ex")]
[name="热情的歌迷"]   结束了......
[Character(name="char_284_spot_1")]
[name="歌迷？"]   呼，我有点头晕。
[Character(name="char_185_frncat_1")]
[name="激动的歌迷"]  结束了！大帝先生赢了！
[Character(name="char_105_emper")]
[name="大帝"]   毫无疑问的结果！
[name="大帝"]   是什么让你们产生能赢我的错觉？集体老眼昏花还是大脑错乱？
[name="大帝"]   不过无所谓，就节目效果来说确实还不错，比之前假模假样的点评会像样多了。
[name="大帝"]   还有，刚刚那些挑战者里面是不是还混了什么怪东西。说真的，你们选人的水平真是一坨屎。
[Character(name="avg_npc_030")]
[name="主持人"]   这也是惊喜的一环，看来效果很好。
[Character(name="avg_npc_074")]
[name="老牌音乐人"]   我也觉得还不错，这不是挺有意思的嘛。
[Character(name="char_105_emper")]
[name="大帝"]   喂，别的不提，为什么这个臭老鼠能在那里坐着？
[Character(name="avg_npc_034#3")]
[name="“沙炫风”"]   站得太久，腿脚撑不住咯。
[Character(name="char_105_emper")]
[name="大帝"]   呸，那你怎么不直接回家养老？
[Character(name="avg_npc_030")]
[name="主持人"]   总之，恭喜大帝先生在这次挑战赛里获得优胜！
[name="主持人"]   我们为获胜者准备了独一无二的纪念雕像，不论是在观赏性还是收藏方面都具有极高的价值！
[Character(name="avg_npc_074")]
[name="老牌音乐人"]   呃，说实话，你们那奖品送我都不想要。
[Character(name="avg_npc_034#3")]
[name="“沙炫风”"]   确实，摆在家里可能会做噩梦。
[Character(name="char_105_emper")]
[name="大帝"]   那是你们不懂欣赏！
[name="大帝"]   算了，别给我，给那边的几个小朋友吧。他们节拍打得不错，和大帝同台这种机会可不常有，是该好好纪念一下。
[Character(name="char_185_frncat_1")]
[name="激动的歌迷"]  可以吗？！
[Character(name="char_105_emper")]
[name="大帝"]   别激动，我说了可以当然就可以。
[name="大帝"]   这事我说了算。怎么，难道还有人不知道吗？我会好心再提醒那些还没搞清楚状况的人最后一次，最后一次！
[name="大帝"]   仔细听。然后喊我的名字，崇拜我。
[CameraShake(duration=2, xstrength=8, ystrength=8, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
[name="大帝"]   我，就是站在这里的唯一真理。
[name="大帝"]   这个舞台上——我说了算！
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Dialog]
[Character]
[Image]
```

### level_act17d7_entry

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[Character]
[Dialog]
[ImageTween(xScaleTo=1.1, yScaleTo=1.1, duration=6)]
[PlayMusic(intro="$fesmetal_intro", key="$fesmetal_loop", volume=0.6, crossfade=1.5)]
[Delay(time=2)]
[Background(image="bg_Festival_2", fadetime=3)]
[Character]
[CameraShake(duration=2, xstrength=8, ystrength=8, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
欢迎来到玛尔特服饰冠名——freestyle星期四，《Loyal to the beats！》说唱之夜！
欢迎本期擂主岸湾霸王流行巨头，我们的大————帝！他将再度迎来新的挑战者......他们是——
[Dialog]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="char_105_emper",fadetime=2,block=true)]
[Delay(time=2)]
[name="大帝"]   逻辑、条理、常识、习惯。
[name="大帝"]   太多人过于在意这些东西，但是可怜兮兮地扮演一个完全合乎情理随处可见平庸至极的人又能有什么乐趣？
[name="大帝"]   你，你来说。你来告诉我。
[name="大帝"]   早上的健康早餐为什么这么难吃，卡特斯是不是都长那么长的耳朵，这份报告书真的非得今天写完，一加一难道一定需要一个结果？
[name="大帝"]   无聊。
[CameraShake(duration=0.5, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="大帝"]   无聊透顶！
[name="大帝"]   比起这种枯燥乏味的按部就班，音乐需要的是更有热情的东西！更感性，更直觉，更热烈！
[name="大帝"]   火花、灵感、爆炸、意外！比所有计划好的表演都更让人瞠目结舌，比这块搭建好的舞台更受瞩目！
[name="大帝"]   丢掉你们那些无聊的习惯常识逻辑，现在，尽情欢呼！
[name="大帝"]   在这里只站着一个真理，一个奇迹。
[name="大帝"]   ——那就是我！
[Dialog]
[Character]
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
[delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_185_frncat_1")]
[name="激动的歌迷"]   大帝先生！是真的大帝先生在说话！
[name="激动的歌迷"]   我没在做梦吧？我、我、结束后我能去要个签名吗......
[Character(name="char_284_spot_1")]
[name="歌迷？"]   喂，小心，别憋气，呼吸，呼吸——
[Character(name="char_185_frncat_1",name2="char_284_spot_1",focus=1)]
[name="激动的歌迷"]   呼......哈......
[Character(name="char_185_frncat_1",name2="char_284_spot_1",focus=2)]
[name="歌迷？"]   真没问题？我总觉得台上那位巨星可能会干点什么离谱的事。
[Character(name="char_130_doberm_ex")]
[name="热情的歌迷"]   别担心，那就是大帝的舞台。就算他真的安排一场爆炸，那也是舞台的一部分！
[Character(name="char_284_spot_1")]
[name="歌迷？"]   真的假的......
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[delay(time=0.1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_105_emper",fadetime=1,block=true)]
[Delay(time=1)]
[name="大帝"]   几个渴望向上爬的新人，一群装模作样的评委，还有没半点新意老掉牙的点评。除此之外还有什么？
[name="大帝"]   喂，特地请了我来，你们这个节目难道就只有这些让人打瞌睡的无聊安排吗？
[Dialog]
[Character]
[Character(name="avg_npc_030",fadetime=1,block=true)]
[Delay(time=1)]
[name="主持人"]   当然不会。
[name="主持人"]   请您放心，大帝先生。我们专门替您准备了一些惊喜——
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="avg_npc_034",fadetime=2,block=true)]
[Delay(time=2)]
[name="？？？"]   闹剧就到此为止了。
[Character(name="char_105_emper")]
[name="大帝"]   哦？
[Character(name="avg_npc_034#3")]
[name="有潜力的说唱新星"]   你在台上的表现实在让人看不过去，大帝。
[name="有潜力的说唱新星"]   你的音乐，就连你的词也肤浅至极，这样的烂歌我一天能写二十首。你过时的flow该和70Percent一起被扫进落叶堆里了。
[name="有潜力的说唱新星"]   就让我这个新人，来给各位展示现在的音乐潮流，让你也看看真正现代的说唱吧。
[Dialog]
[Character]
[Dialog]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$pistol", volume=0.9)]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[CameraShake(duration=0.1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="char_105_emper")]
[name="大帝"]   啧，脱靶。抱歉，没打中是我的失误。
[name="大帝"]   哇哦，怎么回事，你用这种口气说话让我犯恶心。
[name="大帝"]   是谁把臭老鼠放上台的？说唱界新人？我怎么没听过最近有这么个让人火大的新人。
[Character(name="avg_npc_030")]
[name="主持人"]   大帝先生很久没关注过业界了吧？
[name="主持人"]   最近出现了不少有才华的歌手，其中一些已经拥有一定规模的支持者，实力不可小觑。
[name="主持人"]   这位“沙炫风”先生就是新人里最有人气的一位了。
[Character(name="char_105_emper")]
[name="大帝"]   这名字土得让我感觉自己在掉毛。
[Character(name="avg_npc_034#3")]
[name="“沙炫风”"]   是吗？我倒是觉得还不错。
[name="“沙炫风”"]   就让我沙炫风a.k.a.MC.舸瑞来让你明白人不可貌相，也不要随意取笑别人的名字。
[Character(name="avg_npc_074",fadetime=1,block=true)]
[delay(time=2)]
[name="老牌音乐人"]   嗨，我都不知道原来你们关系这么好的吗？但是能不能不要无视我？
[characteraction(name="right", type="jump", xpos=0, power=40, times=3, fadetime=1,block=false)]
[name="老牌音乐人"]   这儿，我在这儿！
[name="老牌音乐人"]   怎么都没人尊重一下老前辈，尖叫和掌声都在哪儿？我发的专辑难道销量都是假的？我可是白金唱片制作人！
[name="老牌音乐人"]   嘿，小伙子们，搭把手，托我一把。
[Character(name="char_105_emper")]
[name="大帝"]   所以，这群杂牌军就是你们安排的意外惊喜？我有没有理解错，确定不是什么整蛊环节？
[Character(name="avg_npc_030")]
[name="主持人"]   如您所见，这几位就是我们本场的“挑战者”！
[name="主持人"]   我们邀请到现场的歌手不止一位，从经验老到的乐坛常青树到备受瞩目的新人，还有诸多神秘嘉宾可以期待！
[name="主持人"]   这些音乐人将向我们的说唱之神发起挑战！
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_185_frncat_1")]
[name="激动的歌迷"]   那是......是最近有名的新人歌手！
[Character(name="char_284_spot_1")]
[name="歌迷？"]   嗯？我好像在屏幕上见过那个后面出来的家伙，这期擂台竟然来了这么多大腕？
[Character(name="char_185_frncat_1")]
[name="激动的歌迷"]   天啊，他们好像准备要开始了！大帝要唱了？！
[Character(name="char_130_doberm_ex")]
[name="热情的歌迷"]   看来这次来现场真是来对了......走，我们过去看看！
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_105_emper")]
[name="大帝"]   ......
[name="大帝"]   很好。做得不错。
[name="大帝"]   狂妄到向我提出挑战的人有很多，但愿你们和那些人会有一些不同，别太扫我的兴！
[name="大帝"]   说吧，你们要怎么挑战，是一起上还是一个一个来，我不介意多花点时间。
[Character(name="avg_npc_034#3")]
[name="“沙炫风”"]   我也不介意给跟不上时代的老前辈来一点冲击。
[Character(name="avg_npc_074")]
[name="老牌音乐人"]   等下，你说的这个跟不上时代是不是把我也算进去了？
[Character(name="char_105_emper")]
[name="大帝"]   等等，我想到了一个好主意！机会难得，不如我们增加点难度，这样才有意思！
[Character(name="avg_npc_030")]
[name="主持人"]   大帝先生需要什么，我们立刻安排......
[Character(name="char_105_emper")]
[name="大帝"]   不用。没那么麻烦。
[Dialog]
[delay(time=1)]
[name="大帝"]   你，对，就是你们，上来这里。
[Character(name="char_185_frncat_1")]
[name="激动的歌迷"]   欸？！我、我吗？
[Character(name="char_130_doberm_ex")]
[name="热情的歌迷"]   有什么需要我们做的吗？
[Character(name="char_105_emper")]
[name="大帝"]   先生小姐们，会乐器吗？不会也没关系，反正接下来只会是一场让所有人看清什么叫实力差距的，由我为各位带来的个人秀！
[Character(name="avg_npc_074")]
[name="老牌音乐人"]   这就是增加难度？喊一群外行来伴奏，即兴演出？
[Character(name="avg_npc_034#3")]
[name="“沙炫风”"]   哼，狂妄。
[Character(name="char_185_frncat_1")]
[name="激动的歌迷"]  这......我们真的可以吗......
[Character(name="char_105_emper")]
[name="大帝"]   放轻松，来多加点打击的伴奏，其他的都

... (全文6387字符)
```


## 统计

- 总字符数：10224
- 对话行数：95


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
