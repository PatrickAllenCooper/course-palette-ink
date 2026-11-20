# Palette Ink

Keep the chart designer’s first choice when it reads well. On 300 reserved swatches the original made 74 correct decisions and returned an unsafe ink 171 times. The selected code made 300 correct decisions, returned zero unsafe inks, and sent 70 swatches for manual review.

[Project guide (PDF)](docs/project-guide.pdf) · [Experiment record (PDF)](docs/experiment-record.pdf) · [Every actual prompt and reply](runs/) · [Complete scores](research/results.json)

## Try it in Cursor’s terminal

Use Python 3.11+. No network, model key or dependency installation is required.

```sh
python3 app.py white "#999999" "#999999" "#777777" "#767676" black
python3 verify.py
python3 score.py
```

The last command exits 1 if the selected implementation misses the frozen target. The verification command succeeds when the recorded measurements reproduce, including a recorded miss.

## Study design

Three fresh plain model requests and three with a shared planning note. The examples use a bounded implementation protocol and synthetic inputs. Plain successes 3/3, assisted successes 3/3. See [the frozen contract](brain/objective.md), [selection protocol](brain/protocol.md), [upstream source and license](vendor/) and [recorded model runner](research/trials.py). The `study-start` tag fixes the starting code and evaluator. A fresh Cursor replication is described in the experiment record. For a new graded study choose a harder objective and reserve fresh cases.

## Contribution

The course materials and evaluation were prepared with AI assistance. The selected implementation is a saved foundation-model response. This repository adds a teaching application to a pinned external library. The swatches are generated solid colors. RGB-byte distance is a chosen brand proxy, not a perceptual study. This result says nothing about photographs behind labels, alpha blending or overall WCAG conformance.
