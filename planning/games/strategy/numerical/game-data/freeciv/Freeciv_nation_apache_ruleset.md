# Freeciv(nation) · apache

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/apache.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的apache定义

## 正文
```ruleset
[nation_apache]

translation_domain="freeciv"

name=_("Apache")
plural=_("?plural:Apaches")
groups="American", "Core"
legend=_("The Apaches are a group of Athabascan speaking Indian tribes\
 living in Arizona, New Mexico and Oklahoma. Apache groups include the\
 Western, Chiricahua, Mescalero, Jicarilla, Lipan and Plains Apache.\
 They came from the Far North around 1000 CE. The Apache are known as\
 fierce warriors. In the 19th century it took the United States half a\
 century to subdue them.")

leaders = {
 "name",        "sex"
 "Dasoda-hae",  "Male" ; Mangas Coloradas
 "K'uu-ch'ish", "Male" ; Cochise
 "Goyaałé",     "Male" ; Geronimo
 "Dos-Teh-Seh", "Male" ; Naiche
 "Góyą́ń",       "Female" ; Gouyen
 "Alchesay",    "Male" ; William Alchesay
}

ruler_titles = {
 "government",      "male_title",            "female_title"
 "Fundamentalism",  _("Great Shaman %s"),    _("?female:Great Shaman %s")
 "Monarchy",        _("Great Chief %s"),     _("?female:Great Chief %s")
}

flag = "apache"
flag_alt = "-"
style = "celtic"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations = "navajo"

cities =

;Mescalero Apache:

"Natahéndé",
"Guhlkahéndé",
"Dzithinahndé",
"Ch'laandé",
"Nit'ahéndé",
"Tsehitcihéndé",
"Tsebekinéndé",
"Tahuundé",
"Tuintsundé",
"Tuetinini",

;Lipan Apache:

"Tséral tuétahä",
"Tche shä",
"Cuelcahen Ndé",
"Tchó'kanä",
"Kóke metcheskó lähä",
"Tsél tátli dshä",
"Ndáwe qóhä",
"Shá i'a Nde",
"Tsés tsembai",
"Te'l kóndahä",
"Tu'tssn Ndé",
"Tsésh ke shéndé",
"Tindi Ndé",
"Tcha shka-ózhäye",
"Twid Ndé",
"Zit'is'ti Nde",
"Bi'uhit Ndé",
"Ha'didla'Ndé",
"Zuá Zuá Ndé",

;Jicarilla Apache:

"Sai T'inde",
"Kolkhahin",

;Kiowa Apache bands:

"Na'isha",
"Khat-tleen-deh",

;White Mountain Apache:

"Lunábáha",
"Dził Ghá'",

;Cibecue Apache:

"Gołkizhn",
"Tł'ohk'aa'digaidn",
"Dził T'aadn",

;San Carlos Apache:

"Nadah Dogalniné",
"Tsék'áádn",
"T'iisibaan",
"Tséjiné",
"Tsé Binest'i'é",

;Tonto Apache:

"Dasziné Dasdaayé Indee",
"Tú Dotł'izh Indee",
"Dotł'izhi Ha'it'Indee",
"Tsé Hichii Indee",
"Tsé Nołtł'izhn",
"Dil Zhe'é",

;Chiricahua Apache:

"Chííhénee",
"Ch'úk'ánéń",
"Nédnaa'í",
"Bedonkohe",
"Cho-kon-nen"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
