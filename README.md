# CS2004

## How to contribute
- Fork the project
- Add or edit any files under `/resources` 
  - Make sure to use Markdown for styling your document, otherwise it'll break the website. [Here is a 
  good link](https://guides.github.com/features/mastering-markdown/) to learn Markdown !
- Open a Pull Request

## Any PR that affects anything outside or `/resources` will be ignored ! 
```Let my spaghetti code be the way it be```

## BTS
This uses Flask running behind UWSGI to serve the website, compiling course notes from Markdown to HTML using Pandoc and the corresponding Python module, PyPandoc. Some JavaScript colors the colors on the navbar, and that's about it !

***If this attracts any interest I'll include deployment instructions***