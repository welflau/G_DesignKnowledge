# 明日方舟 · 干员档案数据（角色背景/故事/语音）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 角色档案, 角色故事, 世界观
> 游戏类型：塔防策略RPG

## 概述
明日方舟全干员档案数据，共420份。含角色背景故事、临床诊断、档案记录、语音文本。

## 正文
## 明日方舟干员档案系统

- 总档案数：420

### 样本1：`char_500_noirc`

```json
{
  "charID": "char_500_noirc",
  "infoName": "Unknown",
  "isLimited": false,
  "storyTextAudio": [
    {
      "stories": [
        {
          "storyText": "【代号】黑角\n【性别】男\n【战斗经验】八年\n【出身地】东国\n【生日】8月30日\n【种族】鬼\n【身高】180cm\n【矿石病感染情况】\n参照医学检测报告，确认为感染者。",
          "unLockType": "DIRECT",
          "unLockParam": "",
          "showType": "DIRECT",
          "showParam": "",
          "unLockString": "",
          "patchIdList": null
        }
      ],
      "storyTitle": "基础档案",
      "unLockorNot": true
    },
    {
      "stories": [
        {
          "storyText": "【物理强度】标准\n【战场机动】普通\n【生理耐受】优良\n【战术规划】普通\n【战斗技巧】普通\n【源石技艺适应性】标准",
          "unLockType": "DIRECT",
          "unLockParam": "",
          "showType": "DIRECT",
          "showParam": "",
          "unLockString": "",
          "patchIdList": null
        }
      ],
      "storyTitle": "综合体检测试",
      "unLockorNot": true
    },
    {
      "stories": [
        {
          "storyText": "罗德岛的基础干员之一，上战场冲在最前线保护队友，回到方舟上退居后勤默默工作的实干型角色。",
          "unLockType": "DIRECT",
          "unLockParam": "",
          "showType": "DIRECT",
          "showParam": "",
          "unLockString": "",
          "patchIdList": null
        }
      ],
      "storyTitle": "客观履历",
      "unLockorNot": true
    },
    {
      "stories": [
        {
          "storyText": "造影检测结果显示，该干员体内脏器轮廓模糊，可见异常阴影，循环系统内源石颗粒检测异常，有矿石病感染迹象，现阶段可确认为矿石病感染者。\n\n【体细胞与源石融合率】11%\n体表暂未出现明显的矿石病病征。\n\n【血液源石结晶密度】0.22u/L\n感染程度尚浅，暂时还没有带来明显身体影响。",
          "unLockType": "FAVOR",
          "unLockParam": "25",
          "showType": "DIRECT",
          "showParam": "",
          "unLockString": "",
          "patchIdList": null
        }
      ],
      "storyTitle": "临床诊断分析",
      "unLockorNot": true
    },
    {
      "stories": [
        {
          "storyText": "罗德岛的老牌干员，年纪在干员中也偏大，因为戴着面具，常给人以难以交流的印象。 不过交流之后就会发现，本人从不摆出前辈或年长者的架子，是能和年轻人打成一片的活泼大哥哥。 ",
          "unLockType": "FAVOR",
          "unLockParam": "50",
          "showType": "DIRECT",
          "showParam": "",
          "unLockString": "",
          "patchIdList": null
        }
      ],
      "storyTitle": "档案资料一",
      "unLockorNot": true
    },
    {
      "stories": [
        {
          "storyText": "黑角的房间里收藏着各式各样的面具，在不同的节日，他会戴上符合节日氛围的面具。\n平时穿戴的似乎是他最喜欢的一款，用他的话说，就是“俺觉得这一款最搭罗德岛的氛围”。\n顺便一提，面具下并没有见不得人的秘密。",
          "unLockType": "FAVOR",
          "unLockParam": "100",
          "showType": "DIRECT",
          "showParam": "",
          "unLockString": "",
          "patchIdList": null
        }
      ],
      "storyTitle": "档案资料二",
      "unLockorNot": true
    },
    {
      "stories": [
        {
          "storyText": "黑角的性格中，唯一有些令人在意的地方，就是他似乎有些畏惧夜刀。并不是恐惧，而是不想惹她生气的感觉。这引起了一些比较八卦的干员的注意。 \n不过无论是两人的履历还是相处模式，都无法看出更多的东西。",
          "unLockType": "FAVOR",
          "unLockParam": "150",
          "showType": "DIRECT",
          "showParam": "",
          "unLockString": "",
          "patchIdList": null
        }
      ],
      "storyTitle": "档案资料三",
      "unLockorNot": true
    }
  ],
  "handbookAvgList": [
    {
      "storySetId": "story_noirc_set_1",
      "storySetName": "甲板另一侧",
      "sortId": 1,
      "storyGetTime": 1617091200,
      "rewardItem": [],
      "unlockParam": [
        {
          "unlockType": "AWAKE",
          "unlockParam1": "0",
          "unlockParam2": "30",
          "unlockParam3": null
        },
        {
          "unlockType": "FAVOR",
          "unlockParam1": "50",
          "unlockParam2": null,
          "unlockParam3": null
        }
      ],
      "avgList": [
        {
          "storyId": "story_noirc_set_1_story_1",
          "storySetId": "story_noirc_set_1",
          "storySort": 1,
          "storyCanShow": true,
          "storyIntro": "下班之后，才是生活。",
          "storyInfo": "info/obt/memory/story_noirc_1_1",
          "storyTxt": "obt/memory/story_noirc_1_1"
        }
      ],
      "charId": "char_500_noirc"
    }
  ]
}
```

### 样本2：`char_501_durin`

```json
{
  "charID": "char_501_durin",
  "infoName": "Unknown",
  "isLimited": false,
  "storyTextAudio": [
    {
      "stories": [
        {
          "storyText": "【代号】杜林\n【性别】女\n【战斗经验】两年\n【出身地】未公开\n【生日】12月15日\n【种族】杜林\n【身高】131cm\n【矿石病感染情况】\n参照医学检测报告，确认为非感染者。",
          "unLockType": "DIRECT",
          "unLockParam": "",
          "showType": "DIRECT",
          "showParam": "",
          "unLockString": "",
          "patchIdList": null
        }
      ],
      "storyTitle": "基础档案",
      "unLockorNot": true
    },
    {
      "stories": [
        {
          "storyText": "【物理强度】缺陷 \n【战场机动】普通 \n【生理耐受】缺陷 \n【战术规划】普通 \n【战斗技巧】普通 \n【源石技艺适应性】优良",
          "unLockType": "DIRECT",
          "unLockParam": "",
          "showType": "DIRECT",
          "showParam": "",
          "unLockString": "",
          "patchIdList": null
        }
      ],
      "storyTitle": "综合体检测试",
      "unLockorNot": true
    },
    {
      "stories": [
        {
          "storyText": "杜林，罗德岛A4行动组所属干员。\n有着较强的法术天赋，但因自身性格和体质原因无法完全施展。\n极度嗜睡，会随时在任何地方进入睡眠状态，日均睡眠时间远高于干员平均值，但工作却鲜少有缺漏。",
          "unLockType": "DIRECT",
          "unLockParam": "",
          "showType": "DIRECT",
          "showParam": "",
          "unLockString": "",
          "patchIdList": null
        }
      ],
      "storyTitle": "客观履历",
      "unLockorNot": true
    },
    {
      "stories": [
        {
          "storyText": "造影检测结果显示，该干员体内脏器轮廓清晰，未见异常阴影，循环系统内源石颗粒检测未见异常，无矿石病感染迹象，现阶段可确认为非矿石病感染者。\n\n【体细胞与源石融合率】0%\n干员杜林没有被源石感染的迹象。\n\n【血液源石结晶密度】0.18u/L\n干员杜林经常接触经过处理的源石制品，但从未发生任何异常。",
          "unLockType": "FAVOR",
          "unLockParam": "25",
          "showType": "DIRECT",
          "showParam": "",
          "unLockString": "",
          "patchIdList": null
        }
      ],
      "storyTitle": "临床诊断分析",
      "unLockorNot": true
    },
    {
      "stories": [
        {
          "storyText": "工作模式：充分借助自己的身高优势，使用法术对敌人发起偷袭。\n普通模式：找个稍微舒适点的地方，睡觉。",
          "unLockType": "FAVOR",
          "unLockParam": "50",
          "showType": "DIRECT",
          "showParam": "",
          "unLockString": "",
          "patchIdList": null
        }
      ],
      "storyTitle": "档案资料一",
      "unLockorNot": true
    },
    {
      "stories": [
        {
          "storyText": "因为出身与众不同，杜林的饮食结构和大家稍有区别，但这并不意味着她吃的就比别人少。杜林虽然矮小，但吃东西的速度比普通人要快上许多，有时，其他干员还没吃上几口，杜林用餐结束找地方睡觉了。",
          "unLockType": "FAVOR",
          "unLockParam": "100",
          "showType": "DIRECT",
          "showParam": "",
          "unLockString": "",
          "patchIdList": null
        }
      ],
      "storyTitle": "档案资料二",
      "unLockorNot": true
    }
  ],
  "handbookAvgList": [
    {
      "storySetId": "story_durin_set_1",
      "storySetName": "午休时间",
      "sortId": 1,
      "storyGetTime": 1625198400,
      "rewardItem": [],
      "unlockParam": [
        {
          "unlockType": "AWAKE",
          "unlockParam1": "0",
          "unlockParam2": "30",
          "unlockParam3": null
        },
        {
          "unlockType": "FAVOR",
          "unlockParam1": "50",
          "unlockParam2": null,
          "unlockParam3": null
        }
      ],
      "avgList": [
        {
          "storyId": "story_durin_set_1_story_1",
          "storySetId": "story_durin_set_1",
          "storySort": 1,
          "storyCanShow": true,
          "storyIntro": "只要不耽误工作，悠悠闲闲地睡久一点也没什么不好嘛。",
          "storyInfo": "info/obt/memory/story_durin_1_1",
          "storyTxt": "obt/memory/story_durin_1_1"
        }
      ],
      "charId": "char_501_durin"
    }
  ]
}
```

### 样本3：`char_502_nblade`

```json
{
  "charID": "char_502_nblade",
  "infoName": "Unknown",
  "isLimited": false,
  "storyTextAudio": [
    {
      "stories": [
        {
          "storyText": "【代号】夜刀\n【性别】女\n【战斗经验】八年\n【出身地】东国\n【生日】5月14日\n【种族】鬼\n【身高】161cm\n【矿石病感染情况】\n参照医学检测报告，确认为感染者。",
          "unLockType": "DIRECT",
          "unLockParam": "",
          "showType": "DIRECT",
          "showParam": "",
          "unLockString": "",
          "patchIdList": null
        }
      ],
      "storyTitle": "基础档案",
      "unLockorNot": true
    },
    {
      "stories": [
        {
          "storyText": "【物理强度】标准 \n【战场机动】优良 \n【生理耐受】标准 \n【战术规划】标准 \n【战斗技巧】标准 \n【源石技艺适应性】标准",
          "unLockType": "DIRECT",
          "unLockParam": "",
          "showType": "DIRECT",
          "showParam": "",
          "unLockString": "",
          "patchIdList": null
        }
      ],
      "storyTitle": "综合体检测试",
      "unLockorNot": true
    },
    {
      "stories": [
        {
          "storyText": "基础干员之一，同时也是他们的组长，忠诚可靠的武士。",
          "unLockType": "DIRECT",
          "unLockParam": "",
          "showType": "DIRECT",
          "showParam": "",
          "unLockString": "",
          "patchIdList": null
        }
      ],
      "storyTitle": "客观履历",
      "unLockorNot": true
    },
    {
      "stories": [
        {
          "storyText": "造影检测结果显示，该干员体内脏器轮廓模糊，可见异常阴影，循环系统内源石颗粒检测异常，有矿石病感染迹象，现阶段可确认为矿石病感染者。\n\n【体细胞与源石融合率】8%\n体表暂未出现明显的矿石病病征。\n\n【血液源石结晶密度】0.22u/L\n感染程度尚浅，暂时还没有带来明显身体影响。",
          "unLockType": "FAVOR",
          "unLockParam": "25",
          "showType": "DIRECT",
          "showParam": "",
          "unLockString": "",
          "patchIdList": null
        }
      ],
      "storyTitle": "临床诊断分析",
      "unLockorNot": true
    },
    {
      "stories": [
        {
          "storyText": "沉默寡言的武士。除了脸上的面具，没有任何引人注意的地方。\n存在感十分稀薄，容易被人忽视，不过本人对此似乎并没有意见，只是坚实地完成着每一个被交给自己的任务。\n“罗德岛的基石。”——凯尔希医生如是评价过。",
          "unLockType": "FAVOR",
          "unLockParam": "50",
          "showType": "DIRECT",
          "showParam": "",
          "unLockString": "",
          "patchIdList": null
        }
      ],
      "storyTitle": "档案资料一",
      "unLockorNot": true
    },
    {
      "stories": [
        {
          "storyText": "没人知道夜刀是什么时候加入罗德岛的，事实上也没有人在意过。 \n她如同理所当然一般存在于罗德岛之中，或许哪天她突然消失也不会有多少人察觉。",
          "unLockType": "FAVOR",
          "unLockParam": "100",
          "showType": "DIRECT",
          "showParam": "",
          "unLockString": "",
          "patchIdList": null
        }
      ],
      "storyTitle": "档案资料二",
      "unLockorNot": true
    },
    {
      "stories": [
        {
          "storyText": "曾有比较八卦的干员询问夜刀，她和黑角是不是曾经交往过，没有得到夜刀的正面回应。 \n无论如何，和黑角一样，她很少摘下她的面具。",
          "unLockType": "FAVOR",
          "unLockParam": "150",
          "showType": "DIRECT",
          "showParam": "",
          "unLockString": "",
          "patchIdList": null
        }
      ],
      "storyTitle": "档案资料三",
      "unLockorNot": true
    }
  ],
  "handbookAvgList": [
    {
      "storySetId": "story_nblade_set_1",
      "storySetName": "授刀",
      "sortId": 1,
      "storyGetTime": 1689667200,
      "rewardItem": [],
      "unlockParam": [
        {
          "unlockType": "AWAKE",
          "unlockParam1": "0",
          "unlockParam2": "30",
          "unlockParam3": null
        },
        {
          "unlockType": "FAVOR",
          "unlockParam1": "50",
          "unlockParam2": null,
          "unlockParam3": null
        }
      ],
      "avgList": [
        {
          "storyId": "story_nblade_set_1_story_1",
          "storySetId": "story_nblade_set_1",
          "storySort": 1,
          "storyCanShow": true,
          "storyIntro": "要承下夜刀的刀可不容易。",
          "storyInfo": "info/obt/memory/story_nblade_1_1",
          "storyTxt": "obt/memory/story_nblade_1_1"
        }
      ],
      "charId": "char_502_nblade"
    }
  ]
}
```

### 样本4：`char_503_rang`

```json
{
  "charID": "char_503_rang",
  "infoName": "Unknown",
  "isLimited": false,
  "storyTextAudio": [
    {
      "stories": [
        {
          "storyText": "【代号】巡林者\n【性别】男\n【战斗经验】五年\n【出身地】未公开\n【生日】7月22日 \n【种族】萨弗拉\n【身高】179cm\n【矿石病感染情况】\n参照医学检测报告，确认为非感染者。",
          "unLockType": "DIRECT",
          "unLockParam": "",
          "showType": "DIRECT",
          "showParam": "",
          "unLockString": "",
          "patchIdList": null
        }
      ],
      "storyTitle": "基础档案",
      "unLockorNot": true
    },
    {
      "stories": [
        {
          "storyText": "【物理强度】普通 \n【战场机动】优良 \n【生理耐受】普通 \n【战术规划】普通 \n【战斗技巧】优良 \n【源石技艺适应性】普通",
          "unLockType": "DIRECT",
          "unLockParam": "",
          "showType": "DIRECT",
          "showParam": "",
          "unLockString": "",
          "patchIdList": null
        }
      ],
      "storyTitle": "综合体检测试",
      "unLockorNot": true
    },
    {
      "stories": [
        {
          "storyText": "巡林者，罗德岛A4行动组所属干员。罗德岛老员工，曾经游历过许多地方，现在则留在罗德岛服从调配。专业的弓手，年事已高，但依旧保持着萨弗拉特有的敏捷与活力。",
          "unLockType": "DIRECT",
          "unLockParam": "",
          "showType": "DIRECT",
          "showParam": "",
          "unLockString": "",
          "patchIdList": null
        }
      ],
      "storyTitle": "客观履历",
      "unLockorNot": true
    },
    {
      "stories": [
        {
          "storyText": "造影检测结果显示，该干员体内脏器轮廓清晰，未见异常阴影，循环系统内源石颗粒检测未见异常，无矿石病感染迹象，现阶段可确认为非矿石病感染者。\n\n【体细胞与源石融合率】0%\n干员巡林者没有被源石感染的迹象。\n\n【血液源石结晶密度】0.12u/L\n干员巡林者甚少前往矿石病高发地区。",
          "unLockType": "FAVOR",
          "unLockParam": "25",
          "showType": "DIRECT",
          "showParam": "",
          "unLockString": "",
          "patchIdList": null
        }
      ],
      "storyTitle": "临床诊断分析",
      "unLockorNot": true
    },
    {
      "stories": [
        {
          "storyText": "比起守株待兔更擅长发起突袭，先发制人，熟练运用环境来掩盖本身体色在隐蔽性上的劣势。",
          "unLockType": "FAVOR",
          "unLockParam": "50",
          "showType": "DIRECT",
          "showParam": "",
          "unLockString": "",
          "patchIdList": null
        }
      ],
      "storyTitle": "档案资料一",
      "unLockorNot": true
    },
    {
      "stories": [
        {
          "storyText": "毫无疑问，巡林者是个优秀的说书人，他的脑袋里，永远储藏着你从未听闻过的精彩故事，他本人似乎也期待着与他人分享这些故事，因此，当罗德岛的小干员们上完清晨的课程后，许多人便会请“巡林者爷爷”讲故事，于是，一杯热水，一个说书人，孩子们美好的休闲时光便开始了。",
          "unLockType": "FAVOR",
          "unLockParam": "100",
          "showType": "DIRECT",
          "showParam": "",
          "unLockString": "",
          "patchIdList": null
        }
      ],
      "storyTitle": "档案资料二",
      "unLockorNot": true
    },
    {
      "stories": [
        {
          "storyText": "与大部分萨弗拉人不同，巡林者的体色完全无法为他提供拟态和遮蔽，但相对的，巡林者要比其他萨弗拉更加自信，也更乐于与人交流。这既是诅咒，也是馈赠。好坏与否只取决于巡林者本人对此的看法。",
          "unLockType": "FAVOR",
          "unLockParam": "150",
          "showType": "DIRECT",
          "showParam": "",
          "unLockString": "",
          "patchIdList": null
        }
      ],
      "storyTitle": "档案资料三",
      "unLockorNot": true
    }
  ],
  "handbookAvgList": []
}
```

### 样本5：`char_122_beagle`

```json
{
  "charID": "char_122_beagle",
  "infoName": "Unknown",
  "isLimited": false,
  "storyTextAudio": [
    {
      "stories": [
        {
          "storyText": "【代号】米格鲁\n【性别】女\n【战斗经验】一年\n【出身地】玻利瓦尔\n【生日】3月2日\n【种族】佩洛\n【身高】154cm\n【矿石病感染情况】\n参照医学检测报告，确认为感染者。",
          "unLockType": "DIRECT",
          "unLockParam": "",
          "showType": "DIRECT",
          "showParam": "",
          "unLockString": "",
          "patchIdList": null
        }
      ],
      "storyTitle": "基础档案",
      "unLockorNot": true
    },
    {
      "stories": [
        {
          "storyText": "【物理强度】优良\n【战场机动】普通 \n【生理耐受】优良\n【战术规划】普通 \n【战斗技巧】标准 \n【源石技艺适应性】标准",
          "unLockType": "DIRECT",
          "unLockParam": "",
          "showType": "DIRECT",
          "showParam": "",
          "unLockString": "",
          "patchIdList": null
        }
      ],
      "storyTitle": "综合体检测试",
      "unLockorNot": true
    },
    {
      "stories": [
        {
          "storyText": "行动预备组A1前卫队员。与芬以及克洛丝一起来到罗德岛。虽然有不成熟的一面，但也逐渐展现出了专业和不认输的一面以及极强的天赋，慢慢成为了被更多人认可的可靠干员。",
          "unLockType": "DIRECT",
          "unLockParam": "",
          "showType": "DIRECT",
          "showParam": "",
          "unLockString": "",
          "patchIdList": null
        }
      ],
      "storyTitle": "客观履历",
      "unLockorNot": true
    },
    {
      "stories": [
        {
          "storyText": "造影检测结果显示，该干员体内脏器轮廓模糊，可见异常阴影，循环系统内源石颗粒检测异常，有矿石病感染迹象，现阶段可确认为矿石病感染者。\n\n【体细胞与源石融合率】8%\n体表暂未出现明显的矿石病病征。\n\n【血液源石结晶密度】0.21 u/L\n感染程度尚浅，暂时还没有带来明显身体影响。",
          "unLockType": "FAVOR",
          "unLockParam": "25",
          "showType": "DIRECT",
          "showParam": "",
          "unLockString": "",
          "patchIdList": null
        }
      ],
      "storyTitle": "临床诊断分析",
      "unLockorNot": true
    },
    {
      "stories": [
        {
          "storyText": "没有花哨的技巧和法术力，米格鲁会利用自己的耐力为身后队友树立起坚实的前卫防御。即使笨拙的自己，只要一直坚持这样的方向不停，就一定可以做得越来越好。事实证明，米格鲁的这个想法一点都没错。",
          "unLockType": "FAVOR",
          "unLockParam": "50",
          "showType": "DIRECT",
          "showParam": "",
          "unLockString": "",
          "patchIdList": null
        }
      ],
      "storyTitle": "档案资料一",
      "unLockorNot": true
    },
    {
      "stories": [
        {
          "storyText": "在哥伦比亚外围警卫预备队的时光，既是米格鲁最辛苦的，也是最宝贵的回忆。为了弥补自身和其他正式成员的差距，芬和克洛丝陪着米格鲁从来没有松懈过。然而最后得知自己感染了矿石病的时候，米格鲁陷入了深深的自责。她觉得是自己拖累了芬和克洛丝，是自己害的大家都失去了机会，一切都是自己的错。",
          "unLockType": "FAVOR",
          "unLockParam": "100",
          "showType": "DIRECT",
          "showParam": "",
          "unLockString": "",
          "patchIdList": null
        }
      ],
      "storyTitle": "档案资料二",
      "unLockorNot": true
    },
    {
      "stories": [
        {
          "storyText": "沉沦之际，芬和克洛丝都站在了米格鲁面前，一起面对了警备队的驱逐和流放。在克洛丝的推荐下，三人第一次来到了罗德岛。从那一天起，米格鲁在心中决定，要用自己的一切回报一直陪伴着她的芬和克洛丝以及身边的关心她的所有人。",
          "unLockType": "FAVOR",
          "unLockParam": "150",
          "showType": "DIRECT",
          "showParam": "",
          "unLockString": "",
          "patchIdList": null
        }
      ],
      "storyTitle": "档案资料三",
      "unLockorNot": true
    },
    {
      "stories": [
        {
          "storyText": "看着每天大家的拌嘴、打闹、欢乐，米格鲁发自内心地感到幸福和感激。每天米格鲁都要努力调和吵架的炎熔和芙蓉，陪芬寻找偷懒消失的克洛丝，还得在空余的时间内陪罗德岛的前辈去跑腿干体力活，但是她也都乐在其中。\n【那个家伙就是完全不会拒绝人......】————克洛丝",
          "unLockType": "FAVOR",
          "unLockParam": "200",
          "showType": "DIRECT",
          "showParam": "",
          "unLockString": "",
          "patchIdList": null
        }
      ],
      "storyTitle": "档案资料四",
      "unLockorNot": true
    }
  ],
  "handbookAvgList": []
}
```



## 策划参考价值
角色叙事数据结构的标杆参考。展示了如何用结构化数据组织角色背景故事。
