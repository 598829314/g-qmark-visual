# G_QMark Identity Master

Status: provisional specification, no artwork approved yet.

This file defines the non-image rules for the G_QMark identity mark. A generated or manually drawn logo does not become canonical until it is explicitly approved and placed in this directory as a master asset.

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

### G_Q

- Keep the horizontal `G_Q` reading stable and immediately legible.
- Use a simple rounded geometric sans-serif construction.
- The circular structures of `G` and `Q` may be emphasized just enough to suggest sleepy eyes.
- Preserve the underscore; it is part of the face-like reading.
- Avoid exaggerated facial distortion, decorative cuts, speed lines, circuitry or pseudo-tech details.
- Keep counters and spacing open enough to remain legible at 24–32 px.

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

- G and question-mark stem: graphite
- question-mark dot: warm yellow

Dark-background use is secondary. If required, use warm off-white for the main strokes and retain the yellow dot.

## 5. Clear space and minimum size

Until a vector master is approved, use these working rules:

- clear space around the mark: at least the diameter of the yellow dot
- minimum compact digital size: 24 px high
- preferred video corner size: 32–64 px high depending on frame size
- do not use the full `G_QMark` wordmark when it becomes visually cramped

## 6. Motion behavior

The mark should support a short deterministic SVG/HTML animation.

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

## 8. Approval targets

Before this identity becomes final, approve at least:

- `gqmark-primary.svg` for `G_Q`
- `gqmark-wordmark.svg` for `G_QMark`
- `gqmark-compact.svg` for the optional `G?` derivative
- `gqmark-mono.svg`
- `gqmark-motion.svg` or equivalent motion source

Test the compact mark at 24 px, 32 px, 64 px and 128 px.
