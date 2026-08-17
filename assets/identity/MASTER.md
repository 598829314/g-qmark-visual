# G_QMark Identity Master

Status: G_Q v1 SVG master approved.

This file defines the canonical rules for the G_QMark identity. The approved v1 assets live beside this file.

## 1. Identity structure

The system has three levels:

1. `G_QMark` — formal project and visual-system name for repositories, documents, title cards and full signatures.
2. `G_Q` — core personality-bearing short mark for avatars, video corner marks, motion reveals and watermarks.
3. `G?` — optional secondary abstract symbol for favicons, micro-icons and derived motion shorthand.

`G_Q` is the primary recognition unit in personal and compact contexts. `G?` remains available when a reduced graphical symbol is genuinely clearer, but it is not the only primary mark.

## 2. Visual character

The mark should feel:

- sleepy
- calm
- quiet
- slightly dazed
- rounded
- restrained
- already starting work

`G_Q` should first read as a tiny emoticon-like face gently rubbing sleepy eyes: the rounded `G` and `Q` suggest two eyes or hands at the eyes, while `_` acts as a calm mouth line or resting facial centerline. It should feel cute but not childish, personal but not mascot-only, and expressive without exaggeration.

It should not feel cyberpunk, gaming-oriented, aggressive, luxury-branded or corporate-heavy.

## 3. Geometry

### Selected G_Q direction

The selected direction is the lower-left concept from the first four-way exploration board.

- Use a compact, heavy, rounded geometric construction.
- Give both letters a low visual center and slightly compressed posture.
- Keep G and Q close to the underscore so the three forms read as one sleepy emoticon.
- Preserve a clear G opening and a short low Q tail.
- Let the underscore sit low and nearly bridge the letters without touching them.
- The sleepy-eye feeling must come from weight, proportion and spacing; do not add literal eyelids, hands or motion marks to the static master.
- Keep the mark legible at 24–32 px.

This geometry is implemented in `gqmark-primary.svg`; do not reopen unrelated logo exploration without revising this master.

### Secondary G?

- When used, the question mark should visually belong to the same stroke family as the G.
- The question-mark dot may use the canonical yellow dot.
- Do not replace the dot with a star, spark, power button, AI chip or other pictogram.
- Do not force G and the question mark into a clever monogram if that harms legibility.

### Relationship

- `G_QMark` is the formal name.
- `G_Q` carries the sleepy, calm personality.
- `G?` carries curiosity in highly reduced contexts.
- The yellow dot remains the smallest persistent color signature.

## 4. Color

Canonical palette:

- graphite: `#30343B`
- warm yellow: `#F2C94C`
- warm off-white: `#FFFDF7`
- white: `#FFFFFF`

Default light-background logo:

- G, underscore and Q: graphite
- warm yellow is optional and secondary; it is not required inside the static G_Q master

Dark-background use is secondary. If required, use warm off-white for the main strokes and retain the yellow dot.

## 5. Clear space and minimum size

Use these rules:

- clear space around the mark: at least the stroke width of the G
- minimum compact digital size: 24 px high
- preferred video corner size: 32–64 px high depending on frame size
- do not use the full `G_QMark` wordmark when it becomes visually cramped

## 6. Motion behavior

The approved deterministic animation is `gqmark-motion.svg`.

Preferred `G_Q` reveal sequence:

1. the two rounded letterforms appear with a tiny sleepy rubbing motion
2. the underscore settles into place
3. the motion becomes still and focused
4. optional `G_QMark` wordmark enters for title-card use

Typical duration: about 0.6–1.2 seconds.

Motion should be quiet and clean. Avoid glitch, neon flicker, particle explosions, lens flares or dramatic 3D rotation.

## 7. Allowed variations

Allowed:

- core short mark `G_Q`
- horizontal `G_QMark`
- secondary compact `G?`
- restrained state derivatives such as `G_?`, `G_!` and `G_O` in motion or status contexts
- monochrome one-color fallback
- yellow-dot-only micro accent
- outline or filled implementation if geometry remains consistent

State derivatives never replace the formal identity.

Not allowed without revising this master:

- changing the yellow dot to another recurring accent
- adding an enclosing shield, hexagon, badge or app-icon frame as part of the core logo
- adding gradients as a required identity feature
- adding literal AI, robot, chip or electrical symbols into the core mark

## 8. Approved v1 assets

- `gqmark-primary.svg` — canonical graphite `G_Q`
- `gqmark-reverse.svg` — warm off-white reverse mark
- `gqmark-wordmark.svg` — horizontal formal-name lockup
- `gqmark-motion.svg` — one-shot sleepy rubbing reveal with reduced-motion fallback

The primary mark has been visually checked at large display size and must remain legible at 24 px, 32 px, 64 px and 128 px. The wordmark's text remains font-dependent until a formal typeface is selected and outlined.
