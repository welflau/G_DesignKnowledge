# Freeciv(nation) · bangladeshi

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/bangladeshi.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的bangladeshi定义

## 正文
```ruleset
[nation_bangladeshi]

name=_("Bangladeshi")
plural=_("?plural:Bangladeshis")
groups="Modern", "Asian"
legend=_("The People's Republic of Bangladesh was formed from the former\
 Pakistani territory of East Bengal following a war of independence.")

leaders = {
 "name",                   "sex"
 "Siraj ud-Daulah",        "Male"
 "Ziaur Rahman",           "Male"
 "Sheikh Mujibur Rahman",  "Male"
 "Maulana Bhashani",       "Male"
 "Hussain Muhammad Ershad", "Male"
 "Khaleda Zia",            "Female"
}

ruler_titles = {
 "government",     "male_title",         "female_title"
 "Despotism",      _("Raja %s"),         _("Rani %s")
 "Monarchy",       _("Maharaja %s"),     _("Maharani %s")
 "Republic",       _("Nabob %s"),        _("?female:Nabob %s")
 "Fundamentalism", _("Mullah %s"),       _("?female:Mullah %s")
}

flag="bangladesh"
flag_alt = "-"
style = "Asian"

init_techs=""
init_buildings=""
init_units=""

conflicts_with="Bengali"
civilwar_nations="Sikkimese", "Assamese"

cities =
 "Dhaka",
 "Chittagong",
 "Khulna",
 "Rajshahi",
 "Tongi",
 "Sylhet",
 "Rangpur",
 "Mymensingh",
 "Narayangonj",
 "Barisal",
 "Jessore",
 "Comilla",
 "Nawabganj",
 "Dinajpur",
 "Bogra",
 "Kadamrasul",
 "Madhabdi",
 "Sirajganj",
 "Tangail",
 "Brahmanbaria",
 "Gazipur",
 "Savar",
 "Naogaon",
 "Jamalpur",
 "Pabna Sadar",
 "Feni",
 "Saidpur",
 "Faridpur",
 "Magura",
 "Chandpur"


```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
