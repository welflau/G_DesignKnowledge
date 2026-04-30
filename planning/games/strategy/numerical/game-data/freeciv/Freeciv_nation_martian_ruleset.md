# Freeciv(nation) · martian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/martian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的martian定义

## 正文
```ruleset
[nation_martian]

name=_("Martian")
plural=_("?plural:Martians")
groups="Imaginary"
legend=_("Marsmen landed on Earth in 4000 BCE!")

leaders = {
 "name",                        "sex"
 "Ray Bradbury",                "Male"
 "Wernher von Braun",           "Male"
 "Arthur C. Clarke",            "Male"
 "Isaac Asimov",                "Male"
 "Gene Roddenberry",            "Male"
 "Ursula Le Guin",              "Female"
 "Andre Norton",                "Female"
 "Alice Bradley Sheldon",       "Female"
 "H. G. Wells",                 "Male"
}

flag="mars"
flag_alt = "-"
style = "Babylonian"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="atlantean"

cities =
	"Olympus Mons", "Utopia Planitia", "Hellas Planitia",
	"Elysium Planitia", "Arsia Mons", "Pavonis Mons", "Ascraeus Mons",
	"Tharsis Tholus", "Argyre Planitia", "Deuteronilus Mensae",
	"Elysium Mons", "Apponolaris Patera", "Sinus Sabaeus",
	"Valles Marineris", "Margaritifer Sinus", "Syria Planum",
	"Sinai Planum", "Solis Planum", "Lunae Planum", "Amazonis Planitia",
	"Arcada Planitia", "Alba Paterna", "Biblis Paterna",
	"Uranius Tholus", "Kassei Vailis"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
