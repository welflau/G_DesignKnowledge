# Freeciv(nation) · tajik

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/tajik.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的tajik定义

## 正文
```ruleset
[nation_tajik]

name=_("Tajik")
plural=_("?plural:Tajiks")
groups="Modern", "Asian"
legend=_("Tajikistan is a nation in Central Asia. The Tajiks trace the\
 foundation of their nation back to the Samanid Empire, one of the first\
 Persian states to appear after the Arab conquest.")

leaders = {
 "name",                "sex"
 "Bobojon Ghafurov",    "Male"
 "Abulqosim Lohuti",    "Male" ; Political activist and poet.
 "Nuh I",               "Male" ; Samanid ruler.
 "Nasri II",            "Male" ; Samanid ruler.
 "Ismoili Somoni",      "Male" ; Samanid ruler.
}

ruler_titles = {
 "government",      "male_title",            "female_title"
 "Monarchy",        _("Emir %s"),            _("Emira %s")
 "Communism",       _("First Secretary %s"), _("?female:First Secretary %s")
}

flag="tajikistan"
flag_alt = "-"
style = "Classical"

init_techs=""
init_buildings=""
init_units=""

conflicts_with="Hungarian" ;similar-looking flag
civilwar_nations="Iranian", "Pakistani", "Afghani"

cities =
 "Dushanbe",
 "Khujand",
 "Kulob",
 "Qurghonteppa",
 "Istaravshan",
 "Konibodom",
 "Vakhdat",
 "Isfara",
 "Panjakent",
 "Tursunzoda",
 "Khorugh",
 "Hisor",
 "Farkhor",
 "Chkalov",
 "Vose'",
 "Maskav",
 "Danghara",
 "Norak",
 "Somoniyon",
 "Ghafurov",
 "Kolkhozobod",
 "Zafarobod",
 "Nov",
 "Proletar",
 "Jirgatol",
 "Shahrtuz",
 "Asht",
 "Sarband",
 "Taboshar",
 "Qayroqqum",
 "Leningrad",
 "Ayni",
 "Vakhsh",
 "Dusti",
 "Buston",
 "Gharm",
 "Kuybyshev",
 "Roghun",
 "Faizobod",
 "Panj",
 "Ishkoshim",
 "Murghob",
 "Qal'ai Khumb",
 "Darband"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
