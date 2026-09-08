# Topic 07 Controlling access — Slide plan
> **Covers:** Topic 07 — see coverage.md
> **STATUS: DRAFT — redrafted 2026-08-28 from the AT2 practice run sheet. Teacher `notes:` not yet
> authored. `coverage.md` not yet reconciled.**

## Depth ceiling
Firewall rules between tiers, and the identity model that operates the platform. Configuration only —
no compute yet, so nothing is tested end to end until the tiers exist.

## Teaching source
Bespoke for the tier-chaining discipline and the constrained-environment identity task. AWS-sourced for
security groups (ACF M05, ACA M07) and identity components (ACF M04).

## AWS pin table
ACF M05 S33–S35; ACA M07 S23–S24; ACF M04 (identity components, S31 recorded demo).

## Slides

### Opener
- [BESPOKE] Nothing is allowed yet
  - The network is built, and by default nothing in it may talk to anything else.
  - Today you write the rules that let each tier reach exactly the tier next to it — and no further.
  - Then the identities: who operates this platform after you hand it over, and how a server gets permission to do its job without holding a password.
  kicker: from plumbing to permission
  image: none

### C1 — Rules between tiers
- Teaches: [ICTCLD401 PC 1.7] · [ICTCLD401 KE 9] · [ICTCLD502 PC 1.3]
- Kicker: who may talk to what
- [PRIMER] What a firewall does
  - A firewall filters traffic by rule and decides what is allowed through.
  - Traffic is identified by address and by port — the number that says which service is being asked for.
  - Least privilege: open only the ports the job needs, and only to whoever needs them.
  kicker: address plus port
  image: none
- [BESPOKE] Security groups
  - A security group is a virtual firewall attached to a resource, not to a subnet.
  - It is stateful — allow traffic in and the reply is automatically allowed back out. You do not write a matching outbound rule.
  - It holds allow-rules only. There is no deny rule, because a new group already denies everything inbound until you add one.
  kicker: stateful, allow-only, deny by default
  image: none
- [BESPOKE] Chaining the tiers
  - You can name another security group as the source of a rule, instead of an address range.
  - The rule then follows membership: however many servers the platform launches, and whatever addresses they get, the rule still fits.
  - That is what makes a chain — the entry point accepts the public, the application tier accepts only the entry point, the database accepts only the application tier.
  - Create the groups empty first. Each names another as a source, which you cannot do until it exists.
  kicker: source = a group, not an address
  image: none
- [BESPOKE] Naming things the platform will accept
  - Providers reserve some prefixes for the identifiers they generate themselves.
  - A name that collides with a reserved prefix is rejected outright, with an error that reads as though your rule is wrong when only the name is.
  - Read the constraint in your run sheet before you type the names.
  kicker: read the constraint first
  image: none
- [EX] Build the security-group chain
  - Run sheet — task 7.
  - Create the three groups as empty shells, then add each inbound rule, naming the upstream group as the source rather than an address range.
  timer: ~20 min
  image: none
  notes:
    Activity = practice run sheet task 7. Two predictable stumbles: trying to add rules before all
    three groups exist, and typing an address range where the run sheet says a group.
    Share-back: show the database group's inbound rule and confirm its source is the application group.
- [TAKEAWAYS] Section 1 · Rules between tiers
  - A security group protects one resource, is stateful, and denies by default.
  - Naming another group as the source makes the rule follow the servers.
  - Create the shells first; the chain cannot be written in one pass.
  image: none

### C2 — Who operates the platform
- Teaches: [ICTCLD401 PC 1.5] · [ICTCLD401 PC 2.1] · [ICTCLD401 KE 8]
- Kicker: identity, and its boundary
- [BESPOKE] The four identity components
  - User — one identity per person or application that signs in.
  - Group — a collection of users who need the same permissions, so you set them once.
  - Role — permissions with no permanent credentials, assumed temporarily by a person or a service.
  - Policy — the document that says what is allowed. Everything is denied until a policy grants it.
  kicker: people, and permissions
  image: reuse 06-iam-components.png
- [BESPOKE] Securing access
  - Attach policies to groups and put users in them, rather than attaching policies to individuals.
  - Grant only what the job needs — you widen a permission when a task proves it necessary, not in advance.
  - Protect the account's founding identity and use it only when nothing else will do.
  - Use roles for services, never long-lived keys.
  kicker: set once, granted narrowly
  image: none
- [BESPOKE] Why the operators cannot change identity
  - The group that runs the platform gets read access to everything and no ability to change permissions — including its own.
  - A group that can rewrite its own permissions has no boundary at all; it can grant itself anything.
  - So operations sit with the team that runs the system, and identity stays with whoever governs the account. That separation is the control.
  kicker: the boundary is the point
  image: none
- [BESPOKE] When the environment refuses you
  - Some environments will not permit identities to be created at all. Yours is one of them.
  - You will complete the form correctly and be refused. That refusal is the evidence.
  - Filling the form correctly is the part worth practising — and a constraint you name and evidence is a professional result, not a failure.
  kicker: the refusal is the capture
  image: none
- [EX] Configure the access model
  - Run sheet — task 8.
  - Complete the group form and the user form with the values your run sheet gives, submit each, and capture the completed form together with the error it returns.
  timer: ~20 min
  image: none
  notes:
    Activity = practice run sheet task 8. Tell them up front they will be refused, so nobody spends
    the session hunting a fault. Both captures must show the completed form *and* the error.
- [TAKEAWAYS] Section 2 · Identity
  - Users and groups are people; roles and policies are permissions.
  - Policies go on groups; grant narrowly; protect the founding identity.
  - Whoever operates a platform should not be able to widen their own access.
  image: none

### C3 — Identity for a server
- Teaches: [ICTCLD401 PC 1.6] · [ICTCLD401 PC 1.7]
- Kicker: permission without a password
- [BESPOKE] How a server gets permission
  - A server needs to reach other services — storage, logging — and it needs permission to do it.
  - It assumes a role: temporary credentials, issued automatically, rotated for you.
  - Nothing is stored on the server. There is no key on disk to find, copy or leak.
  - You attach the role when you define the server, not afterwards by hand.
  kicker: nothing stored on the box
  image: none
- [BESPOKE] Reading a role you did not write
  - Open a role and read its attached policies to see what it actually permits.
  - This is a routine professional move: you inherit roles far more often than you author them, and you are accountable for what they allow.
  - Your environment supplies the role your servers will use. Read it, and write its name down — the next task asks for it.
  kicker: inherit it, then read it
  image: none
- [EX] Review the role your servers will use
  - Run sheet — task 9.
  - Open the role your run sheet names, read which services its policies grant access to, capture it, and note the name exactly as shown.
  timer: ~10 min
  image: none
  notes:
    Activity = practice run sheet task 9. A read, not a build — say so, or they will hunt for a create
    button they do not have. The name matters: the launch template task asks for it verbatim.
- [TAKEAWAYS] Section 3 · Identity for a server
  - A server assumes a role; no credentials are stored on it.
  - Roles are attached when the server is defined.
  - Reading an inherited role's permissions is part of the job.
  image: none

### Close
- [BESPOKE] Next — the application tier
  - The network is built and the rules are written. Nothing is running in it yet.
  - Next: defining a server once, putting a load balancer in front, and letting the platform manage how many there are.
  image: none

## Build notes
~17 slides. Three activities, mapping to practice run sheet tasks 7 · 8 · 9.
Assets: `06-iam-components.png` moves in from `topic_06/images/`. `coverage.md` needs reconciling —
this Topic now owns the identity components that previously sat in Topic 6.

## Changelog
- 2026-08-28 — redrafted from the AT2 practice run sheet; identity moved here from Topic 6 to match
  run-sheet order (tasks 8–9 follow the security groups, not the network).
