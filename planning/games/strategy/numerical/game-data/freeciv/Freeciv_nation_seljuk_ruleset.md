# Freeciv(nation) · seljuk

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/seljuk.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的seljuk定义

## 正文
```ruleset
[nation_seljuk] 

name=_("Seljuk") 
plural=_("?plural:Seljuks") 
groups="Medieval", "Asian" 
legend=_("The Seljuks were a Turkic horde whose name comes from their founder\
 Seljuk. After the victory over the Ghaznavids in 1040 CE they created their\
 own state. In 1055 CE the Seljuks took Baghdad, and their leader\
 Tughril Beg took the title sultan. The Seljuks are famous for the defeat\
 they inflicted upon the Byzantines at the battle of Manzikert in 1071.\
 After the collapse of the Great Seljuk Empire in the 12th century the\
 Seljuks continued to rule in the Sultanate of Rum, which would later form\
 the basis of the Ottoman Turks.")

leaders={
 "name",                	"sex"
 "Selçuk",			"male"
 "Tuğrul",			"male"
 "Alp Arslan",			"male"
 "Melikşah I",			"male"
 "Berkyaruk",			"male"
 "Muhammet Tapar",		"male"
 "Ahmed Sencer",		"male"
 "Kutalmışoğlu Süleyman Şah",	"male"
 "Kılıç Arslan I",		"male"
 "Kılıç Arslan II",		"male"
 "Gıyaseddin Keyhüsrev I",	"male"
 "Gevher Nesibe",		"female"
 "Gıyaseddin Keyhüsrev II",	"male"
 "Gıyaseddin Mesud II",		"male"
}

flag= "seljuk" 
flag_alt = "-" 
style = "Classical" 

ruler_titles = { "government",    "male_title", "female_title"
                "Despotism",      _("%s Bey"),     _("?female:%s Bey")
		"Monarchy",       _("Sultan %s"),  _("Sultana %s")
		"Fundamentalism", _("Caliph %s"),  _("Calipha %s") 
} 

init_techs="" 
init_buildings="" 
init_units="" 

conflicts_with="turkish", "ottoman", "azeri"
civilwar_nations="ottoman", "turkmen", "afghani", "persian", "azeri", "khwarezmian", "crusader"

cities =
"Nişabur",	;Nishapur
"İsfahan",
"Rey",
"Konya",
"İznik",
"Hamedan",	;Hamadan
"Musul",	;Mosul
"Antakya",	;Antioch
"Semerkand",	;Samarkand
"Kayseri",	;Caesarea
"Kâbil",	;Kabul
"Şanlıurfa",	;Edessa
"Halep",	;Aleppo
"Sivas",
"Bağdat",	;Baghdad
"Şam",		;Damsascus
"Kudüs",	;Jerusalem
"Erzurum",
"Malazgirt",	;Manzikert
"Merv",
"Hive",		;Khiva
"Diyâr-ı Bekr",	;Diyarbakir
"Erzincan",
"Aksaray",
"Kangal",
"Urganch",
"Durağan",
"Mezar-ı Şerif", ;Mazar-i-Sharif
"Hekimhan",
"Kandehar",	;Kandahar
"Buhara",	;Bukhara
"Kadınhanı",
"Taşkent",	;Tashkent
"Fergana",
"Basra",
"Ahan"


```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
