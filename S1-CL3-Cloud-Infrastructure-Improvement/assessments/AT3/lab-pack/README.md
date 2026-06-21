# AT3 — Deploy the Ledgerline environment and apply the improvement

This guide walks you, step by step, through building the **starting environment** for AT3 and then
**applying the approved improvement** to it. You do this in your own AWS Academy lab.

**What you are doing:**
1. Deploy the **existing-state** Ledgerline infrastructure (`baseline.yaml`) — a single-AZ environment.
2. Apply the **approved improvement** (`improved.yaml`) to that same environment as a change-set.
3. (Optional) Deploy the small **India residency** stack (`india-residency.yaml`) in the Mumbai region.

**You will need:**
- Your AWS Academy login.
- The files **`baseline.yaml`** and **`improved.yaml`** (download them from your AT3 assessment page).
- A database password you choose (at least 8 characters) — **write it down**.
- About **30 minutes** (the SQL Server database is the slow part to build).

> **Note about reaching the system.** Ledgerline is an **internal** system — in real life staff reach
> it over a private VPN, not the public internet. In the lab there is no VPN, so you will **not** open
> the application in a browser. Instead you confirm everything is working from the **AWS console**
> (stack status, healthy targets, database status). That is normal and expected for this system.

> **Note about the database edition.** In the real system Ledgerline runs on **SQL Server Standard**. The
> lab deploys **SQL Server Express** (free) in its place — the lab database is empty, so it behaves the same
> for what you do here. This is a lab substitution only; it does not change the design you are implementing.

---

## Part 1 — Open the AWS sandbox

1. Log in to **AWS Academy** (the Canvas site your teacher gave you).
2. On your **Dashboard**, open the **AWS Academy Cloud Architecting** course.
3. On the left menu click **Modules**, scroll to **Sandbox**, and click the **Sandbox environment**.
4. On the lab page, click **Start Lab**. Wait for the dot next to **AWS** to turn **green**.
5. Click the green **AWS** dot — the AWS Management Console opens in a new tab.

## Part 2 — Choose the correct region

6. At the **top-right** of the console, click the region name and choose **Asia Pacific (Sydney)**.

> Do this **before** the next part. The main system is built in Sydney.

## Part 3 — Build the baseline (existing state)

7. In the search bar type **CloudFormation** and open it.
8. Click **Create stack** → **With new resources**.
9. **Template source** → **Upload a template file** → **Choose file** → select **`baseline.yaml`** → **Next**.
10. On the next page:
    - **Stack name:** `ledgerline-baseline`
    - **DBMasterPassword:** type a password (8+ characters) and **write it down**.
    - Leave everything else as it is → **Next**.
11. **Configure stack options** → leave as is → **Next**.
12. **Review** → scroll down → **Submit**.
13. **Wait about 15 minutes.** When the stack shows **CREATE_COMPLETE** (green), it is ready.

## Part 4 — Check the baseline worked (from the console)

14. **Stack built?** The `ledgerline-baseline` stack shows **CREATE_COMPLETE**.
15. **App tier healthy?** Search **EC2** → **Target Groups** → click `ledgerline-...` → **Targets** tab.
    You should see the instance with status **healthy** (give it a few minutes after the stack finishes).
16. **Database up?** Search **RDS** → **Databases** → `ledgerline-prod` shows status **Available**, and
    (importantly) **Multi-AZ = No** — Ledgerline runs as a single instance.

If those three are good, your baseline is up.

## Part 5 — Apply the approved improvement (change-set)

You now apply the approved improvement **to the same stack**, so nothing is rebuilt from scratch.

17. Go back to **CloudFormation** → click the **`ledgerline-baseline`** stack → **Update** (top right).
18. Choose **Replace existing template** → **Upload a template file** → select **`improved.yaml`** → **Next**.
19. Keep the **same parameter values** as before (including the **same DBMasterPassword**) → **Next** → **Next**.
20. On the **Review** page, scroll to the bottom and look at the **Change set preview**. You should see
    **Modify** actions (no **Replace**) — the improvement is applied in place. Click **Submit**.
21. **Wait** for **UPDATE_COMPLETE** (green). This is quicker than the first build.

## Part 6 — Check the improvement applied

22. **App tier now Multi-AZ?** EC2 → **Auto Scaling groups** → `ledgerline-app-prod` → **Instance management**.
    You should now see **two** instances, in **two different Availability Zones** (e.g. `ap-southeast-2a`
    and `ap-southeast-2b`). The application tier can now survive an AZ failure.
23. **Database unchanged?** RDS → `ledgerline-prod` is still **Available** and **Multi-AZ = No**.
    That is correct — the improvement does **not** touch the database. Ledgerline does not support a Multi-AZ
    database; its reliability comes from the automated backups and point-in-time restore already in place at
    the baseline, not from failover.

## Part 7 — (Optional) India residency slice

If your assessment asks you to deploy the India residency slice:

24. At the **top-right**, change the region to **Asia Pacific (Mumbai)**.
25. **CloudFormation** → **Create stack** → upload **`india-residency.yaml`** → stack name
    `ledgerline-india` → **Submit**. It builds two storage buckets and finishes in a minute or two.
26. Switch the region **back to Sydney** when you are done.

## Part 8 — Clean up (always do this at the end)

27. **CloudFormation** (Sydney) → select **`ledgerline-baseline`** → **Delete** → confirm. Wait for it to disappear.
28. If you deployed the India stack: switch to **Mumbai** → delete **`ledgerline-india`** too.
29. Back on the lab tab, click **End Lab**.

---

## If something goes wrong

- **Stack says ROLLBACK or FAILED:** open the **Events** tab, find the first red **CREATE_FAILED** /
  **UPDATE_FAILED** row — its **Status reason** says what happened. Tell your teacher what it says.
- **The change-set preview shows "Replace" instead of "Modify":** stop and check you used the **same**
  parameter values (especially the password and the database settings) as the baseline. A changed
  database setting can force a replacement.
- **Target shows unhealthy:** wait a few minutes after the stack finishes — the web server takes a
  moment to start. If it stays unhealthy, delete the stack (Part 8) and redeploy.
