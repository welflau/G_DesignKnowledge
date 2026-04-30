# Freeciv(nation) · ambazonian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/ambazonian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的ambazonian定义

## 正文
```ruleset
[nation_ambazonian]

name = _("Ambazonia")
plural = _("?plural:Ambazonians")
groups="African"
legend=_("The struggle for an independent Ambazonia began in 2017\
 with the Anglophone crisis.")
leaders = {
 "name",                          "sex"
 "Emmanuel Mbela Lifafa Endeley", "Male"   ; (1916-1988) First Premier of British Southern Cameroons
 "Grace Mafuatem",                "Female" ; Mother of Lekea Oliver and Chris Anu
 "Lekeaka Oliver",                "Male"   ; (1968-2022) Leader of the Red Dragon militia
 "Ayuk Ndifon Defcam",            "Male"   ; (????-2023) Known as General Transporter
 "Clement Mbashie",               "Male"   ; (????-2023) Known as General No Pity
 "Chris Anu",                     "Male"   ; Brother of Lekeaka Oliver
}

ruler_titles = {
 "government",      "male_title",                 "female_title"
 "Despotism",       _("Field Marshall %s"),       _("?female:Field Marshall %s")
 "Monarchy",        _("Baron %s"),                _("?Baroness %s")              
 "Communism",       _("Paramount Ruler %s"),      _("?female:Paramount Ruler %s")
}

flag = "ambazonia"
flag_alt = "greece"  ; Looks similar. Greece uses greece_ancient by default
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="cameroonian", "nigerian", "biafran"

cities =
 "Buea",
 "Bamenda",
 "Kumba",
 "Bafut",
 "Bali",
 "Limbé",
 "Wum",
 "Tiko",
 "Kumbo",
 "Mutengene",
 "Buea",
 "Fundong",
 "Fontem",
 "Mbanga",
 "Muyuka",
 "Ndop",
 "Mamfe",
 "Nkambe",
 "Mbengwi",
 "Batibo",
 "Bambili",
 "Ako",
 "Bangem",
 "Eyumojock",
 "Idenau",
 "Menji",
 "Ndu",
 "Santa",
 "Mbanga"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
