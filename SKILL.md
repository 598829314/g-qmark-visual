---
name: g-qmark-visual
description: "Create consistent G_QMark visuals in a bright, calm, rounded editorial style. Use for explanatory images, workflows, comparisons, technical concepts, personal video overlays, transparent character assets, Wenhao scenes, Golden Pup scenes, device illustrations, and reusable visual components."
---

# G_QMark Visual

Create visuals in one shared personal visual system for G_QMark. The system should feel bright, calm, orderly, rounded, restrainedly cute, and technically literate.

Choose one output mode before generating. Do not mix production paths unless the user explicitly asks for a composed final scene plus separate reusable assets.

## Choose the output mode

### Mode A — explanatory image

Use when the image itself must explain a concept, mechanism, workflow, comparison, tradeoff, or result.

- Deliver a finished PNG or WebP with an off-white scene.
- Keep one clear claim, one dominant action or relation, and no more than three major visual regions.
- Use real objects, devices, files, windows, model blocks, arrows, paths, repeated states, or spatial relationships as evidence.
- Essential labels may be generated directly inside the bitmap, but keep them short and exact.
- Characters support the explanation; they do not replace it.

### Mode B — transparent reusable asset

Use when the output will be composed into a video, hero, card, document, slide, lower third, thumbnail, or other layout.

- Generate one reusable subject or compact scene with generous padding.
- Use a perfectly uniform chroma-key background that does not occur in the artwork. Default to `#00FF00`; use `#FF00FF` when the subject contains green.
- Do not include explanatory text unless explicitly requested.
- Remove the background with `scripts/cutout.py` and deliver a transparent PNG.
- Preserve the transparent asset for reuse instead of flattening it into a one-off composition.

If the destination is unclear, choose Mode A when the image itself must communicate the idea, and Mode B when another layout or video will carry the explanation.

## Identity system

### Identity marks

- `G_QMark` is the formal project and visual-system name.
- `G_Q` is the core personality-bearing short mark.
- `G?` is an optional secondary abstract symbol for favicons, micro-icons and derived motion.

Treat `G_Q` as a tiny emoticon-like face gently rubbing sleepy eyes: the rounded G and Q suggest sleepy eyes or hands at the eyes, while the underscore acts as a calm mouth line or resting facial centerline.

- Keep `G_Q` immediately readable; preserve the underscore.
- Use dark charcoal for the main mark.
- Allow only a subtle sleepy-eye association—do not add literal hands, eyelashes or a cartoon face.
- Warm yellow `#F2C94C` remains the recurring color motif and may appear as a chapter marker, status point, cursor, process node, pendant, or small accent.
- Do not place the logo in every image. Use it when the asset is explicitly branded, used as an intro/outro, watermark, title card, profile asset, or reusable identity component.
- Derived states such as `G_?`, `G_!` and `G_O` may express status, but never replace the formal identity.
- Do not invent extra slogans or brand text.

### Wenhao small stick figure

Wenhao is the tiny line-drawn human narrator.

Fixed traits:

- slightly oversized simple round head
- short black hair drawn with only a few strokes
- tiny simple glasses
- sleepy dot or short-line eyes and restrained mouth
- very short line body, arms and legs; total height around 2.5–3 head diameters
- small dark torso shape suggesting a black T-shirt
- one tiny warm-yellow pendant dot
- rounded, slightly imperfect graphite doodle lines

Use Wenhao when a scene benefits from a human decision, test, presentation, camera action, reading, making or device interaction. Never stretch the figure into a tall or anatomically realistic stick figure. Avoid detailed faces, fingers, clothing folds, shoes, anime rendering and painted chibi styling.

### Golden Pup mascot

Golden Pup is a small golden retriever puppy companion representing companionship, curiosity, waiting, observation and lightweight process state.

Fixed traits:

- unmistakably a young golden retriever puppy
- one low bean-shaped head-and-body silhouette with almost no neck
- wide soft semicircle ears hanging at both sides
- very short rounded limbs and a tiny curled tail
- dot eyes, tiny oval nose and relaxed small mouth
- subtle pale-cream muzzle patch
- warm golden-yellow / ochre flat body
- the same thick rounded graphite doodle line language as Wenhao

Golden Pup may sit beside a laptop, NAS, camera, model block or progress bar; lie with its chin on its paws; carry a soft ball; peek from a folder; or accompany Wenhao. Keep it secondary to the information.

Do not give it separate realistic head-and-torso anatomy or turn it into a cat, border collie, adult tall dog, robot, armored animal or realistically rendered pet. Avoid pointy ears, detailed fur, anime eyes and complex clothing.

## Shared visual language

### Overall feel

Aim for:

- bright
- calm
- slightly sleepy
- relaxed
- rounded
- orderly
- restrainedly cute
- editorial rather than childish
- technical through content, not through neon styling

### Base palette

Use these colors as the default system:

- warm off-white background: `#FFFDF7`
- card white: `#FFFFFF`
- primary charcoal / text: `#30343B`
- secondary line gray: `#60656F`
- identity yellow: `#F2C94C`
- sky blue: `#8EC5E8`
- sage green: `#A9C8A5`
- soft orange: `#F2A66F`
- soft purple: `#B9A7D8`

Use one or two semantic accent colors in most scenes. Do not use every accent color simply because it exists in the palette.

Suggested semantic mapping:

- blue = input, information, data, cloud
- purple = AI, Agent, model, transformation, reasoning
- orange = action, warning, cost, friction
- green = success, stable state, completed result
- yellow = identity, focus, small highlight, current point

### Lines and shapes

- Use clean dark-gray outlines instead of pure black whenever possible.
- Prefer medium, confident line weight with slightly softer rounded joins.
- Use rounded rectangles, softly curved arrows, simple folders, windows, devices, chips, papers, and blocks.
- Allow slight hand-drawn character in arrows or small props, but keep the overall composition aligned and stable.
- Use flat fills or very subtle paper-like texture. Avoid glossy rendering.
- Shadows, when needed, should be minimal and soft-edged or represented by a simple flat offset shape.

### Composition

- Use warm off-white negative space as part of the design.
- Keep one dominant focal action.
- Use 2–4 useful environmental cues instead of filling the scene with props.
- Prefer clear left-to-right, top-to-bottom, split comparison, converging flow, or centered focal compositions.
- A viewer should recognize the subject in about 3 seconds and understand the main relation in about 10 seconds.
- Do not default to generic dashboard grids or a wall of cards.

### Explicit exclusions

Avoid:

- cyberpunk or futuristic HUD styling
- large dark backgrounds as the default visual language
- neon blue/purple glow
- glassmorphism
- glossy gradients
- photorealism
- complex 3D rendering
- over-detailed anime characters
- chibi proportions
- exaggerated meme expressions
- corporate PowerPoint icon grids
- random decorative stars, blobs, sparkles, or tech circuitry
- unnecessary robots, AI brains, glowing chips, or holograms
- visual clutter
- watermarks unless explicitly requested

## Mode A workflow — explanatory image

### 1. Write the visual brief

```text
viewer_question: what should be understood in 10 seconds?
concrete_claim: one-sentence conclusion
real_objects: visible devices, files, windows, documents, tools, models, or states
relation: comparison, transformation, causality, sequence, hierarchy, feedback, tradeoff, pipeline, or handoff
visual_evidence: what remains understandable when labels are ignored?
human_role: whether Wenhao is needed and what he is doing
golden-pup_role: whether Golden Pup adds useful state or personality
scene: believable setting and 2–4 useful environmental cues
semantic_colors: what each accent color means
labels: exact short strings plus the evidence surface for each label
```

Show the input, action or relation, and result. Keep one dominant focal action and no more than three major visual regions.

### 2. Decide whether Wenhao and Golden Pup are needed

Do not force both characters into every image.

Use Wenhao when:

- the scene benefits from a human decision, test, observation, presentation, or physical action
- the content is personal or first-person
- a human scale helps make a technical object understandable

Use Golden Pup when:

- the scene benefits from showing AI, Agent, curiosity, waiting, processing, error, or completion
- a small recurring mascot can add identity without obscuring the explanation

Use neither when the relationship is clearer through objects alone.

### 3. Design the labels

- Prefer 2–6 labels.
- Keep each label short and concrete: role, action, state, number, or outcome.
- Place labels directly on or beside their evidence surface.
- Use modern Chinese sans-serif typography, medium or bold, large enough to read at intended display size.
- Do not place body copy, commands, dense tables, or long paragraphs inside generated images.
- Use deterministic layout methods such as SVG, HTML/CSS, or video typography when dense or editable text is required.

When exact bitmap text is required, append:

```text
Text (verbatim): Render these exact labels as part of the illustration:
"<label 1>", "<label 2>", "<label 3>".
Use each phrase exactly once. Do not translate, paraphrase, misspell, repeat,
or add other text. Use modern sans-serif medium/bold typography, large and
readable. Place each label directly on or beside its evidence surface.
```

### 4. Build the generation prompt

Use this order:

1. State the concrete claim and shared task.
2. Describe the real setting and important objects.
3. Describe Wenhao and/or Golden Pup only if they are needed.
4. Describe the evidence geometry: aligned, split, nested, connected, transformed, repeated, moving, converging, or handed off.
5. Assign semantic colors.
6. Quote exact labels and placements when text is required.
7. Add the Mode A style anchor.
8. End with exclusions.

Mode A style anchor:

```text
Bright calm editorial illustration in the G_QMark visual system. Warm off-white
background with generous negative space. Clean rounded dark-charcoal outlines,
soft flat color blocks, orderly composition, and restrained cute details.
Technical information is shown through real devices, files, windows, model
blocks, arrows, states, and spatial relationships rather than futuristic HUD
decoration. Use the G_QMark palette: charcoal and off-white base, identity yellow
for tiny focus points, plus at most two soft semantic colors such as sky blue,
sage green, soft orange, or soft purple. If Wenhao appears, keep a round head, tiny glasses, sparse black hair, very short
line limbs, dark torso and tiny yellow pendant. If Golden Pup appears, keep a
round golden-retriever puppy body, short legs, floppy ears, cream muzzle and
warm golden-ochre flat coat. No cyberpunk, no neon glow, no glassmorphism,
no glossy gradients, no photorealism, no complex 3D, no chibi, no corporate
card grid, no decorative clutter, no watermark.
```

### 5. Inspect and retry

1. Inspect the output at original resolution.
2. Confirm the intended claim and relation are visible without relying only on text.
3. Compare every required label character by character.
4. Confirm Wenhao and Golden Pup retain their fixed traits when used.
5. Confirm identity yellow remains a small accent instead of flooding the scene.
6. Reject outputs that drift into dark neon tech styling, generic cartoon style, or corporate infographic grids.

For a text-only correction, use:

```text
Keep the scene, composition, characters, objects, colors, and all correct labels unchanged.
Change only the incorrect text "<wrong>" to the exact text "<right>".
Do not add, remove, translate, or repeat any other text.
```

## Mode B workflow — transparent asset

### 1. Choose one reusable subject

Prefer a single action or compact scene:

- Wenhao thinking at a laptop
- Wenhao holding a camera or document
- Wenhao presenting a model comparison
- Golden Pup resting on a progress bar
- Golden Pup peeking from a folder
- Golden Pup sitting on a NAS or model block
- Wenhao and Golden Pup observing one device together
- one device, icon, or prop designed for later composition

Leave generous padding around the subject.

### 2. Build the prompt

Describe the subject first, then append this fixed anchor. Replace `<KEY_COLOR>` before generation.

```text
Style: bright calm editorial illustration in the G_QMark visual system. Clean
rounded dark-charcoal outlines, soft flat fills, restrained cute proportions,
and no glossy or photorealistic rendering. Use the G_QMark palette with a
charcoal/off-white base and small identity-yellow accents. If Wenhao appears,
keep a round head, tiny glasses, sparse black hair, very short line limbs, dark
torso and tiny yellow pendant. If Golden Pup appears, keep a compact golden
retriever puppy body, short legs, floppy ears, cream muzzle and warm golden coat. The background must be a perfectly uniform flat <KEY_COLOR>
rectangle with zero gradient, texture, noise, speckles, shadows, floor plane,
or lighting variation. Do not let artwork touch the image border. Keep generous
padding. No text unless explicitly requested. No watermark. PNG format.
```

### 3. Validate the source

- Confirm all four corners are uniform and match the key color.
- Reject gradients, texture, shadows, speckles, or artwork touching the border.
- Confirm all character identity traits before background removal.
- Preserve the source image until the transparent result is approved.

### 4. Remove the background

Install Pillow if needed, then run:

```bash
python3 scripts/cutout.py source.png transparent.png
```

Optional tuning:

```bash
python3 scripts/cutout.py source.png transparent.png \
  --transparent-threshold 12 \
  --opaque-threshold 220
```

### 5. Validate the transparent result

- Confirm RGBA output and transparent corners.
- Confirm glasses, hair, pendant, Golden Pup floppy ears, muzzle and tail, and small yellow details remain complete.
- Check for key-color fringe at 100% zoom.
- Confirm internal light areas were not erased.
- Regenerate the source instead of forcing background removal when the source background is uneven.

## Video and motion readiness

When an asset is intended for video:

- Prefer transparent PNG or SVG when practical.
- Keep enough empty space around characters for motion, scaling, and cropping.
- Avoid baked-in subtitles or titles unless the user explicitly requests them.
- Separate identity marks, characters, mascot, devices, and text into reusable components when deterministic composition is possible.
- For lower thirds, title cards, diagrams, progress indicators, and logo reveals, prefer deterministic SVG/HTML/CSS/GSAP or editing-software animation over generative imagery.
- Keep motion simple: slide, fade, small bounce, tail movement, line drawing, progress movement, or `?` to `!` state changes. Avoid excessive kinetic effects.

## Asset organization

Approved reusable assets should follow this structure when the project supports it:

```text
assets/
  identity/
  characters/wenhao/
  mascot/golden-pup/
  icons/
  backgrounds/
prompts/
examples/
```

Use versioned filenames instead of silently overwriting approved assets.

Suggested naming:

```text
wenhao-thinking-v01.png
wenhao-presenting-v01.png
golden-pup-waiting-v01.png
golden-pup-complete-v01.png
gqmark-logo-mark-v01.svg
icon-local-model-v01.svg
```

## Quality gate

For every output:

- The subject is recognizable in about 3 seconds.
- The main action or relation is clear in about 10 seconds.
- The image feels bright, calm, rounded, orderly, and restrainedly cute.
- The technical content is represented by meaningful objects and relationships rather than generic AI decoration.
- Identity yellow is used sparingly and consistently.
- Wenhao and Golden Pup retain their fixed traits when present.
- The composition contains enough negative space and does not become a card grid or decoration wall.

For Mode A:

- One claim, one focal action, and no more than three major visual regions.
- Visual evidence still communicates the relation when labels are ignored.
- Every required label is exact, appears once, and remains readable.

For Mode B:

- Background removal is clean and genuinely transparent.
- Thin details and fixed identity marks remain intact.
- No source background, fringe, shadow, or border artifact remains.
