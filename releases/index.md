# Releases

This page tracks planned and published releases for the vehicle child and pet detection alert system.

## Versioning

This project uses semantic versioning:

- `MAJOR`: incompatible behavior or API changes
- `MINOR`: new features that preserve compatibility
- `PATCH`: bug fixes, test improvements, and small documentation updates

## Release Process

1. Create a `release/<version>` branch.
2. Confirm all tests, lint checks, and coverage checks pass.
3. Update this release page with highlights, validation results, and known limitations.
4. Open a pull request from the release branch into `main`.
5. Merge only after GitHub Actions validation succeeds.
6. Tag the release as `v<version>`.

## Planned Releases

### v0.1.0 - Project Foundation

Status: Planned

Target scope:

- Requirements documentation
- TDD project structure
- CI validation for pull requests
- Initial domain model for occupant detection and alert decisions
- Simulated sensor input for tests

Validation:

- Unit tests pass
- Integration tests pass
- Lint checks pass
- Coverage threshold passes

Known limitations:

- No physical sensor integration yet
- No production notification provider yet
- Detection model may use rule-based or simulated logic only

## Release Notes Template

### vX.Y.Z - Title

Status: Draft

Highlights:

- 

Validation:

- 

Known limitations:

- 
