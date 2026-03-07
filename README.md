# Garth Documentation

This repository contains the source for the [Garth](https://app.heygarth.ai) documentation site, built with [Mintlify](https://mintlify.com).

## Documentation structure

The site is organised into three navigation tabs, each with focused content:

### Documentation tab

| Section                       | Pages                                                                                                                              |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **Overview**                  | `overview.mdx` — platform introduction, supported Git platforms, feature summary                                                   |
| **Setup your Git repository** | `setup/github.mdx`, `setup/bitbucket.mdx`, `setup/gitlab.mdx`, `setup/azure-devops.mdx`                                            |
| **Pull request review**       | `pull-request-review/features.mdx`, `pull-request-review/repository-configuration.mdx`, `pull-request-review/customize-review.mdx` |
| **Code scan**                 | `code-scan/features.mdx`, `code-scan/code-security.mdx`, `code-scan/code-quality.mdx`, `code-scan/repository-configuration.mdx`    |

### Pull Request Review tab

Deep-dive pages for Garth's PR review capabilities — features, configuration, and custom instructions.

### Code Scan tab

Deep-dive pages for Garth's code scanning capabilities — security, quality, and repository configuration.

---

## Local development

Install the [Mintlify CLI](https://www.npmjs.com/package/mint) to preview changes locally:

```bash
npm i -g mint
```

Run the local preview server from the root of this repository (where `docs.json` is located):

```bash
mint dev
```

Open `http://localhost:3000` to view the docs. The site automatically reloads on save.

If the server fails to start, update the CLI first:

```bash
mint update
```

## Publishing

This repository is connected to Mintlify via the GitHub app. Every push to the default branch is automatically deployed to the live documentation site. No manual build step is required.

To set up or manage the GitHub app integration, visit the [Mintlify dashboard](https://dashboard.mintlify.com/settings/organization/github-app).

## Configuration

All site-wide settings — navigation, colours, logo, redirects, and footer — are defined in [`docs.json`](./docs.json).

Key settings at a glance:

| Setting              | Value                           |
| -------------------- | ------------------------------- |
| Theme                | `aspen`                         |
| Primary colour       | `#8B5CF6`                       |
| Default landing page | `/overview` (redirect from `/`) |
| Favicon & logo       | `/logo/garth.png`               |
| Footer               | LinkedIn → `darnerai`           |

## Assets

| Path             | Contents                                                                        |
| ---------------- | ------------------------------------------------------------------------------- |
| `/logo/`         | Garth logo and Git platform SVG icons (GitHub, GitLab, Azure DevOps, Bitbucket) |
| `/images/setup/` | Screenshots used in the setup guides                                            |

## Resources

- [Mintlify documentation](https://mintlify.com/docs)
- [Mintlify component reference](https://mintlify.com/docs/components)
- [Mintlify settings reference](https://www.mintlify.com/docs/organize/settings)
- [Garth dashboard](https://app.heygarth.ai)
