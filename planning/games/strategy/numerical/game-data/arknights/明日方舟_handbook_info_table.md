# 明日方舟 · 干员档案

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData/blob/master/zh_CN/gamedata/excel/handbook_info_table.json
> 分类：numerical
> 标签：明日方舟, 数据解包, 干员档案

## 概述
干员故事/档案/语音

## 正文
## 数据结构概览

- 文件大小：5.2 MB
- 顶层键数量：6
- 顶层键列表（前50个）：

  - `handbookDict`
  - `npcDict`
  - `teamMissionList`
  - `handbookDisplayConditionList`
  - `handbookStageData`
  - `handbookStageTime`

## 样本数据（第一个条目：`handbookDict`）

```json
{
  "char_500_noirc": {
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
  },
  "char_501_durin": {
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
        "charId": "char_501_du
```


## 策划参考价值
SLG策划参考：可用于分析角色成长体系、战斗数值框架、经济系统设计。
