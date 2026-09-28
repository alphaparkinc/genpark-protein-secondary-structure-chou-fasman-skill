"""Chou-Fasman Protein Secondary Structure Predictor.
100% Python Standard Library.
"""

class ChouFasmanPredictor:
    """Predicts alpha-helix, beta-sheet, and random coil propensities."""
    P_alpha = {
        'E': 1.51, 'M': 1.45, 'A': 1.42, 'L': 1.21, 'K': 1.16, 'F': 1.13, 'Q': 1.11,
        'W': 1.08, 'I': 1.08, 'V': 1.06, 'D': 1.01, 'H': 1.00, 'R': 0.98, 'T': 0.83,
        'S': 0.77, 'C': 0.70, 'Y': 0.69, 'N': 0.67, 'P': 0.57, 'G': 0.57
    }
    P_beta = {
        'M': 1.67, 'V': 1.70, 'I': 1.60, 'C': 1.19, 'Y': 1.47, 'F': 1.38, 'Q': 1.10,
        'L': 1.30, 'T': 1.19, 'W': 1.37, 'A': 0.83, 'R': 0.93, 'G': 0.75, 'D': 0.54,
        'K': 0.74, 'S': 0.75, 'H': 0.87, 'N': 0.89, 'P': 0.55, 'E': 0.37
    }

    @classmethod
    def score_sequence(cls, seq):
        seq = seq.upper()
        res = []
        for aa in seq:
            pa = cls.P_alpha.get(aa, 1.0)
            pb = cls.P_beta.get(aa, 1.0)
            if pa > 1.05 and pa > pb:
                state = 'H'
            elif pb > 1.05 and pb > pa:
                state = 'E'
            else:
                state = 'C'
            res.append((aa, pa, pb, state))
        prediction = "".join(r[3] for r in res)
        return {"sequence": seq, "prediction": prediction, "details": res}
