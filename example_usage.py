"""Example demonstrating Chou-Fasman secondary structure prediction."""
from client import ChouFasmanPredictor

def main():
    seq = "MKAAVVD"
    res = ChouFasmanPredictor.score_sequence(seq)
    print("Sequence:", res["sequence"])
    print("Secondary Structure (H=Helix, E=Sheet, C=Coil):", res["prediction"])

if __name__ == "__main__":
    main()
