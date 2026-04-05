VERSION ?= $(shell git describe --tags --always --dirty 2>/dev/null || echo "dev")
LDFLAGS  := -ldflags "-X main.Version=$(VERSION)"

.DEFAULT_GOAL := help

.PHONY: fmt vet test build generate help

fmt: ## Format Go source files
	gofmt -w .

vet: ## Check formatting and run go vet
	@unformatted=$$(gofmt -l .); \
	if [ -n "$$unformatted" ]; then \
		echo "ERROR: unformatted files:"; \
		echo "$$unformatted"; \
		echo "Run 'make fmt' to fix."; \
		exit 1; \
	fi
	go vet ./...

test: vet ## Run all tests (runs vet first)
	CGO_ENABLED=0 go test ./...

build: ## Build the server binary
	go build $(LDFLAGS) -o bin/server ./cmd/server/
	@if [ "$$(uname)" = "Darwin" ]; then \
		codesign --sign - --force --preserve-metadata=entitlements bin/server; \
	fi

generate: ## Regenerate mocks with mockery
	mockery

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'
