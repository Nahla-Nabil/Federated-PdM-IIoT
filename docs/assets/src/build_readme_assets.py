"""Builds the README graphics in docs/assets/.

Result values are transcribed from the published paper (IEEE Xplore 11430844):
Table I (centralized vs federated), Table II (algorithms), Table III (scalability).
They match the outputs saved in iiot-federated-pdm.ipynb. Standard library only.

    python docs/assets/src/build_readme_assets.py
"""
from svg_style import *  # noqa: F401,F403  (design tokens, primitives, icons, banner/publication/author)

# ---------------------------------------------------------------- published values
TABLE_I = [("Accuracy", 0.9496, 0.9513), ("Precision", 0.9522, 0.9539), ("Recall", 0.9496, 0.9513),
           ("F1-score", 0.9496, 0.9513), ("AUC-ROC", 0.9957, 0.9945)]          # (metric, centralized, federated)
TABLE_II = [("Random Forest", 0.9513, 0.55), ("Gradient Boosting", 0.9513, 7.49),
            ("Decision Tree", 0.9391, 0.01), ("SVM (RBF)", 0.9200, 0.17)]       # (algorithm, accuracy, training s)
TABLE_III = [(2, 0.9504, 0.0009), (4, 0.9483, 0.0014), (8, 0.9335, 0.0056), (16, 0.9158, 0.0136)]
SRC = "Source: published paper (IEEE Xplore 11430844); values match the saved notebook outputs."


def overview():
    W, H = 1200, 380
    b = [t(48, 62, "Research at a glance", 30, TEXT, 700)]
    cols = [("Problem", ["Centralized PdM pools", "sensitive plant data;", "sites differ (Non-IID)"], shield),
            ("Approach", ["Edge Random Forests,", "cloud aggregation,", "SHAP explanations"], gear),
            ("Data", ["CWRU bearings: 2,300", "feature windows,", "10 fault classes"], bars_icon),
            ("Evaluation", ["Non-IID clients, four", "algorithms, 2–16", "clients, SHAP"], magnifier),
            ("Next", ["Multi-site data, edge", "hardware, FedProx,", "privacy analysis"], chip)]
    cw = 206
    for i, (h, lines_, icon) in enumerate(cols):
        x = 48 + i * (cw + 18)
        b.append(r(x, 96, cw, 248, 18, PANEL, STROKE, 1.2))
        b.append(f'<circle cx="{x+44}" cy="146" r="28" fill="{PANEL2}" stroke="{CYAN}" stroke-width="1.5"/>')
        b.append({gear: lambda: gear(x + 44, 146, 15, CYAN, sw=1.8), chip: lambda: chip(x + 44, 146, 11),
                  bars_icon: lambda: bars_icon(x + 44, 142, 0.7), magnifier: lambda: magnifier(x + 46, 148, 0.8),
                  shield: lambda: shield(x + 44, 148, 0.8)}[icon]())
        b.append(t(x + 22, 212, h, 21, CYAN, 700))
        for j, s in enumerate(lines_):
            b.append(t(x + 20, 246 + j * 26, s, 14.5, TEXT))
        if i < 4: b.append(line(x + cw + 3, 220, x + cw + 15, 220, CYAN, 2, marker="ac"))
    return svg(W, H, "\n".join(b), "Research at a glance", "Problem, approach, data, evaluation and next steps of the research.")


def architecture():
    W, H = 1200, 720
    b = [t(48, 62, "Hybrid edge–cloud architecture", 30, TEXT, 700),
         t(48, 94, "Conceptual design as described in the paper (Sec. III-D, Fig. 3). Clients are simulated partitions of the CWRU data.", 16, TEXT2)]
    b.append(r(48, 124, 1104, 230, 20, PANEL, STROKE, 1.2))
    b.append(t(72, 160, "CLOUD", 16, CYAN, 700, ls=3))
    boxes = [(96, "FedAvg aggregation", "w = Σₖ (nₖ/N) · wₖ", "Eq. (2) in the paper"),
             (436, "Global model", "evaluated on the 575-sample", "held-out test set"),
             (776, "Explainability", "SHAP on the global model", "feature importance ranking")]
    for i, (x, title, l1, l2) in enumerate(boxes):
        b.append(r(x, 184, 300, 146, 16, PANEL2, CYAN if i == 0 else STROKE, 1.5))
        b.append([cloud(x + 50, 232, 0.55, PANEL, CYAN, 2), gear(x + 48, 230, 20, CYAN, sw=2), bars_icon(x + 44, 224, 0.9) + magnifier(x + 82, 232, 0.7)][i])
        b.append(t(x + (96 if i == 0 else 100 if i == 1 else 112), 236, title, 19, TEXT, 700))
        b.append(t(x + 24, 284, l1, 16, TEXT, 500, family=MONO if i == 0 else FONT))
        b.append(t(x + 24, 310, l2, 14.5, MUTED))
        if i < 2: b.append(line(x + 306, 257, x + 334, 257, CYAN, 2.5, marker="ac"))
    xs = [192, 464, 736, 1008]
    for x in xs: b.append(line(x, 450, x, 364, CYAN, 2.2, dash="3 8", marker="ac"))
    b.append(r(272, 380, 656, 32, 16, BG, STROKE, 1.2))
    b.append(t(600, 402, "described: local model parameters + sample count nₖ — raw data stays at the edge", 15.5, CYAN, 600, "middle"))
    b.append(r(48, 428, 1104, 262, 20, PANEL, STROKE, 1.2))
    b.append(t(72, 464, "EDGE", 16, CYAN, 700, ls=3))
    for i, x in enumerate(xs):
        bx = x - 120
        b.append(r(bx, 482, 240, 190, 16, PANEL2, STROKE, 1.3))
        b.append(t(x, 514, f"Client {i+1}", 19, TEXT, 700, "middle"))
        b.append(db(bx + 46, 560, 0.8)); b.append(t(bx + 80, 556, "local features", 15, TEXT)); b.append(t(bx + 80, 576, "Dirichlet α = 0.5", 13.5, MUTED))
        b.append(line(x, 600, x, 614, MUTED, 1.8, marker="am"))
        b.append(r(bx + 16, 620, 208, 44, 10, PANEL, CYAN, 1.2))
        b.append(t(x, 640, "Random Forest", 15.5, TEXT, 600, "middle")); b.append(t(x, 658, "80 trees · depth 10", 13.5, MUTED, 400, "middle"))
    return svg(W, H, "\n".join(b), "Hybrid edge–cloud architecture as described in the paper",
               "Four Non-IID edge clients train Random Forests (80 trees, depth 10). As described in the paper, clients send model parameters and sample counts to the cloud, which aggregates them with FedAvg (Eq. 2); the global model is evaluated on a 575-sample test set and explained with SHAP. Conceptual illustration.")


def workflow():
    W, H = 1200, 470
    b = [t(48, 62, "Experimental workflow", 30, TEXT, 700),
         t(48, 94, "Cell order in iiot-federated-pdm.ipynb. The dashed step happens upstream, in the public dataset.", 17, TEXT2)]
    steps = [("0", "Feature extraction", "by dataset provider", True), ("1", "Load CWRU features", "2,300 × 9 · 10 classes", False),
             ("2", "Encode & scale", "labels 0–9 · z-score", False), ("3", "Stratified split", "1,725 train · 575 test", False),
             ("4", "Centralized baseline", "RF 150 trees · depth 12", False), ("5", "Edge clients", "Dirichlet α = 0.5 · RF 80", False),
             ("6", "Cloud aggregation", "global model", False), ("7", "Evaluate + explain", "metrics · ROC · SHAP", False)]
    bw, bh, gap = 240, 112, 48
    for i, (n, a, s, up) in enumerate(steps):
        row, col = divmod(i, 4)
        if row == 1: col = 3 - col
        x, y = 48 + col * (bw + gap), 132 + row * (bh + 74)
        b.append(r(x, y, bw, bh, 16, PANEL if not up else BG, STROKE, 1.4, dash="6 6" if up else None))
        b.append(f'<circle cx="{x+34}" cy="{y+38}" r="17" fill="{CYAN if not up else "none"}" stroke="{CYAN}" stroke-width="1.5"/>')
        b.append(t(x + 34, y + 44, n, 16, BG0 if not up else CYAN, 700, "middle"))
        b.append(t(x + 62, y + 45, a, 17.5, TEXT, 700)); b.append(t(x + 22, y + 86, s, 15.5, TEXT2))
        if i in (0, 1, 2): b.append(line(x + bw + 6, y + bh / 2, x + bw + 40, y + bh / 2, CYAN, 2.4, marker="ac"))
        if i in (4, 5, 6): b.append(line(x - 6, y + bh / 2, x - 40, y + bh / 2, CYAN, 2.4, marker="ac"))
        if i == 3: b.append(path(f"M{x + bw/2} {y + bh + 6} V {y + bh + 66}", stroke=CYAN, sw=2.4, marker="ac"))
    b.append(t(48, 450, "Further cells: algorithm comparison, scalability, statistical test, figures, saved models and CSV files.", 15, MUTED, italic=True))
    return svg(W, H, "\n".join(b), "Experimental workflow",
               "Feature extraction by the dataset provider; then load features, encode and scale, stratified split, centralized baseline, Dirichlet edge clients, cloud step, evaluation and SHAP.")


def dataset():
    W, H = 1200, 400
    b = [t(48, 62, "Dataset: CWRU bearing benchmark", 30, TEXT, 700),
         t(48, 94, "Pre-extracted feature table, Kaggle brjapon/cwru-bearing-datasets · 48 kHz drive-end vibration · motor load 1 hp", 16, TEXT2)]
    stats = [("2,300", "feature windows"), ("230", "per class (balanced)"), ("10", "fault classes"), ("9", "time-domain features")]
    for i, (big, lab) in enumerate(stats):
        x = 48 + i * 180
        b.append(r(x, 124, 164, 110, 14, PANEL, STROKE, 1.2)); b.append(t(x + 20, 178, big, 38, CYAN, 700)); b.append(t(x + 20, 210, lab, 14.5, TEXT2))
    b.append(r(780, 124, 372, 110, 14, PANEL, STROKE, 1.2))
    b.append(t(800, 156, "FEATURES", 13, CYAN, 700, ls=2))
    b.append(t(800, 186, "max · min · mean · std · RMS", 15.5, TEXT)); b.append(t(800, 212, "skewness · kurtosis · crest · form", 15.5, TEXT))
    groups = [("Normal", ["Normal"]), ("Inner race", ["IR 0.007″", "IR 0.014″", "IR 0.021″"]),
              ("Outer race (6 o’clock)", ["OR 0.007″", "OR 0.014″", "OR 0.021″"]), ("Ball", ["Ball 0.007″", "Ball 0.014″", "Ball 0.021″"])]
    x = 48
    for g, items in groups:
        bw = 100 if len(items) == 1 else 94
        w = len(items) * (bw + 6) - 6
        b.append(t(x, 276, g, 15, TEXT, 700))
        for j, it in enumerate(items):
            b.append(r(x + j * (bw + 6), 290, bw, 44, 10, PANEL2, CYAN if g == "Normal" else STROKE, 1.2))
            b.append(t(x + j * (bw + 6) + bw / 2, 318, it, 14, TEXT, 600, "middle"))
        x += w + 26
    b.append(t(48, 372, "Split: stratified 75 / 25 → 1,725 training and 575 test samples (random_state = 42).", 15, MUTED))
    return svg(W, H, "\n".join(b), "CWRU dataset overview", "2,300 feature windows, 230 per class, 10 fault classes, 9 time-domain features; stratified 75/25 split.")


def results_published():
    W, H = 1200, 520
    b = [t(48, 62, "Reported results: centralized vs federated", 30, TEXT, 700),
         t(48, 94, "Paper Table I · single stratified train/test split (575 test samples)", 17, TEXT2)]
    b.append(f'<circle cx="57" cy="128" r="8" fill="{CEN}"/>' + t(72, 133, "Centralized RF (150 trees, depth 12)", 15, TEXT2))
    b.append(f'<circle cx="387" cy="128" r="8" fill="{FED}" stroke="{TEXT}" stroke-width="1.5"/>' + t(402, 133, "Federated (as reported)", 15, TEXT2))
    x0, x1, lo, hi = 260, 1100, 0.94, 1.00
    X_ = lambda v: x0 + (x1 - x0) * (v - lo) / (hi - lo)
    for v in (0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1.00):
        b.append(line(X_(v), 160, X_(v), 440, "#FFFFFF", 1, op=0.08)); b.append(t(X_(v), 464, f"{v:.2f}", 14, MUTED, 400, "middle"))
    for i, (m, c, f) in enumerate(TABLE_I):
        y = 186 + i * 56
        b.append(t(x0 - 24, y + 6, m, 17, TEXT, 600, "end"))
        b.append(line(X_(min(c, f)), y, X_(max(c, f)), y, STROKE, 3))
        b.append(f'<circle cx="{X_(c)}" cy="{y}" r="9" fill="{CEN}"/>')
        b.append(f'<circle cx="{X_(f)}" cy="{y}" r="9" fill="{FED}" stroke="{TEXT}" stroke-width="1.5"/>')
        lab_x = X_(max(c, f)) + 18
        b.append(t(lab_x, y + 6, f"{c:.4f} / {f:.4f}", 15, TEXT, 600))
    b.append(t(48, 500, "Axis starts at 0.94 to make the small differences visible. " + SRC, 14, MUTED))
    return svg(W, H, "\n".join(b), "Reported results, Table I",
               "Centralized vs reported federated: accuracy 0.9496 vs 0.9513, precision 0.9522 vs 0.9539, recall 0.9496 vs 0.9513, F1 0.9496 vs 0.9513, AUC-ROC 0.9957 vs 0.9945.")


def algorithms_published():
    W, H = 1200, 480
    b = [t(48, 62, "Algorithm benchmarking", 30, TEXT, 700),
         t(48, 94, "Paper Table II · test accuracy and training time on the same split", 17, TEXT2)]
    x0, x1 = 260, 900
    for v in (0, 25, 50, 75, 100):
        x = x0 + (x1 - x0) * v / 100
        b.append(line(x, 128, x, 410, "#FFFFFF", 1, op=0.08 if v else 0.25)); b.append(t(x, 434, f"{v}%", 14, MUTED, 400, "middle"))
    b.append(t(1060, 140, "TRAINING TIME", 13, CYAN, 700, "middle", ls=2))
    for i, (a, acc, ts) in enumerate(TABLE_II):
        y = 160 + i * 64
        b.append(t(x0 - 20, y + 28, a, 18, TEXT, 600, "end"))
        wv = (x1 - x0) * acc
        b.append(f'<path d="M{x0} {y+6} H{x0+wv-4} a4 4 0 0 1 4 4 V{y+40} a4 4 0 0 1 -4 4 H{x0} z" fill="{FED if i == 0 else CEN if i == 1 else ISO2}"/>')
        b.append(t(x0 + wv + 12, y + 32, f"{acc*100:.2f}%", 17, TEXT, 700))
        b.append(t(1060, y + 32, f"{ts:.2f} s", 18, TEXT, 600, "middle"))
    b.append(t(48, 466, SRC, 14, MUTED))
    return svg(W, H, "\n".join(b), "Algorithm benchmarking, Table II",
               "Random Forest 95.13% (0.55 s), Gradient Boosting 95.13% (7.49 s), Decision Tree 93.91% (0.01 s), SVM 92.00% (0.17 s).")


def scalability_published():
    W, H = 1200, 520
    b = [t(48, 62, "Scalability across client counts", 30, TEXT, 700),
         t(48, 94, "Paper Table III · mean accuracy and standard deviation for 2, 4, 8 and 16 clients", 17, TEXT2)]
    x0, x1, y0, y1, lo, hi = 250, 950, 420, 140, 0.90, 0.96
    X_ = lambda i: x0 + (x1 - x0) * i / 3
    Y_ = lambda v: y0 - (y0 - y1) * (v - lo) / (hi - lo)
    for v in (0.90, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96):
        b.append(line(x0, Y_(v), x1, Y_(v), "#FFFFFF", 1, op=0.08)); b.append(t(x0 - 56, Y_(v) + 5, f"{v:.2f}", 14, MUTED, 400, "end"))
    top = " ".join(f"{X_(i)},{Y_(m + s)}" for i, (_, m, s) in enumerate(TABLE_III))
    bot = " ".join(f"{X_(i)},{Y_(m - s)}" for i, (_, m, s) in reversed(list(enumerate(TABLE_III))))
    b.append(f'<polygon points="{top} {bot}" fill="{FED}" opacity="0.2"/>')
    b.append(f'<polyline points="{" ".join(f"{X_(i)},{Y_(m)}" for i, (_, m, _s) in enumerate(TABLE_III))}" fill="none" stroke="{FED}" stroke-width="3"/>')
    for i, (n, m, s) in enumerate(TABLE_III):
        b.append(f'<circle cx="{X_(i)}" cy="{Y_(m)}" r="6" fill="{FED}" stroke="{BG}" stroke-width="2"/>')
        b.append(t(X_(i), Y_(m) - 16, f"{m:.4f}", 15, TEXT, 600, "middle")); b.append(t(X_(i), y0 + 30, f"{n} clients", 15, TEXT2, 500, "middle"))
    b.append(t(48, 476, "Shaded band: ± 1 standard deviation. Clients are simulated on one machine. Axis starts at 0.90.", 14, MUTED))
    b.append(t(48, 498, SRC, 14, MUTED))
    return svg(W, H, "\n".join(b), "Scalability, Table III", "Mean accuracy 0.9504, 0.9483, 0.9335, 0.9158 for 2, 4, 8, 16 clients (std 0.0009, 0.0014, 0.0056, 0.0136).")



def highlights():
    W, H = 1200, 400
    b = [t(48, 62, "Project highlights", 30, TEXT, 700),
         t(48, 94, "Peer-reviewed research · real vibration benchmark · open implementation", 17, TEXT2)]
    cards = [("2,300", "Feature windows", "real CWRU vibration data", CYAN), ("10", "Fault classes", "Normal · Inner · Outer · Ball", CYAN),
             ("4", "Edge clients", "Non-IID, Dirichlet α = 0.5", CYAN), ("2 → 16", "Client scaling", "scalability study", CYAN),
             ("4", "ML algorithms", "RF · GB · DT · SVM", BLUE), ("SHAP", "Explainable AI", "feature-level insight", BLUE),
             ("9", "Vibration features", "time-domain statistics", BLUE), ("IEEE", "Published", "IEEE Xplore 11430844", BLUE)]
    cw, ch = 264, 124
    for i, (big, lab, sub, col) in enumerate(cards):
        x, y = 48 + (i % 4) * (cw + 20), 122 + (i // 4) * (ch + 16)
        b.append(r(x, y, cw, ch, 16, PANEL, STROKE, 1.2))
        b.append(t(x + 22, y + 50, big, 36, col, 700))
        b.append(t(x + 22, y + 82, lab, 17, TEXT, 700))
        b.append(t(x + 22, y + 106, sub, 13.5, MUTED))
    return svg(W, H, "\n".join(b), "Project highlights",
               "2,300 feature windows, 10 fault classes, 4 Non-IID edge clients, 2 to 16 client scaling, 4 algorithms, SHAP, 9 features, published on IEEE Xplore.")


def fl_concept():
    W, H = 1200, 520
    b = [t(48, 62, "Centralized vs federated learning", 30, TEXT, 700),
         t(48, 94, "Conceptual comparison of what moves across the network", 17, TEXT2)]
    for k, (x0, head, sub) in enumerate([(48, "Centralized", "raw data is pooled in one place"), (618, "Federated (this framework)", "models move, raw data stays on site")]):
        b.append(r(x0, 124, 534, 360, 20, PANEL, STROKE, 1.2))
        b.append(t(x0 + 28, 166, head, 23, TEXT if k == 0 else CYAN, 700)); b.append(t(x0 + 28, 194, sub, 16, TEXT2))
        cx = x0 + 267
        b.append(cloud(cx, 262, 1.0, PANEL2, CEN if k == 0 else CYAN))
        b.append(t(cx, 270, "train" if k == 0 else "aggregate", 15, TEXT, 600, "middle"))
        for j in range(4):
            sx = x0 + 75 + j * 128
            b.append(r(sx - 46, 380, 92, 86, 14, PANEL2, STROKE, 1.2)); b.append(motor(sx - 4, 416, 0.62))
            b.append(t(sx, 456, f"site {j+1}", 13, MUTED, 400, "middle"))
            if k == 0:
                b.append(path(f"M{sx} 376 Q {sx} 330 {cx + (sx-cx)*0.3} 296", stroke=CEN, sw=4, marker="abig", op=0.85))
                b.append(r(sx - 22, 330, 44, 16, 4, CEN, op=0.9)); b.append(t(sx, 342, "raw", 11, BG0, 700, "middle"))
            else:
                b.append(path(f"M{sx} 376 Q {sx} 330 {cx + (sx-cx)*0.3} 296", stroke=CYAN, sw=2, dash="3 7", marker="ac"))
                b.append(r(sx - 24, 326, 48, 20, 5, PANEL2, CYAN, 1.2) + gear(sx, 336, 6, CYAN, sw=1.2, teeth=6))
                b.append(lock(sx + 32, 398, 0.6, CYAN))
    b.append(t(48, 508, "Conceptual illustration. Federated learning reduces raw-data movement; it is not by itself a formal privacy guarantee.", 14.5, MUTED))
    return svg(W, H, "\n".join(b), "Centralized versus federated learning",
               "Left: sites send raw data to a central server. Right: sites train locally and send models to the cloud for aggregation.")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for name, fn in [("banner", banner), ("highlights", highlights), ("fl-concept", fl_concept), ("overview", overview), ("architecture", architecture), ("workflow", workflow),
                     ("dataset", dataset), ("results-table1", results_published), ("algorithms-table2", algorithms_published),
                     ("scalability-table3", scalability_published), ("publication", publication), ("author", author)]:
        (OUT / f"{name}.svg").write_text(fn(), encoding="utf-8"); print("wrote", f"docs/assets/{name}.svg")
