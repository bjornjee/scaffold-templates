import {FlatCompat} from '@eslint/eslintrc';

const compat = new FlatCompat();

export default [
  ...compat.extends('@react-native'),
  {
    ignores: ['android/', 'ios/', 'node_modules/'],
  },
];
