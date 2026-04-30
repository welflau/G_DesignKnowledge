# Freeciv(nation) · cyrenaican

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/cyrenaican.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的cyrenaican定义

## 正文
```ruleset
[nation_cyrenaican]

name=_("Cyrenaican")
plural=_("?plural:Cyrenaicans")
groups="African"
legend=_("Cyrenaica is a historical region in Eastern Libya. In Classical\
 Antiquity the region was part of the Greek cultural realm. From the 7th\
 century onwards the region was controlled by various Arab dynasties.\
 Cyrenaica was occupied by Italy in 1911. After World War II a short-lived\
 Emirate of Cyrenaica existed, of which the ruling Senussi dynasty\
 established a united Libyan Kingdom in 1951. Cyrenaica has been a hotbed\
 of resistance against the Gaddafi regime. The site of much of Libya's\
 oil reserves, Cyrenaica has seen renewed calls for autonomy following the\
 overthrow of Gaddafi.")

leaders = {
 "name",                "sex"
 "Sharif el-Gariani",   "Male"
 "Fatima el-Sharif",    "Female"
 "Muhammad Idris",      "Male"
 "Ahmed al-Senussi",    "Male"
}

ruler_titles = {
 "government",      "male_title",      "female_title"
 "Despotism",       _("Sheikh %s"),    _("Shaykha %s")
 "Fundamentalism",  _("Mullah %s"),    _("?female:Mullah %s")
 "Monarchy",        _("Emir %s"),      _("Emira %s")
}

flag ="cyrenaica"
style = "Classical"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations = "amazigh", "libyan"

cities =
 "Binghazi",
 "Tubruq",
 "Ajdabiya",
 "Al-Bayda",
 "Al-Marj",
 "Darna",
 "Al-Jawf",
 "Al-Ayba",
 "Shahada",
 "Zawiyat Bishara",
 "Tukra",
 "Suluq",
 "Jalu",
 "Susa",
 "Marsa al-Burayqa",
 "Qaminis",
 "At-Tamimi",
 "Jiharra",
 "Awjila",
 "Sidi Halifa",
 "Daryana",
 "Bi'r al-Ashab",
 "Zahr-al-Huwayr",
 "Al-Gijab",
 "Jardas al-'Abid",
 "Umm Mus'id",
 "Al-Labraq",
 "Barsis",
 "Al-Bardi",
 "An-Nawagiya",
 "Taknis",
 "Al-Jagbub",
 "Qaryat Bashir",
 "Massa",
 "'Ain Mara",
 "Masliwa",
 "Al-Hawwari",
 "Bu Maryam",
 "Talmita",
 "Mudiriyat Matruba",
 "Tubat",
 "Batta",
 "Harat 'Affun",
 "Ash-Shawashna",
 "Kambut",
 "Jardina",
 "Marada",
 "Faidiya",
 "Sulunta",
 "Az-Zuwaytina",
 "Qimada",
 "Qandula",
 "Matruba",
 "Lamluka",
 "Karsa"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
