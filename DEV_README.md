# Developer README

- [Developer README](#developer-readme)
  - [Releasing](#releasing)


## Releasing

Releases are published automatically when a tag is pushed to GitHub.

```bash
  # Set next version number
  export RELEASE=x.x.x

  # Create tags
  git add -A
  git commit --allow-empty -m "Release $RELEASE"
  git tag -a $RELEASE -m "Version $RELEASE"

  # Push
  git push --follow-tags
```