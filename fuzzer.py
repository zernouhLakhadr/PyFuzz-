# fuzzer.py
import random
import string
from target import parse_input

# ── helpers ──────────────────────────────────────────────
def random_string(max_len=20):
    length = random.randint(0, max_len)
    chars  = string.printable          # includes digits, symbols, whitespace
    return ''.join(random.choice(chars) for _ in range(length))

def mutate(seed: str) -> str:
    
    if not seed:
        return random_string()
    strategy = random.choice(["flip", "insert", "delete", "duplicate", "boundary"])
    s = list(seed)
    if strategy == "flip" and s:
        i = random.randrange(len(s))
        s[i] = random.choice(string.printable)
    elif strategy == "insert":
        i = random.randrange(len(s) + 1)
        s.insert(i, random.choice(string.printable))
    elif strategy == "delete" and s:
        s.pop(random.randrange(len(s)))
    elif strategy == "duplicate":
        s = s * random.randint(2, 5)
    elif strategy == "boundary":
        return random.choice(["0", "-1", "", "   ", "!" , "9"*100, "\x00", "\n"])
    return ''.join(s)

# ── seed corpus ──────────────────────────────────────────
seeds = ["123", "hello", "42", "test", "999"]

# ── main fuzzing loop ────────────────────────────────────
def fuzz(iterations=500):
    crashes = []
    corpus  = seeds[:]

    for i in range(iterations):
        seed  = random.choice(corpus)
        case  = mutate(seed)

        try:
            result = parse_input(case)
            # If it succeeds, add to corpus for further mutation
            corpus.append(case)
        except Exception as e:
            crash = {
                "iteration" : i,
                "input"     : repr(case),
                "exception" : type(e).__name__,
                "message"   : str(e),
            }
            crashes.append(crash)
            print(f"[CRASH #{len(crashes)}] iter={i:>4}  "
                  f"input={repr(case):<25}  "
                  f"{type(e).__name__}: {e}")

    print(f"\n{'='*60}")
    print(f"Done. {len(crashes)} crashes found in {iterations} iterations.")
    return crashes

if __name__ == "__main__":
    fuzz(500)
