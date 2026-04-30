# 明日方舟 · 主线/常驻 · rune（2段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 主线/常驻, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟主线/常驻「rune」完整剧情脚本（2个文件，35行对话）

## 正文
## 章节信息

- 分类：主线/常驻
- 目录：obt/rune
- 脚本文件数：2

### ui_rune_season_0_1_cc

```
[HEADER(key="title_test", is_skippable=false, fit_mode="BLACK_MASK")] 危机合约
[Dialog]
[delay(time=1)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Dialog]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.6, crossfade=1, delay=0.5)]
[Background(image="bg_rhodescom",screenadapt="coverall",fadetime=1,block=true)]
[delay(time=2, black=true)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Character(name="char_130_doberm_ex",fadetime=1,block=true)]
[delay(time=1)]
[name="杜宾"]   所有人都到了？
[Character(name="char_002_amiya_1#1")]
[name="阿米娅"]   嗯，各部门人员都到了，我们可以开始了。
[Character(name="char_130_doberm_ex")]
[name="杜宾"]   那么直接进入正题吧。普罗旺斯。
[Character]
[Dialog]
[Character(name="char_145_prove_1",fadetime=1,block=true)]
[delay(time=1)]
[name="普罗旺斯"]   好的，那么我就开始了。
[name="普罗旺斯"]   如大家所见，我们已经收到了来自危机合约的新联络。
[name="普罗旺斯"]   罗德岛上次的合约完成情况远远超出了大家的意料，得到了危机合约机构的一致肯定。
[name="普罗旺斯"]   博士精确地挑选了各项合约，在每一次战斗中完成多项指标，给危机合约机构留下深刻的印象。
[name="普罗旺斯"]   即使是我们也没想到，适宜地安排干员进行作战会让效率提高如此之多。
[Character(name="char_002_amiya_1#2")]
[name="阿米娅"]   因为博士的出色工作，不仅罗德岛本身获取了大量物资帮助，也平复了诸多地区的动乱。
[Decision(options="我只是普通地完成工作而已。;啊，有吗？;因为阿米娅帮助了我很多。",values="1;2;3")]
[Predicate(references="1")]
[Character(name="char_002_amiya_1#2")]
[name="阿米娅"]   博士也太谦虚了，您的付出大家都看在眼里的！
[name="阿米娅"]   如果没有博士的指引的话，我们肯定没法完成那么多的合约需求。
[Predicate(references="2")]
[Character(name="char_145_prove_1")]
[name="普罗旺斯"]   博士竟然完全没有觉察到吗？
[name="普罗旺斯"]   在合约中体现的决断力原来只是下意识的判断？
[name="普罗旺斯"]   不愧是博士！
[Predicate(references="3")]
[Character(name="char_002_amiya_1#2")]
[name="阿米娅"]   我也只是辅助而已，博士才是那个努力最多的人。
[Predicate(references="1;2;3")]
[Character(name="char_130_doberm_ex")]
[name="杜宾"]   ......吹捧的话差不多就行，普罗旺斯继续说这次危机合约。
[Character(name="char_145_prove_1")]
[name="普罗旺斯"]   多亏了上次的成绩，罗德岛和危机合约机构总算是再次达成了稳定的协议关系。
[name="普罗旺斯"]   在今后的时间里，每隔一段时间罗德岛都能稳定地接收到来自危机合约的委托了。
[showitem(image="item_cc2_1")]
[Character(name="char_145_prove_1")]
[name="普罗旺斯"]   这次的合约也同样指向多个地区，已经在相关文件上为博士标注了出来。
[name="普罗旺斯"]   各个地区虽然遭到的问题不尽相同，但是都急切的需要帮助。
[Dialog]
[hideitem(fadetime=0.5,block=true)]
[showitem(image="item_cc2_2")]
[Character(name="char_145_prove_1")]
[name="普罗旺斯"]   然后是各项合约细节内容，和以前一样，需要阿米娅和博士来进行确认和安排。
[name="普罗旺斯"]   判断合约的难度并合理调度干员的工作，相信对你们来说一点都不陌生了。
[Dialog]
[hideitem(fadetime=0.5,block=true)]
[showitem(image="item_cc2_4")]
[Character(name="char_145_prove_1")]
[name="普罗旺斯"]   随着合约内容危险性的提高，我们也采用了新的合约危险度检测机制。
[name="普罗旺斯"]   通过专门的合约评估系统，我们会对每次作战的结果做出记录和数据收集。
[name="普罗旺斯"]   为了避免出现意外，只有在合约完成数目逐渐提高之后，后续危险度评级更高的委托才会逐渐解锁。
[name="普罗旺斯"]   相信我们可以循序渐进地完成这次的危机合约任务。
[Dialog]
[hideitem(fadetime=0.5,block=true)]
[Character(name="char_130_doberm_ex")]
[name="杜宾"]   想要获得更高回报，自然代表着更高风险。
[name="杜宾"]   不管以前做的再好，现在也不能放松警惕。
[showitem(image="item_cc2_5")]
[Character(name="char_130_doberm_ex")]
[name="杜宾"]   与此相对，罗德岛内也设立了新的训练场地，专门为模拟各种合约条件进行作战演习。
[name="杜宾"]   如果博士有需要，也可以多加利用。
[name="杜宾"]   做好战前的准备永远都是胜利的第一步。
[Dialog]
[hideitem(fadetime=0.5,block=true)]
[Character(name="char_145_prove_1")]
[name="普罗旺斯"]   那么，危机合约————代号荒芜行动，正式转交给博士。
[name="普罗旺斯"]   PRTS会做好后续的相关资料整理工作，如果还有疑问博士可以在管理界面进行再确认。
[name="普罗旺斯"]   行动正式开始，祝大家一切顺利。
[name="普罗旺斯"]   愿我们能为这片多灾的大地带去希望。
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=3, block=true)]
[Image(fadetime=0)]
[delay(time=1)]
```

### ui_rune_overall_cc

```
[HEADER(key="title_test", is_skippable=false, fit_mode="BLACK_MASK")] 危机合约
[Dialog]
[Background]
[Character]
[PlayMusic(intro="$lab_intro", key="$lab_loop", volume=0.6, crossfade=1, delay=0.5)]
[delay(time=1)]
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[image(image="avg_9_2",xScale=1.1, yScale=1.1,block=false)]
[imageTween(xScaleTo=1.3, yScaleTo=1.3,duration=30,block=false)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
——天灾。
——不知从什么时候开始，天灾开始越发频繁，让大地支离破碎。
人们躲藏在前人的智慧之中，用混凝土与金属建起躲避天灾的巢穴，称之为移动城邦。
但天灾依旧无情地捕猎着地面上的一切生灵，创造着远胜灾难本身的苦难。
必须有人阻止灾难扩散，必须想办法从互相仇视、互相倾轧的城邦之间取得平衡——
[Dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=1, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[image]
否则在天灾撕裂一切之前，我们将无计可施。
[Dialog]
[delay(time=2, black=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.6, block=true)]
[Image(image="cc_start",x=0, y=0, xScale=1, yScale=1, fadetime=0)]
[Blocker(a=0, fadetime=2, block=false)]
[Character]
[ImageTween(xFrom=0, yFrom=0, xTo=0, yTo=-20, xScaleFrom=1, yScaleFrom=1, xScaleTo=1.1, yScaleTo=1.1, duration=15, block=false)]
但是人类从来不会轻易放弃。
在各地的人们寻求生机之时，名为危机合约的特殊情报交换机制应运而生。
危机合约独立于任何所知的政治实体，由众多天灾信使建立并运作至今。
它接收由各种组织或个人发布的特殊任务，然后转送给有能力完成这些任务的人。
天灾信使们从各方搜集情报和资源，为需要帮助的人带去宝贵的支援，为提供帮助的人准备应有的报酬。
罗德岛无疑，是危机合约最为认可的组织之一。
因为整合运动的暴动，双方的交互在一段时间内被隔断。
但是正如人们的精神一般坚韧，罗德岛与危机合约的桥梁，如今再度被架起。
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.6, block=true)]
[delay(time=2)]
[Image(image="cc_end",x=0, y=0, xScale=1, yScale=1, fadetime=0)]
[Blocker(a=0, fadetime=2, block=false)]
[ImageTween(xFrom=0, yFrom=0, xTo=0, yTo=-20, xScaleFrom=1, yScaleFrom=1, xScaleTo=1.1, yScaleTo=1.1, duration=15, block=false)]
————给希望付出努力的每一个人：
不论出身，不论种族，不论善恶，只要你有足够的实力——活下来，处理目标，获得报酬。
或是，处理危险的目标，获得巨额的报酬，以及，活下来。
不管接下来发生的将是怎样前所未有的灾难，“危机合约”都将在阴暗处继续撑起一张无人知晓的网。
这一切，都是为了更多的生命。
——“危机合约”。
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=3, block=true)]
[Image(fadetime=0)]
[Blocker(a=0, fadetime=1, block=true)]
```


## 统计

- 总字符数：5120
- 对话行数：35


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
