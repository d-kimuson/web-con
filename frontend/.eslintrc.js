module.exports = {
  // svelte 内の typescript サポートがまだされてないので、現状では使わない
  // https://github.com/sveltejs/eslint-plugin-svelte3/issues/68
  root: true,
  parser: "@typescript-eslint/parser",
  parserOptions: {
    tsconfigRootDir: __dirname,
    project: './tsconfig.json'
  },
  extends: [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended",
    "plugin:prettier/recommended"
  ],
  plugins: [
    "@typescript-eslint"
  ],
  rules: {
    "no-console": "off",
    "@typescript-eslint/quotes": [
      2,
      "backtick",
      {
        avoidEscape: true,
      },
    ],
  }
}
