import math


def _rgb(color):
    return tuple(int(color[i:i + 2], 16) for i in (1, 3, 5))


def _luminance(rgb):
    channels = []
    for byte in rgb:
        value = byte / 255.0
        channels.append(
            value / 12.92
            if value <= 0.04045
            else ((value + 0.055) / 1.055) ** 2.4
        )
    return math.fsum(
        weight * value
        for weight, value in zip((0.2126, 0.7152, 0.0722), channels)
    )


def ink(background, preferred, allowed):
    background_luminance = _luminance(_rgb(background))
    preferred_rgb = _rgb(preferred)
    best = None
    best_distance = None

    for candidate in allowed:
        candidate_rgb = _rgb(candidate)
        candidate_luminance = _luminance(candidate_rgb)
        light = max(background_luminance, candidate_luminance)
        dark = min(background_luminance, candidate_luminance)
        if (light + 0.05) / (dark + 0.05) < 4.5:
            continue

        if candidate == preferred:
            return preferred

        distance = sum(
            (actual - target) ** 2
            for actual, target in zip(candidate_rgb, preferred_rgb)
        )
        if best_distance is None or distance < best_distance:
            best = candidate
            best_distance = distance

    return best
