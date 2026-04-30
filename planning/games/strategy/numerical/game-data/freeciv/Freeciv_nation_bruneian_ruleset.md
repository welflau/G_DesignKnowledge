# Freeciv(nation) · bruneian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/bruneian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的bruneian定义

## 正文
```ruleset
[nation_bruneian]

name=_("Bruneian")
plural=_("?plural:Bruneians")
groups="Medieval", "Early Modern", "Modern", "Asian"
legend=_("Brunei Darussalam is a country on Borneo in the Malay achipelago.\
 The sultanate dates from the 14th century and became a fairly powerful\
 state a century later thanks to its control of the maritime trade in much\
 of Southeast Asia. Brunei was a British protectorate from 1888 to 1984.")

leaders = {
 "name",              "sex"
 "Muhammad Shah",     "Male"
 "Bolkiah",           "Male"
 "Saiful Rijal",      "Male"
 "Hussin Kamaluddin", "Male"
 "A. M. Azahari",     "Male"
 "Hassanal Bolkiah",  "Male"
}

ruler_titles = {
 "government",      "male_title",       "female_title"
 "Fundamentalism", _("Grand Mufti %s"), _("?female:Grand Mufti %s")
 "Monarchy",       _("Sultan %s"),      _("Sultana %s")
}

flag="brunei"
flag_alt = "-"
style = "Asian"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations = "malaysian", "majapahit"

cities =
 "Bandar Seri Begawan",
 "Kuala Belait",
 "Pekan Tutong",
 "Pekan Bangar",
 "Kampong Ayer",
 "Seria",
 "Jerudong",
 "Muara",
 "Sukang",
 "Kampong Sawah",
 "Gadong",
 "Berakas",
 "Sungai Liang",
 "Pengkalan Batu",
 "Mentiri",
 "Keriam",
 "Kiudang",
 "Kampong Penapar",
 "Kampong Penkalan Dong",
 "Bangar",
 "Kampong Benkurong",
 "Kampong Beruang",
 "Kilanas",
 "Serasa",
 "Rancangan Perumahan Negara Lambak Kanan",
 "Kampong Sungai Duhon",
 "Kampong Mumong",
 "Kampong Sungai Teraban",
 "Labu",
 "Andulau",
 "Perdayan",
 "Ulu Temburong",
 "Luagan Lalak",
 "Kampong Rasau",
 "Kampong Sungai Mau",
 "Kampong Bukit Sawat",
 "Sungai Tujoh"
 

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
