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


## 5. Git Hooks for testing

## 6. Supplementary Material


## Acknowledgments:
@dmadariaga

@MelanieNICLabs

@lucastorrealba