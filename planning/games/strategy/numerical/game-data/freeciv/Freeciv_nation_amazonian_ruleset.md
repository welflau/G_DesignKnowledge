# Freeciv(nation) · amazonian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/amazonian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的amazonian定义

## 正文
```ruleset
[nation_amazonians]

name=_("Amazonian")
plural=_("?plural:Amazons")
groups="Imaginary"
legend=_("The Amazons are a fictional nation of women warriors \
which appear in Classical Greek writing and art. Authors have located \
them in the Ukraine, Asia Minor, or Libya. The Amazons were reported \
to remove their right breasts in order to better use the bow and other \
weapons.")

leaders = {
 "name",                "sex"
 "Penthesilea",         "Female"
 "Hippolyta",           "Female"
 "Semiramis",           "Female"
 "Myrine",              "Female"
 "Thalestris",          "Female"
 "Antianara",           "Female"
 "Antiope",             "Female"
}

flag="amazon"
flag_alt = "-"
style = "Classical"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations = "Turkish"

cities =
    "Pontus", "Smyrna", "Ephesus", "Sinope", "Paphos", "Themiscyra", 
	"Cyme", "Myrine", "Pitane", "Mytilene", "Priene", "Megara",
	"Chaeronea", "Chalcis", "Scotussa", "Cynoscephalae", "Athens",
	"Palus Maeotis"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
