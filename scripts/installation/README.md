# Installation Utilities

This directory contains modular deployment and environment setup helpers for tools cataloged in RAVEN.

## Philosophy
* **On-Demand Only**: Third-party tools are not installed globally or automatically cloned.
* **Environment Isolation**: Helper scripts here assist in deploying sandboxed environments (Python virtual environments, Docker containers) for specific tool categories or complex dependencies.
* **No Uncontrolled Vendoring**: Third-party code remains in upstream repositories.
