# Freeciv(nation) · hungarian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/hungarian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的hungarian定义

## 正文
```ruleset
[nation_hungarian]

name=_("Hungarian")
plural=_("?plural:Hungarians")
groups="Medieval", "Early Modern", "Modern", "European"
legend=_("Legend says that Hungary was founded by Arpad in the 9th\
 century.")

leaders = {
 "name",                "sex"
 "Árpád",               "Male"
 "Szent István",        "Male"
 "Károly Róbert",       "Male"
 "Hunyadi Mátyás",      "Male"
 "Mária Terézia",       "Female"
 "Batthyány",           "Male"
 "Béla IV",             "Male"
}

flag="hungary"
flag_alt = "-"
style = "European"

init_techs=""
init_buildings=""

init_units=""

conflicts_with="indian", "austriahungary"	; Has a similar flag to India
civilwar_nations = "transylvanian", "croatian", "slovakian"

cities =
 "Budapest", "Debrecen", "Székesfehérvár", "Kolozsvár", "Szeged",
 "Kassa", "Pécs", "Pozsony", "Miskolc", "Nagyvárad", "Gyõr",
 "Esztergom", "Temesvár", "Komárom", "Nyíregyháza", "Marosvásárhely",
 "Sopron", "Szabadka", "Kecskemét", "Veszprém", "Besztercebánya",
 "Békéscsaba", "Munkács", "Eger", "Eperjes", "Gyulafehérvár", "Kaposvár",
 "Szolnok", "Paks", "Zalaegerszeg", "Arad", "Szombathely",
 "Mohács", "Hatvan", "Selmecbánya", "Keszthely", "Ungvár", "Szekszárd",
 "Sárospatak", "Tatabánya", "Baja", "Szigetvár", "Csíkszereda",
 "Nagykanizsa", "Hódmezõvásárhely", "Siklós", "Érsekújvár", "Pápa",
 "Gyöngyös",  "Dunaújváros", "Szatmárnémeti", "Szentes",
 "Mosonmagyaróvár",  "Léva", "Szarvas", "Csáktornya",
 "Mátészalka", "Tata", "Nagykõrös", "Nagyszeben",
 "Salgótarján", "Újvidék", "Siófok", "Losonc", "Gyula",
 "Sátoraljaújhely", "Déva", "Tapolca", "Tiszaújváros", "Dombóvár",
 "Püspökladány", "Balatonfüred", "Vác"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
