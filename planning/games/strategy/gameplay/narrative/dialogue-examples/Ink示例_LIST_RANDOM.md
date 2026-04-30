# Ink脚本示例 · LIST_RANDOM

> 来源：inkle/ink-library
> 原始链接：https://github.com/inkle/ink-library
> 分类：gameplay
> 标签：Ink, 叙事工具, 对话脚本, 分支叙事, 通用
> 游戏类型：叙事工具

## 概述
Ink叙事脚本语言的完整示例故事：LIST_RANDOM

## 正文
```ink
// Note: This will be very slow since it's a recursive function
// and ink isn't a very fast language! It's a strong contender for
// being implemented natively in ink.

=== function LIST_RANDOM(list) 
    { list:
        ~ return getNth(list, RANDOM(1, LIST_COUNT(list)))
    - else:
        ~ return list 
    }
 
=== function getNth(list, n) 
    { LIST_COUNT(list) > 0:
        ~ n = n mod LIST_COUNT(list)
        { n <= 0:
            ~ return LIST_MIN(list) 
        - else: 
            ~ return getNth(list - LIST_MIN(list), n - 1)
        }
    }
    
```

## 策划参考价值
对话脚本格式的实际案例。展示了分支/条件/变量在叙事脚本中的用法。
