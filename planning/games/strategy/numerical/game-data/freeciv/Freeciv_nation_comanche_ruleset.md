# Freeciv(nation) · comanche

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/comanche.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的comanche定义

## 正文
```ruleset
[nation_comanche]

name=_("Comanche")
plural=_("?plural:Comanches")
groups="American"
legend=_("The Comanche or Numunu are a Native American ethnic group whose\
 historic range (the Comancheria) consisted of present-day eastern New\
 Mexico, southern Colorado, northeastern Arizona, southern Kansas, all of\
 Oklahoma, and most of northwest Texas.")

leaders = {
 "name",                "sex"
 "Tu-uh-ku-mah",        "Male" ; Black Horse
 "Isa-tai",             "Male" ; White Eagle
 "Po-bish-e-quasho",    "Male" ; Iron Jacket
 "Mo'pe-choko-pa",      "Male" ; Old Owl
 "Toshaway",            "Male" ; Silver Knife
 "Paruasemana",         "Male" ; Ten Bears
 "Peta Nocona",         "Male"
 "Quanah Parker",       "Male"
}

ruler_titles = {
 "government",      "male_title",      "female_title"
 "Monarchy",        _("Great Chief %s"),  _("?female:Great Chief %s")
 "Fundamentalism",  _("Shaman %s"),       _("?female:Shaman %s")
}

flag = "comanche"
flag_alt = "-"
style = "celtic"
init_techs=""
init_buildings=""
init_units=""

civilwar_nations = "hopi", "apache"

cities =
  "Húpenúú",
"Kúhtsútúúka",
"Kwaarú Núú",
"Mútsahne",
"Nokoni Núú",
"Tahnahwah",
"Tanimúú",
"Pagatsú",
"Pekwi Túhka",
"Penatúka Núú",
"Tayúúwit",
"Kúvahrahtpaht",
"Taykahpwai",
"Pikaatamú",
"Saria Túhka",
"Yaparúhka",
"Ketahtoh Tú",
"Motso Tú",
"Pibianigwai",
"Súhmúhtúhka",
"Titchahkaynah",
"Wahkoh",
"Waw'ai",
"Hai'ne'na'úne",
"It'chit'a'búd'ah",
"Itehtah'o",
"Naú'niem",
"Ohnonúú",
"Pahúraix",
"Pohoi",
"Tútsanoo Yehkú",
"Wianúú"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
