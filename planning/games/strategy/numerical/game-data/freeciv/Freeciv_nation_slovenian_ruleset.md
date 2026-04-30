# Freeciv(nation) · slovenian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/slovenian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的slovenian定义

## 正文
```ruleset
[nation_slovenian]

name=_("Slovenian")
plural=_("?plural:Slovenians")
groups="Medieval", "Modern", "European"
legend=_("Slovenia was the most western and northern republic of the old\
 Yugoslav Federation.")

leaders = {
 "name",                "sex"
 "Valuka",              "Male"
 "Valtunk",             "Male"
 "Kocelj",              "Male"
 "Primož Trubar",       "Male"
}
ruler_titles = {
 "government",      "male_title",      "female_title"
 "Despotism",       _("Ban %s"),       _("?female:Ban %s")
 "Fundamentalism",  _("Bishop %s"),    _("Mother Superior %s")
}
flag="slovenia"
flag_alt = "-"
style = "European"

init_techs=""
init_buildings=""
init_units=""

; Chain of similar flags: Previously "russian"
conflicts_with="slovakian"
civilwar_nations = "serbian"

cities =
  "Ljubljana", "Maribor", "Nova Gorica", "Celje", "Kranj", "Jesenice",
  "Idrija", "Novo Mesto", "Trbovlje", "Velenje", "Koper", "Murska Sobota",
  "Ptuj", "Pragersko", "Hrastnik", "Zagorje", "Kamnik", "Domzale",
  "Skofja Loka", "Radovljica", "Bled", "Postojna", "Izola", "Piran",
  "Kocevje", "Zidani Most", "Brezice", "Krsko", "Catez", "Ormoz",
  "Sentilj", "Dravograd", "Ravne", "Lasko", "Trzic", "Kranjska Gora",
  "Sezana", "Savudrija", "Pivka"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
