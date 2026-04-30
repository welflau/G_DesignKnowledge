# Freeciv(nation) · sherpa

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/sherpa.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的sherpa定义

## 正文
```ruleset
[nation_sherpa]

name=_("Sherpa")
plural=_("?plural:Sherpas")
groups="Asian", "Early Modern"
legend=_("Sherpas are an ethnic group who settled in the Himalaya region\
 of modern-day Nepal in the 15th century. They are of Tibetan stock and\
 speak a language related to modern Tibetan though they are not mutually\
 intelligible. After a few centuries of autonomy, Sherpa communities\
 came by the 18th century under military pressure from encroaching\
 Hindu polities, such as the Bengal based Sen Empire. By the 18th century\
 the Sherpa homeland had been annexed into the Kingdom of Nepal. Following\
 the democratization of Nepal in the beginning of the 21st century,\
 there have been calls for greater autonomy for the Sherpas within the\
 federal republic.")

leaders = {
 "name",                   "sex"
 "Minyag Tonpa Druzang",   "Male"
 "Dujom Dorje",            "Male"
 "Chak Pon Sangye Paljor", "Male"
 "Gegyelpo",               "Male"
}

flag="sherpa"
flag_alt="-"
style = "Asian"

init_techs=""
init_buildings=""
init_units=""

conflicts_with="Nepali"
civilwar_nations="Tibetan", "Nepali"

cities =
; Sherpa villages; Nepali name as comment, if known
 "Zhung", ; Junbesi
 "Phukmoche",
 "Domphuk",
 "Dolange",
 "Takto",
 "Gising Gangdo", ; Sagar-Baganje
 "Sete",
 "Churungkharka",
 "Dudele",
 "Changnyima",
 "Golela",
 "Bhusinga",
 "Ngowur",
 "Kapte",
 "Lhungsa",
 "Solnasa", ; Gora
 "Lhawu Shintok", ; Ghat
 "Ledingma",
 "Thashing", ; Bamti
 "Takshindu",
 "Chulemo",
 "Yawa",
 "Deku",
 "Mopung",
 "Damsere", ; Phera
 "Khamje",
 "Shertong", ; Sertu
 "Changmela", ; Deurali
 "Nauje", ; Namche Bazar
 "Chukebuk", ; Sim
 "Gaichepe",
 "Lhomsa", ; Lumbu
 "Jhareni",
 "Chyangma", ; Bhandar
 "Dzomdingma" ; Gyangtar

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
