# Freeciv(nation) · kenyan

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/kenyan.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的kenyan定义

## 正文
```ruleset
[nation_kenyan]

name = _("Kenyan")
plural = _("?plural:Kenyans")
groups="Modern", "African"
legend=_("Kenya gained independence from Britain in December 1963.")

leaders = {
 "name",                "sex"
 "Shiundu",             "Male"
 "Mumia",               "Male"
 "Ezekiel Apindi",      "Male"
 "Jomo Kenyatta",       "Male"
}

flag = "kenya"
flag_alt = "-"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations="swahili", "maasai"

cities =
  "Nairobi", "Mombasa", "Malindi", "Kisumu", "Labu", "Kitale", "Nakuru",
  "Nyeri", "Lokichoki", "Lodwar", "Moyale", "Ramu", "Marsabi", "Wajir",
  "Eldoret", "Mado Gashi", "Butere", "Kakamega", "Nanyuki", "Isiolo",
  "Kericho", "Embu", "Garissa", "Narok", "Thika", "Garsen", "Voi",
  "Konza", "Machakos", "Magadi", "Kilgoris", "Tsavo", "Maungu",
  "Mwaga", "Kilifi", "Kwale", "Gazi", "Witu", "Lamu", "Wangi", "Hadera",
  "Liboi", "Maralal", "Kisii", "Busonga", "Nginyang", "Dukana",
  "Kakuma", "Lokitaung"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
