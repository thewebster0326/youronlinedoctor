# Deploying to cPanel via Git Version Control

Steps 1–3 are once-off. After that, every deploy is two clicks.

> **Prerequisite:** the GitHub repo must be **public**, so cPanel can clone it over
> https with no key. Check at
> <https://github.com/thewebster0326/youronlinedoctor> — if it shows "Private",
> go to Settings → Danger Zone → Change visibility → Make public.
> (If you'd rather keep it private, see "Private repo" at the bottom.)

## 1. Clone the repo into cPanel

1. In cPanel, search for and open **Git™ Version Control**.
2. Click **Create**.
3. Turn **Clone a Repository** ON.
4. **Clone URL:**
   ```
   https://github.com/thewebster0326/youronlinedoctor.git
   ```
5. **Repository Path:** `repositories/youronlinedoctor`
6. **Repository Name:** `youronlinedoctor`
7. Click **Create**. cPanel clones into `~/repositories/youronlinedoctor`.

## 2. Check the deploy path

`.cpanel.yml` copies the site to `$HOME/public_html/` — correct when
`youronlinedoctor.co.za` is the **primary** domain on the account.

If it's an **addon** domain, look under cPanel → **Domains** for its document root,
then edit the `DEPLOYPATH` line in `.cpanel.yml` to match, e.g.

```
export DEPLOYPATH=$HOME/youronlinedoctor.co.za/
```

Commit and push that change to GitHub before deploying.

## 3. Deploy

1. **Git™ Version Control** → the repo's **Manage** button.
2. Open the **Pull or Deploy** tab.
3. Click **Update from Remote**.
4. Click **Deploy HEAD Commit**.
5. Visit <https://www.youronlinedoctor.co.za> to confirm the page is live.

Every future change: push to GitHub, then repeat step 3.

## 4. Clear out any host placeholder

If cPanel's default page still shows, open **File Manager**, go to the document
root and delete any leftover `index.php`, `index.htm` or `default.html` — the
server serves those ahead of our `index.html`.

## 5. HTTPS

cPanel → **SSL/TLS Status** → tick `youronlinedoctor.co.za` and
`www.youronlinedoctor.co.za` → **Run AutoSSL**, so the site loads over `https://`
without a browser warning.

## 6. Create the info@ mailbox

The page links to `info@youronlinedoctor.co.za`. cPanel → **Email Accounts** →
**Create** → username `info` → set a password, so enquiries land somewhere real.

---

## Private repo (alternative to making it public)

If the repo stays private, cPanel needs a read-only SSH deploy key:

1. cPanel → **SSH Access** → **Manage SSH Keys**. If no key exists, **Generate a
   New Key** with a blank passphrase, then **Manage** → **Authorize** it.
2. **View/Download** the *public* key and copy the whole `ssh-rsa AAAA...` line.
3. <https://github.com/thewebster0326/youronlinedoctor/settings/keys> →
   **Add deploy key** → title `cPanel`, paste it, leave write access unchecked.
4. In step 1 above, use the SSH clone URL instead:
   `git@github.com:thewebster0326/youronlinedoctor.git`
