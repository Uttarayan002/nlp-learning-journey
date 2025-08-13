## **Attention Mechanism – Roadmap**

**Stage: From single-head to full Transformer block**

**1. Why Attention? (Intuition & Motivation)**

* *What problem it solves*: Capturing relationships between tokens regardless of distance.
* *Compare*: RNN limitations, CNN limitations.
* *Analogy*: Weighted focus on relevant words.


**2. Single-Head Scaled Dot-Product Attention**

* **Inputs**: Queries (Q), Keys (K), Values (V)
* **Math flow**:

  1. Similarity scores = $QK^\top$
  2. Scale by $\sqrt{d_k}$
  3. Softmax to get attention weights
  4. Weighted sum with V
* **Visual**: Heatmap of attention weights between tokens.

**3. Multi-Head Attention (MHA)**

* **Why multiple heads**: Learn different relation patterns in parallel.
* **Steps**:

  1. Linear projections for each head
  2. Run scaled dot-product attention for each head
  3. Concatenate & project
* **Visual**: Multiple heatmaps → stacked → merged.


**4. Types of Attention**

* **Self-Attention**: Q, K, V from same sequence.
* **Cross-Attention**: Q from decoder, K/V from encoder.
* **Masked Self-Attention**: Hide future tokens (decoder).


**5. Implementation Tricks & Variations**

* Masking mechanics
* Padding handling
* Efficient attention (sparse, linear)
* Head dropout


**6. Visualization & Interpretation**

* Token-to-token heatmaps
* Head specialization examples (syntax, coreference)
* How attention evolves across layers


**7. Integration in Transformer Block**

* MHA → Add & Norm → Feedforward → Add & Norm
* Where attention sits in encoder & decoder

Do you want me to make that visual now?


