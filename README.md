# Your Online Dr — youronlinedoctor.co.za

Under-construction holding page for **Your Online Dr** (`www.youronlinedoctor.co.za`).

Plain static HTML + CSS. No build step, no framework, no JavaScript.

## Files

```
index.html      the holding page
styles.css      all styling
robots.txt      allows indexing
assets/logo.png the gold-on-black logo
.cpanel.yml     cPanel Git Version Control deployment script
```

## Preview locally

```bash
python -m http.server 4177 --directory .
```

Then open http://localhost:4177

## Editing contact details

Phone number, WhatsApp link and email address all live in `index.html` — search for
`tel:`, `wa.me/` and `mailto:`. There are two places the phone appears (the Call
button and the text line beneath the buttons) and two for the email.

## Deploying

See [DEPLOY.md](DEPLOY.md).
