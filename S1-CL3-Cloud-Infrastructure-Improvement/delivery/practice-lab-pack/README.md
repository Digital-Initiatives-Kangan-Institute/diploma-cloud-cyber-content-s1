# Practice lab-pack — deploy the Website baseline, then apply your own improvement

This is the **practice** counterpart to the AT3 assessment lab-pack. You use it to rehearse the
deploy-and-improve exercise on the **YAT public website** before you do the assessed version on the
assessed system. It is **not assessed** — if a deploy hiccups, working it out is good practice.

**What you are doing:**
1. Deploy the **existing-state** website infrastructure (`baseline.yaml`) — a single-AZ environment.
2. Apply **your own approved improvement** to that same stack as a CloudFormation change-set — the one
   you designed and wrote in the practice design + team-build exercises.

There is **no provided "improved" template here** (unlike the assessment): the improvement is *yours*.

**You will need:**
- Your AWS Academy login.
- `baseline.yaml` (in this folder).
- A database password you choose (8+ characters) — **write it down**.
- ~20 minutes.

> **Region substitution.** The website is designed for Sydney, but the Learner Lab only offers
> `us-east-1`, so that is where you deploy. Wherever you see the notation, the left side is the real
> design region and the right side is where you actually deploy:
> `[scenario: ap-southeast-2 (Sydney) | deploy: us-east-1]`.

> **This one IS public.** The website is internet-facing, so the baseline's `SiteUrl` output opens in
> a browser and shows the placeholder page. Your assessed system is staff-facing, which changes what
> the security and availability arguments have to answer for.

## Steps

1. Start the **AWS Academy Learner Lab**, open the console, confirm the region is **`us-east-1`**.
2. **CloudFormation → Create stack → Upload** `baseline.yaml`. Stack name `yat-website-baseline`;
   set **DBMasterPassword** (8+ chars, write it down); **Submit**. Wait for **CREATE_COMPLETE** (~15 min).
3. **Check it worked:** the `SiteUrl` output opens the placeholder page; **EC2 → Target Groups** shows a
   **healthy** target; **RDS** shows the MySQL instance **Available** with **Multi-AZ = No** (this is the
   single-AZ *before*).
4. **Apply your improvement:** select the stack → **Update** → **Replace existing template** → upload
   **your own** improved template → check the **change-set preview** shows the changes you intend →
   **Submit**. Confirm the result, then **delete the stack** for a clean teardown.

## Notes

- The improvement is **open**. Whether you make the database Multi-AZ is **your** design call —
  justify it on the goals and the cost. Two students can reach opposite verdicts and both be right,
  if both argued.
- **Modelled on the assessment's AT3 baseline** — same structure and substitution patterns, adapted
  for a public, internet-facing site. cfn-lint clean; not lab-proven (practice artefact).
