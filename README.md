# Awesome Depth Maps

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Curated monocular and metric depth estimation models, runtimes, demos, datasets, and use cases, anchored on Apple's **Depth Pro 2**.

**Monocular depth** estimates a distance for every pixel from a single ordinary photo, or from a video taken with one camera. **Metric** depth is in real units, usually meters, rather than a relative, up-to-scale map. Sharp object edges and, for video, low temporal jitter are what make a depth map usable for 3D photos, compositing, and geometry.

**Depth Pro 2** is Apple Machine Learning Research's 2026 follow-up to Depth Pro. The [technical report](https://arxiv.org/abs/2611.26603) (submitted 19 November 2026) and the [model card](https://huggingface.co/apple/DepthPro2) describe a single network that predicts full-resolution metric depth for a photo, a video, or a live feed. Official pages say it outperforms prior single-frame and multi-frame methods on sharpness (Boundary F1) and temporal consistency (jitter), averaged over the Sintel and Spring datasets. The public family has four sizes, S (24M parameters, 97 MB), B (97M, 386 MB), L (334M, 1.3 GB), and H+ (872M, 3.5 GB), plus a shared focal-length estimator (23.5M, 94 MB). Those counts are from the official card and README, not from a secondary recap.

The weights are released under the [Apple Machine Learning Research Model license](https://github.com/apple-aiml-research/ml-depth-pro-2/blob/main/LICENSE_MODEL), for research use only: non-commercial scientific research and academic development. The inference [code](https://github.com/apple-aiml-research/ml-depth-pro-2) has a separate Apple software license. The repository states that it does not include training or evaluation code. A research page at `machinelearning.apple.com/research/depth-pro-2` was not published (that URL returned 404 on 2026-11-19 PT). The [Depth Pro v1 research page](https://machinelearning.apple.com/research/depth-pro) is still up. The project page links an official Hugging Face Space that returned 401 to this checker, so it is not listed; a community Space is.

Quick start, from the official card: `pip install "git+https://github.com/apple-aiml-research/ml-depth-pro-2"`, or clone the repo and run `uv run depth-pro-2 predict -i assets/example.jpg -o out/`. On a laptop, start with `-m depthpro2-s`. Default weights are H+.

The rest of this list is the broader depth-map ecosystem: other monocular and video models, runtimes and ports, live demos, datasets, and applications. A vendor's "open source" slogan is not treated as the license.

Deduplicated by normalized URL (trailing slash, `www.`, query, and fragment stripped).

**176 unique links** · Ingested **2026-11-19 PT** · License for this compilation: [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) (linked projects keep their own licenses).

### Start here

- [Depth Pro 2 model card](https://huggingface.co/apple/DepthPro2) — Official sizes, quick start, and the research-only license.
- [Depth Pro 2 paper](https://arxiv.org/abs/2611.26603) — *Depth Pro 2: Sharp and Temporally Consistent Metric Monocular Depth*, arXiv:2611.26603.
- [ml-depth-pro-2](https://github.com/apple-aiml-research/ml-depth-pro-2) — Inference code, CLI, and the Mac / Core ML demo.
- [LICENSE_MODEL](https://github.com/apple-aiml-research/ml-depth-pro-2/blob/main/LICENSE_MODEL) — Apple ML Research Model license: research use only.
- [Depth Anything V2](https://github.com/DepthAnything/Depth-Anything-V2) — A widely used foundation model for monocular depth, Apache-2.0.
- [Use cases](#use-cases) — 3D photos, Gaussian splatting and NeRF, AR occlusion, VFX, and ControlNet.
- [Datasets and benchmarks](#datasets-and-benchmarks) — KITTI, NYUv2, Sintel, Spring, ETH3D, DIODE, and related sets.

## Contents

- [Depth Pro 2](#depth-pro-2) (13)
  - [Official release](#official-release) (5)
  - [Sizes and weights](#sizes-and-weights) (5)
  - [Ports and demos](#ports-and-demos) (3)
- [Models](#models) (77)
  - [Depth Pro v1](#depth-pro-v1) (5)
  - [Foundation and relative depth](#foundation-and-relative-depth) (20)
  - [Metric monocular](#metric-monocular) (22)
  - [Diffusion and generative](#diffusion-and-generative) (20)
  - [Geometry and point maps](#geometry-and-point-maps) (10)
- [Video and temporal depth](#video-and-temporal-depth) (16)
- [Runtimes and ports](#runtimes-and-ports) (15)
  - [Libraries and official ports](#libraries-and-official-ports) (5)
  - [ONNX, TensorRT and Core ML](#onnx-tensorrt-and-core-ml) (3)
  - [ComfyUI and creative tools](#comfyui-and-creative-tools) (4)
  - [Browser](#browser) (3)
- [Demos](#demos) (10)
- [Use cases](#use-cases) (23)
  - [3D photos and parallax](#3d-photos-and-parallax) (3)
  - [Gaussian splatting and NeRF](#gaussian-splatting-and-nerf) (10)
  - [AR occlusion](#ar-occlusion) (6)
  - [VFX and relighting](#vfx-and-relighting) (1)
  - [Depth-conditioned generation](#depth-conditioned-generation) (3)
- [Datasets and benchmarks](#datasets-and-benchmarks) (17)
- [Awesome lists and indexes](#awesome-lists-and-indexes) (5)
- [Sources](#sources)
- [Contributing](#contributing)
- [License](#license)

## Depth Pro 2

Apple ML Research's 2026 metric monocular depth family: one network for a photo, a video, or a live feed, at the input's full resolution. Weights are research-only.

### Official release

- [Depth Pro 2 model card](https://huggingface.co/apple/DepthPro2) — Apple's Hub card for Depth Pro 2: sharp, temporally consistent metric monocular depth for photos, video, and live feeds at the input's full resolution. Lists the four sizes, the shared focal estimator, the quick start, and the research-only Apple ML Research Model license (apple-amlr).
- [Depth Pro 2 project page](https://apple-aiml-research.github.io/ml-depth-pro-2/) — Official project site with image and video comparisons, the method figure, and the claim that Depth Pro 2 outperforms prior single-frame and multi-frame work on Boundary F1 sharpness and temporal jitter, averaged over Sintel and Spring.
- [ml-depth-pro-2](https://github.com/apple-aiml-research/ml-depth-pro-2) — Official inference code and CLI. Install with pip from this repo, or clone and run uv run depth-pro-2 predict. The README says the repository does not include training or evaluation code. The code license is Apple's software license; the weights are under LICENSE_MODEL.
- [Depth Pro 2 paper](https://arxiv.org/abs/2611.26603) — Hu, Mihajlovic, Duong, Lipson, Dong, Delaunoy, Richter, and Koltun, Depth Pro 2: Sharp and Temporally Consistent Metric Monocular Depth, arXiv:2611.26603, submitted 19 November 2026.
- [Apple ML Research Model license](https://github.com/apple-aiml-research/ml-depth-pro-2/blob/main/LICENSE_MODEL) — LICENSE_MODEL for the Depth Pro 2 weights. The grant is limited to Research Purposes, defined as non-commercial scientific research and academic development, and it excludes commercial product or service use.

### Sizes and weights

- [Depth Pro 2 S](https://huggingface.co/apple/DepthPro2-S) — Smallest public size: 24M parameters, 97 MB download, Hub id apple/DepthPro2-S. Official guidance is to start with S on a laptop. Same apple-amlr research-only license as the rest of the family.
- [Depth Pro 2 B](https://huggingface.co/apple/DepthPro2-B) — 97M parameters, 386 MB download, Hub id apple/DepthPro2-B. Larger sizes are described as sharper and steadier; smaller ones run faster. Research-only apple-amlr license.
- [Depth Pro 2 L](https://huggingface.co/apple/DepthPro2-L) — 334M parameters, 1.3 GB download, Hub id apple/DepthPro2-L. Research-only apple-amlr license.
- [Depth Pro 2 H+](https://huggingface.co/apple/DepthPro2-H) — Largest public size and the default in the official CLI: 872M parameters, 3.5 GB download, Hub id apple/DepthPro2-H (H+ on the card). Research-only apple-amlr license.
- [Depth Pro 2 focal estimator](https://huggingface.co/apple/DepthPro2-focal) — Shared 23.5M-parameter (94 MB) focal-length estimator, Hub id apple/DepthPro2-focal. It loads with each size and predicts focal length in pixels when the camera does not report one. Same research-only license.

### Ports and demos

- [Depth Pro 2 Core ML](https://huggingface.co/apple/DepthPro2-coreml) — Official Core ML packages for S, B, L, H+, and a field-of-view model, for Apple silicon on macOS 15 or later. The card documents w4 temporal windows, named input sizes, and that inverse depth is normalized by focal length. Research-only apple-amlr license.
- [Depth Pro 2 Mac demo](https://github.com/apple-aiml-research/ml-depth-pro-2/blob/main/demo/README.md) — Official demo README for a minimal Mac app that shows live camera depth with Core ML, including how to export a package and use it in an app. Requires Apple silicon, macOS 15 or later, and Xcode 16 or later or its command line tools.
- [Depth Pro 2 Space (akhaliq)](https://huggingface.co/spaces/akhaliq/DepthPro2) — Community Gradio Space for metric monocular depth from photos and videos. The official Space linked from the project page returned 401 to this checker and is not listed.

## Models

Downloadable monocular depth and geometry models besides Depth Pro 2. The blurb says whether a release is metric or relative, and flags a research or custom license when that is what the card or repo says.

### Depth Pro v1

- [ml-depth-pro](https://github.com/apple-aiml-research/ml-depth-pro) — Official code for Depth Pro, Apple's 2024 metric monocular depth model. The older apple/ml-depth-pro URL now redirects here.
- [Depth Pro weights](https://huggingface.co/apple/DepthPro) — Hub weights for Depth Pro v1. The Hub license field is apple-amlr, the same research-license family as Depth Pro 2.
- [Depth Pro (transformers)](https://huggingface.co/apple/DepthPro-hf) — Hub checkpoint used by the Hugging Face transformers DepthPro model. The transformers docs target this v1 line, not Depth Pro 2.
- [Depth Pro paper](https://arxiv.org/abs/2410.02073) — Bochkovskii et al., Depth Pro: Sharp Monocular Metric Depth in Less Than a Second, arXiv:2410.02073.
- [Depth Pro research page](https://machinelearning.apple.com/research/depth-pro) — Apple ML Research page for the original Depth Pro. A corresponding depth-pro-2 research page was not up (404) when this list was built.

### Foundation and relative depth

- [Depth Anything](https://github.com/LiheYoung/Depth-Anything) — Official code for Depth Anything (CVPR 2024), a foundation model for monocular depth trained with large-scale unlabeled data. Apache-2.0.
- [Depth Anything project page](https://depth-anything.github.io/) — Official project site for Depth Anything v1.
- [Depth Anything paper](https://arxiv.org/abs/2401.10891) — Yang et al., Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data, arXiv:2401.10891.
- [Depth Anything V2](https://github.com/DepthAnything/Depth-Anything-V2) — Official code for Depth Anything V2 (NeurIPS 2024), a later foundation model for monocular depth. Apache-2.0.
- [Depth Anything V2 project page](https://depth-anything-v2.github.io/) — Official project site for Depth Anything V2.
- [Depth Anything V2 paper](https://arxiv.org/abs/2406.09414) — Yang et al., Depth Anything V2, arXiv:2406.09414.
- [Depth Anything V2 Large](https://huggingface.co/depth-anything/Depth-Anything-V2-Large) — Hub weights for the large Depth Anything V2 checkpoint.
- [Depth Anything V2 collection](https://huggingface.co/collections/depth-anything/depth-anything-v2) — Official Hub collection of Depth Anything V2 checkpoints.
- [Depth Anything 3](https://github.com/ByteDance-Seed/Depth-Anything-3) — Official ByteDance Seed code for Depth Anything 3 (DA3, ICLR 2026). A plain transformer predicts spatially consistent geometry from any number of views, with or without known poses, and the authors also report monocular depth against Depth Anything V2. Apache-2.0. Trained, the repo says, exclusively on public academic datasets.
- [Depth Anything 3 project page](https://depth-anything-3.github.io/) — Official DA3 project site, including the any-view setting and a community project list.
- [Depth Anything 3 paper](https://arxiv.org/abs/2511.10647) — Lin, Chen, Liew, Chen, Li, Shi, Feng, and Kang, Depth Anything 3: Recovering the Visual Space from Any Views, arXiv:2511.10647.
- [DA3-LARGE](https://huggingface.co/depth-anything/DA3-LARGE) — Hub weights for a large Depth Anything 3 checkpoint.
- [Depth Anything 3 collection](https://huggingface.co/collections/depth-anything/depth-anything-3) — Official Hub collection of Depth Anything 3 checkpoints.
- [MiDaS](https://github.com/isl-org/MiDaS) — Intelligent Systems Lab (Intel ISL) code for robust monocular depth by mixing datasets for zero-shot cross-dataset transfer. MIT. Still the baseline many later models compare against.
- [MiDaS paper](https://arxiv.org/abs/1907.01341) — Ranftl et al., Towards Robust Monocular Depth Estimation: Mixing Datasets for Zero-shot Cross-dataset Transfer, arXiv:1907.01341 (later TPAMI).
- [MiDaS on PyTorch Hub](https://pytorch.org/hub/intelisl_midas_v2/) — PyTorch Hub entry for Intel ISL MiDaS v2, a common way to load the classic relative-depth models.
- [DPT](https://github.com/isl-org/DPT) — Dense Prediction Transformers: ISL's ViT decoder used for monocular depth and later reused inside many depth models, including Depth Pro 2's DPT decoder. MIT.
- [DPT paper](https://arxiv.org/abs/2103.13413) — Ranftl, Bochkovskiy, and Koltun, Vision Transformers for Dense Prediction, arXiv:2103.13413.
- [DPT-Large](https://huggingface.co/Intel/dpt-large) — Hub weights for Intel's DPT-Large dense prediction / depth model.
- [DPT-Hybrid MiDaS](https://huggingface.co/Intel/dpt-hybrid-midas) — Hub weights for the DPT-Hybrid MiDaS checkpoint.

### Metric monocular

- [ZoeDepth](https://github.com/isl-org/ZoeDepth) — ISL's metric depth model that combines relative and metric depth for zero-shot transfer from a single image. MIT.
- [ZoeDepth paper](https://arxiv.org/abs/2302.12288) — Bhat et al., ZoeDepth: Zero-shot Transfer by Combining Relative and Metric Depth, arXiv:2302.12288.
- [Metric3D](https://github.com/YvanYin/Metric3D) — Official repo for Metric3D and Metric3D v2, a monocular geometric foundation model for zero-shot metric depth and surface normals. BSD-2-Clause.
- [Metric3D v2 project page](https://jugghm.github.io/Metric3Dv2/) — Official project site for Metric3D v2.
- [Metric3D paper](https://arxiv.org/abs/2307.10984) — Yin et al., Metric3D: Towards Zero-shot Metric 3D Prediction from A Single Image, arXiv:2307.10984.
- [Metric3D v2 paper](https://arxiv.org/abs/2404.15506) — Hu et al., Metric3Dv2: A Versatile Monocular Geometric Foundation Model for Zero-shot Metric Depth and Surface Normal Estimation, arXiv:2404.15506.
- [UniDepth](https://github.com/lpiccinelli-eth/UniDepth) — Official code for UniDepth and UniDepthV2, universal monocular metric depth estimation that aims to work across cameras and domains.
- [UniDepth project page](https://lpiccinelli-eth.github.io/pub/unidepth/) — Official project site for UniDepth.
- [UniDepth paper](https://arxiv.org/abs/2403.18913) — Piccinelli et al., UniDepth: Universal Monocular Metric Depth Estimation, arXiv:2403.18913.
- [UniDepthV2 paper](https://arxiv.org/abs/2502.20110) — Piccinelli et al., UniDepthV2: Universal Monocular Metric Depth Estimation Made Simpler, arXiv:2502.20110.
- [UniK3D](https://github.com/lpiccinelli-eth/UniK3D) — Official code for UniK3D (CVPR 2025): universal camera monocular 3D estimation, a follow-on in the UniDepth line.
- [UniK3D project page](https://lpiccinelli-eth.github.io/pub/unik3d/) — Official project site for UniK3D.
- [Depth Any Camera](https://github.com/yuliangguo/depth_any_camera) — Official code for Depth Any Camera (CVPR 2025): zero-shot metric depth from any camera. MIT.
- [Depth Any Camera project page](https://yuliangguo.github.io/depth-any-camera/) — Official project site for Depth Any Camera.
- [Depth Any Camera paper](https://arxiv.org/abs/2501.02464) — Guo et al., Depth Any Camera: Zero-Shot Metric Depth Estimation from Any Camera, arXiv:2501.02464.
- [PatchFusion](https://github.com/zhyever/PatchFusion) — Official code for PatchFusion (CVPR 2024), a tile-based framework for high-resolution monocular metric depth. MIT.
- [PatchFusion project page](https://zhyever.github.io/PatchFusion/) — Official project site for PatchFusion.
- [Prompt Depth Anything](https://github.com/DepthAnything/PromptDA) — Official code for Prompt Depth Anything (PromptDA, CVPR 2025): prompting Depth Anything for high-resolution accurate metric depth. Apache-2.0.
- [Prompt Depth Anything project page](https://promptda.github.io/) — Official project site for Prompt Depth Anything.
- [MetricAnything](https://github.com/metric-anything/metric-anything) — Official code for MetricAnything, described in the repo as scaling metric depth pretraining with noisy heterogeneous sources (accepted to ECCV 2026). Apache-2.0.
- [AdaBins](https://github.com/shariqfarooq123/AdaBins) — Official implementation of AdaBins, metric monocular depth via adaptive bins. GPL-3.0.
- [AdelaiDepth](https://github.com/aim-uofa/AdelaiDepth) — Adelaide repo collecting Virtual Normal, DiverseDepth, and related single-image depth and 3D scene shape work. CC0-1.0 for the repo; check each project's terms.

### Diffusion and generative

- [Marigold](https://github.com/prs-eth/Marigold) — Official code for Marigold (CVPR 2024 Oral): repurposing diffusion image generators for monocular depth. Apache-2.0.
- [Marigold project page](https://marigoldmonodepth.github.io/) — Official project site for Marigold monocular depth.
- [Marigold paper](https://arxiv.org/abs/2312.02145) — Ke et al., Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation, arXiv:2312.02145.
- [Marigold Depth v1.1](https://huggingface.co/prs-eth/marigold-depth-v1-1) — Hub weights for the Marigold depth v1.1 checkpoint from the official ETH Zurich group.
- [Lotus](https://github.com/EnVision-Research/Lotus) — Official code for Lotus (ICLR 2025), a diffusion-based model for dense geometry prediction, including zero-shot depth and normals, with generative and regression (discriminative) checkpoints. Apache-2.0.
- [Lotus project page](https://lotus3d.github.io/) — Official project site for Lotus. The lotus-3d.github.io spelling does not resolve; this is the live page.
- [Lotus paper](https://arxiv.org/abs/2409.18124) — He, Li, et al., Lotus: Diffusion-based Visual Foundation Model for High-quality Dense Prediction, arXiv:2409.18124.
- [Lotus depth (regression, disparity)](https://huggingface.co/jingheya/lotus-depth-d-v2-0-disparity) — Hub checkpoint jingheya/lotus-depth-d-v2-0-disparity, the official discriminative / regression Lotus depth model in disparity.
- [Lotus depth (generative, disparity)](https://huggingface.co/jingheya/lotus-depth-g-v2-1-disparity) — Hub checkpoint jingheya/lotus-depth-g-v2-1-disparity, the official generative Lotus depth model in disparity.
- [Lotus-2](https://github.com/EnVision-Research/Lotus-2) — Official code for Lotus-2, a later geometric dense-prediction model built on a stronger image generator. Apache-2.0.
- [Lotus-2 project page](https://lotus-2.github.io/) — Official project site for Lotus-2.
- [Lotus-2 paper](https://arxiv.org/abs/2512.01030) — Lotus-2: Advancing Geometric Dense Prediction with Powerful Image Generative Model, arXiv:2512.01030, as cited by the official repo.
- [DepthFM](https://github.com/CompVis/depth-fm) — Official CompVis code for DepthFM (AAAI 2025 Oral): fast monocular depth estimation with flow matching. MIT.
- [DepthFM project page](https://depthfm.github.io/) — Official project site for DepthFM.
- [DepthFM paper](https://arxiv.org/abs/2403.13788) — Gui et al., DepthFM: Fast Monocular Depth Estimation with Flow Matching, arXiv:2403.13788.
- [GeoWizard](https://github.com/fuxiao0719/GeoWizard) — Official code for GeoWizard (ECCV 2024): diffusion priors for 3D geometry estimation, including depth, from a single image.
- [GeoWizard project page](https://fuxiao0719.github.io/projects/geowizard/) — Official project site for GeoWizard.
- [ECoDepth](https://github.com/Aradhye2002/EcoDepth) — Official code for ECoDepth (CVPR 2024): effective conditioning of diffusion models for monocular depth estimation.
- [ECoDepth project page](https://ecodepth-iitd.github.io/) — Official project site for ECoDepth.
- [ECoDepth paper](https://arxiv.org/abs/2403.18807) — Patni, Agarwal, and Arora, ECoDepth: Effective Conditioning of Diffusion Models for Monocular Depth Estimation, arXiv:2403.18807.

### Geometry and point maps

- [MoGe](https://github.com/microsoft/MoGe) — Official Microsoft code for MoGe, MoGe-2, and MoGe-3: monocular geometry (point maps, depth, optional normals and metric scale) from a single open-domain image. Check the LICENSE in the repo; it is not an OSI SPDX id on GitHub.
- [MoGe project page](https://wangrc.site/MoGePage/) — Official project site for MoGe (v1). The repo points here for videos and interactive results.
- [MoGe paper](https://arxiv.org/abs/2410.19115) — Wang et al., MoGe: Unlocking Accurate Monocular Geometry Estimation for Open-Domain Images with Optimal Training Supervision, arXiv:2410.19115.
- [MoGe-2 paper](https://arxiv.org/abs/2507.02546) — Wang et al., MoGe-2: Accurate Monocular Geometry with Metric Scale and Sharp Details, arXiv:2507.02546.
- [MoGe-2 ViT-L](https://huggingface.co/Ruicheng/moge-2-vitl) — Hub weights for MoGe-2 ViT-L, listed in the official MoGe README as a metric-scale monocular geometry model.
- [MoGe-3 paper](https://arxiv.org/abs/2607.17967) — MoGe-3: Fine-Detail Monocular Geometry Estimation with Self-Guided Sparse Volumetric Refinement, arXiv:2607.17967, as cited by the official MoGe repo.
- [MoGe-3 ViT-L](https://huggingface.co/Ruicheng/moge-3-vitl) — Hub weights for MoGe-3 ViT-L, listed in the official MoGe README.
- [VGGT](https://github.com/facebookresearch/vggt) — Official Meta FAIR code for VGGT (CVPR 2025 Best Paper): Visual Geometry Grounded Transformer, for multi-view geometry including depth.
- [VGGT paper](https://arxiv.org/abs/2503.11651) — Wang et al., VGGT: Visual Geometry Grounded Transformer, arXiv:2503.11651.
- [DUSt3R](https://github.com/naver/dust3r) — Official Naver Labs code for DUSt3R, geometric 3D vision from image pairs that also yields dense depth / point maps. The project site did not reliably load for this checker, so only the repo is listed.

## Video and temporal depth

Methods that estimate depth across frames so the map stays steady over a clip. Depth Pro 2's own video path lives in the Depth Pro 2 section.

- [Video Depth Anything](https://github.com/DepthAnything/Video-Depth-Anything) — Official code (CVPR 2025 Highlight) for consistent depth on long videos, built on Depth Anything V2, with relative and later metric checkpoints. Apache-2.0.
- [Video Depth Anything project page](https://videodepthanything.github.io/) — Official project site for Video Depth Anything.
- [Video Depth Anything paper](https://arxiv.org/abs/2501.12375) — Chen et al., Video Depth Anything: Consistent Depth Estimation for Super-Long Videos, arXiv:2501.12375, as cited by the official repo.
- [DepthCrafter](https://github.com/Tencent/DepthCrafter) — Official Tencent code (CVPR 2025 Highlight) for generating temporally consistent long depth sequences for open-world videos with a diffusion prior, without requiring camera poses or optical flow.
- [DepthCrafter project page](https://depthcrafter.github.io/) — Official project site for DepthCrafter.
- [DepthCrafter paper](https://arxiv.org/abs/2409.02095) — Hu et al., DepthCrafter: Generating Consistent Long Depth Sequences for Open-world Videos, arXiv:2409.02095.
- [DepthCrafter weights](https://huggingface.co/tencent/DepthCrafter) — Official Hub weights for DepthCrafter.
- [GeometryCrafter](https://github.com/TencentARC/GeometryCrafter) — Official Tencent ARC code (ICCV 2025) for consistent geometry estimation on open-world videos, a follow-on to DepthCrafter aimed at video-to-point-cloud geometry.
- [GeometryCrafter project page](https://geometrycrafter.github.io/) — Official project site for GeometryCrafter.
- [GeometryCrafter paper](https://arxiv.org/abs/2504.01016) — GeometryCrafter: Consistent Geometry Estimation for Open-world Videos with Diffusion Priors, arXiv:2504.01016, as cited by the official repo.
- [RollingDepth](https://github.com/prs-eth/RollingDepth) — Official ETH Zurich code (CVPR 2025) for video depth without a dedicated video backbone, rolling a monocular depth model over frames. Apache-2.0.
- [RollingDepth project page](https://rollingdepth.github.io/) — Official project site for RollingDepth.
- [RollingDepth paper](https://arxiv.org/abs/2411.19189) — Video Depth without Video Models, arXiv:2411.19189, as cited by the official RollingDepth repo.
- [DVD](https://github.com/EnVision-Research/DVD) — Official code for DVD: Deterministic Video Depth Estimation with Generative Priors. Apache-2.0.
- [DVD project page](https://dvd-project.github.io/) — Official project site for DVD.
- [DVD paper](https://arxiv.org/abs/2603.12250) — DVD: Deterministic Video Depth Estimation with Generative Priors, arXiv:2603.12250, as cited by the official repo.

## Runtimes and ports

Libraries, converters, and nodes that load a published depth model on your machine or in a tool. A demo Space belongs under Demos.

### Libraries and official ports

- [transformers DepthPro docs](https://huggingface.co/docs/transformers/en/model_doc/depth_pro) — Hugging Face transformers documentation for the DepthPro model class. The examples use apple/DepthPro and apple/DepthPro-hf (Depth Pro v1), not the Depth Pro 2 family.
- [transformers Depth Anything docs](https://huggingface.co/docs/transformers/en/model_doc/depth_anything) — Hugging Face transformers documentation for the Depth Anything model.
- [transformers Depth Anything V2 docs](https://huggingface.co/docs/transformers/en/model_doc/depth_anything_v2) — Hugging Face transformers documentation for Depth Anything V2.
- [transformers ZoeDepth docs](https://huggingface.co/docs/transformers/en/model_doc/zoedepth) — Hugging Face transformers documentation for ZoeDepth.
- [transformers DPT docs](https://huggingface.co/docs/transformers/en/model_doc/dpt) — Hugging Face transformers documentation for DPT dense prediction / depth models.

### ONNX, TensorRT and Core ML

- [Depth Anything ONNX](https://github.com/fabio-sim/Depth-Anything-ONNX) — ONNX-compatible export and inference for Depth Anything. Apache-2.0. Community port, not the official Apple or Depth Anything runtime.
- [Depth Anything V2 Small (ONNX Community)](https://huggingface.co/onnx-community/depth-anything-v2-small) — ONNX Community Hub build of Depth Anything V2 Small, suitable for local ONNX runtimes and some in-browser pipelines.
- [Depth Anything TensorRT](https://github.com/spacewalk01/depth-anything-tensorrt) — C++ TensorRT implementation of Depth Anything V1 and V2. MIT. Community port.

### ComfyUI and creative tools

- [ComfyUI-DepthAnythingV2](https://github.com/kijai/ComfyUI-DepthAnythingV2) — Kijai's ComfyUI nodes for Depth Anything V2 inference.
- [ComfyUI-Depth-Pro](https://github.com/spacepxl/ComfyUI-Depth-Pro) — ComfyUI nodes for Apple Depth Pro. The repo points at the original ml-depth-pro line (v1); this list does not claim Depth Pro 2 support without a first-party note.
- [ComfyUI-DepthCrafter-Nodes](https://github.com/akatz-ai/ComfyUI-DepthCrafter-Nodes) — Community ComfyUI port of Tencent's DepthCrafter, for temporally consistent video depth inside ComfyUI.
- [ComfyUI ControlNet aux preprocessors](https://github.com/Fannovel16/comfyui_controlnet_aux) — ComfyUI's widely used ControlNet auxiliary preprocessors, including depth map preprocessors used with depth-conditioned generation. Apache-2.0.

### Browser

- [Transformers.js](https://github.com/huggingface/transformers.js) — Official library for running Transformers models in the browser, with no server. Apache-2.0. Several community depth WebGPU Spaces returned 401 to this checker and are not listed.
- [Transformers.js docs](https://huggingface.co/docs/transformers.js/en/index) — Documentation home for Transformers.js.
- [Transformers.js pipelines docs](https://huggingface.co/docs/transformers.js/en/pipelines) — Pipeline reference for Transformers.js, the usual entry for vision tasks in the browser.

## Demos

Live pages where you can try a model in the browser. Official project pages that are not runnable demos live with their models.

- [Depth Pro v1 Space (akhaliq)](https://huggingface.co/spaces/akhaliq/depth-pro) — Community Gradio Space for the original Apple Depth Pro model.
- [Depth Anything Space](https://huggingface.co/spaces/LiheYoung/Depth-Anything) — Official-line Gradio Space for Depth Anything v1.
- [Depth Anything V2 Space](https://huggingface.co/spaces/depth-anything/Depth-Anything-V2) — Official Gradio Space for Depth Anything V2.
- [Depth Anything 3 Space](https://huggingface.co/spaces/depth-anything/depth-anything-3) — Official Gradio Space for Depth Anything 3.
- [Video Depth Anything Space](https://huggingface.co/spaces/depth-anything/Video-Depth-Anything) — Official Gradio Space for Video Depth Anything.
- [DepthCrafter Space](https://huggingface.co/spaces/tencent/DepthCrafter) — Official Tencent Gradio Space for DepthCrafter.
- [GeometryCrafter Space](https://huggingface.co/spaces/TencentARC/GeometryCrafter) — Official Tencent ARC Gradio Space for GeometryCrafter.
- [Marigold Space](https://huggingface.co/spaces/prs-eth/marigold) — Official ETH Zurich Gradio Space for Marigold.
- [MoGe Space](https://huggingface.co/spaces/Ruicheng/MoGe) — Official Gradio Space for MoGe, linked from the MoGe README.
- [MoGe-2 Space](https://huggingface.co/spaces/Ruicheng/MoGe-2) — Official Gradio Space for MoGe-2, linked from the MoGe README.

## Use cases

Applications that consume a depth map: 3D photos, geometry initialization, occlusion, compositing, and controlled generation. Sensor-depth APIs are labeled as such.

### 3D photos and parallax

- [3D Photo Inpainting](https://github.com/vt-vl-lab/3d-photo-inpainting) — Official code (CVPR 2020) for 3D photography from a single RGB-D image via context-aware layered depth inpainting, the usual open baseline for monocular 3D photo / parallax effects.
- [3D Photo Inpainting project page](https://shihmengli.github.io/3D-Photo-Inpainting/) — Official project site for 3D Photography using Context-aware Layered Depth Inpainting.
- [3D Photo Inpainting paper](https://arxiv.org/abs/2004.04727) — Shih et al., 3D Photography using Context-aware Layered Depth Inpainting, arXiv:2004.04727.

### Gaussian splatting and NeRF

- [3D Gaussian Splatting](https://github.com/graphdeco-inria/gaussian-splatting) — Original INRIA / Max Planck implementation of 3D Gaussian Splatting for real-time radiance field rendering. Depth maps from monocular models are a common way to initialize or regularize later splat systems.
- [3D Gaussian Splatting project page](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) — Official project site for 3D Gaussian Splatting.
- [DN-Splatter](https://github.com/maturk/dn-splatter) — Official code for DN-Splatter: depth and normal priors for Gaussian splatting and meshing. Apache-2.0.
- [DN-Splatter project page](https://maturk.github.io/dn-splatter/) — Official project site for DN-Splatter.
- [DN-Splatter paper](https://arxiv.org/abs/2403.17822) — Turkulainen et al., DN-Splatter: Depth and Normal Priors for Gaussian Splatting and Meshing, arXiv:2403.17822.
- [DepthSplat](https://github.com/cvg/depthsplat) — Official ETH Zurich / Microsoft code (CVPR 2025) connecting Gaussian splatting and depth. MIT.
- [DepthSplat project page](https://haofeixu.github.io/depthsplat/) — Official project site for DepthSplat.
- [DepthSplat paper](https://arxiv.org/abs/2410.13862) — Xu et al., DepthSplat: Connecting Gaussian Splatting and Depth, arXiv:2410.13862.
- [Nerfstudio](https://github.com/nerfstudio-project/nerfstudio) — Open studio for neural radiance fields and later 3D methods, often used with depth supervision or depth-initialized geometry. Apache-2.0.
- [Nerfstudio docs](https://docs.nerf.studio/) — Documentation for Nerfstudio.

### AR occlusion

- [ARKit](https://developer.apple.com/documentation/ARKit) — Apple's ARKit documentation home. Scene depth and people occlusion on supported devices typically come from platform depth sensors, not from a learned monocular model; listed because occlusion is a primary use of a depth map in AR.
- [ARDepthData](https://developer.apple.com/documentation/arkit/ardepthdata) — ARKit API for per-pixel scene depth data used to occlude or place virtual content.
- [ARKit people occlusion](https://developer.apple.com/documentation/arkit/occluding-virtual-content-with-people) — Apple's guide to occluding virtual content with people in an ARKit scene.
- [ARKit scene-depth point cloud](https://developer.apple.com/documentation/arkit/displaying-a-point-cloud-using-scene-depth) — Apple's sample for displaying a point cloud from ARKit scene depth.
- [WebXR Depth Sensing](https://immersive-web.github.io/depth-sensing/) — Immersive Web Working Group specification for exposing a device depth buffer to WebXR scenes, typically sensor depth, for occlusion and hit-testing in the browser.
- [WebXR Depth Sensing repo](https://github.com/immersive-web/depth-sensing) — Working-group repository for the WebXR Depth Sensing specification.

### VFX and relighting

- [NukeDepthCrafter](https://github.com/Theo-SAMINADIN-td/NukeDepthCrafter) — Community Nuke plugin that runs DepthCrafter inside Foundry Nuke, so VFX comps can generate temporally consistent depth sequences, including EXR export. Linked from the official DepthCrafter README's community section.

### Depth-conditioned generation

- [ControlNet](https://github.com/lllyasviel/ControlNet) — Official ControlNet repo for spatially controlling diffusion models, including depth-conditioned generation. Apache-2.0.
- [ControlNet v1.1 depth (SD 1.5)](https://huggingface.co/lllyasviel/control_v11f1p_sd15_depth) — Official Hub weights for ControlNet v1.1 depth on Stable Diffusion 1.5, the usual depth-to-image ControlNet checkpoint.
- [Diffusers ControlNet guide](https://huggingface.co/docs/diffusers/using-diffusers/controlnet) — Hugging Face Diffusers guide to running ControlNet, including depth conditioning.

## Datasets and benchmarks

Datasets and benches commonly used to train or compare monocular and video depth, including Sintel and Spring, which Depth Pro 2 uses for its sharpness and jitter comparisons.

- [KITTI depth evaluation](https://www.cvlibs.net/datasets/kitti/eval_depth.php) — Official KITTI depth prediction evaluation page, the long-running outdoor driving monocular and stereo depth benchmark.
- [NYU Depth V2](https://cs.nyu.edu/~fergus/datasets/nyu_depth_v2.html) — NYU-Depth V2 indoor RGB-D dataset page (current URL under ~fergus; the older ~silberman path redirects here). A standard indoor monocular depth test set.
- [MPI Sintel](https://sintel.is.tue.mpg.de/) — MPI Sintel dataset and benchmark site. Depth Pro 2 reports sharpness and temporal jitter averaged over Sintel and Spring. The dedicated /depth path returned 500 to this checker, so the main site is the listed entry.
- [Spring](https://spring-benchmark.org/) — Spring dataset and benchmark for high-resolution stereo, optical flow, and scene flow, including per-frame disparity used as depth. Depth Pro 2 uses Spring, with Sintel, for its official sharpness and jitter comparison.
- [Spring paper](https://arxiv.org/abs/2303.01943) — Mehl, Schmalfuss, Jahedi, Nalivayko, and Bruhn, Spring: A High-Resolution High-Detail Dataset and Benchmark for Scene Flow, Optical Flow and Stereo, arXiv:2303.01943, as linked from the official Spring site.
- [ETH3D](https://www.eth3d.net/) — ETH3D benchmark home for multi-view stereo, high-resolution geometry, and related depth evaluation.
- [ETH3D datasets](https://www.eth3d.net/datasets) — ETH3D dataset download and documentation page.
- [DIODE](https://diode-dataset.org/) — DIODE: a dense indoor and outdoor depth dataset with high-precision LiDAR ground truth.
- [DIODE paper](https://arxiv.org/abs/1908.00463) — Vasiljevic et al., DIODE: A Dense Indoor and Outdoor DEpth Dataset, arXiv:1908.00463.
- [ScanNet](https://github.com/ScanNet/ScanNet) — Official ScanNet RGB-D indoor scan dataset repository. The project website did not reliably load for this checker, so the repo is the listed entry.
- [Hypersim](https://github.com/apple-aiml-research/ml-hypersim) — Apple's Hypersim photorealistic synthetic indoor dataset, often used for monocular depth and scene understanding. The older apple/ml-hypersim URL redirects here.
- [MegaDepth](https://www.cs.cornell.edu/projects/megadepth/) — Cornell MegaDepth: single-view depth supervision mined from internet photos and multi-view stereo.
- [BlendedMVS](https://github.com/YoYo000/BlendedMVS) — Official repo for BlendedMVS, a large-scale dataset for generalized multi-view stereo, also used as depth supervision.
- [Virtual KITTI 2](https://europe.naverlabs.com/proxy-virtual-worlds-vkitti-2/) — Naver Labs Europe page for Virtual KITTI 2, a synthetic driving dataset with ground-truth depth and related labels.
- [Middlebury Stereo datasets](https://vision.middlebury.edu/stereo/data/) — Middlebury stereo evaluation datasets, a classic source of high-quality disparity / depth maps.
- [DDAD](https://github.com/TRI-ML/DDAD) — Toyota Research Institute Dense Depth for Autonomous Driving dataset, long-range monocular and stereo depth in driving scenes.
- [TUM RGB-D](https://cvg.cit.tum.de/data/datasets/rgbd-dataset) — TUM RGB-D dataset of indoor RGB-D sequences with camera trajectories, used for depth, odometry, and SLAM evaluation.

## Awesome lists and indexes

Related indexes. This list does not try to replace a complete paper bibliography.

- [Awesome Monocular Depth](https://github.com/choyingw/Awesome-Monocular-Depth) — Curated list of monocular depth estimation papers, last updated in the mid-2024 era on the landing page. Consulted as an index, not bulk-imported.
- [Awesome Foundation-Model-Based Depth](https://github.com/Ideal-111/Awesome-Foundation-Model-Based-Depth) — Curated list of foundation-model depth estimation and completion papers, including 2025-2026 work such as Depth Anything 3 and MetricAnything. The older Depth-Foundation-Model URL redirects here.
- [Awesome 360 Depth Estimation](https://github.com/bikhanal/awesome-360-depth-estimation) — Curated list of 360-degree / panoramic monocular depth papers.
- [Video depth estimation rankings](https://github.com/AIVFI/Video-Depth-Estimation-Rankings-and-Stereo-Video-Conversion-Rankings) — Community rankings for video depth estimation and stereo video conversion. An older repo path redirects to this canonical name.
- [GitHub topic: monocular-depth-estimation](https://github.com/topics/monocular-depth-estimation) — GitHub topic page that surfaces public monocular depth repositories.

## Sources

Indexes consulted for this pass. Entries were not bulk-copied; each README link was checked on its own. Machine-readable rows: [`links.json`](links.json). Counts: [`stats.txt`](stats.txt). Notes on pages that did not earn a README line: [`discoveries/`](discoveries/).

- Manual curation — Entries written for this list on 2026-11-19 PT.
- [Hugging Face Hub API](https://huggingface.co/models) — Model id, license field, pipeline tag, and createdAt for Hub repos in this list.
- [First-party Depth Pro 2 pages](https://huggingface.co/apple/DepthPro2) — Apple model card, GitHub README, project page, Core ML card, LICENSE_MODEL, and arXiv 2611.26603.
- [choyingw/Awesome-Monocular-Depth](https://github.com/choyingw/Awesome-Monocular-Depth) — Consulted as a paper index; links re-checked and not bulk-imported.
- [Ideal-111/Awesome-Foundation-Model-Based-Depth](https://github.com/Ideal-111/Awesome-Foundation-Model-Based-Depth) — Consulted as a foundation-model depth index; links re-checked and not bulk-imported.

## Contributing

One factual line in the right subsection: `[Name](url) — What it actually is.` Say whether a model predicts metric or relative depth, and whether weights are Apache-2.0 or MIT, or a research / non-commercial license. Do not invent star counts, release days, benchmark scores, or paper ids. Prefer a model card or official repo over a roundup. Weak or unverified finds go in [`discoveries/`](discoveries/) instead of the README.

Add the row to [`links.json`](links.json) (url, title, category, subsection, blurb, sources) and run `python3 build.py`. The script dedupes on the normalized URL and rewrites this file.

List text is dedicated to the public domain under [CC0 1.0](LICENSE). Linked projects keep their own licenses.

## License

This compilation is dedicated to the public domain under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). Individual projects and linked content retain their own licenses and terms. Depth Pro 2 weights are under Apple's research-only model license, not this compilation's CC0.
