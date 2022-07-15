Process for making a change to the project! (gotta go fast so this is just a placeholder)

0. **Clone the repository**. You can do this with VS code, or if you already cloned it, you can just open the folder of an existing repository.

![Cloning the repository](https://i.imgur.com/s61Cdtj.png)

1. **Create a branch**. Whenever you want to make a change, you need to set up a branch on bitbucket. This will ensure that we can make multiple changes to the code at the same time without conflicts. First go to https://bitbucket.org/Roc0c0/ai-investo/branches/, then click "Create Branch". Use "master" as the source branch and name your new branch something like "jm/readme-fix" (*user identifier/change identifier*).

![Branching](https://i.imgur.com/Zhx1VbB.png)

2. **Run "Pull" and/or "Fetch" in VS Code**. To get the new branch and new commits from the origin, make sure to do a Pull under the source control tab in VS Code. It's in the "..." options. DO NOT use "Sync" as this will push your changes immediately and overwrite the source (I'll disable this in the future).

3. **Checkout the branch in VS Code**. Now that the branch exists, you can do a git checkout of the branch to get it and edit it. "Checkout" should be an option under the source control tab in VS Code, and from there you can select your branch (which should appear as "origin/jm/readme-fix" in this example).

![Checkout](https://i.imgur.com/G4gBsJR.png)

4. **Make changes**. Now I just add a readme file yadda yadda.

[Make changes](https://i.imgur.com/mU6BN5P.png)

5. **Commit and push**. I suppose you already know how to do this.

6. **Make a pull request in Bitbucket**.