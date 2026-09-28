# Chou-Fasman Protein Secondary Structure Predictor Skill

Conformational parameter-based heuristic algorithm for classifying amino acid segments into alpha-helices, beta-sheets, or random coils.

```mermaid
flowchart LR
    Residue["Residue Sequence (e.g. MKAAVVD)"] --> Propensities["P(α) & P(β) Conformational Propensities"]
    Propensities --> Segment["Windowed Statistical Evaluation"]
    Segment --> Classify["Classify State: H (Helix), E (Sheet), C (Coil)"]
```

## Features
- **100% Python Standard Library**: Canonical statistical tables.
- **Fast Sequence Scanning**: Linear-time scanning across peptide chains.
- **Rich Output Details**: Full numerical propensities per residue.
