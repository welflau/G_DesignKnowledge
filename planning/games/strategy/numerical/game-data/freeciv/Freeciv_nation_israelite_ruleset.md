# Freeciv(nation) · israelite

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/israelite.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的israelite定义

## 正文
```ruleset
[nation_israelite]

name=_("Israelite")
plural=_("?plural:Israelites")
groups="Ancient", "Asian"
legend=_("Israel was a Jewish kingdom on the eastern shore of the\
 Mediterranean founded around 1000 BCE. Much of its history is told in the\
 holy books of the Abrahamic religions. The last Jewish kingdom was\
 destroyed by the Romans in the 1st century CE, leaving the Jews\
 scattered around the world for nineteen centuries.")

leaders = {
 "name",                "sex"
 "Avraham",		"Male"
 "Sara",		"Female"
 "Ya'aqov",		"Male"
 "Moshe",		"Male"
 "Yehoshua",		"Male"
 "Sha'ul",		"Male"
 "David",		"Male"
 "Shelomo",		"Male"
 "Zidqiyyahu",		"Male"
 "Ester",		"Female"
 "Shim'on HamMakabi",	"Male"
 "Hordos",		"Male"
 "Shim'on Bar Giora",	"Male"
}

ruler_titles = {
 "government",      "male_title",        "female_title"
 "Anarchy",         _("Usurper %s"),     _("?female:Usurper %s")
 "Democracy",       _("Judge %s"),       _("?female:Judge %s")
}

flag="israel_ancient"
flag_alt = "israel"
style = "Babylonian"

init_techs=""
init_buildings=""

init_units=""

conflicts_with = "israeli", "palestinian"
civilwar_nations = "aramean", "egyptian", "phoenician"

cities =
 "Yerushalayim", 	;Jerusalem
 "Yeriho",		;Jericho
 "Hevron",		;Hebron
 "Shomron",		;Samaria
 "Be'er Sheva",		;Beersheba
 "Teverya",		;Tiberias
 "Bet El",		;Bethel
 "Shekem",		;Shechem
 "Bet Lehem",		;Bethlehem
 "Akko",		;Acre
 "Yafo",		;Jaffa
 "Bet Horon",		;Bethoron
 "Bet Shemesh",		;Beith Shemesh
 "Bet She'an",		;/* Beith She'an */
 "Keisarya",		;Caesarea
 "Haifa",		;Haifa
 "Ashdod",		;Ashdod
 "Lod",			;Lydda
 "Elat",		;Eilat
 "Ashqelon",		;Askhelon
 "Dan",			;Dan
 "Natzrat",		;Nazareth
 "Abel Bet Maacha",	;Abel-beth-maachah
 "Dimona",		;Dimona
 "Holon",		;Holon
 "Tirza",		;Tirzah
 "'Azza",		;Gaza
 "Sidon",		;Sidon
 "Tzor",		;Tyre
 "Arad",		;Arad
 "Edrei",		;Edrei
 "Ramot Gil'ad",	;Ramoth-Gilead
 "Magdal",		;Magdala
 "Kfar Nahum",		;Capernaum
 "Jisre'el",		;Jezreel
 "Mahanayim",		;Mahanaim
 "Dor",			;Dor
 "Gezer",		;Gezer
 "Yarmuth",		;Jarmut
 "Gat Rimmon",		;Gat-Rimon
 "Kedesh",		;Kedesh
 "Yavesh Gil'ad",	;Jabesh-Gilead
 "Gilgal",		;Gilgal
 "Hazor",		;Hazor
 "Shilo",		;Shiloh
 "Debar",		;Debir
 "Ekron",		;Ekron
 "Jazer",		;Jazer
 "Ai",			;Ai
 "Megiddo"		;Armageddon

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
