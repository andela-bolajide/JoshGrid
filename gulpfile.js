const gulp = require('gulp');

const jsFiles = ['*.js'];

const eslint = require('gulp-eslint');

const wiredep = require('wiredep').stream;

const bowerjson = require('./bower.json');

const options = {
  bowerJson: bowerjson,
  directory: './joshgrid/mail_api/static'
};

gulp.task('lint', () => {
  gulp.src(jsFiles)
    .pipe(eslint())
    .pipe(eslint.format())
    .pipe(eslint.failAfterError());
});

gulp.task('inject', () => {
  gulp.src('./joshgrid/mail_api/templates/*.html')
    .pipe(wiredep(options))
    .pipe(gulp.dest('./joshgrid/mail_api/templates'));
});

gulp.task('default', ['lint'], () => {
  // This will only run if the lint task is successful...
  console.log('Linting Successful!');
});
