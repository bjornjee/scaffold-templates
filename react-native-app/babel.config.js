module.exports = {
  presets: ['@react-native/babel-preset'],
  plugins: [
    [
      'module-resolver',
      {
        root: ['.'],
        alias: {
          '@core': './src/core',
          '@components': './src/components',
        },
      },
    ],
  ],
};
