# cvc5 

cvc5 is an automatic theorem prover for [Satisifiability Modulo Theories (SMT)](http://en.wikipedia.org/wiki/Satisfiability_Modulo_Theories) (for a more formal introduction to SMT see the following book chapter [Satisfiability Modulo Theories](https://cs.stanford.edu/~barrett/pubs/BSST09.pdf)). Technically, it is an automated validity checker for a many-sorted (i.e., typed) first-order logic with built-in theories.
It can be used to prove the validity (or, dually, the satisfiability) of a formula with respect to several built-in logical theories and their combination.

## Web site

For more information and the latest news about cvc5, visit the [cvc5 web site](https://cvc5.github.io).


## Architecture

See the [cvc5 system description](http://dx.doi.org/10.1007/978-3-030-99524-9_24) at TACAS 2022.

- **Arithmetic**

  - cvc5 solves linear real arithmetic using an implementation of [Simplex for DPLL(T)](http://link.springer.com/chapter/10.1007%2F11817963_11?). For a more complete introduction see the [tech report](http://yices.csl.sri.com/sri-csl-06-01.pdf).

  - The linear arithmetic module includes heuristics from [Section 2.5 of Alberto Griggio's thesis](http://eprints-phd.biblio.unitn.it/166/2/thesis.pdf) and a few currently unpublished ones.
  - Integers are currently handled by first solving the real relaxation of the constraints, and then using a combination of [Cuts from Proofs](http://www.cs.wm.edu/~idillig/cav2009.pdf) and branching to ensure integer solutions.  This approach and the equational solver  used are described in [A Practical Approach to Satisfiability Modulo Linear Integer Arithmetic](https://es.fbk.eu/people/griggio/papers/jsat12.pdf).
  - A technical report is planned to explain a number of small details and extensions including analysis to improve simplex's conflicts, handling disequalities, supporting model generation in cvc5's combination framework, heuristically propagating equalities over sharing terms, tableau row based propagation, and terminating simplex with unknown.
  - Non-linear arithmetic is solved by [incremental linearization](https://dl.acm.org/doi/10.1145/3230639) or [cylindrical algebraic coverings](https://www.sciencedirect.com/science/article/pii/S2352220820301188). Additional subsolvers for transcendental functions and other extended operators (IAND and pow2) are integrated as well.

- **Arrays**
  - Arrays are implemented in a manner inspired by the [Generalized, efficient array decision procedures](http://research.microsoft.com/en-us/um/people/leonardo/files/fmcad09.pdf) paper with a few major modifications.
   
- **Bitvectors**
  - Bitvectors is implemented primarily via a lazy schema for bitblasting. See [Anders Franzen's thesis chapter 3](http://eprints-phd.biblio.unitn.it/345/).

- **Combination**
  - Theory combination is based on the care graph framework described in both [Being careful about theory combination](http://cs.nyu.edu/~dejan/papers/jovanovic-fmsd2012.pdf) and [Sharing is Caring: Combination of Theories](http://cs.nyu.edu/~dejan/papers/jovanovic-frocos2011.pdf).

- [**Datatypes**](https://cvc4.github.io/datatypes)
  - cvc5 implements [An Abstract Decision Procedure for a Theory of Inductive Data Types](http://homepage.cs.uiowa.edu/~tinelli/papers/BarST-JSAT-07.pdf).
  - This procedure has been extended to incorporate [coinductive datatypes](http://homepage.cs.uiowa.edu/~ajreynol/cade15.pdf).
  - The datatypes decision procedure is optimized via the use of [shared selectors](http://cs.uiowa.edu/~ajreynol/ijcar18.pdf).

- **Quantifiers**
  - E-matching and conflict-based quantifier instantiation [http://homepage.cs.uiowa.edu/~ajreynol/fmcad14.pdf].
  - Finite model finding [http://homepage.cs.uiowa.edu/~ajreynol/thesis.pdf].
  - Techniques for finding counterexamples for conjectures in the presence of recursive functions [http://homepage.cs.uiowa.edu/~ajreynol/ijcar16a.pdf].
  - Automated induction for datatypes [http://homepage.cs.uiowa.edu/~ajreynol/vmcai15.pdf].
  - A decision procedure for quantified linear arithmetic with one alternation [http://homepage.cs.uiowa.edu/~ajreynol/report-inst-la15.pdf].
  - Support for syntax-guided synthesis, as described in [http://homepage.cs.uiowa.edu/~ajreynol/cav15a.pdf].
   
- **SAT Solver**
  - The main sat solver is based on [minisat v2.2.0](http://minisat.se/).
  - Additionally, we (optionally, and enabled by default for certain theories) use non-clausal analysis to cut down search space of minisat. For more details see the article [A branching heuristic in CVC4](http://cs.nyu.edu/~kshitij/articles/cvc4-branching-heuristic.pdf).

- **Separation Logic**
  - A decision procedure for a fragment quantifier-free separation logic containing negation, separation star and magic wand is implemented and can be composed with other decision procedures supported by cvc5.  For details see [A Decision Procedure for Separation Logic in SMT](http://homepage.divms.uiowa.edu/~ajreynol/atva16.pdf).

- **Sets**
  - Adaptation of tableau-based decision procedure described [here](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.10.5176).

- **Strings**
  - Original approach described in our [CAV 2014 paper: A DPLL(T) Theory Solver for a Theory of Strings and Regular Expressions](http://www.cs.stanford.edu/~barrett/pubs/LRT+14.pdf).
  - Decision procedure for regular memberships with length [http://homepage.cs.uiowa.edu/~ajreynol/frocos15.pdf].
   
- **Uninterpreted functions**
  - UF (without cardinality) is handled in a manner inspired by [Simplify's tech report](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.70.1745).
  - UF + cardinality is described [this presentation](http://www.divms.uiowa.edu/~ajreynol/pres-fmf12.pdf) and is used for finite model finding.
