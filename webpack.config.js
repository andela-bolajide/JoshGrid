// webpack.config.js
module.exports = {
  entry: './main.js',
  output: {
    // path: 'build', // This is where images AND js will go
    publicPath: 'https://joshgrid.herokuapp.com/', // This is used to generate URLs to e.g. images
    filename: 'bundle.js'       
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
      },
      { test: /\.(png|jpg)$/, loader: 'url-loader?limit=8192' }
    ]
  },
  resolve: {
    // you can now require('file') instead of require('file.coffee')
    extensions: ['.js', '.json', '.jsx'] 
  }
};