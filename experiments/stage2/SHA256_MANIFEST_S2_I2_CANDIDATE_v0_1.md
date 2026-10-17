# S2-I2 implementation candidate v0.1 - SHA-256 manifest

Each SHA-256 covers exact uncompressed archive-member bytes, not the ZIP container.

| ZIP member path | Bytes | SHA-256 | EOL |
| --- | ---: | --- | --- |
| `CLAUDE_REVIEW_REQUEST_S2_I2_IMPLEMENTATION_v0_1.md` | 3768 | `14a5ea1f17ae2f2315049760c1a896bb1fdfb1dea9f7a60ec9337fea8d9a0bac` | CRLF |
| `S2_I2_IMPLEMENTATION_REHEARSAL_EVIDENCE_v0_1.md` | 5819 | `89481338f9654faaef848453946b2faf0c808e7427aa66c813f891b13bfe4148` | CRLF |
| `S2_I2_IMPLEMENTATION_v0_1_README_FOR_CLAUDE.md` | 8862 | `0b2a7ab97b63c4f54e3eb483eae7544c7acc24be64642ae8d8487ea618f030de` | CRLF |
| `S2_I2_IMPLEMENTATION_v0_1_TRACEABILITY.md` | 3886 | `1cc0838f67824f2591fb30e4078c8d1ca0e97e56b163139f8e773022724620b3` | CRLF |
| `REPO_OVERLAY/experiments/stage2/S2_I2_prepare_LP_blocky_index_v0_1.bat` | 3096 | `7c1f0a3d6ad286048617cfa5ed04f396420896ef64af8d67cee34446431021b3` | CRLF |
| `REPO_OVERLAY/experiments/stage2/S2_I2_run_registration_v0_1.bat` | 3695 | `4f1f18d496a54c420938e22e691d0bceef8ce5f6fb9945eed7b2b26d5b0707a4` | CRLF |
| `REPO_OVERLAY/experiments/stage2/stage2_check_result_v0_1.py` | 890 | `417a9d219811b9275651786c078e21465ff0859aac05cd3efe851e433d4d4817` | LF |
| `REPO_OVERLAY/experiments/stage2/stage2_ffmpeg_rehearsal_v0_1.py` | 2545 | `1f35d9598f5967acb6af339fc1edcf926c1892a14aee4dd5f9f1dd0b5d73fa62` | LF |
| `REPO_OVERLAY/experiments/stage2/stage2_registration_clip_v0_1.vpy` | 3351 | `8a85aadc85ce6941c3467d444a1cb80c6c775ba2674c857fc659d687ed9e1e6b` | LF |
| `REPO_OVERLAY/experiments/stage2/stage2_registration_stats_v0_1.py` | 31936 | `2f640f17ad600c9866455d73db17142dea6bd7025cd1e99a5fcb28e4679beb1c` | LF |
| `REPO_OVERLAY/experiments/stage2/stage2_registration_tests_v0_1.py` | 3182 | `a1fa72353485b9ec2ac7f3db6b6b1c4a4dd8f4e3b3d95083cb52892b68896af9` | LF |
| `REPO_OVERLAY/experiments/stage2/stage2_validate_lp_blocky_v0_1.py` | 1815 | `bfe38b1dcdce78a5d8f95264208935ab435b7f5c5359455b7b76a9d5745eac6a` | LF |
| `REPO_OVERLAY/experiments/stage2/stage2_vspipe_env_preflight_v0_1.vpy` | 1566 | `333f7db0b1b372e5b26871b66d7b5bd753597a32b4fc179d5e0a08672db4b505` | LF |

Expected overlay: exactly 9 proposed files in `REPO_OVERLAY/experiments/stage2/`; no older v0.1 S2-I1 files, no media/index/executable.
Frozen Stage 1 code, indexes and accepted S2-I1 v0.2 reader are **not** copied or changed.
