# Project Scaffold

A well-organized project structure for building applications.

## 📁 Project Structure

```
.
├── src/              # Source code
├── tests/            # Test files
├── public/           # Static assets
├── assignments/      # Course assignments
├── assets/           # Web assets (legacy)
├── templates/        # Templates
└── README.md         # Project documentation
```

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Node.js (if using JavaScript)
- Git

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd week2-excercise
```

2. Install Python dependencies (if applicable):
```bash
pip install -r requirements.txt
```

3. Install Node dependencies (if applicable):
```bash
npm install
```

### Running the Application

#### Web Application
```bash
python3 -m http.server 8000
# Visit http://localhost:8000
```

#### Python Scripts
```bash
python3 src/main.py
```

## 🧪 Testing

Run tests using:
```bash
pytest tests/           # Python
npm test                # JavaScript
```

## 📚 Documentation

- [Source Code](src/README.md)
- [Tests](tests/README.md)
- [Public Assets](public/README.md)

## 🛠️ Development Guidelines

### Code Style

- **Python**: Follow PEP 8
- **JavaScript**: ES6+ with consistent formatting
- **HTML/CSS**: Semantic HTML5, BEM naming

### Git Workflow

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Make your changes and commit: `git commit -m "Description"`
3. Push to branch: `git push origin feature/your-feature`
4. Create a Pull Request

### Best Practices

- Write clean, readable code
- Add comments for complex logic
- Write tests for new features
- Keep functions small and focused
- Use meaningful names for variables and functions

## 📝 License

See [LICENSE](LICENSE) file for details.

## 👥 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📧 Contact

For questions or support, please open an issue in the repository.
