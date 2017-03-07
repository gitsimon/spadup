from functools import reduce


def combine(dicts):
    d = {}
    for dict in dicts:
        for (name, fat) in dict.items():
            d[name] = fat
    return d


if __name__ == "__main__":
    legumes = {
        'bean': 0.4,
        'broccoli': 0.2,
        'nut': 0.7
    }
    fruits = {
        'apple': 0.03,
        'apricot': 0.1,
        'nut': 0.5
    }
    combined = combine([legumes, fruits])
    print(max(combined.values()))  # outputs 0.5
