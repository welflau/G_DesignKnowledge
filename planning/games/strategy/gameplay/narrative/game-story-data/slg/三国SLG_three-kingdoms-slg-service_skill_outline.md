# 三国SLG · skill_outline（three-kingdoms-slg-service）

> 来源：three-kingdoms-slg-service
> 原始链接：https://github.com/llr104/three-kingdoms-slg-service
> 分类：gameplay
> 标签：三国, SLG, 武将数据, 角色配置
> 游戏类型：SLG

## 概述
三国SLG项目的skill_outline配置数据

## 正文
## 数据概览

- 文件：skill_outline.json

- 键数：3

### 样本

```json
{
  "trigger_type": {
    "des": "触发类型",
    "list": [
      {
        "type": 1,
        "des": "主动"
      },
      {
        "type": 2,
        "des": "被动"
      },
      {
        "type": 3,
        "des": "追击"
      },
      {
        "type": 4,
        "des": "指挥"
      }
    ]
  },
  "effect_type": {
    "des": "效果类型",
    "list": [
      {
        "type": 1,
        "des": "伤害率",
        "isRate": true
      },
      {
        "type": 2,
        "des": "攻击",
        "isRate": false
      },
      {
        "type": 3,
        "des": "防御",
        "isRate": false
      },
      {
        "type": 4,
        "des": "谋略",
        "isRate": false
      },
      {
        "type": 5,
        "des": "速度",
        "isRate": false
      },
      {
        "type": 6,
        "des": "破坏",
        "isRate": false
      }
    ]
  },
  "target_type": {
    "des": "作用目标类型",
    "list": [
      {
        "type": 1,
        "des": "自己"
      },
      {
        "type": 2,
        "des": "我军单体"
      },
      {
        "type": 3,
        "des": "我军1-2个目标"
      },
      {
        "type": 4,
        "des": "我军1-3个目标"
      },
      {
        "type": 5,
        "des": "我军全体"
      },
      {
        "type": 6,
        "des": "敌军单体"
      },
      {
        "type": 7,
        "des": "敌军1-2个目标"
      },
      {
        "type": 8,
        "des": "敌军1-3个目标"
      },
      {
        "type": 9,
        "des": "敌军全体"
      }
    ]
  }
}
```

## 策划参考价值
SLG武将/角色的数据结构参考。
