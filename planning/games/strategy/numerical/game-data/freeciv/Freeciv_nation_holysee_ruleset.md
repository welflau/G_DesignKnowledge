# Freeciv(nation) · holysee

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/holysee.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的holysee定义

## 正文
```ruleset
[nation_holysee]

name = _("Papal")
plural = _("?plural:Papal States")
groups="Medieval", "Early Modern", "Modern", "European"
legend=_("The Papal States were the territories on the Italian Peninsula\
 and elsewhere under the direct sovereign rule by the Roman Catholic popes.\
 Established in the 8th century CE from territory donated to the Church by\
 the pious and the wealthy, the Papal States grew to become the dominant\
 power in Italy for centuries.")

leaders = {
 "name",                "sex"
 "Petrus",              "Male"
 "Clemens I",           "Male"
 "Leo I",               "Male"
 "Gregorius I",         "Male"
 "Ioanna",              "Female"
 "Innocentius III",     "Male"
 "Adrianus VI",         "Male"
 "Pius IX",             "Male"
 "Ioannes Paulus II",   "Male"
 "Benedictus XVI",      "Male"
}

ruler_titles = {
 "government",     "male_title",         "female_title"
 "Anarchy",        _("Antipope %s"),     _("Antipopess %s")
 "Communism",      _("Brother %s"),      _("Sister %s")
 "Democracy",      _("Chancellor %s"),   _("?female:Chancellor %s")
 "Fundamentalism", _("Pope %s"),         _("Popess %s")
 "Monarchy",       _("Grand Master %s"), _("Grand Mistress %s")
 "Republic",       _("Consul %s"),       _("?female:Consul %s")
}

flag = "vatican"
flag_alt = "constantine"
style = "Classical"

init_techs=""
init_buildings=""
init_units=""

conflicts_with = "Roman"
civilwar_nations = "Roman", "Holy Roman", "Swiss"

cities =
 "Civitas Vaticana",	; Vatican City
 "Viterbium",		; Viterbo
 "Interamna",		; Terni
 "Tholentinum",		; Tolentino
 "Ancona",
 "Ravenna",
 "Nomentum",		; Mentana
 "Reate",		; Rieti
; "Castelfidardo",
 "Velitrae",		; Velletri
 "Tarracina",		; Terracina
 "Centumcellae",	; Civitavecchia
 "Spoletium",		; Spoleto
 "Macerata",
 "Urbinum",		; Urbino
 "Pisaurum",		; Pesaro
 "Ariminum",		; Rimini
 "Forum Livii",		; Forlì
 "Bononia",		; Bologna
 "Ferraria",		; Ferrara
 "Tuder",		; Todi
 "Sutrium",		; Sutri
 "Urbs Vetus",		; Orvieto
 "Beneventum",		; Benevento
; "Pontecorvo",
; "Venasque",
 "Carpentoracte",	; Carpentras
 "Avennio"		; Avignon

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
