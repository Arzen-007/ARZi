# core-beta

Rewritten version of the ARZi core theme to use Bootstrap 5, Alpine.js, and vite to improve upon the existing ARZi theme structure. 

## Subtree Installation

### Add repo to themes folder

```
git subtree add --prefix ARZi/themes/core-beta git@github.com:ARZi/core-beta.git main --squash
```

### Pull latest changes to subtree
```
git subtree pull --prefix ARZi/themes/core-beta git@github.com:ARZi/core-beta.git main --squash
```

### Subtree Gotcha

Make sure to use Merge Commits when dealing with the subtree here. For some reason Github's squash and commit uses the wrong line ending which causes issues with the subtree script: https://stackoverflow.com/a/47190256. 

## Todo

- Document how we are using Vite
- Create a cookie cutter template package to use with Vite
