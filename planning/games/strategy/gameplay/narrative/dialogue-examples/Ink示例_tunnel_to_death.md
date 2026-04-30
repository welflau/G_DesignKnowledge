# Ink脚本示例 · tunnel_to_death

> 来源：inkle/ink-library
> 原始链接：https://github.com/inkle/ink-library
> 分类：gameplay
> 标签：Ink, 叙事工具, 对话脚本, 分支叙事, 通用
> 游戏类型：叙事工具

## 概述
Ink叙事脚本语言的完整示例故事：tunnel_to_death

## 正文
```ink
// This is a simple example of tunnel usage to either continue the story or redirect the flow to a death knot.

VAR hp = 2
LIST deaths = beaten, drown

-> main

=== function is_alive ===
// Condition can be more complex here
~ return hp > 0

=== get_hit(x) ===
~ hp = hp - x
{ is_alive():
    // Everything is alright, continue the story
    ->->
}
// Everything is horribly wrong, redirect the flow to the death knot
-> death(beaten)

=== death(reason) ===
{
- reason ? beaten:
You've been beaten to death.
- reason ? drown:
Sadly you've drown in the water.
- else:
Sorry, you're dead
}
-> END

=== main ===
Should you cross the river?
*   [Yes]
    You enter the river but the stream is stronger than you thought.
    -> death(drown)
*   [No]
    You follow the path along the river for some time and finally encounter a huge man with a wooden stick.
    As you start talking to him, he beats you with his weapon.
    -> get_hit(1) ->
    **  [Fight back]
        You can hit the man once before he throws you a punch.
        -> get_hit(RANDOM(0, 2)) ->
        You manage to block his fist and finally push him into the river.
        After this lengendary fight, you continue your journey and never look back.
    **  [Flee]
        You desperatly run for your life and never look back.
    - -> END
    

```

## 策划参考价值
对话脚本格式的实际案例。展示了分支/条件/变量在叙事脚本中的用法。
