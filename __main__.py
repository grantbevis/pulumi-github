"""A Python Pulumi program to manage my GitHub"""

from pip import main
import pulumi
import pulumi_github as github

grantbevis = github.Repository("grantbevis",
    allow_auto_merge=True,
    has_downloads=True,
    has_issues=True,
    has_projects=True,
    has_wiki=True,
    name="grantbevis",
    description="My personal GitHub repo",
    visibility="private",
    vulnerability_alerts=True,
    opts=pulumi.ResourceOptions(protect=True))

pulumi_github = github.Repository("pulumi-github",
    name="pulumi-github",
    description="My personal Pulumi GitHub configuration",
    visibility="public",
    has_wiki=False,
    has_issues=True,
    opts=pulumi.ResourceOptions(protect=True))

# pulumi import github:index/repository:Repository nixos nixos
nixos = github.Repository("nixos",
    allow_auto_merge=True,
    # default_branch="main",
    has_downloads=True,
    has_issues=True,
    has_projects=True,
    has_wiki=True,
    name="nixos",
    description="My personal NixOS repo ❄️",
    visibility="private",
    vulnerability_alerts=True,
    opts=pulumi.ResourceOptions(protect=True))

nixos_default_branch = github.BranchDefault("nixos_default_branch",
    repository=nixos.name,
    branch="main")


# Export the Name of the repository
pulumi.export('name', pulumi_github.name)
