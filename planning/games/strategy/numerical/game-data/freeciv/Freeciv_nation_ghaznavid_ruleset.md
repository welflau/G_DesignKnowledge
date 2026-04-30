# Freeciv(nation) · ghaznavid

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/ghaznavid.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的ghaznavid定义

## 正文
```ruleset
[nation_ghaznavid]

name=_("Ghaznavid")
plural=_("?plural:Ghaznavids")
groups="Asian", "Medieval"
legend=_("The Ghaznavids were a Sunni Muslim dynasty of Turkish origin,\
 reigning from 977 to 1186 CE in Afghanistan and Northern India, and at\
 the peak of their power also in eastern Iran and Central Asia.")
leaders = {
 "name",                "sex"
 "Alp Tegin",           "Male"
 "Ebu Ishak Ibrahim",   "Male"
 "Bilge Tigin",         "Male"
 "Böri Tigin",          "Male"
 "Sebük Tigin",         "Male"
 "Mahmut",              "Male"          ;Mahmud Ghazni
 "Mevdud",              "Male"
 "Abdürreşit",          "Male"
 "Tuğrul Bozan",        "Male"
 "Ferruhzad",           "Male"
 "Şirzad",              "Male"
 "Hüsrevşah",           "Male"
}

flag="ghaznavid"
flag_alt = "-"
style = "Babylonian"

ruler_titles = {
 "government",     "male_title",        "female_title"
 "Despotism",      _("%s Bey"),         _("?female:%s Bey")
 "Monarchy",       _("Emir %s"),        _("Emira %s")
 "Fundamentalism", _("Grand Mufti %s"), _("?female:Grand Mufti %s")
}

init_techs=""
init_buildings=""
init_units=""

conflicts_with="persian", "iranian", "afghani", "pakistani", "tajik", "turkmen",
               "uzbek", "sikh", "timurid", "azeri", "kashmiri"
civilwar_nations = "seljuk", "timurid", "iranian", "afghani"

cities =
 "Gazne",               ;Ghazni
 "Lahor",              ;Lahore
 "Kabil",
 "Kandehar",
 "Herat",
 "Multan",
 "Agra",
 "Belh",
 "Merv",
 "Buhara",
 "Sen",
 "Yezd",
 "Kirman",
 "Rey",
 "Hamedan",
 "Nişabur",
 "İsfahan",
 "Semerkand",
 "Zarani",
 "Marage",
 "Tebriz",
 "Şiraz"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
