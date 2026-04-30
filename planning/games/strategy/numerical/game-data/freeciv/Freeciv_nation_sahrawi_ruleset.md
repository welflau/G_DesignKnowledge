# Freeciv(nation) · sahrawi

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/sahrawi.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的sahrawi定义

## 正文
```ruleset
[nation_sahrawi]

name=_("Sahrawi")
plural=_("?plural:Sahrawis")
groups="African", "Modern"
legend=_("The Sahrawi are the inhabitants of the Western Sahara, a former\
 Spanish colony. Morocco currently controls most of the area, which is\
 considered an illegal occupation by most of the international community.\
 The Moroccan Army and Sahrawi Polisario rebels have been fighting each\
 other since 1975.")

leaders = {
 "name",                        "sex"
 "Muhammad Bassiri",            "Male"
 "El-Ouali Mustapha Sayed",     "Male"
 "Mohamed Abdelaziz",           "Male"
 "Aminatou Haidar",             "Female"
}
ruler_titles = {
 "government",      "male_title",            "female_title"
 "Fundamentalism",  _("Caliph %s"),          _("Calipha %s")
}
flag="sadr"
flag_alt = "-"
style = "Babylonian"

init_techs=""
init_buildings=""
init_units=""
conflicts_with="palestinian" ;similar flag
civilwar_nations="moroccan", "mauritanian"

cities =
 "Al-Ayun",
 "Bir Lehlu",
 "Ad-Dakhla",
 "Smara",
 "Ras Bujadur",
 "El Marsa",
 "Hawza",
 "Al-Mahbass",
 "Guelta Zemmur",
 "Bir Anzarane",
 "Tichla",
 "Awserd",
 "El Argub",
 "La Gouria",
 "Zug",
 "Guerguerat",
 "Tifariti",
 "Dougaj",
 "Agounit",
 "Amgala",
 "Meharrize",
 "Boukra",
 "Lemseid",
 "Umm Dreiga",
 "Jdiriya",
 "Zbayra",
 "Chalwa",
 "Aridal",
 "As-Sakn",
 "Al-Ga'ada",
 "Bir Qanduz"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
