# 明日方舟 · 道具表

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData/blob/master/zh_CN/gamedata/excel/item_table.json
> 分类：numerical
> 标签：明日方舟, 数据解包, 道具表

## 概述
所有道具/材料/配方/掉落来源

## 正文
## 数据结构概览

- 文件大小：1.5 MB
- 顶层键数量：13
- 顶层键列表（前50个）：

  - `items`
  - `expItems`
  - `potentialItems`
  - `apSupplies`
  - `charVoucherItems`
  - `uniqueInfo`
  - `itemTimeLimit`
  - `uniCollectionInfo`
  - `itemPackInfos`
  - `fullPotentialCharacters`
  - `activityPotentialCharacters`
  - `favorCharacters`
  - `itemShopNameDict`

## 样本数据（第一个条目：`items`）

```json
{
  "5001": {
    "itemId": "5001",
    "name": "声望",
    "description": "做得很好，就这样继续变强吧。只要坚持不懈，所有的心血都不会白费的。",
    "rarity": "TIER_5",
    "iconId": "EXP_PLAYER",
    "overrideBkg": null,
    "stackIconId": null,
    "sortId": -10000,
    "usage": "战斗结束后获得的经验。足以见证博士的成长。",
    "obtainApproach": "战斗获取",
    "hideInItemGet": false,
    "classifyType": "NONE",
    "itemType": "EXP_PLAYER",
    "stageDropList": [],
    "buildingProductList": [],
    "voucherRelateList": null,
    "shopRelateInfoList": null
  },
  "SOCIAL_PT": {
    "itemId": "SOCIAL_PT",
    "name": "信用",
    "description": "信用维系着各个群体间的关系，也是社会稳定的象征，有时候甚至比金钱还有用哦，请好好珍惜。",
    "rarity": "TIER_2",
    "iconId": "SOCIAL_PT",
    "overrideBkg": null,
    "stackIconId": null,
    "sortId": -10000,
    "usage": "友谊的见证，用于在商店中兑换物资。",
    "obtainApproach": "好友助战、支援单位、宿舍氛围、线索交流",
    "hideInItemGet": false,
    "classifyType": "NONE",
    "itemType": "SOCIAL_PT",
    "stageDropList": [],
    "buildingProductList": [],
    "voucherRelateList": null,
    "shopRelateInfoList": null
  },
  "AP_GAMEPLAY": {
    "itemId": "AP_GAMEPLAY",
    "name": "理智",
    "description": "“是什么区别了这片大地和我们自身？呼吸，还是情感？又或者是，生、老、病、死？”",
    "rarity": "TIER_5",
    "iconId": "AP_GAMEPLAY",
    "overrideBkg": null,
    "stackIconId": null,
    "sortId": -10000,
    "usage": "用以维持自我的必要概念，支撑着各类行动的策划与执行。",
    "obtainApproach": "自然时间回复",
    "hideInItemGet": false,
    "classifyType": "NONE",
    "itemType": "AP_GAMEPLAY",
    "stageDropList": [],
    "buildingProductList": [],
    "voucherRelateList": null,
    "shopRelateInfoList": null
  },
  "6001": {
    "itemId": "6001",
    "name": "演习券",
    "description": "凡事欲速则不达。对于罗德岛而言，每一次正式交战都意味着会出现人员伤亡的可能性，因此，在进入实战前多利用演习参透对方的布置才是上策，不然等到中了敌方埋伏，一切都来不及了。",
    "rarity": "TIER_5",
    "iconId": "TKT_TRY",
    "overrideBkg": null,
    "stackIconId": null,
    "sortId": -10000,
    "usage": "有关实战前演习的计划书。在选择行动的界面使用，可以模拟出正式交战时的场景，以便指挥部拟定实战策略。",
    "obtainApproach": "每日恢复到30张",
    "hideInItemGet": false,
    "classifyType": "NONE",
    "itemType": "TKT_TRY",
    "stageDropList": [],
    "buildingProductList": [],
    "voucherRelateList": null,
    "shopRelateInfoList": null
  },
  "base_ap": {
    "itemId": "base_ap",
    "name": "无人机",
    "description": "由罗德岛后勤部统一操控的建造用无人机，没有它们，干员们可能要多等十倍的时间才能入住。",
    "rarity": "TIER_5",
    "iconId": "AP_BASE",
    "overrideBkg": null,
    "stackIconId": null,
    "sortId": -10000,
    "usage": "支持罗德岛基础建设的重要机械，通常会用于基建设施的清理与建造升级等。",
    "obtainApproach": "清理房间获取、自然时间回复",
    "hideInItemGet": false,
    "classifyType": "NONE",
    "itemType": "AP_BASE",
    "stageDropList": [],
    "buildingProductList": [],
    "voucherRelateList": null,
    "shopRelateInfoList": null
  },
  "bilibili001": {
    "itemId": "bilibili001",
    "name": "预约干员随机4选1",
    "description": "会是谁呢？真的期待啊~",
    "rarity": "TIER_6",
    "iconId": "bilibili001",
    "overrideBkg": null,
    "stackIconId": null,
    "sortId": -10000,
    "usage": "用于抽取预约奖励。",
    "obtainApproach": "预约活动奖励",
    "hideInItemGet": false,
    "classifyType": "NONE",
    "itemType": "TKT_GACHA_PRSV",
    "stageDropList": [],
    "buildingProductList": [],
    "voucherRelateList": null,
    "shopRelateInfoList": null
  },
  "4002": {
    "itemId": "4002",
    "name": "至纯源石",
    "description": "在工业中用量巨大的源石结晶，但有着较高的提取难度。是世界的主要能源类精加工产物，同时也是几乎所有源石技艺得以施展的根本。如今，即使“它会传播绝症”的传言甚嚣尘上，也依旧没多少人能抵挡住它的诱惑。",
    "rarity": "TIER_6",
    "iconId": "DIAMOND",
    "overrideBkg": null,
    "stackIconId": null,
    "sortId": 10001,
    "usage": "危险而又必不可少的物质。较为珍贵，用途多样。",
    "obtainApproach": "采购中心、首次通关获取",
    "hideInItemGet": false,
    "classifyType": "NORMAL",
    "itemType": "DIAMOND",
    "stageDropList": [],
    "buildingProductList": [],
    "voucherRelateList": null,
    "shopRelateInfoList": null
  },
  "4003": {
    "itemId": "4003",
    "name": "合成玉",
    "description": "由至纯源石加工而来，混合了其他矿物以后的源石产物。以前仅能当作一些传导元件使用，现在却逐渐成为人事交互关系中令人信服的象征物。",
    "rarity": "TIER_5",
    "iconId": "DIAMOND_SHD",
    "overrideBkg": null,
    "stackIconId": "DIAMOND_SHD_STACK",
    "sortId": 10002,
    "usage": "合成物质。常用于招募干员。",
    "obtainApproach": null,
    "hideInItemGet": false,
    "classifyType": "NORMAL",
    "itemType": "DIAMOND_SHD",
    "stageDropList": [
      {
        "stageId": "camp_01",
        "occPer": "ALWAYS",
        "sortId": 0
      },
      {
        "stageId": "camp_r_29",
        "occPer": "ALWAYS",
        "sortId": 1
      },
      {
        "stageId": "camp_r_28",
        "occPer": "ALWAYS",
        "sortId": 2
      },
      {
        "stageId": "camp_r_27",
        "occPer": "ALWAYS",
        "sortId": 3
      },
      {
        "stageId": "camp_r_26",
        "occPer": "ALWAYS",
        "sortId": 4
      },
      {
        "stageId": "camp_r_25",
        "occPer": "ALWAYS",
        "sortId": 5
      },
      {
        "stageId": "camp_r_24",
        "occPer": "ALWAYS",
        "sortId": 6
      },
      {
        "stageId": "camp_r_23",
        "occPer": "ALWAYS",
        "sortId": 7
      },
      {
        "stageId": "camp_r_22",
        "occPer": "ALWAYS",
        "sortId": 8
      },
      {
        "stageId": "camp_r_21",
        "occPer": "ALWAYS",
        "sortId": 9
      },
      {
        "stageId": "camp_r_20",
        "occPer": "ALWAYS",
        "sortId": 10
      },
      {
        "stageId": "camp_r_19",
        "occPer": "ALWAYS",
        "sortId": 11
      },
      {
        "stageId": "camp_r_18",
        "occPer": "ALWAYS",
        "sortId": 12
      },
      {
        "stageId": "camp_r_17",
        "occPer": "ALWAYS",
        "sortId": 13
      },
      {
        "stageId": "camp_r_16",
        "occPer": "ALWAYS",
        "sortId": 14
      },
      {
        "stageId": "camp_r_15",
        "occPer": "ALWAYS",
        "sortId": 15
      },
      {
        "stageId": "camp_r_14",
        "occPer": "ALWAYS",
        "sortId": 16
      },
      {
        "stageId": "camp_r_13",
        "occPer": "ALWAYS",
        "sortId": 17
      },
      {
        "stageId": "camp_02",
        "occPer": "ALWAYS",
        "sortId": 18
      },
      {
        "stageId": "camp_03",
        "occPer": "ALWAYS",
        "sortId": 19
      },
      {
        "stageId": "camp_r_01",
        "occPer": "ALWAYS",
        "sortId": 20
      },
      {
        "stageId": "camp_r_02",
        "occPer": "ALWAYS",
        "sortId": 21
      },
      {
        "stageId": "camp_r_03",
        "occPer": "ALWAYS",
        "sortId": 22
      },
      {
        "stageId": "camp_r_04",
        "occPer": "ALWAYS",
        "sortId": 23
      },
      {
        "stageId": "camp_r_30",
        "occPer": "ALWAYS",
        "sortId": 24
      },
      {
        "stageId": "camp_r_05",
        "occPer": "ALWAYS",
        "sortId": 25
      },
      {
        "stageId": "camp_r_07",
        "occPer": "ALWAYS",
        "sortId": 26
      },
      {
        "stageId": "camp_r_08",
        "occPer": "ALWAYS",
        "sortId": 27
      },
      {
        "stageId": "camp_r_09",
        "occPer": "ALWAYS",
        "sortId": 28
      },
      {
        "stageId": "camp_r_10",
        "occPer": "ALWAYS",
        "sortId": 29
      },
      {
        "stageId": "camp_r_11",
        "occPer": "ALWAYS",
        "sortId": 30
      },
      {
        "stageId": "camp_r_12",
        "occPer": "ALWAYS",
        "sortId": 31
      },
      {
        "stageId": "camp_r_06",
        "occPer": "ALWAYS",
        "sortId": 32
      },
      {
        "stageId": "camp_r_31",
        "occPer": "ALWAYS",
        "sortId": 33
      }
    ],
    "buildingProductList": [],
    "voucherRelateList": null,
    "shopRelateInfoList": null
  },
  "3141": {
    "itemId": "3141",
    "name": "源石碎片",
    "description": "从遭受重度污染的地区回收的源石碎块，存在高感染威胁及一定突变概率，是哥伦比亚疾病防控中心毒性数据库重点提及的危险物质。",
    "rarity": "TIER_5",
    "iconId": "MTL_DIAMOND_SHD",
    "overrideBkg": null,
    "stackIconId": null,
    "sortId": 10003,
    "usage": "从污染区域中收集到的源石碎片，用以制作合成玉。",
    "obtainApproach": null,
    
```


## 策划参考价值
SLG策划参考：可用于分析角色成长体系、战斗数值框架、经济系统设计。
