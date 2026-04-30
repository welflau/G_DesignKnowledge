# Freeciv(nation) · laotian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/laotian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的laotian定义

## 正文
```ruleset
[nation_laotian]

name=_("Laotian")
plural=_("?plural:Laotians")
groups="Modern", "Early Modern", "Medieval", "Asian"
legend=_("The history of Laos starts with the Lan Xang kingdom\
 created in the 14th century and ended in late 18th century\
 with invasion of Siam (Thailand). In the end of the 19th\
 century, Laos became part of French Indochina.\
 French rule ended with independence in 1946 followed\
 by 30 years of civil war. In 1975 the communist Pathet\
 Lao established a strict socialist regime. However,\
 in 1986 the liberalization and a gradual return to\
 private enterprise started.")

leaders = {
 "name",                "sex"
 "Khun Lo",             "Male" ; first laotian king.
 "Fa Ngum",             "Male" ; king of Lan Xang kingdom.
 "Samsenethai",         "Male"
 "Visunarat",           "Male"
 "Photisarath",         "Male"
 "Setthathirath",       "Male"
 "Sourigna Vongsa",     "Male"
 "Anouvong",            "Male"
 "Phetsarath",          "Male" ; founder of modern Laos state.
 "Kaysone Phomvihane",  "Male" ; prime minister and president of Laos.
 "Souphanouvong",       "Male" ; president of Laos.
}

flag="laos"
flag_alt = "-"
style = "Asian"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations = "thai", "cambodian", "burmese", "vietnamese"

cities =
 "Vientiane", ; Viangchan
 "Louangphrabang", ; Luang Prabang
 "Pakxe",
 "Samakkhixai", ; Attapu
 "Saravan", ; Salavan
 "Khanthabouri",
 "Savannakhet",
 "Thakhek", ; Muang Khammouan
 "Pakxan", ; Muang Pakxan
 "Phongsali",
 "Xaisomboun", ; Ban Mouang Cha
 "Xam-Nua",
 "Houayxay", ; Ban Houayxay
 "Xaignabouri", ; Xaignabouli
 "Xai", ; Muang Xai
 "Louang-Namtha",
 "Khong", ; Muang Khong
 "Champasak",
 "Laman", ; Lamarn
 "Pek",
 "Wang Tao",
 "Phin", ; Muang Phin
 "Xepon", ; Muang Xepon
 "Champhon",
 "Nam Phao", ; Ban Na Phao
 "Pakkading",
 "Nakay",
 "Borikhan",
 "Vangviang",
 "Phonhong", ; Muang Phon-Hong
 "Khoun",
 "Kham",
 "Phoukout",
 "Xiangkho",
 "Xiang-Ngeun",
 "Xam-Tai",
 "Chomphet",
 "Xaithani",
 "Phoukhoun", ; Ban Phoukhoun
 "Boun Nua",
 "Pha-Oudom",
 "Pakbeng", ; Muang Pakbeng
 "Boten",
 "Long",
 "Sing"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
