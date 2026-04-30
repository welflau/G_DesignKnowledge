# 明日方舟 · 活动剧情 · act18side（23段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act18side」完整剧情脚本（23个文件，3283行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act18side
- 脚本文件数：23

### level_act18side_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="28_g11_lounge",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Dialog]
[Character(name="char_empty", name2="avg_4046_ebnhlz_1#1$2",fadetime=0.7)]
[delay(time=1)]
[PlaySound(key="$rungeneral", volume=0.9)]
[characteraction(name="left", type="move", xpos=-200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="left", type="move", xpos=200, fadetime=1, block=false)]
[Character(name="avg_npc_482_1#7$1", name2="avg_4046_ebnhlz_1#1$2",fadetime=0.7)]
[delay(time=1.5)]
[Character(name="avg_npc_482_1#7$1", name2="avg_4046_ebnhlz_1#1$2",focus=1)]
[name="白垩"]不好意思，我迟到了......
[Character(name="avg_npc_482_1#7$1", name2="avg_4046_ebnhlz_1#1$2",focus=2)]
[name="黑键"]这可是选拔赛！你再晚个二十分钟，我们俩就可以手牵手打道回府了！
[Character(name="avg_npc_482_1#7$1", name2="avg_4046_ebnhlz_1#1$2",focus=1)]
[name="白垩"]抱歉......
[Character(name="avg_npc_482_1#7$1", name2="avg_4046_ebnhlz_1#1$2",focus=2)]
[name="黑键"]你就不为自己辩解一下？
[Character(name="avg_npc_482_1#6$1", name2="avg_4046_ebnhlz_1#1$2",focus=1)]
[name="白垩"]其实是......早上的时候，爷爷不见了。
[Character(name="avg_npc_482_1#6$1", name2="avg_4046_ebnhlz_1#3$2",focus=2)]
[name="黑键"]不见了？
[Character(name="avg_npc_482_1#9$1", name2="avg_4046_ebnhlz_1#3$2",focus=1)]
[name="白垩"]倒也不是什么大事，我在夕照区的巷子里找到了爷爷，爷爷说他只是醒得太早，出去遛弯了。
[Character(name="avg_npc_482_1#9$1", name2="avg_4046_ebnhlz_1#3$2",focus=2)]
[name="黑键"]一直遛弯，遛到你来之前？
[Character(name="avg_npc_482_1#3$1", name2="avg_4046_ebnhlz_1#3$2",focus=1)]
[name="白垩"]没有没有，我们今早还去罗德岛办了住院手续。
[Character(name="avg_npc_482_1#3$1", name2="avg_4046_ebnhlz_1#3$2",focus=2)]
[name="黑键"]你爷爷？去罗德岛办事处住院？
[Character(name="avg_npc_482_1#3$1", name2="avg_4046_ebnhlz_1#1$2",focus=2)]
[name="黑键"]我记得罗德岛在维谢海姆只有个小办事处，根本不能收住院病人。
[Character(name="avg_npc_482_1#1$1", name2="avg_4046_ebnhlz_1#1$2",focus=1)]
[name="白垩"]原本是不能的，但芙蓉特意把自己的床腾了出来，还向我保证，一定把爷爷的健康放在第一位。
[Character(name="avg_npc_482_1#1$1", name2="avg_4046_ebnhlz_1#7$2",focus=2)]
[name="黑键"]哼......说得好听，实际上要了你不少钱吧？
[Character(name="avg_npc_482_1#1$1", name2="avg_4046_ebnhlz_1#7$2",focus=1)]
[name="白垩"]你昨天给我的钱，今早他们只收了一半还不到。
[Character(name="avg_npc_482_1#1$1", name2="avg_4046_ebnhlz_1#11$2",focus=2)]
[name="黑键"]嗬，那你可得时常去看看你爷爷，免得他们在你看不到的地方节省经费。
[Character(name="avg_npc_482_1#3$1", name2="avg_4046_ebnhlz_1#11$2",focus=1)]
[name="白垩"]“节省经费”？
[Character(name="avg_npc_482_1#3$1", name2="avg_4046_ebnhlz_1#1$2",focus=2)]
[name="黑键"]他们毕竟是商业公司，用这么低的价格收治病人，利润当然还得从病人身上来。比如说，伙食上克扣一点，器材和药品上克扣一点——
[Character(name="avg_npc_482_1#10$1", name2="avg_4046_ebnhlz_1#1$2",focus=1)]
[name="白垩"]我觉得不会的。
[Character(name="avg_npc_482_1#10$1", name2="avg_4046_ebnhlz_1#1$2",focus=2)]
[name="黑键"]你怎么知道不会？
[Character(name="avg_npc_482_1#10$1", name2="avg_4046_ebnhlz_1#1$2",focus=1)]
[name="白垩"]昨天下午，我还没交钱，他们就给爷爷发了口服药。
[Character(name="avg_npc_482_1#1$1", name2="avg_4046_ebnhlz_1#1$2",focus=1)]
[name="白垩"]今天早上芙蓉还留我吃饭，我因为没时间才拒绝了她。
[Character(name="avg_npc_482_1#1$1", name2="avg_4046_ebnhlz_1#7$2",focus=2)]
[name="黑键"]这么刻意的表演，恐怕连你爷爷都看出来了，他才不想去的。
[Character(name="avg_npc_482_1#10$1", name2="avg_4046_ebnhlz_1#7$2",focus=1)]
[name="白垩"]我明白了，我会时常去看爷爷的。
[Character(name="avg_npc_482_1#11$1", name2="avg_4046_ebnhlz_1#7$2",focus=1)]
[name="白垩"]谢谢你。
[Character(name="avg_npc_482_1#11$1", name2="avg_4046_ebnhlz_1#3$2",focus=2)]
[name="黑键"]谢我？
[Character(name="avg_npc_482_1#10$1", name2="avg_4046_ebnhlz_1#3$2",focus=1)]
[name="白垩"]你也是怕我和爷爷吃亏才特意跟我说这些，我明白。
[Character(name="avg_npc_482_1#10$1", name2="avg_4046_ebnhlz_1#3$2",focus=2)]
[name="黑键"]......
[Character(name="avg_npc_482_1#10$1", name2="avg_4046_ebnhlz_1#2$2",focus=2)]
[name="黑键"]算了，不说这个了。
[Character(name="avg_npc_482_1#10$1", name2="avg_4046_ebnhlz_1#1$2",focus=2)]
[name="黑键"]昨天拿到谱子之后，你看得怎么样？
[Character(name="avg_npc_482_1#1$1", name2="avg_4046_ebnhlz_1#1$2",focus=1)]
[name="白垩"]我——
[dialog]
[delay(time=0.6)]
[Character(name="avg_npc_482_1#1$1", name2="avg_4046_ebnhlz_1#1$2",focus=-1)]
[name="礼貌的感染者"]下一组，黑键和白垩！
[Character(name="avg_npc_482_1#1$1", name2="avg_4046_ebnhlz_1#1$2",focus=2)]
[name="黑键"]走了。
[Character(name="avg_npc_482_1#1$1", name2="avg_4046_ebnhlz_1#1$2",focus=2)]
[name="黑键"]今天的选拔赛可是车尔尼亲自坐镇，咱们可不能丢人。
[musicvolume(volume=0.2, fadetime=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Delay(time=1)]
[Character(name="avg_4047_pianst_1#1$1")]
[Background(image="28_g10_stage",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[musicvolume(volume=0.4, fadetime=1)]
[Character(name="avg_4046_ebnhlz_1#1$2")]
[name="黑键"]您好，车尔尼先生......
[Character(name="avg_4047_pianst_1#1$1")]
[name="车尔尼"]不必寒暄，开始吧。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[delay(time=1)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
和观众席上挤满围观群众的报名会不同，选拔赛上，除了车尔尼和参加选拔的人们，只有寥寥几名工作人员。
如果昨天那些观众在场，他们多半会为这段短短的合奏拍红手掌。
但此时此刻，最后的余音已经散去，车尔尼的脸色却并不好看。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character(name="avg_4047_pianst_1#1$1")]
[Background(image="28_g10_stage",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[Character(name="avg_4046_ebnhlz_1#13$2")]
[name="黑键"]车尔尼先生？
[Character(name="avg_4047_pianst_1#2$1")]
[name="车尔尼"]你们没怎么练过吧。
[Character(name="avg_4046_ebnhlz_1#13$2")]
[name="黑键"]如您所说，但是——
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Character(name="avg_4047_pianst_1#1$1")]
[name="车尔尼"]临时拼凑的感觉太重，你吹你的，他拉他的，几乎感觉不到配合。
[Character(name="avg_4047_pianst_1#1$1")]
[name="车尔尼"]尤其是你，完全不管大提琴旋律段的情感表达

... (全文24600字符)
```

### level_act18side_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="28_g5_czernyhome",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Character(name="avg_4047_pianst_1#1$1")]
[name="车尔尼"]虽然我在选拔赛上让你们两个出局了，但现在情况有变，你们是《晨暮》的第一候选了。
[Character(name="avg_4046_ebnhlz_1#3$2")]
[name="黑键"]情况有变是说？
[Character(name="avg_4047_pianst_1#1$1")]
[name="车尔尼"]原定要演奏《晨暮》的那两个人不能参加音乐会了，所以我才找你们过来。
[Character(name="avg_4046_ebnhlz_1#1$2")]
[name="黑键"]不能参加音乐会......他们出什么事了？
[Character(name="avg_4047_pianst_1#1$1")]
[name="车尔尼"]那两个人昨天下午跑到酒馆大吃大喝去了。
[Character(name="avg_4047_pianst_1#1$1")]
[name="车尔尼"]本来这倒也正常，可是，不知为了什么鸡毛蒜皮的小事，这两个活宝竟然在酒馆里和人打了起来。
[Character(name="avg_4047_pianst_1#1$1")]
[name="车尔尼"]结果，吹长笛的胳膊骨折，拉大提琴的更厉害，居然摔断了尾椎骨，坐都坐不下去，还趴在床上说自己可以站着拉琴，简直胡闹！
[Character(name="avg_4046_ebnhlz_1#3$2")]
[name="黑键"]啊？
[Character(name="avg_4047_pianst_1#1$1")]
[name="车尔尼"]你好像很惊讶。
[Character(name="avg_4046_ebnhlz_1#3$2")]
[name="黑键"]这实在有些......出人意料。
[Character(name="avg_4047_pianst_1#1$1")]
[name="车尔尼"]出人意料？
[Character(name="avg_4047_pianst_1#1$1")]
[name="车尔尼"]说实话，入选的第二天就出这种事，假如这不仅仅是一场偶然的打架斗殴，你就是最大的嫌疑人。
[Character(name="avg_4046_ebnhlz_1#3$2")]
[name="黑键"]我就是最大的嫌疑人？
[Character(name="avg_4046_ebnhlz_1#3$2")]
[name="黑键"]不——不不不，这事和我毫无瓜葛。
[Character(name="avg_4046_ebnhlz_1#1$2")]
[name="黑键"]我还是更希望用音乐打动您，而不是对无辜之人拳打脚踢。
[Character(name="avg_4047_pianst_1#1$1")]
[name="车尔尼"]说得倒挺好听。
[Character(name="avg_4047_pianst_1#1$1")]
[name="车尔尼"]不过，既然你有钱资助白垩，花钱雇几个人，对你而言应该也轻而易举，不是吗？
[character(name="avg_npc_482_1#8$1")]
[name="白垩"]车尔尼先生，我也可以作证，黑键没有做这种事。
[Character(name="avg_4047_pianst_1#1$1")]
[name="车尔尼"]你能作证？你昨天一直盯着他？
[character(name="avg_npc_482_1#8$1")]
[name="白垩"]——是的。
[Character(name="avg_4047_pianst_1#1$1")]
[name="车尔尼"]你盯着他干什么？
[character(name="avg_npc_482_1#3$1")]
[name="白垩"]我......
[Character(name="avg_4046_ebnhlz_1#1$2")]
[name="黑键"]当然不是“他盯着我”，而是我们俩在一起，商量如何让您回心转意啊。
[Character(name="avg_4046_ebnhlz_1#9$2")]
[name="黑键"]虽然直到最后也没商量出什么结果。
[Character(name="avg_4047_pianst_1#1$1")]
[name="车尔尼"]白垩，他说的是真的？
[character(name="avg_npc_482_1#1$1")]
[name="白垩"]是真的。
[Character(name="avg_4047_pianst_1#2$1")]
[name="车尔尼"]（摇头）
[Character(name="avg_4047_pianst_1#1$1")]
[name="车尔尼"]既然这样，那我姑且相信白垩一次。
[character(name="avg_npc_482_1#10$1")]
[name="白垩"]谢谢车尔尼先生！
[Character(name="avg_4046_ebnhlz_1#13$2")]
[name="黑键"]那么......
[Character(name="avg_4047_pianst_1#1$1")]
[name="车尔尼"]别急着高兴。
[Character(name="avg_4047_pianst_1#1$1")]
[name="车尔尼"]说到底，你们是替补上来的，离我的要求还有不小的差距。
[Character(name="avg_4047_pianst_1#1$1")]
[name="车尔尼"]尤其是黑键，你是拖后腿的那个。
[Character(name="avg_4047_pianst_1#1$1")]
[name="车尔尼"]我给你们一天时间练习，晚上再到我家来，我来验收。
[Character(name="avg_4047_pianst_1#1$1")]
[name="车尔尼"]只有达到我的最低标准，你们才算是入选了。要不然，我宁可把《晨暮》这首曲子撤掉，明白吗？
[Character(name="avg_4046_ebnhlz_1#1$2")]
[name="黑键"]明白，请您放心。
[Character(name="avg_4047_pianst_1#1$1")]
[name="车尔尼"]还有，白垩，你不是没有大提琴吗？这把琴你先拿回去。
[character(name="avg_npc_482_1#3$1")]
[name="白垩"]我......我真的可以拿吗？
[Character(name="avg_4047_pianst_1#1$1")]
[name="车尔尼"]当然可以。
[Character(name="avg_4047_pianst_1#1$1")]
[name="车尔尼"]如果今晚你们能达到我的要求，这把琴就是你的了。
[character(name="avg_npc_482_1#11$1")]
[name="白垩"]——谢谢，谢谢您！
[Character(name="avg_4047_pianst_1#1$1")]
[name="车尔尼"]好了，回去吧，我也要整理一下自己的思路——
[dialog]
[PlaySound(key="$doorknockquite", volume=0.6)]
[delay(time=1)]
[Character(name="avg_4047_pianst_1#1$1")]
[name="车尔尼"]是乌尔苏拉吗？你又忘记带钥匙了？
[dialog]
[character]
[name="门外的声音"]车尔尼先生，我是罗德岛的干员，您可以叫我芙蓉。
[character(name="avg_npc_482_1#3$1")]
[name="白垩"]是芙蓉！难道爷爷出了什么状况——
[Dialog]
[PlaySound(key="$rungeneral", volume=0.9)]
[characteraction(name="middle", type="move", xpos=-300, fadetime=2,block=false)]
[Character(fadetime=0.5)]
[delay(time=2)]
[PlaySound(key="$doorclosequite")]
[delay(time=2.5)]
[Character(name="char_empty")]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="middle", type="move", xpos=-200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="middle", type="move", xpos=200, fadetime=1.5, block=false)]
[Character(name="avg_1024_hbisc2_1#1$1",fadetime=0.7)]
[delay(time=2)]
[name="芙蓉"]您好，车尔尼先生，初次见面。
[Character(name="avg_4047_pianst_1#1$1")]
[name="车尔尼"]你好。
[Character(name="avg_4047_pianst_1#1$1")]
[name="车尔尼"]我和他们已经聊完了，你要是有事就带他们走吧。
[character(name="avg_npc_482_1#3$1")]
[name="白垩"]芙蓉，爷爷的病情有什么变化吗？
[Character(name="avg_1024_hbisc2_1#10$1")]
[name="芙蓉"]放心，放心。你爷爷经过治疗之后，情况已经比较稳定了。
[Character(name="avg_1024_hbisc2_1#1$1")]
[name="芙蓉"]车尔尼先生，其实我不是来找白垩，而是来找您的。
[Character(name="avg_4047_pianst_1#1$1")]
[name="车尔尼"]找我？
[Character(name="avg_1024_hbisc2_1#1$1")]
[name="芙蓉"]我希望能了解一下您最近的病情变化，不知道您现在方不方便。
[Character(name="avg_4047_pianst_1#6$1")]
[name="车尔尼"]问我这个干嘛？
[Character(name="avg_1024_hbisc2_1#8$1")]
[name="芙蓉"]最近夕照区出现了不少异常好转的感染者，我来夕照区就是为了调查这一现象。
[Character(name="avg_1024_hbisc2_1#1$1")]
[name="芙蓉"]另外，您在夕照区家喻户晓，没准您对整体情况也有一些把握。
[Character(name="avg_4047_pianst_1#2$1")]
[name="车尔尼"]不好意思，我自己一直好得很，至于别人的病情，我不知道。
[Character(name="avg_1024_hbisc2_1#7$1")]
[name="芙蓉"]可您不是要开告别音乐会吗？一般来说——
[Character(name="avg_4047_pianst_1#6$1")]
[name="车尔尼"]不好意思，我需要一个安静的环境，现在能请你离开了吗？
[dialog]
[PlaySound(key="$doorknockquite")]
[delay(time=1)]
[Character(name="avg_4047_pianst_1#6$1")]
[name="车尔尼"]又是哪位？
[Character(name="avg_4047_pianst_1#1$1",focus=-1)]
[name="门外的声音"]先生，开开门，咱忘记带钥匙啦。
[Character(name="avg_4047_pianst_1#7$1")]
[name="车尔尼"]......
[Character(name="avg_4047_pianst_1#1$1")]
[name="车尔尼"]白垩，能不能麻烦你再去开个门？
[dialog]
[Character(name="avg_npc_482_1#1$1")]
[Dialog]
[delay(time=0.7)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="middle", type="move", xpos=-300, fadetime=2,block=false)]
[Character(fadetime=0.5)]
[delay(time=2)]
[PlaySound(key="$dooropenquite", volume=1)]
[Delay(time=2)]
[name="白垩"]老奶奶，您拎了好多东西啊。
[name="？？？"]好孩子，快去屋里坐着，咱自己就能拿得动。
[name="白垩"]没关系的，我来帮您把东西送到厨房！
[dialog]
[delay(time=1)]
[Character(name="avg_4046_ebnhlz_1#1$2")]
[name="黑键"]这

... (全文19019字符)
```

### level_act18side_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="28_g2_slumstreets",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Character(name="avg_1024_hbisc2_1#4$1")]
[name="芙蓉"]呼......
[Character(name="avg_1024_hbisc2_1#7$1")]
[name="芙蓉"]虽然车尔尼先生那里不怎么顺利，但夕照区的其他居民都挺好说话的。
[Character(name="avg_1024_hbisc2_1#1$1")]
[name="芙蓉"]走访了十多家，还采到了几份血样，成果还算不错。
[name="芙蓉"]天已经快黑了啊......
[dialog]
[Dialog]
[Character(name="avg_1024_hbisc2_1#1$1", name2="char_empty")]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="right", type="move", xpos=200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="right", type="move", xpos=-200, fadetime=1, block=false)]
[Character(name="avg_1024_hbisc2_1#1$1", name2="avg_npc_494_1#1$1",fadetime=0.7)]
[delay(time=2)]
[Character(name="avg_1024_hbisc2_1#1$1",name2="avg_npc_494_1#1$1",focus=2)]
[name="小吃摊主"]姑娘，我看你这一整天都没闲着，在周围到处跑，也该饿了吧？
[Character(name="avg_1024_hbisc2_1#1$1",name2="avg_npc_494_1#6$1",focus=2)]
[name="小吃摊主"]尝尝夕照区特产怎么样？
[Character(name="avg_1024_hbisc2_1#3$1",name2="avg_npc_494_1#6$1",focus=1)]
[name="芙蓉"]特产？
[Character(name="avg_1024_hbisc2_1#3$1",name2="avg_npc_494_1#6$1",focus=2)]
[name="小吃摊主"]瞧瞧，油煎酸渍卷心菜，这香气，这色泽！
[Character(name="avg_1024_hbisc2_1#7$1",name2="avg_npc_494_1#6$1",focus=1)]
[name="芙蓉"]（高温油煎的腌渍食品，这和健康完全背道而驰啊......）
[Character(name="avg_1024_hbisc2_1#7$1",name2="avg_npc_494_1#1$1",focus=2)]
[name="小吃摊主"]怎么，怕我宰客？来，这一份是送你的，不要钱！
[Character(name="avg_1024_hbisc2_1#7$1",name2="avg_npc_494_1#1$1",focus=2)]
[name="小吃摊主"]别不好意思，你在我们这儿走街串巷替大家看病，这是感谢你的。
[Character(name="avg_1024_hbisc2_1#4$1",name2="avg_npc_494_1#1$1",focus=1)]
[name="芙蓉"]（唉，盛情难却......）
[Character(name="avg_1024_hbisc2_1#8$1",name2="avg_npc_494_1#1$1",focus=1)]
[name="芙蓉"]那就多谢您了。
[Character(name="avg_1024_hbisc2_1#8$1",name2="avg_npc_494_1#6$1",focus=2)]
[name="小吃摊主"]客气！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Delay(time=1)]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="avg_1024_hbisc2_1#1$1",name2="avg_npc_494_1#1$1",focus=2)]
[name="小吃摊主"]怎么吃了一口就放下了，说了是送你的嘛。
[Character(name="avg_1024_hbisc2_1#1$1",name2="avg_npc_494_1#1$1",focus=1)]
[name="芙蓉"]我还不饿，一会儿再吃。
[Character(name="avg_1024_hbisc2_1#10$1",name2="avg_npc_494_1#1$1",focus=1)]
[name="芙蓉"]不过，您有没有考虑过稍微调整一下配方？
[Character(name="avg_1024_hbisc2_1#10$1",name2="avg_npc_494_1#4$1",focus=2)]
[name="小吃摊主"]调整配方？
[Character(name="avg_1024_hbisc2_1#1$1",name2="avg_npc_494_1#4$1",focus=1)]
[name="芙蓉"]您看，这一份餐食大约是一个成年人一餐的量，但其中含有的盐和油至少是推荐摄入量的三倍和五倍，这对健康可有害无利啊。
[Character(name="avg_1024_hbisc2_1#1$1",name2="avg_npc_494_1#1$1",focus=2)]
[name="小吃摊主"]姑娘，这道菜我可做了几十年了，来吃的人就没有不说好的。
[Character(name="avg_1024_hbisc2_1#1$1",name2="avg_npc_494_1#1$1",focus=2)]
[name="小吃摊主"]突然改了配方，我那些老主顾可是要骂人的！
[Character(name="avg_1024_hbisc2_1#2$1",name2="avg_npc_494_1#1$1",focus=1)]
[name="芙蓉"]这也是为了大家的健康着想。
[Character(name="avg_1024_hbisc2_1#5$1",name2="avg_npc_494_1#1$1",focus=1)]
[name="芙蓉"]来这里消费的，包括我自己在内，都是感染者，这种高油高盐的饮食对感染者的伤害只会比对健康人更大......
[Character(name="avg_1024_hbisc2_1#5$1",name2="avg_npc_494_1#1$1",focus=2)]
[name="小吃摊主"]我就问你一件事，我做的这道菜到底好不好吃？
[Character(name="avg_1024_hbisc2_1#8$1",name2="avg_npc_494_1#1$1",focus=1)]
[name="芙蓉"]......非常美味。
[Character(name="avg_1024_hbisc2_1#8$1",name2="avg_npc_494_1#6$1",focus=2)]
[name="小吃摊主"]这不就结了！
[Character(name="avg_1024_hbisc2_1#4$1",name2="avg_npc_494_1#6$1",focus=1)]
[name="芙蓉"]可我还是觉得——
[Character(name="avg_1024_hbisc2_1#4$1",name2="avg_npc_494_1#1$1",focus=2)]
[name="小吃摊主"]好啦好啦，知道你无福消受我的手艺了。
[Character(name="avg_1024_hbisc2_1#4$1",name2="avg_npc_494_1#1$1",focus=1)]
[name="芙蓉"]哈哈......
[Character(name="avg_1024_hbisc2_1#1$1",name2="avg_npc_494_1#1$1",focus=1)]
[name="芙蓉"]对了，我问您一些问题，可以吗？
[Character(name="avg_1024_hbisc2_1#1$1",name2="avg_npc_494_1#1$1",focus=2)]
[name="小吃摊主"]反正现在又没生意上门，你问就是了。
[Character(name="avg_1024_hbisc2_1#1$1",name2="avg_npc_494_1#1$1",focus=1)]
[name="芙蓉"]您最近生意怎么样？
[Character(name="avg_1024_hbisc2_1#1$1",name2="avg_npc_494_1#1$1",focus=2)]
[name="小吃摊主"]忙得很！可能是因为天气暖和，这几天来吃饭的人越来越多了。
[dialog]
[PlaySound(key="$d_avg_penrustle")]
[delay(time=0.7)]
[Character(name="avg_1024_hbisc2_1#1$1",name2="avg_npc_494_1#1$1",focus=1)]
[name="芙蓉"]来吃饭的人您都认识吗？
[Character(name="avg_1024_hbisc2_1#1$1",name2="avg_npc_494_1#1$1",focus=2)]
[name="小吃摊主"]认识啊。来照顾我生意的都是夕照区的人，我基本上都认识。
[Character(name="avg_1024_hbisc2_1#9$1",name2="avg_npc_494_1#1$1",focus=1)]
[name="芙蓉"]大家都是感染者？
[Character(name="avg_1024_hbisc2_1#9$1",name2="avg_npc_494_1#1$1",focus=2)]
[name="小吃摊主"]没错。
[dialog]
[PlaySound(key="$d_avg_penrustle")]
[delay(time=0.7)]
[Character(name="avg_1024_hbisc2_1#7$1",name2="avg_npc_494_1#1$1",focus=1)]
[name="芙蓉"]有没有已经一段时间不露面，但这几天又来光顾的客人？
[Character(name="avg_1024_hbisc2_1#7$1",name2="avg_npc_494_1#1$1",focus=2)]
[name="小吃摊主"]有，好像还不少呢。
[Character(name="avg_1024_hbisc2_1#8$1",name2="avg_npc_494_1#1$1",focus=1)]
[name="芙蓉"]能不能麻烦您告诉我，都有哪几位客人是这种情况？他们都住哪里？
[musicvolume(volume=0.2, fadetime=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[musicvolume(volume=0.4, fadetime=1)]
[Character(name="avg_1024_hbisc2_1#10$1",name2="avg_npc_494_1#1$1",focus=1)]
[name="芙蓉"]谢谢您！
[Character(name="avg_1024_hbisc2_1#10$1",name2="avg_npc_494_1#1$1",focus=2)]
[name="小吃摊主"]客气！
[Character(name="avg_1024_hbisc2_1#8$1",name2="avg_npc_494_1#1$1",focus=1)]
[name="芙蓉"]最后......您最近感觉怎么样？
[Character(name="avg_1024_hbisc2_1#8$1",name2="avg_npc_494_1#1$1",focus=2)]
[name="小吃摊主"]你说矿石病？挺正常的，不好不坏。不过最近生意好，我每天进货都特别有劲儿。
[Charact

... (全文18150字符)
```

### level_act18side_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="28_g2_slumstreets",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$frontline_intro", key="$frontline_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
行板竭力为芙蓉抵挡着人潮，但一个人的力量实在太过渺小。
[dialog]
[Character(name="avg_1024_hbisc2_1#5$1",fadetime=0.3)]
[PlaySound(key="$d_avg_crowdrun", volume=1)]
[delay(time=0.6)]
人群很快越过行板，将芙蓉团团围住。
[Character(name="avg_npc_498_1#1$1")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="醉酒的感染者"] 别让我说第二遍，滚！
[dialog]
[character]
[name="行板"]你们到底在干什么？！她是来帮你们的，你们为什么要这么做？！
[Character(name="avg_npc_488_1#1$1")]
[name="可疑的感染者"] 行板，这事跟你没关系！要是想保护这个魔族佬，就赶紧让她离开夕照区！
[dialog]
[character]
[multiline(name="白垩")] 这——
[multiline(name="白垩")] 这是怎么了？
[name="行板"]白垩？芙蓉在里面......她被人围攻了！
[dialog]
[character]
[name="白垩"]让开，让开——让我进去！！
[dialog]
[PlaySound(key="$rungeneral", volume=0.9)]
[CameraShake(duration=2, xstrength=0, ystrength=15, vibrato=20, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.1, block=true)]
[PlaySound(key="$fightgeneral",volume=0.3)]
[PlaySound(key="$fightgeneral",channel="F",delay=0.2,volume=0.3)]
[backgroundTween(xFrom=0, yFrom=0, xTo=0, yTo=0, xScaleFrom=1, yScaleFrom=1, xScaleTo=1.1, yScaleTo=1.1, duration=2.5, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1.2)]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[Blocker(a=0, r=1,g=1, b=1, fadetime=0, block=true)]
[Blocker(a=1, r=1,g=1, b=1, fadetime=0.5, block=true)]
[background]
[delay(time=0.51)]
[Image(image="28_i02", fadetime=0.7,xScale=1.5, yScale=1.5, x=300, y=280)]
[Blocker(a=0, r=1,g=1, b=1, fadetime=0.5, block=true)]
[delay(time=0.7)]
[ImageTween(xScaleTo=1, yScaleTo=1, duration=3, xTo=0, yTo=0, ease="InOutQuint", block=false)]
[delay(time=1.5)]
[name="醉酒的感染者"]你又是从哪儿冒出来的？
[name="醉酒的感染者"]哦，我想起来了，你是之前流浪到夕照区的那小子吧？乖乖照顾你爷爷去，别多管闲事！
[CameraShake(duration=0.3, xstrength=20, ystrength=20, vibrato=90, randomness=90, fadeout=true, block=false)]
[name="白垩"]芙蓉她明明是来帮助大家的，你们为什么要这么对她？
[name="醉酒的感染者"]你这种人根本不可能懂，我们是在从魔族佬手里保护自己的家园！滚！
[name="白垩"]芙蓉不是这样的人！
[name="白垩"]我只知道芙蓉是来治矿石病的，她全心全意扑在这件事上，你们不也都看在眼里吗？
[name="可疑的感染者"] 治矿石病？谁的矿石病被她治好了？
[name="芙蓉"]白垩，你别来蹚这摊浑水，这里毕竟是维谢海姆，他们不敢——
[name="醉酒的感染者"]谁说我不敢？！
[Dialog]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[image]
[PlaySound(key="$b_char_tokendead", volume=0.6)]
[PlaySound(key="$e_atk_magic_m", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.3, block=true)]
[PlaySound(key="$d_avg_doorbreak", volume=0.8)]
[Character(name="avg_npc_482_1#3$1")]
[Background(image="28_g2_slumstreets",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=0.51)]
[name="白垩"]大提琴？！
[Character(name="avg_1024_hbisc2_1#6$1")]
[name="芙蓉"]你疯了吗？！
[Character(name="avg_1024_hbisc2_1#6$1")]
[name="芙蓉"]有什么事情冲我来，为什么要冲着他施术？这事跟他有什么关系？！
[Character(name="avg_npc_498_1#1$1")]
[name="醉酒的感染者"]我......我没想冲着人——
[Character(name="avg_npc_488_1#1$1")]
[name="可疑的感染者"] 没什么好解释的！再不走，你们就要和这把大提琴一样，身上开个洞了！
[dialog]
[character]
[stopmusic(fadetime=1)]
[delay(time=1)]
[PlaySound(key="$d_avg_flute_attack", volume=0.8)]
[Character(name="avg_npc_488_1#1$1")]
[name="可疑的感染者"] 笛声？
[Character(name="avg_npc_488_1#1$1")]
[name="可疑的感染者"] 又从哪冒出来一个碍事的，出来！
[playMusic(intro="$ponder_intro", key="$ponder_loop", volume=0.4)]
[delay(time=1)]
[Character(name="avg_npc_496_1#1$1")]
[name="好事的感染者"]......
[Character(name="avg_npc_496_1#1$1")]
[name="好事的感染者"]我——心跳得好快......
[Character(name="avg_npc_488_1#1$1")]
[name="可疑的感染者"] *莱塔尼亚粗口*，他怎么冒出来了......
[Dialog]
[PlaySound(key="$rungeneral", volume=0.9)]
[characteraction(name="middle", type="move", xpos=-300, fadetime=2,block=false)]
[Character(fadetime=0.5)]
[delay(time=2)]
[Character(name="avg_npc_498_1#1$1")]
[name="醉酒的感染者"]大家，大家别走啊，怎么......
[Character(name="avg_npc_496_1#1$1")]
[name="好事的感染者"]你还没听见吗，那个声音......
[Dialog]
[PlaySound(key="$rungeneral", volume=0.9)]
[characteraction(name="middle", type="move", xpos=-300, fadetime=2,block=false)]
[Character(fadetime=0.5)]
[delay(time=2)]
[Character(name="avg_npc_498_1#1$1")]
[name="醉酒的感染者"]......难道是......难道是那位——难道是......
[Character(name="avg_npc_498_1#1$1")]
[name="醉酒的感染者"]您千万开恩，您手下留情，您——我就是多喝了几口，绝对没有对您不敬的意思......
[Character(name="avg_npc_498_1#1$1")]
[name="醉酒的感染者"]——我到底在干什么啊！
[Dialog]
[PlaySound(key="$rungeneral", volume=0.9)]
[characteraction(name="middle", type="move", xpos=-300, fadetime=2,block=false)]
[Character(fadetime=0.5)]
[delay(time=2)]
[Character(name="avg_1024_hbisc2_1#9$1")]
[multiline(name="芙蓉")] 人群......
[Character(name="avg_1024_hbisc2_1#3$1")]
[multiline(name="芙蓉")]这么快就散了？
[Character(name="avg_1024_hbisc2_1#9$1")]
[name="芙蓉"]白垩，你怎么样？没受伤吧！
[Character(name="avg_npc_482_1#7$1")]
[name="白垩"]我没事，可是琴......
[Character(name="avg_1024_hbisc2_1#4$1")]
[name="芙蓉"]啊，这大提琴......面板破得这么严重，还能修吗？
[Character(name="avg_npc_482_1#7$1")]
[name="白垩"]不知道......
[Dialog]
[stopmusic(fadetime=3)]
[delay(time=2)]
[Character(name="char_empty", name2="avg_1024_hbisc2_1#1$1")]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[Character(name="avg_4046_ebnhlz_1#1$2", name2="avg_1024_hbisc2_1#1$1",fadetime=0.7)]
[delay(time=1.5)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.4)]
[Character(name="avg_4046_ebnhlz_1#1$2", name2="avg_1024_hbisc2_1#1$1",focus=2)]
[name="芙蓉"]多谢你出手相助。
[Character(name="avg_4046_ebnhlz_1#1$2", name2="avg_1024_hbi

... (全文18858字符)
```

### level_act18side_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="28_g1_gorgeousstreets",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Character(name="avg_4046_ebnhlz_1#1$1", name2="avg_npc_482_1#1$1",focus=1)]
[name="黑键"]让我看看......没错，就是这家。
[Character(name="avg_4046_ebnhlz_1#1$1", name2="avg_npc_482_1#3$1",focus=2)]
[name="白垩"]这么豪华，真的是乐器店吗？
[Character(name="avg_4046_ebnhlz_1#1$1", name2="avg_npc_482_1#3$1",focus=1)]
[name="黑键"]当然，这是全维谢海姆最好的乐器商店，要不然我也不会带你来了。
[Character(name="avg_4046_ebnhlz_1#1$1", name2="avg_npc_482_1#12$1",focus=2)]
[name="白垩"]可我来高庭区根本没申请......
[Character(name="avg_4046_ebnhlz_1#7$1", name2="avg_npc_482_1#12$1",focus=1)]
[name="黑键"]那帮官僚效率低得很，等他们看到你的申请，音乐会都结束了。
[Character(name="avg_4046_ebnhlz_1#1$1", name2="avg_npc_482_1#12$1",focus=1)]
[name="黑键"]再说，就算被发现了，不也就是罚款么。
[Character(name="avg_4046_ebnhlz_1#1$1", name2="avg_npc_482_1#7$1",focus=2)]
[name="白垩"]我听说，要是有人协助感染者离开夕照区，对这个人的处罚比对感染者本人更重......
[Character(name="avg_4046_ebnhlz_1#1$1", name2="avg_npc_482_1#7$1",focus=1)]
[name="黑键"]怕什么，没关系的。
[Character(name="avg_4046_ebnhlz_1#11$1", name2="avg_npc_482_1#7$1",focus=1)]
[name="黑键"]把腰挺直了，别畏缩，要是被看出来也很麻烦的——
[Character(name="avg_npc_068")]
[name="资历尚浅的店员"]先生您好，请问您是要挑选乐器，还是......
[Character(name="avg_4046_ebnhlz_1#1$1", name2="avg_npc_482_1#7$1",focus=1)]
[name="黑键"]当然，我们来选购一把大提琴。
[Character(name="avg_npc_068")]
[name="资历尚浅的店员"]好的。
[Character(name="avg_npc_068")]
[name="资历尚浅的店员"]不知这位先生是？
[Character(name="avg_4046_ebnhlz_1#9$1", name2="avg_npc_482_1#7$1",focus=1)]
[name="黑键"]他？他是我的......
[Character(name="avg_npc_068")]
[name="资历尚浅的店员"]先生，虽然失礼，但我得提醒您，衣着不整的人是禁止入店的。
[Character(name="avg_4046_ebnhlz_1#1$1", name2="avg_npc_482_1#9$1",focus=2)]
[name="白垩"]那我还是在外面等着......
[Character(name="avg_npc_068")]
[name="资历尚浅的店员"]在外面？您这样鬼鬼祟祟，到底在害怕什么？您——
[Character(name="avg_4046_ebnhlz_1#8$1", name2="avg_npc_482_1#9$1",focus=1)]
[name="黑键"]你知道自己在怀疑谁吗？衣着不整、鬼鬼祟祟......竟敢这样形容一位贵族，是不是不想在这儿干下去了？
[Character(name="avg_4046_ebnhlz_1#8$1", name2="avg_npc_482_1#9$1",focus=1)]
[name="黑键"]他现在只是一时困窘，不得已穿得朴素些，衣着既无脏污又无缺损，你凭什么不让他入店？
[Character(name="avg_npc_068")]
[name="资历尚浅的店员"]请恕我失言，可这位先生的穿着，与本店的整体格调......
[Character(name="avg_4046_ebnhlz_1#7$1", name2="avg_npc_482_1#9$1",focus=1)]
[name="黑键"]格调？
[Character(name="avg_4046_ebnhlz_1#8$1", name2="avg_npc_482_1#9$1",focus=1)]
[name="黑键"]我这位——堂兄弟，刚刚遭了很大的变故，视若珍宝的大提琴也在动荡中遭到破坏。
[Character(name="avg_4046_ebnhlz_1#8$1", name2="avg_npc_482_1#9$1",focus=1)]
[name="黑键"]我正想带他来买把新琴，略表慰问之意，哪轮得到你来妄谈什么格调？
[Character(name="avg_npc_068")]
[name="资历尚浅的店员"]我对此感到十分痛心，但衣着不整之人禁止入内，这也是我们的规定。
[Character(name="avg_npc_068")]
[name="资历尚浅的店员"]很抱歉，我不能让您的这位同伴入店。
[Character(name="avg_4046_ebnhlz_1#13$1", name2="avg_npc_482_1#9$1",focus=1)]
[name="黑键"]好！
[dialog]
[PlaySound(key="$d_avg_clothmovement", volume=0.7)]
黑键把自己的斗篷脱了下来，直接披在白垩身上。
[Character(name="avg_4046_ebnhlz_1#13$2")]
[name="黑键"]现在他和我穿了一样的衣服，他能不能进？还是说，我这件斗篷也算衣着不整的一部分？
[Character(name="avg_4046_ebnhlz_1#8$2")]
[name="黑键"]那我一会儿再穿上这件斗篷，是不是连我都不能进了？
[Character(name="avg_npc_068")]
[name="资历尚浅的店员"]这......
[Character(name="avg_npc_068")]
[name="资历尚浅的店员"]我......我去问下店长。
[dialog]
[playsound(key="$d_gen_walk_n")]
[character(fadetime=1.5)]
[delay(time=2)]
[Character(name="avg_4046_ebnhlz_1#8$2")]
[name="黑键"]这个看人下菜碟的家伙！
[character(name="avg_npc_482_1#1$1")]
[name="白垩"]你的外套，给你......
[dialog]
[dialog]
[PlaySound(key="$d_avg_clothmovement", volume=0.7)]
[Character(name="avg_4046_ebnhlz_1#1$1", name2="avg_npc_482_1#10$1",focus=2)]
[name="白垩"]谢谢你。
[Character(name="avg_4046_ebnhlz_1#11$1", name2="avg_npc_482_1#10$1",focus=1)]
[name="黑键"]别客气。
[Character(name="avg_4046_ebnhlz_1#11$1", name2="avg_npc_482_1#10$1",focus=1)]
[name="黑键"]从一开始就是我答应要给你买琴，也是我把你拉过来的。
[Character(name="avg_4046_ebnhlz_1#11$1", name2="avg_npc_482_1#10$1",focus=1)]
[name="黑键"]就算跟那个人打一架，我也得把你带进这家店。
[dialog]
[character]
[delay(time=1)]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_npc_068",fadetime=1.5)]
[delay(time=2)]
[name="资历尚浅的店员"]万分抱歉，本店向两位致以诚挚的歉意。
[Character(name="avg_npc_068")]
[name="资历尚浅的店员"]店长马上就来，他将亲自为两位介绍本店的乐器......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_1024_hbisc2_1#1$1")]
[Delay(time=2)]
[Background(image="28_g2_slumstreets",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[name="芙蓉"]您好，请问您现在有时间吗？
[Character(name="avg_npc_497_1#1$1")]
[name="和善的感染者"]是芙蓉呀。
[name="和善的感染者"]有的有的。
[Character(name="avg_1024_hbisc2_1#1$1")]
[name="芙蓉"]关于您的病情......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="28_g1_gorgeousstreets",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$warm_intro", key="$warm_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[Character(name="avg_4046_ebnhlz_1#1$1", name2="avg_npc_482_1#1$1",fadetime=0.7)]
[delay(time=1)]
[Character(name="avg_4046_ebnhlz_1#1$1", name2="avg_npc_482_1#1$1",focus=2)]
[name="白垩"]呼......
[Character(name="avg_4046_ebnhlz_1#1$1", name2="avg_npc_482_1#5$1",focus=2)]
[name="白垩"]我真怕刚才那个店员突然报告治安官......
[Character(name="avg_4046_ebnhlz_1#1$1", name2="avg_npc_482_1#5$1",focus=1)]
[name="黑键"]怎么会呢，他又不知道你是感染者，只不过看你穿得穷酸，把你当成一般的平民——
[Character(name="avg_4046_ebnhlz_1#9$1", name2="avg_npc_482_1#5$1",focus=1)]
[name="黑键"]啧啧，我们忘了一样东西。
[Character(name="avg_4046_ebnhlz_1#9$1", name2="avg_npc_482_1#3$1",focus=2)]
[name="白垩"]忘了东西？
[Character(name="avg_4046_ebnhlz_1#1$1", name2="avg_npc_482_1#3$1",focus=1)]
[name="黑键"]演出服啊。
[Character(name="avg_4046_ebnhlz_1#1$1", name2="avg_npc_482_1#3$1",focus=1)]
[name="黑键"]你可不能穿这一身上台演出，太不正式了。
[Character(name="avg_4046_ebnhlz_1#1$1", name2="avg_npc_482_1#3$1",focus=1)]
[name="黑键

... (全文20669字符)
```

### level_act18side_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="28_g5_czernyhome",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Character(name="avg_4046_ebnhlz_1#1$2", name2="avg_4047_pianst_1#6$1",focus=2)]
[name="车尔尼"]不行。
[Character(name="avg_4046_ebnhlz_1#1$2", name2="avg_4047_pianst_1#6$1",focus=2)]
[name="车尔尼"]三连音这里......不，整首曲子都是这样。
[Character(name="avg_4046_ebnhlz_1#1$2", name2="avg_4047_pianst_1#6$1",focus=2)]
[name="车尔尼"]之前我以为你在炫耀，可这几遍练下来，你不像是炫耀，倒像是故意把高难处处理得花里胡哨，好把不那么要求技巧的段落糊弄过去。
[Character(name="avg_4046_ebnhlz_1#1$2", name2="avg_4047_pianst_1#6$1",focus=2)]
[name="车尔尼"]按理说，这首曲子你现在已经很熟了，简单的地方有什么好糊弄的？
[Character(name="avg_4046_ebnhlz_1#8$2", name2="avg_4047_pianst_1#6$1",focus=1)]
[name="黑键"]简单的地方有什么好糊弄的......把刻板的重复训练糊弄过去，你觉得这个回答怎么样？
[Character(name="avg_4046_ebnhlz_1#8$2", name2="avg_4047_pianst_1#1$1",focus=2)]
[name="车尔尼"]生气了？
[Character(name="avg_4046_ebnhlz_1#8$2", name2="avg_4047_pianst_1#1$1",focus=1)]
[name="黑键"]什么炫耀啊糊弄啊，不就是些说辞吗？
[Character(name="avg_4046_ebnhlz_1#2$2", name2="avg_4047_pianst_1#1$1",focus=1)]
[name="黑键"]在我看来，我就只是在一遍一遍地重复着同一首曲子。
[Character(name="avg_4046_ebnhlz_1#2$2", name2="avg_4047_pianst_1#1$1",focus=2)]
[name="车尔尼"]不理解也没关系，但你现在要上的是我的音乐会，我说不行，就是不行。
[Character(name="avg_4046_ebnhlz_1#2$2", name2="avg_4047_pianst_1#1$1",focus=2)]
[name="车尔尼"]练下去，直到你彻底理解我说的是什么。
[Character(name="avg_4046_ebnhlz_1#1$2", name2="avg_4047_pianst_1#1$1",focus=1)]
[name="黑键"]好啊，正好我也想知道，我到底在逃避什么子虚乌有的东西。
[Character(name="avg_4046_ebnhlz_1#1$2", name2="avg_4047_pianst_1#1$1",focus=2)]
[name="车尔尼"]从第十七小节开始，一、二、三、四，预备......
[musicvolume(volume=0.2, fadetime=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[musicvolume(volume=0.4, fadetime=1)]
[Character(name="avg_4046_ebnhlz_1#1$2", name2="avg_4047_pianst_1#1$1",focus=2)]
[name="车尔尼"]......
[Character(name="avg_4046_ebnhlz_1#13$2", name2="avg_4047_pianst_1#1$1",focus=1)]
[name="黑键"]怎么了？
[Character(name="avg_4046_ebnhlz_1#13$2", name2="avg_4047_pianst_1#1$1",focus=2)]
[name="车尔尼"]......你吹刚才这一遍的时候，是什么感觉？
[Character(name="avg_4046_ebnhlz_1#1$2", name2="avg_4047_pianst_1#1$1",focus=1)]
[name="黑键"]什么感觉？没什么感觉啊。
[Character(name="avg_4046_ebnhlz_1#1$2", name2="avg_4047_pianst_1#2$1",focus=2)]
[name="车尔尼"]不对。
[Character(name="avg_4046_ebnhlz_1#1$2", name2="avg_4047_pianst_1#1$1",focus=2)]
[name="车尔尼"]你在跟我怄气。
[Character(name="avg_4046_ebnhlz_1#13$2", name2="avg_4047_pianst_1#1$1",focus=1)]
[name="黑键"]......这也值得你特地跟我说一声？
[Character(name="avg_4046_ebnhlz_1#13$2", name2="avg_4047_pianst_1#8$1",focus=2)]
[name="车尔尼"]我直说吧，这一遍的效果是今天最好的。
[Character(name="avg_4046_ebnhlz_1#8$2", name2="avg_4047_pianst_1#8$1",focus=1)]
[name="黑键"]开什么玩笑。
[Character(name="avg_4046_ebnhlz_1#8$2", name2="avg_4047_pianst_1#1$1",focus=2)]
[name="车尔尼"]我有跟你开玩笑的必要吗？
[Character(name="avg_4046_ebnhlz_1#3$2", name2="avg_4047_pianst_1#1$1",focus=1)]
[name="黑键"]......
[Character(name="avg_4046_ebnhlz_1#3$2", name2="avg_4047_pianst_1#8$1",focus=2)]
[name="车尔尼"]你满脑子跟我较劲的想法，对不对？
[Character(name="avg_4046_ebnhlz_1#3$2", name2="avg_4047_pianst_1#8$1",focus=2)]
[name="车尔尼"]其实这就对了。我作这首曲子时心中所想的，正是一个经常和我较劲的人。
[Character(name="avg_4046_ebnhlz_1#3$2", name2="avg_4047_pianst_1#8$1",focus=1)]
[name="黑键"]......
[Character(name="avg_4046_ebnhlz_1#3$2", name2="avg_4047_pianst_1#1$1",focus=2)]
[name="车尔尼"]一言不发，看来还在气头上？
[Character(name="avg_4046_ebnhlz_1#3$2", name2="avg_4047_pianst_1#1$1",focus=2)]
[name="车尔尼"]还是说对我意见实在太大，已经不想理我了？
[Character(name="avg_4046_ebnhlz_1#3$2", name2="avg_4047_pianst_1#1$1",focus=1)]
[name="黑键"]不，我其实是以为......
[Character(name="avg_4046_ebnhlz_1#3$2", name2="avg_4047_pianst_1#1$1",focus=2)]
[name="车尔尼"]以为？
[Character(name="avg_4046_ebnhlz_1#5$2", name2="avg_4047_pianst_1#1$1",focus=1)]
[name="黑键"]（深呼吸）
[Character(name="avg_4046_ebnhlz_1#9$2", name2="avg_4047_pianst_1#1$1",focus=1)]
[name="黑键"]——以为你对我有意见。
[Character(name="avg_4046_ebnhlz_1#9$2", name2="avg_4047_pianst_1#1$1",focus=2)]
[name="车尔尼"]......我对你确实有意见。
[Character(name="avg_4046_ebnhlz_1#9$2", name2="avg_4047_pianst_1#1$1",focus=1)]
[name="黑键"]确实有意见......因为我是贵族？
[Character(name="avg_4046_ebnhlz_1#9$2", name2="avg_4047_pianst_1#2$1",focus=2)]
[name="车尔尼"]这是原因之一，但并不特别重要。
[Character(name="avg_4046_ebnhlz_1#9$2", name2="avg_4047_pianst_1#1$1",focus=2)]
[name="车尔尼"]我的确不喜欢贵族，但这不妨碍我为贵族的音乐击节赞叹。
[Character(name="avg_4046_ebnhlz_1#9$2", name2="avg_4047_pianst_1#1$1",focus=2)]
[name="车尔尼"]就像那些贵族视我为不洁者，也不妨碍他们在家练习我的曲子一样。
[Character(name="avg_4046_ebnhlz_1#9$2", name2="avg_4047_pianst_1#1$1",focus=2)]
[name="车尔尼"]即使是养尊处优、不知人间疾苦的幸运儿，只要他对音乐有足够的敬畏和追求，也未必不能诠释出生之欢乐。
[Character(name="avg_4046_ebnhlz_1#9$2", name2="avg_4047_pianst_1#6$1",focus=2)]
[name="车尔尼"]但你的演奏，有时刻意炫技，有时敷衍了事，整体上就像......
[Character(name="avg_4046_ebnhlz_1#9$2", name2="avg_4047_pianst_1#1$1",focus=2)]
[name="车尔尼"]一边心不在焉地应付工作，一边又在细枝末节处做些花活，来向别人证明你不是不行，只是不愿意做。
[Character(name="avg_4046_ebnhlz_1#9$2", name2="avg_4047_pianst_1#6$1",focus=2)]
[name="车尔尼"]我很严肃地认为，这是一种对音乐的亵渎，我绝对不能接受这种态度。
[Character(name="avg_4046_ebnhlz_1#9$2", name2="avg_4047_pianst_1#1$1",focus=2)]
[name="车尔尼"]好在你已经向我证明，你不是故意的。
[Character(name="avg_4046_ebnhlz_1#9$2", name2="avg_4047_pianst_1#1$1",focus=2)]
[name="车尔尼"]至少，你有摆脱这种状态的能力。
[Character(name="avg_4046_ebnhlz_1#9$2", name2="avg_4047_pianst_1#7$1",focus=2)]
[name="车尔尼"]我现在更怀疑，你可能有一个技巧很高明，对学生却极不负责任的音乐教师。
[Character(name="avg_4046_ebnhlz_1#1$2", name2="avg_4047_pianst_1#7$1",focus=1)]
[name="黑键"]......没错，我的音乐教师就是这样一个人。
[Character(name="avg_4046_ebnhlz_1#8$2", name2="avg_4047_pianst_1#7$1",focus=1)]
[name="黑键"]拜他所赐，几乎每一样乐器我都能演上几手，可我从骨子里讨厌他。
[Character(name="avg_4046_ebnhlz_1#8$2", name2="avg_4047_pianst_1#7$1",focus=2)]
[name="车尔尼"]如果真是这样，他的音乐恐怕也很不同寻常

... (全文20525字符)
```

### level_act18side_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="28_g6_whitehome",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$d_avg_knockdoorfast", volume=0.4)]
[delay(time=2)]
[Character(name="avg_npc_482_1#6$1")]
[name="白垩"]（哈欠）
[Character(name="avg_npc_482_1#6$1")]
[name="白垩"]来了，来了......
[dialog]
[character]
[PlaySound(key="$dooropenquite")] 
[character(name="avg_1024_hbisc2_1#5$1",fadetime=1.5)]
[delay(time=2)]
[Character(name="avg_npc_482_1#3$1")]
[name="白垩"]......芙蓉？
[Character(name="avg_npc_482_1#6$1")]
[name="白垩"]早上好......你起得好早啊，天刚刚亮——
[Character(name="avg_1024_hbisc2_1#5$1")]
[name="芙蓉"] 黑键呢？
[Character(name="avg_npc_482_1#6$1")]
[name="白垩"]黑键？黑键还在睡啊。
[Character(name="avg_npc_482_1#12$1")]
[name="白垩"]你眼睛好红，难道是熬夜了？
[Character(name="avg_1024_hbisc2_1#5$1")]
[name="芙蓉"] ——把他也叫起来，赶快。
[musicvolume(volume=0.2, fadetime=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Delay(time=1)]
[Background(image="28_g2_slumstreets",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[musicvolume(volume=0.4, fadetime=1)]
[Character(name="avg_4046_ebnhlz_1#1$2")]
[name="黑键"]假愈？
[Character(name="avg_4046_ebnhlz_1#1$2")]
[name="黑键"]我完全听不懂你想说什么。
[Character(name="avg_1024_hbisc2_1#5$1")]
[name="芙蓉"] 你是真的听不懂，还是——
[Character(name="avg_1024_hbisc2_1#5$1")]
[name="芙蓉"] 算了，我再解释一遍。
[Character(name="avg_1024_hbisc2_1#5$1")]
[name="芙蓉"] 我来夕照区，是为了调查这里感染者异常好转的现象。
[Character(name="avg_1024_hbisc2_1#5$1")]
[name="芙蓉"] 但根据我们这几天的走访，夕照区的感染者并不是好转，而是“假愈”。
[Character(name="avg_1024_hbisc2_1#5$1")]
[name="芙蓉"] 就是说，病人的状况看起来好转了，实际上却是在恶化。
[Character(name="avg_npc_482_1#3$1")]
[name="白垩"]为什么明明恶化了，看起来还像是好转？
[Character(name="avg_1024_hbisc2_1#2$1")]
[name="芙蓉"] ......我这么说吧。
[Character(name="avg_1024_hbisc2_1#5$1")]
[name="芙蓉"] 一般来说，身体受到损伤之后，最好的结局是“恢复原状”。
[Character(name="avg_1024_hbisc2_1#5$1")]
[name="芙蓉"] 如果做不到恢复原状，身体就会调动没受损的部分，去补偿在损伤中失去的功能，我们一般称为“代偿”。
[Character(name="avg_1024_hbisc2_1#5$1")]
[name="芙蓉"] 现在夕照区的大多数感染者，身体的代偿功能都被异常调动起来，导致他们看起来状态非常好，有的甚至和健康人看不出区别。
[Character(name="avg_1024_hbisc2_1#5$1")]
[name="芙蓉"] 可是，在看不见的地方，在体内，矿石病的感染程度正在快速加深......
[Character(name="avg_1024_hbisc2_1#5$1")]
[name="芙蓉"] 按照现在的速度，即将有一批人进展到失代偿阶段了。
[Character(name="avg_4046_ebnhlz_1#1$2")]
[name="黑键"]失代偿？
[Character(name="avg_1024_hbisc2_1#5$1")]
[name="芙蓉"] 损伤的程度超出了身体最大的代偿能力，脆弱的平衡被打破，患者进入矿石病的急性发作期，病情急转直下，危及生命。
[Character(name="avg_1024_hbisc2_1#5$1")]
[name="芙蓉"] 事实上，已经有人进入急性发作期了。
[Character(name="avg_npc_482_1#4$1")]
[name="白垩"]怎么会......
[Character(name="avg_4046_ebnhlz_1#1$2")]
[name="黑键"]我明白你的意思了，但这和我们有什么关系——
[Character(name="avg_4046_ebnhlz_1#3$2")]
[name="黑键"]等等，难道说白垩也危险了？
[Character(name="avg_1024_hbisc2_1#5$1")]
[name="芙蓉"] 不......
[Character(name="avg_1024_hbisc2_1#11$1")]
[name="芙蓉"] 问题不在这儿，根据对调查结果的分析......你和白垩，似乎是引发这一切的主要因素。
[Character(name="avg_4046_ebnhlz_1#3$2")]
[name="黑键"]我和白垩是引发这一切的主要因素？！
[Character(name="avg_4046_ebnhlz_1#8$2")]
[name="黑键"]你在说什么梦话！
[Character(name="avg_1024_hbisc2_1#5$1")]
[name="芙蓉"] 在分析了你们的行动轨迹之后，我可以确定，你们......或者你们携带着的什么东西，与假愈现象的发生有着极强的相关性。
[Character(name="avg_1024_hbisc2_1#5$1")]
[name="芙蓉"] 比如你们住所隔壁洗衣店的女工，前天还说自己“感觉特别好”，昨天夜里病情恶化，差点被送进感染者临终事务处。
[Character(name="avg_1024_hbisc2_1#5$1")]
[name="芙蓉"] 我现在恳请你们配合，如果有任何线索，请立刻告诉我！这是为了夕照区所有人的生命安全着想！
[Character(name="avg_4046_ebnhlz_1#9$2", name2="avg_npc_482_1#9$1")]
[name="黑键&白垩"]......
[Character(name="avg_1024_hbisc2_1#11$1")]
[name="芙蓉"] 完全想不起来吗？
[Character(name="avg_4046_ebnhlz_1#1$2")]
[name="黑键"]确实想不到。
[Character(name="avg_1024_hbisc2_1#5$1")]
[name="芙蓉"] 以防万一，你们两人跟我去一趟办事处，让我检查一下，可以吗？
[musicvolume(volume=0.2, fadetime=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Delay(time=1)]
[Background(image="28_g4_embassy",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[musicvolume(volume=0.4, fadetime=1)]
[Character(name="avg_1024_hbisc2_1#5$1")]
[name="芙蓉"] 从指标上看，一个是再正常不过的健康人，一个是稳定期的矿石病患者......
[Character(name="avg_1024_hbisc2_1#7$1")]
[name="芙蓉"] 这怎么可能......
[Dialog]
[Character(name="avg_1024_hbisc2_1#7$1", name2="char_empty")]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="right", type="move", xpos=200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="right", type="move", xpos=-200, fadetime=1, block=false)]
[Character(name="avg_1024_hbisc2_1#7$1", name2="avg_npc_501_1#1$1",fadetime=0.7)]
[delay(time=2)]
[Character(name="avg_1024_hbisc2_1#7$1", name2="avg_npc_501_1#1$1",focus=2)]
[name="行板"]芙蓉，这次是夕照厅后面乐器店的老板！
[Character(name="avg_1024_hbisc2_1#5$1", name2="avg_npc_501_1#1$1",focus=1)]
[name="芙蓉"] ——情况如何？
[Character(name="avg_1024_hbisc2_1#5$1", name2="avg_npc_501_1#1$1",focus=2)]
[name="行板"]还好，老板和高庭区的医院签过协议，人已经被接走了。
[Character(name="avg_1024_hbisc2_1#5$1", name2="avg_npc_501_1#1$1",focus=1)]
[name="芙蓉"] 也是假愈？
[Character(name="avg_1024_hbisc2_1#5$1", name2="avg_npc_501_1#1$1",focus=2)]
[name="行板"]没错，他昨天下午报告的是“没有任何不适”。
[Character(name="avg_1024_hbisc2_1#5$1", name2="avg_npc_501_1#1$1",focus=2)]
[name="行板"]我去跟进一下，免得医院方面在协议上耍手段。
[Character(name="avg_1024_hbisc2_1#5$1", name2="avg_npc_501_1#1$1",focus=2)]
[name="行板"]他们俩......
[Character(name="avg_1024_hbisc2_1#1$1", name2="avg_npc_501_1#1$1",focus=1)]
[name="芙蓉"] 有我呢。
[Character(name="avg_1024_hbisc2_1#1$1", name2="avg_npc_501_1#1$1",focus=2)]
[name="行板"]那我去了！
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="right", type="move", xpos=300, fadetime=2,block=false)]
[character(name="avg_1024_hbisc2_1#1$1",name2="char_empty",fadetime=0.5)]
[delay(time=2)]
[Character(name="avg_1024_hbisc2_1#5$1")]
[name="芙蓉"] 我再问一遍，你们有任何能想到的线索吗？
[Character(name="avg_1024_hbisc2_1#5$1")]
[name="芙蓉"

... (全文18104字符)
```

### level_act18side_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="28_g1_gorgeousstreets",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$suspenseful_intro", key="$suspenseful_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Character(name="avg_4046_ebnhlz_1#4$2")]
[name="黑键"]（疯了！她疯了！那可是整整一个区块的人！）
[Character(name="avg_4046_ebnhlz_1#8$2")]
[name="黑键"]（再说，引发这种规模的事件，她以为她能逃得掉吗？）
[Character(name="avg_4046_ebnhlz_1#8$2")]
[name="黑键"]（如果我真的听了她的话，到时候她第一个供出来的就是我！）
[Character(name="avg_4046_ebnhlz_1#8$2")]
[name="黑键"]（就算失去这个机会也没什么好可惜的，我还有机会......我还等得起！）
[playsound(key="$d_gen_walk_n")]
[delay(time=1)]
[Character(name="avg_4046_ebnhlz_1#1$2")]
[name="黑键"]（到了......维谢海姆出入登记办公室......）
[dialog]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.2, block=true)]
[Blocker(a=0.4, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[Blocker(a=0.6, r=1, g=1, b=1, fadetime=0.3, block=true)]
[PlaySound(key="$d_avg_tinnitus", volume=1)]
[character]
[delay(time=0.01)]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.8, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.3, block=true)]
黑键正要推开出入登记办公室的门，激烈的头痛差点让他摔倒在地。
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.7, block=true)]
[delay(time=0.7)]
[Character(name="avg_4046_ebnhlz_1#1$2",blackstart=0.2,blackend=0.3,focus=-1)]
[name="凭空出现的声音"]临阵脱逃的懦夫......
[Character(name="avg_4046_ebnhlz_1#1$2",blackstart=0.2,blackend=0.3)]
[name="黑键"]不用你来指手画脚！
[Character(name="avg_4046_ebnhlz_1#1$2",blackstart=0.2,blackend=0.3)]
[name="黑键"]我就算死在乌提卡，也不想变成和你一样的杀人犯！
[Character(name="avg_4046_ebnhlz_1#1$2",blackstart=0.2,blackend=0.3,focus=-1)]
[name="凭空出现的声音"]你在......害怕......恐惧！
[Character(name="avg_4046_ebnhlz_1#1$2",blackstart=0.2,blackend=0.3,focus=-1)]
[name="凭空出现的声音"]如果受困于区区恐惧......你此生都无法重获自由！
[Character(name="avg_4046_ebnhlz_1#1$2",blackstart=0.2,blackend=0.3)]
[name="黑键"]闭嘴！
[Character(name="avg_4046_ebnhlz_1#1$2",blackstart=0.2,blackend=0.3,focus=-1)]
[name="凭空出现的声音"]天真的蠢货......
[Character(name="avg_4046_ebnhlz_1#1$2",blackstart=0.2,blackend=0.3)]
[name="黑键"]你爱怎么骂就怎么骂......
[Character(name="avg_4046_ebnhlz_1#1$2",blackstart=0.2,blackend=0.3,focus=-1)]
[name="凭空出现的声音"]你以为那个女人能让你从这里顺利离开吗？
[Character(name="avg_4046_ebnhlz_1#1$2",blackstart=0.2,blackend=0.3)]
[name="黑键"]？！
[musicvolume(volume=0.2, fadetime=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Delay(time=1)]
[Background(image="28_g7_concerthall_outside",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[musicvolume(volume=0.4, fadetime=1)]
[Character(name="avg_4046_ebnhlz_1#1$2")]
[name="黑键"]（好，这里现在没什么人......）
[Character(name="avg_4046_ebnhlz_1#1$2")]
[name="黑键"]（我得再小心一点，免得有人看到我......）
[musicvolume(volume=0.2, fadetime=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Delay(time=1)]
[Background(image="28_g2_slumstreets",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[musicvolume(volume=0.4, fadetime=1)]
[Character(name="avg_4046_ebnhlz_1#1$2")]
[name="黑键"]......
[Character(name="avg_4046_ebnhlz_1#1$2")]
[name="黑键"]（再往前走一点，就能走到移动城市边缘的无人地块......）
[musicvolume(volume=0, fadetime=1)]
[Character(name="avg_4046_ebnhlz_1#2$2")]
[name="黑键"]（深呼吸）
[playsound(key="$d_avg_snowstormflp", channel="wind", loop=true, volume=0.4)]
[PlaySound(key="$d_avg_deep_breath", volume=0.9)]
[dialog]
[character]
[delay(time=2)]
[stopsound(channel="wind", fadetime=2)]
[name="格特鲁德"]难道您想从移动城市边缘跳下去？
[Character(name="avg_4046_ebnhlz_1#8$2")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="黑键"]？！
[dialog]
[character]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_npc_484_1#1$1",fadetime=1.5)]
[delay(time=2)]
[musicvolume(volume=0.4, fadetime=1)]
[Character(name="avg_npc_484_1#1$1")]
[name="格特鲁德"] 这么做确实可以在最短时间内离开维谢海姆，但我非常不推荐这种方法。
[Character(name="avg_4046_ebnhlz_1#8$2")]
[name="黑键"]别逼我，格特鲁德。
[Character(name="avg_npc_484_1#1$1")]
[name="格特鲁德"] 我没有任何强迫您的意思。
[Character(name="avg_4046_ebnhlz_1#8$2")]
[name="黑键"]那就放我走，现在就从我眼前消失。
[Character(name="avg_npc_484_1#1$1")]
[name="格特鲁德"] 您想去哪儿？
[Character(name="avg_npc_484_1#1$1")]
[name="格特鲁德"] 直到音乐会结束之前，维谢海姆都处在移动中，您哪儿也去不了。
[Character(name="avg_npc_484_1#1$1")]
[name="格特鲁德"] 就算您冒着生命危险强行离开，也只能进入人迹罕至的荒野。
[Character(name="avg_4046_ebnhlz_1#9$2")]
[name="黑键"]进入人迹罕至的荒野......
[Character(name="avg_4046_ebnhlz_1#8$2")]
[name="黑键"]我宁可......
[Character(name="avg_npc_484_1#1$1")]
[name="格特鲁德"] 宁可死在荒野上，也不在维谢海姆多待一秒钟？
[Character(name="avg_4046_ebnhlz_1#1$2")]
[name="黑键"]完全正确。
[Character(name="avg_npc_484_1#2$1")]
[name="格特鲁德"] 我理解您的心情了，但您能否也冷静一下，听我把话说完呢？
[Character(name="avg_4046_ebnhlz_1#1$2")]
[name="黑键"]还有什么好说的？
[Character(name="avg_npc_484_1#5$1")]
[name="格特鲁德"] 您真的想让我在这儿把一切和盘托出吗，我的乌提卡伯爵？
[Character(name="avg_4046_ebnhlz_1#1$2")]
[name="黑键"]乌提卡伯爵......
[Character(name="avg_4046_ebnhlz_1#1$2")]
[name="黑键"]不用强调我的头衔，我知道你想说什么。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="bg_ltroom",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$plot_intro", key="$plot_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[Character(name="avg_npc_484_1#1$1",name2="avg_4046_ebnhlz_1#1$2",fadetime=0.7)]
[delay(time=1)]
[Character(name="avg_npc_484_1#1$1",name2="avg_4046_ebnhlz_1#1$2",focus=1)]
[name="格特鲁德"]首先，我可以保证，在现有条件下，我们的计划仍然可以顺利进行。
[Character(name="avg_npc_484_1#1$1",name2="avg_4046_ebnhlz_1#1$2",focus=2)]
[name="黑键"]不是我们的计划，是你的。
[Character(name="avg_npc_484_1#6$1",name2="avg_4046_ebnhlz_1#1$2

... (全文22361字符)
```

### level_act18side_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="28_g6_whitehome",screenadapt="showall")]
[Delay(time=1)]
[playsound(key="$d_avg_clock", channel="clk", loop=true, volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Character(name="avg_4046_ebnhlz_1#1$2",fadetime=0.7)]
[palysound(name="d_avg_cloakmovement",volume=0.7)]
[delay(time=1.5)]
[Character(name="avg_4046_ebnhlz_1#1$2",name2="avg_npc_482_1#7$1")]
[delay(time=0.51)]
[Character(name="avg_4046_ebnhlz_1#1$2",name2="avg_npc_482_1#7$1",focus=2)] 
[name="白垩"]你现在感觉怎么样，没问题了吗？
[Character(name="avg_4046_ebnhlz_1#1$2",name2="avg_npc_482_1#7$1",focus=1)] 
[name="黑键"]没问题......
[name="黑键"]没问题的，一定没问题的。你和我都会没问题的。
[name="黑键"]我出去一会儿，你好好在这儿待着。
[Character(name="avg_4046_ebnhlz_1#1$2",name2="avg_npc_482_1#3$1",focus=2)] 
[name="白垩"]你才刚好一点，这是要去哪里？
[Character(name="avg_4046_ebnhlz_1#2$2",name2="avg_npc_482_1#3$1",focus=1)] 
[name="黑键"]......去办事。
[Character(name="avg_4046_ebnhlz_1#2$2",name2="avg_npc_482_1#7$1",focus=2)] 
[name="白垩"]不管什么事，都等到你恢复再说吧。
[Character(name="avg_4046_ebnhlz_1#1$2",name2="avg_npc_482_1#7$1",focus=1)] 
[name="黑键"]不用担心我。
[Character(name="avg_4046_ebnhlz_1#1$2",name2="avg_npc_482_1#7$1",focus=2)] 
[name="白垩"]芙蓉也说了，如果醒了，最好休息一段时间，观察一下情况......
[Character(name="avg_4046_ebnhlz_1#8$2",name2="avg_npc_482_1#7$1",focus=1)] 
[name="黑键"]这是急事，很急的事，好吗？
[Character(name="avg_4046_ebnhlz_1#8$2",name2="avg_npc_482_1#7$1",focus=2)] 
[name="白垩"]可是我们离音乐会已经没多长时间了。我觉得现在最重要的还是把身体养好，加紧练习......这也是你的愿望啊。
[Character(name="avg_4046_ebnhlz_1#8$2",name2="avg_npc_482_1#7$1",focus=1)] 
[name="黑键"]现在就别拿这个烦我了，好不好？
[Character(name="avg_4046_ebnhlz_1#8$2",name2="avg_npc_482_1#4$1",focus=2)] 
[name="白垩"]烦？
[Character(name="avg_4046_ebnhlz_1#9$2",name2="avg_npc_482_1#4$1",focus=1)] 
[name="黑键"]......我不是这个意思。
[Character(name="avg_4046_ebnhlz_1#2$2",name2="avg_npc_482_1#4$1",focus=1)] 
[name="黑键"]但我确实非去不可，别拦着我了。我会尽快回来的。
[Character(name="avg_4046_ebnhlz_1#2$2",name2="avg_npc_482_1#7$1",focus=2)] 
[name="白垩"]真的......不能告诉我要去做什么吗？
[Character(name="avg_4046_ebnhlz_1#2$2",name2="avg_npc_482_1#7$1",focus=1)] 
[name="黑键"]如果一切顺利的话......你会知道的。
[Character(name="avg_4046_ebnhlz_1#1$2",name2="avg_npc_482_1#7$1",focus=1)] 
[name="黑键"]对了，衣服。
[Character(name="avg_4046_ebnhlz_1#1$2",name2="avg_npc_482_1#3$1",focus=2)] 
[name="白垩"]衣服？
[Character(name="avg_4046_ebnhlz_1#1$2",name2="avg_npc_482_1#3$1",focus=1)] 
[name="黑键"]约好今天下午去取的，我没法陪你去了，你自己去一趟吧。
[name="黑键"]记得带大提琴，试穿的时候试着拉一小段，看看会不会有不舒服的地方。
[name="黑键"]我走了。
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="left", type="move", xpos=300, fadetime=2,block=false)]
[character(name="char_empty",name2="avg_npc_482_1#3$1",fadetime=0.5)]
[delay(time=2)]
[StopSound(channel="clk", fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="28_g5_czernyhome",screenadapt="showall")]
[Delay(time=1)]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[character(name="avg_4047_pianst_1#1$1",name2="avg_1024_hbisc2_1#5$1",focus=1)]
[name="车尔尼"]又是你？
[character(name="avg_4047_pianst_1#1$1",name2="avg_1024_hbisc2_1#5$1",focus=2)]
[name="芙蓉"]......是我。
[name="芙蓉"]我来请求您停办这次音乐会，至少不要让黑键和白垩在音乐会上合奏了。
[character(name="avg_4047_pianst_1#6$1",name2="avg_1024_hbisc2_1#11$1",focus=1)]
[name="车尔尼"]你说什么？
[character(name="avg_4047_pianst_1#6$1",name2="avg_1024_hbisc2_1#6$1",focus=2)]
[name="芙蓉"]如果让黑键和白垩合奏，夕照区会出大事的！
[musicvolume(volume=0.2, fadetime=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(name="avg_4047_pianst_1#6$1",name2="avg_1024_hbisc2_1#5$1")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[musicvolume(volume=0.4, fadetime=1)]
[character(name="avg_4047_pianst_1#1$1",name2="avg_1024_hbisc2_1#5$1",focus=1)]
[name="车尔尼"]按你的说法，我最近身体好转，是因为黑键和白垩引发的所谓“假愈”，但假愈期一过去，我就会变成重症患者，命在旦夕。
[character(name="avg_4047_pianst_1#1$1",name2="avg_1024_hbisc2_1#5$1",focus=2)]
[name="芙蓉"]是的，您和他们接触很多，因此症状也更明显。
[character(name="avg_4047_pianst_1#1$1",name2="avg_1024_hbisc2_1#5$1",focus=1)]
[name="车尔尼"]其他和他们接触较少的人也会受到影响，如果放任他们合奏，很可能有人死去？
[character(name="avg_4047_pianst_1#1$1",name2="avg_1024_hbisc2_1#5$1",focus=2)]
[name="芙蓉"]是的。虽然原因尚不明确，但让这两个人在一起合奏，有很大可能增强他们对周围的影响。
[character(name="avg_4047_pianst_1#1$1",name2="avg_1024_hbisc2_1#5$1",focus=1)]
[name="车尔尼"]多大可能？
[character(name="avg_4047_pianst_1#1$1",name2="avg_1024_hbisc2_1#4$1",focus=2)]
[name="芙蓉"]暂时还不知道......
[character(name="avg_4047_pianst_1#2$1",name2="avg_1024_hbisc2_1#4$1",focus=1)]
[name="车尔尼"]除了我，还有谁会因此面临生命危险？
[character(name="avg_4047_pianst_1#2$1",name2="avg_1024_hbisc2_1#4$1",focus=2)]
[name="芙蓉"]......夕照区的十多人已经被送去高庭区的医院了。
[character(name="avg_4047_pianst_1#2$1",name2="avg_1024_hbisc2_1#4$1",focus=1)]
[name="车尔尼"]高庭区......也就是说，他们已经离开了黑键和白垩的影响范围？
[character(name="avg_4047_pianst_1#2$1",name2="avg_1024_hbisc2_1#4$1",focus=2)]
[name="芙蓉"]应该是这样的。
[character(name="avg_4047_pianst_1#1$1",name2="avg_1024_hbisc2_1#4$1",focus=1)]
[name="车尔尼"]我明白你的意思了。
[character(name="avg_4047_pianst_1#1$1",name2="avg_1024_hbisc2_1#9$1",focus=2)]
[name="芙蓉"]那么......
[character(name="avg_4047_pianst_1#2$1",name2="avg_1024_hbisc2_1#9$1",focus=1)]
[name="车尔尼"]不行。
[character(name="avg_4047_pianst_1#2$1",name2="avg_1024_hbisc2_1#3$1",focus=2)]
[name="芙蓉"]什么？！
[character(name="avg_4047_pianst_1#2$1",name2="avg_1024_hbisc2_1#6$1",focus=2)]
[name="芙蓉"]我不奢求您取消整场音乐会，但就算单独把黑键和白垩合奏的曲目撤了也好！或者换人也可以！
[character(name="avg_4047_pianst_1#1$1",name2="avg_1024_hbisc2_1#6$1",focus=1)]
[name="车尔尼"]如果你能证明他们的合奏一定会导致我以外的人受害，我立刻就取消这场音乐会。
[name="车尔尼"]但现在不同，连你也无法得知合奏的后果究竟是什么。我不能仅仅因为虚无缥缈的“担忧”，就让整个夕照区的努力和希望付诸东流。
[character(name="avg_4047_pianst_1#1$1",name2="avg_1024_hbisc2_1#3$1",focus=2)]
[name="芙蓉"

... (全文14799字符)
```

### level_act18side_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="28_g3_slumstreets_night",screenadapt="showall")]
[Delay(time=1)]
[Character(name="avg_4046_ebnhlz_1#8$1")]
[PlayMusic(intro="$suspenseful_intro", key="$suspenseful_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[name="黑键"]是谁？！
[Dialog]
[Character]
[Delay]
[Character(name="avg_npc_488_1$1")]
[Dialog]
[delay(time=0.7)]
[PlaySound(key="$rungeneral", volume=0.9)]
[characteraction(name="middle", type="move", xpos=-300, fadetime=2,block=false)]
[Character(fadetime=0.5)]
[delay(time=2)]
[Character(name="avg_4046_ebnhlz_1#4$1",name2="avg_npc_486_1#1$1",focus=2)]
[name="？？？"]说了别回头，人被你放跑了吧。
[Character(name="avg_4046_ebnhlz_1#8$1",name2="avg_npc_486_1#1$1",focus=1)]
[name="黑键"]你到底是谁？！
[Character(name="avg_4046_ebnhlz_1#8$1",name2="avg_npc_486_1#9$1",focus=2)]
[name="？？？"]伯爵大人，冷静，冷静。
[Character(name="avg_4046_ebnhlz_1#8$1",name2="avg_npc_486_1#10$1",focus=2)]
[name="？？？"]我正式的身份解释起来有点麻烦，你就当我是一名密探吧。我叫别格勒。
[Character(name="avg_4046_ebnhlz_1#8$1",name2="avg_npc_486_1#10$1",focus=1)]
[name="黑键"]你......为什么要挑这个时候跳出来？人是被你放跑的！
[Character(name="avg_4046_ebnhlz_1#8$1",name2="avg_npc_486_1#9$1",focus=2)]
[name="别格勒"]反正是跑进了下水道里，他要想从别的出入口逃出去，要花好长时间。
[name="别格勒"]再说，你在他进去之前就把他叫住，谁知道是不是你们察觉到了什么，见势不妙，想跟我演戏呢。
[Character(name="avg_4046_ebnhlz_1#8$1",name2="avg_npc_486_1#9$1",focus=1)]
[name="黑键"]想跟你演戏？我和他？！
[Character(name="avg_4046_ebnhlz_1#8$1",name2="avg_npc_486_1#9$1",focus=2)]
[name="别格勒"]还是说，你之前去找格特鲁德其实是被胁迫的？可别逗了。
[Character(name="avg_4046_ebnhlz_1#1$1",name2="avg_npc_486_1#9$1",focus=1)]
[name="黑键"]......
[Character(name="avg_4046_ebnhlz_1#1$1",name2="avg_npc_486_1#1$1",focus=2)]
[name="别格勒"]您的价值比他高多了，乌提卡伯爵。
[Character(name="avg_4046_ebnhlz_1#1$1",name2="avg_npc_486_1#1$1",focus=1)]
[name="黑键"]你拦不住我。
[Character(name="avg_4046_ebnhlz_1#1$1",name2="avg_npc_486_1#1$1",focus=2)]
[name="别格勒"]论打架，我确实拦不住你，但你可要想好。
[name="别格勒"]这是女皇陛下颁发的委任状，你可以看看。
[dialog]
[playsound(key="$d_avg_paper1",volume=0.8)]
[delay(time=1.2)]
[Character(name="avg_4046_ebnhlz_1#1$1",name2="avg_npc_486_1#1$1",focus=1)]
[name="黑键"]......这玩意儿我六岁就有了。
[Character(name="avg_4046_ebnhlz_1#1$1",name2="avg_npc_486_1#1$1",focus=2)]
[name="别格勒"]斗嘴我没意见，不过事关女皇陛下，你最好收敛点。
[Character(name="avg_4046_ebnhlz_1#8$1",name2="avg_npc_486_1#1$1",focus=1)]
[name="黑键"]收敛？倒是你，区区一个密探，等你明白自己抓错了人，你才是吃不了兜着走的那个。
[Character(name="avg_4046_ebnhlz_1#8$1",name2="avg_npc_486_1#2$1",focus=2)]
[name="别格勒"]你对自己的处境似乎还没什么自觉，亲爱的乌提卡伯爵。
[Character(name="avg_4046_ebnhlz_1#8$1",name2="avg_npc_486_1#1$1",focus=2)]
[name="别格勒"]行了，别在这儿拖延时间了，跟我走吧。
[Character(name="avg_4046_ebnhlz_1#1$1",name2="avg_npc_486_1#1$1",focus=1)]
[name="黑键"]去哪儿？
[Character(name="avg_4046_ebnhlz_1#1$1",name2="avg_npc_486_1#1$1",focus=2)]
[name="别格勒"]去你该去的地方。别担心，我们为各个阶层的嫌疑犯准备了符合他们身份的拘押处，你算最高级的那一批。
[Character(name="avg_4046_ebnhlz_1#1$1",name2="avg_npc_486_1#1$1",focus=1)]
[name="黑键"]我说，别格勒先生。
[Character(name="avg_4046_ebnhlz_1#1$1",name2="avg_npc_486_1#9$1",focus=2)]
[name="别格勒"]准备求饶了？还是贿赂？如果是后者，我很乐意收下。
[Character(name="avg_4046_ebnhlz_1#1$1",name2="avg_npc_486_1#9$1",focus=1)]
[name="黑键"]我很怀疑，如果我给你钱，你真的会放我走吗？我怎么觉得你把钱收进口袋之后，还是会把我抓走呢？
[Character(name="avg_4046_ebnhlz_1#1$1",name2="avg_npc_486_1#10$1",focus=2)]
[name="别格勒"]聪明。
[Character(name="avg_4046_ebnhlz_1#1$1",name2="avg_npc_486_1#10$1",focus=1)]
[name="黑键"]我开始觉得和你相处很让人痛快了，别格勒先生。你让我想起我熟悉的乌提卡，那里的人大多和你一样“高尚”。
[Character(name="avg_4046_ebnhlz_1#1$1",name2="avg_npc_486_1#10$1",focus=2)]
[name="别格勒"]荣幸之至。
[Character(name="avg_4046_ebnhlz_1#1$1",name2="avg_npc_486_1#10$1",focus=1)]
[name="黑键"]但是，我真的很想知道，刚才那个人要在下水道里搞什么名堂。
[Character(name="avg_4046_ebnhlz_1#1$1",name2="avg_npc_486_1#1$1",focus=2)]
[name="别格勒"]可你在我的眼皮子底下把他叫住了。
[Character(name="avg_4046_ebnhlz_1#1$1",name2="avg_npc_486_1#1$1",focus=1)]
[name="黑键"]这个嘛，说来惭愧，我想在地面上解决这件事。
[Character(name="avg_4046_ebnhlz_1#5$1",name2="avg_npc_486_1#1$1",focus=1)]
[name="黑键"]我的某位伯爵代理喜欢搜集让人倒胃口的故事。在一系列让人吃不下饭的故事里，只有下水道的故事劲头最大。
[Character(name="avg_4046_ebnhlz_1#5$1",name2="avg_npc_486_1#9$1",focus=2)]
[name="别格勒"]呵，既然觉得倒胃口，不如去喝杯咖啡缓一缓。
[Character(name="avg_4046_ebnhlz_1#1$1",name2="avg_npc_486_1#9$1",focus=1)]
[name="黑键"]我也想走，可我还是想知道他到底想做什么，只好也跟着他钻进去了。
[name="黑键"]这可都是你害的啊，别格勒先生。
[name="黑键"]只要你放我进去，大可以一直用法杖对准我，我不会跑的。
[Character(name="avg_4046_ebnhlz_1#1$1",name2="avg_npc_486_1#1$1",focus=2)]
[name="别格勒"]......
[name="别格勒"]我事先警告你，擅自脱离我的控制，不管出于什么原因，都一定会受到惩罚。
[Character(name="avg_4046_ebnhlz_1#1$1",name2="avg_npc_486_1#1$1",focus=1)]
[name="黑键"]会怎么样？死刑？
[Character(name="avg_4046_ebnhlz_1#1$1",name2="avg_npc_486_1#2$1",focus=2)]
[name="别格勒"]至少也是降爵。你以后一步也不能踏进乌提卡的高塔，就算你真的清白无辜也不行。
[Character(name="avg_4046_ebnhlz_1#11$1",name2="avg_npc_486_1#2$1",focus=1)]
[name="黑键"]那真是太好了，我甚至有点想试着跑一跑了呢。
[Character(name="avg_4046_ebnhlz_1#11$1",name2="avg_npc_486_1#2$1",focus=2)]
[name="别格勒"]（摇头）
[Character(name="avg_4046_ebnhlz_1#11$1",name2="avg_npc_486_1#1$1",focus=2)]
[name="别格勒"]总之，既然你非要进去不可，那就请进吧，乌提卡伯爵。
[name="别格勒"]我会紧紧盯着你的。
[Dialog]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Delay(time=1)]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[character(name="avg_1024_hbisc2_1#4$1",name2="avg_npc_489_1#2$1",focus=2)]
[name="乌尔苏拉"]芙蓉啊，不是咱说你，你不能那么跟先生说话啊。
[character(name="avg_1024_hbisc2_1#4$1",name2="avg_npc_489_1#2$1",focus=1)]
[name="芙蓉"]可是车尔尼先生他......
[character(name="avg_1024_hbisc2_1#4$1",name2="avg_npc_489_1#2$1",focus=2)]
[name="乌尔苏拉"]有很多话，先生自己是说不出口的，只好由咱老婆子来说了。
[character(name="avg_1024_hbisc2_1#4$1",name2="avg_npc_489_1#2$1",focus=1)]
[name="芙蓉"]......您请讲。
[character(name="avg_1024_hbisc2_1#4$1",name2="avg_npc_489_1#2$1",focus=2)]
[name="乌尔苏拉"]你知道夕照区的名字是怎么来的吗？
[character(name="avg_1024_hbisc2_1#4$1",name2="avg_npc_489_1#2$1",focus=1)]
[name="芙蓉"]不知道。
[charact

... (全文12737字符)
```

### level_act18side_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="28_g12_sewer",screenadapt="showall")]
[Delay(time=1)]
[PlayMusic(intro="$suspenseful_intro", key="$suspenseful_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[playsound(key="$d_avg_sewer")]
两人在幽暗而宽阔的下水道里前行。
水声聒噪，却比纯粹的寂静更让人觉得阴气森森。
[Dialog]
[Character(name="avg_4046_ebnhlz_1#1$1",name2="avg_npc_486_1#1$1",fadetime=0.7)]
[delay(time=1)]
[Character(name="avg_4046_ebnhlz_1#1$1",name2="avg_npc_486_1#1$1",focus=2)]
[name="别格勒"]别往前走了，这里右拐。
[Character(name="avg_4046_ebnhlz_1#1$1",name2="avg_npc_486_1#1$1",focus=1)]
[name="黑键"]你很熟啊。
[Character(name="avg_4046_ebnhlz_1#1$1",name2="avg_npc_486_1#1$1",focus=2)]
[name="别格勒"]我当然熟。
[Character(name="avg_4046_ebnhlz_1#1$1",name2="avg_npc_486_1#1$1",focus=1)]
[name="黑键"]密探的基本功？
[Character(name="avg_4046_ebnhlz_1#1$1",name2="avg_npc_486_1#1$1",focus=2)]
[name="别格勒"]基本中的基本。
[Character(name="avg_4046_ebnhlz_1#1$1",name2="avg_npc_486_1#1$1",focus=1)]
[name="黑键"]那你在夕照区已经干了很多年了吧。
[Character(name="avg_4046_ebnhlz_1#1$1",name2="avg_npc_486_1#9$1",focus=2)]
[name="别格勒"]想套近乎？
[Character(name="avg_4046_ebnhlz_1#1$1",name2="avg_npc_486_1#9$1",focus=1)]
[name="黑键"]只是好奇。
[Character(name="avg_4046_ebnhlz_1#1$1",name2="avg_npc_486_1#10$1",focus=2)]
[name="别格勒"]这是保密事项。
[Character(name="avg_4046_ebnhlz_1#9$1",name2="avg_npc_486_1#10$1",focus=1)]
[name="黑键"]没劲。
[Dialog]
[Delay(time=1)]
[PlaySound(key="$d_avg_runstop", volume=1)]
[Character(name="avg_4046_ebnhlz_1#3$1",name2="avg_npc_486_1#10$1",focus=1)]
[name="黑键"]......
[Character(name="avg_4046_ebnhlz_1#3$1",name2="avg_npc_486_1#1$1",focus=2)]
[name="别格勒"]怎么不走了？
[Character(name="avg_4046_ebnhlz_1#1$1",name2="avg_npc_486_1#1$1",focus=1)]
[name="黑键"]那边有什么东西。
[Character(name="avg_4046_ebnhlz_1#1$1",name2="avg_npc_486_1#1$1",focus=2)]
[name="别格勒"]别想靠这种老掉牙的把戏脱身。
[Character(name="avg_4046_ebnhlz_1#1$1",name2="avg_npc_486_1#1$1",focus=1)]
[name="黑键"]不是——你看那边，有东西在动。
[dialog]
[character]
[playsound(key="$e_atk_vibe_n")]
[delay(time=0.7)]
别格勒用手中的武器抵住乌提卡伯爵的后心，然后朝伯爵手指的方向看去。
[Character(name="avg_4046_ebnhlz_1#1$1",name2="avg_npc_486_1#1$1",focus=2)]
[name="别格勒"]只是源石虫而已。源石虫你都没见过？
[Character(name="avg_4046_ebnhlz_1#6$1",name2="avg_npc_486_1#1$1",focus=1)]
[name="黑键"]真的......只是源石虫吗？
[Character(name="avg_4046_ebnhlz_1#6$1",name2="avg_npc_486_1#7$1",focus=2)]
[name="别格勒"]堂堂乌提卡伯爵，居然被源石虫吓得走不动路，我也算是长见识了。
[Character(name="avg_4046_ebnhlz_1#6$1",name2="avg_npc_486_1#7$1",focus=1)]
[name="黑键"]我还是觉得有点不对劲......
[Character(name="avg_4046_ebnhlz_1#6$1",name2="avg_npc_486_1#3$1",focus=2)]
[name="别格勒"]别傻了，赶紧走！
[Character(name="avg_4046_ebnhlz_1#1$1",name2="avg_npc_486_1#3$1",focus=1)]
[name="黑键"]......好，好。
[Dialog]
[playsound(key="$e_atk_airshipvibe")]
[playsound(key="$e_atk_vibe_n",delay=0.4)]
[Character(name="avg_npc_486_1#4$1")]
[name="别格勒"]等等，等等。
[name="别格勒"]这个源石虫的数量......
[Character(name="avg_npc_486_1#7$1")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="别格勒"]......这绝对不正常！会出大事的！
[Character(name="avg_npc_486_1#3$1")]
[name="别格勒"]跑起来！快！
[Dialog]
[Character(name="avg_4046_ebnhlz_1#1$1", name2="char_empty")]
[characteraction(name="right", type="move", xpos=200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="right", type="move", xpos=-200, fadetime=0.5, block=false)]
[Character(name="avg_4046_ebnhlz_1#1$1", name2="avg_npc_486_1#3$1",fadetime=0.5)]
[delay(time=0.51)]
[Character(name="avg_4046_ebnhlz_1#3$1",name2="avg_npc_486_1#3$1",focus=1)]
[name="黑键"]你干什么——
[Character(name="avg_4046_ebnhlz_1#3$1",name2="avg_npc_486_1#3$1",focus=2)]
[name="别格勒"]已经要来不及了！赶快！
[Dialog]
[characteraction(name="right", type="move", xpos=-150, fadetime=0.5,block=true)]
[delay(time=0.51)]
[PlaySound(key="$rungeneral", volume=0.9)]
[characteraction(name="left", type="move", xpos=200, fadetime=0.5,block=false)]
[characteraction(name="right", type="move", xpos=200, fadetime=0.5,block=true)]
[delay(time=0.7)]
[character(fadetime=0.7)]
别格勒紧紧抓着黑键的手腕，两人在下水道里飞跑起来。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[PlaySound(key="$rungeneral", volume=0.9)]
[character(name="avg_4046_ebnhlz_1#8$1",name2="avg_npc_486_1#7$1",fadetime=1.5)]
[delay(time=2)]
[character(name="avg_4046_ebnhlz_1#8$1",name2="avg_npc_486_1#7$1",focus=1)]
[name="黑键"]呼、呼......
[name="黑键"]你脑子里是装了下水道的地图吗......
[character(name="avg_4046_ebnhlz_1#8$1",name2="avg_npc_486_1#7$1",focus=2)]
[name="别格勒"]有时间跟我阴阳怪气，还不如多喘几口。
[character(name="avg_4046_ebnhlz_1#8$1",name2="avg_npc_486_1#7$1",focus=1)]
[name="黑键"]不是阴、阴阳怪气，我是真觉得每条岔路长得都一样......
[character(name="avg_4046_ebnhlz_1#8$1",name2="avg_npc_486_1#7$1",focus=2)]
[name="别格勒"]休息好了吗？
[character(name="avg_4046_ebnhlz_1#8$1",name2="avg_npc_486_1#7$1",focus=1)]
[name="黑键"]才——
[character(name="avg_4046_ebnhlz_1#8$1",name2="avg_npc_486_1#3$1",focus=2)]
[name="别格勒"]接着跑！跑！
[Dialog]
[characteraction(name="left", type="move", xpos=200,fadetime=0.51)]
[characteraction(name="right", type="move", xpos=200,fadetime=0.51)]
[character(name="char_empty",name2="char_empty",fadetime=0.51)]
[PlaySound(key="$rungeneral", volume=0.9)]
[delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[PlaySound(key="$rungeneral", volume=0.9)]
[character(name="avg_4046_ebnhlz_1#10$1",name2="avg_npc_486_1#7$1",fadetime=1.5)]
[delay(time=2)]
[character(name="avg_4046_ebnhlz_1#10$1",name2="avg_npc_486_1#7$1",focus=1)]
[name="黑键"]（喘息声）
[name="黑键"]我......不行了......
[character(name="avg_4046_ebnhlz_1#10$1",name2="avg_npc_486_1#1$1",focus=2)]
[name="别格勒"]正好，我们也找到了该找的人。
[character(name="avg_4046_ebnhlz_1#10$1",name

... (全文21017字符)
```

### level_act18side_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="28_g3_slumstreets_night",screenadapt="showall")]
[Delay(time=1)]
[PlayMusic(intro="$escape_intro", key="$escape_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[PlaySound(key="$d_avg_magic_5")]
[CameraShake(duration=1, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.7, block=true)]
[Delay(time=0.71)]
[playsound(key="$rungeneral")]
[character(name="avg_4046_ebnhlz_1#8$1",fadetime=1.5)]
[delay(time=2)]
[character(name="avg_4046_ebnhlz_1#8$1")]
[name="黑键"]呼......呼......
[character(name="avg_4046_ebnhlz_1#10$1")]
[name="黑键"]白垩，我来了，别再拉琴了！
[character(name="avg_4046_ebnhlz_1#10$1")]
[name="黑键"]你到底想做什么，自杀吗？
[character(name="avg_npc_482_1#3$1")]
[name="白垩"]我......
[character(name="avg_npc_482_1#5$1")]
[name="白垩"]我确实在考虑这个问题。
[character(name="avg_4046_ebnhlz_1#4$1")]
[name="黑键"]？！
[character(name="avg_npc_482_1#1$1")]
[name="白垩"]用琴声将源石虫吸引过来，然后......将我自己和它们一起烧成飞灰。
[character(name="avg_npc_482_1#5$1")]
[name="白垩"]不过，既然你来了......我大概不会再有这样的机会了。
[character(name="avg_4046_ebnhlz_1#6$1")]
[name="黑键"]白垩......你......
[character(name="avg_npc_482_1#1$1")]
[name="白垩"]从很小的时候开始，我就知道，自己的体质有些不寻常。
[name="白垩"]有的感染者和我相处时间长了，病情就会变糟。
[name="白垩"]因为这个，我和爷爷一起被赶出了当时的住所，开始在村庄之间流浪。
[name="白垩"]但我一直以为，不是所有的感染者都会被我影响，而且，只要相处的时间不长就不碍事。
[character(name="avg_npc_482_1#7$1")]
[name="白垩"]但爷爷的病终于越来越重，我的第一个幻想破灭了。
[name="白垩"]然后，芙蓉告诉我们，这种叫做“假愈”的现象，在我来到夕照区短短几周之后，就造成了严重的后果。
[name="白垩"]......既然活着就会造成灾难，那我还是死了的好。
[character(name="avg_4046_ebnhlz_1#8$1")]
[name="黑键"]这不怪你！
[character(name="avg_npc_482_1#7$1")]
[name="白垩"]怎么可能不怪我呢？
[character(name="avg_4046_ebnhlz_1#6$1")]
[name="黑键"]......
[character(name="avg_4046_ebnhlz_1#1$1")]
[name="黑键"]——你知道尘世之音吗？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[delay(time=0.51)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.51)]
[character(name="avg_npc_482_1#7$1",name2="avg_4046_ebnhlz_1#6$1",focus=1)]
[name="白垩"]听你说完，我......终于想起来了。
[name="白垩"]尘世之音，死于实验的人，巫王残党......还有你。
[name="白垩"]我全都想起来了。
[character(name="avg_npc_482_1#7$1",name2="avg_4046_ebnhlz_1#10$1",focus=2)]
[name="黑键"]所以这根本就不是你的错！
[name="黑键"]错在巫王，错在那些残党，错在格特鲁德——但你是无辜的！
[character(name="avg_npc_482_1#7$1",name2="avg_4046_ebnhlz_1#10$1",focus=1)]
[name="白垩"]......嗯。
[character(name="avg_npc_482_1#1$1",name2="avg_4046_ebnhlz_1#10$1",focus=1)]
[name="白垩"]多亏了你让我想起了那些事情，我才知道，这不是什么与生俱来的体质，而是一场实验的恶果。
[character(name="avg_npc_482_1#1$1",name2="avg_4046_ebnhlz_1#6$1",focus=2)]
[name="黑键"]我也是在听了你的大提琴之后才想起来的，我才应该向你道谢。
[character(name="avg_npc_482_1#7$1",name2="avg_4046_ebnhlz_1#6$1",focus=1)]
[name="白垩"]但是......
[character(name="avg_npc_482_1#7$1",name2="avg_4046_ebnhlz_1#6$1",focus=2)]
[name="黑键"]哪有什么但是？
[character(name="avg_npc_482_1#7$1",name2="avg_4046_ebnhlz_1#6$1",focus=1)]
[name="白垩"]事情已经超出了我们的掌控，我已经连减轻自己的危害都做不到了。
[name="白垩"]再说，如果那位伯爵小姐说得没错，我本来也时日无多，不如在这里......
[character(name="avg_npc_482_1#7$1",name2="avg_4046_ebnhlz_1#8$1",focus=2)]
[name="黑键"]不！
[character(name="avg_npc_482_1#7$1",name2="avg_4046_ebnhlz_1#8$1",focus=2)]
[name="黑键"]我为什么会上格特鲁德的当？就是因为尘世之音是可以转移的！
[character(name="avg_npc_482_1#7$1",name2="avg_4046_ebnhlz_1#8$1",focus=1)]
[name="白垩"]可我的尘世之音已经是坏的了，就算转移给你......
[character(name="avg_npc_482_1#7$1",name2="avg_4046_ebnhlz_1#8$1",focus=2)]
[name="黑键"]不试一试怎么知道！
[name="黑键"]如果你已经决定赴死了，还有什么好怕的？
[character(name="avg_npc_482_1#7$1",name2="avg_4046_ebnhlz_1#8$1",focus=1)]
[name="白垩"]我不想害你。
[character(name="avg_npc_482_1#7$1",name2="avg_4046_ebnhlz_1#1$1",focus=2)]
[name="黑键"]如果我真的受害了，你再去替我操心吧。
[name="黑键"]就在这里，我们来赌一把。
[character(name="avg_npc_482_1#8$1",name2="avg_4046_ebnhlz_1#1$1",focus=1)]
[name="白垩"]......好。
[character(name="avg_npc_482_1#8$1",name2="avg_4046_ebnhlz_1#1$1",focus=2)]
[name="黑键"]你平时能感受到尘世之音的旋律吗？
[name="黑键"]不管是演奏还是施术，我都能模糊地感受到尘世之音的存在......一段已经了如指掌，但又和我完全没有关系的，刺耳的旋律。
[character(name="avg_npc_482_1#8$1",name2="avg_4046_ebnhlz_1#1$1",focus=1)]
[name="白垩"]我明白。
[character(name="avg_npc_482_1#7$1",name2="avg_4046_ebnhlz_1#1$1",focus=1)]
[name="白垩"]但我感受到的旋律并不刺耳，反而很温柔——不对，应该说是，和谐得过了头，到了空洞的地步。
[character(name="avg_npc_482_1#7$1",name2="avg_4046_ebnhlz_1#1$1",focus=2)]
[name="黑键"]我们俩努力去贴合各自感受到的旋律，试着合奏一场吧。
[character(name="avg_npc_482_1#5$1",name2="avg_4046_ebnhlz_1#1$1",focus=1)]
[name="白垩"]合奏......可是没有听众啊。
[character(name="avg_npc_482_1#5$1",name2="avg_4046_ebnhlz_1#11$1",focus=2)]
[name="黑键"]不，我们有这么多听众呢。
[character(name="avg_npc_482_1#3$1",name2="avg_4046_ebnhlz_1#11$1",focus=1)]
[name="白垩"]源石虫？
[character(name="avg_npc_482_1#3$1",name2="avg_4046_ebnhlz_1#11$1",focus=2)]
[name="黑键"]把那个老家伙留在尘世的旋律演奏给源石虫听，我觉得挺好，很人道。
[Dialog]
[Character(fadetime=0.7)]
[Delay(time=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="长笛和大提琴刚一出声，两人都察觉到了问题。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="两段旋律之间几乎没有任何共性。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="长笛声急迫、狂躁、刺耳，忽快忽慢，充斥着将眼前的一切拖入深渊的冲动。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="提琴声缓慢、忧郁、空洞，节奏一成不变，仿佛被天灾夷平后的大地，一无所有。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="但他们还是硬着头皮，将不成其为合奏的合奏继续下去。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="很快，源石虫如潮水一般奔涌而来。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="在漫天的臭气里，两个人生被尘世之音搅得乱七八糟的人在进行一场荒腔走板的合奏，他们的曲谱是脑子里不知道是否实存的旋律，听众则是源石虫。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="越是这么想，黑键越觉得，自己似乎摸到了尘世之音旋律的尾巴。", x=300, y=370, alignment="le

... (全文16745字符)
```

### level_act18side_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="28_g5_czernyhome",screenadapt="showall")]
[Delay(time=1)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=0.51)]
[Character(name="avg_4046_ebnhlz_1#3$2")]
[name="黑键"]不在？
[character(name="avg_npc_489_1#2$1")]
[name="乌尔苏拉"]先生已经出去好一会儿了。
[character(name="avg_1024_hbisc2_1#7$1")]
[name="芙蓉"]出去了？
[character(name="avg_npc_489_1#2$1")]
[name="乌尔苏拉"]应该是为了收治中毒的感染者的问题，要去和夕照区之外的医院交涉......
[Dialog]
[Character]
[playsound(key="$d_avg_doorknob")]
[Delay(time=1)]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_4047_pianst_1#1$1",fadetime=1.5)]
[delay(time=2.5)]
[character(name="avg_npc_489_1#1$1")]
[name="乌尔苏拉"]先生，怎么样，那些医院——
[character(name="avg_4047_pianst_1#2$1")]
[name="车尔尼"]勉强谈下来了两家最大的，合同已经签好，其他的......实在是不行了。
[character(name="avg_1024_hbisc2_1#5$1")]
[name="芙蓉"]可罗德岛和医院签过协议！
[character(name="avg_4047_pianst_1#1$1")]
[name="车尔尼"]你也在啊。
[character(name="avg_4047_pianst_1#2$1")]
[name="车尔尼"]没用的。罗德岛和那些医院的合同仅限矿石病本身引起的症状，他们有充足的理由不收治因中毒而倒下的感染者。
[character(name="avg_npc_489_1#2$1")]
[name="乌尔苏拉"]不管怎么说，先生好歹谈下了两家医院，应该足够了吧？
[character(name="avg_4047_pianst_1#7$1")]
[name="车尔尼"]哼，够了，当然够了！我用自己手里全部的版权做抵押，他们背后的财团当然觉得够了！
[character(name="avg_1024_hbisc2_1#3$1")]
[name="芙蓉"]难道您——把自己的版权转让给了那家财团？！
[character(name="avg_4047_pianst_1#7$1")]
[name="车尔尼"]是啊，不光以前的版权，连明天音乐会录音的发行权我都卖给他们了。
[character(name="avg_4047_pianst_1#5$1")]
[name="车尔尼"]现在我可以从零开始了......咳、咳。
[character(name="avg_4047_pianst_1#5$1")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="车尔尼"]咳......咳！
[Dialog]
[PlaySound(key="$bodyfalldown2", volume=1)]
[characteraction(name="middle", type="move", ypos=-50, fadetime=2,block=true)]
[character(fadetime=0.5)]
[delay(time=1.3)]
[character(name="avg_npc_489_1#3$1")]
[name="乌尔苏拉"]先生，先生？！
[Dialog]
[musicvolume(volume=0, fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character]
[delay(time=0.51)]
[musicvolume(volume=0.4, fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.51)]
[Character(name="avg_4047_pianst_1#5$1", name2="avg_1024_hbisc2_1#4$1",fadetime=1)]
[delay(time=1.5)]
[Character(name="avg_4047_pianst_1#5$1", name2="avg_1024_hbisc2_1#4$1",focus=2)]
[name="芙蓉"]您醒了？
[Character(name="avg_4047_pianst_1#5$1", name2="avg_1024_hbisc2_1#4$1",focus=1)]
[name="车尔尼"]唔......嗯。
[Character(name="avg_4047_pianst_1#5$1", name2="avg_1024_hbisc2_1#4$1",focus=2)]
[name="芙蓉"]车尔尼先生，您在出门的时候没做任何防护措施，对不对？
[Character(name="avg_4047_pianst_1#7$1", name2="avg_1024_hbisc2_1#4$1",focus=1)]
[name="车尔尼"]你说那些源石虫散发出来的臭气？合同能早一秒签下来都是好的，我出门时没考虑这些。
[Character(name="avg_4047_pianst_1#7$1", name2="avg_1024_hbisc2_1#4$1",focus=2)]
[name="芙蓉"]您绝对不能再像今天这样莽撞了。
[Character(name="avg_4047_pianst_1#1$1", name2="avg_1024_hbisc2_1#4$1",focus=1)]
[name="车尔尼"]“不能再”？也就是说，我还有一段时间好活？
[Character(name="avg_4047_pianst_1#1$1", name2="avg_1024_hbisc2_1#11$1",focus=2)]
[name="芙蓉"]......有我在呢。
[Character(name="avg_4047_pianst_1#2$1", name2="avg_1024_hbisc2_1#11$1",focus=1)]
[name="车尔尼"]唉，身体一垮下来，看医生也觉得顺眼多了。
[Character(name="avg_4047_pianst_1#8$1", name2="avg_1024_hbisc2_1#11$1",focus=1)]
[name="车尔尼"]谢谢你，芙蓉。
[Character(name="avg_4047_pianst_1#8$1", name2="avg_1024_hbisc2_1#1$1",focus=2)]
[name="芙蓉"]这是我应该做的。
[Character(name="avg_4047_pianst_1#1$1", name2="avg_1024_hbisc2_1#1$1",focus=1)]
[name="车尔尼"]倒是黑键，你怎么一句话都不说？难道是觉得现在夕照区太危险，想退出了？
[name="车尔尼"]我可告诉你，到了现在这一步，音乐会我无论如何也要办好，不要想临阵脱逃的事。
[character(name="avg_4046_ebnhlz_1#7$2")]
[name="黑键"]不要想临阵脱逃......
[name="黑键"]我......
[character(name="avg_4046_ebnhlz_1#6$2")]
[name="黑键"]（小声）他现在能受得了吗？
[character(name="avg_1024_hbisc2_1#4$1")]
[name="芙蓉"]（小声）稍等一等吧......
[character(name="avg_4047_pianst_1#1$1")]
[name="车尔尼"]看来不是要退出音乐会？
[character(name="avg_4046_ebnhlz_1#3$2")]
[name="黑键"]啊，不是要退出音乐会......
[character(name="avg_4047_pianst_1#2$1")]
[name="车尔尼"]黑键，你一紧张就喜欢重复别人的话，我从一开始就能看得出来。
[character(name="avg_4047_pianst_1#1$1")]
[name="车尔尼"]有什么话就说吧，我倒要看看，都现在这副样子了，还有什么事是我受不了的。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.51)]
[character(name="avg_4047_pianst_1#5$1",name2="avg_1024_hbisc2_1#4$1")]
[Delay(time=0.51)]
[character(name="avg_4047_pianst_1#5$1",name2="avg_1024_hbisc2_1#4$1",focus=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="车尔尼"]咳——咳咳咳！！
[character(name="avg_4047_pianst_1#5$1",name2="avg_1024_hbisc2_1#4$1",focus=2)]
[name="芙蓉"]车尔尼先生，水、水！
[Dialog]
[characteraction(name="right", type="move", xpos=-150,fadetime=0.7)]
[Delay(time=1)]
[PlaySound(key="$pourwater", volume=1)]
[delay(time=3)]
[characteraction(name="right", type="move", xpos=150,fadetime=1)]
[Delay(time=2)]
[character(name="avg_4047_pianst_1#3$1",name2="avg_1024_hbisc2_1#4$1",focus=1)]
[Delay(time=0.51)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_glass_break", volume=1)]
[Delay(time=1)]
[name="车尔尼"]咳、咳咳，格特鲁德这个——这个！
[character(name="avg_4047_pianst_1#3$1",name2="avg_1024_hbisc2_1#4$1",focus=1)]
[name="车尔尼"]还有你，你怎么想的，居然能同意这种计划？亏我还觉得你算是可造之才，你就想用音乐表达这种东西？一场阴谋？
[character(name="avg_4046_ebnhlz_1#6$2")]
[name="黑键"]我不是这个意思——
[character(name="avg_4047_pianst_1#3$1",name2="avg_1024_hbisc2_1#4$1",focus=1)]
[name="车尔尼"]怎么不是？你一开始不是老老实实答应那个疯女人了吗？
[character(name="avg_4046_ebnhlz_1#6$2")]
[name="黑键"]车尔尼，我记得你说过，就算是刻骨的憎恨，只要能用合适的技法表达出来，那也是纯粹的音乐。
[character(name="avg_4047_pianst_1#6$1",name2="avg_1024_hbisc2_1#4$1",focus=1)]
[name="车尔尼"]我是说过，然后呢？你想表达什么？
[character(name="avg_4046_ebnhlz_1#7$2")]
[name="黑键"]......说实话，现在我已经觉得自己当时的想法很可笑了。
[char

... (全文16570字符)
```

### level_act18side_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="28_g3_slumstreets_night",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$tense_intro", key="$tense_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[CameraShake(duration=1, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_magic_1")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.7, block=true)]
[Delay(time=0.71)]
[PlaySound(key="$d_avg_magic_2")]
[CameraShake(duration=1, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.7, block=true)]
[Delay(time=1)]
[playsound(key="$rungeneral")]
[character(name="avg_npc_484_1#8$1",fadetime=1)]
[delay(time=1.2)]
[name="格特鲁德"]给我躺下！
[Dialog]
[PlaySound(key="$d_avg_magic_4")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[CameraShake(duration=1, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_explo_n",volume=0.8)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.7, block=true)]
[delay(time=0.71)]
[playsound(key="$rungeneral")]
[character(name="avg_4046_ebnhlz_1#8$1",fadetime=1)]
[delay(time=1.2)]
[name="黑键"]别做梦了！
[Dialog]
[playsound(key="$d_avg_flute_attack")]
[delay(time=2.5)]
[PlaySound(key="$d_avg_magic_5")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[delay(time=0.51)]
[CameraShake(duration=1, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_explo_n")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.7, block=true)]
[delay(time=0.71)]
[character(name="avg_npc_484_1#8$1")]
[name="格特鲁德"]亏你还能腾出手来......
[dialog]
[PlaySound(key="$d_gen_explo_n")]
[CameraShake(duration=1, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=1,g=1, b=1, fadetime=2, block=true)]
[Character]
[Image(image="28_i06",screenadapt="coverall", fadetime=0)]
[Blocker(a=0, fadetime=1, block=true)]
[Delay(time=0.51)]
[name="黑键"]这次我来真的了，斯特罗洛女士！
[Dialog]
[PlaySound(key="$d_avg_magic_4")]
[CameraShake(duration=1, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=1,g=1, b=1, fadetime=0.05, block=true)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0.05, block=true)]
[Delay(time=0.51)]
[name="格特鲁德"]你——算计我？！
[name="黑键"]怎么，你也有力不从心的时候？
[name="格特鲁德"]还早呢，你也不过是仗着尘世之音......论法术的操控，你还早了——
[Dialog]
[PlaySound(key="$d_avg_magic_5")]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0.7,g=0.2, b=0.2, fadetime=0.05, block=true)]
[Blocker(a=0, fadetime=1, block=true)]
[ImageTween(xFrom=0, yFrom=0, xTo=-50, yTo=10, xScaleFrom=1, yScaleFrom=1, xScaleTo=1.1, yScaleTo=1.1, duration=0.1, block=true)]
[name="黑键"]喝啊！！
[Delay(time=1)]
[Dialog]
[PlaySound(key="$d_avg_magic_3")]
[ImageTween(xFrom=-50, yFrom=10, xTo=100, yTo=-10, xScaleFrom=1.1, yScaleFrom=1.1, xScaleTo=1.2, yScaleTo=1.2, duration=0.2, block=true)]
[Delay(time=0.51)]
[stopmusic(fadetime=2)]
[PlaySound(key="$d_gen_explo_n")]
[CameraShake(duration=1, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=1, block=true)]
[Image]
[Delay(time=0.51)]
[Background(image="28_g3_slumstreets_night",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlayMusic(intro="$escape_intro", key="$escape_loop", volume=0.4)]
[Delay(time=1)]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_4046_ebnhlz_1#8$1",fadetime=1.5)]
[delay(time=0.51)]
[name="黑键"]呼、呼、呼......
[name="黑键"]打、打倒了吗......
[Dialog]
[Character]
[Delay(time=0.51)]
[Character(name="avg_npc_484_1#6$1",fadetime=0.7)]
[palysound(name="d_avg_clothmovement",volume=1)]
[delay(time=1.5)]
[name="格特鲁德"]......呵，乌提卡伯爵，没想到，我居然输给了你。
[Character(name="avg_4046_ebnhlz_1#7$1")]
[name="黑键"]你也会认输？
[Character(name="avg_npc_484_1#6$1")]
[name="格特鲁德"]哼，输了就是输了，难道我不承认，就会变成我的胜利吗？
[Character(name="avg_4046_ebnhlz_1#1$1")]
[name="黑键"]你......为什么你还能这么从容不迫？
[Character(name="avg_npc_484_1#1$1")]
[name="格特鲁德"]因为......你们又能拿我怎么样呢？
[name="格特鲁德"]我是这座城市的领主，你们在深夜闯入了我管理的音乐厅，并且妄图拆除一些经过我批准的合法改造。
[name="格特鲁德"]甚至我想要阻止你们，还被你们打伤——
[name="格特鲁德"]乌提卡伯爵，罗德岛的人，还有你，车尔尼，该担心的，是你们才对，不是吗？
[Character(name="avg_4047_pianst_1#6$2")]
[name="车尔尼"]格特鲁德，你还是这么卑鄙。
[Character(name="avg_npc_484_1#

... (全文39847字符)
```

### level_act18side_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="28_g7_concerthall_outside",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=2)]
[Character(name="avg_npc_497_1#1$1")]
[name="满心期待的观众"]加油，我会在观众席上给你鼓劲的！
[Character(name="avg_npc_496_1#1$1")]
[name="惴惴不安的乐手"]可我......虽然一直练到今天，可还是有点没信心......
[name="惴惴不安的乐手"]还有那个预言，说是合奏，会不会就是我......
[Character(name="avg_npc_497_1#1$1")]
[name="满心期待的观众"]哎呀，别怕，别怕！昨晚受影响的人都得到了救治，今天也肯定没关系的！
[Character(name="avg_npc_493_1#1$1")]
[name="挑剔的评论家"]我还是第一次和这么多感染者同处一地，但愿这场音乐会值得我这么做。
[name="挑剔的评论家"]车尔尼先生来了吗？
[Character(name="avg_npc_492_1#1$1")]
[name="附庸风雅的贵族"]听组织者说，昨天晚上的源石虫骚动似乎也波及到了他，但他并未取消今天的出场预定。
[Character(name="avg_npc_493_1#1$1")]
[name="挑剔的评论家"]哼......也好。
[Character(name="avg_npc_496_1#1$1")]
[name="礼貌的感染者"]请大家先进场吧，车尔尼先生随后就到。
[Character(name="avg_npc_493_1#1$1")]
[name="挑剔的评论家"]你可没骗人吧？该不会等我们进了音乐厅，你们就把门一关，再宣布车尔尼先生不能来了——
[Character(name="avg_npc_496_1#1$1")]
[name="礼貌的感染者"]请您放心，这种情况绝不会发生。车尔尼先生只是偶感风寒，很快就会到达夕照厅......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="bg_ltroom",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$darkalley_intro", key="$darkalley_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[Character(name="avg_npc_486_1#7$1")]
[name="别格勒"]那个老家伙......我就说资料怎么可能会不翼而飞。
[name="别格勒"]对他的处置先延后。资料并不重要，重要的是对尘世之音的研究本身。
[Character(name="avg_npc_486_1#4$1")]
[name="别格勒"]——他要去音乐厅？
[name="别格勒"]算了......让他去吧。
[Dialog]
[PlaySound(key="$d_avg_telephone", volume=1)]
[delay(time=1)]
[Dialog]
[Character(name="avg_npc_486_1#4$1", name2="char_empty")]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="right", type="move", xpos=200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="right", type="move", xpos=-200, fadetime=1, block=false)]
[Character(name="avg_npc_486_1#4$1", name2="avg_npc_484_1#1$1",fadetime=0.7)]
[delay(time=1.5)]
[character(name="avg_npc_486_1#4$1",name2="avg_npc_484_1#7$1",focus=2)]
[name="格特鲁德"]看起来，密探的工作也不好做啊。
[character(name="avg_npc_486_1#1$1",name2="avg_npc_484_1#7$1",focus=1)]
[name="别格勒"]哼，比起担心我，还是先关心你自己吧，斯特罗洛伯爵。
[name="别格勒"]在自己的领地上包庇巫王残党，暗中支持尘世之音的研究，这可是重罪。
[character(name="avg_npc_486_1#1$1",name2="avg_npc_484_1#7$1",focus=2)]
[name="格特鲁德"]说起来，密探先生，我很好奇，在你们的记录中，我的父亲和哥哥是怎么死的？
[character(name="avg_npc_486_1#7$1",name2="avg_npc_484_1#7$1",focus=1)]
[name="别格勒"]别转移话题。
[character(name="avg_npc_486_1#7$1",name2="avg_npc_484_1#6$1",focus=2)]
[name="格特鲁德"]他们和这个话题紧密相关。
[character(name="avg_npc_486_1#1$1",name2="avg_npc_484_1#6$1",focus=1)]
[name="别格勒"]......
[character(name="avg_npc_486_1#2$1",name2="avg_npc_484_1#6$1",focus=1)]
[name="别格勒"]你的父亲，十五年前，为尘世之音的研究提供庇护，在被我们发现后，他想要供出背后的人，却在那之前被灭口。
[name="别格勒"]如果你知情，那你的嫌疑又加重了一层，斯特罗洛伯爵。
[character(name="avg_npc_486_1#2$1",name2="avg_npc_484_1#6$1",focus=2)]
[name="格特鲁德"]难道你觉得我在掩盖这件事吗？
[character(name="avg_npc_486_1#1$1",name2="avg_npc_484_1#6$1",focus=1)]
[name="别格勒"]......
[character(name="avg_npc_486_1#1$1",name2="avg_npc_484_1#12$1",focus=2)]
[name="格特鲁德"]我对父亲的看法也是随时间变化的。
[name="格特鲁德"]我小时候觉得，父亲是世界上最恐怖的人，他的意志是绝对的，谁也不能改变他的决定。
[name="格特鲁德"]喜欢乱跑乱跳，父亲就关我的禁闭；喜欢在吃饭时说话，父亲就撤掉我的晚饭，强迫我对着墙说上一个小时......
[name="格特鲁德"]后来，我年岁渐长，对父亲的敬畏有增无减。我亲眼见识了那些小贵族对斯特罗洛伯爵的谄媚，和伯爵大人对他们的不屑一顾。
[name="格特鲁德"]就连巫王的特使来到斯特罗洛的高塔里，也必须轻声细语，不像在地面上那样颐指气使......
[name="格特鲁德"]这就是斯特罗洛家，我们的领主，那位选帝侯，曾经最为器重的家族。
[character(name="avg_npc_486_1#1$1",name2="avg_npc_484_1#8$1",focus=2)]
[name="格特鲁德"]可这一切，都随着巫王的陨落而发生了改变。
[musicvolume(volume=0.2, fadetime=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Delay(time=1)]
[Background(image="28_g5_czernyhome",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[musicvolume(volume=0.4, fadetime=1)]
[character(name="avg_4047_pianst_1#4$1",name2="avg_1024_hbisc2_1#5$1",focus=2)]
[name="芙蓉"]事先声明，您现在的身体状况很不好。
[name="芙蓉"]作为医生，我应该阻止您前往音乐厅进行演奏。
[character(name="avg_4047_pianst_1#4$1",name2="avg_1024_hbisc2_1#5$1",focus=1)]
[name="车尔尼"]但你看起来不像是要阻止我的样子。
[character(name="avg_4047_pianst_1#4$1",name2="avg_1024_hbisc2_1#2$1",focus=2)]
[name="芙蓉"]......我不希望您燃烧生命创作的乐曲蒙尘。
[character(name="avg_4047_pianst_1#8$1",name2="avg_1024_hbisc2_1#2$1",focus=1)]
[name="车尔尼"]看来你也学会了一些变通。
[character(name="avg_4047_pianst_1#8$1",name2="avg_1024_hbisc2_1#7$1",focus=2)]
[name="芙蓉"]我只是明白了，有的时候，目标也有轻重缓急之分。
[musicvolume(volume=0.2, fadetime=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Delay(time=1)]
[Background(image="bg_ltroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[musicvolume(volume=0.4, fadetime=1)]
[character(name="avg_npc_486_1#1$1",name2="avg_npc_484_1#6$1",focus=2)]
[name="格特鲁德"]我时常觉得可笑，我的父亲竟然蠢到真心拥护巫王的统治。
[name="格特鲁德"]他惊人的愚蠢甚至让他拒绝掩饰自己的想法。
[name="格特鲁德"]斯特罗洛家在他的带领下，迅速失去了选帝侯的支持。
[name="格特鲁德"]我们家也失去了两座移动城市的领地，被迫来到了这座临近巫王的故乡乌提卡，毫无亮点可言的维谢海姆。
[character(name="avg_npc_486_1#1$1",name2="avg_npc_484_1#7$1",focus=2)]
[name="格特鲁德"]治理维谢海姆的斯特罗洛伯爵，是不是有种愚蠢的错位感？
[character(name="avg_npc_486_1#4$1",name2="avg_npc_484_1#7$1",focus=1)]
[name="别格勒"]所以，你的父亲因此心存不满，开始和巫王残党接触。
[character(name="avg_npc_486_1#4$1",name2="avg_npc_484_1#7$1",focus=2)]
[name="格特鲁德"]哈，这是我当时的想法，而你显然不像当时的我一样天真，密探先生。
[name="格特鲁德"]你们密探应该比我更清楚，老斯特罗洛从一开始就和巫王的残党有接触，不是吗？
[character(name="avg_npc_486_1#4$1",name2="avg_npc_484_1#4$1",focus=2)]
[name="格特鲁德"]对了，密探先生，你刚才还没有回答我，在你们眼里，我哥哥是怎么死的？
[character(name="avg_npc_486_1#1$1",name2="avg_npc_484_1#4$1",focus=1)]
[name="别格勒"]你的哥哥死于食物中毒，这是官方口径，也是我们的最终结论。
[character(name="avg_npc_486_1#1$1",name2="avg_npc_484_1#7$1",focus=2)]
[name="格特鲁德"]食物中毒，啊哈。
[character(name="av

... (全文50172字符)
```

### level_act18side_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[Background(image="28_g8_concerthall_outside_n",screenadapt="showall")]
[Delay(time=1)]
[PlayMusic(intro="$white_01_intro", key="$white_01_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Character(name="avg_npc_495_1#5$1")]
[name="爷爷"]傻孩子，真是个傻孩子......
[name="爷爷"]你明明可以不用做这样的事的。
[name="爷爷"]这片大地欠你这么多，你又何必做到这一步？
[Character(name="avg_1024_hbisc2_1#3$1")]
[name="芙蓉"]老先生？！
[Character(name="avg_1024_hbisc2_1#6$1")]
[name="芙蓉"]请您赶快离开！这里的源石活性正在不断上升！
[Character(name="avg_npc_495_1#5$1")]
[name="爷爷"]我还想见我孙子最后一面呢。
[Character(name="avg_4046_ebnhlz_1#8$2")]
[name="黑键"]就差最后一下了，芙蓉，拜托你牵制他的注意力——
[Character(name="avg_npc_495_1#5$1")]
[name="爷爷"]白垩，爷爷在这儿。
[Character(name="avg_4046_ebnhlz_1#4$2")]
[name="黑键"]您？！
[Character(name="avg_npc_495_1#5$1")]
[name="爷爷"]白垩，我亲爱的孩子。
[name="爷爷"]如果你觉得有怨气，就冲我来吧。
[name="爷爷"]在你毁掉更多东西之前，先冲我来吧！
[Character(name="avg_npc_495_1#2$1")]
[name="爷爷"]我骗了你许多年，瞒了你许多年......我想过因你而死，却没想过你会遭遇这样的结局！
[name="爷爷"]既然你选择让其他人活下去，那就让时日无多的我随你而去，又有何妨？
[Character(name="avg_npc_495_1#5$1")]
[name="爷爷"]让我再陪你一程吧，我亲爱的孩子！
[Dialog]
[Character]
[delay(time=0.51)]
源石结晶组成的怪物不能理解老人的话。
刚刚那瞬间的清醒已经是奇迹中的奇迹，此时的怪物只想随着大提琴声，将四周拖入永久的虚无。
于是，怪物循着声音传来的方向，全力喷吐死亡的旋律。
[Dialog]
[PlaySound(key="$d_avg_magic_1")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[delay(time=0.51)]
[CameraShake(duration=1, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_explo_n",volume=0.6)]
[CameraShake(duration=1, xstrength=20,ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[Delay(time=0.51)]
[Character(name="avg_4046_ebnhlz_1#4$2")]
[name="黑键"]老先生？！
[Dialog]
[Character(name="avg_1024_hbisc2_1#11$1",fadetime=0.5)]
[Delay(time=0.51)]
[PlaySound(key="$bodyfalldown1")]
[CameraShake(duration=1, xstrength=20,ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=1.5)]
[Character(name="avg_1024_hbisc2_1#11$1",name2="avg_npc_495_1#5$1",focus=2)]
[name="爷爷"]小姑娘，你何必——
[Character(name="avg_1024_hbisc2_1#6$1",name2="avg_npc_495_1#5$1",focus=1)]
[name="芙蓉"]——黑键，这里由我挡住，趁现在！
[Character(name="avg_4046_ebnhlz_1#8$2")]
[name="黑键"]喝啊啊啊啊啊啊！！！
[Dialog]
[stopmusic(fadetime=3)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=3, block=true)]
[Character]
[Delay(time=0.51)]
[Background(image="bg_black",screenadapt="showall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.51)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.51)]
[Background(image="bg_ltroom",screenadapt="showall")]
[playMusic(intro="$darkness02_intro", key="$darkness02_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[Character(name="avg_npc_484_1#4$1")]
[name="格特鲁德"]怎么可能？！
[name="格特鲁德"]友情、牺牲、奉献——如此幼稚的信念，就应该在现实中摔得粉身碎骨，凭什么，凭什么？！
[Character(name="avg_npc_484_1#8$1")]
[name="格特鲁德"]不，还没有结束！
[name="格特鲁德"]白垩确实把两段尘世之音强行纳入了自己这一侧，可他最终还是敌不过它们叠加在一起的无序和疯狂！
[name="格特鲁德"]我听得见，白垩的旋律已经消散殆尽，但黑键的尘世之音并未离去，我还——
[Dialog]
[PlaySound(key="$d_avg_knife")]
[CameraShake(duration=0.5, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0.7, g=0.2, b=0.2, fadetime=0.05, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Delay(time=0.51)]
[Character(name="avg_npc_484_1#3$1")]
[name="格特鲁德"]唔呃！
[Dialog]
[PlaySound(key="$bodyfalldown2", volume=1)]
[characteraction(name="middle", type="move", ypos=-50, fadetime=2,block=true)]
[character(fadetime=0.5)]
[delay(time=2)]
[Character(name="avg_npc_486_1#1$1")]
[name="别格勒"]够了，斯特罗洛伯爵。
[Dialog]
[Character]
[Delay(time=0.51)]
格特鲁德刚刚搭上琴弦的手无力地垂下。
别格勒把匕首从格特鲁德的后背抽出，血染脏了他的衣服。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.51)]
[Background(image="bg_black",screenadapt="showall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.51)]
[playsound(key="$d_avg_crystal_shatter")]
源石外壳层层崩解。
广场上失去了声音，只有失去活性的源石外壳落在地上的沉闷响动。
最后，外壳尽数剥落，留在原地的，是奄奄一息的白垩，还有他身边的大提琴。
[Dialog]
[stopmusic(fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Delay(time=0.51)]
[Background(image="28_g8_concerthall_outside_n",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$storyendjp_intro", key="$storyendjp_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[Character(name="avg_4046_ebnhlz_1#8$2")]
[name="黑键"]等着我......等着我！！
[Character(name="avg_1024_hbisc2_1#6$1")]
[name="芙蓉"]等等！他现在很危险，我们该做的是呼叫感染者临终事务处......
[Character(name="avg_4046_ebnhlz_1#8$2")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="黑键"]你说什么？！
[name="黑键"]......白垩不会死的！
[Dialog]
[playsound(key="$rungeneral")]
[character(fadetime=1.5)]
[delay(time=2.5)] 
[Character(name="avg_4046_ebnhlz_1#8$2",name2="avg_npc_483_1#1$1",focus=2)] 
[name="白垩"]咳......
[Character(name="avg_4046_ebnhlz_1#4$2",name2="avg_npc_483_1#1$1",focus=1)] 
[name="黑键"]白垩，你醒了？！
[name="黑键"]看到了吗，白垩有救的！
[Character(name="avg_1024_hbisc2_1#4$1")]
[name="芙蓉"]......
[Character(name="avg_4046_ebnhlz_1#4$2",name2="avg_npc_483_1#1$1",focus=2)] 
[name="白垩"]黑键......？
[Character(name="avg_4046_ebnhlz_1#4$2",name2="avg_npc_483_1#1$1",focus=1)] 
[name="黑键"]我在这里，我在这里！
[Character(name="avg_4046_ebnhlz_1#4$2",name2="avg_npc_483_1#1$1",focus=2)] 
[name="白垩"]别......白费力气了，我......
[Character(name=

... (全文15683字符)
```

### level_act18side_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[PlaySound(key="$d_avg_animal_loop",volume=0.4, channel="HB", loop=true)]
[Delay(time=2)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=3, block=true)]
[soundvolume(channel="HB",volume=0.8,fadetime=2)]
[Subtitle(text="“天空湛蓝晴朗，\n微风轻声歌唱；\n河水潺潺流淌，\n我的心充满希望。\n阴霾一夕散尽，\n大地迎接晨光；\n赞美莱塔尼亚，\n自由之人的故乡。”\n——《晴空之歌》（1078）", x=290, y=210, alignment="center", size=24, delay=0.04, width=700)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopsound(channel="HB", fadetime=3)]
[Delay(time=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Subtitle]
[Background(image="28_g2_slumstreets",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=2)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[Character(name="avg_1024_hbisc2_1#1$1",fadetime=1)]
[delay(time=1)]
[name="芙蓉"]（按照地图，这里已经离罗德岛办事处不远了。）
[name="芙蓉"]（进入维谢海姆时耽搁了一会儿，不过快走几步，应该还能在预定时间到达办事处......）
[Dialog]
[Character(name="char_empty", name2="avg_1024_hbisc2_1#1$1")]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="left", type="move", xpos=-200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="left", type="move", xpos=200, fadetime=1, block=false)]
[Character(name="avg_npc_498_1#1$1", name2="avg_1024_hbisc2_1#1$1",fadetime=0.7)]
[delay(time=1.5)]
[Character(name="avg_npc_498_1#1$1", name2="avg_1024_hbisc2_1#1$1",focus=1)]
[name="热情的感染者"]请留步！
[Character(name="avg_npc_498_1#1$1", name2="avg_1024_hbisc2_1#3$1",focus=2)]
[name="芙蓉"]呃......我？
[Character(name="avg_npc_498_1#1$1", name2="avg_1024_hbisc2_1#3$1",focus=1)]
[name="热情的感染者"]对，就是你，美丽的女士！我没见过你，请问你是第一次到夕照区来吗？
[Character(name="avg_npc_498_1#1$1", name2="avg_1024_hbisc2_1#1$1",focus=2)]
[name="芙蓉"]是的，我是罗德岛的干员，来夕照区调查感染者异常好转现象——
[Character(name="avg_npc_498_1#1$1", name2="avg_1024_hbisc2_1#1$1",focus=1)]
[name="热情的感染者"]暂时忘掉那些身份和任务吧，我在此诚挚地邀请你与我合奏一曲！
[Character(name="avg_npc_498_1#1$1", name2="avg_1024_hbisc2_1#3$1",focus=2)]
[name="芙蓉"]合奏？
[Character(name="avg_npc_498_1#1$1", name2="avg_1024_hbisc2_1#4$1",focus=2)]
[name="芙蓉"]可我这把长笛是买来当法杖用的，我一首曲子也不会吹......
[Character(name="avg_npc_498_1#1$1", name2="avg_1024_hbisc2_1#4$1",focus=1)]
[name="热情的感染者"]没关系！只要你能吹响它，我就有信心将这几个音变成一首乐曲，并把它赠送给你，女士，纪念这美好的一天！
[Character(name="avg_npc_498_1#1$1", name2="avg_1024_hbisc2_1#4$1",focus=2)]
[name="芙蓉"]我和别人约了时间，现在已经快迟到了。
[Character(name="avg_npc_498_1#1$1", name2="avg_1024_hbisc2_1#4$1",focus=1)]
[name="热情的感染者"]别担心，别担心。这么美好的天气，无论是谁，都会允许一些小小的延迟的。
[Character(name="avg_npc_498_1#1$1", name2="avg_1024_hbisc2_1#4$1",focus=1)]
[name="热情的感染者"]来吧，不会花很长时间的！
[Character(name="avg_npc_498_1#1$1", name2="avg_1024_hbisc2_1#7$1",focus=2)]
[name="芙蓉"]那我......随便吹几个音？
[Character(name="avg_npc_498_1#1$1", name2="avg_1024_hbisc2_1#7$1",focus=1)]
[name="热情的感染者"]请！
[dialog]
[PlaySound(key="$d_avg_flute", volume=1)]
[delay(time=5)]
[Character(name="avg_npc_498_1#1$1", name2="avg_1024_hbisc2_1#8$1",focus=2)]
[name="芙蓉"]（还好还好，吹响了......）
[Character(name="avg_npc_498_1#1$1", name2="avg_1024_hbisc2_1#8$1",focus=1)]
[name="热情的感染者"]哆......发......啦......嗦......发......咪......
[Character(name="avg_npc_498_1#1$1", name2="avg_1024_hbisc2_1#8$1",focus=1)]
[name="热情的感染者"]很好，一个充满希望的动机！
[Character(name="avg_npc_498_1#1$1", name2="avg_1024_hbisc2_1#8$1",focus=1)]
[name="热情的感染者"]艾玛，我来奏乐，请你和我们的客人共舞一曲如何？
[Character(name="avg_npc_498_1#1$1", name2="avg_1024_hbisc2_1#3$1",focus=2)]
[name="芙蓉"]共舞？
[Dialog]
[character(fadetime=0.3)]
[delay(time=0.51)]
[Character(name="avg_1024_hbisc2_1#3$1", name2="char_empty")]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="right", type="move", xpos=200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="right", type="move", xpos=-200, fadetime=1, block=false)]
[Character(name="avg_1024_hbisc2_1#3$1", name2="avg_npc_497_1#1$1",fadetime=0.7)]
[delay(time=2)]
[Character(name="avg_1024_hbisc2_1#3$1", name2="avg_npc_497_1#1$1",focus=2)]
[name="开朗的感染者"]来吧，美丽的小姐，让我们跳起来！
[Character(name="avg_1024_hbisc2_1#7$1", name2="avg_npc_497_1#1$1",focus=1)]
[name="芙蓉"]可是我真的没时间，我的舞跳得也——
[dialog]
[Character(name="avg_1024_hbisc2_1#7$1", name2="avg_npc_497_1#1$1")]
[characteraction(name="right", type="move", xpos=-200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[Characteraction(name="right", type="jump",  power=20, times=1, fadetime=0.5, block=true)]
[name="开朗的感染者"]别担心，大家都有跳得不好的时候，没人会笑话你的。
[Character(name="avg_npc_498_1#1$1")]
[name="热情的感染者"]好的，我会用三拍子......
[name="热情的感染者"]一二三一二三，预备——起！
[musicvolume(volume=0.2, fadetime=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[musicvolume(volume=0.4, fadetime=1)]
[Character(name="avg_1024_hbisc2_1#1$1", name2="avg_npc_497_1#1$1",fadetime=0.7)]
[PlaySound(key="$d_avg_cheer_street", volume=0.3)]
[delay(time=0.7)]
[PlaySound(key="$livecrowd",volume=0.4)]
[characteraction(name="left", type="move", ypos=-50, fadetime=0.4,block=false)]
[characteraction(name="right", type="move", ypos=-50, fadetime=0.4,block=true)]
[delay(time=0.7)]
[characteraction(name="left", type="move", ypos=50, fadetime=0.5,block=false)]
[characteraction(name="right", type="move", ypos=50, fadetime=0.5,block=true)]
[delay(time=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Character(name="avg_1024_hbisc2_1#4$1")]
[delay(time=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[name="芙蓉"]对不起，我踩了你好多下......
[Character(name="avg_npc_497_1#1$1")]
[name="开朗的感染者"]没关系，和你共舞很愉快！感谢你的配合！
[Character(name="avg_npc_498_1#1$1")]
[name="热情的感染者"]再见！

... (全文32740字符)
```

### level_act18side_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_ltstrongpoint",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Character(name="avg_npc_492_1#1$1")]
[name="畏首畏尾的贵族"]和陛下有血脉联系的人......就只剩这些了？
[Character(name="avg_npc_491_1#1$1")]
[name="肆无忌惮的术师"]那两个女人下手太快太狠，这已经是极限了。
[Character(name="avg_npc_492_1#1$1")]
[name="畏首畏尾的贵族"]我还是觉得，陛下留下的旋律不应该这么随随便便地——
[Character(name="avg_npc_491_1#1$1")]
[name="肆无忌惮的术师"]那你想怎么办？
[Character(name="avg_npc_492_1#1$1")]
[name="畏首畏尾的贵族"]我觉得我们还是应该稳重一点......
[Character(name="avg_npc_491_1#1$1")]
[name="肆无忌惮的术师"]稳重？我们的人每天都在被杀，你还敢说稳重？这是最后的机会了！
[Character(name="avg_npc_491_1#1$1")]
[name="肆无忌惮的术师"]陛下的血脉与陛下的旋律结合，就算不能复现陛下全部的力量，至少......
[dialog]
[character(fadetime=1)]
[delay(time=1.2)]
我......到底几岁？两岁？三岁？
我正站在一片破败的建筑中间，茫然地环顾四周。
带我来的人告诉我，我的父亲和母亲已经死于私刑，而那时的我还无法理解什么是私刑，什么是死。
他还说，从今以后，这里就是我的家，我将成为伟大计划的一部分，运气好的话，我会成为莱塔尼亚的下一任统治者。
不懂。完全听不懂。
我只能懵懵懂懂地意识到，我的那个房间，每天上午会有阳光直射进来的房间，似乎回不去了。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[Character(name="avg_npc_492_1#1$1")]
[name="畏首畏尾的贵族"]我已经说过了，把人当成尘世之音的容器，这种事情不可能成功的......
[Character(name="avg_npc_491_1#1$1")]
[name="肆无忌惮的术师"]你早知道不可能？计划实行之前你明确表示反对了吗？现在倒好，人死了，你倒跳出来说风凉话了？晚了！
[Character(name="avg_npc_492_1#1$1")]
[name="畏首畏尾的贵族"]不是，我......
[Character(name="avg_npc_491_1#1$1")]
[name="肆无忌惮的术师"]我告诉你，这不是浪费，这是为了成功必须付出的代价。
[Character(name="avg_npc_491_1#1$1")]
[name="肆无忌惮的术师"]只要他们之中能有一个活下来，我们就没必要像做贼一样躲在这种穷乡僻壤了！
[Character(name="avg_npc_491_1#1$1")]
[name="肆无忌惮的术师"]维多利亚、乌萨斯、卡西米尔......对我们的计划感兴趣的人有的是！只要能成功，我们就能借来他们的军队，向那两个女人复仇！
[dialog]
[character(fadetime=1)]
[delay(time=1.2)]
那天，到这儿之后一直照顾着我们的大姐姐不见了。
大姐姐不见后，那些会给我们送饭，但和我们不住在一起的人吵了起来。
我还是听不懂他们在吵什么，只知道，那个会给我们哼歌的大姐姐，好像不会回来了。
那首歌好像是这么唱的：
天空湛蓝晴朗，
微风轻声歌唱；
河水潺潺流淌，
我的心充满希望。
歌曲似乎还有后半段，但大姐姐从来没有唱过。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[Character(name="avg_npc_491_1#1$1")]
[name="肆无忌惮的术师"]这次怎么样，我问你，这次怎么样？
[Character(name="avg_npc_492_1#1$1")]
[name="畏首畏尾的贵族"]可人还是死了......
[Character(name="avg_npc_491_1#1$1")]
[name="肆无忌惮的术师"]死了又怎么样？我们已经在进步了！
[Character(name="avg_npc_491_1#1$1")]
[name="肆无忌惮的术师"]下次我们把手术室搬到更远的地方，用阻隔声音的材料装修一下......会成功的！
[dialog]
[character(fadetime=1)]
[delay(time=1.2)]
天气冷了又暖。
一开始的时候，每当有人消失，那些人就会大吵特吵。
后来，他们渐渐不吵了，但我们的餐食越来越差，好在吃饭的人也越来越少，所以还能填饱肚子。
大概人就是这样的东西，一不小心就消失不见了。
他们的东西也一样。
某个老奶奶的拐杖，某个大哥哥的音乐盒，某个叔叔爱不释手的法杖和源石骰子......
但有些东西会留下来，比如那位大姐姐爱唱的歌。
有个孩子学会了那首歌，他常把那首歌挂在嘴边。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[Character(name="avg_npc_492_1#1$1")]
[name="畏首畏尾的贵族"]我们——我们究竟在做什么？！
[Character(name="avg_npc_492_1#1$1")]
[name="畏首畏尾的贵族"]陛下的血脉被我们保护下来，最后却......死在我们手上......
[Character(name="avg_npc_491_1#1$1")]
[name="肆无忌惮的术师"]清醒一点，这是必要的代价！为了让陛下的血脉掌握相应的力量，这是必须付出的牺牲！
[Character(name="avg_npc_491_1#1$1")]
[name="肆无忌惮的术师"]我们对尘世之音的了解已经越来越多了，很快就能成功的！
[Character(name="avg_npc_492_1#1$1")]
[name="畏首畏尾的贵族"]可那些死去的人......
[Character(name="avg_npc_492_1#1$1")]
[name="畏首畏尾的贵族"]不，我们别再搞这种疯狂的实验了......我们隐姓埋名，教育剩下的这几个，没准他们也能像陛下一样......
[Character(name="avg_npc_491_1#1$1")]
[name="肆无忌惮的术师"]别做梦了，尘世之音是必需的！
[dialog]
[character(fadetime=1)]
[delay(time=1.2)]
后来，又过了一年，或者两年，我不知道。
只剩下我和那个孩子。
每当那些人到房间里来的时候，我都吓得全身发抖。
这时，那个孩子就会安慰我，告诉我没事，然后主动站到那些人面前。
等他们走后，他就会给我唱起那首歌。
“我的心充满希望。”
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[Character(name="avg_npc_491_1#1$1")]
[name="肆无忌惮的术师"]你们在这儿待了这么久，就算是孩子，也该知道是怎么回事了。
[Character(name="avg_npc_491_1#1$1")]
[name="肆无忌惮的术师"]你们毕竟是陛下仅存的血脉，我也不想搞得太难看。下一个轮到谁，你们俩自己决定吧。
[Character(name="avg_npc_492_1#1$1")]
[name="畏首畏尾的贵族"]这次我们的技术有了很大的改进......也许会成功......也说不定。所以，没准这次接受实验的那个人，会......成为很厉害很厉害的术师哦。
[dialog]
[character(fadetime=1)]
[delay(time=1.2)]
我们两个谁都不傻。
那个贵族装束的人前几次也这么说，可离开房间的那些人谁也没回来。
我双腿发抖，偷偷看了看旁边的孩子，他的嘴唇也变得煞白。
我不想消失，我也不想让他消失，但是......
他注意到我的眼神，扭过头来，颤抖着对我抬起嘴角。
“我来吧。”
听见他开口，我再也支撑不住，两腿一软，跪倒在地。
[musicvolume(volume=0.2, fadetime=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Delay(time=1)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[musicvolume(volume=0.4, fadetime=1)]
我一个人在空荡荡的房间里住了两个月。
然后，一个下雨的晚上，那个孩子被抬了过来，双目紧闭，咬着嘴唇，但他活着。
我以为奇迹真的发生了，可几天之后，他又从房间里被抬走，从此像其他人一样消失不见。
临走之前，他还在哼那首歌。
“我的心充满希望。”
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Delay(time=1)]
[Background(image="bg_ltstrongpoint",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
又过了几天，终于轮到我了。
我一路跟着那两个人走，一路看到好多以前从未见到过的房间，里面是各种各样的装置和仪器。
我们走到一间小小的房间里，里面的一切都是白的。
那个穿高塔术师衣服的人让我躺在床上。她戴上了白色的口罩和手套，看起来很怪异。
她把一个面罩扣在我的脸上，然后我就什么都不知道了。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Delay(time=1)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
我是在那些人的欢呼声中醒来的。
我刚一醒来，立刻就觉得自己的脑袋里面有岩浆正在沸腾，几乎要把我的眼睛烤熟。
剧痛持续了......多长时间？几天？几个星期？几个月？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Delay(time=1)]
[Background(image="bg_ltstrongpoint",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0

... (全文8700字符)
```

### level_act18side_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_hotel",screenadapt="showall")]
[Delay(time=1)]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=2)]
[name="？？？"]这就是全部了？
[name="沉稳的贵族"]绝无一丝隐瞒。
[name="？？？"]这种处理方式......倒也有些出乎意料。
[name="沉稳的贵族"]现在该怎么办？
[name="？？？"]怎么办？不怎么办。
[name="？？？"]这件事本来就和你无关，现在不过是改了改对涉事领地的处置，能和你扯上任何关系吗？
[name="沉稳的贵族"]您说得是。可这样一来，那些感染者得以继续在那个地块上生活，难保他们不乱说......
[name="？？？"]那又如何？谁会相信一群感染者的胡言乱语？
[name="沉稳的贵族"]那我们接下来......
[name="？？？"]接下来？
[name="？？？"]不必着急，该做的事情还有很多。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[stopmusic(fadetime=3)]
[Character]
[delay(time=1)]
[Background(image="bg_ltroom",screenadapt="showall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[name="恭谨的侍从"]......以上就是这次事件的最终报告。
[Character(name="avg_npc_487_1#1$1")]
[name="女性"]辛苦你了。
[name="女性"]那个叫车尔尼的，他在这次事件中作的那首曲子，你们找来了吗？
[Character(name="avg_npc_487_1#1$1",focus=-1)]
[name="恭谨的侍从"]女皇之声随时可以采谱，几小时后就能为您演奏。
[Character(name="avg_npc_487_1#1$1")]
[name="女性"]不必，我听录音就好。
[dialog]
[playMusic(intro="$leithanien_intro", key="$leithanien_loop", volume=0.4)]
[Character(name="avg_npc_487_1#2$1")]
[delay(time=2)]
[name="女性"]......
[Character(name="avg_npc_487_1#1$1")]
[name="女性"]不错，我甚至能听见他作曲时发自心底的吼声。
[Character(name="avg_npc_487_1#9$1")]
[name="女性"]这人很有些才华，可惜，还不太够。
[musicvolume(volume=0.2, fadetime=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Delay(time=1)]
[Background(image="28_g2_slumstreets",screenadapt="showall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[musicvolume(volume=0.4, fadetime=1)]
[Character(name="avg_npc_496_1#1$1",name2="avg_npc_498_1#1$1",fadetime=0.7)]
[delay(time=1)]
[Character(name="avg_npc_496_1#1$1",name2="avg_npc_498_1#1$1",focus=1)]
[name="紧张的感染者"]结果怎么样？
[Character(name="avg_npc_496_1#1$1",name2="avg_npc_498_1#1$1",focus=2)]
[name="颓废的感染者"]还行，没加重。
[name="颓废的感染者"]行板说，那次事件导致的感染加重很奇特，许多人的感染在那之后都进入了持续的稳定期，我也不例外。
[Character(name="avg_npc_496_1#1$1",name2="avg_npc_498_1#1$1",focus=1)]
[name="紧张的感染者"]不会是像之前那样先好后坏吧？
[Character(name="avg_npc_496_1#1$1",name2="avg_npc_498_1#1$1",focus=2)]
[name="颓废的感染者"]按行板的说法，他们彻底调查了这一现象，发现在事件中活性化的源石，几乎全部进入了持续的低活性状态。
[name="颓废的感染者"]换句话说，我还能晃悠一阵子。
[Character(name="avg_npc_496_1#1$1",name2="avg_npc_498_1#1$1",focus=1)]
[name="紧张的感染者"]太好了......
[name="紧张的感染者"]对了，行板知道公爵大人打算拿夕照区怎么办吗？
[Character(name="avg_npc_496_1#1$1",name2="avg_npc_498_1#1$1",focus=2)]
[name="颓废的感染者"]她也是听说的，说是女皇之声要求公爵大人不能动夕照区。
[Character(name="avg_npc_496_1#1$1",name2="avg_npc_498_1#1$1",focus=1)]
[name="紧张的感染者"]谢天谢地！感谢女皇陛下的仁慈——
[Character(name="avg_npc_496_1#1$1",name2="avg_npc_498_1#1$1",focus=2)]
[name="颓废的感染者"]小点声！
[Character(name="avg_npc_496_1#1$1",name2="avg_npc_498_1#1$1",focus=1)]
[name="紧张的感染者"]......
[name="紧张的感染者"]唉，这以后的日子该怎么过啊......
[Character(name="avg_npc_496_1#1$1",name2="avg_npc_498_1#1$1",focus=2)]
[name="颓废的感染者"]闭嘴吧，你还嫌事情不够大是不是？
[name="颓废的感染者"]以后的日子？过一天算一天罢了。
[Character(name="avg_npc_496_1#1$1",name2="avg_npc_498_1#1$1",focus=1)]
[name="紧张的感染者"]可我还想多活两天呢。
[Character(name="avg_npc_496_1#1$1",name2="avg_npc_498_1#1$1",focus=2)]
[name="颓废的感染者"]那你就更该把嘴闭严实了。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Delay(time=1)]	
[Background(image="28_g4_embassy",screenadapt="showall")]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[Character(name="avg_npc_501_1#1$1",focus=1)]
[name="行板"]......
[name="行板"]芙蓉，我现在算是理解了，有些事还是不知道比较轻松。
[name="行板"]等处理完这里的后续工作，我还是申请调动到其他地方好了。
[name="行板"]或者去本舰上看看，应该也不错......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Background(image="28_g12_sewer",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]	
[character(name="avg_npc_486_1#1$1",name2="avg_npc_495_1#6$1",focus=1)]
[name="别格勒"]站住。
[name="别格勒"]为了找你，我们也费了不少功夫。
[character(name="avg_npc_486_1#1$1",name2="avg_npc_495_1#6$1",focus=2)]
[name="爷爷"]......
[character(name="avg_npc_486_1#1$1",name2="avg_npc_495_1#6$1",focus=1)]
[name="别格勒"]有什么想说的吗？
[character(name="avg_npc_486_1#1$1",name2="avg_npc_495_1#6$1",focus=2)]
[name="爷爷"]......是你的人骗白垩来维谢海姆的吧。
[character(name="avg_npc_486_1#1$1",name2="avg_npc_495_1#6$1",focus=1)]
[name="别格勒"]......
[character(name="avg_npc_486_1#1$1",name2="avg_npc_495_1#6$1",focus=2)]
[name="爷爷"]除了音乐会的报酬之外，告诉他的全是真话，就为了把急着赚钱给我治病的他引到这个局里来......
[name="爷爷"]可是他和你无冤无仇，你为什么这么做？！
[character(name="avg_npc_486_1#2$1",name2="avg_npc_495_1#6$1",focus=1)]
[name="别格勒"]要是听了内情，我就不能放你走了。
[character(name="avg_npc_486_1#2$1",name2="avg_npc_495_1#6$1",focus=2)]
[name="爷爷"]我本来也没几天好活。
[character(name="avg_npc_486_1#1$1",name2="avg_npc_495_1#6$1",focus=1)]
[name="别格勒"]行吧，看在我们俩共事过的分上，我告诉你。
[name="别格勒"]斯特罗洛伯爵已经在找白垩了，而且快找到了。
[character(name="avg_npc_486_1#1$1",name2="avg_npc_495_1#3$1",focus=2)]
[name="爷爷"]那又怎样？白垩一直在我身边，也就等于一直在你的掌控之下！
[character(name="avg_npc_486_1#1$1",name2="avg_npc_495_1#3$1",focus=1)]
[name="别格勒"]你看到过她的研究笔记，你应该知道，她对尘世之音的研究确实很令人惊讶。
[name="别格勒"]在没拿到那些笔记之前，我只知道她对这东西研究很深，却不知道深到了什么程度。
[character(name="avg_npc_486_1#2$1",name2="avg_npc_495_1#3$1",focus=1)]
[name="别格勒"]我害怕的是，如果让她接着研究下去，她没准能用尘世之音干出些更恐怖的事来，比如在更远的距离引发和诱导共振。
[character(name="avg_npc_486_1#3$1",name2="avg_npc_495_1#3$1",focus=1)]
[name="别格勒"]一觉醒来，身边的好孙子变成了怪物，这就是你想要的？
[character(name="avg_npc_486_1#1$1",name2="avg_npc_495_1#3$1",focus=1)]
[name="别格勒"]与其这样，还不如直接把白垩塞到她鼻子底下，让她觉得时不我待，在技术尚有瑕疵的时候推进计划。
[name="别格勒"]怎么样，还有疑问吗？
[character(name="avg_npc_486_1#1$1",name2="avg_npc_495_1#6$1",focus=2)]
[name="

... (全文19279字符)
```

### training_act18side_01_a

```
[HEADER(is_skippable=true, is_autoable=false)] 活动18side教学关1_a

[PopupDialog(dialogHead="$avatar_ardign")] 这些敌人不仅打人有点痛，还会额外造成法术伤害......
[PopupDialog(dialogHead="$avatar_ardign")] 这里的废能干扰也很严重！它在拖慢我的动作，让我没法治疗自己！
[Tutorial(focusX=-270, focusY=270, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_melan", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
战场上的能量重整装置，<@tu.kw>“低音号”</>，能够利用废能形成“<@tu.kw>重整束流</>”。站在<@tu.kw>重整束流</>上，就可以免受干扰，还能反制敌人的特殊能力。
[PopupDialog(dialogHead="$avatar_ardign")] 欸？可<@tu.kw>重整束流</>并不经过我这里啊。
[PopupDialog(dialogHead="$avatar_adnach")] 只要将干员部署在<@tu.kw>重整束流</>上，就可以引导它的流向，让它往部署的方向延伸。
[PopupDialog(dialogHead="$avatar_adnach")] 卡缇，你再坚持一下，我马上就把<@tu.kw>重整束流</>导向你的位置！

```

### training_act18side_01_b

```
[HEADER(is_skippable=true, is_autoable=false)] 活动18side教学关1_b

[PopupDialog(dialogHead="$avatar_stward")] 我们来支援了！前方似乎有强力敌人正在接近，大家最好都站到重整束流上面。
[Tutorial(focusX=-100, focusY=20, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_melan", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
这里的<@tu.kw>“回音壁”</>可以反射重整束流，我们也可以用它来改变重整束流的流向。
[PopupDialog(dialogHead="$avatar_adnach")] 利用好<@tu.kw>重整束流</>，消灭这些敌人吧。

```

### training_act18side_02_a

```
[HEADER(is_skippable=true, is_autoable=false)] 活动18side教学关2_a

[PopupDialog(dialogHead="$avatar_ardign")] 奇怪，重整束流似乎被前面的什么东西挡住了。
[PopupDialog(dialogHead="$avatar_amgoat")] 没关系的，那是重整束流在为“<@tu.kw>谐振器</>”充能。
[Tutorial(focusX=-100, focusY=-90, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amgoat")] \
只要将<@tu.kw>谐振器</>与重整束流连通一段时间，就能将谐振器激活。
[PopupDialog(dialogHead="$avatar_amgoat")] 将干员部署在<@tu.kw>激活的谐振器</>上，就可以获得一个新的重整束流起点，不必再和“低音号”连通了。
[PopupDialog(dialogHead="$avatar_ardign")] 了解！
```

### training_act18side_02_b

```
[HEADER(is_skippable=true, is_autoable=false)] 活动18side教学关2_b
[Tutorial(focusX=-100, focusY=-90, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_melan")] \
第一个<@tu.kw>谐振器</>已经激活！让我们再接再厉，把废能干扰的影响降到最低吧。
```


## 统计

- 总字符数：412865
- 对话行数：3283


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
