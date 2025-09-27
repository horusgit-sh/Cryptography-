from collections import Counter

ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cz_freq = {
    'A': 0.085, 'B': 0.020, 'C': 0.026, 'D': 0.034, 'E': 0.100,
    'F': 0.011, 'G': 0.012, 'H': 0.023, 'I': 0.065, 'J': 0.025,
    'K': 0.036, 'L': 0.055, 'M': 0.030, 'N': 0.067, 'O': 0.081,
    'P': 0.031, 'Q': 0.001, 'R': 0.047, 'S': 0.064, 'T': 0.046,
    'U': 0.033, 'V': 0.042, 'W': 0.002, 'X': 0.0015, 'Y': 0.021, 'Z': 0.019
}

def best_shift(group):
    counts, total = Counter(group), len(group)

    def score(s):
        chi2 = 0
        for i, c in enumerate(ABC):
            observed = counts.get(c, 0)
            plain_letter = ABC[(i - s) % 26]
            expected = cz_freq[plain_letter] * total
            if expected > 0:
                chi2 += (observed - expected) ** 2 / expected
        return chi2

    return min(range(26), key=score)

def main(text, key_len=3):
    text = text.upper()
    shifts = [best_shift(text[i::key_len]) for i in range(key_len)]
    key = ''.join(ABC[s] for s in shifts)
    k = [ABC.index(ch) for ch in key]
    out, j = [], 0
    for c in text:
        if c in ABC:
            out.append(ABC[(ABC.index(c)-k[j%key_len])%26].lower())
            j += 1
        else:
            out.append(c)
    return key, ''.join(out)

syfr = "dejlogmnpnnravvncvtkrsegvbcjkrkejuakwejurvenzfvippvtadpskbtepskjnrcycpjrloebskvpejcbzskbttfsbpscpvvosbbpifdkjmvyijuomblfkabpjvenraeuwolsegvbcjktfsbpscpvvosbffveeibcvoambzlkekbkvoamjcvoequijjczmekfdvkiezcvtkvttrunfttzbklmtlsygpdcfsmfujuamzjvdejlaifplclzlagbrcbmvotejdvnobsakjcbzpibvejskbtjmisfrrmnznskbtejmifzznedbpfmikjcbzmjzskfmvnzrmoqfnpnnrtvfcouoejpukfzzqocjtzdkpdhjurroayoukjhcbvfvskbtlkegseqjdvotifplclzlymscyplezmrkeujnpnzrloepdrsnpnoihaefmafdmpubpmfsomzprslrneeucvtkvsegvbcjkpoamscypllnotjvploeoejuoajvcbdrdejleifplclzlytfsbpjvaedfskszejmypsgpdrsskwidltvsagpdcfebpnfnitlytisfdirmnzdhrqocjtzdkpdhzodzlakprlkabpjvidgoafcymbtvmezodvylzesbfhfsoqwoafieeeotvfcouztztkldizodvysmpbfeyzotvsnvuufecvozlsygbtijkmzsfdeipzmjnluydttruudtvvuavloepmzdkpqaksiumejwekpvvcaelyupsbvpzoyksitftzkeuoaefjsphruszdhjuakvsmftrtnvkvptszniwjnrocejmzqrzkmpwpfsomoaejsajnpnijuakzmrwecnidblpqoujlfcymbtvmzzkitjcyqouqrrieddhleoszvplaqvjvueqqodfrefnzakfvnvsomoojumvaiefjsphruszniroeadhlesznifcymbtvmirsecbtzwnvwymbzvoegseipzuflfwaejbfiakttmjnrqrzdpfqucbczniibnvaadfskoaepskjjvelfvhfeosfnzakrbpfepivmvsedwyjqeczcyaedjvzodvyuvlocpgzdkvttfqyafcvtkfppiptzoebueizmajnpnvptpvmydaedjmdfnjjmvlocpgzdkpndcvzejkvncvtkfteumolioupbvsaujmvaigbtebckoeaceqqetoeatitizvniebsmftv"
k, plain = main(syfr, 3)
print("Klic:", k)
print("Text:", plain)