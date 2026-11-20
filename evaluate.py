"""Independent WCAG ratio calculation, exact choice oracle and hard safety guards."""
import random


def channels(color):
    return bytes.fromhex(color[1:])


def luminance(color):
    rgb = [v/255 for v in channels(color)]
    linear = [v/12.92 if v<=0.04045 else ((v+0.055)/1.055)**2.4 for v in rgb]
    return sum(w*v for w,v in zip((0.2126,0.7152,0.0722), linear))


def score(policy, seed, batches):
    rng = random.Random(seed)
    total = correct = unsafe = needless = reviews = 0
    def color():
        return "#" + rng.randbytes(3).hex()
    for i in range(batches):
        bg, pref = color(), color()
        allowed = [color() for _ in range(5)]
        if i%3: allowed.append(pref)
        if i%4: allowed.extend(["#ffffff", "#000000"])
        if i%9==0: allowed = [bg]
        def qualifies(c):
            a,b=sorted((luminance(bg),luminance(c)))
            return (b+0.05)/(a+0.05)>=4.5
        def distance(c):
            return sum((a-b)**2 for a,b in zip(channels(pref),channels(c)))
        valid = [c for c in allowed if qualifies(c)]
        expected = min(valid, key=distance, default=None)
        got = policy(bg,pref,allowed.copy())
        total+=1
        correct+=got==expected
        unsafe+=got is not None and got not in valid
        needless+=pref in valid and got!=pref
        reviews+=got is None
    return dict(total=total,correct=correct,unsafe=unsafe,unnecessary_changes=needless,
                reviews=reviews,passed=correct>=total*0.98 and unsafe==0 and needless==0)
