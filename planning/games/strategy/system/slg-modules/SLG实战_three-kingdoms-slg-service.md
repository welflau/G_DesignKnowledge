# SLG实战项目 · 三国SLG微服务(Go+gRPC)

> 来源：three-kingdoms-slg-service
> 原始链接：https://github.com/fitz2019/three-kingdoms-slg-service
> 分类：system
> 标签：SLG, 开源项目, 系统实现

## 概述
完整SLG项目实现：三国SLG微服务(Go+gRPC)

## 正文
# SLGGame-Three-Kingdoms-Strategy
# slg三国策略游戏服务器Demo

## 客户端demo：[https://github.com/fitz2019/three-kingdoms-slg--client-](https://github.com/fitz2019/three-kingdoms-slg--client-)

## 概要
- mysql数据落地，orm映射
- 事件处理支持中间件
- 服务器与服务器之间websocket连接
- 服务器与服务器之间rpc调用
- 高并发

### 多进程服务
- httpserver  提供一些api调用
- gateserver  网关，可以部署多个进行负载均衡，客户端的所有loginserver、chatserver、slgserver的消息都通过该服进行转发
- loginserver 登录服，可以部署多个进行负载均衡
- chatserver  聊天服，可以部署多个，原则上一个slgserver对应一个chatserver
- slgserver   游戏服，可以部署多个，不同服之间的玩家数据不共通

### 服务端使用简要介绍
- cd slgserver
- 项目已经使用go mod管理，推荐使用goland打开
- 创建MySQL数据库：在MySQL中执行 data/conf/db.sql 文件创建服务所需的数据库，库名默认为slgdb
- 修改配置： 修改 data/conf/env.ini 中数据库的配置，主要是密码、端口修改成自己所使用的一致即可，其他保持默认即可
- 拉取依赖包：命令行执行 go mod tidy
- 生成可执行程序： main 目录下包含了 httpserver、gateserver、loginserver、chatserver、slgserver 5个进程的代码，
  通过 go build main/xxxserver.go(上方5个进程源代码)即可生成 5个进程执行文件，在windows环境下也可以在直接执行 shell/build.bat
  生成5个进程可执行文件，可执行文件会存放在bin目录下
- 复制配置文件到工作目录：将data文件夹拷贝到bin目录下，5个进程会用到data里的配置， window环境可以运行shell/copydata.bat完成拷贝操作
- 启动运行：启动5个进程，无顺序要求，windows环境下可以运行shell/run.bat代劳
- 客户端联调：cocos creator 3.4.0版本 打开客户端运行即可联机测试
- 注意在goland中点击对应的进程 run 或者 debug 前需要将输出路径和工作路径都设置成bin目录，
  并且data目录已经拷贝到bin目录下，否则进程找不到运行的配置文件会异常终止

### 服务部署

**支持docker-compose 一键部署，数据库和表都会创建好的，步骤如下：**

1. **部署需要编译go源码，编译比较占内存，内存2G以下有可能编译不成功，请保证编译内存在2G以上**

2. **cd slgserver**

3. **docker-compose up**

4. **客户端可修改 GameConfig.ts 文件中的连接地址，也可使用下方默认**

   ```typescript
   import { _decorator } from 'cc';
   const GameConfig = {
       serverUrl: "ws://127.0.0.1:8004", //httpserver 地址
       webUrl: "http://127.0.0.1:8088",  //gateserver 地址
   }
   export { GameConfig };
   
   ```



## 客户端截图

### 队伍征兵
![队伍征兵](https://s1.imagehub.cc/images/2023/05/08/01.png)

### 占领领地
![占领领地](https://s1.imagehub.cc/images/2023/05/08/02.png)

### 出征返回
![出征返回](https://s1.imagehub.cc/images/2023/05/08/03.png)

### 城内设施
![城内设施](https://s1.imagehub.cc/images/2023/05/08/10.png)

### 武将
![武将](https://s1.imagehub.cc/images/2023/05/08/11a2c81d5956c6dee0.png)

### 武将详情
![武将详情](https://s1.imagehub.cc/images/2023/05/08/12.png)

### 友方主城
![友方主城](https://s1.imagehub.cc/images/2023/05/08/04.png)

### 敌方主城
![敌方主城](https://s1.imagehub.cc/images/2023/05/08/05.png)

### 军队前往敌方主城
![军队前往敌方主城](https://s1.imagehub.cc/images/2023/05/08/06.png)

### 抽卡结果
![抽卡结果](https://s1.imagehub.cc/images/2023/05/08/07.png)

### 战报
![战报](https://s1.imagehub.cc/images/2023/05/08/13.png)

### 技能
![技能](https://s1.imagehub.cc/images/2023/05/08/08.png)

### 联盟
![联盟](https://s1.imagehub.cc/images/2023/05/08/09.png)

### 聊天
![聊天](https://s1.imagehub.cc/images/2023/05/08/14.png)



## 项目文件结构

```
three-kingdoms-slg-service/
  .gitignore
  Dockerfile-chat
  Dockerfile-gate
  Dockerfile-http
  Dockerfile-login
  Dockerfile-mysql
  Dockerfile-slg
  LICENSE
  README.md
  docker-compose.yaml
  go.mod
  go.sum
  middleware/
    check_login.go
    check_rid.go
    check_role.go
    elapsed_time.go
    log.go
  net/
    clientconn.go
    conn.go
    connMgr.go
    proxyClient.go
    router.go
    server.go
    serverconn.go
  util/
    crypto.go
    math.go
    msgpack.go
    random.go
    session.go
  config/
    config.go
    reload_unix.go
    reload_windows.go
  shell/
    build.bat
    copydata.bat
    kill.bat
    run.bat
  server/
    loginserver/
      init.go
      proto/
        account.go
      controller/
        account.go
      model/
        login.go
        user.go
    chatserver/
      init.go
      proto/
        chat.go
      logic/
        entity.go
        group.go
        queue.go
      controller/
        chat.go
    httpserver/
      myerror.go
      middleware/
        cors.go
      logic/
        account.go
      controller/
        account.go
    gateserver/
      init.go
      controller/
        handle.go
    slgserver/
      ILogic/
        IArmyLogic.go
      proto/
        city.go
        coalition.go
        general.go
        interior.go
        nation_map.go
        role.go
        skill.go
        war.go
      static_conf/
        basic.go
        const.go
        map_build.go
        map_build_custom.go
        skill/
          skill.go
          skill_conf.go
          skill_outline.go
        general/
          general.go
          general_arms.go
          general_basic.go
        facility/
          facility.go
          facility_addition.go
          facility_conf.go
        npc/
          npc_army.go
      logic/
        init.go
        army/
          army_logic.go
          sys_army_logic.go
          view.go
        mgr/
          army_mgr.go
          city_facility_mgr.go
          coalition_mgr.go
          general_mgr.go
          national_map_mgr.go
          role_attribute_mgr.go
          role_build_mgr.go
          role_city_mgr.go
          role_mgr.go
          role_res_mgr.go
          skill_mgr.go
        war/
          armyPosition.go
          army_war.go
          warCamp.go
          warResult.go
        union/
          union_logic.go
        check/
          check_build.go
      controller/
        army.go
        city.go
        coalition.go
        general.go
        interior.go
        nation_map.go
        role.go
        skill.go
        war.go
      pos/
        position.go
      model/
        army.go
        city_facility.go
        coalition.go
        general.go
        map_role_build.go
        map_role_city.go
        national_map.go
        role.go
        role_attribute.go
        role_res.go
        skill.go
        util.go
        war_report.go
      run/
        init.go
      global/
        global.go
      conn/
        push_sync.go
  img/
    01.png
    02.png
    03.png
    04.png
    05.png
    06.png
    07.png
    08.png
    09.png
    10.png
    11.png
    12.png
    13.png
    14.png
  constant/
    code.go
  db/
    conn.go
  log/
    log.go
  main/
    chatserver.go
    gateserver.go
    httpserver.go
    loginserver.go
    slgserver.go
    wstest.go
  data/
    conf/
      db.sql
      env.ini
      mapRes_0.json
      json/
        basic.json
        map_build.json
        map_build_custom.json
        skill/
          skill_outline.json
          zuiji/
            zhongzhan.json
          zhudong/
            tuji.json
          zhihui/
            fengshi.json
          beidong/
            baizhanjingbing.json
        general/
          general.json
          general_arms.json
          general_basic.json
        facility/
          facility.json
          facility_addition.json
          facility_army_jfy.json
          facility_army_jjy.json
          facility_army_swy.json
          facility_army_tby.json
          facility_barrack_by.json
          facility_barrack_yby.json
          facility_camp_han.json
          facility_camp_qun.json
          facility_camp_shu.json
          facility_camp_wei.json
          facility_camp_wu.json
          facility_city.json
          facility_fct.json
          facility_general_jc.json
          facility_general_tst.json
          facility_market.json
          facility_mbs.json
          facility_produce_csc.json
          ... 共28个文件
        npc/
          npc_army.json
```

## 关键配置数据

### data/conf/mapRes_0.json

```json
{"w":200,"h":200,"list":[[53,6],[55,4],[52,7],[55,6],[54,6],[54,6],[55,7],[54,2],[53,2],[53,4],[52,6],[55,1],[52,6],[52,7],[54,6],[54,4],[55,6],[54,4],[52,4],[52,3],[54,8],[53,4],[54,4],[54,1],[52,5],[53,5],[55,4],[53,2],[55,2],[55,4],[53,2],[52,4],[54,4],[52,6],[53,1],[54,3],[55,6],[54,2],[53,7],[0,0],[0,0],[54,7],[52,2],[55,5],[53,7],[53,4],[52,6],[53,1],[52,7],[52,4],[52,5],[53,2],[55,2],[55,6],[55,3],[55,1],[53,6],[55,3],[0,0],[0,0],[0,0],[55,3],[52,6],[54,1],[52,2],[55,6],[55,1],[54,1],[55,6],[54,2],[53,6],[54,1],[53,5],[52,2],[53,6],[54,1],[53,5],[54,3],[52,1],[53,2],[53,6],[55,6],[50,5],[52,1],[53,2],[52,5],[54,1],[52,2],[53,7],[53,1],[54,1],[54,5],[53,7],[55,2],[52,1],[52,4],[52,1],[53,3],[53,3],[54,1],[55,5],[0,0],[55,2],[54,2],[53,1],[53,1],[53,1],[52,7],[52,1],[55,2],[53,1],[52,2],[52,5],[52,1],[54,2],[53,8],[55,4],[53,4],[55,7],[53,2],[52,1],[53,4],[52,6],[53,2],[52,5],[53,1],[54,1],[54,7],[55,1],[55,3],[52,4],[53,6],[52,2],[54,7],[55,3],[52,6],[53,1],[55,6],[54,2],[54,3],[52,5],[52,2],[52,7],[53,6],[55,1],[53,8],[55,5],[52,1],[55,7],[55,5],[55,1],[53,2],[54,7],[54,2],[54,1],[55,6],[55,2],[53,6],[53,2],[54,8],[54,1],[54,3],[54,4],[52,4],[52,2],[55,3],[55,4],[55,1],[55,1],[53,5],[55,1],[54,3],[54,5],[52,8],[54,2],[55,4],[54,2],[52,3],[55,2],[52,6],[55,1],[54,5],[52,3],[55,5],[55,6],[52,1],[53,2],[54,4],[53,5],[55,7],[54,6],[55,3],[55,7],[52,3],[53,2],[52,5],[53,3],[55,7],[53,2],[52,2],[52,4],[0,0],[0,0],[0,0],[54,3],[52,7],[52,5],[55,2],[52,2],[54,2],[52,3],[55,3],[53,7],[54,1],[53,4],[52,5],[52,6],[53,5],[55,2],[54,7],[55,2],[53,1],[55,5],[55,3],[55,3],[54,6],[54,6],[53,3],[52,6],[52,6],[53,7],[54,1],[55,5],[54,5],[55,8],[53,6],[54,5],[55,6],[53,4],[0,0],[0,0],[0,0],[0,0],[52,4],[55,5],[55,3],[55,1],[55,5],[53,2],[55,1],[53,2],[52,5],[54,7],[53,2],[53,2],[55,4],[55,7],[54,2],[0,0],[0,0],[0,0],[55,2],[52,3],[53,7],[52,2],[54,1],[55,2],[54,1],[53,2],[52,1],[54,8],[55,2],[54,3],[52,1],[53,4],[54,1],[52,6],[55,1],[52,7],[55,2],[55,2],[53,2],[54,6],[55,5],[53,2],[53,5],[52,6],[55,3],[55,3],[54,1],[52,1],[53,2],[53,6],[53,2],[52,4],[55,8],[55,3],[55,1],[52,2],[54,7],[52,1],[0,0],[52,5],[53,1],[54,3],[52,2],[54,1],[53,5],[53,7],[55,1],[55,2],[52,6],[55,2],[55,4],[52,7],[54,6],[53,2],[50,5],[54,1],[53,5],[55,2],[52,5],[50,5],[55,2],[52,1],[53,3],[53,1],[53,5],[55,5],[54,4],[52,3],[55,1],[52,1],[52,1],[52,4],[55,5],[53,7],[55,2],[52,1],[55,7],[54,4],[54,7],[54,6],[53,2],[54,3],[54,6],[55,2],[55,6],[52,3],[54,5],[54,5],[55,8],[52,6],[53,7],[55,4],[55,2],[53,5],[52,6],[55,1],[55,5],[53,2],[53,2],[55,5],[53,3],[54,2],[54,4],[50,5],[53,2],[52,2],[52,7],[52,3],[52,5],[55,5],[55,1],[55,1],[55,8],[54,5],[54,5],[55,1],[55,5],[53,1],[53,6],[54,1],[53,8],[54,7],[52,5],[53,1],[54,3],[53,2],[53,2],[54,7],[55,4],[53,8],[52,7],[55,3],[55,8],[52,6],[52,3],[52,7],[54,3],[52,1],[0,0],[0,0],[0,0],[53,5],[54,2],[55,2],[53,1],[54,3],[53,3],[52,2],[53,2],[55,4],[52,4],[52,7],[54,3],[52,1],[52,1],[53,6],[52,2],[52,1],[55,5],[53,8],[55,7],[55,1],[54,2],[52,1],[54,4]
```

### data/conf/json/map_build.json

```json
{
  "title": "地图资源配置",
  "cfg":[
    {"type": 50,
      "des": "系统要塞",
      "name": "要塞",
      "level": 5,
      "grain": 0,
      "wood": 0,
      "iron": 0,
      "stone": 0,
      "durable": 30000,
      "defender": 1
    },
    {"type": 51,
    "name": "城区",
    "level": 1,
    "grain": 0,
    "wood": 0,
    "iron": 0,
    "stone": 0,
    "durable": 100000,
    "defender": 5
   },
    {"type": 51,
      "name": "城区",
      "level": 2,
      "grain": 0,
      "wood": 0,
      "iron": 0,
      "stone": 0,
      "durable": 200000,
      "defender": 5
    },
    {"type": 51,
      "name": "城区",
      "level": 3,
      "grain": 0,
      "wood": 0,
      "iron": 0,
      "stone": 0,
      "durable": 300000,
      "defender": 5
    },
    {"type": 51,
      "name": "城区",
      "level": 4,
      "grain": 0,
      "wood": 0,
      "iron": 0,
      "stone": 0,
      "durable": 400000,
      "defender": 5
    },
    {"type": 51,
      "name": "城区",
      "level": 5,
      "grain": 0,
      "wood": 0,
      "iron": 0,
      "stone": 0,
      "durable": 500000,
      "defender": 5
    },
    {"type": 51,
      "name": "城区",
      "level": 6,
      "grain": 0,
      "wood": 0,
      "iron": 0,
      "stone": 0,
      "durable": 600000,
      "defender": 5
    },
    {"type": 51,
      "name": "城区",
      "level": 7,
      "grain": 0,
      "wood": 0,
      "iron": 0,
      "stone": 0,
      "durable": 700000,
      "defender": 5
    },
    {"type": 51,
      "name": "城区",
      "level": 8,
      "grain": 0,
      "wood": 0,
      "iron": 0,
      "stone": 0,
      "durable": 800000,
      "defender": 5
    },
    {"type": 51,
      "name": "城区",
      "level": 9,
      "grain": 0,
      "wood": 0,
      "iron": 0,
      "stone": 0,
      "durable": 900000,
      "defender": 5
    },
    {"type": 51,
      "name": "城区",
      "level": 10,
      "grain": 0,
      "wood": 0,
      "iron": 0,
      "stone": 0,
      "durable": 1000000,
      "defender": 5
    },
   {"type": 52,
     "name": "土地Lv.1",
     "level": 1,
     "grain": 100,
     "wood": 100,
     "iron": 100,
     "stone": 100,
     "durable": 10000,
     "defender": 1
   },
   {"type": 52,
     "name": "土地Lv.2",
     "level": 2,
     "grain": 200,
     "wood": 200,
     "iron": 200,
     "stone": 200,
     "durable": 10000,
     "defender": 2
   },
   {"type": 52,
     "name": "土地Lv.3",
     "level": 3,
     "grain": 300,
     "wood": 300,
     "iron": 300,
     "stone": 300,
     "durable": 100,
     "defender": 3
   },
   {"type": 52,
     "name": "土地Lv.4",
     "level": 4,
     "grain": 0,
     "wood": 4000,
     "iron": 0,
     "stone": 0,
     "durable": 10000,
     "defender": 4
   },
   {"type": 52,
     "name": "土地Lv.5",
     "level": 5,
     "grain": 0,
     "wood": 5000,
     "iron": 0,
     "stone": 0,
     "durable": 10000,
     "defender": 5
   },
    {"type": 52,
      "name": "土地Lv.6",
      "level": 6,
      "grain": 0,
      "wood": 1000,
      "iron": 0,
      "stone": 0,
     
```

### data/conf/json/map_build_custom.json

```json
{
  "title": "地图用户建设的建筑配置",
  "cfg": [
    {
      "type": 56,
      "name": "要塞",
      "levels": [
        {
          "level": 1,
          "durable": 10000,
          "defender": 5,
          "time": 100,
          "need": {
            "decree": 2,
            "grain": 1000,
            "wood": 1000,
            "iron": 1000,
            "stone": 1000
          },
          "result": {
            "army_cnt": 1
          }
        },
        {
          "level": 2,
          "durable": 10000,
          "defender": 5,
          "time": 200,
          "need": {
            "decree": 3,
            "grain": 2000,
            "wood": 2000,
            "iron": 2000,
            "stone": 2000
          },
          "result": {
            "army_cnt": 2
          }
        }
      ]
    }
  ]
}
```

### data/conf/json/basic.json

```json
{
  "conscript": {
    "des": "每征一个兵需要消耗的资源",
    "cost_wood":10,
    "cost_iron":10,
    "cost_stone":0,
    "cost_grain":10,
    "cost_gold":1,
    "cost_time":1
  },
  "general": {
    "des": "武将的一些配置",
    "physical_power_limit": 100,
    "cost_physical_power": 1,
    "recovery_physical_power": 10,
    "reclamation_time": 30,
    "reclamation_cost": 1,
    "draw_general_cost": 30,
    "pr_point": 1000,
    "limit": 500
  },
  "role": {
    "des": "角色的一些配置",
    "wood": 10000,
    "iron": 10000,
    "stone": 10000,
    "grain": 10000,
    "gold": 10000,
    "decree": 20,
    "wood_yield": 1000,
    "iron_yield": 1000,
    "stone_yield": 1000,
    "grain_yield": 1000,
    "gold_yield": 1000,
    "depot_capacity": 1000000,
    "build_limit": 20,
    "recovery_time": 20,
    "decree_limit": 20,
    "collect_times_limit": 3,
    "collect_interval": 30,
    "pos_tag_limit": 10
  },
  "city": {
    "des": "城池的一些配置",
    "cost": 75,
    "durable": 100000,
    "transform_rate": 50,
    "recovery_time": 600
  },
  "build": {
    "des": "建筑的一些配置",
    "war_free": 20,
    "giveUp_time": 30,
    "fortress_limit": 10
  },
  "union": {
    "des": "联盟的一些配置",
    "member_limit": 100
  }

}
```

### data/conf/json/skill/skill_outline.json

```json
{
  "trigger_type": {
    "des": "触发类型",
    "list": [
      {
        "type": 1,
        "des": "主动"
      },
      {
        "type": 2,
        "des": "被动"
      },
      {
        "type": 3,
        "des": "追击"
      },
      {
        "type": 4,
        "des": "指挥"
      }
    ]
  },
  "effect_type": {
    "des": "效果类型",
    "list": [
      {
        "type": 1,
        "des": "伤害率",
        "isRate": true
      },
      {
        "type": 2,
        "des": "攻击",
        "isRate": false
      },
      {
        "type": 3,
        "des": "防御",
        "isRate": false
      },
      {
        "type": 4,
        "des": "谋略",
        "isRate": false
      },
      {
        "type": 5,
        "des": "速度",
        "isRate": false
      },
      {
        "type": 6,
        "des": "破坏",
        "isRate": false
      }

    ]
  },
  "target_type": {
    "des": "作用目标类型",
    "list": [
      {
        "type": 1,
        "des": "自己"
      },
      {
        "type": 2,
        "des": "我军单体"
      },
      {
        "type": 3,
        "des": "我军1-2个目标"
      },
      {
        "type": 4,
        "des": "我军1-3个目标"
      },
      {
        "type": 5,
        "des": "我军全体"
      },
      {
        "type": 6,
        "des": "敌军单体"
      },
      {
        "type": 7,
        "des": "敌军1-2个目标"
      },
      {
        "type": 8,
        "des": "敌军1-3个目标"
      },
      {
        "type": 9,
        "des": "敌军全体"
      }
    ]
  }
}
```

### data/conf/json/skill/zuiji/zhongzhan.json

```json
{
  "cfgId": 301,
  "name": "重斩",
  "trigger": 3,
  "target": 6,
  "des": "普通攻击后，对攻击目标再次发动攻击（伤害率%n%%）",
  "limit": 3,
  "duration": 0,
  "arms": [
    1,
    4,
    7,
    3,
    6,
    9
  ],

  "include_effect": [
    1
  ],
  "levels": [
    {
      "probability":30,
      "effect_value": [50],
      "effect_round": [0]
    },
    {
      "probability":30,
      "effect_value": [50],
      "effect_round": [0]
    },
    {
      "probability":30,
      "effect_value": [50],
      "effect_round": [0]
    },
    {
      "probability":30,
      "effect_value": [50],
      "effect_round": [0]
    },
    {
      "probability":30,
      "effect_value": [50],
      "effect_round": [0]
    },
    {
      "probability":30,
      "effect_value": [50],
      "effect_round": [0]
    },
    {
      "probability":30,
      "effect_value": [50],
      "effect_round": [0]
    },
    {
      "probability":30,
      "effect_value": [50],
      "effect_round": [0]
    },
    {
      "probability":30,
      "effect_value": [50],
      "effect_round": [0]
    },
    {
      "probability":30,
      "effect_value": [50],
      "effect_round": [0]
    }
  ]
}

```

### data/conf/json/skill/zhudong/tuji.json

```json
{
  "cfgId": 101,
  "name": "突击",
  "trigger": 1,
  "target": 6,
  "des": "对敌军单体发动一次攻击（伤害率`%n%%`)",
  "limit": 3,
  "duration": 0,
  "arms": [
    1,
    4,
    7,
    3,
    6,
    9
  ],

  "include_effect": [
    1
  ],
  "levels": [
    {
      "probability":30,
      "effect_value": [50],
      "effect_round": [0]
    },
    {
      "probability":30,
      "effect_value": [50],
      "effect_round": [0]
    },
    {
      "probability":30,
      "effect_value": [50],
      "effect_round": [0]
    },
    {
      "probability":30,
      "effect_value": [50],
      "effect_round": [0]
    },
    {
      "probability":30,
      "effect_value": [50],
      "effect_round": [0]
    },
    {
      "probability":30,
      "effect_value": [50],
      "effect_round": [0]
    },
    {
      "probability":30,
      "effect_value": [50],
      "effect_round": [0]
    },
    {
      "probability":30,
      "effect_value": [50],
      "effect_round": [0]
    },
    {
      "probability":30,
      "effect_value": [50],
      "effect_round": [0]
    },
    {
      "probability":30,
      "effect_value": [50],
      "effect_round": [0]
    }
  ]
}

```

### data/conf/json/skill/zhihui/fengshi.json

```json
{
  "cfgId": 401,
  "name": "锋矢",
  "trigger": 4,
  "target": 5,
  "des": "战斗中，使我军全体进行普通攻击的伤害提升%n%",
  "limit": 3,
  "duration": 0,
  "arms": [
    2,
    5,
    8,
    3,
    6,
    9
  ],

  "include_effect": [
    1
  ],
  "levels": [
    {
      "probability":30,
      "effect_value": [50],
      "effect_round": [0]
    },
    {
      "probability":30,
      "effect_value": [50],
      "effect_round": [0]
    },
    {
      "probability":30,
      "effect_value": [50],
      "effect_round": [0]
    },
    {
      "probability":30,
      "effect_value": [50],
      "effect_round": [0]
    },
    {
      "probability":30,
      "effect_value": [50],
      "effect_round": [0]
    },
    {
      "probability":30,
      "effect_value": [50],
      "effect_round": [0]
    },
    {
      "probability":30,
      "effect_value": [50],
      "effect_round": [0]
    },
    {
      "probability":30,
      "effect_value": [50],
      "effect_round": [0]
    },
    {
      "probability":30,
      "effect_value": [50],
      "effect_round": [0]
    },
    {
      "probability":30,
      "effect_value": [50],
      "effect_round": [0]
    }
  ]
}

```

### data/conf/json/skill/beidong/baizhanjingbing.json

```json
{
  "cfgId": 201,
  "name": "百战精兵",
  "trigger": 2,
  "target": 1,
  "des": "使自身攻击属性提升%n%、防御属性提升%n%、谋略属性提升%n%、速度属性提升%n%",
  "limit": 3,
  "duration": 0,
  "arms": [
    1,
    4,
    7,
    2,
    5,
    8,
    3,
    6,
    9
  ],

  "include_effect": [
    2,3,4,5
  ],
  "levels": [
    {
      "probability":30,
      "effect_value": [50,50,50,50],
      "effect_round": [0]
    },
    {
      "probability":30,
      "effect_value": [50,50,50,50],
      "effect_round": [0]
    },
    {
      "probability":30,
      "effect_value": [50,50,50,50],
      "effect_round": [0]
    },
    {
      "probability":30,
      "effect_value": [50,50,50,50],
      "effect_round": [0]
    },
    {
      "probability":30,
      "effect_value": [50,50,50,50],
      "effect_round": [0]
    },
    {
      "probability":30,
      "effect_value": [50,50,50,50],
      "effect_round": [0]
    },
    {
      "probability":30,
      "effect_value": [50,50,50,50],
      "effect_round": [0]
    },
    {
      "probability":30,
      "effect_value": [50,50,50,50],
      "effect_round": [0]
    },
    {
      "probability":30,
      "effect_value": [50,50,50,50],
      "effect_round": [0]
    },
    {
      "probability":30,
      "effect_value": [50,50,50,50],
      "effect_round": [0]
    }
  ]
}

```

### data/conf/json/general/general.json

```json
{
	"title": "武将配置",
	"list": [
		{
			"name": "十常士",
			"cfgId": 100002,
			"force": 8400,
			"strategy": 8500,
			"defense": 9000,
			"speed": 6200,
			"destroy": 2100,
			"cost": 30,
			"force_grow": 30,
			"strategy_grow": 40,
			"defense_grow": 40,
			"speed_grow": 20,
			"destroy_grow": 40,
			"physical_power_limit": 100,
			"cost_physical_power": 1,
			"probability": 7,
			"star": 5,
			"arms": [
				2,
				5,
				8
			],
			"camp": 1
		},
		{
			"name": "吕布",
			"cfgId": 100003,
			"force": 9600,
			"strategy": 5500,
			"defense": 9700,
			"speed": 9000,
			"destroy": 1800,
			"cost": 30,
			"force_grow": 80,
			"strategy_grow": 20,
			"defense_grow": 50,
			"speed_grow": 80,
			"destroy_grow": 50,
			"physical_power_limit": 100,
			"cost_physical_power": 1,
			"probability": 12,
			"star": 5,
			"arms": [
				3,
				6,
				9
			],
			"camp": 1
		},
		{
			"name": "蔡文姬",
			"cfgId": 100004,
			"force": 8500,
			"strategy": 8500,
			"defense": 8100,
			"speed": 8300,
			"destroy": 2000,
			"cost": 25,
			"force_grow": 80,
			"strategy_grow": 60,
			"defense_grow": 55.00000000000001,
			"speed_grow": 78,
			"destroy_grow": 55.00000000000001,
			"physical_power_limit": 100,
			"cost_physical_power": 1,
			"probability": 21,
			"star": 5,
			"arms": [
				3,
				6,
				9
			],
			"camp": 1
		},
		{
			"name": "貂蝉",
			"cfgId": 100005,
			"force": 8800,
			"strategy": 8400,
			"defense": 8900,
			"speed": 8300,
			"destroy": 2000,
			"cost": 30,
			"force_grow": 65,
			"strategy_grow": 75,
			"defense_grow": 80,
			"speed_grow": 67,
			"destroy_grow": 80,
			"physical_power_limit": 100,
			"cost_physical_power": 1,
			"probability": 22,
			"star": 5,
			"arms": [
				3,
				6,
				9
			],
			"camp": 2
		},
		{
			"name": "袁绍",
			"cfgId": 100006,
			"force": 8100,
			"strategy": 5000,
			"defense": 7900,
			"speed": 4300,
			"destroy": 7000,
			"cost": 30,
			"force_grow": 30,
			"strategy_grow": 50,
			"defense_grow": 50,
			"speed_grow": 20,
			"destroy_grow": 50,
			"physical_power_limit": 100,
			"cost_physical_power": 1,
			"probability": 24,
			"star": 5,
			"arms": [
				1,
				4,
				7
			],
			"camp": 1
		},
		{
			"name": "卢植",
			"cfgId": 100007,
			"force": 8900,
			"strategy": 8000,
			"defense": 9000,
			"speed": 8600,
			"destroy": 1600,
			"cost": 35,
			"force_grow": 70,
			"strategy_grow": 50,
			"defense_grow": 50,
			"speed_grow": 76,
			"destroy_grow": 50,
			"physical_power_limit": 100,
			"cost_physical_power": 1,
			"probability": 5,
			"star": 5,
			"arms": [
				3,
				6,
				9
			],
			"camp": 1
		},
		{
			"name": "张角",
			"cfgId": 100008,
			"force": 9100,
			"strategy": 9200,
			"defense": 8900,
			"speed": 9000,
			"destroy": 1300,
			"cost": 35,
			"force_grow": 80,
			"strategy_grow": 88,
			"defense_grow": 84,
			"speed_grow": 83,
			"destroy_grow": 84,
			"physical_power_limit": 100,
			"cost_physical_power": 1,
			"probability": 10,
			"star": 5,
			"arms": [
				3,
				6,
				9
			],
			"camp": 2
		},
		{
		
```



## 策划参考价值
SLG系统模块的代码实现参考（征兵/出征/建筑/联盟等）。
