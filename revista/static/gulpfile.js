const gulp = require('gulp');
const less = require('gulp-less'); 
const autoprefixer = require('gulp-autoprefixer');
const minifyCSS = require('gulp-csso');
const sourcemaps = require('gulp-sourcemaps');
 
/* Task to compile less */
gulp.task('compile-less', function() {  
  gulp.src('./styles/src/style.less')
    .pipe(sourcemaps.init())
    .pipe(less())
    .pipe(autoprefixer({
      browsers: ['last 2 versions'],
      cascade: false
    }))
    .pipe(minifyCSS())
    .pipe(sourcemaps.write('./'))
    .pipe(gulp.dest('./styles/dist/'));
}); 

/* Task to watch less changes */
gulp.task('watch-less', function() {  
  gulp.watch('./styles/src/*.less' , ['compile-less']);
});

gulp.task('default', ['watch-less']); 
