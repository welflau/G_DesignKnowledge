# Freeciv(nation) · cornish

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/cornish.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的cornish定义

## 正文
```ruleset
[nation_cornish]

name = _("Cornish")
plural = _("?plural:Cornish")
groups= "Medieval", "European"
legend=_("Cornwall is a region in the extreme southwest of England,\
 traditionally the home of the legendary King Arthur.")

leaders = {
 "name",                "sex"
 "Selina Cooper",       "Female"
 "Tommas Flamank",      "Male" ; Thomas Flamank
 "Humphrey Arundell",   "Male"
 "Myhal an Gof",        "Male" ; Michael Joseph
 "Arthur Gernow",       "Male" ; King Arthur
}

ruler_titles = {
 "government",      "male_title",      "female_title"
 "Despotism",       _("Chieftain %s"), _("?female:Chieftain %s")
 "Monarchy",        _("High King %s"), _("High Queen %s")
}

flag = "cornwall"
flag_alt = "england"
style = "Celtic"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="Welsh", "Breton"

cities =
 "Truru",		; Truro
 "Austol",		; St Austell
 "Aberfal",		; Falmouth
 "Pensans",		; Penzance
 "Lulynn",		; Newlyn
 "Cambron",		; Camborne
 "Tewyn Plustry",	; Newquay
 "Essa",		; Saltash
 "Bosvenegh",		; Bodmin
 "Resrudh",		; Redruth
 "Porth Ia",		; St Ives
 "Hellys",		; Helston
 "Bud",			; Bude
 "Liskeard",		; Lys Kerwyd
 "Penntorr",		; Torpoint
 "Heyl",		; Hayle
 "Lannstefan",		; Launceston
 "Lanndreth",		; St Blazey
 "Ponsrys",		; Wadebridge
 "Penrynn",		; Penryn
 "Logh",		; Looe
 "Kelliwik",		; Callington
 "Lannyust",		; St Just in Penwith
 "Plew Golom",		; St Columb Major
 "Lannwedhenek",	; Padstow
 "Sen Mewen",		; St Mewan
 "Tredhinas",		; St Dennis
 "Lostwydhyel",		; Lostwithiel
 "Ryskammel",		; Camelford
 "Fowydh",		; Fowey
 "Lannvorek",		; Mevagissey
 "Lannaghevran",	; St Keverne
 "Marghasyow",		; Marazion
 "Porth",		; Par
 "Morvedh",		; Morvah
 "Karnrosveur",		; Bugle
 "Trewoen",		; Trewoon
 "Egloslasek",		; Ladock
 "Komm",		; Coombe
 "Lannvowsedh",		; St Mawes
 "Porthynys",		; Mousehole
 "Pennwydh",		; Reawla
 "Porthmeur",		; Charlestown
 "Sen Kubi"		; Cuby

; City names for which no Cornish equivalent could be found

; "Grampound",
; "Tregony",
; "Polmassick",
; "Bissom",
; "Swanpool",
; "Halvosso",
; "Madron",
; "Crowlas",
; "Hellesveor",
; "Trink",
; "Lelant",
; "Gwithian"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
