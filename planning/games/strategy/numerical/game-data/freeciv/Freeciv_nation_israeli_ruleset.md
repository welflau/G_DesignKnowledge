# Freeciv(nation) · israeli

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/israeli.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的israeli定义

## 正文
```ruleset
[nation_israeli]

name=_("Israeli")
plural=_("?plural:Israelis")
groups="Modern", "Asian"
legend=_("The nation of Israel was founded in 1948 as a scattered collection\
 of cantons in British Palestine, and has gradually expanded through winning\
 wars in 1948, 1967 and 1973.")

leaders = {
 "name",                "sex"
 "Theodor Herzl",       "Male"
 "Ze'ev Jabotinsky",    "Male"
 "David Ben-Gurion",    "Male"
 "Golda Meir",          "Female"
 "Moshe Dayan",         "Male"
 "Menachem Begin",	"Male"
 "Yitzhak Rabin",	"Male"
 "Shimon Peres",	"Male"
}
ruler_titles = { "government",     "male_title",       "female_title"
                 "Communism",      _("Kibbutznik %s"), _("?female:Kibbutznikit %s")
                 "Despotism",      _("General %s"),    _("?female:General %s")
                 "Fundamentalism", _("Rabbi %s"),      _("?female:Rabbi %s")
	       }

flag="israel"
flag_alt = "menora"
style = "Babylonian"

init_techs=""
init_buildings=""

init_units=""
civilwar_nations = "palestinian"

cities =
;claimed capital
 "Yerushalayim",		;Jerusalem	

;internationally recognized capital
 "Tel Aviv-Yafo (ocean)",	;Tel Aviv-Jaffa

;other cities in Israel proper
 "Haifa (ocean)",
 "Be'er Sheva (desert)",	;Beersheba
 "Natzrat",			;Nazareth
 "Ramlah",
 "Ashdod (ocean)",
 "Ashqelon (ocean)",		;Ashkelon
 "Rishon LeZiyyon",
 "Petah Tiqwa",
 "Netanya",
 "Holon",
 "Bene Beraq",
 "Ramat Gan",
 "Bat Yam",
 "Rehovot",
 "Herzliyya",
 "Kefar Sava",
 "Hadera",
 "Bet Shemesh",
 "Ra'anana",
 "Modi'in-Makkabbim-Re'ut",
 "Lod",
 "Nahariyya",
 "Qiryat Atta",
 "Giv'atayim",
 "Hod HaSharon",
 "Elat",			;Eilat
 "Akko",			;Acre
 "Karmi'el",
 "Umm al-Fahm",
 "Rahat",
 "Natzrat Illit",
 "Tverya",			;Tiberias
 "Afula",
 "Qiryat Motzkin",
 "Rosh HaAyin",
 "Ramat HaSharon",
 "Qiryat Yam",
 "Qiryat Bialik",
 "Tayibe",
 "Shefar'am",
 "Nes Ziyyona",
 "El'ad",
 "Dimona",
 "Baqa-Jatt",
 "Or Yehuda",
 "Yavne",
 "Shaghur",
 "Qiryat Ono",
 "Zefat",
 "Tamra",
 "Netivot",
 "Yehud-Monosson",
 "Sakhnin",
 "Ofaqim",
 "Migdal HaEmeq",
 "Arad",
 "Qiryat Shemona",
 "Tira",
 "Nesher",
 "Ma'alot-Tarshiha",
 "Giv'at Shmuel",
 "Qiryat Mal'akhi",
 "Sederot",
 "Tirat Carmel",
 "Yokneam",
 "Kfar Kassem",
 "Qalansawe",
 "Bet She'an",
 "Or Aqiva",

;cities in Judea and Samaria (West Bank)
 "Modi'in Illit",
 "Beitar Illit",
 "Ma'ale Adumim",
 "Ari'el"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
