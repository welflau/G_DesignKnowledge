# 明日方舟 · 活动剧情 · act10d5（7段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act10d5」完整剧情脚本（7个文件，2445行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act10d5
- 脚本文件数：7

### level_act10d5_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 古米 习惯
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
古米是宿舍里第二个醒来的人，她有个习惯。
一旦被真理叫醒，她就会握握真理的手，然后用同样的方法到隔壁去叫醒凛冬。
至于凛冬握不握她的手，纯看“冬将军”醒来时的心情。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_room_2",screenadapt="coverall")]
[Blocker(a=0.4, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
6:30 a.m.
罗德岛宿舍区  真理与古米的宿舍
[Dialog]
[Character]
[delay(time=2)]
[name="古米"]  呼......呼......
[name="古米"]  （早上到了。）
[name="古米"]  （唔，真理姐应该快来了。）
[name="古米"]  呼......呼......
[name="古米"]  （真理姐今天好慢啊，是最近太累了吗？）
[name="古米"]  （但再等下去的话早上勤务就要迟到了，别再等真理姐了，快起来吧古米。）
[name="古米"]  呼......呼......
[name="古米"]  （你做得到的，古米，加油！）
[name="古米"]  呼......唔唔，嗯。
[Character]
[Dialog]
[Character(name="char_196_sunbr_1#5",fadetime=1,block=true)]
[delay(time=2)]
[name="古米"]  我起来了！
[Character(name="char_196_sunbr_1#7")]
[name="古米"]  好黑啊。
[name="古米"]  小夜灯怎么关了？
[name="古米"]  真理姐？真理姐！
[name="古米"]  奇怪，是出门了吗？
[name="古米"]  过去看看吧。
[name="古米"]  ......
[name="古米"]  不在呢。
[name="古米"]  可能是真的急着出门吧。
[name="古米"]  发生什么了？
[name="古米"]  啊。
[name="古米"]  这是......
[name="古米"]  “古米，今天有事出门，晚上才回来，自己照顾好自己。”
[name="古米"]  “真理——”
[name="古米"]  “——和凛冬。”
[Character(name="char_196_sunbr_1#4")]
[name="古米"]  哼，又把我当小孩子看待，我当然能照顾好自己啦！
[name="古米"]  原来凛冬姐也起床了。
[name="古米"]  嗯......
[Character(name="char_196_sunbr_1#2")]
[name="古米"]  啊，时候不早了，得赶紧去报到。
[name="古米"]  平底锅要带好，还有硬梆梆的盾牌......
[name="古米"]  好，准备完毕。
[name="古米"]  出发！！
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_canteen",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
11:28 a.m.
罗德岛食堂   料理区
[Dialog]
[delay(time=1)]
咕——
[Character(name="char_196_sunbr_1#2",fadetime=1,block=true)]
[delay(time=1)]
[name="古米"]  有点饿了啊......
[name="古米"]  早上走得太急，没来得及填饱肚子。
[name="古米"]  还是先专心干活吧，干完就能吃饭了。
[name="古米"]  嗯——
[Character(name="char_196_sunbr_1#5")]
[name="古米"]  这锅菜好了，请放到取餐区去！
[Character(name="char_260_durnar_1")]
[PlaySound(key="$rungeneral", volume=0.9)]
[name="坚雷"]  来了！
[Character(name="char_196_sunbr_1#2")]
[name="古米"]  下一锅是上汤浇菜吗，好，加油！
[name="古米"]  ......
[Character]
[Dialog]
[delay(time=1)]
[Character(name="char_196_sunbr_1#2")]
[name="古米"]  好了！
[name="古米"]  这锅菜好了，请放到取餐区去!
[name="古米"]  下一锅是......唔，还有一份油炸肉饺。
[name="古米"]  那等人来把菜放去取餐区去，回来继续烧个菜，早上的活就算干完啦。
[Character]
[name="坚雷"]  古米，我忙不过来了！你能自己把菜送过去吗！
[Character(name="char_196_sunbr_1#5")]
[name="古米"]  没问题！！
[name="古米"]  嘿咻。
[name="古米"]  还好，没盾牌重。
[Character(name="char_196_sunbr_1#7")]
[name="古米"]  是送到哪里呢？
[name="古米"]  坚雷教官！
[name="古米"]  ......
[name="古米"]  坚雷教官？
[name="古米"]  奇怪。
[name="古米"]  今天大家怎么动作都这么快？一回头人就不见了。
[Character(name="char_196_sunbr_1#5")]
[name="古米"]  算了，我直接问取餐区的人好了。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_canteen",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_196_sunbr_1#5")]
[name="古米"]  应该就是这里了吧，今天负责收银的是——远山姐姐吗？
[name="古米"]  远山姐姐，您好。
[Dialog]
[Character]
[Character(name="char_109_fmout_1",fadetime=1,block=true)]
[delay(time=1)]
[name="远山"]  中午好，小熊。
[name="远山"]  你怎么拿着锅子就出来了，要我搭把手吗？
[Character(name="char_196_sunbr_1#2")]
[name="古米"]  不用了姐姐，您告诉古米应该把菜放到哪里就好，再这样悬着，菜都要凉啦！
[Character(name="char_2013_cerber_1")]
[name="刻俄柏"]  ......
[Character(name="char_109_fmout_1")]
[name="远山"]  这是上汤浇菜吧，如果我没记错，应该是中间，讯使站着的地方。
[Character(name="char_196_sunbr_1#2")]
[name="古米"]  好叻。
[Character(name="char_109_fmout_1")]
[name="远山"]  真的不用帮把手吗，小熊？
[Character(name="char_196_sunbr_1#5")]
[name="古米"]  不用不用，再见远山姐姐。
[Character(name="char_109_fmout_1")]
[name="远山"]  ......
[Character(name="char_284_spot_1")]
[name="斑点"]  别看了，拿不动的。
[Character(name="char_109_fmout_1")]
[name="远山"]  我知道。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_canteen",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_198_blackd_1")]
[name="讯使"]  欢迎，今天想来点什么？
[name="讯使"]  野菜扣肉，好的，清炒时蔬再加个炖蛋，没问题。
[name="讯使"]  来，请您拿好。
[name="讯使"]  小心烫。
[name="讯使"]  嗯，再见~
[Character(name="char_196_sunbr_1#2")]
[name="古米"]  讯使哥哥，菜来了。
[Character(name="char_198_blackd_1")]
[name="讯使"]  哦好，谢谢你古米。
[Character(name="char_196_sunbr_1#5")]
[name="古米"]  不客气~
[Character(name="char_198_blackd_1")]
[name="讯使"]  嘿！
[name="讯使"]  喝！好，完工。
[name="讯使"]  不好意思古米，能麻烦你把锅带回去吗。
[Character(name="char_196_sunbr_1#2")]
[name="古米"]  好的讯使哥哥。
[Dialog]
[Character(name="char_196_sunbr_1#2")]
咕噜————
[delay(time=1)]
[Character(name="char_196_sunbr_1#2")]
[name="古米"]  唔唔......
[Character(name="char_198_blackd_1")]
[name="讯使"]  真是辛苦你了，来，哥哥这里有块饼干，拿去垫垫肚子吧。
[Character(name="char_196_sunbr_1#5")]
[name="古米"]  谢谢讯使哥哥！
[Character(name="char_198_blackd_1")]
[name="讯使"]  不客气，记得忙完了以后好好吃饭哦。
[Character(name="char_196_sunbr_1#5")]
[name="古米"]  好的！
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_canteen",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_196_sunbr_1#2")]
[name="古米"]  再见远山姐姐，我回去干活了。
[Character(name="char_109_fmout_1")]
[name="远山"]  路上当心。
[Character(name="char_196_sunbr_1#2")]
[name="古米"]  好的！
[Dialog]
咕噜噜————
[delay(time=1)]
[Character(name="char_196_sunbr_1#7")]
[name="古米"]  （马上就能吃饭了，再忍一小会。）
[Character(name="char_2013_cerber_1")]
[name="刻俄柏"]  好吃的我来啦！
[Character(name="char_2013_cerber_1",name2="char_196_sunbr_1#3",focus=2)]
[name="古米"]  呜啊啊小刻你不能进去！！
[Character(name="char_2013_cerber_1",name2="char_196_sunbr_1#3",focus=1)]
[name="刻俄柏"]  不行吗？
[Character(name="char_2013_cerber_1",name2="char_196_sunbr_1#3",focus=2)]
[nam

... (全文31216字符)
```

### level_act10d5_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 真理 被选择的
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_room_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$dignified_intro", key="$dignified_loop", crossfade=3,volume=0.4)]
[Character(name="char_195_glassb_2",fadetime=1,block=true)]
[delay(time=1)]
[name="真理"]  ......
[name="真理"]  电源，接上了，没问题。
[name="真理"]  在录了吗？啊——啊——
[name="真理"]  嗯，好像没问题了。
[name="真理"]  ......
[name="真理"]  ......
[name="真理"]  该说点什么好呢。
[Dialog]
[Character(name="char_195_glassb_2#6")]
[delay(time=1)]
[name="真理"]  唔嗯。
[name="真理"]  现在我使用的这台器械，是可露希尔小姐租借给我的，用途是......嗯，申请书上写的用途是“真实情境暴露式创伤记录自我诊疗”。
[name="真理"]  ......好长。
[name="真理"]  总之，机械的操作很方便，只要确认电量充足，然后打开开关......像这样，就会自动开始录像了。嗯。
[name="真理"]  呼.......
[name="真理"]  （好难，自说自话好难。）
[name="真理"]  （只是自己对着屏幕说话，本来还以为会比较简单呢......）
[name="真理"]  在我提出想要尝试去缓和与克制自己的症状时，医疗部的干员向我提出了这样的建议——
[Character(name="char_195_glassb_2")]
[name="真理"]  “要不要试试看自我倾诉”......这样的建议。
[name="真理"]  啊，虽然现在是开着录像，但这些并不是会给别人看的东西。不如说，我绝不想给任何人看到！
[name="真理"]  放轻松，真理，放轻松。嗯嗯，只是随便说点什么，不要紧张，给自己听，想说什么都行。
[name="真理"]  ......那些现在还没有办法说给别人听的事，可以一遍一遍说给自己听。
[name="真理"]  我觉得，这是一个可行的想法。
[name="真理"]  关于之前的一些事情......
[name="真理"]  就算现在大家看起来都还没什么问题，但是我知道，我们有很多东西要解决，只是迟早的事。
[name="真理"]  我知道，古米也好早露也好，都没能忘记之前的那些事，在学校里发生的那些，彻底离开学校之后发生的那些，不会有人忘得掉。
[name="真理"]  凛冬她......凛冬她最近好像总是在做噩梦，烈夏看起来很放得下，但是真的......可以放得下吗？
[name="真理"]  我呢？我又是怎么样呢，我认为我可以面对，但是，我真的......可以吗？
[name="真理"]  大家都闭口不谈，可是，不论如何，最后总归还是要面对。
[Dialog]
[Character(name="char_195_glassb_2")]
[delay(time=1)]
[name="真理"]  ......
[name="真理"]  ......真难啊。
[name="真理"]  呼......好吧，我觉得我好像逐渐有一点习惯这样自言自语了。
[name="真理"]  正式开始吧。
[name="真理"]  首先，或许应该从自我介绍开始？
[name="真理"]  （深呼吸）
[name="真理"]  我叫做“真理”——当然，这只是个代号，本名是安娜·莫罗佐娃。
[name="真理"]  唔嗯，总觉得有很久没有提过这个名字了，明明是自己的名字，却有点陌生，真奇怪。
[Dialog]
[showitem(image="item_act10_1")]
[delay(time=1)]
[hideitem(fadetime=1)]
[Delay(time=1)]
[Character(name="char_195_glassb_2")]   
[name="真理"]  这位是薇卡，是我的好朋友。
[name="真理"]  薇卡她，是我在加入学生自治团前，最好的朋友。
[Character(name="char_195_glassb_2")]
[name="真理"]  现在，我居住于罗德岛这个组织的本营内，隶属于“乌萨斯学生自治团”。
[name="真理"]  呃，学生自治团，虽然是我的提议，但真正组建它的人是凛冬。以及，虽说是一个独立的团体，目前成员也不过只有五个人而已。
[name="真理"]  凛冬，娜塔莉娅，烈夏，古米，还有我。
[name="真理"]  之前其实还有更多的成员，不过现在只剩下我们。
[name="真理"]  啊，当然，薇卡她也是我们之中的一员。
[name="真理"]  目前我们都作为罗德岛的“干员”......应该算是在工作？
[name="真理"]  我觉得这样不坏。劳有所得，这很公平。
[name="真理"]  凛冬暂时不打算离开这里，虽然她不说，但我知道她也不讨厌这样。有时我也会想，或许我们就这样一直走下去也不错。
[Character(name="char_195_glassb_2")]
[name="真理"]  ......呼。
[name="真理"]  其实，虽然现在大家聚在一起，但我们五个人并不是同一所学校的学生。
[name="真理"]  我和古米，还有娜塔莉娅，是同一所高中的学生，而凛冬还有烈夏属于另一所学校。
[name="真理"]  啊，虽然不是同校，但是凛冬从过去起就一直很出名，市内相邻的几所学校，没有学生不认识她。
[name="真理"]  ......我认为她是那种天生就适合成为领袖的类型。实际上，她也的确理所应当一样做着我们的领头人。
[name="真理"]  在我们都毫无防备的时候，整合运动进攻、并占领了我们的城市切尔诺伯格。
[name="真理"]  发生了一些......事情，整合运动占领城区时，我所在的学校中的一部分学生，被强行押送到了凛冬她们所在的校园。
[name="真理"]  或许还有其他学校的学生也被聚集到了一起，我不清楚，那时候所有的一切都很混乱。
[name="真理"]  我并不清楚他们这样做的用意，为首的那个整合运动头目，是个白头发的少年。
[name="真理"]  看起来没有多大年纪，他是不是还没有我们大？我不知道。
[name="真理"]  他似乎用一套什么理由说服了在场的其他头目，将许多学生带走，我们都被关在了凛冬他们的学校内。
[Character(name="char_195_glassb_2#6")]
[name="真理"]  现在回想起来，真是太荒唐了。
[name="真理"]  在那之后，是长达十数天的封锁，以及......
[Dialog]
[Character]
[Background]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[cameraEffect(effect="Grayscale", keep=true, amount=1, fadetime=0)]
[Background(image="bg_cher_0",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_cher_5",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_school",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_schoolyard",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[name="？？？"]  安娜！
[name="？？？"]  呼，太好了，幸好来的人是你。
[name="？？？"]  拉我一把，安娜。
[name="？？？"]  ......安娜？
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[cameraEffect(effect="Grayscale", keep=true, amount=0, fadetime=0)]
[Background(image="bg_room_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_195_glassb_2#7",fadetime=1,block=true)]
[delay(time=1)]
[name="真理"]  ......以及争斗。
[name="真理"]  被封锁在校园内的争斗，还有彻底脱离校园后，在整个切尔诺伯格城区中的争斗。
[name="真理"]  我们每个人，都有一些不得不去面对的东西。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
[name="真理"]  我们——
[Dialog]
[stopmusic(fadetime=3)]
[PlaySound(key="$doorknockquite")]
[delay(time=1)]
[Character(name="char_195_glassb_2#3")]
[name="真理"]  （这个时间，应该不是古米，那会是谁......）
[name="真理"]  请稍等。
[name="真理"]  （这个录像，关闭之前的保存操作有点麻烦，就这么放着应该也没问题吧。）
[name="真理"]  请问是哪位？
[Character]
[name="？？？"]  是我啦是我！
[Character(name="char_195_glassb_2")]
[name="真理"]  ......哪位？
[Character]
[name="？？？"]  哈啊？预备探员真理小姐！你是不是在装傻，我的声音你怎么可能听不出来啦！
[Character(name="char_195_glassb_2#5")]
[name="真理"]  唔嗯，好吵。
[name="真理"]  以及，之前也说过了，我并不是什么预备探员。
[Character]
[name="？？？"]  呵呵，你们的关系真好呢。
[name="？？？"]  下午好，安娜，我也一起来叨扰了。
[Character(name="char_195_glassb_2#3")]
[name="真理"]  ......欸？
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[name="真理"]  娜塔莉娅？
[Dialog]
[PlaySound(key="$dooropenquite")]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fa

... (全文32494字符)
```

### level_act10d5_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 凛冬 无尽的梦
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_indoor_u",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.4)]
清晨，我像往常一样走出自己的房间。
[name="母亲"]  索尼娅，洗漱都完成了吗？
[name="索尼娅"]  妈妈，我已经不是小孩子了。
[Character(fadetime=1)]
[Dialog]
厨房里传来妈妈的声音，她正在厨房忙碌，接下来，我只要坐在餐桌前等一会儿，就能吃到热腾腾的早餐。
早餐通常会是一碗粥配上面包和火腿，妈妈最近似乎想要减肥，所以早餐的粥都是据说最不会长肉的燕麦粥。
我无所谓。
爸爸一如既往地坐在一边看报纸，报纸上总是写些无聊的东西，经济，政治，国家，我一点也不喜欢。
为什么它们不能刊登一些我的丰功伟绩？
[name="父亲"]  索尼娅，最近在学校怎么样？
又来了。
每天只有在这个时候和晚饭时才会出现的象征性关心，他真的不会感到厌烦吗？还是说他其实也不在乎？
[name="索尼娅"]  ......一般。 
[name="父亲"]  你已经是个七年级的学生了，别再像以前那样撒野了。
[Character]
[Dialog]
为什么？我还只是七年级。
[name="父亲"]  还有，你已经决定好九年级毕业后的发展了吗？
[name="索尼娅"]  ......没有。
[Character]
[Dialog]
九年级毕业后，我就要决定是继续学习，还是去技术学校学一门手艺。
我知道爸爸希望我去技术学校，而且他接下来肯定会这么说。
[name="父亲"]  那你应该.......
[name="母亲"]  别对着女儿摆你的架子，你的工作呢？
妈妈端着早餐走出厨房，一边打断了爸爸的话。
[name="父亲"]  ......我今天会有一个面试。
自从失业后，爸爸在妈妈面前总是抬不起头来，当然，其实以前也没有好到哪里去。
[name="母亲"]  皮埃尔，你应该学会放下你那点可怜的架子，尊严不能当饭吃。
[name="父亲"]  我知道，我在尝试了，安娜。
妈妈其实比爸爸更关心我的学业，并且希望我在毕业后能够继续学习，她甚至已经在为此存钱的样子。
她总是说，在她的年代，可没有免费读完九年级这样的好事。
然后每当她提到这个话题，她总会说起自己幸运的经历——作为一名贵族的女仆。
在一所女子学校完成了学业——这让她能在如今并不景气的市场中总是能够找到一份不错的工作。
有的时候，我也会希望自己能够成为她口中的好孩子，可惜我不是。
[name="母亲"]  但愿你真的知道了。好了，索尼娅，快点吃早饭，不然你要赶不上校车了。
[name="索尼娅"]  我知道，妈妈。
[Character]
[Dialog]
我低头准备吃我的早饭，但我却看到了奇怪的东西——少得可怜的粥，半块面包，奇形怪状的火腿。
[name="索尼娅"]  ......妈妈，这些是什么？
[name="母亲"]  你在说什么，索尼娅，这不是我们每天在吃的东西吗？
[name="索尼娅"]  我们怎么可能每天在吃这些东西？！
[stopmusic(fadetime=1)]
[Character(name="char_115_headbr_9#11")]
[name="索尼娅？"]  你忘了吗？
[Character]
[Dialog]
一个和我一模一样的人忽然出现在餐桌边。
[dialog]
[Character(name="char_115_headbr_9#5",fadetime=1,block=true)]
[delay(time=1)]
[name="索尼娅"]  你是谁，为什么长得和我一样？
[Character(name="char_115_headbr_9#5",name2="char_115_headbr_9#11",focus=2)]
[name="索尼娅？"]  我是你。
[Character]
[Dialog]
她是我？真可笑，那我是谁？
[Character(name="char_115_headbr_9#10")]
[name="索尼娅？"]  你是索尼娅。
[Character]
[Dialog]
莫名其妙。
但是真奇怪，明明又多出一个和我长得一样的人，爸爸和妈妈却没有任何反应。
[name="父亲"]  索尼娅，你在发呆干什么，快点吃饭。
噢，我知道了，这一定是一个噩梦，这样就解释得通了，哈，只是一些食物而已，我在梦里面对过更加可怕的东西。
[Character(name="char_115_headbr_9#10")]
[name="索尼娅？"]  不，那些可怕的东西只是你从漫画和游戏中获得的妄想。
[name="索尼娅？"]  你过去确实以为世上最可怕的东西就是拥有无匹力量的东西。
[name="索尼娅？"]  钢铁洪流，巨大的怪兽，父亲的巴掌，简单粗暴。
[Character]
[Dialog]
她在说什么？为什么她会知道？
[Character(name="char_115_headbr_9#6")]
[name="索尼娅"]  就算是又怎么样？你也是我的梦，不然你怎么会知道我在想什么？
[Character(name="char_115_headbr_9#6",name2="char_115_headbr_9#11",focus=2)]
[name="索尼娅？"]  仔细看看你手里的食物。
[Character(name="char_115_headbr_9#6",name2="char_115_headbr_9#11",focus=1)]
[name="索尼娅"]  你在说......？！
[Character]
[Dialog]
这根本不是粥，只是一些米和水外加杂草的混合物，和妈妈做的粥差远了！
面包......确实是面包，但它散发着难闻的味道，好像已经在没有好好保存的情况下放了好几天的样子。
......我为什么会知道它被放了好几天？
火腿像是从一块巨大的肉上强行撕扯下来的一样，而且......带着一丝腥味，等等，这是......血迹？！
[Character(name="char_115_headbr_9#4")]
[name="索尼娅"]  ......呕。
[name="索尼娅"]  这只是一个噩梦！
[Character(name="char_115_headbr_9#4",name2="char_115_headbr_9#11",focus=2)]
[name="索尼娅？"]  但你从未做过这样的梦，而且这些东西的细节是如此真实，就好像......
[Character]
[Dialog]
我感觉另一个我似乎想要嘲笑我，但老师说，嘲笑是通过伤害别人来让自己获得快乐的行为。
她看起来并不快乐。
无论如何，我有一种预感，我不能让她说下去。
就算吃的糟糕点，这样的生活不好吗？
我一定要让她闭嘴，我等会儿还要去上学呢！
[Character(name="char_115_headbr_9#6")]
[name="索尼娅"]  闭嘴！
[Character]
[Dialog]
很显然，我知道该用什么方法让人闭嘴，对，就是用我的拳头！
[Character(name="char_115_headbr_9#11")]
[name="索尼娅？"]  就好像，你真的吃过一样。
[stopmusic(fadetime=1)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
我握起拳头向她冲去，但我还是晚了一步。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_school",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$darkness02_intro", key="$darkness02_loop", volume=0.4)]
我的拳头狠狠砸在面前的人的脸上。
骨头与对方的脸接触产生的触感令人安心。
[name="学生A"]  咕啊！！
[name="学生B"]  太、太强了，原本以为十几个人一定可以解决她的，居然被她一个人给全灭......
[Character(name="char_115_headbr_9")]
[name="索尼娅"]  *乌萨斯粗口*，就你们这样的软脚虾也想欺压别人，再回去练练吧。
[Character]
[name="学生C"]  啧，走，冬将军，你给我等着，这事没完！
[Character]
[Dialog]
老实说，冬将军这个绰号我还挺喜欢的。
嗯，很酷。
不过，这些人老是在我午睡的时候来找我麻烦，她们难道不知道我下午的课一般也不会去上吗？
[name="受欺凌的学生"]  那个，谢谢你，冬将军。
[Character(name="char_115_headbr_9")]
[name="索尼娅"]  嗯？你还在啊，不是让你跑了吗？
[Character]
[name="受欺凌的学生"]  因为这次我想感谢你。
[Character]
[Dialog]
这次？
[name="受欺凌的学生"]  那个，果然你已经不认识我了吗？我叫瓦莱里娅，之前你也救过我。
[Dialog]
噢，这么说来，这个女孩儿头上绑的黄色蝴蝶结我好像有印象。
是上周，还是上个月来着？反正我帮过她吧，大概。
[name="受欺凌的学生"]  还有你之前也帮过我的朋友，我们都很崇拜你。
[Dialog]
看到她脸上喜悦的表情，我也跟着有些高兴起来，不过，样子还是要做的。
[Character(name="char_115_headbr_9")]
[name="索尼娅"]  我只是看不惯这些人仗着自己人多有力气就欺负别人而已。
[name="索尼娅"]  你也应该鼓起勇气，如果你有勇气，他们其实反而会被你吓跑。
[Character]
[name="受欺凌的学生"]  嗯......你说得对，我会试一试的。
[Character(name="char_115_headbr_9")]
[name="索尼娅"]  好了，你该走了。
[Character]
[name="受欺凌的学生"]  嗯，再次感谢你！
[Dialog]
那个女孩说着跑了出去。
[Character(name="char_115_headbr_9")]
[name="索尼娅"]  嗯？
[Dialog]
[Character]
教室里的桌椅和黑板好像变得脏乱了许多，是我的错觉吗，还是这间教室本来就是这样？
算了，管他的，我要睡午觉。
我将四张椅子拼在一起，躺了上去。
[Character(name="char_115_headbr_9")]
[name="索尼娅"]  什么东西？
[Dialog]
[Character]
我的背后好像压到了一个比较小的东西。
我伸手拿起来一看，发现是一个黄色的蝴蝶结。
这个蝴蝶结感觉有些眼熟，上面很脏，而且断了一边。
[Character(name="char_115_headbr_9#5")]
[name="索尼娅"]  嗯？！
[Dialog]
[Character]
蝴蝶结的背面，有浓浓的深黑色，就好像......
血迹。
[Character(name="char_115_headbr_9")]
[name="索尼娅"]  ......一定是番茄酱吧。
[Dialog]
[Character]
我把蝴蝶结丢到一边，决定继续午睡。
在我陷入沉睡之前，我好像听到自己的声音。
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_115_headbr_9#11",fadetime=1,block=true)]
[delay(time=1)]
[name="索尼娅？"]  后来，你在学校的某个教室里发现了这个蝴蝶结。
[name="索尼娅？"]  其实你知道，她已经死了。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_school",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
教室的门忽然被推开，打断了我的午睡。
一个拿着书本，戴着眼镜的女孩儿站在那里，看校服应该不是这所学校的。
[Character(name="char_195_glassb_2")]
[name="？？？"]  请问，这间教室里还有别人吗？
[Character(name="char_195_glassb_2",name2="char_

... (全文26336字符)
```

### level_act10d5_st04

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 早露 赎罪？
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_canteen",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$relax_intro", key="$relax_loop", volume=0.4)]
[name="近卫干员"]  这稍微有些生涩的口感，这好像放多了盐的味道，啊，回家的感觉！
[name="后勤干员"]  不就是出了一次长任务，你至于吗？
[name="近卫干员"]  哎，你是不知道，乌萨斯的食物我实在是吃不惯。
[name="近卫干员"]  还是罗德岛的食堂好，全是我喜欢吃的东西。
[name="后勤干员"]  从你刚才的感慨来看，我可听不出这是你喜欢吃的东西......
[name="近卫干员"]  好吃和喜欢吃又不一样。
[name="近卫干员"]  那我还被一些找到亲戚的难民请去吃了大餐呢，啧啧，那叫一个精致典雅高贵。
[name="近卫干员"]  但我还是觉得不习惯。
[name="后勤干员"]  行吧，以后你就叫被罗德岛食堂驯服的男人了。
[name="后勤干员"]  所以这次任务怎么样？
[name="近卫干员"]  很简单啊，你又不是不知道，把我们从切尔诺伯格救出来的难民送去其他的乌萨斯城市。就是跑跑腿，只是比较花时间而已。
[name="后勤干员"]  当我没问，你这家伙，听到能帮难民就最上心了。
[name="近卫干员"]  是啊，虽然时间和人数都不允许我们做很多事，但救一个是一个吧。
[name="近卫干员"]  我也听杜宾说了我们现在的处境不好和乌萨斯有什么接触，所以阿米娅和博士愿意做这样的救援我就已经很高兴了。
[name="后勤干员"]  嗯，我们这边也为有这样的领袖高兴。
[name="后勤干员"]  不过，这件事上，除了阿米娅和博士，还要特别感谢一个人呢。
[name="近卫干员"]  噢，我知道我知道，路上的时候听其他人说了，好像是一个叫娜塔莉娅的女孩是吧。
[name="后勤干员"]  嗯，她可是我们这里的大明星呢。
[Character]
[name="？？？"]  哎呀，我好像听到有人在谈论我的样子？
[name="后勤干员"]  啊，娜塔莉娅，中午好。
[Dialog]
[Character(name="char_197_poca_1",fadetime=1,block=true)]
[PlaySound(key="$d_gen_walk_n")]
[delay(time=1)]
[name="娜塔莉娅"]  塞伦先生，午安。还有这位是......
[Character(name="char_013_riop")]
[name="近卫干员"]  我代号叫圆规，叫我圆规就好。
[Character(name="char_197_poca_1")]
[name="娜塔莉娅"]  圆规......是个好代号呢，午安。不介意的话，我能坐在这里吃饭吗？
[Character(name="avg_npc_012")]
[name="干员塞伦"]  当然可以！
[Character(name="char_013_riop",name2="avg_npc_012",focus=1)]
[name="圆规"]  喂，我听说只是个学生......
[name="圆规"]  这不是一眼就看得出是个超级大小姐吗！
[Character(name="char_013_riop",name2="avg_npc_012",focus=2)]
[name="干员塞伦"]  又不冲突！
[Character(name="char_013_riop",name2="avg_npc_012",focus=1)]
[name="圆规"]  我完全不知道该怎么跟这样的人说话啊！
[Character(name="char_013_riop",name2="avg_npc_012",focus=2)]
[name="干员塞伦"]  别紧张，娜塔莉娅很好说话的。
[Character(name="char_197_poca_1")]
[name="娜塔莉娅"]  说起来，听两位刚才说的话，圆规先生是刚刚完成护送难民的任务回来吗？
[Character(name="char_013_riop",name2="char_197_poca_1",focus=1)]
[name="圆规"]  对，我们刚才还在聊这个呢。
[Character(name="char_013_riop",name2="avg_npc_012",focus=2)]
[name="干员塞伦"]  对对，我正打算跟他说娜塔莉娅你在这件事里起的作用呢。
[Character(name="char_197_poca_1",name2="avg_npc_012",focus=1)]
[name="娜塔莉娅"]  我只是做了一些微不足道的工作而已。
[Character(name="char_197_poca_1",name2="avg_npc_012",focus=2)]
[name="干员塞伦"]  你太谦虚了，如果不是娜塔莉娅你主动去游说那些难民，我们的工作绝对不会进展得这么顺利。
[Character(name="char_013_riop",name2="avg_npc_012",focus=1)]
[name="圆规"]  我在路上也听难民们说过，说是有一个特别好心和善良的小姐告诉他们罗德岛都是好人。
[name="圆规"]  哎，听塞伦这么说，我也得好好感谢你了，娜塔莉娅小姐。
[name="圆规"]  老实说，一些难民对我们的态度也好不到哪里去，没有你的话，我完全可以想象路上会有多少不愉快。
[name="圆规"]  虽然我自己也是难民出身，完全可以理解他们，但我也不想做好事还遭白眼啊。
[Character(name="char_013_riop",name2="char_197_poca_1",focus=2)]
[name="娜塔莉娅"]  这些都是我应该做的，真正辛苦的是圆规先生你们护送的人。
[name="娜塔莉娅"]  大家不是不相信罗德岛，只是他们刚刚蒙受了灾难，对谁都没有办法很好信任。
[name="娜塔莉娅"]  我也只是感觉到罗德岛确实是为大家好，而且我以前作为学生会长最常做的就是这样的事，这些都是我擅长的。
[Character(name="char_013_riop",name2="char_197_poca_1",focus=1)]
[name="圆规"]  啧啧，塞伦，你听听，这才叫人话，听了让人舒坦。
[Character(name="char_013_riop",name2="avg_npc_012",focus=2)]
[name="干员塞伦"]  我刚才就跟你说了，娜塔莉娅很好说话的好吧。
[name="干员塞伦"]  一开始听说新人过去是贵族大小姐时我们还有点担心不好相处。
[name="干员塞伦"]  结果来了之后发现，工作能力又强，又很好说话，跟谁都能打好关系，每个人都喜欢她。
[Character(name="char_197_poca_1")]
[name="娜塔莉娅"]  没有的事，只是我年纪还小，大家都愿意照顾我而已。
[Character(name="char_013_riop",name2="char_197_poca_1",focus=1)]
[name="圆规"]  这么说起来，娜塔莉娅小姐已经决定留在罗德岛了？
[Character(name="char_013_riop",name2="char_197_poca_1",focus=2)]
[name="娜塔莉娅"]  是的，上个星期我已经通过了后勤部门的考核，正式成为了罗德岛的员工之一。
[Character(name="char_013_riop",name2="char_197_poca_1",focus=1)]
[name="圆规"]  噢，那太好了，相信我，你一定会喜欢上这里的。
[Character(name="char_013_riop",name2="char_197_poca_1",focus=2)]
[name="娜塔莉娅"]  我已经有些喜欢上这里了。
[name="娜塔莉娅"]  说起来，塞伦先生，第二批难民的名单和他们需要被送往的目的地我也已经准备好了，午休结束后就麻烦你推进下去了。
[Character(name="avg_npc_012",name2="char_197_poca_1",focus=1)]
[name="干员塞伦"]  哦？这么快吗？
[name="干员塞伦"]  也就是说，救出来的难民们实质上已经全部有了去处了吗？
[Character(name="avg_npc_012",name2="char_197_poca_1",focus=2)]
[name="娜塔莉娅"]  嗯，除了还有一部分在接受治疗的之外，其他已经全部确认完成了。
[Character(name="avg_npc_012",name2="char_197_poca_1",focus=1)]
[name="干员塞伦"]  厉害厉害，部长把这件事交给你负责果然是正确的选择。
[Character(name="avg_npc_012",name2="char_197_poca_1",focus=2)]
[name="娜塔莉娅"]  我只是做了我该做的事而已。
[Character(name="char_013_riop",name2="char_197_poca_1",focus=1)]
[name="圆规"]  这么说，我也得赶紧去申请参加第二批的护送了。
[Character(name="char_013_riop",name2="avg_npc_012",focus=2)]
[name="干员塞伦"]  第二批你也要去？你不是吃不惯乌萨斯的饭菜吗？
[Character(name="char_013_riop",name2="avg_npc_012",focus=1)]
[name="圆规"]  但我看到他们回到自己熟悉的地方，找到亲戚的表情就很开心啊。
[name="圆规"]  哎，不说了，饭也吃差不多了，帮我倒一下，我先去申请了！
[Character(name="char_013_riop",name2="avg_npc_012",focus=2)]
[name="干员塞伦"]  喂，我才不要帮你倒饭啊！
[name="干员塞伦"]  啧，不好意思啊，娜塔莉娅，让你见笑了，他就是这样急匆匆的性格。
[Character(name="char_197_poca_1")]
[name="娜塔莉娅"]  圆规先生对难民是有一些执着......吗？
[Character(name="avg_npc_012",name2="char_197_poca_1",focus=1)]
[name="干员塞伦"]  对，你刚才也听到了，他过去也是难民，是被我们一支小队救的，所以每次遇到和难民有关的任务他就特别上心。
[Character(name="avg_npc_012",name2="char_197_poca_1",focus=2)]
[name="娜塔莉娅"]  两位关系很好吗？
[Character(name="avg_npc_012",name2="char_197_poca_1",focus=1)]
[name="干员塞伦"]  啊，是啊，算不错吧。他一开始也在后勤呆了一段时间，后来才转去前线的，算是同期，性格也挺合得来，不知不觉就成了好朋友。
[name="干员塞伦"]  我记得娜塔莉娅你也是那个自治团的一员吧。
[Character(name="avg_npc_012",name2="char_197_poca_1",focus=2)]
[name="娜塔莉娅"]  是的，不过索......凛冬她们和圆规先生一样是前线干员，而我留在了后勤部而已。
[Character(name="avg_npc_012",name2="char_197_poca_1",focus=1)]
[name="干员塞伦"]  听说你们是一起被发现的，你们的关系也很好吧？
[Character(name="avg_npc_012",name2="char_197_poca_1",focus=2)]
[name="娜塔莉娅"]  ......嗯，是的，那段时光我们一直在一起，关系很好。
[Character(name="avg_npc_012",name2="char_197_poca_1",focus=1)]
[name="干员塞伦"]  共患难啊，那很好，啊，别误会，我不是说灾难好。
[Character(name="avg_npc_012",name2="char_197_poca_1",focus=2)]
[name="娜塔莉娅"]  我知道的。
[Dialog]
[Character]
[stopmusic(fadetime=3)]
[Character(name="char_115_headbr_9")]
[name="凛冬"]  ......
[Character(name="char_197_poca_1")]
[name="娜塔莉娅"]  嗯？那是......
[Character(name="avg_npc_012",name2="char_197_poca_1",focus=1)]
[name="干员塞伦"]  那不是凛冬吗，真巧，我们刚提到她。
[name="干员塞伦"]  咦，她是不是在看你？
[Character(name="avg_npc_012",name2="char_197_p

... (全文32957字符)
```

### level_act10d5_st05

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 烈夏 胡言秘语
[stopmusic]
[Dialog]
[Delay(time=1)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_trainingcom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
罗德岛训练中心
单对单近身格斗训练室
[Dialog]
[PlaySound(key="$fightgeneral")]
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadetime=0.4, block=true)]
[PlaySound(key="$fightgeneral")]
[CameraShake(duration=0.1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true)]
[PlaySound(key="$fightgeneral")]
[CameraShake(duration=0.1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true)]
[Delay(time=0.55)]
[Character(name="char_194_rosali_1#2")]
[PlaySound(key="$fightgeneral")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=120, fadeout=true, block=true)]
[name="烈夏"]  喝！
[Character(name="char_194_rosali_1#2",name2="char_137_brownb_1",focus=2)]
[name="猎蜂"]  太慢了。
[Character(name="char_194_rosali_1",name2="char_137_brownb_1",focus=1)]
[name="烈夏"]  很慢吗，那为什么还要格挡，耍嘴皮子谁不会！
[Character(name="char_194_rosali_1",name2="char_137_brownb_1",focus=2)]
[name="猎蜂"]  要是真在擂台上，你早该被我捶倒了知道不。
[Character(name="char_194_rosali_1",name2="char_137_brownb_1",focus=1)]
[name="烈夏"]  我才不信。
[Character(name="char_194_rosali_1",name2="char_137_brownb_1",focus=2)]
[name="猎蜂"]  这样吧烈夏，你再来一组连拳，要是打得好，我就给你个奖励，怎么样？
[Character(name="char_194_rosali_1",name2="char_137_brownb_1",focus=1)]
[name="烈夏"]  有意思，这可是你说的啊。
[name="烈夏"]  看拳！
[Dialog]
[Character]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="char_194_rosali_1",name2="char_137_brownb_1",focus=2)]
[name="猎蜂"]  嗯，不错不错，力度上去了。
[name="猎蜂"]  气息也保持得很好。
[name="猎蜂"]  该我了，领奖吧！
[name="猎蜂"]  噢啦噢啦！！
[Dialog]
[Character]
[PlaySound(key="$fightgeneral")]
[CameraShake(duration=0.1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadetime=0.4, block=true)]
[PlaySound(key="$fightgeneral")]
[CameraShake(duration=0.1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true)]
[delay(time=1)]
[Character(name="char_194_rosali_1",name2="char_137_brownb_1",focus=1)]
[name="烈夏"]  唔啊！
[name="烈夏"]  唔，咳，咳咳......
[name="烈夏"]  舒拉，你！
[name="烈夏"]  咳咳咳，哈......哈。
[name="烈夏"]  你能教我这招吗！
[Character(name="char_194_rosali_1",name2="char_137_brownb_1",focus=2)]
[name="猎蜂"]  教是没问题，但你可能学不来。
[Character(name="char_194_rosali_1",name2="char_137_brownb_1",focus=1)]
[name="烈夏"]  不就是拿拳头挥几下，有什么学不来的。
[Character(name="char_194_rosali_1",name2="char_137_brownb_1",focus=2)]
[name="猎蜂"]  这招可是我采蜜时对付那些“小虫子”用的，擂台里不少棘手的家伙也吃过。
[Character(name="char_194_rosali_1",name2="char_137_brownb_1",focus=1)]
[name="烈夏"]  然后呢？
[Character(name="char_194_rosali_1",name2="char_137_brownb_1",focus=2)]
[name="猎蜂"]  当然是全被我摁倒了啊，哪还有什么然后。
[name="猎蜂"]  你要是想学，先去野外采次蜜吧，这样很快就能悟的。
[name="猎蜂"]  信我。
[Character(name="char_194_rosali_1",name2="char_137_brownb_1",focus=1)]
[name="烈夏"]  啊，那还是算了。
[name="烈夏"]  你可是猎蜂。
[Character(name="char_194_rosali_1",name2="char_137_brownb_1",focus=2)]
[name="猎蜂"]  猎蜂只是会搏命的乌萨斯，要论未来，还是前途无量的小烈夏比较强。
[Character(name="char_194_rosali_1",name2="char_137_brownb_1",focus=1)]
[name="烈夏"]  嘻嘻，这话我爱听。
[Character(name="char_194_rosali_1",name2="char_137_brownb_1",focus=2)]
[name="猎蜂"]  好了，休息结束了，过来打人。
[name="猎蜂"]  当然了，想挨打也可以，我不介意和会动的沙包一起耗费掉训练室剩下的租用时间。
[Character(name="char_194_rosali_1",name2="char_137_brownb_1",focus=1)]
[name="烈夏"]  你等着舒拉，我这就来打你！
[Character(name="char_194_rosali_1",name2="char_137_brownb_1",focus=2)]
[name="猎蜂"]  哦——
[name="猎蜂"]  拳头打不过，准备上武器了？
[Character(name="char_194_rosali_1#4",name2="char_137_brownb_1",focus=1)]
[name="烈夏"]  我也是好面子的，舒拉。
[name="烈夏"]  当然了，训练室的武器都有保护措施，打到人身上顶多也就有一点疼。
[name="烈夏"]  你也挑把武器，我们练练。
[Character(name="char_194_rosali_1#4",name2="char_137_brownb_1",focus=2)]
[name="猎蜂"]  好啊。
[Character(name="char_194_rosali_1#2",name2="char_137_brownb_1",focus=1)]
[name="烈夏"]  你要用指虎了？
[Character(name="char_194_rosali_1#2",name2="char_137_brownb_1",focus=2)]
[name="猎蜂"]  毕竟擂台上喜欢拿长柄的也不少。
[Character(name="char_194_rosali_1",name2="char_137_brownb_1",focus=1)]
[name="烈夏"]  哼哼，终于动真格了吗。
[Character(name="char_194_rosali_1",name2="char_137_brownb_1",focus=2)]
[name="猎蜂"]  小烈夏，你知道对付长柄有几种办法吗。
[Character(name="char_194_rosali_1",name2="char_137_brownb_1",focus=1)]
[name="烈夏"]  不知道，你教我。
[Character(name="char_194_rosali_1",name2="char_137_brownb_1",focus=2)]
[name="猎蜂"]  好啊。
[Character]
[PlaySound(key="$radio")] 
[name="提示音"]  本训练室剩余租借时间为——20分钟。请各位干员把握好时间，方便其他干员进行使用。重复一遍，本——
[Character(name="char_194_rosali_1",name2="char_137_brownb_1",focus=2)]
[name="猎蜂"]  时间不多，看好了！
[Character(name="char_194_rosali_1",name2="char_137_brownb_1",focus=1)]
[name="烈夏"]  来啊！！
[Character(name="char_194_rosali_1#2")]
[name="烈夏"]  好快！
[name="烈夏"]  咕啊。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="char_137_brownb_1",fadetime=1,block=true)]
[delay(time=1)]
[name="猎蜂"]  咕嘟——
[Character(name="char_194_rosali_1#4",name2="char_137_brownb_1",focus=1)]
[name="烈夏"]  咕嘟咕嘟，哈——爽了。
[Character(name="char_194_rosali_1#4",name2="char_137_brownb_1",focus=2)]
[name="猎蜂"]  刚刚运动完喝水喝那么快，小心半夜肚子疼。
[Character(name="char_194_rosali_1",name2="char_137_brownb_1",focus=1)]
[name="烈夏"]  疼就疼，至少现在舒服。
[Character(name="char_194_rosali_1",name2="char_137_brownb_1",focus=2)]
[name="猎蜂"]  怎么样，这次有学到点什么没。
[Character(name="char_194_rosali_1",name2="char_137_brownb_1",focus=1)]
[name="烈夏"]  有啊。
[Character(name="char_194_rosali_1",name2="char_137_brownb_1",focus=2)]
[name="猎蜂"]  嘿嘿，说来听听？
[Character(name="char_194_rosali_1",name2="char_137_brownb_1",focus=1)]
[name="烈夏"]  以后千万不能被拳击手近身。
[Character(name="char_194_rosali_1",name2="char_137_brownb_1",focus=2)]
[name="猎蜂"]  嗨，我拿指虎只是吓吓你。
[name="猎蜂"]  冲上来招呼你用的都是手肘和肩，你又穿着防护服，疼肯定是不疼的。
[Character(name="char_194_ros

... (全文34238字符)
```

### level_act10d5_st06

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 总集篇 太阳照常升起
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_corridor",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Decision(options="......米娅", values="1")]
[Predicate(references="1")]
[Decision(options="阿米娅。", values="1")]
[Predicate(references="1")]
[Character(name="char_002_amiya_1#6")]
[name="阿米娅"]  诶？啊，抱歉，博士，我不小心发呆了。
[Decision(options="你的脸色不太好。", values="1")]
[Predicate(references="1")]
[Character(name="char_002_amiya_1")]
[name="阿米娅"]  啊，嗯，有些稍微在意的事呢。
[name="阿米娅"]  博士，你看，这里有一份内部的调岗申请。
[name="阿米娅"]  申请人是，娜塔莉娅·罗斯托娃。
[name="阿米娅"]  意向是从后勤部门调往前线。
[Decision(options="是乌萨斯自治团的......;......;呃，是谁来着？", values="1;2;3")]
[Predicate(references="1")]
[Character(name="char_002_amiya_1")]
[name="阿米娅"]  是的，她是唯一一个在后勤部门工作的自治团成员。
[name="阿米娅"]  她似乎因为工作能力出众，在后勤部门风评非常好呢。
[Predicate(references="2")]
[Character(name="char_002_amiya_1")]
[name="阿米娅"]  博士果然也会在意吧。老实说，这一次，我也不是很想通过呢。
[Predicate(references="3")]
[Character(name="char_002_amiya_1")]
[name="阿米娅"]  乌萨斯人的名字都有些难记，博士不记得也很正常呢。
[name="阿米娅"]  她是我们从切尔诺伯格营救出来的难民之一，也是凛冬的乌萨斯自治团中的成员。
[name="阿米娅"]  其实也是我们救出来的难民中，唯一的贵族。
[Predicate(references="1;2;3")]
[Character(name="char_002_amiya_1")]
[name="阿米娅"]  博士你还记得吧，凛冬她们之所以能够成为干员，是因为她们本人的要求。
[name="阿米娅"]  我一开始其实是很反对的。
[Decision(options="毕竟她们才刚被救出来没多久......;......;我相信你的判断。", values="1;2;3")]
[Predicate(references="1")]
[Character(name="char_002_amiya_1")]
[name="阿米娅"]  是的。原本，即使是她们本人的意向，我也会说服凯尔希医生否决掉的。
[Character(name="char_002_amiya_1#4")]
[name="阿米娅"]  只是......
[Predicate(references="2")]
[Character(name="char_002_amiya_1")]
[name="阿米娅"]  她们有定期接受心理方面的辅导，从报告来看，她们虽然有一定的阴影，但总体是健康的。
[Character(name="char_002_amiya_1#4")]
[name="阿米娅"]  只是......
[Predicate(references="3")]
[Character(name="char_002_amiya_1")]
[name="阿米娅"]  谢谢博士。
[Character(name="char_002_amiya_1#4")]
[name="阿米娅"]  但是......
[Predicate(references="1;2;3")]
[Character(name="char_002_amiya_1#4")]
[name="阿米娅"]  我不知道该怎么说比较好。
[name="阿米娅"]  ......博士，你可以去看一看娜塔莉娅小姐吗？
[Decision(options="好。;......;好麻烦。", values="1;2;3")]
[Predicate(references="1")]
[Character(name="char_002_amiya_1")]
[name="阿米娅"]  那就拜托博士你了。
[Predicate(references="2")]
[Character(name="char_002_amiya_1")]
[name="阿米娅"]  博士，虽然这件事会有些麻烦，但也只能拜托博士你了。
[Predicate(references="3")]
[Character(name="char_002_amiya_1")]
[name="阿米娅"]  博士，这可是非常重要的事，不要偷懒啦。
[name="阿米娅"]  而且，也不用非常严肃地去观察，就当做是工作之余的转换心情去看一看就好了。
[Predicate(references="1;2;3")]
[Character(name="char_002_amiya_1#3")]
[name="阿米娅"]  啊，午休时间也到了，博士也不用太急，吃完午饭后去找她吧。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_bridge",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_115_headbr_9",fadetime=1,block=true)]
[delay(time=1)]
[name="凛冬"]  喂，博士。
[Decision(options="有什么事吗？;......;嘿，凛冬。", values="1;2;3")]
[Predicate(references="1")]
[Character(name="char_115_headbr_9")]
[name="凛冬"]  没事，我只是看到你叫你一声。
[Predicate(references="2")]
[Character(name="char_115_headbr_9")]
[name="凛冬"]  喂，别装作没听到，你明明停下来了吧。
[name="凛冬"]  你这家伙不是工作很多吗，怎么在这里闲逛。
[Predicate(references="3")]
[Character(name="char_115_headbr_9")]
[name="凛冬"]  你看起来很闲的样子。
[Predicate(references="1;2;3")]
[Character(name="char_115_headbr_9")]
[name="凛冬"]  我接下来要出任务，可没你这样的闲工夫乱逛。
[Dialog]
[Character]
[Character(name="char_148_nearl_1",fadetime=1,block=true)]
[delay(time=1)]
[name="临光"]  凛冬，我说过，出发前不要随便走动。
[Character(name="char_115_headbr_9", name2="char_148_nearl_1",focus=1)]
[name="凛冬"]  ......
[Character(name="char_148_nearl_1")]
[name="临光"]  午安，博士。
[name="临光"]  好了，凛冬，快回休息室去，该出发了。
[Character(name="char_115_headbr_9", name2="char_148_nearl_1",focus=1)]
[name="凛冬"]  哼，总有一天我也要当队长对你发号施令。
[name="凛冬"]  还有你，博士，我总有一天会超过你的。
[Character(name="char_115_headbr_9", name2="char_148_nearl_1",focus=2)]
[name="临光"]  志气不错，不过等你赢得过我一只手之后再说吧。
[name="临光"]  至于博士，嗯，赢过全力的我再说吧。
[Character(name="char_115_headbr_9", name2="char_148_nearl_1",focus=1)]
[name="凛冬"]  啧。
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n")]
[delay(time=1)]
[Character(name="char_148_nearl_1")]
[name="临光"]  哦，博士，你应该知道，最近轮到我带新人小队。
[name="临光"]  那么要是没有什么事的话，我也先离开了。
[Decision(options="你觉得凛冬怎么样？", values="1")]
[Predicate(references="1")]
[Character(name="char_148_nearl_1")]
[name="临光"]  嗯？
[name="临光"]  嗯......首先正如你刚才看到的，不服管教，目无尊长。
[name="临光"]  而且，作为战士，在这个年纪，往往不知道自己在和什么战斗，也不知道自己该为什么战斗，这很正常。
[name="临光"]  但在她身上这一点尤为明显。
[name="临光"]  她有着很重的迷茫，我不知道那是什么，但这是一个很不好的现象，是我接下来要重点纠正她的地方。
[Decision(options="你是说，她只是看上去很凶狠？;......;唉，我还挺想跟她搞好关系的。", values="1;2;3")]
[Predicate(references="1")]
[Character(name="char_148_nearl_1")]
[name="临光"]  没错。外露的暴力是一种保护壳。
[name="临光"]  我不敢说她外壳下的内心就是脆弱的，但我至少敢说，她的凶狠在我面前不堪一击。
[Predicate(references="2")]
[Character(name="char_148_nearl_1")]
[name="临光"]  别担心，博士，她还是个孩子。
[name="临光"]  我听说她来自切尔诺伯格，在那里她恐怕有一些不好的回忆，但她还有未来。
[Predicate(references="3")]
[Character(name="char_148_nearl_1")]
[name="临光"]  哈哈，博士，不要急。
[name="临光"]  你也知道，她并不是讨厌你或怎么样。
[name="临光"]  倒不如说，她对于亲近自己的人才会下意识地去攻击。
[Predicate(references="1;2;3")]
[Character(name="char_148_nearl_1")]
[name="临光"]  不过，我必须要说，我并不讨厌这孩子，博士。
[name="临光"]  其实我挺喜欢她的，她身上有一种纯粹的正直，即使迷茫，这股正直也会带领她不至于走偏。
[name="临光"]  这是一件很难得的事。
[name="临光"]  啊，要到出发时间了，那么，我先失陪了。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_canteen",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_196_sunbr_1#2",fadetime=1,block=true)]
[delay(time=1)]
[name="古米"]  咦，是博士！
[Decision(options="中午好，古米。;......;咦，是古米！", values="1;2;3")]
[Predicate(references="1")]
[Character(name="char_196_sunbr_1#2")]
[name="古米"]  博士中午好！
[Predicate(references="2")]
[Character(name="char_196_sunbr_1#3")]
[name="古米"]  难道是古米太矮了吗？！
[name="古米"]  博士，喂，看得到古米吗？
[Predicate(references="3")]
[Character(name="char_196_sunbr_1#5")]
[name="古米"]  博士今天心情看起来不错呢！
[Predicate(references="1;2;3")]
[Character(n

... (全文19285字符)
```

### level_act10d5_st07

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 小警察 在春天之前
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
人们在一切作品中常说邪不胜正。
我时常想，这当然是无可辩驳的。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_cherbefore_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[name="女性"]  你真的要去吗？
[name="女性"]  我看到报道了，他们说暴民和警官们起了争执。
[name="女性"]  我看到有人流血，很多人流血......
[name="男性"]  别担心，亲爱的，事情没有那么严重。
[name="男性"]  记者们总会胡乱夸大一些消息，你知道的，他们要靠这个吃饭，所以总是专盯着那些最坏的报道。
[name="男性"]  放心，别让他们吓到你。
[name="女性"]  可是......
[name="女性"]  听烟草店的老板说，最近来买酒的贵族老爷越来越少，在桑坦利勋爵家做工的妮娜婶婶也回了家，说是勋爵一家暂时不要人做工。
[name="女性"]  你说，会不会、会不会是——
[name="男性"]  别瞎说！
[name="女性"]  ......
[name="男性"]  ......抱歉，我不该这么大声。原谅我。
[name="女性"]  洛班，我只是，我只是真的很担心。
[name="男性"]  放心吧，别害怕，还有我在呢。你要相信我，我总会保护好你们，对不对？
[name="男性"]  还有我们军警在这座城市里，我们的军队驻扎在城市外围，相信我，没什么好怕的。
[name="女性"]  洛班......
[name="男性"]  放心吧，达丽雅。这个家，还有我们的城市，都会由我们来守护，这是我们曾经对自己的职责发过誓的。
[name="男性"]  别烦恼了，嗯？这个冬天很快就会过去，等到天气暖和一些，我们就去好好放松一下，怎么样？
[name="男性"]  不告诉卓娅，就我们俩，偷偷去，好不好？
[name="女性"]  ......噗嗤。
[name="女性"]  哎，你这人，怎么都这把岁数了，还不老实？
[name="女性"]  现在天气这么冷，到时候雪化了，路上全是泥，要去哪里放松？
[name="男性"]  这不是正好要送冬？等到时候，我们去跳舞，你从家里带点蜜酒，我亲手给你做饼吃。
[name="女性"]  呵呵，说大话，你还记得怎么做？......我想想，也好。到时卓娅也该开学了，等她去了寄宿学校，我们再去。
[name="男性"]  行！哎，她还有多久才开学？要不然我提前送她回学校吧？
[name="女性"]  瞎说什么呢！
[name="女性"]  卓娅？卓娅你来得正好，快过来，爸爸要去值夜班了，来和爸爸说再见。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[stopmusic(fadetime=3)]
所有幸福的事情，或许会在当时强烈地爆发，彰显无与伦比的存在感。
又或许好像从来都很平淡，只是当回头再看时，才意识到那是怎样的时光。
只是寻常的对话，只是单调的日常。
就好像默认春天一定会照常到来，郊外的雪会融化，人们会拾起干草扎成草人，在淡蜜酒的香气中踩了满脚泥。
理所当然一样，说早上好，说晚安，说你好，说再见。
直到那一天——
我们的城市在我眼前，扭曲，变形，爆发。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_cher_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Character(name="char_405_absin_ed_1",fadetime=1,block=true)]
[delay(time=1)]
[name="？？？"]  左前方，无人。
[name="？？？"]  好机会。
[Dialog]
[Character]
[PlaySound(key="$rungeneral", volume=1)]
[delay(time=1)]
[Character(name="char_405_absin_ed_1",fadetime=1,block=true)]
[delay(time=1)]
[name="？？？"]  ......
[name="？？？"]  没有信号，还是联系不上外面。
[name="？？？"]  呼，总算被我摸清他们的巡逻规律了，到这里应该就没问题了。接下来只要能越过围墙......
[name="？？？"]  这次一定要成功！
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[Character(name="char_405_absin_ed_1#2")]
[name="？？？"]  ！
[PlaySound(key="$runsand", volume=1)]
[Character(name="char_405_absin_ed_1#2")]
[name="？？？"]  （怎么回事，有什么人来了！这个点明明不应该有巡逻队的......不行，得先找个地方藏起来。）
[Character(name="char_1002_nsabr_1",name2="char_1002_nsabr_1",focus=1)]
[name="整合运动士兵"]  （模糊的说话声）
[Character(name="char_1002_nsabr_1",name2="char_1002_nsabr_1",focus=2)]
[name="整合运动士兵"]  （有点激动的说话声）
[Character(name="char_405_absin_ed_1")]
[name="？？？"]  （好，暂时藏在这里应该就没问题了。）
[name="？？？"]  （这个声音，好像是那群自称整合运动的人，而且来的不止一个......左边的那个，看起来不像是在平常巡逻的那种士兵。）
[Character(name="char_405_absin_ed_1#2")]
[name="？？？"]  （到底是怎么一回事，突然出现又把我们全都关在学校里，那帮暴徒到底想干什么？）
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[name="？？？"]  （......！他们走过来了！）
[Character(name="char_1002_nsabr_2",name2="char_1002_nsabr_1",focus=1)]
[name="整合运动士兵队长"]  你说，梅菲斯特他是怎么想的？
[name="整合运动士兵队长"]  他真会自愿接手这种活，要去和那一边的学生打交道？我很难相信他有这种好心。
[name="整合运动士兵队长"]  他们把那批学生全关在彼得海姆中学那边，那些贵族的孩子大多都被带过去了，到底为什么要跑那么远？
[name="整合运动士兵队长"]  那所学校离我们驻扎的这一所还有一段距离，梅菲斯特他就算真的要做什么，我们也很难插手......
[name="整合运动士兵队长"]  唉，希望他能顾全大局，不要乱来。
[Character(name="char_1002_nsabr_2",name2="char_1002_nsabr_1",focus=2)]
[name="整合运动士兵"]  谁**知道那个小疯子怎么想？也许他就是故意这么干的！
[name="整合运动士兵"]  他就是个疯子！怪物！*！
[Character(name="char_1002_nsabr_2",name2="char_1002_nsabr_1",focus=1)]
[name="整合运动士兵队长"]  喂，你冷静点，再怎么说我们和他们，也还算是一伙的......
[Character(name="char_1002_nsabr_2",name2="char_1002_nsabr_1",focus=2)]
[name="整合运动士兵"]  我怎么冷静！？难道你上次没见到他用那种见鬼的恶毒法术？
[Character(name="char_1002_nsabr_2",name2="char_1002_nsabr_1",focus=1)]
[name="整合运动士兵队长"]  ......小声点说话！
[Character(name="char_1002_nsabr_2",name2="char_1002_nsabr_1",focus=2)]
[name="整合运动士兵"]  他真有把我们当一伙的？全都是放屁！
[Character(name="char_1002_nsabr_2",name2="char_1002_nsabr_1",focus=1)]
[name="整合运动士兵队长"]  我叫你小声点！别吓到楼里的学生们！
[Character(name="char_1002_nsabr_2",name2="char_1002_nsabr_1",focus=2)]
[name="整合运动士兵"]  ......*！
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="char_1002_nsabr_2",name2="char_1002_nsabr_1",focus=2)]
[name="整合运动士兵"]  对不住，是我太激动。
[Character(name="char_1002_nsabr_2",name2="char_1002_nsabr_1",focus=1)]
[name="整合运动士兵队长"]  我能理解。我明白你的心情，谁不是这样呢。
[Character(name="char_1002_nsabr_2",name2="char_1002_nsabr_1",focus=2)]
[name="整合运动士兵"]  说真的，有时候我真想杀了梅菲斯特，如果不是大尉不准，我保准现在就去杀了他！
[Character(name="char_1002_nsabr_2",name2="char_1002_nsabr_1",focus=1)]
[name="整合运动士兵队长"]  别说这样的傻话。你想杀他，难道我不想？大尉难道就不想？
[name="整合运动士兵队长"]  但是不行，只要我们还是同胞，这种行为就不被允许，我们不该互相伤害，这和我们的初衷不符。
[name="整合运动士兵队长"]  不过，确实，你会生气也是正常的......他这次行动中干的算是什么事啊。
[name="整合运动士兵队长"]  就这么纵容他手下那些人乱来，我们是这种闯进别人家杀人放火的暴徒吗？
[Character(name="char_405_absin_ed_1#2")]
[name="？？？"]  （梅菲斯特？那是谁？）
[name="？？？"]  （他们在说什么......杀人？！）
[name="？？？"]  （是我听错了？这些人明明没有对学生们动手，为什么......）
[Character(name="char_1002_nsabr_2",name2="char_1002_nsabr_1",focus=2)]
[name="整合运动士兵"]  哈，说得好听。我们不就是暴徒吗？
[name="整合运动士兵"]  可能你们这些大尉手下的部队不是，但要我说，我们在这座城市内可没干什么好事。
[name="整合运动士兵"]  我们毁掉多少街区了？被从家里拖出来杀死的人还少吗？现在外头都乱成什么样了，你自己也清楚。
[Character(name="char_1002_nsabr_2",name2="char_1002_nsabr_1",focus=1)]
[name="整合运动士兵队长"]  我......
[Character]
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[delay(time=1)]
[Character(name="char_1011_wizard_1")]
[name="整合运动术师"]  这是没办法的事，你不能指望这里的人真的能区别看待我们之中不同的小队。
[name="整合运动术师"]  只要所有同胞中，有任何一个人像你说的那么做了，那么我们在这里的人眼中就都是暴徒。
[Character(name="char_1

... (全文29068字符)
```


## 统计

- 总字符数：205594
- 对话行数：2445


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
