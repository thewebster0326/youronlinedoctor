# Deploying to cPanel via Git Version Control

The repo is **private**, so cPanel needs an SSH deploy key before it can clone.
Steps 1–3 are once-off; after that every deploy is two clicks.

## 1. Get the cPanel account's SSH public key

1. Log into cPanel for `youronlinedoctor.co.za`.
2. Open **SSH Access** → **Manage SSH Keys**.
3. If there is no key listed, click **Generate a New Key** (leave the passphrase
   blank — cPanel's Git tool can't type one), then **Manage** → **Authorize** it.
4. Click **View/Download** next to the **public** key and copy the whole
   `ssh-rsa AAAA...` line.

## 2. Add it to GitHub as a deploy key

1. Go to <https://github.com/thewebster0326/youronlinedoctor/settings/keys>
2. **Add deploy key** → Title: `cPanel`, paste the public key.
3. Leave "Allow write access" **unchecked**. Click **Add key**.

## 3. Clone the repo in cPanel

1. In cPanel, open **Git™ Version Control** → **Create**.
2. Turn **Clone a Repository** ON.
3. **Clone URL:** `git@github.com:thewebster0326/youronlinedoctor.git`
   (the SSH URL — not the https one, or the deploy key won't be used)
4. **Repository Path:** `repositories/youronlinedoctor`
5. **Repository Name:** `youronlinedoctor`
6. Click **Create**. cPanel clones the repo into `~/repositories/youronlinedoctor`.

## 4. Check the deploy path

`.cpanel.yml` copies the site to `$HOME/public_html/`, which is correct when
`youronlinedoctor.co.za` is the **primary** domain on the account.

If it's an **addon** domain, edit `.cpanel.yml` and change the `DEPLOYPATH` line to
that domain's document root — cPanel shows it under **Domains**, usually something like:

```
export DEPLOYPATH=$HOME/youronlinedoctor.co.za/
```

Commit and push that change before deploying.

## 5. Deploy

1. In cPanel, **Git™ Version Control** → the repo's **Manage** button.
2. Open the **Pull or Deploy** tab.
3. Click **Update from Remote**, then **Deploy HEAD Commit**.
4. Visit <https://www.youronlinedoctor.co.za> to confirm the page is live.

For every future change: push to GitHub, then repeat step 5.

## 6. Clear out any host placeholder

If cPanel's own default page still shows, open **File Manager**, go to the
document root and delete any leftover `index.php`, `index.htm` or
`default.html` — the server may be serving those ahead of our `index.html`.

## 7. HTTPS

In cPanel open **SSL/TLS Status**, tick `youronlinedoctor.co.za` and
`www.youronlinedoctor.co.za`, and click **Run AutoSSL** so the site loads over
`https://` without a browser warning.

## 8. Create the info@ mailbox

The page's email link points at an address on the domain. In cPanel open
**Email Accounts** → **Create**, and make the mailbox that matches the address
shown on the page, so enquiries actually land somewhere.
