# Freeciv(nation) · pashtun

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/pashtun.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的pashtun定义

## 正文
```ruleset
[nation_pashtun]

name=_("Pashtun")
plural=_("?plural:Pashtuns")
groups="Early Modern", "Asian"
legend=_("The Pashtuns are an ethnic group that lives mainly in Afghanistan\
 and Pakistan. They speak Pashto, a language closely related to Persian, and\
 live by an age-old code of honor known as Pashtunwali.")

leaders = {
 "name",               "sex"
 "Malalai Anaa",       "Male"
 "Akbar Khan",         "Male"
 "Dost Mohammad Khan", "Male"
 "Ahmad Shah Baba",    "Male"
 "Mirwais Hotak",      "Male"
 "Ibrahim Lodi",       "Male"
 "Sher Shah Suri",     "Male"
}

ruler_titles = {
 "government",      "male_title",      "female_title"
 "Monarchy",        _("Emir %s"),      _("Emira %s")
 "Fundamentalism",  _("Mullah %s"),    _("?female:Mullah %s")
}

flag="pashtun"
flag_alt=""
style = "Classical"

init_techs=""
init_buildings=""
init_units=""

conflicts_with="Afghani"
civilwar_nations="Afghani", "Pakistani", "Iranian"

cities =
 "Kandahar",
 "Kuwatah", ; Quetta
 "Peshawar",
 "Jalalabad",
 "Saidu Sharif",
 "Kabul",
 "Ghazni",
 "Kunduz",
 "Chaman",
 "Khost",
 "Zaranj",
 "Farah",
 "Shindand",
 "Zhob",
 "Dera Ismail Khan",
 "Wana",
 "Banu", ; Bannu
 "Parachinar",
 "Kohat",
 "Mardan",
 "Dir",
 "Kalat", ; Qalat
 "Sibi",
 "Chagai",
 "Gereshk",
 "Delaram",
 "Nushki",
 "Nok Kundi",
 "Dalbandin",
 "Surab",
 "Panjgur",
 "Qila Ladgasht",
 "Malar",
 "Hoshab",
 "Turbat",
 "Pasni",
 "Gwadar",
 "Jiwani",
 "Bela",
 "Moqor",
 "Zarghun Shahr",
 "Tank",
 "Thal",
 "Dargai",
 "Arandu",
 "Kalam",
 "Chitral",
 "Mastuj",
 "Lasht Khot",
 "Derakht-e Yahya",
 "Nag",
 "Sheykhabad"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
