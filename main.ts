// Entry for make.fun's "Sum up 18 November's world news in one image"
// (news-image-20261118): a newspaper-style infographic drawn with
// Pillow and the DejaVu Sans font, 1024x1024 PNG, seven stories from
// Wednesday 18 November 2026. The copy below is fully deterministic:
// the same entry.png is written on every run.
//
// A news-image entry (Node 22, standard library only): its image is
// the entry.png beside this file, and the program copies it to
// /output/entry.png. The gate takes a whole PNG or JPEG of at most
// 1 MiB and 1024 by 1024 pixels, and the judge sees exactly the
// bytes copied.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
// /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync } from 'node:fs';
import { join } from 'node:path';

copyFileSync(new URL('./entry.png', import.meta.url), join(process.env.MAKEFUN_OUTPUT_DIR ?? '/output', 'entry.png'));
