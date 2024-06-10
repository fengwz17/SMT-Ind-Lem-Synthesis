# Inductive Reasoning & Lemma Synthesis调研

## Inductive Reasoning

### 工具

- cvc5 
  - ADT inductive reasoning([Automated induction for datatypes](http://homepage.cs.uiowa.edu/~ajreynol/vmcai15.pdf))
    - `--quant-ind`, `int-wf-ind`
  - [fmf-fun](https://github.com/cvc5/cvc5/issues/5189) 
    - Finite model finding
  - [ijcar16 Model Finding for Recursive Functions in SMT](https://homepage.divms.uiowa.edu/~ajreynol/ijcar16a.pdf)
    - Techniques for finding counterexamples for conjectures in the presence of recursive functions
  - 非线性（可能有用）
    - `--nl-ext-planes`
   
- Z3
  - 不能做inductive reasoning([Z3 will not prove inductive facts](https://www.philipzucker.com/z3-rise4fun/guide.html), [z3-induction](https://microsoft.github.io/z3guide/docs/theories/Datatypes/#z3-will-not-prove-inductive-facts)), 通常方法是手动提供induction hypothesis([does z3 support proving inductive facts at all?](https://stackoverflow.com/questions/45947230/does-z3-support-proving-inductive-facts-at-all)), Z3不断展开递归函数定义，但不涉及inductive reasoning:[Recursive Functions](https://microsoft.github.io/z3guide/docs/logic/Recursive%20Functions)
  - [Proving some Inductive Facts about Lists using Z3 python](https://www.philipzucker.com/proving-some-inductive-facts-about-lists-using-z3-python/): 提到VMCAI'15的方法

- Vampire
  - [vampire](https://vprover.github.io/)
  - [Inductive proofs in theorem provers (Z3, Vampire, with TPTP syntax)](https://stackoverflow.com/questions/71935852/inductive-proofs-in-theorem-provers-z3-vampire-with-tptp-syntax)
  - `--induction int/struct/both`

- Zipperposition
  - [Zipperposition, a new platform for Deduction Modulo](https://simon.cedeela.fr/assets/talks/2017_lsv_zipper.pdf)
  - [An overview of the Superposition Calculus](https://simon.cedeela.fr/assets/jetbrains_2021.pdf)
  - [Superposition with Structural Induction](https://simon.cedeela.fr/assets/talks/2017_frocos.pdf)a
  - a superposition prover
  - input TIP, TPTP

- ACL2，Zeno？
  - 自动定理证明器


### 文章

- TIP相关
  - **LPAR'15 TIP Tools**
    - In this paper, we demonstrate a set of tools for transformaing and processing inductive problems.
    - TIP format consists of: SMT-LIB plus `declare-datatypes`, `define-funs-rec`, `match`, `par`.
    - Supply a transformation that applies structral induction to the conjecture.

- Vampire
  - **CAV'13 First-Order Theorem Proving and VAMPIRE**
  - **CADE'19 Induction in Saturation-Based Proof Search**
  - **CICM'20 Induction with Generalization in Superposition Reasoning**
  - **CADE'21 Integer Induction in Saturation**
    - 
  - **FMCAD'21 Induction with Recursive Definitions in Superposition**
    - Induction formula generation method, inductive strengthening and generalization.
  - **PAAR'22workshop The Vampire Approach to Induction**
    - Using an appropriate induction schema to generate inductive formulas as (4). 
      - $(F[nil] \wedge \forall y, z. (F[z] \rightarrow F[cons(y, z)])) \rightarrow \forall x. F[x]$
    - goal oriented
    - two ways/options for applying induction formulas in saturation
      - Addition
      - Resolution
  - **Thesis'20 Automating Inductive reasoning with Recursive Functions**
    - The superposition calculus
      - An *inference*: $\frac{F_1 \cdots F_n}{G}$, the *premise* and the *conclusion*.
      - 'Most modern first-order theorem provers use the *superposition calculus as their inference system*'.
      - Sup is *sound* and *refutationally complete*.
        - A *refutation* is a derivation of $\bot$.
        - Refutational completeness means for any unsatisfiable formula set, we can derive the empty clause.
        - "Therefore, with superposition we usually negate our input conjecture and try to refute it which, if successful, means the original conjecture is valid." 
      - Sup consists of the following rules (CAV'13 First Order Theorem Proving and Vampire)
        - Resolution, Factoring, Superposition, Equality Resolution, Equality Factoring.
    - **Chapter 4. Induction in proof search**
      - 4.1 Induction inference
        - 证明目标$\forall x. L[x]$, 生成induction function $formula \rightarrow \forall x. L[x]$.
        - Binary resolve(the inference rule): $\frac{formula \rightarrow \forall x_1, \cdots, x_n. \overline{L}[x_1]\cdots[x_n] \quad L[\sigma_1]\cdots[\sigma_n]\vee C}{cnf(\neg formula \vee C)}(Ind)$. where $L[\sigma_1]\cdots[\sigma_n]$ is a ground literal and $formula\rightarrow \forall x_1, \cdots, x_n.\overline{L}[x_1]\cdots[x_n]$ is a valid induction formula.
        - 在saturation-based proof search中可以直接加入clausified induction formula到搜索空间.
        - Refer to CADE'19 (*Induction in Saturation-Based Proof Search*) and CICM'20 (*Induction with Generalization in Superposition Reasoning*).
      - 4.2 Rewriting with function definitions
      - 
  - **Getting Saturated with Induction**

- cvc5
  - **VMCAI'12 Automating Induction with an SMT Solver**
  - ***VMCAI'15 Induction for SMT Solvers***
    - Automated induction for datatypes and integers in cvc5
    - Skolemization with inductive strengthening, subgoal generation 
      - inductive strengthening
        - the general scheme* for strengthening the skolemization according to R is $(\forall x. P(x)) \vee (\neg P(k) \wedge \forall x. (R(x, k) \Rightarrow P(x)))$, where $k$ is a fresh constant. We call $\forall x. (R(x, k) \Rightarrow P(x))$ the *inductive strengthening*.
        - example: $\neg len(k) \ge 0 \wedge \forall y. (k \approx cons(head(k), tail(k)) \wedge y \approx tail(k)\Rightarrow len(y) \ge 0)$ 
        - simplifies to $k \approx cons(head(k), tail(k)) \Rightarrow len(tail(k)) \ge 0$.
      - filtering candidate subgoals
        - **filtering based on active conjectures**
          - the solver cannot reason about $\Sigma'$-constraints simply based on a combination of ground theory reasoning and unfolding function defs by quantifier instantiation. The first filtering is to generate candidate subgoals that state properties about terms that generalize $\Sigma'$-terms only.
          - ones that are not entailed to be equivalent to $\Sigma$-terms in the current context are **active**.
          - in Example 4, $sum(x)$ is relevant, since it generates $sum(k)$ and $sum(k)$ is ground-relevant since $k$ is active; $sum(rev(x))$ is not relevant since it only generates $sum(rev(k))$, which is not ground-relevant since $rev(k)$ is inactive. Then all candidate subgoals of the form $\forall x. sum(rev(x)) \approx s$.
        - **filtering based on canonicity**
          - compute a set of equalities $U$ (from M) and $U^*$ (from subgoal). A term is **canonical** in $U^*$ iff it is a representative of an equivalence class in $U^*$ and **non-canonical** in $U^*$ iff it exists in $U^*$ and is not cannonical. If a subgoal contains the non-canonical subterm, then it is redundant.
        - **filtering based on ground facts**
    - Inductive strenghtening: 
      - `dt-stc-ind`:apply strengthening for existential quantification over datatypes based on structural induction 
      - `int-wf-ind`:apply strengthening for integers based on well-founded induction 
      - `quant-ind`:use all available techniques for inductive reasoning 

- Zipperposition
  - **thesis'15 Extending Superposition with Integer Arithmetic,Structural Induction, and Beyond**
  - **FroCoS'17 Superposition with Structural Induction**


## Synthesis

### 文章

- SyGuS
  - syntax-guided synthesis in cvc5
    - **CAV'15 Counterexample-Guided Quantifier Instantiation for Synthesis in SMT**
  - **CP'19 Lemma Synthesis for Automating Induction over Algebraic Data Types**
- data-driven
  - **OOPSLA'22 Data Driven Lemma Synthesis**
- Learning-based
  - **OOPLSA'22 Synthesizing Axiomatizations using Logic Learning**
    - implement based on z3
- CEGIS
  - **OOPSLA'22 Model-Guided Synthesis of Inductive Lemmas for FOL with Least Fixpoints**
- 综述
  - **Lemma Discovery for Induction - A Survey**
    - top-down
      - Trying to derive a lemma from the conjecture we are trying to prove.
      - Zeno: automated inductive prover for proving properties about a subset of Haskell programs. It can generate lemmas by the common sub-term technique shown in Example 1, and applies a counter-example finder to avoid over-generalisations.
      - Generalisation方法可以工作的很好，但也可能因为over-generalise而产生false statements，一般需要和counter-example checking结合。应用generalisation的时机对效果影响比较大。
      - Example 2:单纯使用common sub-term generalisation无法证明。
      - **Rippling**方法：
        - Lemma Calculation:应用归纳假设后如果归纳证明失败，适用common sub-term generalisation，尝试将其视作lemma进行证明
        - Generalisation:对example2这种例子如果证明失败的话，heuristics会意识到需要引入conjuecture的generalisation，这被称为*sink*. 构建schematic lemma（包含一些高阶meta-variables），尝试进行归纳证明，并应用归纳假设和重写对meta-ariables做实例化.该方法可以用于证明example2,但仍然需要预先引入一些关于append-functions的lemma.
        - Lemma Speculation:如果rippling在归纳假设可以应用之前stuck，类似generalisation，构建一个underspecified lemma，右边匹配一些合适的sub-term来进行重写，左边由higher-order meta-variable组成.
        - 这些方法是现在OYSTERCLAM system中.
    - bottom-up
      - 上面的方法可以认为是目标导向，对目标进行证明的过程中构建missing lemma，另一种方法被称为*theory exploration*，从available symbols开始构建“basic，interesting lemmas”.
      - 相关方法具有相同的框架：首先通过对具体值或反例检查来生成terms和equations，然后尝试通过之前发现和证明的lemma来自动进行归纳证明。不同的地方在于他们生成conjuectures的heuristics不同，以及evaluate和judge这些conjuectures的方法不同.
      - **MATHsAiD**:首先从小的term中构建terms of interest, 使用一些heuristics比如寻找公共属性如交换律、结合律和分配律等；然后选择一个terms of insterst中的变量用concrete value比如two做实例化，然后通过用变量替换two再构建candidate equation
      - **IsaCoSy**:只生成irreducible的terms，即不能被适用任何equations进一步重写来reduce的terms. 从minimal size如single constants，variables开始生成equational terms，然后生成每个size下所有可能的irreducible type-correct terms；然后这些equations被通过counter-example finder来filter. 剩下的交给IsaPlanner去证明.
      - **IsaScheme**:user-defined schemas capture common patterns比如交换律等;自动进行实例化.另外包含了Knuth-Bendix completion pass来保证新发现的conjuecture不是之前某一个的generalisation，从而使发现的lemmas形成一个termination set of rewrite rules.
      - **QuickSpec**:自动构造和测试Haskell程序中equational specifications的系统，不做证明，理论上更快. 不一次生成所有的equations，而是只有可能make candidate left- and right hand sides的terms；然后调用QuickCheck进行检查，来对所有terms中的variables生成随机值. 最初所有terms都在一个等价类中，经过许多轮的testing之后建立equivalence class，从中提取出equations
      - **HipSpec system**:在一个inductive theorem prover中集成了QuickSpec，对conjecture应用induction然后将proof obligations传到一个external automated provers（first-order or SMT solvers）中.
      - **Hipster**：类似HipSpec，但适用Isabelle/HOL进行formally checked. 两个tactics，*routine reasoning*和*hard reasoning*；被routine reasoning证明的lemmas不展示给users，hard reasoning证明的lemmas返回. Common configurations是使用Isabelle's simplifier（rewriting）或Sledgehammer(调用外部自动定理证明器)作为routine tactics. 然后一些形式的induction作为hard tactics.
    - Machine Learning and Lemma by Analogy
      - 使用machine learning来identify新的conjecture和library中已有lemma的相似性.
    - Inductin in first-order provers and SMT solvers.
      - **cvc4**:在DPLL(T)引擎中集成了local theory exploration. 类似QuickSpec，枚举terms到最大size，然后heuristically基于当前context选择一个子集用于proof search.
        - removing reducible terms，类似IsaCoSy.
        - generating ground instances of terms来探测falsify，类似QuickSpec使用QuickCheck
      - **Pirate**：扩展superposition calculus，使其包含type system和datatypes上的induction.
      - **Zipperposition**:Simon Cruanes对其进行扩展使得能支持structural induction.
- **CADE'21 Integer Induction in Saturation**文章提到的invariant generation文章
  - **CAV‘19 Quantified Invariants via Syntax-Guided Synthesis**
  - **FMCAD‘20 Trace Logic for Inductive Loop Reasoning**


## ADT with RDF

### Papers

- **POPL'10 Decision Procedures for Algebraic Data Types with Abstractions**
  - Describe a parametric decision procedure for reasoning about algebraic data types using catamorphism (fold) funcions.

- **VSTTE'13 An Improved Unrolling-Based Decision Procedure for Algebraic Data Types**
  - rada

- **Model Finding for Recursive Functions in SMT**
  - 本文主要关注"model finding"，由于经典的"finite model finding"方法不适用于infinite domains，比如integers或ADT，本文提出一种转换，可以将ADT和integer的递归函数问题转换到有限定义域上再应用fmf方法.

### 材料

[6.S981 Introduction to Program Synthesis Fall 2023](https://people.csail.mit.edu/asolar/SynthesisCourse/index.htm)

## Notes 

### 0329

- 研究的RDF公式形式和范围
```
def rec(l: ADT)
case nil => a
case (h :: tail) => hx + 2 * rec(tail)
```
- 关注递归定义相关的求解，包括chc

- 对比实验，现在的工具能不能求解我们的公式，分析比较，按照什么样的方式分析总结

- 注意归纳定义：每个工具能处理的归纳定义形式，带量词，不带量词，优缺点

### 0401 

- 文章思路：对于一个RDF问题，对于用户来说，可能有什么解决办法，是用chc还是smt，不同的方法有什么作用范围和优势。分别用了什么样的技术，各有色和什么特点和应用范围。

### 0403

- 关注递归定义函数的问题，不局限于ADT，还有参数为整数等其他更一般情况
- 对catamorphism相关文章的调研，关注相关文章的方法适用范围，对操作需要做什么样的限定，怎么取catamorphism的子集。
- 另外调研其他更一般的递归函数的问题，有没有其他方法。
- 工具状态，有些工具是不是没有维护了

### 0410

- 分析整理不同的技术，理解他们的应用范围和异同，学习survey的写法，把这些技术统一到我们的框架里面
- 收集benchmark，跑工具，比较效果，看看不同工具的能力.
- Vampire: cade/ijcar证明比赛冠军

### 0417

- 收集benchmark，注意要尝试用stainless生成乘除法器例子的benchmark

### 0424

- 看一下CHC那边的benchmarks，也是相关的，考虑把这边的公式用那边的工具跑一下（通过加入存在量词进行转换，成为CHC那边的形式？）

### 0430

- 收集自己的benchmark，用smt和chc工具跑.

### 0508

- 通过脚本等构造benchmark
- 目前的一个例子：pow2连除是无法自动证明的.

- cvc5 configuration
  - 注意非线性可以考虑加上`--nl-ext-planes`
- vampire
  - `--ignore-missing on`
  
### 0515
- 整理benchmark suit分类，评估
  - 比如按照benchmark中递归定义的类型 
  - 评测不同工具的能力
- 把div转成乘法尝试一下.

### 0521
- cvc5无法求解`x >= Pow2(bitLength(x) - 1)`是因为无法处理整数除法？
  - 中间需要一步`x / 2 * 2 <= x`?
  - `(div x 2)`?

- *inductive benchmarks*
  - data type
    - list
      - crafted_assorted, 23个例子
        - `declare-datatypes (nat, lst)`
          - `add`, `app`
  - integer
    - power, `pow(x, e)`
      - `e >= 0, 2, 16, 1024`, `pow(x * y, e) = pow(x, e) * pow(y, e)`
      - `x <= 0, y <= 0, e >= 0, 2, 16, 1024`, `pow(x * y, e) = pow(x, e) * pow(y, e)`
      - `x >= 0, y >= 0, e >= 0, 2, 16, 1024`, `pow(x * y, e) = pow(x, e) * pow(y, e)`
      - `e >= 1, 3, 17, 1025`, `pow(x * y, e) = pow(x, e) * pow(y, e)`
      - `x <= 0, y <= 0, e >= 1, 3, 17, 1025`, `pow(x * y, e) = pow(x, e) * pow(y, e)`
      - `x >= 0, y >= 0, e >= 1, 3, 17, 1025`, `pow(x * y, e) = pow(x, e) * pow(y, e)`
    - sumX, `sumX(x, y)`, `x + (x + 1) + ... + y`
    - f



### 0604

- 思考能够从什么方向提出改进
- 归纳定义，含有量词的
  - 归纳定义可以看作是一个全称量词的模板
- 强归纳
- 归纳定义加上量词，提一些量词消去的方法；有全称量词和存在量词嵌套的时候

### 0609

- 读*Integer Induction in Saturation*文章
  - 关注invariant generation技术，用于生成recursive function的invariants，作为lemma