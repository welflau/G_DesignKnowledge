# Freeciv(nation) · paeonian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/paeonian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的paeonian定义

## 正文
```ruleset
[nation_paeonian]

name=_("Paeonian")
plural=_("?plural:Paeonians")
groups="Ancient", "European"
legend=_("The Paeonians were an ancient people that inhabited the areas\
 north of Macedon, between the Thracian and Illyrian tribes. Their\
 language probably had a mixed Thraco-Illyrian origin. The seat of the\
 Paeonian kings was Bylazora. In 360-359 BCE, southern Paeonian tribes\
 launched raids into Macedon, but the Macedons defeated and\
 conquered them. A Paeonian military contingent participated in the\
 expedition of Alexander the Great to Persia.")
leaders = {
"name",                "sex"
"Agis",                "Male"
"Lykkeios",            "Male"
"Patraos",             "Male"
"Audoleon",            "Male"
"Ariston",             "Male"
"Dropion",             "Male"
"Bastareios",          "Male"
}
flag="paeonia"
flag_alt = "-"
style = "Celtic"

init_techs=""
init_buildings=""
init_units=""

conflicts_with="yugoslav", "macedonian", "serbian", "albanian", "bulgarian",
 "hellenic", "kosovar"
civilwar_nations = "macedon", "thracian", "illyrian"

cities =
  "Bylazora",
  "Antigoneia",
  "Stobi",
  "Damastion",
  "Alalkomenai",
  "Damastion",
  "Idomenai",
  "Bargala",
  "Astibo",
  "Gordynia",
  "Estipeion",
  "Norakos",
  "Deuriopos",
  "Europos",
  "Perseis"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
