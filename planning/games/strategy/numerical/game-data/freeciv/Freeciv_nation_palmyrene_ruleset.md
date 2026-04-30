# Freeciv(nation) · palmyrene

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/palmyrene.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的palmyrene定义

## 正文
```ruleset
[nation_palmyrene]

name=_("Palmyrene")
plural=_("?plural:Palmyrenes")
groups= "Asian", "Ancient"
legend=_("Palmyra was a breakaway Roman state in Asia governed by queen\
 Zenobia. In 273 CE Aurelian brought it back under Roman control.")

leaders = {
 "name",                        "sex"
 "Septimius Odaenathus",        "Male"
 "Septimia Zenobia",            "Female"
 "Vabalathus",                  "Male"
 "Cassius Longinus",            "Male"
}

ruler_titles = {
 "government",      "male_title",      "female_title"
 "Anarchy",         _("Usurper %s"),   _("?female:Usurper %s")
 "Despotism",       _("Dictator %s"),  _("Dictatrix %s")
 "Republic",        _("Consul %s"),    _("?female:Consul %s")
}

flag="palmyra"
flag_alt = "-"
style = "Classical"

init_techs=""
init_buildings=""
init_units=""

conflicts_with = "byzantine", "syrian", "aramean"
civilwar_nations = "roman", "aramean", "israelite"

cities =
 "Palmyra",
 "Dura Europus",
 "Heliopolis",
 "Beroea",
 "Damascus",
 "Alexandria",
 "Memphis",
 "Caesarea Palestina",
 "Antiochia ad Orontem",
 "Petra",
 "Byzantium",
 "Tyrus",
 "Aelia Capitolina Hierosolyma",
 "Tripolis",
 "Tarsus",
 "Edessa",
 "Cyrrhus",
 "Nova Traiana Bostra",
 "Gaza",
 "Emesa",
 "Samaria",
 "Caesarea in Cappadocia",
 "Nicopolis",
 "Sinope",
 "Raphaneae",
 "Zeugma",
 "Apamea",
 "Carrhae",
 "Laodicea",
 "Samosata",
 "Resafa",
 "Trapezus",
 "Ancyra",
 "Sura",
 "Heracleopolis",
 "Nicaea",
 "Dara",
 "Nisibis",
 "Amasis",
 "Nicomedia",
 "Amisus",
 "Metilene",
 "Satala"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
