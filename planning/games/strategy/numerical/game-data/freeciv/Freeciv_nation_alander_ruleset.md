# Freeciv(nation) · alander

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/alander.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的alander定义

## 正文
```ruleset
[nation_alander]

name=_("Ålander")
; pre-2.6 had plain ASCII names
rule_name="Alander"
plural=_("?plural:Ålanders")
groups="European"
legend=_("Åland is an archipelago in the Baltic Sea, located between\
 Sweden and Finland. The islands' inhabitants are Swedish speaking, but\
 Åland is an autonomous province in Finland, a status that was reached\
 in 1921 after a long period in which the islands were contested between\
 Sweden and Finland. Åland's special and demilitarized status is protected\
 by international law.")

leaders = {
 "name",                     "sex"
 "Nils Psilander",           "Male"
 "Eric Arén",                "Male"
 "Frans Peter von Knorring", "Male"
 "Gustaf Erikson",           "Male"
 "Julius Sundblom",          "Male"
 "Carl Björkman",            "Male"
 "Fanny Sundström",          "Female"
}
ruler_titles = {
 "government",     "male_title",     "female_title"
 "Democracy",      _("Premier %s"),  _("Premiere %s")
 "Despotism",      _("Earl %s"),     _("?female:Earl %s")
 "Fundamentalism", _("Vicar %s"),    _("?female:Vicar %s")
 "Republic",       _("Governor %s"), _("?female:Governor %s")
}
flag="aland"
flag_alt = ""
style = "celtic"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations = "swedish", "finnish"

cities =
 "Mariehamn",
 "Kyrkby",	;Jomala
 "Godby",	;Finström
 "Söderby",     ;Lemland
 "Ödkarby",     ;Saltvik
 "Kattby",	;Hammarland
 "Björby",	;Sund
 "Storby",	;Eckerö
 "Degerby", 	;Föglö
 "Åva",		;Brändö
 "Vestergeta",	;Geta
 "Strömsby",	;Vårdö
 "Klemetsby",	;Lumparland
 "Kumlinge",
 "Kökar",
 "Sottunga",
 "Kastelholm",
 "Långnäs",
 "Lappo",
 "Märket",
 "Germundö",
 "Hastersboda",
 "Kasberget",
 "Hellsö",
 "Husö",
 "Norrsunda",
 "Önningeby",
 "Vestansunda",
 "Överö",
 "Tängsödavik",
 "Snäckö",
 "Fiskö",
 "Apalängen",
 "Möckelgräs",
 "Vessingsboda",
 "Krogstad",
 "Bamböle",
 "Vargata",
 "Höckböle",
 "Ytterby",
 "Prästgården",
 "Västra Ytternäs",
 "Granboda",
 "Åsgårda",
 "Överboda",
 "Ytternäs",
 "Björkö",
 "Pålsböle",
 "Emkarby",
 "Kråkböle",
 "Jomalby",
 "Sibby",
 "Torp",
 "Bråttö",
 "Övernäs",
 "Bovik",
 "Enklinge",
 "Hellestorp",
 "Ingby",
 "Västanträsk",
 "Ämnäs",
 "Östernäs",
 "Överby Degersand",
 "Bistorp",
 "Grelsby",
 "Äppelö",
 "Björnhuvud",
 "Nääs",
 "Espholm",
 "Ängö",
 "Finnö",
 "Postad",
 "Flisö",
 "Bistorp",
 "Skag",
 "Strömsvik"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
