# Freeciv(nation) · lesothoan

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/lesothoan.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的lesothoan定义

## 正文
```ruleset
[nation_lesothoan]

name=_("Lesothoan")
plural=_("?plural:Lesothoans")
groups="African", "Modern"
legend=_("Lesotho first formed a unified polity in the early 19th century\
 under king Moshoeshoe I, who united the Sotho clans. Moshoeshoe sought\
 protection from the British against Boer incursions and in 1869 the\
 country turned into the British protectorate of Basutoland. Although\
 surrounded by South Africa on all sides, that country's apartheid\
 policies prevented its integration into South Africa. In 1966 Basutoland\
 became the independent Kingdom of Lesotho.")

leaders = {
 "name",                     "sex"
 "Moshoeshoe I",             "Male"
 "Lerotholi",                "Male"
 "Mantsebo Amelia 'Matsaba", "Female"
 "Leabua Jonathan",          "Male"
 "Moshoeshoe II",            "Male"
 "Ntsu Mokhehle",            "Male"
 "Letsie III",               "Male"
}

flag="lesotho"
flag_alt = "-"
style = "Celtic"

init_techs=""
init_buildings=""
init_units=""

conflicts_with="sotho"
civilwar_nations="zulu", "xhosa", "tswana"

cities =
 "Maseru",
 "Teyateyaneng",
 "Mafeteng",
 "Mohale's Hoek",
 "Hlotse", ;leribe
 "Quthing",
 "Butha-Buthe",
 "Qacha's Nek",
 "Mokhotlong",
 "Thaba-Tseka",
 "Maputsoa",
 "Peka",
 "Roma",
 "Thaba Bosiu",
 "Nyakosoba",
 "Nkoebe",
 "Seshote",
 "Khomo-Phatsoa",
 "Makhunoane",
 "Semonkong",
 "White-Hill",
 "Makhalaneng",
 "Monyake",
 "Malumeng",
 "Seforong",
 "Rafolatsane",
 "Mosetoa",
 "Kao",
 "Makheka",
 "Mabote",
 "Manka",
 "Nazareth",
 "Mantsonyane",
 "Ha Baroana",
 "Marakabei"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
