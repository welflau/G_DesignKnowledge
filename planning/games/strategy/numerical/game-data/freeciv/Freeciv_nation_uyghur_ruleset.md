# Freeciv(nation) · uyghur

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/uyghur.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的uyghur定义

## 正文
```ruleset
[nation_uyghur]

name=_("Uyghur")
plural=_("?plural:Uyghurs")
groups="Medieval", "Early Modern", "Asian"
legend=_("Uyghur was an east Turk empire and civilization. At its height in\
 820 CE it controlled most of Central and North Asia. After clashing with\
 the Chinese for several centuries, they were finally subdued by the Qing\
 dynasty in the 1700s. Today, descendants of the Uyghur form the\
 populations of the Central Asian states of Uzbekistan, Kazakhstan and\
 Kyrgyzstan. They are also the main minority of the Xinjiang province of\
 China.")

leaders = {
 "name",                "sex"
 "Kutluk Bilge Kul",    "Male"
 "Moyunchur",           "Male"
 "Khitan",              "Male"
 "Bugu",                "Male"
 "Baga Tarkan",         "Male"
 "Kutlug Bilge",        "Male"
 "Sutuk Bugra",         "Male"
 "Guyuk",               "Male"
}

ruler_titles = {
 "government",      "male_title",      "female_title"
 "Despotism",       _("%s Khan"),      _("%s Khatan")
 "Monarchy",        _("%s Khagan"),    _("?female:%s Khagan")
}

flag="uyghur"
flag_alt = "-"
style = "Classical"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations = "turkish", "tocharian"

cities =
 "Ürümqi",
 "Karamay",
 "Kuytun",
 "Karabalgasun",
 "Haml",
 "Kashi",
 "Hotan",
 "Korla",
 "Turpan",
 "Kuqa",
 "Aksu",
 "Balguntay",
 "Nilka",
 "Baxkorgan",
 "Boron Sum",
 "Ikanbujmal",
 "Shihanza",
 "Serikbuya",
 "Karakhoja",
 "Ulanlinggi",
 "Tumshuke",
 "Kashgar",
 "Markit",
 "Alar",
 "Narat",
 "Tikanlik",
 "Altay",
 "Tura",
 "Üjachu",
 "Yakatograk"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
