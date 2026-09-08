# Topic 13 Checking the design, and planning the work — Slide plan
> **Covers:** Topic 13 — see coverage.md
> **STATUS: DRAFT — redrafted 2026-08-28 from the AT3 practice workbook, Part A tasks 13–18. Teacher
> `notes:` not yet authored. `coverage.md` not yet reconciled.**

## Depth ceiling
Check a design against the review that produced it, then plan the change and the proof. Still on paper
— nothing is built until Topic 14.

**Answer discipline:** these tasks check the student's own design against their own review. The slides
teach how to check; they do not supply the findings.

## Teaching source
Bespoke — ICTCLD502 (documenting a design) plus change-management and planning practice, which the
vendor decks do not cover.

## AWS pin table
None.

## Slides

### Opener
- [BESPOKE] Does it actually do what you said?
  - You have a design. Whether it closes the gap you measured is a separate question, and it is the one your client will ask.
  - Today: check the design against your own review, check it hangs together, then plan how you will apply it and how you will prove it.
  - Everything today is on paper. It is also what makes next topic survivable.
  kicker: check it before you build it
  image: none

### C1 — Checking the design against the review
- Teaches: [ICTCLD502 PC 3.2] · [ICTCLD502 PC 3.3] · [ICTCLD502 PC 3.4]
- Kicker: every row accounted for
- [BESPOKE] Close the loop on every weakness
  - Take the list of weaknesses you produced and account for every one of them — removed by something specific in your design, or knowingly accepted.
  - Copy the list across before you write anything in the other columns. It stops you quietly dropping the awkward ones.
  - If your design removes something that was never on your list, the list was incomplete. Go back and fix it rather than leaving the two documents disagreeing.
  kicker: removed, or accepted — nothing unmentioned
  image: none
- [BESPOKE] Redo the numbers against the design
  - You estimated what the environment achieved. Now estimate what your design achieves, the same way, per component.
  - The point is the difference between the two tables. If you cannot state it in a sentence, the design has not been shown to do anything.
  - Then answer the question that was actually asked: does the whole service now meet the targets? An honest gap beats a number you cannot defend.
  kicker: the difference is the argument
  image: none
- [BESPOKE] What is still constrained
  - Some things your design will not have changed. A component that could only be replaced rather than added to probably still is.
  - What may have changed is what it costs you — the same event, with something else still serving while it happens.
  - Say which, and say what the impact is now.
  kicker: same event, different cost
  image: none
- [EX] Check the design against your review
  - Workbook — tasks 13, 14 and 15.
  - Account for every weakness you listed, re-estimate the recovery numbers against your design, and record what still cannot simply be added to.
  timer: ~35 min
  image: none
  notes:
    Activity = practice workbook tasks 13–15. Watch for weaknesses that quietly vanish between the
    review and this table — that is the thing this task exists to catch.
    Finding a contradiction here is a good outcome; make sure they say so rather than hiding it.
- [TAKEAWAYS] Section 1 · Checking
  - Every weakness is removed or knowingly accepted — none unmentioned.
  - Re-estimate the numbers; the difference between the tables is the argument.
  - Say what is still constrained and what it costs now.
  image: none

### C2 — Does it hang together?
- Teaches: [ICTCLD502 PC 3.5]
- Kicker: read it as one document
- [BESPOKE] Reading your own design cold
  - You wrote the tiers one at a time. Nobody will read them that way.
  - Read the whole thing back in one pass and ask: does every layer have an answer, do the answers agree with each other, and could someone build this without asking you what you meant?
  - Cross-tier contradictions are the common failure — something designed in one tier that another tier never provides for.
  - Finding one now is a good outcome. Finding it while the change window is running is not.
  kicker: could someone else build it?
  image: none
- [EX] Check your design is complete
  - Workbook — task 16.
  - Read tasks 7 to 15 back as one document, note anything that had to change on the read-through, and record what you changed.
  timer: ~15 min
  image: none
  notes:
    Activity = practice workbook task 16. The workbook's considerations name the specific
    cross-references worth checking — let them do that work.
    Pair students and have them try to build from each other's; the questions they have to ask are
    the gaps.
- [TAKEAWAYS] Section 2 · Completeness
  - Read it as one document, not as the tiers you wrote.
  - Contradictions between tiers are the usual failure.
  - Something you had to change on the read-through is worth recording.
  image: none

### C3 — Ordering a change to a live service
- Teaches: [ICTCLD401 FS Planning and organising]
- Kicker: the window is finite
- [BESPOKE] Three ways to put a change in
  - All at once — switch everything over in one go. Quickest, and when it goes wrong it goes wrong everywhere at the same time.
  - A bit at a time — add and change in stages, checking after each one. Slower, but problems surface while they are still small and while you still have somewhere to go back to.
  - Side by side — stand the new one up next to the old one, run both, then switch. Safest fall-back there is, and you pay for two of everything while it lasts.
  - What you are about to plan is the second one. You are adding to a system that keeps serving the whole time, and never taking it down to do it.
  kicker: all at once · in stages · side by side
  image: none
- [BESPOKE] What a change window is
  - You do not get to take a live system down whenever you like. You get an agreed window, and it is shorter than you would like.
  - Organisations have rules for changing a running system — what has to be planned, what has to be approved, and what a rollback plan has to contain. Read them; they are not optional.
  kicker: agreed, and finite
  image: none
- [BESPOKE] Ordering the work
  - Sort your changes into two piles: the ones that add something new, and the ones that alter something already serving traffic.
  - Additive changes affect nobody, so they go first. Anything that interrupts a running service goes later, when everything it depends on is already in place.
  - Anything long-running that proceeds by itself once started should be kicked off early, so it runs while you do something else.
  kicker: additive first, disruptive later
  image: none
- [BESPOKE] What each row of a plan carries
  - For each change: how long you expect it to take, what a user sees while it happens, how you will confirm it worked, and what you will do if it does not.
  - "Keep going and hope" is not a rollback. If you cannot finish the sentence "if this fails I will ___", you do not have a plan for that row.
  - Add the durations up and compare them to the window. If the total is nearly the whole window you have no plan, you have a hope.
  kicker: time · impact · verification · rollback
  image: none
- [EX] Plan the order of work
  - Workbook — task 17.
  - Plan the order you will apply your changes in, with a duration, impact, verification and rollback for each, and state the total and the buffer left.
  timer: ~30 min
  image: none
  notes:
    Activity = practice workbook task 17. Point them at the organisation's change-management page —
    the rollback requirement comes from there, not from the task.
    The two things to press on: a rollback for every row, and actually adding the durations up.
- [TAKEAWAYS] Section 3 · The plan
  - Read the organisation's rules for changing a running system.
  - Additive changes first; disruptive ones later; long-running ones early.
  - Every row carries a duration, an impact, a verification and a rollback.
  - Add it up and check the buffer.
  image: none

### C4 — Planning the proof
- Teaches: [ICTCLD502 PC 4.6]
- Kicker: predict it first
- [BESPOKE] A design is a claim until something tests it
  - Redundancy on paper is an assertion. It becomes a fact when a failure happens and the service keeps serving.
  - You plan at least one failure and one resize — one proves it survives losing something, the other proves growing it does not cost what it used to.
  kicker: assertion, then fact
  image: none
- [BESPOKE] Write down what you expect, before you run it
  - This is the part everyone skips and it is the part that makes the exercise worth anything.
  - If you have not written down what you expect, then whatever happens will look like what you expected, and you will have learned nothing.
  - For each simulation: what you will do, what you expect to happen, and how you will know whether it did. "It worked" is not evidence — name what you would capture, and when.
  - How you will know matters most. Watching the console is not the same as watching the service.
  kicker: predict, then run
  image: none
- [EX] Plan how you will prove it
  - Workbook — task 18.
  - Plan your simulations — at least one failure and one resize — with what you will do, what you expect, and how you will know.
  timer: ~20 min
  image: none
  notes:
    Activity = practice workbook task 18. These plans are executed in Topic 15 and compared against
    what actually happened, so vague predictions cost them later — say so now.
    Press "how will you know" hardest; that is where the measurement discipline starts.
- [TAKEAWAYS] Topic 13 · Key takeaways
  - Account for every weakness; re-estimate and state the difference.
  - Read the design back as one document before anyone builds from it.
  - Order the work additive-first, with a rollback on every row and a real buffer.
  - Write down what you expect before you run anything.
  image: none

### Close
- [BESPOKE] Next — building it
  - The design is checked and the work is planned.
  - Next you deploy the environment and apply your own design to it, in your own order.
  image: none

## Build notes
~18 slides. Four activities, mapping to practice workbook tasks 13–15 · 16 · 17 · 18.
Carries one slide on rollout approaches — not assessed by any task, kept because it names the
reasoning task 17 requires. Load and stress testing is deliberately not taught: nothing asks for it,
and the practice environment serves a placeholder page, so there is no real load to test against.
New topic content — the previous Topic 13 (implementation and simulation) moves to Topics 14 and 15.
No images used yet; the change-window planning section may warrant a diagram. `coverage.md` needs
reconciling — this Topic previously covered AT3 Part B.

## Changelog
- 2026-08-28 — new plan; carries workbook tasks 13–18, which previously had one bullet between them.
