# Freeciv(nation) · greenlander

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/greenlander.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的greenlander定义

## 正文
```ruleset
[nation_greenlander]

name=_("Greenlander")
plural=_("?plural:Greenlanders")
groups="American"
legend=_("Legend says that the Great Shaman Qitdlarssuaq led the Inuit\
 people to Thule (Qaanaaq) on the west coast of Greenland in the 10th\
 century. Around the same time, Scandinavian settlers arrived at the fjords\
 on the southwestern tip of the island. Today, Greenland is a self-governing\
 country within the Kingdom of Denmark with mixed Inuit and Scaninavian\
 population.")

leaders = {
 "name",                "sex"
 "Kuupik Kleist",       "Male"
 "Lena Pedersen",       "Female"
 "Eske Brun",           "Male"
 "Hinrich Rink",        "Male"
 "Poul Egede",          "Male"
 "Eirikr Thorvaldsson", "Male" ; Eric the Red
 "Qitdlarssuaq",        "Male"
}

ruler_titles = {
 "government",      "male_title",           "female_title"
 "Fundamentalism",  _("Bishop %s"),         _("?female:Bishop %s")
 "Republic",        _("Governor %s"),       _("?female:Governor %s")
}

flag="greenland"
flag_alt = "-"
style = "European"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations="Inuit", "Danish"

cities =
 "Nuuk",		; Godthåb (Danish/Norwegian)
 "Sisimiut",
 "Ilulissat",		; Jakobshavn (Danish/Norwegian)
 "Qaqortorq",
 "Asiaat",
 "Maniitsoq",
 "Tasiilaq",
 "Paamiut",		; Frederikshåb (Danish/Norwegian)
 "Narsaq",
 "Nanortalik",
 "Uummannaq",
 "Qasigiannguit",
 "Upernavik",
 "Qeqertarsuaq",	; Godhavn (Danish/Norwegian)
 "Qaanaaq",		; Thule (Danish/Norwegian)
 "Kangaatsiaq",
 "Kangerlussuaq",	; Søndre Strømfjord (Danish/Norwegian)
 "Ittoqqortoormiit",	; Scoresbysund (Danish/Norwegian)
 "Kullorsuaq",
 "Kuummiit",
 "Kangaamiut",
 "Alluitsup Paa",
 "Niaqornaarsuk",
 "Kulusuk",
 "Tasiusaq",
 "Ikerasak",
 "Qeqertarsuatsiaat",
 "Attu",
 "Sermiligaaq",
 "Saattut",
 "Nuussuaq",
 "Upernavik Kujalleq"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
