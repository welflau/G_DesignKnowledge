# Freeciv(nation) · khmer

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/khmer.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的khmer定义

## 正文
```ruleset
[nation_khmer]

translation_domain="freeciv"

name=_("Khmer")
plural=_("?plural:Khmers")
groups="Asian", "Medieval", "Core"
legend=_("The Khmer Empire, established in 802 CE, dominated Southeast\
 Asia for many centuries during the Middle Ages. Heavily influenced by\
 Indian culture, the Khmers were great builders who erected innumerable\
 stone temples to Hindu deities. The Khmers today are the majority\
 ethnicity of Cambodia.")

leaders = {
 "name",                "sex"
 "Jayavarman VII",      "Male"
 "Suryavarman II",      "Male"
 "Suryavarman I",       "Male"
 "Jayavarman II",       "Male"
 "Jayavedi",            "Female"
 "Ishanavarman",        "Male"
}

ruler_titles = {
 "government",      "male_title",        "female_title"
 "Despotism",       _("Raja %s"),        _("Rani %s")
 "Monarchy",        _("Maharaja %s"),    _("Maharani %s")
 "Communism",       _("Brother %s"),     _("Sister %s")
}

flag="khmer"
flag_alt = "-"
style = "Asian"

init_techs=""
init_buildings=""
init_units=""

conflicts_with="Cambodian"
civilwar_nations="Mon", "Cham"

cities =
 "Shreshthapura",
 "Ishanapura",
 "Indrapura",
 "Hariharalaya",
 "Yasodharapura",
 "Mahendraparvata",
 "Vyadhapura",
 "Koh Ker",
 "Jayenanagari",
 "Angkor Thom",
 "Kompong Svay",
 "Vat Nokor",
 "Bati",
 "Phnom Chisor",
 "Beng Melea",
 "Vat Banon",
 "Banteay Chmar",
 "Muang Tam",
 "Preah Vihear",
 "Vat Phu",
 "Sikhoraphum",
 "Phimai",
 "Roy Et",
 "Prasat Kamphaeng Yai",
 "Phra Phang Sam Yod",
 "Muang Sing"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
