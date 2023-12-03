### Advent of Code 2023: Variables are for the weak

Python, but any instances of `' = '` are an auto-failure.

Usage: `./check.sh <path-to-solution>.py`

If using VSCode, you can use these:

`launch.json`

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Current File",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "justMyCode": true,
      "cwd": "${fileDirname}",
      "preLaunchTask": "Check for Variable Declarations"
    }
  ]
}
```

`tasks.json`

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Check for Variable Declarations",
      "type": "shell",
      "command": "bash",
      "args": ["${workspaceFolder}/2023/check.sh", "${file}"],
      "problemMatcher": []
    }
  ]
}
```
