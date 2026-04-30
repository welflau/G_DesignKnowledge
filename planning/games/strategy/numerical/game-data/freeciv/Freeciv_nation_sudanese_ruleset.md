# Freeciv(nation) · sudanese

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/sudanese.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的sudanese定义

## 正文
```ruleset
[nation_sudanese]

name=_("Sudanese")
plural=_("?plural:Sudanese")
groups="Modern", "African"
legend=_("In 1820 Sudan came under Egyptian rule and later British rule.\
 Sudan became independent in 1956.")

leaders = {
 "name",                        "sex"
 "Muhammad ibn Abdalla",        "Male"
 "Gaafar Nimeiry",              "Male"
 "Ibrahim Abboud",              "Male"
 "Omar al-Bashir",              "Male"
}
ruler_titles = {
 "government",      "male_title",           "female_title"
 "Despotism",       _("%s Pasha"),          _("?female:%s Pasha")
 "Fundamentalism",  _("Mahdi %s"),          _("?female:Mahdi %s")
 "Monarchy",        _("Sultan %s"),         _("Sultana %s")
}
flag="sudan"
flag_alt = "-"
style = "Classical"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations="south sudanese", "darfuri"

cities =
 "Al-Khartum",
 "Umm Durman",
 "Al-Fashir",
 "Nyala",
 "Al-Qadarif",
 "Atbara",
 "Bur Sudan (ocean)",	; English: "Port Sudan"
 "Wadi Haifa",
 "Kassala",
 "Kusti",
 "Al-Ubayyid",
 "Al-Junaynah",
 "Wad Madani",
 "Rabak",
 "Sannar",
 "Kaduqli",
 "Ad-Damir",
 "Kurmuk",
 "Ad-Damazin",
 "Kutum",
 "Shandi",
 "Qaysan",
 "Gallabat",
 "Umm Ruwaba",
 "Abu Hamad",
 "Berber",
 "Merowe"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
