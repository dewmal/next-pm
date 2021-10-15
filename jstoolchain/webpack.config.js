const path = require('path');

module.exports = {
    watch: false,
    entry: {
        index: './src/index.js',
    },
    output: {
        filename: 'component.bundle.js',
        path: path.resolve(__dirname, '../static/app/'),
    },
    resolve: {
        extensions: ['.js', '*'],
        modules: [path.resolve(__dirname, "src"), "node_modules"]
    }
};