# Handover for Next Session

Date: 2026-05-03  
Project: Charlotte O'Connor songwriter/singer portfolio and ACM final project submission site  
Current local server: `npm run dev` serving `http://localhost:8080/`

## Original Roadmap Advice vs Current State

The first review in this work session identified that the site needed to serve two functions at once:

1. A professional showcase for Charlotte as a songwriter, singer and recording artist.
2. A clear assessment portfolio for the ACM final project, with Family Business presented as the main/latest project.

The initial roadmap focused on replacing placeholders, strengthening the Family Business project evidence, making Insomnia Club subordinate to the current project, improving CV professionalism, adding live performance evidence, and removing anything that looked like internal notes or unfinished scaffold.

## What Has Been Achieved

- Family Business is now presented as the current central album project.
- A full Family Business album overview has been added.
- Each Family Business track has its own page with final reflective copy, cleaned spelling/punctuation and track-specific collaborator notes.
- The track title is consistently "The Wedding Song" across visible site text.
- Freefall lyrics were added in the corrected lyric flow.
- Girl I Used To Be and Freefall now include optimized 30-second live performance excerpts from 20 April 2026.
- The Gigs page now shows the recent 20 April 2026 Hot Vox show and the next 2 June 2026 headline slot at The Lucky Pig.
- The Insomnia Club page has been reframed as earlier supporting work so it does not eclipse Family Business.
- Insomnia Club now uses individual Spotify embeds per track instead of only linking away to the whole album.
- Family Business mentions on the Insomnia Club page link back to the Family Business page.
- Site-wide email references have been updated to `charlotteoconnormusic@gmail.com`.
- The CV download has been rebuilt as a professional one-page PDF with a matching HTML source.
- Collaborator credits have been added for Josh Croly, Imogen Danbury, Emma Hampton, Ann O'Connor and Mark O'Connor.
- Family Business track artwork sections now use lightweight overlapping Polaroid-style mood boards rather than single underfilled frames.
- Optimized WebP artwork variants have been created for track cards and Polaroid collages.
- Reminder/placeholder copy has been removed from the worked-on pages.
- `npm run build` passes.

## Key Files Changed

- `src/work/family-business/index.njk`
- `src/work/family-business/mind-over-matter/index.njk`
- `src/work/family-business/girl-i-used-to-be/index.njk`
- `src/work/family-business/the-wedding/index.njk`
- `src/work/family-business/freefall/index.njk`
- `src/work/family-business/traffic-lights/index.njk`
- `src/work/album/index.njk`
- `src/gigs/index.njk`
- `src/cv/index.njk`
- `src/_includes/layouts/base.njk`
- `src/assets/css/styles.css`
- `src/assets/cv/charlotte-oconnor-cv.html`
- `src/assets/charlotte-oconnor-cv.pdf`
- `src/assets/video/`
- `src/assets/family-business/collage/`

## Validation Completed

- Ran `npm run build`; Eleventy completed successfully.
- Confirmed the Eleventy dev server rebuilt after content/CSS/asset changes.
- Checked for leftover visible scaffold phrases such as "PDF page image", "placeholder", "reminder", and old artwork reminder text in Family Business pages.
- Optimized new collage artwork assets to roughly 104 KB total.
- Kept performance clips to around 1.1 MB and 1.3 MB.

## Todo for Next Session

- Review Family Business pages visually in browser at desktop and mobile sizes, especially the new Polaroid collage layout.
- Confirm Charlotte is happy with the final proofed wording on all five track pages.
- Add final studio audio links for Family Business tracks when available.
- Replace "Audio and video links will be added when final assets are ready" on tracks that still have no media, once final links/assets exist.
- Check whether the Family Business overview should include more direct ACM assessment language, for example aims, evidence, reflection and process.
- Add any missing evidence artefacts Charlotte wants assessed: lyric drafts, demo excerpts, production notes, collaborator feedback, screenshots or project timeline.
- Confirm whether the live clips should also appear on the Family Business overview, or only on Gigs and individual track pages.
- Review the CV PDF content for any factual gaps, especially phone number, dates, training details and selected achievements.
- Consider adding a short "Project evidence" section to Family Business if the marker needs assessment materials collected in one place.
- Do a final accessibility and responsive polish pass before submission: headings, alt text, button labels, video controls, text contrast and mobile spacing.
- Run a final production build immediately before deployment/submission.

## Notes for Next Codex Session

- Do not let The Insomnia Club visually or narratively overtake Family Business; it is supporting early work.
- Keep Family Business as the first and strongest current-project signal.
- Preserve the current live video optimization approach: short clips, no autoplay, `preload="metadata"`, local posters.
- Preserve the live email: `charlotteoconnormusic@gmail.com`.
- The local CV PDF is generated from `src/assets/cv/charlotte-oconnor-cv.html` using `npm run cv:pdf`.
