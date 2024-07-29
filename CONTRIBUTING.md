# Contributing Guidelines

## Branch Naming Conventions

When creating a new branch, please use one of the following naming conventions based on the purpose of your branch:

- **Feature Branches:** `feature/<description>`
  - Example: `feature/add-login`
- **Bugfix Branches:** `bugfix/<description>`
  - Example: `bugfix/fix-crash-on-startup`
- **Request Branches:** `request/<description>`
  - Example: `request/add-new-endpoint`
- **Support Branches:** `support/<description>`
  - Example: `support/update-dependencies`

## Pull Requests

When you push to any branch following the above naming conventions, an automatic pull request will be created targeting the `qa` branch. 

If your branch does not follow these conventions, the push will not trigger a pull request, and a message will be posted to inform you about the correct naming conventions.

## Code Review Process

1. Ensure your branch name follows the conventions.
2. Open a pull request if it wasn't automatically created.
3. Provide a clear description of the changes and any related issue numbers.
4. Wait for the code review and approval from at least one reviewer.
5. Merge the pull request after approval.

Thank you for contributing!
