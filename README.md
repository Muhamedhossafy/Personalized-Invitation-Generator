# Personalized Invitation Generator - Python Project

## 🎯 Project Overview

**Personalized Invitation Generator** is a Python application that automates the creation of personalized invitation letters by merging a template with a list of recipient names. This project demonstrates file handling, string manipulation, and batch processing capabilities in Python.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![File Handling](https://img.shields.io/badge/File-Handling-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📁 Project Structure

```
invitation-generator/
├── Input/
│   └── Letters/
│       └── starting_letter.txt      # Template with {name} and {signature} placeholders
├── Names/
│   └── invited_names.txt            # List of recipient names
├── Output/
│   └── Ready_to_send/               # Generated personalized invitations
├── invitation_generator.py          # Main application file
└── README.md                        # Project documentation
```

## 🛠️ Technologies Used

- **Python 3** - Core programming language
- **File I/O Operations** - Reading and writing text files
- **String Manipulation** - Template replacement techniques
- **Batch Processing** - Handling multiple files efficiently

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your system

### Installation & Execution

1. Clone or download the project files
2. Navigate to the project directory
3. Run the generator:
   ```bash
   python invitation_generator.py
   ```

### How to Use

1. Prepare your template in `Input/Letters/starting_letter.txt` with `{name}` and `{signature}` placeholders
2. Add recipient names to `Names/invited_names.txt` (one name per line)
3. Run the script to generate personalized invitations
4. Find all generated letters in the `Output/Ready_to_send/` directory

## 💻 Code Explanation

The application works as follows:

1. **File Reading**: Loads template and recipient names from text files
2. **Template Processing**: Replaces placeholders with personalized information
3. **Batch Generation**: Creates individual invitation files for each recipient
4. **Output**: Saves personalized invitations with descriptive filenames

Key functions:
- `read_template()`: Reads the template file with placeholders
- `read_names()`: Extracts recipient names from the name list
- `generate_invitations()`: Creates personalized letters for each recipient

## 🌟 Features

- **Efficient Batch Processing**: Generate hundreds of invitations in seconds
- **Flexible Templates**: Easy-to-modify template system
- **Organized Output**: Automatically named and sorted invitation files
- **Error Handling**: Robust file operations with proper exception handling

## 🎨 Customization

You can easily customize:
- The invitation template (`starting_letter.txt`)
- The signature that replaces the `{signature}` placeholder
- The output filename format
- The list of recipients

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the project
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

Possible enhancements:
- Add support for CSV/Excel recipient lists
- Implement email sending capability
- Add GUI interface
- Include attachment handling
- Add template variables for dates, events, etc.

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

## 📧 Contact
- ✉️ **Email**: [muhamad.ammar09001@gmail.com](mailto:muhamad.ammar09001@gmail.com)  
- 🔗 **LinkedIn**: [Muhamad Ammar](https://www.linkedin.com/in/muhamad-ammar-18b427306)
- 🔗 **Portfolio**: [https://muhamedhossafy.github.io/My-Portfolio-DevMA/](https://muhamedhossafy.github.io/My-Portfolio-DevMA/)

---

💌 **Happy inviting!** 🎉
