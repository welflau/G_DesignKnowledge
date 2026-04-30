# Freeciv(nation) · riffian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/riffian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的riffian定义

## 正文
```ruleset
[nation_riffian]

name=_("Riffian")
plural=_("?plural:Riffians")
groups="African"
legend=_("The Confederal Republic of the Tribes of the Rif was a short-lived\
 nation founded in September 1921 when Riffians revolted against the Spanish\
 and Moroccans. The country was conquered by the Spanish and French in\
 1926. The area is now part of Morocco.")

leaders = {
 "name",                "sex"
 "Abd el-Krim",         "Male" ; First president
 "Hajj Hatmi",          "Male" ; Prime minister 1923 - 1926
 "Mohammed Ameziane",   "Male" ; 19th century freedom fighter
}

ruler_titles = {
 "government",     "male_title",         "female_title"
 "Fundamentalism", _("Imam %s"),            _("Imama %s")
 "Monarchy",       _("Emir %s"),            _("Emira %s")
 "Despotism",      _("%s Pasha"),           _("?female:%s Pasha")
}

flag="rif"
flag_alt = "-"
style = "Classical"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="Spanish", "French", "Moroccan"

cities =
 "Ajdir",
 "Nador",
 "Al Hoceima", ; a.k.a. Biya
 "Azghenghan",
 "Selwan",
 "Tawrirt",
 "Taza",
 "El Jebha",
 "Tetouan",
 "Saïdia",
 "Ras El Ma",
 "Kariet Arkmane",
; Misc. localities in the Rif region
 "Ait Kamara",
 "Annual",
 "Fnideq",
 "Bouanqoud",
 "Aknoul",
 "Tara Tazougaght",
 "Bord",
 "Tastite",
 "Kassita",
 "Tamjount",
 "Tisliouine",
 "Imzouren",
 "Khadab",
 "Mezguitem",
 "Ras Kebdana",
 "Targist",
 "Temsaman",
 "Bouadia",
 "Imezzean",
 "Imbrabden",
 "Ikecheouen"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
