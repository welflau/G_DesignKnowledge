# Freeciv(nation) · ghana

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/ghana.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的ghana定义

## 正文
```ruleset
[nation_ghana]

name=_("Ghana")
plural=_("?plural:Ghana")
groups="African", "Medieval"
legend=_("The Ghana or Wagadou Empire existed in West Africa from the\
 9th to the 13th centuries CE. It takes its name from the king, whose title\
 \'ghana\' means \'great warrior\'. The Ghana Empire grew rich thanks to the\
 trans-Saharan trade and the goldmines in its territory. The modern\
 Republic of Ghana takes its name from the Ghana Empire, even though the\
 empire was located in what is now Mali and Mauretania.")
leaders = {
 "name",              "sex"
 "Majan Dyabe Cisse", "male"
 "Bassi",             "male"
 "Tunka Menin",       "male"
 "Soumaba Cisse",     "male"
}

flag="ghana_ancient"
flag_alt = "ghana"
style = "Babylonian"

ruler_titles = { "government",      "male_title",      "female_title"
                 "Monarchy",        _("Ghana %s"),      _("?female:Ghana %s")
	       }

init_techs=""
init_buildings=""
init_units=""

conflicts_with = "malian"
civilwar_nations = "mali", "jolof", "songhai"

cities =
 "Kumbi Saleh",
 "Sama",
 "Bure",
 "Walata",
 "Bamako",
 "Segu",
 "Morfil",
 "Awdaghost",
 "Sosso",
 "Kirina",
 "Auker",
 "Bambuk",
 "Tekrur",
 "Mande",
 "Faleme",
 "Nema",
 "Sila",
 "Tagant"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
