"""A Python Pulumi program to manage my GitHub"""

import pulumi
import pulumi_github as github

grantbevis = github.Repository("grantbevis",
    name="grantbevis",
    description="My personal GitHub repo",
    visibility="public")


pulumi_github = github.Repository("pulumi-github",
    name="pulumi-github",
    description="My personal Pulumi GitHub configuration",
    visibility="public",
    has_wiki=False,
    has_issues=True)


nixos = github.Repository("nixos",
    allow_auto_merge=True,
    default_branch="main",
    has_downloads=True,
    has_issues=True,
    has_projects=True,
    has_wiki=True,
    name="nixos",
    description="My personal NixOS repo ❄️",
    visibility="private",
    vulnerability_alerts=True,
    opts=pulumi.ResourceOptions(protect=True))


# Export the Name of the repository
pulumi.export('name', pulumi_github.name)
