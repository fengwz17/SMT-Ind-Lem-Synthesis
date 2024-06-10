# SMT

## EUF and Combination of Theories 

### The Nelson-Oppen method

#### Step1: Purification: validity-preserving transformation of the formula after which predicates from different theories are not mixed.

`f(f(x1) - f(x2)) != f(x3)` => `f(a) != f(x3) /\ a = f(x1) - f(x2)` => ...

#### After purification we are left with several sets of pure expressions F1 ... Fn:

- Fi belongs to some 'pure' theory which we can decide.
- Shared variables are allowed.
- $\phi$ is satisfiable <-> F1 /\ ... /\ Fn is satisfiable
- `x2 >= x1 /\ x1 - x3 >= x2 /\ x3 >= 0 /\ f(a) != f(x3) /\ a = a1 - a2 /\ a1 = f(x1) /\ a2 = f(x2)` => `\phi_1: x2 >= x1 /\ ... /\ a = a1 - a2` /\ `\phi_2: f(a) != f(x3) /\ a_1 = f(x1) ...` 

#### A basic algorithm

- 1. Purify `\phi` into `F1 /\ ... /\ Fn`
- 2. if $\exists i, F_i$ is unsat, return unsat
- 3. if $\exists i, j. F_i$ implies an equality not implied by $F_j$, add it to $F_j$ and goto step2.
- 4. Return `sat`
- 等式传播结束后没冲突就返回sat

#### Convexity of Theories

- Convex: Linear Arithmetic over R, EUF
- Linear arithmetic over Z is not convex
  - $x_1 = 1 \wedge x_2 = 2 \wedge 1 \le x_3 \wedge x_3 \le 2 \Rightarrow (x_3 = x_1) \vee x_3 = x_2$ holds, neither $x_1 = 1 \wedge x_2 = 2 \wedge 1 \le x_3 \wedge x_3 \le 2 \Rightarrow x_3 = x_1$ nor $x_1 = 1 \wedge x_2 = 2 \wedge 1 \le x_3 \wedge x_3 \le 2 \Rightarrow x_3 = x_2$
- 基本版本要求理论凸性
- 对非凸理论要能够传播析取式（propagate disjunction for nun-convex theories）
  - 划分成好几个凸的空间
  - $x = 1 \wedge x = 2$分情况求解.

#### The full algorithm

#### Stably Infinite Theories

- A $\Sigma$-theory is stably infinite if every satisfiable formula has a model with an inifinite domain.

#### 正确性