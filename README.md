# JohnnyCPU Simulator RAM translating tool

**Description:**
The TXT-to-JohnnyOptCode Translating Tool is a powerful open-source project designed to streamline the process of translating plain text instructions into special OptCode (Operational Code) for Johnny CPU Simulator program execution.

**Key Features:**

TXT-to-OptCode Translation: The tool automates the process of translating text files containing Johnny predicted codes into the corresponding .ram numbers codes, eliminating the need for manual coding.

**Explanation of operation:**
- The available commands are: ['TAKE', 'ADD', 'SUB', 'SAVE', 'JMP', 'TST', 'INC', 'DEC', 'NULL', 'HLT'], and they must be written in capital letters. Opt-codes can take up to 2 arguments: memory address (with the option to enter a label), a label indicating a reference to a specific code fragment.
- Variables are written in the form `lowercase_variable value_of_variable`.
- Loop labels are written as the second argument of each command, starting with a capital letter and ending with `:`.
- You can provide a regular memory value in the form of a number, but it must end with a semicolon `;`.
