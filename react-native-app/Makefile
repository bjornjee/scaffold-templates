METRO_HOST ?= $(shell ipconfig getifaddr en0 2>/dev/null || hostname -I 2>/dev/null | awk '{print $$1}')
METRO_PORT ?= 8081
ENTRY_FILE := index.js

.DEFAULT_GOAL := help

.PHONY: install bundle-ios bundle-android build-ios build-android \
        run-ios run-android run-android-usb metro metro-wifi \
        lint typecheck test clean help

install: ## Install Node dependencies
	npm install

# ---------------------------------------------------------------------------
# Pre-build JS bundles
# ---------------------------------------------------------------------------

bundle-ios: ## Pre-build JS bundle for iOS
	npx react-native bundle \
		--entry-file $(ENTRY_FILE) \
		--platform ios \
		--dev false \
		--minify true \
		--bundle-output ios/main.jsbundle \
		--assets-dest ios \
		--reset-cache

bundle-android: ## Pre-build JS bundle for Android
	mkdir -p android/app/src/main/assets
	npx react-native bundle \
		--entry-file $(ENTRY_FILE) \
		--platform android \
		--dev false \
		--minify true \
		--bundle-output android/app/src/main/assets/index.android.bundle \
		--assets-dest android/app/src/main/res \
		--reset-cache

# ---------------------------------------------------------------------------
# Build native apps
# ---------------------------------------------------------------------------

build-ios: ## Build iOS app (Release)
	npx react-native build-ios --mode Release

build-android: ## Build Android app (Release)
	npx react-native build-android --mode release

# ---------------------------------------------------------------------------
# Run on device / emulator
# ---------------------------------------------------------------------------

run-ios: ## Run iOS app on simulator
	npx react-native run-ios

run-android: ## Run Android app on emulator
	npx react-native run-android

run-android-usb: ## Run Android app over USB (sets up adb reverse)
	adb reverse tcp:$(METRO_PORT) tcp:$(METRO_PORT)
	npx react-native run-android --port $(METRO_PORT)

# ---------------------------------------------------------------------------
# Metro dev server
# ---------------------------------------------------------------------------

metro: ## Start Metro dev server
	npx react-native start --port $(METRO_PORT)

metro-wifi: ## Start Metro for WiFi (override with METRO_HOST=<ip>)
	@if [ -z "$(METRO_HOST)" ]; then echo "Error: could not detect IP. Set METRO_HOST manually: make metro-wifi METRO_HOST=192.168.1.42"; exit 1; fi
	@echo "------------------------------------------------------------"
	@echo "Metro will listen on $(METRO_HOST):$(METRO_PORT)"
	@echo "On your device, open Dev Menu and set:"
	@echo "  Debug server host & port -> $(METRO_HOST):$(METRO_PORT)"
	@echo "------------------------------------------------------------"
	npx react-native start --host $(METRO_HOST) --port $(METRO_PORT)

# ---------------------------------------------------------------------------
# Quality
# ---------------------------------------------------------------------------

lint: ## Run ESLint
	npx eslint src/

typecheck: ## Run TypeScript type checker
	npx tsc --noEmit

test: ## Run Jest tests
	npx jest

# ---------------------------------------------------------------------------
# Maintenance
# ---------------------------------------------------------------------------

clean: ## Remove build artifacts and caches
	rm -rf node_modules ios/build ios/Pods android/build android/app/build
	rm -f ios/main.jsbundle
	rm -f android/app/src/main/assets/index.android.bundle
	watchman watch-del-all 2>/dev/null || true
	rm -rf /tmp/metro-* /tmp/haste-map-*

help: ## Show available targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
