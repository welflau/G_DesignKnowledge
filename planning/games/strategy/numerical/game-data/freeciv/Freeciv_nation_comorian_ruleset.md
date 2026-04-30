# Freeciv(nation) · comorian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/comorian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的comorian定义

## 正文
```ruleset
[nation_comorian]

name=_("Comorian")
plural=_("?plural:Comorians")
groups="Modern", "African"
legend=_("The Comoros is an island country in the Mozambique channel,\
 consisting of Grande Comore, Moheli and Anjouan, although the Comoran\
 government also claims Mayotte, which is currently a French overseas\
 departement. Having been under Arab influence since the 8th century,\
 the Comoros is the southernmost Muslim-majority country in the world.")

leaders = {
 "name",            "sex"
 "Qumralu",         "Male"
 "Salima Machimba", "Female"
 "Ahmed Abdallah",  "Male"
 "Bob Denard",      "Male"
 "Ali Soilih",      "Male"
 "Azali Assoumani", "Male"
}

ruler_titles = {
 "government",     "male_title",        "female_title"
 "Communism",      _("Chairman %s"),    _("Chairwoman %s")
 "Fundamentalism", _("Grand Mufti %s"), _("?female:Grand Mufti %s")
 "Monarchy",       _("Sultan %s"),      _("Sultana %s")
}

flag="comoros"
flag_alt = "-"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations = "swahili", "arab" ; anjouan

cities =
 "Moroni",
 "Moutsamoudou",
 "Fomboni",
 "Iconi",
 "Domoni",
 "Nioumachoua",
 "Ounkazi",
 "Tsémbehou",
 "Djoièzi",
 "Mbéni",
 "Ongodjou",
 "Wanani",
 "Mitsamiouli",
 "Sima",
 "Ndrodoni",
 "Ouéllah",
 "Adda Daouéni",
 "Mtakoudja",
 "Mvouni",
 "Ouani",
 "Mboigoma",
 "Foumbouni",
 "Mirontsi",
 "Ziroudani",
 "Tsidjé",
 "Bazmini",
 "Barakani",
 "Nkourani ya Simi",
 "Koni Djodjo",
 "Mbatsé",
 "Mitsoundjé-Troumbeni",
 "Moyo",
 "Hoani",
 "Démbeni",
 "Dindri",
 "Bandar Salama",
 "Ntsoundjini",
 "Ngandzalé",
 "Kangani",
 "Mdé-Sahani",
 "Barakani",
 "Miringoni",
 "Ivémbeni-Bandasamoulini",
 "Mbambao Mtsanga",
 "Hamavouna"
 

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
