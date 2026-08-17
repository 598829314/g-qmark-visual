# G? Identity Master

Status: provisional specification, no artwork approved yet.

This file defines the non-image rules for the G_QMark identity mark. A generated or manually drawn logo does not become canonical until it is explicitly approved and placed in this directory as a master asset.

## 1. Identity structure

The system has three levels:

1. `G?` — primary compact mark for avatar, video corner mark, motion reveal and watermark.
2. `G_QMark` — wordmark for repository, title cards and larger identity placements.
3. yellow dot — micro-signature that can appear independently as a recurring visual cue.

`G?` is the primary recognition unit. `G_QMark` supports it; the wordmark should not replace the compact mark everywhere.

## 2. Visual character

The mark should feel:

- bright
- calm
- rounded
- friendly
- precise
- lightly playful

It should not feel cyberpunk, gaming-oriented, aggressive, luxury-branded or corporate-heavy.

## 3. Geometry

### G

- Use a simple geometric sans-serif construction.
- Prefer rounded terminals over sharp cuts.
- Keep the counter open enough to remain legible at 24–32 px.
- Avoid decorative cuts, speed lines, circuitry or pseudo-tech details.

### Question mark

- The question mark should visually belong to the same stroke family as the G.
- It may sit close to the G or partially share visual rhythm with it, but should remain readable as `?`.
- The question mark dot is the canonical yellow dot.
- Do not replace the dot with a star, spark, power button, AI chip or other pictogram.

### Relationship

- `G` is the stable identity component.
- `?` carries curiosity, inquiry and exploration.
- The yellow dot is the smallest persistent signature.

Do not force the G and question mark into one clever monogram if that harms legibility.

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

Preferred reveal sequence:

1. yellow dot appears
2. question-mark curve/stem resolves
3. G draws or fades in
4. optional `G_QMark` wordmark enters for title-card use

Typical duration: about 0.6–1.2 seconds.

Motion should be quiet and clean. Avoid glitch, neon flicker, particle explosions, lens flares or dramatic 3D rotation.

## 7. Allowed variations

Allowed:

- compact `G?`
- horizontal `G_QMark`
- monochrome one-color fallback
- yellow-dot-only micro accent
- outline or filled implementation if geometry remains consistent

Not allowed without revising this master:

- changing the yellow dot to another recurring accent
- adding an enclosing shield, hexagon, badge or app-icon frame as part of the core logo
- adding gradients as a required identity feature
- adding literal AI, robot, chip or electrical symbols into the core mark

## 8. Approval targets

Before this identity becomes final, approve at least:

- `gqmark-primary.svg`
- `gqmark-compact.svg`
- `gqmark-wordmark.svg`
- `gqmark-mono.svg`
- `gqmark-motion.svg` or equivalent motion source

Test the compact mark at 24 px, 32 px, 64 px and 128 px.
