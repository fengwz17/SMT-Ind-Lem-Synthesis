# Induction for SMT Solvers

## Section 2

Well-founded ordering(良基)

- An order $\le$ is well-founded R <=> $\forall a_1 \ge a_2 \cdots $, there exists $i > 0$, such that $a_i = a_{i+1} = ...$, or $\forall a_1 > a_2 \cdots$ <=> the chain will terminate at some $i > 0$, or (From wiki) $\forall S \subseteq M$, and $S \ne \empty \Rightarrow \exists s \in S, \forall m \in S, (s, m) \notin R$, here $R$ is a relation.  
  - From the definition from wikipedia, we know that The Minimal Element in a set is an element which can not compare by relation R, so we got that: $b \in B$ is a minimal element <=> $\forall x \in B, x \nprec b$.

- [(6) 笔记：自然数，数学归纳原理，强归纳原理，良序，良基关系，无穷递降原理 - AC-DC的文章](https://zhuanlan.zhihu.com/p/666022582)
  - 设X是集合，$\prec$是X上的二元关系，称$\prec$是X上的良基关系，当且仅当X的每一个非空子集在$\prec$下都有极小元。（$\prec$是X上的良基关系蕴含了非自反性，即$\forall x\in X(\neg (x \prec x))$）.

## 3 Subgoal Generation

A naive approach: enumerate candidate subgoals according to a fair strategy until a set of sufficient subgoals is discovered.

- not scalable.
- it is crucial to avoid enumeration of a vast majority of candidate subgoals $\varphi$, either by determining that $\varphi$ is not relevant, redundant, or does not hold.

- subgoal generation module
  - First describe the scheme for **basic operation** of the subgoal generation module in relation to the rest of the SMT solver, 
  - and then describe several **heuristics** for how it determines which subgoals are likely to be relevant. 
  - The approach is similar to that of subgoal generation in the Quickspec, which enumerates candidate subgoals in a principled fashion that can in turn be used within a theorem prover.

### 3.1 Subgoal Generation in DPLL(T)


