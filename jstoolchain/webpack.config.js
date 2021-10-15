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
};