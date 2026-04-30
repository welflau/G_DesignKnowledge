# Ink脚本示例 · swings

> 来源：inkle/ink-library
> 原始链接：https://github.com/inkle/ink-library
> 分类：gameplay
> 标签：Ink, 叙事工具, 对话脚本, 分支叙事, 通用
> 游戏类型：叙事工具

## 概述
Ink叙事脚本语言的完整示例故事：swings

## 正文
```ink
// Functions for tracking character relationships.
// This is the exact file as used in Heaven's Vault.
// TODO: Some examples of usage.


CONST INITIAL_SWING = 1001

=== function swing_ready(x) 
    ~ return (upness(x) + downness(x)) > 3

=== function raise(ref x)
	~ x = x + 1000
	

=== function push(ref x)
	~ raise(x)
	

=== function bump(ref x)
    ~ raise(x)
    ~ raise(x)
    ~ raise(x)

=== function lower(ref x)
	~ x = x + 1 

== function ditch (ref x) 
    ~ lower(x) 
    ~ lower(x) 
    ~ lower(x)

=== function demolish(ref x)
    ~ x = x + 20
    
=== function escalate(ref x)
    ~ x = x + (20 * 1000)

=== function pull(ref x)
	~ lower(x)
	

=== function upness(x)
	~ return x / 1000

=== function downness(x)
	~ return x % 1000


=== function high(x)
    ~ return (1 * upness(x) >= downness(x) * 9)

=== function up(x)
	~ return swing_ready(x) && (4 * upness(x) >= downness(x) * 6)

=== function down(x)
	~ return swing_ready(x) && (6 * upness(x) <= downness(x) * 4)
	
=== function low(x)
	~ return swing_ready(x) && (9 * upness(x) <= downness(x) * 1)
	
=== function mid(x)
    // not swing_ready -> true 
    // because up is false and down is false
    ~ return (not up(x) && not down(x))
```

## 策划参考价值
对话脚本格式的实际案例。展示了分支/条件/变量在叙事脚本中的用法。
