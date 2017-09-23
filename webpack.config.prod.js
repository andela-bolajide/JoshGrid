const path = require('path');
const webpack = require('webpack');
const ExtractTextPlugin = require('extract-text-webpack-plugin');

const GLOBALS = {
  'process.env.NODE_ENV': JSON.stringify(process.env.NODE_ENV) || JSON.stringify('staging')
};

// webpack.config.js
module.exports = {
  devtool: 'source-map',
  entry: path.resolve(__dirname, 'src/index'),
  target: 'web',
  output: {
    path: path.join(__dirname,'./dist/'), // Note: Physical files are only output by the production build task `npm run build`.
    filename: 'bundle.js',
    publicPath: '/'
  },
  module: {
    loaders: [
      { test: /\.(js|jsx)$/, include: path.join(__dirname, 'src'),loader: 'babel-loader', query: { presets: ['es2015', 'react'] } },
      { test: /(\.css)$/, loader: ExtractTextPlugin.extract('css-loader?sourceMap&modules&importLoaders=1&localIdentName=[name]__[local]___[hash:base64:5]!postcss-loader!sass-loader') },
      { test: /\.(jpe?g|png|gif|svg|jpg|otf)$/i, loaders: [ 'file-loader', 'image-webpack-loader' ] },
      { test: /\.eot(\?v=\d+\.\d+\.\d+)?$/, loader: 'file-loader' },
      { test: /\.(woff|woff2)$/, loader: 'url?prefix=font/&limit=5000' },
      { test: /\.ttf(\?v=\d+\.\d+\.\d+)?$/, loader: 'url?limit=10000&mimetype=application/octet-stream' },
      { test: /\.svg(\?v=\d+\.\d+\.\d+)?$/, loader: 'url?limit=10000&mimetype=image/svg+xml' }
    ]
  },
  devServer: {
    historyApiFallback: true,
    contentBase: path.resolve(__dirname, 'dist')
  },
  plugins: [
    new ExtractTextPlugin('styles.css'),
    new webpack.optimize.OccurrenceOrderPlugin(),
    new webpack.DefinePlugin(GLOBALS),
    new webpack.optimize.UglifyJsPlugin(),
  ],
  resolve: {
    // you can now require('file') instead of require('file.coffee')
    extensions: ['.ts', '.tsx', '.js']
  }
};