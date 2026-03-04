# Cryptanalysis Investigation: Search Space & Heuristics

This repository documents a comprehensive cryptanalysis of five distinct ciphertexts. The investigation pivoted from manual frequency analysis to a high-level strategic approach: **analyzing mathematical search space complexity** and utilizing **AI-assisted tool building** to navigate it.

## 📂 [View the Investigation Notebook](./cyrptanalysis_story_v1.ipynb)

---

## 🔬 The Strategy: Search Space vs. Effort

The core methodology was defined by the total key space $K$ of each cipher. By leveraging AI to scaffold complex solvers, the coding effort was neutralized, leaving the mathematical limits of the search space as the only true constraint.

### 1. Exhaustive Search (Brute Force)
For ciphers with a relatively small $K$, I utilized optimized scripts to iterate through the entire key space.

* **Hill Cipher ($2 \times 2$):** With $26^4 = 456,976$ total possibilities, the space was reduced further to invertible matrices modulo 26:
    $$\text{Key Space } |K| \approx 157,248$$
* **Columnar Transposition:** With key lengths restricted to $8 \le L \le 10$, the maximum search space was 4,032,000



### 2. Heuristic Optimization
For ciphers where $|K|$ exceeds $10^{20}$, brute force is physically impossible. 

* **Monoalphabetic Substitution:** The search space is defined by $26!$:
    $$26! \approx 4.03 \times 10^{26}$$
* **The Approach:** I initially attempted a "Skeleton" attack by fixing the top 9 English letters (representing $\approx 75\%$ of the language) and brute-forcing the remaining positions. When this failed to provide enough context, I implemented **Simulated Annealing** to escape the **Local Maxima** encountered during standard Hill Climbing.



---

## 📈 Technical Highlights
* **Fitness Functions:** Built scoring engines based on English quadgram log-probabilities and Index of Coincidence.
* **Annealing Schedules:** Developed a custom cooling schedule to ensure global convergence on the $26!$ search space.
* **60% Success Rate:** Successfully recovered the plaintext for three of the five targeted communications.

---
