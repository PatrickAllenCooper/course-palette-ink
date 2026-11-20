# Palette Ink
> Keep the chart designer’s first choice when it reads well.
## Shop for the project
Look at a dashboard with an accessible light theme and a newly added dark theme. A designer wants the same color vocabulary, but a label can disappear into its background. I chose a palette-selection utility over redesigning the entire theme because the input, permissible substitutes and review decision can all be inspected.
## Start with something people already use
webcolors 24.11.1 normalizes named colors and short hex codes. The course application starts with the preferred ink whenever available. We add a policy for choosing from the designer’s approved palette or requesting manual review. The distribution URL, exact version, digest and upstream license live in vendor/. The course application and its starting policy are new.
## Turn the tradeoff into a number
Compare every choice against independent enumeration. Count unsafe output separately so good average accuracy cannot hide an unreadable label. The 4.5 minimum applies here to ordinary text on solid sRGB backgrounds. [W3C explanation](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)
With white behind #999999, #777777 falls just below 4.5 and #767676 just above. Rounding the displayed ratio before comparing reverses the decision for a boundary color.
## Try it locally
Open the repository in Cursor. Use Python 3.11 or newer from its terminal. No package install, dataset download or model account is needed to run the example.
`python3 app.py white "#999999" "#999999" "#777777" "#767676" black`
The program returns #767676. The similar-looking #777777 misses the ratio on white. Black also passes but moves farther from the preferred gray.
## Correct swatch decisions
Original 74 · Selected 300
---
# From objective to portfolio claim
## Write the contract first
A designer wants readable ink on chart labels while retaining as much of the chosen palette as possible. Implement ink(background, preferred, allowed), taking normalized #rrggbb strings and returning one of allowed. With the sRGB relative-luminance contrast ratio at least 4.5 to 1, choose the admissible ink nearest to preferred in squared sRGB byte distance. Break ties in input order. Keep preferred if eligible and allowed. If none qualifies return None for manual review. Achieve correct choices on at least 98% of reserved swatches, with zero unsafe returns and zero unnecessary changes to eligible preferred inks. Example: on white with preferred #999999 and choices #999999, #777777, #767676, #000000, choose #767676. The public app parses color names using webcolors before calling you.
## Plan with the model
Filter the palette by measured contrast first. Among the survivors choose the smallest squared RGB-byte distance to the preferred ink, preserving input order for ties. A black-or-white shortcut could pass many contrast checks while violating the designer’s choice. A second design you could investigate follows.
Change each background color until the original ink is readable. That solves a different design brief and may change brand semantics. Ask which element the designer owns before giving the agent edit rights.
## Hand off one decision
In a clean copy of the starting policy, use Cursor Plan to name the edge case that could make a plausible patch fail. Save its reasoning as a short plan. Give a fresh Agent chat the objective, approved plan, editable function and a stopping budget. The experiment record links the exact inputs used here.
## Inspect the evidence
On 300 reserved swatches the original made 74 correct decisions and returned an unsafe ink 171 times. The selected code made 300 correct decisions, returned zero unsafe inks, and sent 70 swatches for manual review. Plain runs passed 3/3, and plan-assisted runs passed 3/3. The unchanged application policy and the plain model are two different baselines.
`python3 verify.py` reproduces the saved outcomes. `python3 score.py` evaluates the selected candidate and exits 1 if it misses the target.
## Where the claim ends
The swatches are generated solid colors. RGB-byte distance is a chosen brand proxy, not a perceptual study. This result says nothing about photographs behind labels, alpha blending or overall WCAG conformance. Try a real design system with approved tokens and gradients. Ask a designer to rate substitutes, then freeze the rating rule on different themes before a new comparison.
~ [Repository, source code and second PDF](https://github.com/PatrickAllenCooper/course-palette-ink)   |   [Machine-readable results](https://github.com/PatrickAllenCooper/course-palette-ink/blob/main/research/results.json)
