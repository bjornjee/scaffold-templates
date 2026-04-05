# react-native-app

A React Native project scaffold with a clear separation between platform-agnostic core logic and thin native view layers. Uses the bare React Native CLI (not Expo) for full control over native builds.

## Setup

```bash
# 1. Initialise native projects (generates android/ and ios/ directories)
npx @react-native-community/cli init MyApp --directory .

# 2. Install dependencies
make install

# 3. Configure environment
cp .env.example .env

# 4. Replace placeholder app name in app.json, package.json, and native configs
#    The "name" in app.json must match the native module name in:
#    - android/app/src/main/res/values/strings.xml
#    - ios/ Xcode target name
```

## Commands

Run `make help` to see all available targets.

| Command | Description |
|---------|-------------|
| `make install` | Install Node dependencies |
| `make bundle-ios` | Pre-build JS bundle for iOS |
| `make bundle-android` | Pre-build JS bundle for Android |
| `make build-ios` | Build iOS app (Release) |
| `make build-android` | Build Android app (Release) |
| `make run-ios` | Run iOS app on simulator |
| `make run-android` | Run Android app on emulator |
| `make run-android-usb` | Run Android over USB (sets up adb reverse) |
| `make metro` | Start Metro dev server |
| `make metro-wifi` | Start Metro for WiFi devices |
| `make lint` | Run ESLint |
| `make typecheck` | Run TypeScript type checker |
| `make test` | Run Jest tests |
| `make clean` | Remove build artifacts and caches |

## Project Structure

```
src/
  core/               # SHARED — platform-agnostic business logic
    constants/         #   App-wide constants
    hooks/             #   Custom hooks (no UI, no react-native imports)
    models/            #   Domain types and interfaces
    services/          #   API clients, data transformations
    utils/             #   Pure utility functions
  components/          # SHARED — reusable UI building blocks
  screens/             # GLUE  — thin screen compositions
  navigation/          # GLUE  — routing setup
  assets/              # Images, fonts, icons
```

### Architecture Principles

- **`core/`** contains platform-agnostic business logic. Everything here should be testable without a device or simulator. Do not import from `react-native` in this directory — only React and plain TypeScript.
- **`components/`** contains reusable UI building blocks (buttons, cards, inputs). These are shared across screens.
- **`screens/`** are thin glue code. They compose hooks from `core/hooks/`, pass data to `components/`, and handle navigation. Keep these minimal.
- **`navigation/`** contains React Navigation setup and route definitions.
- **Path aliases** `@core/*` and `@components/*` are configured in `tsconfig.json` and `babel.config.js` for clean imports.

## Running on Device

### USB (Android)

```bash
# Connects adb reverse and launches the app
make run-android-usb
```

### WiFi (Android / iOS)

```bash
# Start Metro bound to your machine's IP
make metro-wifi

# Or specify a different IP
make metro-wifi METRO_HOST=192.168.1.42
```

Then on your device:
1. Shake to open the Dev Menu
2. Go to **Dev Settings** > **Debug server host & port for device**
3. Enter the IP and port printed by the command (e.g. `192.168.1.42:8081`)
4. Reload from the Dev Menu

### USB (iOS)

```bash
make run-ios
# Or target a specific device
npx react-native run-ios --device "iPhone Name"
```

## Pre-building Bundles

Use `make bundle-ios` and `make bundle-android` to create offline JS bundles. This is useful for:
- CI builds where Metro is not available
- Release builds that embed the bundle in the native binary
- Testing production bundle behavior locally
