# 明日方舟 · 活动剧情 · act1sandbox（94段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act1sandbox」完整剧情脚本（94个文件，743行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act1sandbox
- 脚本文件数：94

### dialog_sandbox_0_default

```
[HEADER(actId="act1sandbox", npcId="")] 
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name="？？？"]你好
[End]

```

### dialog_sandbox_0_escape

```
[HEADER(actId="act1sandbox", npcId="")] 
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name=""]该地区存在逃脱点，可用于建立跨域通讯。
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name=""]跨域通讯建成后，可自由选择时机结束本局演算。
[End]

```

### dialog_sandbox_0_main_10b_appear

```
[HEADER(actId="act1sandbox", npcId="trap_432_oldisin")] 
[character(name="avg_npc_173", offsetX="100", offsetY="100")]
[name="老伊辛"]......
[name="老伊辛"]这样的惨象......老伊辛也是很多年都没有再看到了......
[End]

```

### dialog_sandbox_0_main_10b_click

```
[HEADER(actId="act1sandbox", npcId="trap_432_oldisin")] 
[character(name="avg_npc_173", offsetX="100", offsetY="100")]
[name="老伊辛"]唉......孩子们，我也不能帮到更多了......
[name="老伊辛"]你们快过去吧......
[Decision(option1="（从余火里拉出受伤的孩子）", value1="1.1")]
[predicate(references="1.1")]
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name="受伤的孩子"]呜呜呜......！妈妈被烧死了......
[name="受伤的孩子"]妈妈被烧死了......！！
[Decision(option1="（合力抬起倒塌的墙体）", value1="2.1")]
[predicate(references="2.1")]
[character(name="avg_npc_071", offsetX="100", offsetY="100")]
[name="受伤的部族人"]......没救了，已经死了......
[name="受伤的部族人"]先去救那些......还活着的人吧......
[Decision(option1="（查看临时搭起的小棚）", value1="3.1")]
[predicate(references="3.1")]
[character(name="avg_npc_073", offsetX="100", offsetY="100")]
[name="忙碌的部族人"]忍一忍，先忍一忍......
[name="忙碌的部族人"]药也被毁了......你先咬着毛巾......
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name=""]怎么会这样......我们怎么......这么晚才回来啊？
[name=""]部落里剩下的人都在这里了，但是，刚刚还和我们传递了消息，更快回去的那些人呢？
[name=""]......为什么没看到他们？
[character(name="avg_npc_163", offsetX="75", offsetY="100")]
[name="爱麦拉"]你们在找谁？之前回来的那一批人吗？
[name="爱麦拉"]他们刚刚为了保护一群孩子，挡在前面，被那些人轰烂了。救不回来，已经死了。我的爱人也......
[name="爱麦拉"]我给他们盖了草席，就在那边。
[Decision(option1="（去她所说的地方）", value1="4.1")]
[predicate(references="4.1")]
[character(name="avg_npc_163", offsetX="75", offsetY="100")]
[name="爱麦拉"]你们要干什么？现在去看他们吗？不许去！
[name="爱麦拉"]那边还有更多人等着我们去帮忙去救，你们现在去看他们只是浪费时间！巴塞尔......我的爱人死之前还在保护着这个他忠心了一辈子的部落......
[name="爱麦拉"]和我一起到那边去！先把他们还没做完的事情做完！
[SetConditionProgress(conditionKey="route_main", itemCount="11")]
[SetConditionProgress(conditionKey="route_main_b", itemCount="4")]
[SetConditionProgress(conditionKey="main_10b_enemy_rush", itemCount="1")]
[withdraw(charId="trap_432_oldisin")]
[End]

```

### dialog_sandbox_0_main_11a_click

```
[HEADER(actId="act1sandbox", npcId="trap_435_trsrhuntr")] 
[character(name="avg_npc_805_1", offsetX="100", offsetY="100")]
[name="寻宝人"]呜哇，吓了我一跳，注意力都放在眼前的东西上了，完全没有注意到后面来了人......
[character(name="avg_npc_165", offsetX="100", offsetY="50")]
[name="巴塞尔"]啊，抱歉，我们不是故意的......
[character(name="avg_npc_805_1", offsetX="100", offsetY="100")]
[name="寻宝人"]没事！看，这是我刚刚才做好清理的古金币，它很美丽，对吧？
[name="寻宝人"]嘿嘿，真没想到居然在这里也能遇到同行。
[name="寻宝人"]各位好啊，我是为了搜集各种各样的古金币而来到这里的寻宝专家！
[Decision(option1="寻宝专家！这么厉害啊。", value1="1.1", option2="寻宝专家？你看起来很年轻的样子。", value2="1.2")]
[predicate(references="1.1")]
[character(name="avg_npc_805_1", offsetX="100", offsetY="100")]
[name="寻宝人"]虽然也没有那么厉害，但我对自己还是很有自信的。
[name="寻宝人"]如果能成为像爸爸那样的考古学家，那就再好不过了。
[character(name="avg_npc_805_1", offsetX="100", offsetY="100")]
[name="寻宝人"]哼，怎么我又提到那个人了，他几年前执意外出考古后就再没回来，我已经不会再去期待了。
[name="寻宝人"]不说这些了，你们拿着的是一张......藏宝图？
[name="寻宝人"]唔，这古朴的纸张，发黄漶漫的文字，真令人好奇啊，它的背后蕴藏着一个怎样的故事，上面的这些文字可不是萨尔贡语，嗯......
[name="寻宝人"]似乎是在说什么“宝物”“岩居”“沉埋”......之类的......
[Decision(option1="“宝物”？", value1="2.1")]
[predicate(references="2.1")]
[character(name="avg_npc_805_1", offsetX="100", offsetY="100")]
[name="寻宝人"]对啊，加上前面的这些字符......连起来应该是“堆成山的宝物”这样的意思。
[Decision(option1="“堆成山的宝物”！", value1="3.1")]
[predicate(references="3.1")]
[character(name="avg_npc_165", offsetX="100", offsetY="50")]
[name="巴塞尔"]哇......如果我们找到它，是不是就可以不用担心王酋征税了！
[name="巴塞尔"]我们部落那些钱，一旦交了税，可能就不剩下多少了。一个月辛辛苦苦下来，大部分却不能属于我们......
[character(name="avg_npc_805_1", offsetX="100", offsetY="100")]
[name="寻宝人"]上面这些文字真的有些难懂呢，你们居然能理解吗？看不出来，你们也挺厉害的嘛。
[Decision(option1="完全不能。", value1="4.1")]
[predicate(references="4.1")]
[character(name="avg_npc_805_1", offsetX="100", offsetY="100")]
[name="寻宝人"]嗯......嗯？所以你们现在只是在乱走吗？那么，请带上我一起吧！
[name="寻宝人"]这样的藏宝图并不常见，它可能是几十年、几百年之前的人们所写下的。试想一下，仅仅是一张藏宝图，就能将你我和此处的先人们联系在一起，我们寻找他们尘封的宝藏，也是在寻找一段历史。
[name="寻宝人"]这是一件多么让人向往的事情啊。
[name="寻宝人"]......
[name="寻宝人"]欸，你们怎么光看着我点头呀？
[name="寻宝人"]......现在才开始仔细看这张藏宝图吗？
[name="寻宝人"]......你们不是我的同行吧！
[Decision(option1="我们是哥伦比亚大名鼎鼎的考古队。", value1="5.1", option2="不是哦。", value2="5.2")]
[predicate(references="5.1")]
[character(name="avg_npc_805_1", offsetX="100", offsetY="100")]
[name="寻宝人"]骗人！
[name="寻宝人"]咳咳......我是说，不要再骗我啦。怎么会有考古学家把这样珍贵的藏宝图不加保护地随身携带呢。
[name="寻宝人"]你们应该就只是一群偶然间发现了藏宝图的普通人吧？
[character(name="avg_npc_165", offsetX="100", offsetY="50")]
[name="巴塞尔"]如果真的能发现一笔宝藏，我们可以不用担心王酋的收税，也能再建出很多建筑，和黑市打好关系......
[name="巴塞尔"]毕竟之前曾有一位黑市的大人物说愿意帮助我们，但这么久过去，或许我们没有达到他的期待吧。
[name="巴塞尔"]但只要有了这样一大笔钱，很多问题都可以解决！不用再费力打猎采矿，即使每天在家里躺着也有钱花！
[Decision(option1="（讲述发现它的过程）", value1="6.1")]
[predicate(references="6.1")]
[character(name="avg_npc_805_1", offsetX="100", offsetY="100")]
[name="寻宝人"]老伊辛？是那位在黑市的老占卜师吗？
[name="寻宝人"]我在他那里占卜了一些问题，他告诉我，或许我此行能找到我这几年一直在寻找的人。是一位有些神秘的老先生呢......
[name="寻宝人"]不过既然如此，你们考不考虑在队伍里加上一个专业的寻宝专家作为顾问呢？我可以帮你们翻译上面的文字！
[name="寻宝人"]虽然可能有些冒昧，但是我其实来这里就是为了寻找遗迹，寻找一个人。如果发现了宝藏，我不要一分钱！拜托了！
[Decision(option1="凭什么啊，我们为什么相信你。", value1="7.1", option2="好啊，当然可以，辛苦你了！", value2="7.2")]
[predicate(references="7.1")]
[character(name="avg_npc_805_1", offsetX="100", offsetY="100")]
[name="寻宝人"]......
[name="寻宝人"]也对，这是各位的东西，是我太激动了。
[SetConditionProgress(conditionKey="route_main", itemCount="12")]
[SetConditionProgress(conditionKey="route_main_a", itemCount="5")]
[withdraw(charId="trap_435_trsrhuntr")]
[End]
[predicate(references="7.2")]
[character(name="avg_npc_805_1", offsetX="100", offsetY="100")]
[name="寻宝人"]太感谢了！我一定不会辜负各位的信任的。
[name="寻宝人"]过几天，我一定带着已经翻译好的信息再来找各位！
[SetConditionProgress(conditionKey="route_main", itemCount="13")]
[SetConditionProgress(conditionKey="route_main_a", itemCount="6")]
[withdraw(charId="trap_435_trsrhuntr")]
[End]
[predicate(references="5.2")]
[character(name="avg_npc_805_1", offsetX="100", offsetY="100")]
[name="寻宝人"]果然......是我一开始太激动了，毕竟你们就这样直接用手拿着这张藏宝图......
[name="寻宝人"]我可以问问吗，你们是怎么发现这幅藏宝图的？
[character(name="avg_npc_165", offsetX="100", offsetY="50")]
[name="巴塞尔"]如果真的能发现一笔宝藏，我们可以不用担心王酋的收税，也能再建出很多建筑，和黑市打好关系......
[name="巴塞尔"]毕竟之前曾有一位黑市的大人物说愿意帮助我们，但这么久过去，或许我们没有达到他的期待吧。
[name="巴塞尔"]但只要有了这样一大笔钱，很多问题都可以解决！不用再费力打猎采矿，即使每天在家里躺着也有钱花！
[Decision(option1="（讲述发现它的过程）", value1="8.1")]
[predicate(references="8.1")]
[character(name="avg_npc_805_1", offsetX="100", offsetY="100")]
[name="寻宝人"]老伊辛？是那位在黑市的老占卜师吗？
[name="寻宝人"]我在他那里占卜了一些问题，他告诉我，或许我此行能找到我这几年一直在寻找的人。是一位有些神秘的老先生呢......
[name="寻宝人"]不过既然如此，你们考不考虑在队伍里加上一个专业的寻宝专家作为顾问呢？我可以帮你们翻译上面的文字！
[name="寻宝人"]虽然可能有些冒昧，但是我其实来这里就是为了寻找遗迹，寻找一个人。如果发现了宝藏，我不要一分钱！拜托了！
[Decision(option1="凭什么啊，我们为什么相信你。", value1="9.1", option2="好啊，当然可以，辛苦你了！", value2="9.2")]
[predicate(references="9.1")]
[character(name="avg_npc_805_1", offsetX="100", offsetY="100")]
[name="寻宝人"]......
[name="寻宝人"]也对，这是各位的东西，是我太激动了。
[SetConditionProgress(conditionKey="route_main", itemCount="12")]
[SetConditionProgress(conditionKey="route_main_a", itemCount="5")]
[withdraw(charId="trap_435_trsrhuntr")]
[End]
[predicate(references="9.2")]
[character(name="avg_npc_805_1", offsetX="100", offsetY="100")]
[name="寻宝人"]太感谢了！我一定不会辜负各位的信任的。
[name="寻宝人"]过几天，我一定带着已经翻译好的信息再来找各位！
[SetConditionProgress(conditionKey="route_main", itemCount="13")]
[SetConditionProgress(conditionKey="route_main_a", itemCount="6")]
[withdraw(charId="trap_435_trsrhuntr")]
[End]
[predicate(references="1.2")]
[character(name="avg_npc_805_1", offsetX="100", offsetY="100")]
[name="寻宝人"]你在说什么啊？不要因为年纪轻就小瞧别人。
[name="寻宝人"]之前看不起我的老古董们，后来可都对我做出的成绩十分认可哦。
[name="寻宝人"]就算是爸爸那样的考古学家，之前也夸赞过我的能力。
[character(name="avg_npc_805_1", offsetX="100", offsetY="100")]
[name="寻宝人"]哼，怎么我又提到那个人了，他几年前执意外出考古后就再没回来，我已经不会再去期待了。
[name="寻宝人"]不说这些了，你们拿着的是一张......藏宝图？
[name="寻宝人"]唔，这古朴的纸张，发黄漶漫的文字，真令人好奇啊，它的背后蕴藏着一个怎样的故事，上面的这些文字可不是萨尔贡语，嗯......
[name="寻宝人"]似乎是在说什么“宝物”“岩居”“沉埋”......之类的......
[Decision(option1="“宝物”？", value1="10.1")]
[predicate(references="10.1")]
[character(name="avg_npc_805_1", offsetX="100", offsetY="100")]
[name="寻宝人"]对啊，加上前面的这些字符......连起来应该是“堆成山的宝物”这样的意思。
[Decision(option1="“堆成山的宝物”！", value1="11.1")]
[predicate(references="11.1")]
[character(name="avg_npc_165", offsetX="100", offsetY="50")]
[name="巴塞尔"]哇......如果我们找到它，是不是就可以不用担心王酋征税了！
[name="巴塞尔"]我们

... (全文9786字符)
```

### dialog_sandbox_0_main_12a_click

```
[HEADER(actId="act1sandbox", npcId="trap_435_trsrhuntr")] 
[character(name="avg_npc_805_1", offsetX="100", offsetY="100")]
[name="寻宝人"]总算等到各位了！
[name="寻宝人"]经过最近一段时间的努力，我已经成功破解了藏宝图上所写的文字内容。
[name="寻宝人"]这种文字之前并没有十分详尽的记录，这次翻译结束后，我整理出了数百个新词，极大程度地填补了这些空白。
[name="寻宝人"]不仅如此，这张藏宝图的背面还有一首叙事长诗，翻译下来可以知道，拥有它的是一个十分富饶的部族，先祖留下的宝藏已经传了几代。
[name="寻宝人"]不知道后来发生了什么导致了这张藏宝图的遗落，有可能是场天灾，有可能是战争，这里面还提到了“梦魇”！
[name="寻宝人"]或许我以后可以顺着这条线索往下继续探究，说不定还能找到有关父亲的线索......
[name="寻宝人"]不对，我怎么又想到他了......明明是他不告而别！
[Decision(option1="（试图插话）", value1="1.1")]
[predicate(references="1.1")]
[character(name="avg_npc_805_1", offsetX="100", offsetY="100")]
[name="寻宝人"]啊，抱歉，一想到我的工作，我就有些太激动了......
[name="寻宝人"]既然现在我已经破解了这份藏宝图，就请继续让我带着各位，一起去寻找上面所指明的地点吧！
[character(name="avg_npc_165", offsetX="100", offsetY="50")]
[name="巴塞尔"]虽然部落里其实很多人对能找到宝藏并不抱有什么期望，但我们还是决定试一试。
[name="巴塞尔"]就算没找到，沿途也能打到一些猎物，说不定还有矿脉，总不至于空手而归。
[name="巴塞尔"]而且算算日子，为王酋征税的人也快到了，我们要尽早为税金做准备才行！
[character(name="avg_npc_805_1", offsetX="100", offsetY="100")]
[name="寻宝人"]那么，请各位按照我所列的清单整理一下随身物品，注意保持体力。
[name="寻宝人"]寻宝可不是一个轻松活哦！
[SetConditionProgress(conditionKey="route_main", itemCount="14")]
[SetConditionProgress(conditionKey="route_main_a", itemCount="7")]
[withdraw(charId="trap_435_trsrhuntr")]
[End]

```

### dialog_sandbox_0_main_12b_appear

```
[HEADER(actId="act1sandbox", npcId="trap_434_klmantc")] 
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name="？？？"]......好，做到了......没有留下痕迹，也没有人注意到我......
[name="？？？"]我不想......再这么胆小下去了，我为什么要继续躲下去......？明明当时他们......只是来问问我到底有没有做那些事，我为什么要逃走......？
[name="？？？"]我想做点什么......多拿走一份文件，也不会有人发现，还能帮到他们......
[name="？？？"]再往下一点点......就能拿到了......！
[name="？？？"]再往下一点点......
[Decision(option1="根据“沙卒”的信息，王酋据点就是这里！", value1="1.1")]
[predicate(references="1.1")]
[Decision(option1="投掷燃烧物和炸药！", value1="2.1")]
[predicate(references="2.1")]
[Decision(option1="二、一！", value1="3.1")]
[predicate(references="3.1")]
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name="？？？"]......啊！爆炸......？
[name="？？？"]为什么......难道是我暴露了吗......？不应该......他们完全没有注意到我......
[name="？？？"]外面这些人是......是他们？
[name="？？？"]一定出了什么事......我要赶快出去......！
[Decision(option1="为了死去的家人和朋友！", value1="4.1")]
[predicate(references="4.1")]
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name="？？？"]......啊——！
[name="？？？"]尾巴......尾巴被压住了......！动不了......
[character(name="avg_npc_008", offsetX="100", offsetY="100")]
[name="王酋据点驻扎人员"]什么人！
[character(name="avg_npc_802_1", offsetX="125", offsetY="100")]
[name="曼提柯杀手"]......被发现了！
[character(name="avg_npc_008", offsetX="100", offsetY="100")]
[name="王酋据点驻扎人员"]里面还发现了个探子！先把这个解决了！
[character(name="avg_npc_802_1", offsetX="125", offsetY="100")]
[name="曼提柯杀手"]......又是这样......
[character(name="avg_npc_008", offsetX="100", offsetY="100")]
[name="王酋据点驻扎人员"]......在那边！抓住她！
[name="王酋据点驻扎人员"]剩下的去处理外面！
[Decision(option1="是曼提柯姑娘？她怎么......？！", value1="5.1")]
[predicate(references="5.1")]
[SetConditionProgress(conditionKey="route_main", itemCount="13")]
[SetConditionProgress(conditionKey="route_main_b", itemCount="6")]
[End]

```

### dialog_sandbox_0_main_12b_click

```
[HEADER(actId="act1sandbox", npcId="trap_434_klmantc")] 
[character(name="avg_npc_802_1", offsetX="125", offsetY="100")]
[name="曼提柯杀手"]......谢谢......救了我......
[name="曼提柯杀手"]我没事......这个给你们......
[Decision(option1="（收下）", value1="1.1")]
[predicate(references="1.1")]
[AddItem(itemId="sandbox_0_building_11", itemCount="1")]
[AddItem(itemId="sandbox_0_building_14", itemCount="1")]
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name=""]【获得了1个坚固筑台Ⅱ、1个防御工事Ⅱ】
[character(name="avg_npc_802_1", offsetX="125", offsetY="100")]
[name="曼提柯杀手"]我看了......他们武器的弱点......这个，能很好地帮你们......
[name="曼提柯杀手"]所以那时才让你们......建那些东西，不是......骗你们......
[Decision(option1="你就是为了拿这个？！", value1="2.1")]
[predicate(references="2.1")]
[character(name="avg_npc_802_1", offsetX="125", offsetY="100")]
[name="曼提柯杀手"]......我太胆小了......我不想再胆小了......
[name="曼提柯杀手"]你们明明是相信我的......
[name="曼提柯杀手"]......我是能在那里跟你们一起好好生活下去的......对不起......是我逃走了......
[character(name="avg_npc_163", offsetX="75", offsetY="100")]
[name="爱麦拉"]你受伤了，别再说话了，我们背你回去。
[name="爱麦拉"]这个如果真的能帮我们重创王酋，你就是我的恩人。
[name="爱麦拉"]你就是我们部落的恩人。
[character(name="avg_npc_802_1", offsetX="125", offsetY="100")]
[name="曼提柯杀手"]......我见过你......但是，之前那个......？
[character(name="avg_npc_163", offsetX="75", offsetY="100")]
[name="爱麦拉"]......他死了。
[character(name="avg_npc_802_1", offsetX="125", offsetY="100")]
[name="曼提柯杀手"]......
[name="曼提柯杀手"]这原本是我现在的雇主交给我的任务......
[name="曼提柯杀手"]......王酋会在几天后，经过我们这里......
[name="曼提柯杀手"]你们......
[Decision(option1="我们明白了。", value1="3.1")]
[predicate(references="3.1")]
[SetConditionProgress(conditionKey="route_main", itemCount="14")]
[SetConditionProgress(conditionKey="route_main_b", itemCount="7")]
[withdraw(charId="trap_434_klmantc")]
[End]

```

### dialog_sandbox_0_main_13b_appear

```
[HEADER(actId="act1sandbox", npcId="trap_434_klmantc")] 
[character(name="avg_npc_802_1", offsetX="125", offsetY="100")]
[name="曼提柯杀手"]......咳......咳......
[name="曼提柯杀手"]......
[End]

```

### dialog_sandbox_0_main_13b_click

```
[HEADER(actId="act1sandbox", npcId="trap_434_klmantc")] 
[character(name="avg_npc_802_1", offsetX="125", offsetY="100")]
[name="曼提柯杀手"]......这是......哪里？
[character(name="avg_npc_163", offsetX="75", offsetY="100")]
[name="爱麦拉"]她醒了......她醒了！我们还是能从王酋手下......救回来人的，对不对？！我们还是能救下来人的......！还是能救下来的......！
[name="爱麦拉"]姑娘，你那天在里面，是还有什么任务吗？告诉我好不好？你是个杀手，是个刺客，对不对？
[name="爱麦拉"]是我救活的你，你那天肯定有什么任务，你肯定拿到了什么和王酋有关的东西！这个据点已经被烧掉了，你是最后的......
[character(name="avg_npc_802_1", offsetX="125", offsetY="100")]
[name="曼提柯杀手"]......
[character(name="avg_npc_163", offsetX="75", offsetY="100")]
[name="爱麦拉"]......你说什么......？声音太小了......
[character(name="avg_npc_802_1", offsetX="125", offsetY="100")]
[name="曼提柯杀手"]......夹......层......
[character(name="avg_npc_163", offsetX="75", offsetY="100")]
[name="爱麦拉"]......
[Decision(option1="是什么？", value1="1.1")]
[predicate(references="1.1")]
[character(name="avg_npc_163", offsetX="75", offsetY="100")]
[name="爱麦拉"]一张建筑草图......？
[character(name="avg_npc_802_1", offsetX="125", offsetY="100")]
[name="曼提柯杀手"]我看了......他们武器的弱点......这个，能很好地帮你们......
[name="曼提柯杀手"]所以那时才让你们......建那些东西，不是......骗你们......
[name="曼提柯杀手"]......我太胆小了......我不想再胆小了......
[name="曼提柯杀手"]你们明明是相信我的......
[name="曼提柯杀手"]......我是能在那里跟你们一起好好生活下去的......对不起......是我逃走了......
[character(name="avg_npc_163", offsetX="75", offsetY="100")]
[name="爱麦拉"]......你刚醒来，别再说话了。
[name="爱麦拉"]这个如果真的能帮我们重创王酋，你就是我的恩人。
[name="爱麦拉"]你就是我们部落的恩人。
[character(name="avg_npc_802_1", offsetX="125", offsetY="100")]
[name="曼提柯杀手"]......我见过你......但是，之前那个......？
[character(name="avg_npc_163", offsetX="75", offsetY="100")]
[name="爱麦拉"]......他死了。
[character(name="avg_npc_802_1", offsetX="125", offsetY="100")]
[name="曼提柯杀手"]......
[name="曼提柯杀手"]这原本是我现在的雇主交给我的任务......
[name="曼提柯杀手"]......王酋会在几天后，经过我们这里......
[name="曼提柯杀手"]你们......
[Decision(option1="我们明白了。", value1="2.1")]
[predicate(references="2.1")]
[SetConditionProgress(conditionKey="route_main", itemCount="14")]
[SetConditionProgress(conditionKey="route_main_b", itemCount="7")]
[withdraw(charId="trap_434_klmantc")]
[End]

```

### dialog_sandbox_0_main_15b_appear

```
[HEADER(actId="act1sandbox", npcId="trap_434_klmantc")] 
[character(name="avg_npc_802_1", offsetX="125", offsetY="100")]
[name="曼提柯杀手"]......这是，我之前住的......？
[name="曼提柯杀手"]之前这里不是......？
[End]

```

### dialog_sandbox_0_main_15b_click

```
[HEADER(actId="act1sandbox", npcId="trap_434_klmantc")] 
[character(name="avg_npc_802_1", offsetX="125", offsetY="100")]
[name="曼提柯杀手"]是你们，为我重新搭了这间屋子吗......？
[character(name="avg_npc_163", offsetX="75", offsetY="100")]
[name="爱麦拉"]你这次回来疗伤让我们......想起了之前的日子。
[name="爱麦拉"]很平静，很美好，虽然什么都还没有，黑市里的人也看不起我们，但大家都还在。
[name="爱麦拉"]你刚来的时候，这里还什么事都没有发生。我们当初搭这间小屋子，也是想着是不是干脆你以后也不要做什么杀手了，就在我们这里住下，我们一起生活。
[name="爱麦拉"]......
[name="爱麦拉"]你重新回来......说不定也挺好的......吧......
[Decision(option1="解释清楚后，大家也理解了你为什么走。", value1="1.1")]
[predicate(references="1.1")]
[character(name="avg_npc_802_1", offsetX="125", offsetY="100")]
[name="曼提柯杀手"]......我想好了，我不走了。
[name="曼提柯杀手"]我想就在这里，和你们一起......你们给了我屋子，这是我的家......
[name="曼提柯杀手"]我其实......很讨厌那样，很讨厌去杀人，很讨厌那些事......
[name="曼提柯杀手"]我希望能在这里住下......
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name=""]这段日子没有发生什么大事，我们在这片被袭击的土地上，重建起了我们的家园。
[name=""]人不多，房子也少了不少，一小片生长作物的地方。我们和曼提柯姑娘这个外来人似乎已经消除了最开始的隔阂。
[name=""]大部分人决定把目光放在当下，但仍然有人没有放下那天的事，他们偷偷去找“沙卒”，带回了来路不明的佣兵，在部落里爆发了激烈的争执。
[name=""]我们开始怀疑......当初执意去寻求与“沙卒”的合作，这个决定是否正确？
[name=""]......
[SetConditionProgress(conditionKey="route_main", itemCount="16")]
[SetConditionProgress(conditionKey="route_main_b", itemCount="9")]
[withdraw(charId="trap_434_klmantc")]
[End]

```

### dialog_sandbox_0_main_18b_appear

```
[HEADER(actId="act1sandbox", npcId="trap_434_klmantc")] 
[character(name="avg_npc_802_1", offsetX="125", offsetY="100")]
[name="曼提柯杀手"]......你们是谁！
[name="曼提柯杀手"]再靠近......我就要动手了......！
[End]

```

### dialog_sandbox_0_main_18b_click

```
[HEADER(actId="act1sandbox", npcId="trap_434_klmantc")] 
[character(name="avg_npc_802_1", offsetX="125", offsetY="100")]
[name="曼提柯杀手"]你们终于来了！
[character(name="avg_npc_007", offsetX="100", offsetY="100")]
[name="黑市商人A"]怕什么，我们只是来做笔交易。
[name="黑市商人A"]这里的东西就这么多，你们之前占了好的，现在“沙卒”走了，你们也该还回来了。
[Decision(option1="......我们要怎么还？", value1="1.1")]
[predicate(references="1.1")]
[character(name="avg_npc_802_1", offsetX="125", offsetY="100")]
[name="曼提柯杀手"]等等......他们不是商人......他们是来杀我们的！
[character(name="avg_npc_008", offsetX="100", offsetY="100")]
[name="黑市商人B"]只是来做个交易嘛。
[name="黑市商人B"]或者也很简单，你们把东西都留下来，我们可以告诉你们一条路。
[name="黑市商人B"]走出去，活着离开这。很合算了。
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name=""]要打吗？还是要离开？
[name=""]之前部落中的争论并没有停息，仍旧有人没有放弃寻找“沙卒”，包括爱麦拉。她接过了自己爱人的责任，同时日日寻求能为他报仇的方法。
[name=""]可部落中大部分人已经厌倦争斗，只想安静地在这里生活下去。
[name=""]但显然现在不是犹豫的时候。
[Decision(option1="（交出资源）", value1="2.1", option2="凭什么！我们不给！", value2="2.2")]
[predicate(references="2.1")]
[character(name="avg_npc_007", offsetX="100", offsetY="100")]
[name="黑市商人A"]这样啊，你们真的选择交出这些东西啊。
[name="黑市商人A"]那现在我们就要走了。等着下次吧，你们很快就会再遇到我们的。
[character(name="avg_npc_008", offsetX="100", offsetY="100")]
[name="黑市商人B"]王酋大人会很喜欢这些东西的。
[character(name="avg_npc_163", offsetX="75", offsetY="100")]
[name="爱麦拉"]......
[name="爱麦拉"]凭什么？！
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name=""]凭我们现在只有零星的几个人，凭我们的资源和力量不如从前，我们只能接受这一切。
[name=""]部落中大部分人松了一口气。
[name=""]在他们看来，只要还留有这个家园，只要家人和朋友还活在自己身边，我们就还有未来。
[character(name="avg_npc_163", offsetX="75", offsetY="100")]
[name="爱麦拉"]呼......王酋......王酋......他过几天就会经过这里......
[name="爱麦拉"]我受够了。这些商人，如果还有下次，我发誓我还会和今天一样站在最前面，把他们的血留在这片沙地上。
[character(name="avg_npc_070", offsetX="125", offsetY="100")]
[name="部族人A"]......可以加上我一个。
[character(name="avg_npc_071", offsetX="100", offsetY="100")]
[name="部族人B"]我们离开这里，再找一个地方生活，不好吗......？
[character(name="avg_npc_072", offsetX="100", offsetY="100")]
[name="部族人C"]不要再争执了......！
[character(name="avg_npc_802_1", offsetX="125", offsetY="100")]
[name="曼提柯杀手"]......不管怎么样......我们，要赶快为此做准备了......
[name="曼提柯杀手"]要好好活下去，我们现在的东西太少了......
[name="曼提柯杀手"]如果不能建起足够多的防御工事，我们......肯定都会死的......！
[SetConditionProgress(conditionKey="route_main", itemCount="19")]
[SetConditionProgress(conditionKey="route_main_b", itemCount="12")]
[withdraw(charId="trap_434_klmantc")]
[End]
[predicate(references="2.2")]
[character(name="avg_npc_007", offsetX="100", offsetY="100")]
[name="黑市商人A"]你们真以为这样能打过我们？
[name="黑市商人A"]一个只剩下老弱病幼的部落......
[name="黑市商人A"]还有你们这些在路边白送都没人想要的武器？
[character(name="avg_npc_008", offsetX="100", offsetY="100")]
[name="黑市商人B"]兄弟们，上！
[name="黑市商人B"]给他们点颜色瞧瞧！
[character(name="avg_npc_802_1", offsetX="125", offsetY="100")]
[name="曼提柯杀手"]......
[character(name="avg_npc_007", offsetX="100", offsetY="100")]
[name="黑市商人A"]......什么人？！我们背后......？
[character(name="avg_npc_802_1", offsetX="125", offsetY="100")]
[name="曼提柯杀手"]......
[character(name="avg_npc_008", offsetX="100", offsetY="100")]
[name="黑市商人B"]啊啊！——
[character(name="avg_npc_802_1", offsetX="125", offsetY="100")]
[name="曼提柯杀手"]......我们都说了......凭什么！不要......再来骚扰我们了！
[character(name="avg_npc_163", offsetX="75", offsetY="100")]
[name="爱麦拉"]快上！曼提柯姑娘已经帮我们解决了最麻烦的那几个！
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name=""]我们经历了无比惨痛的一战。虽然击退了那些黑市的商人，但部落已经绝对无法再承受再来一次的可能。
[name=""]部落中大部分人脸上的表情分不清是喜悦还是悲伤，他们放下武器，互相拥抱着自己受伤的家人和朋友。
[character(name="avg_npc_163", offsetX="75", offsetY="100")]
[name="爱麦拉"]......*萨尔贡粗口*......赚了！
[character(name="avg_npc_163", offsetX="75", offsetY="100")]
[name="爱麦拉"]呼......王酋......王酋......他过几天就会经过这里......
[name="爱麦拉"]我受够了。这些商人，如果还有下次，我发誓我还会和今天一样站在最前面，把他们的血留在这片沙地上。
[character(name="avg_npc_070", offsetX="125", offsetY="100")]
[name="部族人A"]......可以加上我一个。
[character(name="avg_npc_071", offsetX="100", offsetY="100")]
[name="部族人B"]我们离开这里，再找一个地方生活，不好吗......？
[character(name="avg_npc_072", offsetX="100", offsetY="100")]
[name="部族人C"]不要再争执了......！
[character(name="avg_npc_802_1", offsetX="125", offsetY="100")]
[name="曼提柯杀手"]......不管怎么样......我们，要赶快为此做准备了......
[name="曼提柯杀手"]要好好活下去，我们现在的东西太少了......
[name="曼提柯杀手"]如果不能建起足够多的防御工事，我们......肯定都会死的......！
[SetConditionProgress(conditionKey="route_main", itemCount="19")]
[SetConditionProgress(conditionKey="route_main_b", itemCount="12")]
[withdraw(charId="trap_434_klmantc")]
[End]

```

### dialog_sandbox_0_main_19b_appear

```
[HEADER(actId="act1sandbox", npcId="trap_434_klmantc")] 
[character(name="avg_npc_802_1", offsetX="125", offsetY="100")]
[name="曼提柯杀手"]......别再吵了......！
[name="曼提柯杀手"]我们，就在这里......不好吗？为什么要去刺杀王酋......？
[name="曼提柯杀手"]你们，都疯了......！你们真的会死的！
[End]

```

### dialog_sandbox_0_main_19b_click

```
[HEADER(actId="act1sandbox", npcId="trap_434_klmantc")] 
[character(name="avg_npc_802_1", offsetX="125", offsetY="100")]
[name="曼提柯杀手"]我们找个别的地方，躲起来，我们都能活着，就像之前那样......！
[character(name="avg_npc_163", offsetX="75", offsetY="100")]
[name="爱麦拉"]你可以不去的。你们也都可以不去的。只有我们几个去，这是我们几个人的决定。
[name="爱麦拉"]你可以什么都不知道地继续在这里生活下去啊，我都说了这些和你们无关，只是我们几个的决定。
[name="爱麦拉"]你已经在这里住下了，你们也有自己的家人和朋友，你们的未来还有希望，没必要和我们一起冒这个险。
[character(name="avg_npc_802_1", offsetX="125", offsetY="100")]
[name="曼提柯杀手"]......
[name="曼提柯杀手"]真的要，这样吗......？
[name="曼提柯杀手"]我们把这些东西交出去，我们，就能平安度过那一天......王酋就能暂时放过我们......
[name="曼提柯杀手"]我们都不会死，这样......不好吗......？
[character(name="avg_npc_163", offsetX="75", offsetY="100")]
[name="爱麦拉"]再过几天就是他路过这里的日子了。
[name="爱麦拉"]......我等了......很久啦。
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name=""]部落中的人们已经明显分成了两部分。
[name=""]是时候作出选择了。
[Decision(option1="（不支持复仇，活下来最重要）", value1="1.1", option2="（支持复仇，刺杀王酋）", value2="1.2")]
[predicate(references="1.1")]
[character(name="avg_npc_163", offsetX="75", offsetY="100")]
[name="爱麦拉"]......哈哈......
[name="爱麦拉"]我知道了。
[Decision(option1="你要做什么？", value1="2.1")]
[predicate(references="2.1")]
[character(name="avg_npc_163", offsetX="75", offsetY="100")]
[name="爱麦拉"]这是部落中大家共同的决定，我会遵守的，我什么都不会做。
[name="爱麦拉"]我什么都不会做的。
[name="爱麦拉"]把这些东西交出去吧，它们能保证过几天后，王酋能不在意我们这个小小的部落。
[Decision(option1="（交出物资）", value1="3.1")]
[predicate(references="3.1")]
[character(name="avg_npc_802_1", offsetX="125", offsetY="100")]
[name="曼提柯杀手"]我们......都能在这里活着，就最好了......
[name="曼提柯杀手"]哪怕是交税，只要......我们都还活着，总会好的......！
[SetConditionProgress(conditionKey="route_main", itemCount="20")]
[SetConditionProgress(conditionKey="route_main_b", itemCount="13")]
[withdraw(charId="trap_434_klmantc")]
[End]
[predicate(references="1.2")]
[character(name="avg_npc_163", offsetX="75", offsetY="100")]
[name="爱麦拉"]......哈哈......
[name="爱麦拉"]谢谢你们啦。
[Decision(option1="我们失去了太多，已经没有可以再失去的了！", value1="4.1")]
[predicate(references="4.1")]
[Decision(option1="就算是死，也要让王酋知道我们的仇恨！", value1="5.1")]
[predicate(references="5.1")]
[Decision(option1="族人们！我们要拿起武器，向王酋复仇！", value1="6.1")]
[predicate(references="6.1")]
[Decision(option1="我们要继续呐喊，我们是活在这里的人们！", value1="7.1")]
[predicate(references="7.1")]
[character(name="avg_npc_802_1", offsetX="125", offsetY="100")]
[name="曼提柯杀手"]......
[name="曼提柯杀手"]这是，你们的决定......
[SetConditionProgress(conditionKey="route_main", itemCount="21")]
[SetConditionProgress(conditionKey="route_main_b", itemCount="14")]
[SetConditionProgress(conditionKey="main_19b_enemy_rush", itemCount="1")]
[withdraw(charId="trap_434_klmantc")]
[End]

```

### dialog_sandbox_0_main_1_click

```
[HEADER(actId="act1sandbox", npcId="trap_415_trademan")] 
[character(name="avg_npc_803_1", offsetX="100", offsetY="100")]
[name="联络员"]哎，各位，又见面了！
[name="联络员"]真巧啊！
[name="联络员"]你们来这里是要做什么？狩猎？还是采集矿物？真辛苦啊！
[name="联络员"]不管是来做什么，相逢就是有缘！各位还记得我吧？我是太阳谷机械工业驻扎在这里的联络员。
[name="联络员"]要是各位对之前的事还有疑惑，或者这几天又遇到了什么不好解决的问题，都可以来问问我！
[name="联络员"]当然，各位问完以后能再来看看敝司这些新推出的产品，就更好了！
[name="联络员"]如何？
[Decision(option1="要为部落发展找资源，我们应该去哪？", value1="1.1", option2="太好了，快帮帮我们！", value2="1.2")]
[predicate(references="1.1")]
[character(name="avg_npc_803_1", offsetX="100", offsetY="100")]
[name="联络员"]各位首选自然是太阳谷机械工业，也就是敝司了。
[name="联络员"]敝司的产品全都经过层层改良和试用，不仅物美价廉，还提供整套售后服务！保证能够满足各位在这里生存发展的一切需求哦。
[name="联络员"]各位看看？
[Decision(option1="（诉说困难）", value1="2.1")]
[predicate(references="2.1")]
[character(name="avg_npc_803_1", offsetX="100", offsetY="100")]
[name="联络员"]......原来如此！
[name="联络员"]难得我和各位如此聊得来，我从业这么久还是第一次遇到如此有缘之人！
[name="联络员"]不如这样，为了表达我的欣喜之情，我们从今天开始就是合作者了，如何？
[name="联络员"]我还可以再给大家透露一个伊巴特地区最大的交易场——沁礁黑市，就在各位驻扎地的西北处！在那里只要有钱，就能买到各位想要的所有东西。
[name="联络员"]哦，那边的小哥我之前好像在你们部落里也见过，这么急匆匆的样子，干什么去了？
[character(name="avg_npc_165", offsetX="100", offsetY="50")]
[name="巴塞尔"]呼......呼......这鬼天气......
[name="巴塞尔"]我们回来了！刚才带着几个人一起去附近看了看，有不少可以捕猎采集的地方，我们过一会儿就先去收集资源吧。
[name="巴塞尔"]还有什么事需要我去做吗？
[Decision(option1="暂时没有了。", value1="3.1")]
[predicate(references="3.1")]
[Decision(option1="我们在听这位联络员讲黑市的事。", value1="4.1")]
[predicate(references="4.1")]
[character(name="avg_npc_165", offsetX="100", offsetY="50")]
[name="巴塞尔"]黑市......我们在来的时候好像注意过那个地方。
[name="巴塞尔"]如果只是单纯地在这里生活一阵，我们之前倒已经做了一些准备——这片土地虽然有些贫瘠，但暂时养活我们，还没什么问题。
[name="巴塞尔"]但这里毕竟还是萨尔贡，征税队发现我们，只是早晚的问题，我们现在根本没有钱去交税......
[name="巴塞尔"]......出于更长远的考虑，黑市，确实是一个选择。
[character(name="avg_npc_803_1", offsetX="100", offsetY="100")]
[name="联络员"]对，这就是我刚刚说的了！各位，不论是想花钱买想要的东西，还是想要快速地挣钱，黑市都是一个好去处。
[name="联络员"]只要各位愿意，找一位雇主接下几个单子，或者是帮他们送送东西，报酬够各位这样的部落好好生活一阵子了。
[name="联络员"]特别是——
[name="联络员"]（小声）要是能得到黑市背后某位的支持......
[name="联络员"]那位掌控着整个黑市的人名叫“沙卒”，我对他慕名已久，可惜自己只是一个小小的联络员......
[Decision(option1="黑市......谢谢你告诉我们。", value1="5.1", option2="好，我们这就去！", value2="5.2")]
[predicate(references="5.1")]
[character(name="avg_npc_803_1", offsetX="100", offsetY="100")]
[name="联络员"]各位是我的合作者，这点小忙不算什么。
[name="联络员"]你们刚到这里，却被我一直拉着说话，真是过意不去。各位请先在这里安顿下来，我那时再来打扰吧！
[name="联络员"]别忘了，黑市就在各位驻扎地的西北处，而且，敝司在那里也有点小生意，各位也要多多光顾我们太阳谷啊！
[SetConditionProgress(conditionKey="route_main", itemCount="1")]
[withdraw(charId="trap_415_trademan")]
[End]
[predicate(references="5.2")]
[character(name="avg_npc_803_1", offsetX="100", offsetY="100")]
[name="联络员"]欸，请再稍等一下！不来看看敝司的新产品吗？价格十分优惠！比如这个——
[name="联络员"]欸，真走了？
[name="联络员"]那、那——别忘了黑市在各位驻扎地的西北处，敝司在那里也有点小生意——祝各位今天一切顺利！
[SetConditionProgress(conditionKey="route_main", itemCount="1")]
[withdraw(charId="trap_415_trademan")]
[End]
[predicate(references="1.2")]
[character(name="avg_npc_803_1", offsetX="100", offsetY="100")]
[name="联络员"]哎呀，这么急迫啊。
[name="联络员"]别着急，敝司正好最近新研发出了一款械能按摩椅，能消除人体上的一切疲劳，身上不累了，心里就不烦了，事也就好办了。
[name="联络员"]不如我们先坐下来慢慢聊？
[Decision(option1="（诉说困难）", value1="6.1")]
[predicate(references="6.1")]
[character(name="avg_npc_803_1", offsetX="100", offsetY="100")]
[name="联络员"]......原来如此！
[name="联络员"]难得我和各位如此聊得来，我从业这么久还是第一次遇到如此有缘之人！
[name="联络员"]不如这样，为了表达我的欣喜之情，我们从今天开始就是合作者了，如何？
[name="联络员"]我还可以再给大家透露一个伊巴特地区最大的交易场——沁礁黑市，就在各位驻扎地的西北处！在那里只要有钱，就能买到各位想要的所有东西。
[name="联络员"]哦，那边的小哥我之前好像在你们部落里也见过，这么急匆匆的样子，干什么去了？
[character(name="avg_npc_165", offsetX="100", offsetY="50")]
[name="巴塞尔"]呼......呼......这鬼天气......
[name="巴塞尔"]我们回来了！刚才带着几个人一起去附近看了看，有不少可以捕猎采集的地方，我们过一会儿就先去收集资源吧。
[name="巴塞尔"]还有什么事需要我去做吗？
[Decision(option1="暂时没有了。", value1="7.1")]
[predicate(references="7.1")]
[Decision(option1="我们在听这位联络员讲黑市的事。", value1="8.1")]
[predicate(references="8.1")]
[character(name="avg_npc_165", offsetX="100", offsetY="50")]
[name="巴塞尔"]黑市......我们在来的时候好像注意过那个地方。
[name="巴塞尔"]如果只是单纯地在这里生活一阵，我们之前倒已经做了一些准备——这片土地虽然有些贫瘠，但暂时养活我们，还没什么问题。
[name="巴塞尔"]但这里毕竟还是萨尔贡，征税队发现我们，只是早晚的问题，我们现在根本没有钱去交税......
[name="巴塞尔"]......出于更长远的考虑，黑市，确实是一个选择。
[character(name="avg_npc_803_1", offsetX="100", offsetY="100")]
[name="联络员"]对，这就是我刚刚说的了！各位，不论是想花钱买想要的东西，还是想要快速地挣钱，黑市都是一个好去处。
[name="联络员"]只要各位愿意，找一位雇主接下几个单子，或者是帮他们送送东西，报酬够各位这样的部落好好生活一阵子了。
[name="联络员"]特别是——
[name="联络员"]（小声）要是能得到黑市背后某位的支持......
[name="联络员"]那位掌控着整个黑市的人名叫“沙卒”，我对他慕名已久，可惜自己只是一个小小的联络员......
[Decision(option1="黑市......谢谢你告诉我们。", value1="9.1", option2="好，我们这就去！", value2="9.2")]
[predicate(references="9.1")]
[character(name="avg_npc_803_1", offsetX="100", offsetY="100")]
[name="联络员"]各位是我的合作者，这点小忙不算什么。
[name="联络员"]你们刚到这里，却被我一直拉着说话，真是过意不去。各位请先在这里安顿下来，我那时再来打扰吧！
[name="联络员"]别忘了，黑市就在各位驻扎地的西北处，而且，敝司在那里也有点小生意，各位也要多多光顾我们太阳谷啊！
[SetConditionProgress(conditionKey="route_main", itemCount="1")]
[withdraw(charId="trap_415_trademan")]
[End]
[predicate(references="9.2")]
[character(name="avg_npc_803_1", offsetX="100", offsetY="100")]
[name="联络员"]欸，请再稍等一下！不来看看敝司的新产品吗？价格十分优惠！比如这个——
[name="联络员"]欸，真走了？
[name="联络员"]那、那——别忘了黑市在各位驻扎地的西北处，敝司在那里也有点小生意——祝各位今天一切顺利！
[SetConditionProgress(conditionKey="route_main", itemCount="1")]
[withdraw(charId="trap_415_trademan")]
[End]

```

### dialog_sandbox_0_main_2_click

```
[HEADER(actId="act1sandbox", npcId="trap_432_oldisin")] 
[character(name="avg_npc_173", offsetX="100", offsetY="100")]
[name="老伊辛"]......
[name="老伊辛"]喔......少见的人，少见的人。老伊辛看到了一簇新生的火......
[name="老伊辛"]你们是否也听到了什么吸引人的话语，指引你们来到了这里......？
[character(name="avg_npc_165", offsetX="100", offsetY="50")]
[name="巴塞尔"]......这人好奇怪，他是在和我们说话吗？
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name=""]还是先看看那些商人们吧，或许他们能有对我们部落有用的信息。
[character(name="avg_npc_007", offsetX="100", offsetY="100")]
[name="黑市商人A"]这些是莱塔尼亚那边的施术单元，经过了哥伦比亚商人的改造，非常好用！
[name="黑市商人A"]您不如来看看这些？黑钢的源石制武器——
[character(name="avg_npc_008", offsetX="100", offsetY="100")]
[name="黑市商人B"]......这点赤金看起来可不太够吧，可别用你私炼的东西糊弄我啊。
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name=""]这里就是那个联络员所说的黑市。
[name=""]如果能找到“沙卒”并接到什么单子，或许我们的发展就会简单许多。
[name=""]先四处问问看吧。
[character(name="avg_npc_007", offsetX="100", offsetY="100")]
[name="黑市商人A"]（......那边好像来了几个新人。）
[character(name="avg_npc_008", offsetX="100", offsetY="100")]
[name="黑市商人B"]（新来的？还是谁又安排了点人进来？等等，我试探下，别又是什么“独角”或“漆黑的蝎子”插进来的眼线，我可不想再损失好几个人。）
[name="黑市商人B"]喂！
[Decision(option1="一块有花纹的铁牌？怎么冲我们丢这个？", value1="1.1", option2="怎么拿垃圾砸人！", value2="1.2")]
[predicate(references="1.1")]
[character(name="avg_npc_008", offsetX="100", offsetY="100")]
[name="黑市商人B"]（不像装的，看起来是真的不认识这东西......还真是新来的。）
[name="黑市商人B"]......不好意思啊，几位，我的东西。失手了。
[name="黑市商人B"]这样，几位要不来我这看看？都是好东西，看上什么了我就给几位多便宜几个金币。
[Decision(option1="要是想找“沙卒”，你们知道些什么吗？", value1="2.1", option2="我们没钱，想挣钱，你们老大在哪里？", value2="2.2")]
[predicate(references="2.1")]
[character(name="avg_npc_008", offsetX="100", offsetY="100")]
[name="黑市商人B"]“沙卒”？......
[character(name="avg_npc_007", offsetX="100", offsetY="100")]
[name="黑市商人A"]新来的，就算是买卖，也是要等价交换的。就你们现在身上这些，就算是王酋大人来了，我也没什么可说的。
[name="黑市商人A"]走远些吧！
[character(name="avg_npc_165", offsetX="100", offsetY="50")]
[name="巴塞尔"]你们！
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name=""]这里的人看起来不太好惹的样子，我们势单力薄，还是去别处再问问看吧。
[name=""]......
[name=""]在这里兜兜转转许久，但什么都没打听到。
[character(name="avg_npc_165", offsetX="100", offsetY="50")]
[name="巴塞尔"]似乎黑市的人们很看不起我们。
[name="巴塞尔"]我们现在既不具备和他们做生意的能力，也没有足够让他们为我们做事的实力。
[name="巴塞尔"]不过，刚刚那个奇怪的斗篷人靠过来了......
[Decision(option1="这个乞丐一样的人居然能和他们相安无事。", value1="3.1")]
[predicate(references="3.1")]
[Decision(option1="他肯定有点什么吧。", value1="4.1")]
[predicate(references="4.1")]
[character(name="avg_npc_173", offsetX="100", offsetY="100")]
[name="老伊辛"]......
[name="老伊辛"]老伊辛看到了......勇敢的年轻人踏入这片黄沙，他们大部分会被风沙掩埋，老伊辛见过很多。
[name="老伊辛"]你们想在沙暴中找到一棵足以依靠的巨木，但一味的热情并不能为你们带来什么，你们现在需要做的是在这里生存下来。
[name="老伊辛"]或许等到下次......你们能寻到沙暴中的那颗沙砾，“沙卒”会帮助你们。
[character(name="avg_npc_165", offsetX="100", offsetY="50")]
[name="巴塞尔"]这个人在说些什么......？“沙卒”？
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name=""]斗篷老人摇摇晃晃地离开了，看衣着，他应该是一名占卜师。
[name=""]虽然有些奇怪，但他似乎是这里唯一一个表现出善意的人。
[name=""]最重要的是，他知道有关“沙卒”的消息。
[character(name="avg_npc_165", offsetX="100", offsetY="50")]
[name="巴塞尔"]看来今天在这里是问不到什么了，我们先回去，做点最基础的准备吧。
[name="巴塞尔"]而且那位老人......或许他知道我们在寻找“沙卒”，用这个方式提供了信息。
[name="巴塞尔"]下次再遇到，我们好好问问他吧。
[SetConditionProgress(conditionKey="route_main", itemCount="2")]
[SetConditionProgress(conditionKey="route_main_interval", itemCount="0")]
[withdraw(charId="trap_432_oldisin")]
[End]
[predicate(references="2.2")]
[character(name="avg_npc_007", offsetX="100", offsetY="100")]
[name="黑市商人A"]......
[name="黑市商人A"]（这么直接？他们是来干什么的？）
[character(name="avg_npc_008", offsetX="100", offsetY="100")]
[name="黑市商人B"]（没见过这几个，试下来感觉什么都不知道，等等看吧，他们会自己倒霉的。）
[character(name="avg_npc_165", offsetX="100", offsetY="50")]
[name="巴塞尔"]我们好像问得太直接了，他们不想回答，都走开了......
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name=""]这里的人看起来不太好惹的样子，我们势单力薄，还是去别处再问问看吧。
[name=""]......
[name=""]在这里兜兜转转许久，但什么都没打听到。
[character(name="avg_npc_165", offsetX="100", offsetY="50")]
[name="巴塞尔"]似乎黑市的人们很看不起我们。
[name="巴塞尔"]我们现在既不具备和他们做生意的能力，也没有足够让他们为我们做事的实力。
[name="巴塞尔"]不过，刚刚那个奇怪的斗篷人靠过来了......
[Decision(option1="这个乞丐一样的人居然能和他们相安无事。", value1="5.1")]
[predicate(references="5.1")]
[Decision(option1="他肯定有点什么吧。", value1="6.1")]
[predicate(references="6.1")]
[character(name="avg_npc_173", offsetX="100", offsetY="100")]
[name="老伊辛"]......
[name="老伊辛"]老伊辛看到了......勇敢的年轻人踏入这片黄沙，他们大部分会被风沙掩埋，老伊辛见过很多。
[name="老伊辛"]你们想在沙暴中找到一棵足以依靠的巨木，但一味的热情并不能为你们带来什么，你们现在需要做的是在这里生存下来。
[name="老伊辛"]或许等到下次......你们能寻到沙暴中的那颗沙砾，“沙卒”会帮助你们。
[character(name="avg_npc_165", offsetX="100", offsetY="50")]
[name="巴塞尔"]这个人在说些什么......？“沙卒”？
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name=""]斗篷老人摇摇晃晃地离开了，看衣着，他应该是一名占卜师。
[name=""]虽然有些奇怪，但他似乎是这里唯一一个表现出善意的人。
[name=""]最重要的是，他知道有关“沙卒”的消息。
[character(name="avg_npc_165", offsetX="100", offsetY="50")]
[name="巴塞尔"]看来今天在这里是问不到什么了，我们先回去，做点最基础的准备吧。
[name="巴塞尔"]而且那位老人......或许他知道我们在寻找“沙卒”，用这个方式提供了信息。
[name="巴塞尔"]下次再遇到，我们好好问问他吧。
[SetConditionProgress(conditionKey="route_main", itemCount="2")]
[SetConditionProgress(conditionKey="route_main_interval", itemCount="0")]
[withdraw(charId="trap_432_oldisin")]
[End]
[predicate(references="1.2")]
[character(name="avg_npc_008", offsetX="100", offsetY="100")]
[name="黑市商人B"]（不像装的，看起来是真的不认识这东西......还真是新来的。）
[name="黑市商人B"]......不好意思啊，几位，我的东西。失手了。
[name="黑市商人B"]这样，几位要不来我这看看？都是好东西，看上什么了我就给几位多便宜几个金币。
[Decision(option1="要是想找“沙卒”，你们知道些什么吗？", value1="7.1", option2="我们没钱，想挣钱，你们老大在哪里？", value2="7.2")]
[predicate(references="7.1")]
[character(name="avg_npc_008", offsetX="100", offsetY="100")]
[name="黑市商人B"]“沙卒”？......
[character(name="avg_npc_007", offsetX="100", offsetY="100")]
[name="黑市商人A"]新来的，就算是买卖，也是要等价交换的。就你们现在身上这些，就算是王酋大人来了，我也没什么可说的。
[name="黑市商人A"]走远些吧！
[character(name="avg_npc_165", offsetX="100", offsetY="50")]
[name="巴塞尔"]你们！
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name=""]这里的人看起来不太好惹的样子，我们势单力薄，还是去别处再问问看吧。
[name=""]......
[name=""]在这里兜兜转转许久，但什么都没打听到。
[character(name="avg_npc_165", offsetX="100", offsetY="50")]
[name="巴塞尔"]似乎黑市的人们很看不起我们。
[name="巴塞尔"]我们现在既不具备和他们做生意的能力，也没有足够让他们为我们做事的实力。
[name="巴塞尔"]不过，刚刚那个奇怪的斗篷人靠过来了......
[Decision(option1="这个乞丐一样的人居然能和他们相安无事。", value1="8.1")]
[predicate(references="8.

... (全文8688字符)
```

### dialog_sandbox_0_main_3_click

```
[HEADER(actId="act1sandbox", npcId="trap_432_oldisin")] 
[character(name="avg_npc_173", offsetX="100", offsetY="100")]
[name="老伊辛"]唔......老伊辛一直在寻找一个能用生机盖过黄沙的人。
[name="老伊辛"]老伊辛看到，你们已经用双手建立起了一个家园的雏形啦......
[character(name="avg_npc_070", offsetX="125", offsetY="100")]
[name="部族人A"]我们加油干！有了这些物资，我们就能再建一个厨房！说不定真的能在这里好好生活下去！
[character(name="avg_npc_071", offsetX="100", offsetY="100")]
[name="部族人B"]干活......干活......我昨天一整天都在打猎......我们捕猎的效率还是太低了！
[name="部族人B"]我昨天还不小心摔到矿坑里去了！
[character(name="avg_npc_070", offsetX="125", offsetY="100")]
[name="部族人A"]别丧气！大家鼓起劲来，这里还等着我们呢！
[character(name="avg_npc_165", offsetX="100", offsetY="50")]
[name="巴塞尔"]嘿——哈！嘿——哈！运完这批矿，再运下一批，美好的明天在招手了！
[Decision(option1="（一同欢呼）", value1="1.1")]
[predicate(references="1.1")]
[character(name="avg_npc_173", offsetX="100", offsetY="100")]
[name="老伊辛"]过去的事让老伊辛清楚，一支涓流能浸润一小片青草，但最终只会被沙海吞下......
[name="老伊辛"]涓流需要汇集更多的力量。
[name="老伊辛"]你们需要研究，需要学习......一时的果腹不能带来长久的繁荣，智慧才是能够长久留存的事物。
[name="老伊辛"]老伊辛会给你们提供更多的力量。
[Decision(option1="（接过物资）", value1="2.1")]
[predicate(references="2.1")]
[AddItem(itemId="sandbox_0_wood", itemCount="15")]
[AddItem(itemId="sandbox_0_stone", itemCount="5")]
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name=""]【获得了15个木材、5个石材】
[character(name="avg_npc_165", offsetX="100", offsetY="50")]
[name="巴塞尔"]我们只要按照这个势头继续发展下去，再大的困难也不算什么了！
[name="巴塞尔"]还有这位老人，真的十分感谢您提供这些东西。对我们很有帮助！
[character(name="avg_npc_173", offsetX="100", offsetY="100")]
[name="老伊辛"]一切都应当从最基础的开始做起......
[Decision(option1="（表达感谢）", value1="3.1")]
[predicate(references="3.1")]
[character(name="avg_npc_173", offsetX="100", offsetY="100")]
[name="老伊辛"]你们的感谢老伊辛会收下，但老伊辛不需要酬劳。
[name="老伊辛"]老伊辛过来，只是为了消息的传递。
[name="老伊辛"]“沙卒”......是的，“沙卒”希望你们能够在此处立足。危机即将到来，你们需要一把......锋利的宝刀。
[character(name="avg_npc_165", offsetX="100", offsetY="50")]
[name="巴塞尔"]“锋利的宝刀”......？
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name=""]这个老人果然知道什么！
[name=""]“沙卒”......我们还从未见过这个人，但他似乎对我们这里发生的任何事情都了如指掌。
[name=""]最重要的是，他现在表现出的态度是善意的。
[name=""]或许我们可以尝试一下，在这里拥有一个靠山，对我们的发展没有任何坏处。
[SetConditionProgress(conditionKey="route_main", itemCount="3")]
[SetConditionProgress(conditionKey="route_main_interval", itemCount="0")]
[withdraw(charId="trap_432_oldisin")]
[End]

```

### dialog_sandbox_0_main_4_click

```
[HEADER(actId="act1sandbox", npcId="trap_415_trademan")] 
[character(name="avg_npc_803_1", offsetX="100", offsetY="100")]
[name="联络员"]喂！喂！各位怎么还在这里愣神？！
[name="联络员"]你们新开垦的地挤占了王酋领地上的小溪，王酋大人很不满意，现在派人过来打你们了！
[name="联络员"]你们问我怎么知道？
[name="联络员"]上个月就有两位王酋大人因为划分领地出了分歧，两方属下打了三天三夜，最后连分界线上一棵果树的果子都分得清清楚楚。
[name="联络员"]而且你们......也还没有给王酋大人交过税吧？他们当然要过来找个说法了！
[Decision(option1="只能打了吗？不能再商量商量吗？", value1="1.1", option2="这，小溪难道不是公共资源吗？", value2="1.2")]
[predicate(references="1.1")]
[character(name="avg_npc_803_1", offsetX="100", offsetY="100")]
[name="联络员"]现在说这些还有什么用啊？他们就要打过来了！虽然过来可能还需要一些时间......
[name="联络员"]我可是一知道这个消息就赶过来告知各位了，各位可千万要重视起来才行！前几天还有一个小部落因为发展不下去被吞并。
[name="联络员"]你们要有足够的钱和资源，才能在这里站稳脚跟。比如，我这里正好有能帮上各位忙的好东西——瞧瞧它！
[name="联络员"]这可是太阳谷工业最新......
[Decision(option1="（打断他）", value1="2.1")]
[predicate(references="2.1")]
[character(name="avg_npc_803_1", offsetX="100", offsetY="100")]
[name="联络员"]这、这样啊......
[name="联络员"]看来还是我们太阳谷的商品没有满足各位的需求了......
[name="联络员"]不过，既然选择来萨尔贡发展，想必各位之前对这种情况也不是没有准备吧？现在最要紧的还是在他们过来之前，起码建几个防御建筑！
[name="联络员"]而且我也听说过，沁礁黑市曾经售卖过一些能跨地块的联络基站，有了它，各位可以联络到这个地块之外的佣兵寻求援助，直接逃跑！
[name="联络员"]不仅如此，还能带走不少钱财！留得黄沙在，不怕没坑挖嘛！
[Decision(option1="明白了，我们会好好准备的！", value1="3.1", option2="是可以跑的吗？", value2="3.2")]
[predicate(references="3.1")]
[character(name="avg_npc_803_1", offsetX="100", offsetY="100")]
[name="联络员"]那我们就不要在这里聊天了，各位快去做准备吧！我一定会以十二万分的精神，为各位祈祷获得胜利的！
[character(name="avg_npc_803_1", offsetX="100", offsetY="100")]
[name="联络员"]总之，各位先好好加固一下他们打过来时要经过的各个区块，升级技术也是发展的必经之路，还有，要多造些建筑......
[character(name="avg_npc_165", offsetX="100", offsetY="50")]
[name="巴塞尔"]我大致明白了。我这就去组织大家清点各类物资，部落里的其他人都会对这次的袭击做好准备的。
[name="巴塞尔"]没想到在这里也逃不开这样的事情，不过，以我之前的经验，我们应该是可以成功抵挡的。
[name="巴塞尔"]等结束后，我们再一起商量一下以后应当怎么做吧。
[Decision(option1="还有交税的事情......", value1="4.1")]
[predicate(references="4.1")]
[character(name="avg_npc_165", offsetX="100", offsetY="50")]
[name="巴塞尔"]看来我们也需要为这个做准备了，不知道需要交多少呢......
[character(name="avg_npc_803_1", offsetX="100", offsetY="100")]
[name="联络员"]各位，毕竟打仗可不是闹着玩的，要是需要敝司的商品作为帮助，也一定不要吝惜钱财！
[name="联络员"]你们可一定要挺过来啊！
[character(name="avg_npc_173", offsetX="100", offsetY="100")]
[name="老伊辛"]老伊辛看到了你们的勇敢......年轻而有活力的部族正在这片黄沙上成长起来。
[name="老伊辛"]你们能够经受住这一切的。
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name=""]嗯？这位老人什么时候来的？
[character(name="avg_npc_173", offsetX="100", offsetY="100")]
[name="老伊辛"]你们在想些什么？老伊辛看不出来，老伊辛只是来兑现自己之前的承诺。
[name="老伊辛"]沙暴无法吹倒的树苗只会长出更加遒劲的根系，会汇集更多的水源。
[name="老伊辛"]请来黑市吧，带着胜利，“沙卒”会想要见见你们的。
[Decision(option1="这里真的适合我们生活吗......？", value1="5.1", option2="我们绝对不会轻易被欺负！", value2="5.2")]
[predicate(references="5.1")]
[character(name="avg_npc_173", offsetX="100", offsetY="100")]
[name="老伊辛"]唔......老伊辛无权干涉你们的决定。
[name="老伊辛"]你们会得到自己的答案。
[SetConditionProgress(conditionKey="route_main", itemCount="4")]
[withdraw(charId="trap_415_trademan")]
[End]
[predicate(references="5.2")]
[character(name="avg_npc_173", offsetX="100", offsetY="100")]
[name="老伊辛"]......老伊辛没有看错。
[name="老伊辛"]请收下这个吧。它能帮助你们看清那黄沙中未知的未来......
[Decision(option1="（接过）", value1="6.1")]
[predicate(references="6.1")]
[AddItem(itemId="sandbox_0_craft_6", itemCount="1")]
[SetConditionProgress(conditionKey="market_isin", itemCount="1")]
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name=""]【获得了跨局信物<命运的水晶球>】
[character(name="avg_npc_173", offsetX="100", offsetY="100")]
[name="老伊辛"]......祝各位一切顺利。
[SetConditionProgress(conditionKey="route_main", itemCount="5")]
[withdraw(charId="trap_415_trademan")]
[End]
[predicate(references="3.2")]
[character(name="avg_npc_803_1", offsetX="100", offsetY="100")]
[name="联络员"]当然！不然各位以为我是如何做生......
[name="联络员"]如何发展的！
[name="联络员"]必要的时候权衡利弊，多给自己留一条路，才是生存的硬道理啊......
[character(name="avg_npc_803_1", offsetX="100", offsetY="100")]
[name="联络员"]总之，各位先好好加固一下他们打过来时要经过的各个区块，升级技术也是发展的必经之路，还有，要多造些建筑......
[character(name="avg_npc_165", offsetX="100", offsetY="50")]
[name="巴塞尔"]我大致明白了。我这就去组织大家清点各类物资，部落里的其他人都会对这次的袭击做好准备的。
[name="巴塞尔"]没想到在这里也逃不开这样的事情，不过，以我之前的经验，我们应该是可以成功抵挡的。
[name="巴塞尔"]等结束后，我们再一起商量一下以后应当怎么做吧。
[Decision(option1="还有交税的事情......", value1="7.1")]
[predicate(references="7.1")]
[character(name="avg_npc_165", offsetX="100", offsetY="50")]
[name="巴塞尔"]看来我们也需要为这个做准备了，不知道需要交多少呢......
[character(name="avg_npc_803_1", offsetX="100", offsetY="100")]
[name="联络员"]各位，毕竟打仗可不是闹着玩的，要是需要敝司的商品作为帮助，也一定不要吝惜钱财！
[name="联络员"]你们可一定要挺过来啊！
[character(name="avg_npc_173", offsetX="100", offsetY="100")]
[name="老伊辛"]老伊辛看到了你们的勇敢......年轻而有活力的部族正在这片黄沙上成长起来。
[name="老伊辛"]你们能够经受住这一切的。
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name=""]嗯？这位老人什么时候来的？
[character(name="avg_npc_173", offsetX="100", offsetY="100")]
[name="老伊辛"]你们在想些什么？老伊辛看不出来，老伊辛只是来兑现自己之前的承诺。
[name="老伊辛"]沙暴无法吹倒的树苗只会长出更加遒劲的根系，会汇集更多的水源。
[name="老伊辛"]请来黑市吧，带着胜利，“沙卒”会想要见见你们的。
[Decision(option1="这里真的适合我们生活吗......？", value1="8.1", option2="我们绝对不会轻易被欺负！", value2="8.2")]
[predicate(references="8.1")]
[character(name="avg_npc_173", offsetX="100", offsetY="100")]
[name="老伊辛"]唔......老伊辛无权干涉你们的决定。
[name="老伊辛"]你们会得到自己的答案。
[SetConditionProgress(conditionKey="route_main", itemCount="4")]
[withdraw(charId="trap_415_trademan")]
[End]
[predicate(references="8.2")]
[character(name="avg_npc_173", offsetX="100", offsetY="100")]
[name="老伊辛"]......老伊辛没有看错。
[name="老伊辛"]请收下这个吧。它能帮助你们看清那黄沙中未知的未来......
[Decision(option1="（接过）", value1="9.1")]
[predicate(references="9.1")]
[AddItem(itemId="sandbox_0_craft_6", itemCount="1")]
[SetConditionProgress(conditionKey="market_isin", itemCount="1")]
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name=""]【获得了跨局信物<命运的水晶球>】
[character(name="avg_npc_173", offsetX="100", offsetY="100")]
[name="老伊辛"]......祝各位一切顺利。
[SetConditionProgress(conditionKey="route_main", itemCount="5")]
[withdraw(charId="trap_415_trademan")]
[End]
[predicate(references="1.2")]
[character(name="avg_npc_803_1", offsetX="100", offsetY="100")]
[name="联络员"]现在说这些还有什么用啊？他们就要打过来了！虽然过来可能还需要一些时间......
[name="联络员"]我可是一知道这个消息就赶过来告知各位了，各位可千万要重视起来才行！前几天还有一个小部落因为发展不下去被吞并。
[name="联络员"]你们要有足够的钱和资源，才能在这里站稳脚跟。比如，我这里正好有能帮上各位忙的好东西——瞧瞧它！
[name="联络员"]这可是太阳谷工业最新......
[Decision

... (全文10963字符)
```

### dialog_sandbox_0_main_5_click

```
[HEADER(actId="act1sandbox", npcId="trap_433_sandsdr")] 
[character(name="avg_npc_801_1", offsetX="100", offsetY="100")]
[name="“沙卒”"]各位就是老伊辛口中的那个部落吧？
[name="“沙卒”"]能为各位提供帮助，是我的荣幸。
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name=""]竟然......这么轻易地就见到了“沙卒”本人？
[name=""]那位老人看来真的没有骗我们。
[name=""]只是，就这样见到了黑市的幕后人，还是有些......
[character(name="avg_npc_801_1", offsetX="100", offsetY="100")]
[name="“沙卒”"]啊，不用紧张。沁礁黑市只是一个能够为各位提供物资渠道的地方，我也只是一个生意人。
[name="“沙卒”"]各位付出金钱，得到帮助，而我也能从其中得到一部分的利益。
[name="“沙卒”"]这就是我很乐意与各位接触的原因——我与各位，有很多交易可做。
[name="“沙卒”"]各位也不需要着急，这只不过是我们第一次见面。
[Decision(option1="（收下）", value1="1.1")]
[predicate(references="1.1")]
[AddItem(itemId="sandbox_0_building_8", itemCount="4")]
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name=""]【获得了4个都市风壁障Ⅰ】
[character(name="avg_npc_801_1", offsetX="100", offsetY="100")]
[name="“沙卒”"]——只是见面礼罢了。
[name="“沙卒”"]不过各位看起来，似乎还有什么想问？
[name="“沙卒”"]请尽管问吧，我不希望给各位留有太多的疑惑。
[Decision(option1="您为什么选了我们？", value1="2.1")]
[predicate(references="2.1")]
[character(name="avg_npc_801_1", offsetX="100", offsetY="100")]
[name="“沙卒”"]......很直接的提问。
[name="“沙卒”"]如果我说，是很早就盯上了你们呢？
[name="“沙卒”"]......
[name="“沙卒”"]我看到各位之中已经有人紧张了起来——把武器放下吧，你们还没有能在这里与我发生冲突的资本。
[name="“沙卒”"]沁礁黑市，自然是为了生意。
[name="“沙卒”"]一个能在黄沙中立足的部落，当然值得我的注意——我能看到各位在以后能为我带来的利益。
[name="“沙卒”"]这样的回答，各位满意吗？
[Decision(option1="满意。", value1="3.1", option2="不满意。", value2="3.2")]
[predicate(references="3.1")]
[character(name="avg_npc_801_1", offsetX="100", offsetY="100")]
[name="“沙卒”"]那，祝我们合作愉快。
[character(name="avg_npc_801_1", offsetX="100", offsetY="100")]
[name="“沙卒”"]来吧，趁我还有些时间，告诉我，各位回去后要做的事，已经有目标了吗？
[name="“沙卒”"]以及在此之前，我还想再提供一条小小的情报......
[name="“沙卒”"]王酋大人对发生在他土地上的一切事情都无比感兴趣，各位也不例外，那条小溪就是最好的证明。
[name="“沙卒”"]这和我的个人利益无关，只是一个对要在这里生活的人们的善意劝告。
[SetConditionProgress(conditionKey="route_main", itemCount="6")]
[withdraw(charId="trap_433_sandsdr")]
[End]
[predicate(references="3.2")]
[character(name="avg_npc_801_1", offsetX="100", offsetY="100")]
[name="“沙卒”"]唔。
[name="“沙卒”"]只是一个新生的部落而已，各位这样我倒是有些感兴趣了。
[name="“沙卒”"]虽然你们的人数并不多，但生命总是珍贵的。除此之外，你们还有什么可以作为与我交易的筹码？
[Decision(option1="不甘心。", value1="4.1")]
[predicate(references="4.1")]
[character(name="avg_npc_801_1", offsetX="100", offsetY="100")]
[name="“沙卒”"]只是一个刚刚在此安定下来的部落，只为了一条小溪旁的贫瘠土地，你们就遭到了王酋的警告......
[name="“沙卒”"]为此而不甘心啊。
[name="“沙卒”"]作为第一次见面的自我介绍，各位已经做得很好了。
[name="“沙卒”"]那么，我很乐意为各位提供帮助。
[character(name="avg_npc_801_1", offsetX="100", offsetY="100")]
[name="“沙卒”"]来吧，趁我还有些时间，告诉我，各位回去后要做的事，已经有目标了吗？
[name="“沙卒”"]以及在此之前，我还想再提供一条小小的情报......
[name="“沙卒”"]王酋大人对发生在他土地上的一切事情都无比感兴趣，各位也不例外，那条小溪就是最好的证明。
[name="“沙卒”"]这和我的个人利益无关，只是一个对要在这里生活的人们的善意劝告。
[SetConditionProgress(conditionKey="route_main", itemCount="6")]
[withdraw(charId="trap_433_sandsdr")]
[End]

```

### dialog_sandbox_0_main_6_appear

```
[HEADER(actId="act1sandbox", npcId="trap_433_sandsdr")] 
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name="？？？"]......灰飞烟灭吧。
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name=""]我们明明听从了“沙卒”的建议，有意避开了王酋大人的势力发展。
[name=""]但即便如此，王酋的卫队还是找上了我们。
[name=""]我们被迫拿起武器，对此作出反应，只希望这次结束后，部落的生活能回到之前的状态。
[character(name="avg_npc_165", offsetX="100", offsetY="50")]
[name="巴塞尔"]看那边！那边似乎已经有人和王酋的卫队打起来了......?
[name="巴塞尔"]不是我们部落的人，还有人和他们在这附近起了冲突吗？
[name="巴塞尔"]太远了，有些看不清......
[End]

```

### dialog_sandbox_0_main_6_click

```
[HEADER(actId="act1sandbox", npcId="trap_433_sandsdr")] 
[character(name="avg_npc_801_1", offsetX="100", offsetY="100")]
[name="“沙卒”"]唔。
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name=""]......“沙卒”？他为什么在这里？
[character(name="avg_npc_801_1", offsetX="100", offsetY="100")]
[name="“沙卒”"]啊，是你们。
[name="“沙卒”"]别紧张，只是一些王酋雇下的军士，而我有些在意之前的某一笔交易。
[name="“沙卒”"]我很感谢各位的帮助。能与这样一支队伍抗争并且获得胜利，各位的实力不错。
[name="“沙卒”"]不过我有些好奇，各位在迈出这一步之前，是否真的清楚刚才那些人背后的势力？
[Decision(option1="我们知道那是王酋的卫队。", value1="1.1", option2="还不是很清楚......", value2="1.2")]
[predicate(references="1.1")]
[character(name="avg_npc_801_1", offsetX="100", offsetY="100")]
[name="“沙卒”"]啊，那各位真的是十分勇敢。
[name="“沙卒”"]这支小队由伊巴特的现任王酋所指挥。各位今天只是暂时地延缓了他查看这方土地的脚步，并没有将他们彻底击败。
[name="“沙卒”"]别紧张，战场混乱，他们只会以为各位是我带来的增援。
[name="“沙卒”"]至于我，他们并不会知道是谁。
[name="“沙卒”"]不过，仍旧有一些事情需要各位清楚。
[name="“沙卒”"]各位作为最近在伊巴特崭露头角的部族势力，虽然实力足以挫败一支王酋军，但你们还没有学会遮掩锋芒，隐藏目的。你们已然吸引了王酋的目光。
[name="“沙卒”"]如果各位觉得自身实力已经足够，又想要和王酋抗衡......
[name="“沙卒”"]或许，我们可以聊聊。
[Decision(option1="我们不想再时时低头了。", value1="2.1", option2="直接和王酋宣战？我们为什么要这么做？", value2="2.2")]
[predicate(references="2.1")]
[character(name="avg_npc_801_1", offsetX="100", offsetY="100")]
[name="“沙卒”"]有勇气的选择。
[name="“沙卒”"]我会在沁礁黑市等待各位。
[SetConditionProgress(conditionKey="route_main", itemCount="7")]
[withdraw(charId="trap_433_sandsdr")]
[End]
[predicate(references="2.2")]
[character(name="avg_npc_801_1", offsetX="100", offsetY="100")]
[name="“沙卒”"]......
[name="“沙卒”"]自然，你们不需要做到这一步......
[name="“沙卒”"]但你们不必辜负你们今日应得的喜悦。
[name="“沙卒”"]一支新生的力量能够击败王酋的行军，你们为什么不返回部落，共同为此庆祝？
[character(name="avg_npc_165", offsetX="100", offsetY="50")]
[name="巴塞尔"]呼......呼......感谢您！
[name="巴塞尔"]我们太需要一次庆祝了......
[SetConditionProgress(conditionKey="route_main", itemCount="7")]
[withdraw(charId="trap_433_sandsdr")]
[End]
[predicate(references="1.2")]
[character(name="avg_npc_801_1", offsetX="100", offsetY="100")]
[name="“沙卒”"]啊，那各位真的是十分勇敢。
[name="“沙卒”"]这支小队由伊巴特的现任王酋所指挥。各位今天只是暂时地延缓了他查看这方土地的脚步，并没有将他们彻底击败。
[name="“沙卒”"]别紧张，战场混乱，他们只会以为各位是我带来的增援。
[name="“沙卒”"]至于我，他们并不会知道是谁。
[name="“沙卒”"]不过，仍旧有一些事情需要各位清楚。
[name="“沙卒”"]各位作为最近在伊巴特崭露头角的部族势力，虽然实力足以挫败一支王酋军，但你们还没有学会遮掩锋芒，隐藏目的。你们已然吸引了王酋的目光。
[name="“沙卒”"]如果各位觉得自身实力已经足够，又想要和王酋抗衡......
[name="“沙卒”"]或许，我们可以聊聊。
[Decision(option1="我们不想再时时低头了。", value1="3.1", option2="直接和王酋宣战？我们为什么要这么做？", value2="3.2")]
[predicate(references="3.1")]
[character(name="avg_npc_801_1", offsetX="100", offsetY="100")]
[name="“沙卒”"]有勇气的选择。
[name="“沙卒”"]我会在沁礁黑市等待各位。
[SetConditionProgress(conditionKey="route_main", itemCount="7")]
[withdraw(charId="trap_433_sandsdr")]
[End]
[predicate(references="3.2")]
[character(name="avg_npc_801_1", offsetX="100", offsetY="100")]
[name="“沙卒”"]......
[name="“沙卒”"]自然，你们不需要做到这一步......
[name="“沙卒”"]但你们不必辜负你们今日应得的喜悦。
[name="“沙卒”"]一支新生的力量能够击败王酋的行军，你们为什么不返回部落，共同为此庆祝？
[character(name="avg_npc_165", offsetX="100", offsetY="50")]
[name="巴塞尔"]呼......呼......感谢您！
[name="巴塞尔"]我们太需要一次庆祝了......
[SetConditionProgress(conditionKey="route_main", itemCount="7")]
[withdraw(charId="trap_433_sandsdr")]
[End]

```

### dialog_sandbox_0_main_7a_click

```
[HEADER(actId="act1sandbox", npcId="trap_432_oldisin")] 
[character(name="avg_npc_173", offsetX="100", offsetY="100")]
[name="老伊辛"]......
[name="老伊辛"]老伊辛做了一个梦......
[name="老伊辛"]......还是那个梦......
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name=""]按照和“沙卒”的约定，我们来到了沁礁黑市。
[name=""]但这里怎么只有老伊辛一个人？他好像在一个人嘟囔着什么，有些听不清。
[name=""]这才几天没见，他怎么看上去更加不妙了。
[Decision(option1="（上前询问情况）", value1="1.1")]
[predicate(references="1.1")]
[character(name="avg_npc_173", offsetX="100", offsetY="100")]
[name="老伊辛"]梦......老伊辛反复地做着同一个梦，百余年了......
[name="老伊辛"]老伊辛记得，黄沙之中的城市......移动时带起的金色沙砾，湛蓝的天空......帕夏大人在老伊辛耳边诉说......！
[name="老伊辛"]老伊辛还记得......
[name="老伊辛"]啊，现在只有那群、那群酒囊饭袋......！他们怎么可能重现......昔日的荣光？！
[character(name="avg_npc_165", offsetX="100", offsetY="50")]
[name="巴塞尔"]......
[name="巴塞尔"]他怎么看起来有点怪怪的，之前他是这样的吗？
[Decision(option1="（继续询问）", value1="2.1")]
[predicate(references="2.1")]
[character(name="avg_npc_173", offsetX="100", offsetY="100")]
[name="老伊辛"]只有那位帕夏，那些真正心怀荣光的人才能配得上这片土地......！
[name="老伊辛"]呜......只要找到......在那所宫殿里，我们就能齐聚在他的座下，听他描述那些未来......
[name="老伊辛"]我为何还在这里徘徊？我究竟浪费了多少时光？我何敢自称为他的下属？
[name="老伊辛"]老伊辛要去往......要去往那个......！
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name=""]他摇摇晃晃地离开了。那个方向是......？
[name=""]风将黄沙吹起，也扬起了老占卜师兜帽的一角。你看到了他正在流泪的脸。
[name=""]他在走向沙漠。
[SetConditionProgress(conditionKey="route_main", itemCount="8")]
[SetConditionProgress(conditionKey="route_main_a", itemCount="1")]
[withdraw(charId="trap_432_oldisin")]
[withdraw(charId="trap_434_klmantc")]
[End]

```

### dialog_sandbox_0_main_7b_click

```
[HEADER(actId="act1sandbox", npcId="trap_434_klmantc")] 
[character(name="avg_npc_802_1", offsetX="125", offsetY="100")]
[name="曼提柯杀手"]......
[name="曼提柯杀手"]你们......为什么还要来找我......？
[Decision(option1="部落里的人相信了你背叛了我们。", value1="1.1")]
[predicate(references="1.1")]
[Decision(option1="他们拆了你的屋子，东西都丢到了外面。", value1="2.1")]
[predicate(references="2.1")]
[Decision(option1="但“沙卒”说的情况和你说的完全相反。", value1="3.1")]
[predicate(references="3.1")]
[character(name="avg_npc_802_1", offsetX="125", offsetY="100")]
[name="曼提柯杀手"]......
[name="曼提柯杀手"]雇主，只会让杀手去做那些危险的任务......所以，信任是最重要的......我需要有价值，才能在那里留下来......
[name="曼提柯杀手"]我希望有人能注意到我......但是，不是那样的注意......
[name="曼提柯杀手"]一个杀手如果失去了信任，她就已经等于死了......我只是想，活下来......
[name="曼提柯杀手"]逃出去，我或许还能活，但是你们，还是找到了我......
[name="曼提柯杀手"]我不会做，任何......任何对你们部落不好的事情......！
[name="曼提柯杀手"]......我只是害怕......
[name="曼提柯杀手"]而且，“沙卒”确实看重你们......
[character(name="avg_npc_165", offsetX="100", offsetY="50")]
[name="巴塞尔"]......等等，你又想逃跑吗？你要去哪里？
[name="巴塞尔"]她去哪了？......她这个源石技艺怎么会这么好用......？！
[name="巴塞尔"]她从部落走的时候带上药了吗？啧！把事情好好地都解释清楚不就好了！部落之前都已经接纳她了......！
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name=""]如果只是害怕，我们已经表达出了善意和信任，为什么她还是要走？
[name=""]如果她确实背叛了我们部落，那刚才那些话为什么要和我们说？
[SetConditionProgress(conditionKey="route_main", itemCount="8")]
[SetConditionProgress(conditionKey="route_main_b", itemCount="1")]
[withdraw(charId="trap_434_klmantc")]
[withdraw(charId="trap_432_oldisin")]
[End]

```

### dialog_sandbox_0_main_8b_click

```
[HEADER(actId="act1sandbox", npcId="trap_433_sandsdr")] 
[character(name="avg_npc_801_1", offsetX="100", offsetY="100")]
[name="“沙卒”"]如果是当初我的帮助让各位与那位姑娘产生了一些误会，抱歉了。
[name="“沙卒”"]如果各位需要，她接下来的行踪消息我都可以提供给各位。
[name="“沙卒”"]以及，我很乐意拥有像各位这样的盟友。收下这个吧。
[Decision(option1="（收下）", value1="1.1")]
[predicate(references="1.1")]
[AddItem(itemId="sandbox_0_craft_9", itemCount="1")]
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name=""]【获得了跨局信物<黄沙钱币>】
[SetConditionProgress(conditionKey="market_sandsdr", itemCount="1")]
[character(name="avg_npc_801_1", offsetX="100", offsetY="100")]
[name="“沙卒”"]当然，这次合作并不是出于歉意。
[name="“沙卒”"]“不甘心”是大多人的常态，愿意迈出那一步的还是少数。
[name="“沙卒”"]各位不需要我再多说什么了，你们早就做好了准备。
[SetConditionProgress(conditionKey="route_main", itemCount="9")]
[SetConditionProgress(conditionKey="route_main_b", itemCount="2")]
[withdraw(charId="trap_433_sandsdr")]
[End]

```

### dialog_sandbox_0_main_9b_click

```
[HEADER(actId="act1sandbox", npcId="trap_433_sandsdr")] 
[character(name="avg_npc_801_1", offsetX="100", offsetY="100")]
[name="“沙卒”"]不过是几个之前骚扰你们的部落和佣兵小队，还不需要各位亲自来找到我道谢。
[name="“沙卒”"]虽然那些人的数量不多，但安静下来对大家都不是坏事。各位可是我的盟友。
[name="“沙卒”"]最近我还听到了不少有关之前那位姑娘的消息。杀手总是不缺任务的，她下一个目的地似乎是王酋的某个营地。
[name="“沙卒”"]唔......很凶险呢。
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name=""]曼提柯杀手上次离开后就再也没有回来，我们早已失去了有关她的各种消息。
[name=""]我们和“沙卒”的合作则十分顺利，部落中的生活风平浪静，一切都在稳定发展。
[name=""]带着与“沙卒”刚交换的情报，我们决定回到部落，规划接下来的方向。
[character(name="avg_npc_165", offsetX="100", offsetY="50")]
[name="巴塞尔"]......快回去！我们快点回去！
[name="巴塞尔"]王酋的人......袭击了我们的驻扎地！
[Decision(option1="发生了什么？！", value1="1.1")]
[predicate(references="1.1")]
[character(name="avg_npc_165", offsetX="100", offsetY="50")]
[name="巴塞尔"]上回我们不想把全部的钱都交出去当税金，王酋就派人袭击了我们的部落！那根本就不符合规定，我们根本不需要交出那么多！
[name="巴塞尔"]但这回不是警告了，王酋是想让我们从这里消失......！部落里已经......他们为了不让那群人烧了我们的屋子，为了保护那些孩子，已经......
[name="巴塞尔"]凭什么，我们的生命就这么轻贱？！
[name="巴塞尔"]我先回去......！我不能再等了！
[SetConditionProgress(conditionKey="route_main", itemCount="10")]
[SetConditionProgress(conditionKey="route_main_b", itemCount="3")]
[withdraw(charId="trap_433_sandsdr")]
[End]

```

### dialog_sandbox_0_main_sp11a_click

```
[HEADER(actId="act1sandbox", npcId="trap_435_trsrhuntr")] 
[character(name="avg_npc_805_1", offsetX="100", offsetY="100")]
[name="寻宝人"]我就知道，你们还是想要我这个专业人士的帮助的，对不对？
[name="寻宝人"]请各位相信，我一定能破解上面所写的信息！
[Decision(option1="只是偶然路过。", value1="1.1", option2="那还是拜托你了！", value2="1.2")]
[predicate(references="1.1")]
[character(name="avg_npc_805_1", offsetX="100", offsetY="100")]
[name="寻宝人"]唉......好吧。
[withdraw(charId="trap_435_trsrhuntr")]
[End]
[predicate(references="1.2")]
[character(name="avg_npc_805_1", offsetX="100", offsetY="100")]
[name="寻宝人"]太感谢了！我一定不会辜负各位的信任的！
[name="寻宝人"]过几天，我一定带着已经翻译好的信息再来找各位！
[SetConditionProgress(conditionKey="route_main", itemCount="13")]
[SetConditionProgress(conditionKey="route_main_a", itemCount="6")]
[withdraw(charId="trap_435_trsrhuntr")]
[End]

```

### dialog_sandbox_0_main_sp4_click

```
[HEADER(actId="act1sandbox", npcId="trap_432_oldisin")] 
[character(name="avg_npc_173", offsetX="100", offsetY="100")]
[name="老伊辛"]年轻人，纷争不会从这片黄沙上消失。
[name="老伊辛"]你们改换了自己的想法吗？
[Decision(option1="只是偶然路过。", value1="1.1", option2="我们会去沁礁黑市找“沙卒”的。", value2="1.2")]
[predicate(references="1.1")]
[character(name="avg_npc_173", offsetX="100", offsetY="100")]
[name="老伊辛"]可惜......
[withdraw(charId="trap_432_oldisin")]
[End]
[predicate(references="1.2")]
[character(name="avg_npc_173", offsetX="100", offsetY="100")]
[name="老伊辛"]老伊辛没有看错......
[name="老伊辛"]请收下这个吧。它能帮助你们看清那黄沙中未知的未来......
[Decision(option1="（接过）", value1="2.1")]
[predicate(references="2.1")]
[AddItem(itemId="sandbox_0_craft_6", itemCount="1")]
[SetConditionProgress(conditionKey="market_isin", itemCount="1")]
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name=""]【获得了跨局信物<命运的水晶球>】
[character(name="avg_npc_173", offsetX="100", offsetY="100")]
[name="老伊辛"]那么，祝各位顺利。
[SetConditionProgress(conditionKey="route_main", itemCount="5")]
[withdraw(charId="trap_432_oldisin")]
[End]

```

### dialog_sandbox_0_mantic_10_click

```
[HEADER(actId="act1sandbox", npcId="trap_433_sandsdr")] 
[character(name="avg_npc_801_1", offsetX="100", offsetY="100")]
[name="“沙卒”"]......任务......完成......？
[character(name="avg_npc_802_1", offsetX="125", offsetY="100")]
[name="曼提柯杀手"]......雇主......答谢......
[character(name="avg_npc_165", offsetX="100", offsetY="50")]
[name="巴塞尔"]追上了！就在前面......！呼......不管怎么样也要说清楚了再走......！
[name="巴塞尔"]前面那是......“沙卒”？
[name="巴塞尔"]什么意思？她为什么会去见“沙卒”？
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name=""]怎么会是“沙卒”？
[name=""]曼提柯杀手在部落这段日子，所有行动都在我们的安排之下，行动时间也从没出过错，她不该和“沙卒”有什么联系。
[name=""]究竟发生了什么？
[name=""]但这样贸然上去询问她为什么背叛，不会得到什么回答，我们需要换一种方式。
[Decision(option1="“沙卒”。", value1="1.1")]
[predicate(references="1.1")]
[character(name="avg_npc_802_1", offsetX="125", offsetY="100")]
[name="曼提柯杀手"]......嗬？！
[Decision(option1="我们很感激您之前对部落的帮助。", value1="2.1")]
[predicate(references="2.1")]
[Decision(option1="为了能更好地和您达成合作，", value1="3.1")]
[predicate(references="3.1")]
[Decision(option1="我们也付出了很多努力。", value1="4.1")]
[predicate(references="4.1")]
[Decision(option1="但如果是想通过这位杀手姑娘利用我们，", value1="5.1")]
[predicate(references="5.1")]
[Decision(option1="不如请直接说明。", value1="6.1")]
[predicate(references="6.1")]
[Decision(option1="我们相信自己有能力成为“沙卒”的盟友，", value1="7.1")]
[predicate(references="7.1")]
[Decision(option1="而不是一枚棋子。", value1="8.1")]
[predicate(references="8.1")]
[character(name="avg_npc_801_1", offsetX="100", offsetY="100")]
[name="“沙卒”"]啊，我想你们......应该是误会了什么。
[name="“沙卒”"]对于各位，我从来没有利用的想法。
[name="“沙卒”"]相反，我一直在帮助各位。
[name="“沙卒”"]之前你们能从王酋的手下那里连夜安全回到自己的部落，仅仅依靠几个每天打猎的猎手，和一位已经重伤的姑娘，难道一次都没有想过是为什么吗？
[name="“沙卒”"]......
[name="“沙卒”"]我总是愿意去帮助像各位这样的人——收下吧，会有用的。
[Decision(option1="(收下)", value1="9.1")]
[predicate(references="9.1")]
[AddItem(itemId="sandbox_0_craft_13", itemCount="1")]
[character(name="char_empty_b", offsetX="100", offsetY="100")]
[name=""]【获得了跨局信物<划线的名单>】
[character(name="avg_npc_801_1", offsetX="100", offsetY="100")]
[name="“沙卒”"]但......“盟友”？
[name="“沙卒”"]或许我们可以在沁礁好好谈一谈。
[name="“沙卒”"]这位姑娘的事情也一样。
[SetConditionProgress(conditionKey="route_klmantic", itemCount="10")]
[withdraw(charId="trap_433_sandsdr")]
[End]

```


> 本章节共94个脚本文件，此处展示前30个。

## 统计

- 总字符数：69623
- 对话行数：743


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
