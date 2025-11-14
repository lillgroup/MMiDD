# MMiDD
Molecular Modelling in Drug Design

## Setup

**Prerequisites:** Install [git](https://git-scm.com/downloads) and [micromamba](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html)

**Run setup:**
```bash
curl -sSL https://raw.githubusercontent.com/lillgroup/MMiDD/COMMIT_SHA_PLACEHOLDER/setup_environments.sh | bash
```

Alternative (if curl not available):
```bash
wget -qO- https://raw.githubusercontent.com/lillgroup/MMiDD/COMMIT_SHA_PLACEHOLDER/setup_environments.sh | bash
```

The script will:
1. Clone the repository into `MMiDD/` folder
2. Show available environments
3. Prompt you to select an environment to install

**Activate environment:**
```bash
cd MMiDD
micromamba activate <environment_name>
```

---

## For Maintainers

**Update setup script workflow:**

1. Edit `setup_environments.sh`
2. Test locally
3. Commit and push changes
4. Get commit SHA: `git log -1 --format="%H" -- setup_environments.sh`
5. Replace `COMMIT_SHA_PLACEHOLDER` in README with actual SHA
6. Commit and push README

**Why commit SHA URLs?** They are cryptographically immutable and secure - the URL always points to the exact same verified script version.
