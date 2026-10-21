# INF605 Final Project — Group 10: Canny Edge Detector

Our own Python implementation of

> J. Canny, "A computational approach to edge detection," *IEEE Trans. Pattern Anal. Mach. Intell.*, vol. PAMI-8, no. 6, pp. 679–698, 1986. doi: [10.1109/TPAMI.1986.4767851](https://doi.org/10.1109/TPAMI.1986.4767851)

## What we implement

1. Gaussian smoothing
2. Gradient magnitude and direction
3. Non-maximum suppression
4. Hysteresis thresholding (double threshold + edge tracking)

The presentation also covers the paper's three criteria (good detection, good localization, single response) without the derivations.

**Library rule:** the method is written by us. `cv2.Canny` is used **only** to compare results. General tools (NumPy, SciPy, Matplotlib, image I/O, color conversion, general convolution such as `cv2.filter2D`) are allowed.

## Repository layout

| Path | Content |
|---|---|
| `notebooks/` | Final Jupyter notebook (must run top to bottom without errors) |
| `images/` | Test images (standard test images + our own) |
| `requirements.txt` | Python packages we use |

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows  (macOS/Linux: source .venv/bin/activate)
pip install -r requirements.txt
jupyter notebook
```

## Members

| # | Name | GitHub |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |

Every member commits their own work from their own GitHub account.

## Milestones

| Week | Milestone |
|---|---|
| 6 | Sign-up, repository (deadline 25.10.2026) |
| 10 | Progress check report (images load, first step runs) |
| 13 | Presentation (theory, 8 min + 2 min questions) |
| 14 | Final notebook, report and live demo |

## Sources and AI use

List every source used besides the paper, and every AI tool with the parts it helped with and the prompts given (also required in the final report).
