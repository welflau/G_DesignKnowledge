# Freeciv(nation) · ryukyuan

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/ryukyuan.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的ryukyuan定义

## 正文
```ruleset
[nation_ryukyuan]

name=_("Ryukyuan")
plural=_("?plural:Ryukyuans")
groups="Medieval", "Early Modern", "Asian"
legend=_("The Ryukyu Kingdom (1372-1879) was the Land of Propriety, a\
 peaceful maritime trading nation eventually invaded, occupied, and annexed\
 by Japan.")

leaders = {
 "name",        "sex"
 "Sho Shisho",  "Male"
 "Sho Hashi",   "Male"
 "Sho En",      "Male"
 "Sho Nei",     "Male"
 "Sho Ho",      "Male"
 "Yosoidon",	"Female"
}

flag="ryukyu"
flag_alt="-"
style = "Asian"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations="japanese", "taiwanese"

cities=
; Okinawan name used, Japanese in comment
 "Sui",			; Shuri
 "Naafa",		; Naha
 "Uchinaa",		; Okinawa
 "Uruma",
 "Urashii",		; Urasoe
 "Jinoon",		; Ginowan
 "Nagu",		; Nago
 "Ichuman",		; Itoman
 "Tumigushiku",		; Tomigusuku
 "Naaku",		; Miyako
 "Ishigachi",		; Ishigaki
 "Nanjoo",		; Nanjo
 "Yuntan",		; Yomitan
 "Nishibaru",		; Nishihara
 "Feebaru",		; Haebaru
 "Chatan",
 "Nakagushiku",		; Nakagusuku
 "Yunabaru",		; Yonabaru
 "Mutubu",		; Motobu
 "Kadina",		; Kadena
 "Chi'n",		; Kin
 "Nachijin",		; Nakijin
 "Unna",		; Onna
 "Kumijima (ocean)",	; Kumejima
 "Iijima (ocean)",	; Ie
 "Jinuza",		; Ginoza
 "Dakidun",		; Taketomi
 "Ujimi",		; Ogimi
 "Agarijima (ocean)",	; Higashi
 "Ijina",		; Izena
 "Yunaguni",		; Yonaguni
 "Ihyaa",		; Iheya
 "Tarama",
 "Aguni",
 "Zamami",
 "Tukashichi",		; Tokashiki
 "Ufuagarijima (ocean)",; Kitadaito
 "Tunachi"		; Tonaki

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
