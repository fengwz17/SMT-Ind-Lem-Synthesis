# Constrained Horn Clauses (CHC)

A Constrained Horn Clause (CHC) is a FOL formula of the form 
- $\forall V.(\varphi \wedge p_1[X_1] \wedge \cdots \wedge p_n [X_n]) \implies h[X]$
- $\varphi$: constraint in a background theory.
- V: variables, and $X_i$ are terms over V
- $p_1, \cdots, p_n, h$: n-ary predicates
- $p_i[X]$: application of a predicate to first-order 

ADT验证
特定类型理论
用smt求解 处理UF
深度有个界限，和用到的UF，变量有关，cut off
list