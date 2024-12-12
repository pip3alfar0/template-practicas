# template-practicas
This template provides the basic information required for the GitHub project of the internship. Additionally, it includes tutorials and additional information that will facilitate better use of the GitHub platform and some of its services.

## 1. Creation of `.project_info`
Create a file called `.project_info` in the root folder of the project with the following structure:
```
Title:<Project Title>  
Objective:<The main objective of the project>  
Description:<Brief description of what your project does>  
Members:<Member1,Member2,...>  
Keywords: <see keyword.file>
Collaboration: <collaborator1>
Start Date: <YYYY-MM-DD>
End Date: <YYYY-MM-DD> (estimated)
Status: <Starting, In Progress, Completed>
```

## 2. README.md

## 3. Issues & Milestones

Your project MUST utilize Issues and Milestones to effectively plan, track, and manage tasks, ensuring progress is monitored and objectives are met in a timely manner.

#### 3.1 Issues
Issues can be used to plan, discuss, or track the project's progress. They are also useful for following specific activities, such as bug fixes, new features, and new ideas. 
[About issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues).

[A brief tutorial](https://docs.github.com/en/issues/tracking-your-work-with-issues/configuring-issues/quickstart) provided by GitHub explains how to create issues. It is important at this point to label the issue (new categories can be created) and associate it with a milestone.

### 3.2 Milestones
Milestones can be used to track progress on groups of issues or pull requests in a repository. They allow you to group related tasks and visualize the status of a feature or a project's progress. Milestones can be used to set short- or long-term goals, and each milestone can be linked to one or more specific issues or pull requests. When creating a milestone, it is important to set an estimated completion date to help with better project planning.
[A brief tutorial](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/creating-and-editing-milestones-for-issues-and-pull-requests) for creating milestones is available from GitHub.

Additionally, this [supplementary material](./slides-COM4602/Clase_8_seguimiento_de_tareas.pdf) may be useful.

## 4. Commits & Branches
### 4.1 Commits
Commits are essential for saving changes in your project. They allow you to track modifications, revert to previous states, and collaborate efficiently. When making commits, it is important to:
*  Write clear and concise commit messages
* Make small, focused commits (Atomic)
* Commit frequently

It is important to maintain the atomicity of commits in order to better track the project's progress. [Here](https://kapeli.com/cheat_sheets/Conventional_Commits.docset/Contents/Resources/Documents/index) you can find examples of conventional commits that might be helpful.

### 4.2 Branches
Branches allow for parallel development, helping to isolate different features or fixes. When working with branches, follow these best practices:

* Use descriptive names for branches: Branch names should reflect the purpose or feature, e.g., feature/login-page, bugfix/header-error.
* Create branches for features or fixes: Avoid committing directly to the main branch. Instead, create a new branch for each task/version.
* Use Pull Requests (PRs): Once the changes in a branch are complete, create a pull request to merge it into the main branch. This allows for code review and testing before integration. [Here](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) is information about the creation and use of pull requests.
* Keep branches up to date: Regularly merge the main branch into your feature branches to minimize merge conflicts.

this supplementary material ([branches](./slides-COM4602/Clase_5_Manejo_de_ramas.pdf),[commits](./slides-COM4602/Clase_6_Alteraci_n_de_commits.pdf), [issues, milestones & pull request](./slides-COM4602/Clase_8_seguimiento_de_tareas.pdf)) may be useful.
## 5. Git Hooks for testing
Git hooks are scripts that run automatically. They can be useful for automating tasks such as running tests, linting, or formatting checks before committing or pushing changes. In the context of testing, hooks can help ensure that code is always validated before it enters the repository, helping to maintain the quality of the codebase.

Git hooks are stored in the ./git/hooks/ directory of a repository, and each hook corresponds to a different Git event (e.g., pre-commit, pre-push, etc.). Here we have examples of GitHooks used for testing:
* Pre-commit Hook: This hook runs before the commit is completed. If the test fails, the commit will not be executed, ensuring that only code that passes tests successfully is committed. Its use can range from unit tests to static code analysis, among others.
* Post-commit Hook: This Hook runs after a commit has been made. If theres is an error in this stage, it will not stop the commit itself (since it occurs post-commit) but can trigger notifications or log the issue for later review. This hook can be useful for tasks such as updating documentation, sending notifications, or recording details about the commit.
* Pre-push Hook: This hook runs before pushing to the remote repository. If there is an error, the push will be stopped, allowing you to catch and fix issues before updating the remote branch. This hook is useful for running integration tests or end-to-end teststo ensure that code pushed to the repository does not break functionality.
* Post-push Hook: This hook runs after a push to a remote repository. It does not stop the push itself but can be useful for tasks like sending notifications, logging changes, or updating a dashboard. If errors occur, they won’t affect the push but can provide alerts for later review.


Here are examples of the most commonly used Git hooks, like `pre-commit`, `post-commit`, and `pre-push`, which can help automate various tasks. Other hooks, such as `commit-msg` and `pre-merge`, might also be useful depending on your needs. Each hook serves a unique purpose, allowing for customization and quality control at different points in your workflow.

For a comprehensive list of all available Git hooks, you can refer to the official Git documentation [here](https://git-scm.com/docs/githooks).


### How to use
This is an example of creating a pre-commit hook to verify that the functions `binary_search` and `seq_search` from `search_algorithm.py` pass all tests in `test_search_algorithm.py` before making the commit.

0. Replace the `binary_search` function in the `search_algorithm.py` file with this incorrect version.
```python
def binary_search(arr, target):
    return True # devolvera siempre True
```
1. In the root folder, create the Hook file (if it doesn't exist already). Example:
```bash
$ cd .git/hooks
$ touch pre-commit
```
2. Add testing commands to the hook file. Example:
```
#!/bin/bash
echo "Running tests before committing..."

# Run the tests
python testing.py

# Check for errors and halt commit if tests fail
if [ $? -ne 0 ]; then
    echo "Tests failed. Commit aborted."
    exit 1
fi

echo "Tests passed. Proceeding with commit."

```
Note: You can use any scripting language, as long as you specify the interpreter at the beginning of the file (e.g., `#!/bin/bash`, `#!/usr/bin/env python3`, etc.).

3. Make the file executable. Example
```bash
.git/hooks$ cd ../..
$ chmod +x .git/hooks/pre-commit
```
4. Please try to commit the changes made to `binary_search`, and you should not be able to complete the commit.
```bash
$ git add search_algorithm.py
$ git commit -m "bad commit"
```

## 6. Supplementary Material


## Acknowledgments:
@dmadariaga

@MelanieNICLabs

@lucastorrealba