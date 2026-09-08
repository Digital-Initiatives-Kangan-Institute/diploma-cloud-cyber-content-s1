# Topic 09 The data tier and knowing when it breaks — Slide plan
> **Covers:** Topic 09 — see coverage.md
> **STATUS: DRAFT — redrafted 2026-08-28 from the AT2 practice run sheet. Teacher `notes:` not yet
> authored. `coverage.md` not yet reconciled.**

## Depth ceiling
Provision a managed relational database into the private tier, and stand up baseline alarms.
Single-zone, no standby — the availability options are named and deferred to AT3.

## Teaching source
AWS-sourced for the managed database service and the monitoring service (ACF M08, ACA M06, ACA M10
monitoring). Bespoke for the empty-instance boundary and alarm design.

## AWS pin table
ACF M08 S6–S29, S22 (recorded demo); ACA M06 S37 (backups demo); ACA M10 S9–S12.

## Slides

### Opener
- [BESPOKE] Somewhere to keep it
  - The application tier runs and scales, and stores nothing that survives a server being replaced.
  - Today: a managed database in the private tier, and the alarms that tell you when something has stopped working.
  - The run sheet's second decision is here, and it is asked the same way as the first.
  kicker: data, and knowing about it
  image: none

### C1 — A managed relational database
- Teaches: [ICTCLD401 PC 2.5] · [ICTCLD401 PC 1.1] · [ICTCLD401 PC 1.3] · [ICTCLD401 PE 2] · [ICTCLD401 KE 6]
- Kicker: someone has to run it
- [PRIMER] Relational databases, and who operates them
  - A relational database stores structured data in tables and is queried with SQL.
  - Somebody has to install and patch it, take and test backups, secure it and scale it. That work never disappears — the only question is who does it.
  kicker: the work does not go away
  image: none
- [BESPOKE] Self-hosted or managed
  - Self-hosted — you run the engine on your own server. Complete control of the engine and the operating system, and all of the operational work is yours.
  - Managed — the provider installs, patches, backs up and scales it. You keep the schema, the data and the query performance.
  - Control against effort. Choose managed unless you genuinely need engine-level control.
  kicker: control, or effort
  image: none
- [BESPOKE] The managed database service
  - Two dials size it: an instance class for processing and memory, and storage.
  - It runs inside your own private network, in the subnets you allow it, reachable only from where your rules permit — not on the public internet.
  - Automated backups let you restore to a point in time; encryption at rest is a setting you turn on at creation.
  - A standby in a second zone is available and deliberately off here. That is the AT3 work.
  kicker: class · storage · private · backed up
  image: none
- [BESPOKE] Telling the service where it may live
  - Before you can create the database you have to give the service a subnet group — the set of subnets it is permitted to use.
  - Like the load balancer, it will not accept subnets in a single zone.
  - This is the second time that constraint has shaped your network. It is why the empty subnets exist.
  kicker: the second two-zone requirement
  image: none
- [BESPOKE] You deliver an empty database
  - You provision the container, correctly configured. You do not load the schema or the data.
  - That is the customer's data and the customer's responsibility, and moving it is a separate piece of work with its own risks.
  - An empty, correctly configured, private, encrypted, backed-up instance is the finished deliverable.
  kicker: the container, not the contents
  image: none
- [EX] Create the subnet group and the database
  - Run sheet — tasks 14 and 15.
  - Create the subnet group, then create the database to the settings your run sheet gives — private, encrypted, with its backups configured and no standby.
  - Make the sizing decision the same way as last topic: choose, name what you rejected, justify it against this workload.
  timer: ~30 min
  image: none
  notes:
    Activity = practice run sheet tasks 14–15, including the decision box. The subnet group lives in
    the database console, not the network console — most people go looking in the wrong place.
    Push them off the simplified creation path; it silently makes four of the specified choices for them.
    The database takes several minutes to become available — start the alarms task while it builds.
- [TAKEAWAYS] Section 1 · The data tier
  - Managed shifts the operational work; the schema and data stay yours.
  - It lives in your private network, and the subnet group is what puts it there.
  - Encryption and backups are set at creation; the standby is deferred.
  - You hand over an empty instance.
  image: none

### C2 — Knowing when it breaks
- Teaches: [ICTCLD502 PC 4.3] · [ICTCLD401 KE 5]
- Kicker: find out before your users do
- [PRIMER] Metric, alarm, log
  - A metric is a measurement taken over time.
  - An alarm is a rule watching a metric, which fires when a threshold is crossed.
  - A log is a record of events — what happened, and when.
  - You monitor so that you find out before your users do.
  kicker: the number, the rule, the diary
  image: reuse 09-cloudwatch.png
- [BESPOKE] What an alarm is actually made of
  - A threshold on its own is not an alarm. It takes five things:
    - the metric · the statistic (maximum, minimum, average) · the period · the threshold · how many periods must breach before it fires
  - Choose the statistic to match the question. "Is anything unhealthy?" wants a maximum; "are we running out of room?" wants a minimum.
  - The count of breaching periods is what stops a single momentary spike waking someone up.
  kicker: five parts, not one
  image: none
- [BESPOKE] Finding the right metric
  - Metrics are grouped by dimension, and services often publish several similar-looking groupings.
  - Picking the wrong grouping gives you an alarm that never fires, and looks correct while it does not.
  - Read what the run sheet names carefully, and confirm the row you tick is the resource you built.
  kicker: a wrong grouping never fires
  image: none
- [BESPOKE] Units are not what the graph shows
  - Some thresholds are entered in raw units — bytes, seconds — while the graph above the field is drawn in something friendlier.
  - It is very easy to type a number a thousand times too small and see nothing wrong.
  - Work the arithmetic out deliberately, write it down, and sanity-check it against the graph.
  kicker: do the arithmetic on purpose
  image: none
- [EX] Create the baseline alarms
  - Run sheet — task 16.
  - Create the alarms your run sheet specifies, each with its metric, statistic, period, threshold and breach count, and a notification destination.
  timer: ~25 min
  image: none
  notes:
    Activity = practice run sheet task 16. The storage threshold is the one that goes wrong — it is
    entered in bytes while the graph is drawn in gigabytes. Have them show their working.
    A new alarm sits in an insufficient-data state for a few minutes; that is normal, not a fault.
- [TAKEAWAYS] Section 2 · Monitoring
  - Metric, alarm and log are three different things.
  - An alarm is metric + statistic + period + threshold + breach count.
  - The wrong metric grouping produces an alarm that never fires.
  - Check the units against the field, not the graph.
  image: none

### C3 — Who secures what
- Teaches: [ICTCLD401 PC 1.2] · [ICTCLD401 KE 7]
- Kicker: the line through your own build
- [BESPOKE] The shared responsibility model
  - The provider secures the cloud: the facilities, the hardware, the network underneath it all.
  - You secure what you put in it: the operating system, the configuration, the access rules, and your data.
  - Knowing exactly where the line falls tells you what you must configure and what you can rely on. That is the whole practical value of it.
  kicker: security of the cloud, security in it
  image: reuse 06-shared-responsibility.png
- [BESPOKE] The line moves with the service
  - Run software yourself on a server and you own more of it — the operating system, the patching, the configuration.
  - Use a managed service and the provider takes the engine, the host and the maintenance. You keep the data and who may reach it.
  - So the same piece of software has a different owner depending on how you chose to run it. That choice is the one you made in this topic.
  kicker: more managed, more on the provider
  image: none
- [BESPOKE] What never moves
  - Responsibility for the data itself never transfers, under any service model, to any provider.
  - Neither does deciding who may reach it. A managed database still leaves the access rules and the connection permissions entirely yours.
  - This is where the model is most often got wrong: "it's managed" gets read as "it's theirs".
  kicker: the data is always yours
  image: none
- [EX] Assign the security responsibilities
  - Run sheet — task 17.
  - Work through your build component by component and record who secures each part and what that actually involves — then say which responsibilities the managed database moved, and which it did not.
  timer: ~25 min
  image: none
  notes:
    Activity = practice run sheet task 17. The two rows that decide the result are the database (a split,
    not a handover) and the data (never the provider's). Press anyone who writes the database off as
    "AWS's responsibility".
    Answers must name their own resources — this is about the thing they built, not the model in general.
- [TAKEAWAYS] Section 3 · Who secures what
  - The provider secures the cloud; you secure what you put in it.
  - The line moves with how managed the service is.
  - The data, and who may reach it, never move.
  image: none

### Close
- [BESPOKE] Next — proving it works
  - Everything on the run sheet is now built, and you have said who is responsible for securing it.
  - Next: test every path, prove the isolation, make it scale in front of you, and hand it over.
  image: none

## Build notes
~15 slides. Two activities, mapping to practice run sheet tasks 14–15 · 16.
`09-cloudwatch.png` already in `topic_09/`. `coverage.md` needs reconciling — this Topic now owns the
data tier (previously Topic 8b) and drops the validation/justification components (validation moves to
Topic 10; justification is now taught at the two decision points in Topics 8 and 9).

## Changelog
- 2026-08-28 — redrafted from the AT2 practice run sheet; data tier moved here from Topic 8b,
  monitoring reduced to what task 16 actually asks for.
