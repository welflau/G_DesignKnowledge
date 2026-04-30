# Freeciv(nation) · guinean

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/guinean.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的guinean定义

## 正文
```ruleset
[nation_guinean]

name=_("Guinean")
plural=_("?plural:Guinean")
groups="African", "Modern"
legend=_("Guinea declared independence from France in 1958. Its first\
 president Ahmed Sékou Touré continued to rule the country until his death\
 in 1984. Guinea is not to be confused with neighboring Guinea-Bissau.")
leaders = {
 "name",                   "sex"
 "Ahmed Sékou Touré",	   "male"
 "Louis Lansana Beavogui", "male"
 "Lansana Conté",          "male"
 "Alpha Condé",            "male"
}
ruler_titles = { "government",     "male_title",         "female_title"
                 "Despotism",      _("General %s"),      _("?female:General %s")
                 "Fundamentalism", _("Grand Mufti %s"),  _("?female:Grand Mufti %s")
	       }
flag="guinea"
flag_alt = "-"
style = "tropical"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations = "fulani", "bissau-guinean"

cities =
 "Conakry",
 "Nzérékoré",
 "Kankan",
 "Kindia",
 "Labé",
 "Guékédou",
 "Boké",
 "Kissidougou",
 "Fria",
 "Faranah",
 "Macenta",
 "Coyah",
 "Kamsar",
 "Mamou",
 "Lalo",
 "Kérouane",
 "Yomou",
 "Siguiri",
 "Forécariah",
 "Dinguiraye",
 "Boffa",
 "Sangaredi",
 "Dabola",
 "Tondon",
 "Télimélé",
 "Koundara",
 "Pita",
 "Beyla",
 "Tokonou",
 "Kouroussa",
 "Dubréka",
 "Sanguéya",
 "Mandiana",
 "Youkounkoun",
 "Gaoual",
 "Dalaba",
 "Lélouma",
 "Mali",
 "Tougué",
 "Koubia"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
