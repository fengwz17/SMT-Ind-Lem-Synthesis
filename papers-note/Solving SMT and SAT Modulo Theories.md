# Solving SAT and SAT Modulo Theories: From an Abstract Davis-Putnam-Logemann-Loveland Procedure to DPLL(T)

## Abstract DPLL in the Propositional Case

### The Classical DPLL Procedure.

Transition system Cl consisting of the following five transition rules.

- UnitPropagate
- PureLiteral
- Decide
- Fail
- Backtrack

### 2.4 Modern DPLL Procedures.

引入backjumping.

- Such entailed clauses are called *backjump clauses* if their presence would have allowed a unit propagation at an **earlier** decision level.

Conflict-driven learing

- Most modern DPLL implementations make additional use of backjump clauses: they

### 3.2 An Informal Presentation of SMT Proceducers

#### 3.2.1 Eager SMT Techniques

#### 3.2.2 Lazy SMT Techniques


