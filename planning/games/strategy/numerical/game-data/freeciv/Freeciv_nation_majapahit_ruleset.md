# Freeciv(nation) · majapahit

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/majapahit.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的majapahit定义

## 正文
```ruleset
[nation_majapahit]

name=_("Majapahit")
plural=_("?plural:Majapahit")
groups="Asian", "Medieval"

legend=_("This empire began in 1293 CE when a local prince used invading\
 Yuan dynasty troops to his own advantage by having them defeat his\
 enemies and then expelling them. The Majapahit, centered in eastern Java,\
 was heavily influenced by Buddhism and Hinduism and was a major regional\
 power in the insular Southeast Asian world, a position which allowed them\
 to control much of the trade between China, India and the Middle East.\
 They lasted until 1500 when they were eclipsed by the Sultanate of\
 Malacca and the rise of Islam in the Indonesian world.")

leaders = {
 "name",                "sex"
 "Suhita",              "Female"
 "Hayam Wuruk",         "Male" ; Throne name: Rajasanagara.
 "Dyah Gitarja",        "Female" ; Throne name: Tribhuwana Wijayatunggadewi.
 "Gajah Mada",          "Male"
 "Raden Wijaya",        "Male" ; Throne name: Nararya Sangramawijaya.
}

ruler_titles = {
 "government",      "male_title",        "female_title"
 "Despotism",       _("Raja %s"),        _("Rani %s")
 "Monarchy",        _("Maharaja %s"),    _("Maharani %s")
}

flag         = "majapahit"
flag_alt     = "-"
style        = "Tropical"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="Sri Vijaya", "indonesian", "malaysian", "bruneian"

cities =
 "Majapahit",
 "Kediri",
 "Batu",
 "Madiun",
 "Surabaya",
 "Malang",
 "Blitar",
 "Pasuruan",
 "Probolinggo",
 "Mojokerto",
 "Bandung",
 "Bekasi",
 "Karawang",
 "Purwakarta",
 "Subang",
 "Indramayu",
 "Bodjanegara",
 "Sumedang",
 "Majalengka",
 "Sumber",
 "Kuningan",
 "Ciamis",
 "Sukoharjo",
 "Garut",
 "Purbalingga",
 "Cianjur",
 "Pelabuhan Ratu",
 "Cibinong",
 "Bogor",
 "Sukabumi",
 "Bandung",
 "Cirebon",
 "Klaten",
 "Depok",
 "Wonosobo",
 "Tasikmalaya",
 "Banjar",
 "Jepara",
 "Blora",
 "Minangkabau"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
