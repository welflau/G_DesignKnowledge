# Ink脚本示例 · print_num

> 来源：inkle/ink-library
> 原始链接：https://github.com/inkle/ink-library
> 分类：gameplay
> 标签：Ink, 叙事工具, 对话脚本, 分支叙事, 通用
> 游戏类型：叙事工具

## 概述
Ink叙事脚本语言的完整示例故事：print_num

## 正文
```ink
// Print numbers out in English.
You have {print_num(58)} coins.

=== function print_num(x) 
{
    - x >= 1000:
        {print_num(x / 1000)} thousand { x mod 1000 > 0:{print_num(x mod 1000)}}
    - x >= 100:
        {print_num(x / 100)} hundred { x mod 100 > 0:and {print_num(x mod 100)}}
    - x == 0:
        zero
    - else:
        { x >= 20:
            { x / 10:
                - 2: twenty
                - 3: thirty
                - 4: forty
                - 5: fifty
                - 6: sixty
                - 7: seventy
                - 8: eighty
                - 9: ninety
            }
            { x mod 10 > 0:
                <>-<>
            }
        }
        { x < 10 || x > 20:
            { x mod 10:
                - 1: one
                - 2: two
                - 3: three
                - 4: four
                - 5: five
                - 6: six
                - 7: seven
                - 8: eight
                - 9: nine
            }
        - else:
            { x:
                - 10: ten
                - 11: eleven
                - 12: twelve
                - 13: thirteen
                - 14: fourteen
                - 15: fifteen
                - 16: sixteen
                - 17: seventeen
                - 18: eighteen
                - 19: nineteen
            }
        }
}   
```

## 策划参考价值
对话脚本格式的实际案例。展示了分支/条件/变量在叙事脚本中的用法。
