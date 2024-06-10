# para-bv benchmark try

测试不同的函数引入lemma和DSL对Stainless求解的影响，以及在para-bv上一些例子的相关尝试

## Xiangshan divider

`def lemma_shftReg_range`函数：

- 去掉整个DSL，改为`Pow2.Pow2Mul(len, cnt + 1, len - cnt - 1)`, 可以求解.


## cvc5 source code

pow2 Lemma for exponential Laws 

- src/theory/arith/nl/pow2_solver.cpp

  ```cpp
  // laws of exponents: 2^x * 2^y = 2^(x+y)
  for (uint64_t j = i + 1; j < size; j++)
  {
    Node m = d_pow2s[j];
    Node valPow2yAbstract = d_model.computeAbstractModelValue(m);
    Node valYConcrete = d_model.computeConcreteModelValue(m[0]);  
    Integer y = valYConcrete.getConst<Rational>().getNumerator();
    Integer pow2y = valPow2yAbstract.getConst<Rational>().getNumerator();  
    Node n_mul_m = nm->mkNode(Kind::MULT, n, m);
    Node x_plus_y = nm->mkNode(Kind::ADD,n[0], m[0]);
    Node pow2_x_plus_y = nm->mkNode(Kind::POW2, x_plus_y);
    Node lem = nm->mkNode(Kind::EQUAL, n_mul_m, pow2_x_plus_y);
    d_im.addPendingLemma(
        lem, InferenceId::ARITH_NL_POW2_EXP_LAW_REFINE, nullptr, true);
  }

  // End of additional lemma schemas 
  ```

- src/theory/inference_id.cpp
- test/regress/cli/CMakeLists.txt
  
  ```cpp
  regress0/nl/pow2-native-3.smt2
  regress0/nl/pow2-pow.smt2
  regress0/nl/pow2-pow-isabelle.smt2
  regress0/nl/pow2-laws-of-exp.smt2
  regress0/nl/proj-issue-348.smt2
  regress0/nl/proj-issue-425.smt2
  regress0/nl/proj-issue-444-memout-eqelim.smt2
  ```

- test/regress/cli/regress0/nl/pow2-laws-of-exp.smt2

  ```cpp
  (set-logic ALL)
  (set-option :produce-models true)
  (set-option :incremental true)
  (set-info :smt-lib-version 2.6)
  (set-info :status unsat)
  (declare-const x Int)
  (declare-const y Int)
  (assert (distinct (* (^ 2 x) (^ 2 y)) (^ 2 (+ x y))))
  (check-sat)
  (exit)
  ```

## stainless-hand-example

发现pow2base和pow2mul同时assert，会造成e-matching的死循环.

