# 🔒 Cryptography Writeup: `Riverst Shamir Adleman`

**Kategori:** Cryptography
**Poeng:** 230

Du har snappet opp en kryptert melding sendt til Raymond, som bruker RSA. Men noe virker svakt med tallene hans...

RSA (Rivest-Shamir-Adleman) er en asymmetrisk kryptografialgoritme som bygger på matematikken bak store primtall og modulus-operasjoner. I dette tilfellet har Raymond brukt svake primtall, noe som gjør det mulig å knekke meldingen.

## 📉 RSA-formler og bakgrunn

**Nøkkelgenerering:**

* Velg to primtall: $p$ og $q$
* Regn ut $n = p \cdot q$
* Regn ut Euler's totient: $\varphi(n) = (p - 1)(q - 1)$
* Velg en offentlig eksponent $e$, slik at $1 < e < \varphi(n)$ og $gcd(e, \varphi(n)) = 1$
* Beregn den private eksponenten $d$ slik at $d \cdot e \equiv 1 \mod \varphi(n)$

**Kryptering:**
$C = M^e \mod n$

**Dekryptering:**
$M = C^d \mod n$

---

## 📍 1. Oppgavetekst og data

![Oppgavevisning](RSA.png)

Vi får:

```
e = 19
n = 9797
C = 6060
```

Målet er å dekryptere `C` til `M`, og sende inn flagget i formatet: `NITO{M}`.

---

## 🔍 2. Bryt n ved faktorisering

n = 9797 ser lite ut. Vi prøver å faktorisere det for å finne p og q:

```python
from sympy import factorint
print(factorint(9797))

e = 19
n = 9797
c = 6060
```

Resultat:

```
{97: 1, 101: 1}
```

Altså: `p = 97`, `q = 101`

---

## ⚖️ 3. Finn φ(n) og d

```python
from sympy import mod_inverse

phi = (97 - 1) * (101 - 1)
d = mod_inverse(e, phi)
print(d)
```

Output:

```
d = 7579
```

---

## 🛠️ 4. Dekrypter meldingen

```python
c = 6060
m = pow(c, d, n)
print(m)
```

Output:

```
M = 9292
```

---

## ✅ Flagget

**NITO{9292}**

Oppgaven viser svakheter i RSA dersom n er lite og lett å faktorisere.

---
