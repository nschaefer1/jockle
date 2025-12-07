## Full-System Carrying Capacity Function (Medium Size)

Let $S \in \mathbb{Z}_{\ge 1}$ be the Strength score.

The carrying capacity functions

$$
(\text{Light}(S),\ \text{Medium}(S),\ \text{Heavy}(S))
$$

are defined as follows:

---

### Piece 1 — Strength ≤ 9 (table lookup)

$$
(\text{Light}(S),\ \text{Medium}(S),\ \text{Heavy}(S)) = T(S)
\qquad \text{for } S \le 9
$$

where $T(S)$ is the fixed rulebook table:

| Strength $S$ | Light | Medium | Heavy |
|--------------|--------|---------|--------|
| 1 | 3 | 6 | 10 |
| 2 | 6 | 13 | 20 |
| 3 | 10 | 20 | 30 |
| 4 | 13 | 26 | 40 |
| 5 | 16 | 33 | 50 |
| 6 | 20 | 40 | 60 |
| 7 | 23 | 46 | 70 |
| 8 | 26 | 53 | 80 |
| 9 | 30 | 60 | 90 |

Formally:

$$
T(S) = (\text{Light},\ \text{Medium},\ \text{Heavy})
$$

according to the table above.

---

### Piece 2 — Strength ≥ 10 (formula)

Define:

$$
d = S - 10, \qquad
k = \left\lfloor \frac{d}{5} \right\rfloor, \qquad
r = d \bmod 5
$$

Multiplier function:

$$
m(r) =
\begin{cases}
1.00 & r = 0 \\
1.17 & r = 1 \\
1.33 & r = 2 \\
1.50 & r = 3 \\
1.75 & r = 4 
\end{cases}
$$

Heavy load:

$$
\text{Heavy}(S)
=
\left\lfloor
100 \cdot 2^{k} \cdot m(r)
\right\rfloor
$$

Medium load:

$$
\text{Medium}(S)
=
\left\lfloor
\frac{2}{3}\,\text{Heavy}(S)
\right\rfloor
$$

Light load:

$$
\text{Light}(S)
=
\left\lfloor
\frac{1}{3}\,\text{Heavy}(S)
\right\rfloor
$$

---

### Full Combined Definition

$$
(\text{Light}(S),\ \text{Medium}(S),\ \text{Heavy}(S))
=
\begin{cases}
T(S), & S \le 9 \\
\left(
\left\lfloor \frac{1}{3}H(S) \right\rfloor,\ 
\left\lfloor \frac{2}{3}H(S) \right\rfloor,\ 
H(S)
\right), & S \ge 10
\end{cases}
$$

where

$$
H(S)
=
\left\lfloor
100 \cdot 2^{\left\lfloor (S-10)/5 \right\rfloor}
\cdot
m\!\left( (S-10) \bmod 5 \right)
\right\rfloor.
$$