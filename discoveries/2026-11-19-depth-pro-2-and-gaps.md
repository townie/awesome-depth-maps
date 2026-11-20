# Depth Pro 2 release notes and pages that did not get a README line

Ingest: **2026-11-19 PT** (America/Los_Angeles).

## Depth Pro 2, as first-party pages stand today

- The [Hub card](https://huggingface.co/apple/DepthPro2) was created 2026-11-03 (Hub `createdAt`). Weight repos S/B/L/H were created 2026-11-05. The Core ML repo was created 2026-11-09. The standalone focal-length repo, `apple/DepthPro2-focal`, was created 2026-11-19. These are Hub timestamps, not a claim about when Apple announced the work.
- The [technical report](https://arxiv.org/abs/2611.26603) is live: *Depth Pro 2: Sharp and Temporally Consistent Metric Monocular Depth*, submitted 19 November 2026. Some secondary posts written earlier treated the arXiv id as a placeholder. This list uses the live paper, not those recaps.
- Official counts, from the card and the GitHub README: S 24M / 97 MB, B 97M / 386 MB, L 334M / 1.3 GB, H+ 872M / 3.5 GB (`apple/DepthPro2-H`), shared focal estimator 23.5M / 94 MB.
- The README is explicit that the public repo is inference-only: no training or evaluation code.
- Weights: Apple Machine Learning Research Model license, research use only. Code: Apple software license. Neither is Apache-2.0 or MIT.

## Checked, not given a README line

- **`machinelearning.apple.com/research/depth-pro-2`** returned **404**. The v1 research page at [machinelearning.apple.com/research/depth-pro](https://machinelearning.apple.com/research/depth-pro) is listed under Depth Pro v1.
- **`huggingface.co/spaces/apple/DepthPro2`** returned **401**. The project page still links it. It is omitted until a public fetch succeeds. The community Space [akhaliq/DepthPro2](https://huggingface.co/spaces/akhaliq/DepthPro2) is listed instead.
- **Transformers DepthPro** documents `apple/DepthPro` and `apple/DepthPro-hf` (v1). This checker did not find Depth Pro 2 support in those docs, so the list does not claim it.
- **`spacepxl/ComfyUI-Depth-Pro`** points at the original Depth Pro repo. It is listed as a v1-era ComfyUI node, not as a Depth Pro 2 port.
- **WebGPU / in-browser Spaces** `Xenova/depth-anything-webgpu` and `webml-community/depth-anything-webgpu` returned **401** and are omitted. Transformers.js docs and an ONNX Community V2 Small build are listed instead.
- **Official Lotus Spaces** (`EnVision-Research/Lotus`, `jingheya/lotus`, `jingheya/lotus-depth`) returned **401**. The GitHub repo, project page, paper, and two disparity checkpoints are listed.
- **`lotus-3d.github.io`** returned **404**. The live project page is [lotus3d.github.io](https://lotus3d.github.io/).
- **`paperswithcode.com/task/monocular-depth-estimation`** redirected to `huggingface.co/papers/trending`, which is not a depth-estimation task page. Not listed.
- **ScanNet's website** (`scan-net.org`, `kaldir.vc.in.tum.de/scannet/`) did not reliably load (error or 403). The [ScanNet GitHub repo](https://github.com/ScanNet/ScanNet) is listed instead.
- **`sintel.is.tue.mpg.de/depth`** returned **500**. The [main Sintel site](https://sintel.is.tue.mpg.de/) is listed.
- **DUSt3R's project site** (`dust3r.europe.naverlabs.com`) did not reliably load. The [GitHub repo](https://github.com/naver/dust3r) is listed.
- **Guessed paper ids that were wrong**, and therefore never listed: `arXiv:2501.12378` is *A quantum algorithm for Khovanov homology*, not Video Depth Anything (the official id is `2501.12375`). `arXiv:2303.02122` is a Banach-space paper, not Spring (the official id, from spring-benchmark.org, is `2303.01943`). `arXiv:2502.16598` was a guessed UniDepthV2 id; the official id is `2502.20110`.
- **Other 404s** from first-guess URLs (wrong orgs for RollingDepth, Depth Any Camera, PromptDA, GeoWizard, DepthFM, ECoDepth, MetricAnything, several ComfyUI and TensorRT forks, older awesome-list paths) were dropped. Live official URLs, when found, were used instead.

## Out of scope on purpose

- Thin or unverified student robotics and accessibility repos were not added. ARKit and WebXR depth are listed and labeled as typically **sensor** depth, because that is what the first-party docs describe. A first-party monocular-depth accessibility product page was not confirmed.
- NVIDIA Isaac ROS DNN stereo depth is a stereo stack, not monocular, and was left out.
- Star counts, Hub like counts, and unofficial runtime or memory numbers (including blog recaps) were not copied into the README.
