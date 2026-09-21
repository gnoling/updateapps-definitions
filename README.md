# updateapps definitions

Definitions for [updateapps](https://github.com/gnoling/updateapps): one YAML file per app in
`apps.d/`, named `<id>.yaml`.

## Use it

Add it to `~/.config/updateapps/config.yaml`, then `updateapps repos pull` (it lands in
`~/.config/updateapps/apps.d/gnoling/`):

```yaml
repositories:
  - name: gnoling
    url: https://github.com/gnoling/updateapps-definitions
    default: disabled        # browse first; turn apps on with the enabled: list
enabled: [dolphin, rpcs3]
```

Nothing here needs `trusted: true`: no definition runs shell commands, installs as root, or
writes outside your apps directories.

## Contribute

Add or edit one file in `apps.d/` and open a pull request. There's nothing to build or
package: updateapps downloads the branch as the archive the host generates on request.

- Check it first: `updateapps --defs apps.d validate`, then `updateapps --defs apps.d check <id>`.
- Prefer a declarative `source:`; reach for Lua only when upstream's publishing can't be
  described otherwise (see updateapps' `docs/LUA.md`).
- `name:` is the app's proper name, `description:` one sentence-case line.
- Use `${APPDIR}` / `${APPIMAGEDIR}`, never a literal home directory.
- Put anything a maintainer should know (why a pattern is odd, what upstream changed) in `notes:`.
