"""Select readable chart-label ink from an allowed palette."""


def _rgb(color):
    return tuple(int(color[i:i + 2], 16) for i in (1, 3, 5))


def _luminance(rgb):
    linear = []
    for byte in rgb:
        channel = byte / 255.0
        linear.append(
            channel / 12.92
            if channel <= 0.04045
            else ((channel + 0.055) / 1.055) ** 2.4
        )
    return (
        0.2126 * linear[0]
        + 0.7152 * linear[1]
        + 0.0722 * linear[2]
    )


def ink(background, preferred, allowed):
    """Return the closest allowed ink with contrast >= 4.5, or None."""
    background_luminance = _luminance(_rgb(background))
    preferred_rgb = _rgb(preferred)
    best = None
    best_distance = None

    for candidate in allowed:
        candidate_rgb = _rgb(candidate)
        candidate_luminance = _luminance(candidate_rgb)
        contrast = (
            (max(background_luminance, candidate_luminance) + 0.05)
            / (min(background_luminance, candidate_luminance) + 0.05)
        )
        if contrast < 4.5:
            continue

        if candidate == preferred:
            return preferred

        distance = sum(
            (channel - target) ** 2
            for channel, target in zip(candidate_rgb, preferred_rgb)
        )
        if best_distance is None or distance < best_distance:
            best = candidate
            best_distance = distance

    return best
