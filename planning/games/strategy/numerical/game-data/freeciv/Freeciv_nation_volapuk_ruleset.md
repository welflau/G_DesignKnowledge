# Freeciv(nation) · volapuk

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/volapuk.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的volapuk定义

## 正文
```ruleset
[nation_volapuk]

name=_("Volapükan")
; pre-2.6 had plain ASCII names
rule_name="Volapukan"
plural=_("?plural:Volapükans")
groups="Imaginary"
legend=_("Volapük is an international auxiliary language constructed by\
 the German priest Johann Martin Schleyer in 1879. It enjoyed a brief\
 popularity in the late 19th century. The language is often considered\
 unnecessarily complex when compared with alternatives like Esperanto,\
 which had almost completely displaced Volapük by the turn of the\
 century. Today only a few dozen Volapük speakers remain.")

leaders = {
 "name",                   "sex"
 "Johann Martin Schleyer", "Male"
 "Charles E. Sprague",     "Male"
 "Corinne Cohn",           "Female"
 "Auguste Kerckhoffs",     "Male"
 "Arie de Jong",           "Male"
 "Brian Reynold Bishop",   "Male"
}

flag="volapuk"
flag_alt = "-"
style = "Classical"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations = "esperant", "lojbanistani"

cities =
 "Volapükazif",
 "Zif Nulik",
 "Kongredazif",
 "Sabajol (ocean)",
 "Nolübels (mountains)",
 "Fälid Vienöfik (plains, grassland)",
 "Yebalänedaflum",
 "Delaprim",
 "Flumed Feragik (river)",
 "Leig",
 "Bel Liegik (mountains)",
 "Kien Stäga Deadik",
 "Lufut Bera",
 "Stäg Fibik",
 "Bel Lupa (mountains)",
 "Neif Dölik",
 "Smaglehon",
 "Blövat (ocean)",
 "Gur Biadas",
 "Lak Boadagik (forest)",
 "Lubel Viestona (hills)",
 "Lak Bobuba Deadik",
 "Luflum Vieböda (river)",
 "Vat Kleilik (ocean)",
 "Glehog",
 "Lubel Peinagik",
 "Püd",
 "Spel",
 "Glebel",
 "Grüfot",
 "Blülak (river)",
 "Relak (river)",
 "Bläbel",
 "Nifabel",
 "Viestonabel",
 "Bödaflum",
 "Gleflum",
 "Banakased su Flumed (river)",
 "Gleflumed (river)",
 "Kased Nulik ko Mel (ocean)",
 "Menad Bal",
 "Pük Bal"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
