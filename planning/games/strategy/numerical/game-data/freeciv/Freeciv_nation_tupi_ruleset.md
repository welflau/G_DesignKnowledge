# Freeciv(nation) · tupi

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/tupi.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的tupi定义

## 正文
```ruleset
[nation_tupi]

translation_domain="freeciv"

name=_("Tupi")
plural=_("?plural:Tupi")
groups="American", "Core"

legend=_("The Tupi are a native Brazilian people related to the Guarani who\
 inhabited the modern Brazilian states of Paraiba, Pernambuco, Ceara, Rio\
 Grande do Norte, Alagoas, Sergipe and others as well. Their chiefdoms were\
 destroyed through Portuguese slave-raids, the creation of mission-villages,\
 and disease. The Tupi intermarried with African slaves and Europeans alike\
 and a great many Brazilian place names are derived from Tupi words. ")

leaders = {
 "name",        "sex"
 "Tibiriça",    "Male"
 "Pindubuçu",   "Male"
 "Jugasu",      "Male"
 "Konyan Bebe", "Male"
}
ruler_titles = {
 "government",      "male_title",           "female_title"
 "Democracy",      _("Principal Chief %s"), _("?female:Principal Chief %s")
 "Fundamentalism", _("Shaman %s"),          _("?female:Shaman %s")
 "Monarchy",       _("Great Chief %s"),     _("?female:Great Chief %s")
}
flag         = "tupi"
flag_alt     = "-"
style        = "Tropical"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations = "taino", "tairona", "guarani"

cities =
 "Alagoa",
 "Syara",
 "Paráyba",
 "Paranã",
 "Piauy",
 "Siri Jibe",
 "Tukantin",
 "Itapeva",
 "Ka'aokai",
 "Capuan",
 "Icaraí",
 "Jandaiguaba",
 "Paumirim",
 "Pabussu",
 "Tabapuá",
 "Igaporã",
 "Uubatyba",
 "Iperoig",
 "Itauna",
 "Potengi",
 "Sergipe",
 "Yûasú",
 "Ypanema",
 "Itáañãgá",
 "Itákûakesétyba",
 "Îagûaraíuna",
 "Pakaembu",
 "Paranãyba",
 "Paranãmirĩ",
 "Pindó",
 "Piráí",
 "Ũbuarama",
 "Tupinambarana",
 "Uwattibi",
 "Arari"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
