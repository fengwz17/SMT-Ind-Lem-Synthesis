# Lemma Synthesis for Automating Induction over ADT

## 4 Lemma Synthesis

- Rewrite
- Generalize
- EnumerateLemmas

### 4.1 Lemma Synthesis by Generalization

Given a formula $\varphi$, outputs a lemma candidate $\psi$.

- gathering common subterms in $\varphi$.
- replaces occurrences of subterms by fresh variables and universally quantifies them.

### 4.2 SyGus-based Lemma Synthesis

**Outer loop**: Picks a term which occurs in some failure, and use its parse tree to extract function and predicate symbols to construct a formal grammar.

**Inner loop**: The grammar is then used to generate the desired candidate lemmas automatically.

### 4.3 Automatic Construction of Grammars

**Templates**

- $\varphi = \langle ??? \rangle + \langle ??? \rangle$ ...........(4.1)
- $\varphi = \langle ??? \rangle$ ...........(4.2)
- $\langle ??? \rangle = \langle ??? \rangle$ .............(4.3)

After choosing one of these templates, the algorithm defines the rules for nonterminals $\langle ??? \rangle$, based on the variables, UFs, and predicates occurring in $\varphi$.

two higher-level templates, commutativity and associativity of certain UFs.

- $\langle ??? \rangle (a, b) = \langle ??? \rangle (b, a)$ ................(4.4)
- $\langle ??? \rangle (a, \langle ??? \rangle (b, c)) = \langle ??? \rangle (\langle ??? \rangle (a, b), c)$ ..............(4.5)

**Example**
Goal: prove that length of queue increases by 1 after *qpush*
$\forall l_1, l_2. qlen(qpush(queue(l_1, l_2), n)) = 1 + qlen(queue(l_1, l_2))$ ........(3.6)

Performs several rewriting steps of applying function definitions, then the base case of induction on variable $l_1$ leads to:

$\forall l_2, n. 1 + len(l_2) = len(concat(rev(l_2), cons(n, nil)))$ .........(3.7)

This formula constitutes a failure, try to apply generalization by lemmas.

- choose 4.1, and let $\varphi = len(concat(rev(l_2), cons(n, nil)))$ (the larger and more complex expression).
- automatically extracts grammars from $\varphi$.

**Genaralized $\varphi$:**

Replace function applications by fresh variables

$\forall l_3, l_4. \langle ??? \rangle + \langle ??? \rangle = len(concat(l_3, l_4))$ ...........(3.8)

The generalized $\varphi$ gives rise to the following grammar (4.7):

$\langle \textbf{int-term} \rangle ::= len(\langle \textbf{list-term} \rangle) \\
 \langle \textbf{list-term} ::= l_3 | l_4 | concat(\langle \textbf{list-term} \rangle, \langle \textbf{list-term} \rangle) .............(4.7)$ 

Finally the resulting production rules are embedded into the chosen template to generate a complete grammar, where $\langle ??? \rangle$ is instantiated by $\langle \textbf{int-term} \rangle$.

### Producing Terms from Grammar

First, checks the generated formula for *non-triviality*: there should be no application of a function on only base constructors of an ADT.

Second, a generated lemma candidate should cover as many variables occuring in templates (4.1)-(4.3) as possible.

### Filtering by Refutation

Given a candidate lemma, the algorithm instantiates quantified variables with concrete values, creates quantifier-free expressions, and repeated simplifies them by applying assumptions.