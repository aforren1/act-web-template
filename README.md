
## Use

```
# TODO: note about forking template from github
# then clone that repo

# Go into the repository
$ cd <your name here>

# init heroku
$ heroku create <your name>

# Install dependencies
$ npm install

# Start the local development server (on port 8080)
$ npm start

# Ready for production?
# Build the production ready code to the /dist folder
$ npm run build

# Play your production ready game in the browser
$ npm run serve
```


## Original

The original repository is https://github.com/yandeu/phaser-project-template-es6.

The following changes were made:
 - Updated icons (see src/icons/README for info), and updated paths to those icons
 - Removed PWA materials (we'll never use PWAs, AFAIK)
 - Added https://github.com/webpack-contrib/terser-webpack-plugin to strip comments from production build
 - Updated css in index.html
 - Added heroku-specific files (Procfile, requirements.txt, runtime.txt, server.py)
 - Can probably remove serve dependency? We're going to use a python server

## License

The MIT License (MIT) 2019 - [Yannick Deubel](https://github.com/yandeu). Please have a look at the [LICENSE](LICENSE) for more details.
