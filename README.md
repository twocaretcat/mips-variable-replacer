<!-- Project Header -->
<div align="center">
  <h1 class="projectName">MIPS Variable Replacer</h1>

  <p class="projectBadges">
    <img src="https://img.shields.io/badge/type-CLI_App-f44336.svg" alt="Project type" title="Project type"/>
    <img src="https://img.shields.io/github/languages/top/jerboa88/mips-variable-replacer.svg" alt="Language" title="Language"/>
    <img src="https://img.shields.io/github/repo-size/jerboa88/mips-variable-replacer.svg" alt="Repository size" title="Repository size"/>
    <a href="LICENSE">
      <img src="https://img.shields.io/github/license/jerboa88/mips-variable-replacer.svg" alt="Project license" title="Project license"/>
    </a>
  </p>
  
  <p class="projectDesc">
    A command-line tool to simplify development in MIPS assembly. Use easy to remember variable names in MIPS and map them to actual registers before assembling
  </p>
  
  <br/>
</div>


> **Note:** This script is intended to simplify MIPS coding and is not a substitute for properly learning the language yourself


## About
This Python script is a sort of precompiler that lets you use custom register names in MIPS assembly. By running the script before you assemble, custom names are mapped to real registers you specify

**Features:**
- Warns when command line inputs are incorrect
- Warns if you have defined variables you never use
- Warns if you try to replace with invalid register names
- Warns if you have formatted the definitions wrong
- Warns if you have variables in your code that you have not added definitions more (very useful)
- Tells you how many variables were replaced

**Todo:**
- Add support for custom output filenames
- Add option for keeping definitions in output file
- Optimize for very large definition lists


## Usage
Put a definitions section somewhere in your MIPS assembly file that looks something like this:
```
# MVR
# cat: s0
# dog: t1
# bird: a0
# turtle: v0
# MVR

.text
main:
# ...
add $cat, $bird, $zero
and $turtle, $dog, $t3
jr $ra
```
This section is removed when the script is run so you might want to put it at the bottom of your code. Make sure your definitions start and end with `# MVR`. The values on the left are your custom register names and the values on the right are the actual registers they are mapped to.

Run `python3 mvr.py ORIGINALCODE.s` where `ORIGINALCODE.s` is your assembly code in the same directory to replace variable names.

A new file is created in the same directory with the name `ORIGINALCODE_c.s` with the replaced registers.
```
.text
main:
# ...
add $s0, $a0, $zero
and $v0, $t1, $t3
jr $ra
```


## Contributing
This is a personal project but forks and suggestions are welcome.


## Disclaimer
This project is licensed under the Mozilla Public License 2.0. See [LICENSE](LICENSE) for details.

Knowledge of MIPS registers and their functions are still necessary, even with this script. If you are learning MIPS, make sure you are able to program by hand. This script will not help you on assignments. Use at your own risk.
