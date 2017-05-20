const webpack = require('webpack');
const path = require('path');

module.exports = {
  entry: [
    './app.js'
  ],
  output: {
    path: path.join(__dirname, '/'),
    filename: 'bundle.js'
  },
  module: {
    loaders: [
      {
        test: /\.(js|jsx)$/, 
        exclude: /node_modules/,
        loaders: 'babel-loader',
        query: {
            presets: ['react']
          }
      },
      {
        test: /(\.css)$/, 
        loaders: ['style', 'css']
      }
    ]
  },
  resolve: {
    extensions: ['.js', '.jsx']
  }
}