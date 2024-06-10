# Solving Constrained Horn Clauses Modulo Algebraic Data Types and Recursive Functions

## 4 CHCs Modulo ADT And Catamorphisms

### Catamorphisms

[Catamorphisms in 15 Miniutes](http://chrislambda.github.io/blog/2014/01/30/catamorphisms-in-15-minutes/)

A catamorphism (or, generalized fold) is an **RDF** that abstracts the content of an ADT into a single value.

Formally, given $b, \oplus$, the following function axiom defines $f$ as a catamorphism over $\text{List}_s$

$\forall x. f(x) = ite(x = nil, b, head(x) \oplus f(tail(x)))$

We denote such a function axiom $\varphi(|b, \oplus|)$ and call it a catamorphism axiom for $f$.

- Example 4.1. The *length* of a list is a catamorphism from List to Int specified by: 
$\varphi(|0, +1|) \triangleq \forall x. length(x) = ite(x = nil, 0, 1 + length(tail(x)))$

The theory of ADTs with catamorphisms (and, more generally, RDFs) is undecidable.


## 5 Reducting CHCs Modulo Catamorphisms to CHCs

In this section, the paper presents a transformation that takes as input a set of CHCs modulo RDFs, $C_f \wedge \varphi_{(|b, \oplus|)}$, and produces a set of CHCs without RDFs, $C_F$. 

The transformation preseves satisfiability (Thm. 5.7) but not solutions (Ex. 5.8). Note that all solutions to $C_F$ are solutions to $C_f \wedge RC_F^+(\varphi(|b, \oplus|))$.

## 6 Introducing RDF Abstractions Into CHCs

### 6.1 Abstraction of RDF

- The first abstraction unfolds RDF applications using the axioms of RDF and then replaces any remaining RDF applications with UF.
- The second abstraction further replaces the literals containing UF with $\top$ 



## 10 Conclusion

- One abstraction compiles RDF to CHCs while preserving satisfiablility (but not solution).

- The other abstraction, parameerized by the depth of unfolding k, replaces RDFs by their finite unfolding. As k increases, the abstraction enables more solutions that are potentially lost the first abstraction.

The two abstractions are explored in tandem in an IC3-style algorithm. Remarkably, the algorithm is able to automatically combine learning inductive invariants over ADTs and RDFs with learning inductive lemmas of RDFs.