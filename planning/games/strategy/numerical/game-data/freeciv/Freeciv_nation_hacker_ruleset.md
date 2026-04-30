# Freeciv(nation) · hacker

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/hacker.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的hacker定义

## 正文
```ruleset
[nation_hacker]

name=_("Hacker")
plural=_("?plural:Hackers")
groups="Imaginary"
legend=_("h4xx0r r0xx0rz!")

leaders = {
 "name",                "sex"
 "Linus Torvalds",      "Male"
 "Richard Stallman",    "Male"
 "Dennis Ritchie",      "Male"
 "Ken Thompson",        "Male"
 "Robert Pike",         "Male"
 "Donald Knuth",        "Male"
 "Ada Lovelace",        "Female"
 "Grace Murray Hopper", "Female"
 "Jean Sammet",         "Female"
 "Barbara Liskov",      "Female"
 "Julf",                "Male" ; Johan Helsingius
 "Cap'n Crunch",        "Male" ; John Draper
 "Condor",              "Male" ; Kevin Mitnick
 "Dark Dante",          "Male" ; Kevin Poulsen
 "Phiber Optik",        "Male" ; Mark Abene
 "rtm",                 "Male" ; Robert Morris
 "Woz",                 "Male" ; Steve Wozniak
 "Edsger Dijkstra",     "Male"
 "Alan Kay",            "Male"
 "Bjarne Stroustrup",   "Male"
 "Niklaus Wirth",       "Male"
}

ruler_titles = {
 "government",     "male_title",        "female_title"
 "Despotism",      _("?title:Hacker %s"),  _("?female:Hacker %s")
 "Monarchy",       _("?title:1337 %s"),    _("?female:1337 %s")
}

flag="hacker"
flag_alt = "-"
style = "Classical"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="antarctican", "martian"

cities = 
 "Core Dump",
 "Kernel Panic",
 "One More Turn",
 "Segmentation Fault",
 "Stack Overflow",
 "Bus Error",
 "Divide by Zero",
 "Buffer Underrun",
 "Buffer Overrun",
 "NullPointerException",
 "Macro",
 "Assembler",
 "Interpreter",
 "Compiler",
 "Kernel",
 "Shell",
 "Editor",	; Why not "Emacs" ;)
 "Word Processor",
 "Program Counter",
 "Garbage Collection",
 "Deadlock",
 "Named Pipe",
 "Press Any Key To Continue",
 "Multitasking",
 "Crontab",
 "Type Mismatch"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
