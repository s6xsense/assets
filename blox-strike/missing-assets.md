# Missing BloxStrike assets

## Migration status

- Available originals: **419 files** uploaded to `s6xsense/assets`, branch `main`, under `blox-strike/`; all 419 public raw downloads matched original SHA-256 hashes.
- Unavailable originals: **63 skybox face images**, listed below. Original Litterbox requests returned HTTP 403 locally and HTTP 404 from a GitHub-hosted runner on 2026-11-11. The exact reason for their unavailability is unknown.
- Another **6 skybox faces** had empty URLs in the original visual companion; these are listed separately.
- User decision: retain incomplete presets unchanged. Do not remove presets, substitute images, or fall back to Catbox/File Garden. Missing files have not been uploaded; their GitHub target paths remain unavailable.
- Runtime fetch root: `https://raw.githubusercontent.com/s6xsense/assets/main/blox-strike/`.
- Executor cache root: `sixsense/blox-strike/`. Existing `Archived/` cache files are left untouched and are not used by the migrated loaders.
- Paimon (53 frames), hitsounds (50 files), and hit vignette (1 file) were all recovered. The uploaded skybox inventory contains 315 face images.

## Unavailable original downloads

Paths are relative to the asset repository's `blox-strike/` directory. These same relative paths are used below the executor cache root. Face keys: `bk` back, `dn` bottom, `ft` front, `lf` left, `rt` right, `up` top.

| Missing target file | Original source URL |
| --- | --- |
| `skybox/Goodnight/dn.png` | https://litter.catbox.moe/q0dxd0.png |
| `skybox/Goodnight/ft.png` | https://litter.catbox.moe/2m8bh0.png |
| `skybox/Goodnight/lf.png` | https://litter.catbox.moe/agfl71.png |
| `skybox/Goodnight/rt.png` | https://litter.catbox.moe/832hrc.png |
| `skybox/Goodnight/up.png` | https://litter.catbox.moe/vo7dbe.png |
| `skybox/Hades/bk.png` | https://litter.catbox.moe/b26c5b.png |
| `skybox/Hades/dn.png` | https://litter.catbox.moe/puhrtm.png |
| `skybox/Hades/ft.png` | https://litter.catbox.moe/le4uur.png |
| `skybox/Hades/lf.png` | https://litter.catbox.moe/35lxic.png |
| `skybox/Hades/rt.png` | https://litter.catbox.moe/wcdcr0.png |
| `skybox/Hades/up.png` | https://litter.catbox.moe/4zwpda.png |
| `skybox/Hazy/bk.png` | https://litter.catbox.moe/qef0yo.png |
| `skybox/Hazy/dn.png` | https://litter.catbox.moe/4k1vil.png |
| `skybox/Hazy/ft.png` | https://litter.catbox.moe/m7dp1v.png |
| `skybox/Hazy/lf.png` | https://litter.catbox.moe/61od45.png |
| `skybox/Hazy/rt.png` | https://litter.catbox.moe/ipcsiq.png |
| `skybox/Hazy/up.png` | https://litter.catbox.moe/712jip.png |
| `skybox/Light Blue/bk.png` | https://litter.catbox.moe/9lz6rb.png |
| `skybox/Light Blue/dn.png` | https://litter.catbox.moe/qg3tf7.png |
| `skybox/Light Blue/ft.png` | https://litter.catbox.moe/f62sw8.png |
| `skybox/Light Blue/lf.png` | https://litter.catbox.moe/ye7294.png |
| `skybox/Light Blue/rt.png` | https://litter.catbox.moe/qddfio.png |
| `skybox/Light Blue/up.png` | https://litter.catbox.moe/ljp1qa.png |
| `skybox/Light Pink/bk.png` | https://litter.catbox.moe/2j6j8r.png |
| `skybox/Light Pink/dn.png` | https://litter.catbox.moe/0h3pb2.png |
| `skybox/Light Pink/ft.png` | https://litter.catbox.moe/3pskdd.png |
| `skybox/Moonlight/bk.png` | https://litter.catbox.moe/n1sra2.png |
| `skybox/Moonlight/dn.png` | https://litter.catbox.moe/7v2lc0.png |
| `skybox/Moonlight/ft.png` | https://litter.catbox.moe/pz4lik.png |
| `skybox/Moonlight/lf.png` | https://litter.catbox.moe/64uqq9.png |
| `skybox/Moonlight/rt.png` | https://litter.catbox.moe/ip7at9.png |
| `skybox/Moonlight/up.png` | https://litter.catbox.moe/ovs88h.png |
| `skybox/Neon Sky 2/bk.png` | https://litter.catbox.moe/6g55mp.png |
| `skybox/Neon Sky 2/dn.png` | https://litter.catbox.moe/og36j4.png |
| `skybox/Neon Sky 2/ft.png` | https://litter.catbox.moe/of5kte.png |
| `skybox/Neon Sky 2/lf.png` | https://litter.catbox.moe/dzab2x.png |
| `skybox/Neon Sky 2/rt.png` | https://litter.catbox.moe/bekc0t.png |
| `skybox/Neon Sky 2/up.png` | https://litter.catbox.moe/etxq7z.png |
| `skybox/Neon Sky/bk.png` | https://litter.catbox.moe/qonxeb.png |
| `skybox/Neon Sky/dn.png` | https://litter.catbox.moe/umld6a.png |
| `skybox/Neon Sky/ft.png` | https://litter.catbox.moe/fnh5nz.png |
| `skybox/Neon Sky/lf.png` | https://litter.catbox.moe/c59xxk.png |
| `skybox/Neon Sky/rt.png` | https://litter.catbox.moe/nomifx.png |
| `skybox/Neon Sky/up.png` | https://litter.catbox.moe/wp7xfo.png |
| `skybox/Night Sky With Moon/bk.png` | https://litter.catbox.moe/ex5rdd.png |
| `skybox/Night Sky With Moon/dn.png` | https://litter.catbox.moe/cwmzvc.png |
| `skybox/Night Sky With Moon/ft.png` | https://litter.catbox.moe/bj4oo5.png |
| `skybox/Night Sky With Moon/lf.png` | https://litter.catbox.moe/p8l0vb.png |
| `skybox/Night Sky With Moon/rt.png` | https://litter.catbox.moe/mbfw8m.png |
| `skybox/Night Sky With Moon/up.png` | https://litter.catbox.moe/4mlnjx.png |
| `skybox/Night/bk.png` | https://litter.catbox.moe/uxlms8.png |
| `skybox/Night/dn.png` | https://litter.catbox.moe/xwxuz0.png |
| `skybox/Night/ft.png` | https://litter.catbox.moe/grhder.png |
| `skybox/Night/lf.png` | https://litter.catbox.moe/83xd75.png |
| `skybox/Night/rt.png` | https://litter.catbox.moe/rzox9l.png |
| `skybox/Night/up.png` | https://litter.catbox.moe/6kxaam.png |
| `skybox/Northern Lights/bk.png` | https://litter.catbox.moe/i20bv7.png |
| `skybox/Northern Lights/dn.png` | https://litter.catbox.moe/xkqb6s.png |
| `skybox/Northern Lights/ft.png` | https://litter.catbox.moe/u1u0t3.png |
| `skybox/Northern Lights/lf.png` | https://litter.catbox.moe/gzti88.png |
| `skybox/Northern Lights/rt.png` | https://litter.catbox.moe/v9pls0.png |
| `skybox/Northern Lights/up.png` | https://litter.catbox.moe/345o4q.png |
| `skybox/Oblivion/dn.png` | https://litter.catbox.moe/vygtmz.png |

## Faces already absent in the original source

These had no download URL; they are not newly lost during migration.

| Preset | Faces with empty original URLs |
| --- | --- |
| Oblivion | `bk.png`, `ft.png`, `lf.png`, `rt.png`, `up.png` |
| Orange Sky | `bk.png` |

## Original-source evidence

- `open-source/archived_reconsturcted.lua:10621` stores a Paimon download URL, not embedded frame image data.
- Original skybox declarations are in the visual companion `../sixsense/lua/loadstring8-upd2/loadstring8/loadstring7.txt`; its 63 Litterbox URLs match the failed downloads.
- The embedded PNG payload identified in the reconstructed main source is the small Paimon speech-bubble tail, not the missing skybox images.
- Original executor caches inspected did not contain the missing preset faces.

## Verification

- Public GitHub raw downloads: 419/419 SHA-256 matches.
- Actual loader smoke: encoded skybox paths, case-sensitive audio filenames, hit-vignette download, ordered cache-directory creation, and warm-cache reuse passed.
- Paimon 53-frame download/cache/reload and cleanup regression passed.
- Incomplete preset rendering is intentionally not claimed to work; files listed here still require the original images before those presets can be complete.
