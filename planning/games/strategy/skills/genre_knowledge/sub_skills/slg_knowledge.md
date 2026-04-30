# SubSkill: SLG品类知识

## 触发条件
用户需求涉及SLG品类设计、SLG玩法特征、SLG与其他品类融合

## 优先检索条目
1. `comprehensive/project-mgmt/GameDevMind_游戏研运资产样例-SLG手游（2D）.md`
2. `system/slg-modules/SLG实战_slgserver.md` — 完整SLG模块清单
3. `numerical/game-data/freeciv/Freeciv_civ2civ3_units_ruleset.md` — 4X单位设计
4. `numerical/game-data/freeciv/Freeciv_civ2civ3_buildings_ruleset.md` — 4X建筑设计
5. `numerical/game-data/openra/OpenRA_ra_structures.md` — RTS建筑设计

## SLG品类核心框架
```
SLG 核心循环:
  资源获取 → 基地建设 → 军队养成 → 战争征服 → 扩张领地 → 更多资源
  
SLG 核心系统:
  ├── 基地系统（建筑/升级/功能解锁）
  ├── 资源系统（产出/消耗/交易/掠夺）
  ├── 军事系统（兵种/将领/编队/行军）
  ├── 战斗系统（结算/战报/克制/地形）
  ├── 科技系统（研发树/加成/解锁）
  ├── 地图系统（大地图/区域/据点/雾）
  ├── 联盟系统（创建/加入/援助/联盟战）
  └── 赛季系统（重置/排行/奖励）
```
