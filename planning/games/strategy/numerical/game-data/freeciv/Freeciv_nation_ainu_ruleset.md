# Freeciv(nation) · ainu

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/ainu.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的ainu定义

## 正文
```ruleset
[nation_ainu]

name=_("Ainu")
plural=_("?plural:Ainu")
groups="Asian"

legend=_("The Ainu are the indigenous people of northern Japan, the\
 Kuril islands, Sakhalin, and the southern part of the Kamchatka peninsula.")

leaders = {
 "name",                "sex"
 "Kayano Shigeru",      "Male"
 "Kosamaynu",           "Male"
 "Samkusaynu",          "Male"
 "Tsukinoe",            "Male"
}

flag="ainu"
flag_alt = "-"
style = "Asian"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="japanese", "russian"

; Sources for city names:
; Hokkaido: http://kam-r.sub.jp/ainu/index.html
; Aomori: http://www.asahi-net.or.jp/~hi5k-stu/aynu/sanpotimei2.htm
; Kuril: http://www.fortunecity.com/olympia/ince/698/rurik/kuril.html
; Sakhalin: http://www.city.wakkanai.hokkaido.jp/main/sakhalin.info/city.other.htm
;
; Orthography based on: http://city.hokkai.or.jp/~ayaedu/ainugo/text09.html
cities =
; Hokkaido - Japanese name in parentheses
 "Cipasiri", ; (Abashiri)
 "Mopet", ; (Monbetsu)
 "Tomakomanay", ; (Tomakomanai)
 "Nupurpet (river)", ; (Noboribetsu)
 "Moruerani", ; (Muroran)
 "Satporopet (river)", ; (Sapporo)
 "Esikaripet (river)", ; (Ishikari)
 "Iput", ; (Ebetsu)
 "Eeniwa", ; (Eniwa)
 "Cupupet (river)", ; (Asahikawa)
 "Sipet (river)", ; (Shibetsu)
 "Nayoroputo", ; (Nayoro)
 "Furanuy", ; (Furano)
 "Kusiru", ; (Kushiro)
 "Nimuoro", ; (Nemuro)
 "Rurumotpe", ; (Rumoi)
 "Pipay", ; (Bibai)
 "Yuuparo", ; (Yubari)
 "Sorapuci", ; (Takikawa)
 "Oohonay", ; (Fukagawa)
 "Hasupet (river)", ; (Ashibetsu)
 "Akapira", ; (Akabira)
 "Otausinay", ; (Sunagawa & Utashinai)
 "Yamwatkanay", ; (Wakkanai)
 "Operuperukepu", ; (Obihiro)
; Sakhalin - Russian name in parentheses
 "Poronay (river)", ; (Polonaisk)
 "Rutaka", ; (Aniva)
; Aomori - Japanese name in parentheses
 "Towatara", ; (Towada)
 "Aomori", ; (Aomori)
 "Piranay", ; (Hiranai)
 "Wankii", ; (Wakinosawa)
; Kuril Islands - Russian name in parentheses
 "Ituruupu", ; (Iturup)
 "Paramusir (ocean)", ; (Paramushir)
 "Onnekotan", ; (Onekotan)
 "Usisir (ocean)", ; (Ushishir)
 "Ciripoy", ; (Chiripoy)
 "Urup", ; (Urup)
 "Kunasir (ocean)", ; (Kunashir)
 "Sikotan" ; (Shikotan)

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
