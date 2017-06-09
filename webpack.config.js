const path = require('path');

// webpack.config.js
module.exports = {
  entry: './src/main.js',
  output: {
    path: path.join(__dirname,'./dist/'),
    filename: 'bundle.js',
    publicPath: '/'
  },
  module: {
    loaders: [
        { test: /(\.css)$/,
          loaders: ['style', 'css']
        },
        {
          test: /\.(js|jsx)$/,
          loader: 'babel-loader',
          query: {
            presets: ['es2015', 'react']
          }
        }
    ]
  },
  devServer: {
    historyApiFallback: true
  },
  resolve: {
    // you can now require('file') instead of require('file.coffee')
    extensions: ['.js', '.json', '.jsx']
  }
};