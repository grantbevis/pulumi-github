"""A GitHub Python Pulumi program to create it's own repo"""

import pulumi
import pulumi_github as github

pulumi_github_repo = github.Repository("pulumi-github",
    name="pulumi-github",
    description="My personal Pulumi GitHub configuration",
    visibility="public")

# Export the Name of the repository
pulumi.export('name', pulumi_github_repo.name)
