# chinasoft

## 1201

### 基于断言的动态验证

- 微处理器敏捷设计：硬件“软化”
  - 软件工程技术在微处理器设计中的迁移
- verilog阻塞赋值和非阻塞赋值区别


### 袁军

- 芯片形式验证漫谈
- 芯片设计前端
- 为什么要形式验证
  
```
既然是人类两大认知体系归纳和演繹之一，形式验证虽然迟到于仿真，但只能会更快的找到属于自己的应用场景
lntel的浮点除法事件之后，形式验证从科研走向实际应用
形式验证工具也从院校科研和芯片公司自研整合到龙头EDA企业
形式验证做法方法已经应用在芯片前端设计验证(模型验证），设计实现流程验证(各种等价验证)，时序验证（跨时钟域，跨复位域
，时钟约束），低功括，x态传插，芯片数据流安全，SOC连线等诸多领域
而新的应用场景如汽车功能安全(Fusa)，算法硬件加速(C2RTU), Al形式验证等正在不断酒现
简言之，大规模，高端，高复杂度，高可第性要求，高市场占有度的芯片设计对形式验证是刚需国内龙头通讯企业，大型信创企业，中高端CPU/MCU/GPU企业等国sntel, Apple, IBM, Qualcom, NXP三星等
```

- Inter, Apple
- Japser
  - AE
  - 形式验证服务公司Oski，Nvidia收购

- k-ind
  - induction strengthening
  - 关键是unique path constraint
- interpolation
  - caig-inter
  - double over-approx loop
- IC3/PDR
- Abstraction
- 学术界
  - Spin/Cospan
  - Verdict.
  - ...
- 商用
  - OneSpin
  - VCFormal/Synopsys
    - LTL
  - IFV/Cadence
  - JasperGold/Jasper
  - Averant: ARM's first model checking partner
  - 国产
    - AveMC/奥卡斯
    - 芯华章
  
### 硬件安全验证和形式化验证

- 属性提取
  
### 基于数据通路的模型检验

- data path abstraction
  - 常量抽象成未解释符号
    - 00 => zero, 11 => max
  - 操作抽象成未解释函数
    - > => GT, +1 => INC
- data path propagation: add data path lemmas /\ ADD(0, 1) = 1
  - propagatin constant values from the concrete domain to abstract domain
  - 如果抽象域没定义，不做传播
  - 把数据通路操作、语义用规则方式记录，再注入到model checking中
- IC3 call SMT solvers之前调用数据通路传播检查

- 相比层次化SMT solver，做到程序里面可以更灵活地处理规则

### 金意儿

- microScope
- 形式化工具认识硬件代码
  - 代码翻译工具，做验证
- assertion怎么生成
  - 什么叫硬件漏洞
  - AES电路侧信道
  - llm
  - HW-SCM：当前工具围绕电路性质来，不同时间点给不同的指令，组合成漏洞挖掘的应用，处理时序逻辑的能力不够
  - SVA提供了框架，但是很多工具对SVA的支撑不太好
- ASP-DAC
- JasperGold:测试和形式化的结合跟平衡
  - 工业界关注把版图先补上去，后面可以迭代
  - 先给一个东西
  - 把原来做测试的能力赋能过来
- 最终目的：能达到什么效果，易用性大于能达到的效果
  - 能支撑，再到能干啥
- CAV，大模型把自然语言转成时序逻辑
