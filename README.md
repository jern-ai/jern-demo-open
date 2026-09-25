# jern demo — the Open profile

A small Python project with one failing test, for trying
[Jern Cloud](https://jern.ai/cloud/) with no setup.

This repository has no `.jern/baseline.json` and no `jern.json`. A session
on it runs under Jern Cloud's **Open** profile: the agent may edit anything
outside `.jern/` and run any command, in the same confined machine as any
other session, and the pull request it opens is the gate. The test command,
`python3 -m unittest discover -s tests -t .`, is read from the tree.

Ask for "fix the failing test" and review the pull request.
