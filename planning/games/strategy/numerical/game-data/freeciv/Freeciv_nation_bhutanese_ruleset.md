# Freeciv(nation) · bhutanese

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/bhutanese.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的bhutanese定义

## 正文
```ruleset
[nation_bhutanese]

name=_("Bhutanese")
plural=_("?plural:Bhutanese")
groups="Early Modern", "Modern", "Asian"
legend=_("Located in the Himalayas, Bhutan is one of the most isolated\
 countries in the world. Bhutan has not been conquered or occupied\
 by foreign invaders for a millennium if not more. In the 17th century\
 Bhutan became a unified nation under Shabdrung Ngawang Namgyal, who\
 repelled a Mongol invasion and united the rivaling Bhutanese tribes.")

leaders = {
 "name",                        "sex"
 "Guru Rinpoche",               "Male"
 "Phajo Drugom Zhigpo",         "Male"
 "Shabdrung Ngawang Namgyal",   "Male"
 "Gyalse Tenzin Rabgye",        "Male"
 "Ugyen Wangchuck",             "Male"
 "Jigme Dorji Wangchuck",       "Male"
 "Jigme Singye Wangchuck",      "Male"
}

ruler_titles = {
 "government",      "male_title",          "female_title"
 "Fundamentalism",  _("Lama %s"),           _("?female:Lama %s")
 "Monarchy",        _("Dragon King %s"),    _("Dragon Queen %s")
}

flag="bhutan"
flag_alt = "-"
style = "Asian"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations = "tibetan", "nepali"

cities =
 "Punakha", ;ancient capital
 "Thimpu", ;modern capital
 "Chhukha",
 "Samtse",
 "Tashigang",
 "Gelegphug",
 "Samdrup Jongkhar",
 "Monggar",
 "Paro",
 "Wangdue Phodrang",
 "Damphu",
 "Zhemgang",
 "Daga",
 "Trashi Yangtse",
 "Jakar",
 "Lhuntse",
 "Pamagatshel",
 "Tongsa",
 "Ha",
 "Gasa",
 "Phuentsholing",
 "Trashigang",
 "Taga Dzong",
 "Trongsa",
 "Gedu",
 "Bumthang",
 "Gomtu",
 "Deothang",
 "Sarpang",
 "Tsimalakha",
 "Gyalposhing",
 "Dala",
 "Kanglung",
 "Khaling",
 "Tsimasham",
 "Namglam",
 "Jomotsangkha",
 "Sipsu",
 "Lingithang",
 "Lhamoyzingkhar",
 "Tingtibi",
 "Nankhor",
 "Rangjung",
 "Wamrong",
 "Bondey",
 "Drukyegang",
 "Dremtse",
 "Nobding",
 "Samdrup Choeling",
 "Panbang",
 "Rurichu",
 "Gypsum",
 "Autsho",
 "Duksum",
 "Khotakakpa",
 "Reserboo",
 "Dagapela",
 "Kherigonpa",
 "Sunkosh",
 "Mongling",
 "Yalang"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
