# Freeciv(nation) · gambian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/gambian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的gambian定义

## 正文
```ruleset
[nation_gambian]

name=_("Gambian")
plural=_("?plural:Gambians")
groups="African", "Modern"
legend=_("The Gambia is a small country in West Africa, straddling both\
 banks of the Gambia river. It achieved independence from the United\
 Kingdom in 1965.")

leaders = {
 "name",                  "sex"
 "Dawda Jawara",          "Male"
 "Yahya Jammeh",          "Male"
}

ruler_titles = {
 "government",      "male_title",            "female_title"
 "Fundamentalism",  _("Grand Mufti %s"), _("?female:Grand Mufti %s")
 "Monarchy",        _("Mansa %s"),       _("?female:Mansa %s")
}

flag="gambia"
flag_alt = "-"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="senegalese", "ghanaian"

cities =
 "Banjul",
 "Brikama",
 "Basse Kanta Su",
 "Kerewan",
 "Janjanbureh",
 "Sera Kunda",
 "Mansa Konko",
 "Bakau",
 "Lamin",
 "Nema Kunku",
 "Farafenni",
 "Brufut",
 "Gunjur",
 "Sukuta",
 "Wellingara",
 "Busumbala",
 "Yundum",
 "Mandinari",
 "Soma",
 "Gambisara",
 "Banjulunding",
 "Sabi",
 "Bansang",
 "Kunkujang",
 "Abuko",
 "Garawoll",
 "Kerr Seringe Ngaga",
 "Siffoe",
 "Essau",
 "Tanju",
 "Farato",
 "Sanyang",
 "Jambajeli",
 "Barra",
 "Allunhari",
 "Kartong",
 "Tujereng",
 "Demba Kunda",
 "Bijilo",
 "Sibanor",
 "Madiana",
 "Kularr",
 "Kafuta",
 "Brikama Ba"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
