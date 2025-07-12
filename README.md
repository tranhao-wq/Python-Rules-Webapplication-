# 🧠 RulePy - Life Rules Tracking & Analytics Platform

<div align="center">

![RulePy Logo](https://img.shields.io/badge/RulePy-Life%20Rules%20Tracker-blue?style=for-the-badge&logo=lightbulb)

[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0+-green?style=flat-square&logo=flask)](https://flask.palletsprojects.com)
[![SQLite](https://img.shields.io/badge/SQLite-Database-orange?style=flat-square&logo=sqlite)](https://sqlite.org)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.1+-purple?style=flat-square&logo=bootstrap)](https://getbootstrap.com)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

*A sophisticated web application for capturing, analyzing, and discovering patterns in life's unwritten rules*

[🚀 Quick Start](#-quick-start) • [📸 Screenshots](#-application-screenshots) • [✨ Features](#-features) • [🛠️ Tech Stack](#️-tech-stack) • [📊 Analytics](#-analytics--insights)

</div>

---

## 🎯 **What is RulePy?**

RulePy is an intelligent **life rules tracking platform** that helps you systematically observe, document, and analyze the patterns that govern your daily experiences. From psychological insights to social dynamics, behavioral patterns to natural phenomena - capture everything and discover the meta-rules that shape your world.

> *"The unexamined life is not worth living"* - Socrates
> RulePy makes life examination systematic, insightful, and actionable.

---

## 🚀 **Quick Start**

### Prerequisites
- Python 3.8+ 🐍
- pip package manager 📦

### Installation & Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/rulepy.git
cd rulepy

# Install dependencies
pip install -r requirements.txt

# Launch the application
python app.py

# Open your browser
# Navigate to: http://localhost:5000
```

🎉 **That's it!** Your personal rule tracking system is now running.

---

## 📸 **Application Screenshots**

### 🏠 **Home Dashboard - Rule Creation Hub**
```
┌─────────────────────────────────────────────────────────────────┐
│  🧠 RulePy                    [➕ Add Rule] [📋 List] [📊 Analytics] │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│           💡 Capture Life's Unwritten Rules                     │
│        Observe, document, and analyze daily patterns            │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │                    ➕ Add New Rule                          │ │
│  ├─────────────────────────────────────────────────────────────┤ │
│  │                                                             │ │
│  │  📝 Rule Description *                                      │ │
│  │  ┌─────────────────────────────────────────────────────────┐ │ │
│  │  │ When I wake up early, I feel more productive...        │ │ │
│  │  └─────────────────────────────────────────────────────────┘ │ │
│  │                                                             │ │
│  │  🏷️ Category *                                              │ │
│  │  ┌─────────────────┐                                       │ │
│  │  │ 🧠 Psychology   ▼│                                       │ │
│  │  └─────────────────┘                                       │ │
│  │                                                             │ │
│  │  ▶️ Trigger/Cause *              ➡️ Effect/Result *         │ │
│  │  ┌─────────────────────────────┐ ┌─────────────────────────┐ │ │
│  │  │ Waking up before 6 AM       │ │ Higher energy levels    │ │ │
│  │  │                             │ │ throughout the day      │ │ │
│  │  └─────────────────────────────┘ └─────────────────────────┘ │ │
│  │                                                             │ │
│  │  🔗 Meta-note (Optional)                                   │ │
│  │  ┌─────────────────────────────────────────────────────────┐ │ │
│  │  │ Similar to the "early bird" principle...               │ │ │
│  │  └─────────────────────────────────────────────────────────┘ │ │
│  │                                                             │ │
│  │                    [💾 Save Rule]                          │ │
│  └─────────────────────────────────────────────────────────────┘ │
│                                                                 │
│  📊 Quick Stats:                                               │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐               │
│  │ 📋 View All │ │ 📈 Analytics│ │ 💾 Export   │               │
│  │    Rules    │ │  & Insights │ │    Data     │               │
│  └─────────────┘ └─────────────┘ └─────────────┘               │
└─────────────────────────────────────────────────────────────────┘
```

### 📋 **Rules Library - Your Personal Knowledge Base**
```
┌─────────────────────────────────────────────────────────────────┐
│  📋 Rules Library                           [➕ Add] [📊 Export] │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │ 🧠 Psychology    💡 Rule #1        🕐 2024-07-12 14:30     │ │
│  ├─────────────────────────────────────────────────────────────┤ │
│  │ 📝 When I wake up early, I feel more productive and        │ │
│  │     energetic throughout the entire day                    │ │
│  │                                                             │ │
│  │ ▶️ Trigger: Waking up before 6 AM                          │ │
│  │ ➡️ Effect: Higher energy levels, better focus              │ │
│  │                                                             │ │
│  │ 🔗 Meta-note: Similar to "early bird catches the worm"    │ │
│  │                                               [🗑️ Delete] │ │
│  └─────────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │ 👥 Social       💡 Rule #2        🕐 2024-07-12 15:45     │ │
│  ├─────────────────────────────────────────────────────────────┤ │
│  │ 📝 People respond better to requests when asked during     │ │
│  │     their good mood periods                                 │ │
│  │                                                             │ │
│  │ ▶️ Trigger: Timing requests with positive emotional states │ │
│  │ ➡️ Effect: Higher success rate, better relationships       │ │
│  │                                                             │ │
│  │ 🔗 Meta-note: Emotional intelligence in action             │ │
│  │                                               [🗑️ Delete] │ │
│  └─────────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │ 💪 Habits       💡 Rule #3        🕐 2024-07-12 16:20     │ │
│  ├─────────────────────────────────────────────────────────────┤ │
│  │ 📝 Small consistent actions compound into significant      │ │
│  │     results over time                                       │ │
│  │                                                             │ │
│  │ ▶️ Trigger: Daily 15-minute practice sessions              │ │
│  │ ➡️ Effect: Noticeable skill improvement after 30 days     │ │
│  │                                                             │ │
│  │ 🔗 Meta-note: The compound effect in personal development  │ │
│  │                                               [🗑️ Delete] │ │
│  └─────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘

### 📊 **Analytics Dashboard - Discover Your Patterns**
```
┌─────────────────────────────────────────────────────────────────┐
│  📊 Analytics & Pattern Discovery                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  📈 Summary Statistics                                          │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ │
│  │     42      │ │      8      │ │     15      │ │    "habit"  │ │
│  │ Total Rules │ │ Categories  │ │ Most/Field  │ │ Top Keyword │ │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘ │
│                                                                 │
│  🥧 Category Distribution              📈 Timeline Trends       │
│  ┌─────────────────────────────────┐   ┌─────────────────────────┐ │
│  │     🧠 Psychology (35%)         │   │ Rules Added Over Time   │ │
│  │     👥 Social (20%)             │   │                         │ │
│  │     💪 Habits (15%)             │   │  ●●●                    │ │
│  │     🏢 Work (12%)               │   │ ●   ●●                  │ │
│  │     💰 Finance (8%)             │   │●     ●●●●               │ │
│  │     🎯 Other (10%)              │   │ Jan Feb Mar Apr May Jun │ │
│  └─────────────────────────────────┘   └─────────────────────────┘ │
│                                                                 │
│  🔥 Hot Keywords                    🧠 Meta-Insights            │
│  ┌─────────────────────────────────┐   ┌─────────────────────────┐ │
│  │ 1. "habit"        (23 times)   │   │ 🎯 Dominant Field:      │ │
│  │ 2. "morning"      (18 times)   │   │    Psychology (35%)     │ │
│  │ 3. "energy"       (15 times)   │   │                         │ │
│  │ 4. "productivity" (12 times)   │   │ 📈 Recording Frequency: │ │
│  │ 5. "focus"        (11 times)   │   │    1.4 rules/month      │ │
│  │ 6. "social"       (9 times)    │   │                         │ │
│  │ 7. "time"         (8 times)    │   │ 🔍 Pattern Detected:    │ │
│  │ 8. "exercise"     (7 times)    │   │    Morning routines →   │ │
│  │ 9. "sleep"        (6 times)    │   │    Productivity boost   │ │
│  │ 10. "mood"        (5 times)    │   │                         │ │
│  └─────────────────────────────────┘   └─────────────────────────┘ │
│                                                                 │
│  💡 Suggested Meta-Rules:                                       │
│  • You tend to observe more psychological patterns than others  │
│  • Morning-related rules show strong correlation with success   │
│  • Habit formation is a recurring theme in your observations   │
│  • Consider exploring more rules in underrepresented areas     │
│                                                                 │
│  [📥 Export JSON] [📊 Export CSV] [🔄 Refresh Analysis]        │
└─────────────────────────────────────────────────────────────────┘
```

---

## ✨ **Features**

### 🎯 **Core Functionality**

| Feature | Description | Icon |
|---------|-------------|------|
| **Rule Capture** | Document life observations with structured format | 📝 |
| **Smart Categorization** | 10+ predefined categories (Psychology, Social, Habits, etc.) | 🏷️ |
| **Cause-Effect Mapping** | Link triggers to outcomes systematically | ⚡ |
| **Meta-Analysis** | Connect rules to discover higher-order patterns | 🔗 |
| **Timeline Tracking** | Automatic timestamping for temporal analysis | ⏰ |

### 📊 **Analytics & Insights**

| Feature | Description | Icon |
|---------|-------------|------|
| **Pattern Discovery** | Identify recurring themes and keywords | 🔍 |
| **Category Analytics** | Distribution analysis across life domains | 📈 |
| **Trend Visualization** | Timeline charts for rule creation patterns | 📊 |
| **Meta-Insights** | AI-powered suggestions for deeper exploration | 🧠 |
| **Export Capabilities** | JSON/CSV export for external analysis | 💾 |

### 🛠️ **Technical Features**

| Feature | Description | Icon |
|---------|-------------|------|
| **Responsive Design** | Works seamlessly on desktop and mobile | 📱 |
| **Real-time Updates** | Instant feedback and live data refresh | ⚡ |
| **Data Persistence** | SQLite database with migration support | 💾 |
| **Search & Filter** | Quick rule discovery and organization | 🔍 |
| **Backup & Restore** | Export/import your entire rule database | 🔄 |

---

## 🛠️ **Tech Stack**

### Backend
- **🐍 Python 3.8+** - Core application logic
- **🌶️ Flask 3.0** - Web framework
- **🗄️ SQLAlchemy** - Database ORM
- **💾 SQLite** - Default database (PostgreSQL/MySQL supported)

### Frontend
- **🎨 Bootstrap 5.1** - Responsive UI framework
- **✨ FontAwesome 6.0** - Icon library
- **📊 Plotly.js** - Interactive charts (optional)
- **⚡ Vanilla JavaScript** - Client-side interactions

### Development
- **🔧 Flask-SQLAlchemy** - Database integration
- **🛡️ Werkzeug** - WSGI utilities
- **📦 pip** - Package management

---

## 📁 **Project Structure**

```
rulepy/
├── 📄 app.py                 # Main Flask application
├── 📋 requirements.txt       # Python dependencies
├── 💾 rules.db              # SQLite database (auto-created)
├── 📁 templates/            # Jinja2 HTML templates
│   ├── 🏠 base.html         # Base template with navigation
│   ├── ➕ index.html        # Home page - rule creation
│   ├── 📋 rules.html        # Rules library listing
│   └── 📊 analytics.html    # Analytics dashboard
├── 📁 static/               # Static assets (CSS, JS, images)
│   ├── 🎨 css/              # Custom stylesheets
│   ├── ⚡ js/               # JavaScript modules
│   └── 🖼️ img/              # Images and icons
├── 📖 README.md             # This documentation
└── 📄 LICENSE               # MIT License
```

---

## 🚀 **Getting Started**

### 1️⃣ **Environment Setup**

```bash
# Ensure Python 3.8+ is installed
python --version

# Create virtual environment (recommended)
python -m venv rulepy-env

# Activate virtual environment
# Windows:
rulepy-env\Scripts\activate
# macOS/Linux:
source rulepy-env/bin/activate
```

### 2️⃣ **Installation**

```bash
# Clone repository
git clone https://github.com/yourusername/rulepy.git
cd rulepy

# Install dependencies
pip install -r requirements.txt
```

### 3️⃣ **Configuration**

```python
# Optional: Customize categories in app.py
CATEGORIES = [
    '🧠 Psychology', '👥 Social', '💪 Habits',
    '🏢 Work', '👨‍👩‍👧‍👦 Family', '📚 Learning',
    '💰 Finance', '🏃‍♂️ Health', '🌱 Personal Growth',
    '🎯 Other'
]
```

### 4️⃣ **Launch**

```bash
# Start the application
python app.py

# Access in browser
open http://localhost:5000
```

---

## 📊 **Analytics & Insights**

### 🔍 **Pattern Recognition**
RulePy automatically analyzes your rules to discover:

- **📈 Trending Topics** - Most frequently mentioned concepts
- **🏷️ Category Preferences** - Which life areas you observe most
- **⏰ Temporal Patterns** - When you're most likely to capture insights
- **🔗 Rule Relationships** - Connections between different observations

### 🧠 **Meta-Rule Discovery**
The system suggests higher-order patterns:

```
🔍 Detected Pattern: "Morning Productivity Loop"
├── 🌅 Early wake-up rules (5 instances)
├── ☕ Morning routine rules (3 instances)
├── 💪 Energy management rules (4 instances)
└── 🎯 Productivity rules (6 instances)

💡 Meta-Rule Suggestion:
"Morning habits create cascading positive effects throughout the day"
```

### 📈 **Export & Integration**

```python
# Example: Analyze exported data with pandas
import pandas as pd
import json

# Load your rules
with open('rules_export.json', 'r') as f:
    rules = json.load(f)

df = pd.DataFrame(rules)

# Discover insights
category_trends = df['category'].value_counts()
monthly_patterns = df.groupby(df['timestamp'].dt.month).size()
keyword_frequency = df['description'].str.split().explode().value_counts()
```

---

## 🎨 **Customization**

### 🏷️ **Adding Custom Categories**

```python
# In app.py, modify the CATEGORIES list:
CATEGORIES = [
    '🧠 Psychology', '👥 Social', '💪 Habits',
    '🏢 Work', '👨‍👩‍👧‍👦 Family', '📚 Learning',
    '💰 Finance', '🏃‍♂️ Health', '🌱 Personal Growth',
    '🎯 Your Custom Category'  # Add your own!
]
```

### 🎨 **UI Theming**

```css
/* Custom CSS in static/css/custom.css */
:root {
    --primary-color: #667eea;
    --secondary-color: #764ba2;
    --success-color: #28a745;
    --info-color: #17a2b8;
}

.hero-section {
    background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
}
```

### 🗄️ **Database Configuration**

```python
# For PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:pass@localhost/rulepy'

# For MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:pass@localhost/rulepy'

# For SQLite (default)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rules.db'
```

---

## 🔧 **Advanced Usage**

### 📊 **Data Analysis Examples**

#### 🐍 **Python Analysis**
```python
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import json

# Load exported rules
with open('rules_export.json', 'r', encoding='utf-8') as f:
    rules = json.load(f)

df = pd.DataFrame(rules)

# 1. Category distribution
category_counts = df['category'].value_counts()
plt.figure(figsize=(10, 6))
category_counts.plot(kind='bar')
plt.title('Rules by Category')
plt.show()

# 2. Word frequency analysis
all_text = ' '.join(df['description'] + ' ' + df['trigger'] + ' ' + df['effect'])
words = all_text.lower().split()
word_freq = Counter(word for word in words if len(word) > 3)
print("Top 10 keywords:", word_freq.most_common(10))

# 3. Temporal patterns
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['month'] = df['timestamp'].dt.month
monthly_rules = df.groupby('month').size()
print("Rules per month:", monthly_rules)

# 4. Meta-rule discovery
psychology_rules = df[df['category'] == '🧠 Psychology']
common_triggers = psychology_rules['trigger'].value_counts().head(5)
print("Common psychology triggers:", common_triggers)
```

#### 📊 **Excel Analysis**
1. Import CSV file into Excel
2. Create Pivot Tables for category analysis
3. Use COUNTIF functions for keyword frequency
4. Generate charts for visual insights

### 🔄 **Backup & Migration**

```bash
# Backup your rules database
cp rules.db backup_$(date +%Y%m%d).db

# Export all data
curl http://localhost:5000/export/json > backup_rules.json

# Migrate to new installation
# Simply copy rules.db to new directory
```

---

## 🤝 **Contributing**

We welcome contributions! Here's how you can help:

### 🐛 **Bug Reports**
- Use GitHub Issues
- Include steps to reproduce
- Provide system information

### ✨ **Feature Requests**
- Describe the use case
- Explain expected behavior
- Consider implementation complexity

### 🔧 **Development Setup**

```bash
# Fork the repository
git clone https://github.com/yourusername/rulepy.git
cd rulepy

# Create feature branch
git checkout -b feature/amazing-feature

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/

# Submit pull request
```

### 📋 **Development Guidelines**
- Follow PEP 8 style guide
- Add tests for new features
- Update documentation
- Use meaningful commit messages

---

## 🚀 **Deployment**

### 🐳 **Docker Deployment**

```dockerfile
# Dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
```

```bash
# Build and run
docker build -t rulepy .
docker run -p 5000:5000 -v $(pwd)/data:/app/data rulepy
```

### ☁️ **Cloud Deployment**

#### Heroku
```bash
# Install Heroku CLI
heroku create your-rulepy-app
git push heroku main
heroku open
```

#### Railway
```bash
# Connect GitHub repository
# Deploy automatically on push
```

#### DigitalOcean App Platform
```yaml
# app.yaml
name: rulepy
services:
- name: web
  source_dir: /
  github:
    repo: yourusername/rulepy
    branch: main
  run_command: gunicorn --worker-tmp-dir /dev/shm app:app
```

---

## 📈 **Roadmap**

### 🎯 **Version 2.0 - Enhanced Analytics**
- [ ] 🤖 AI-powered pattern recognition
- [ ] 📊 Advanced visualization with D3.js
- [ ] 🔍 Full-text search capabilities
- [ ] 📱 Progressive Web App (PWA) support
- [ ] 🔄 Real-time collaboration features

### 🎯 **Version 3.0 - Intelligence Layer**
- [ ] 🧠 Machine learning insights
- [ ] 🔗 Automatic rule relationship detection
- [ ] 📈 Predictive analytics
- [ ] 🎨 Custom dashboard builder
- [ ] 🌐 Multi-language support

### 🎯 **Version 4.0 - Ecosystem**
- [ ] 📱 Mobile companion app
- [ ] 🔌 API for third-party integrations
- [ ] 👥 Community rule sharing
- [ ] 🎓 Educational content integration
- [ ] 🏢 Team/organization features

---

## 📚 **Resources**

### 📖 **Documentation**
- [API Reference](docs/api.md)
- [Database Schema](docs/schema.md)
- [Deployment Guide](docs/deployment.md)
- [Troubleshooting](docs/troubleshooting.md)

### 🎓 **Learning Resources**
- [Pattern Recognition in Daily Life](docs/pattern-recognition.md)
- [Meta-Rule Discovery Techniques](docs/meta-rules.md)
- [Data Analysis Best Practices](docs/analysis.md)

### 🌟 **Inspiration**
- [The Art of Living](https://example.com) - Philosophy behind rule tracking
- [Systems Thinking](https://example.com) - Understanding interconnections
- [Personal Knowledge Management](https://example.com) - Building your second brain

---

## 🏆 **Acknowledgments**

### 💡 **Inspiration**
- **Aristotle** - "We are what we repeatedly do"
- **Charles Darwin** - Systematic observation methodology
- **Richard Feynman** - "What I cannot create, I do not understand"

### 🛠️ **Technology**
- **Flask Team** - Excellent web framework
- **Bootstrap Team** - Beautiful responsive design
- **SQLAlchemy Team** - Powerful ORM
- **Open Source Community** - Making this possible

### 🎨 **Design**
- **FontAwesome** - Beautiful icons
- **Unsplash** - Inspiration images
- **Material Design** - Design principles

---

## 📄 **License**

```
MIT License

Copyright (c) 2024 RulePy Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🌟 **Support the Project**

If RulePy helps you discover meaningful patterns in your life, consider:

- ⭐ **Star the repository** on GitHub
- 🐛 **Report bugs** and suggest features
- 🤝 **Contribute code** or documentation
- 💬 **Share your experience** with others
- ☕ **Buy us a coffee** (coming soon)

---

<div align="center">

### 🧠 **Start Your Journey of Self-Discovery Today**

*"The unexamined life is not worth living, but the examined life is worth optimizing."*

[![Get Started](https://img.shields.io/badge/Get%20Started-Now-blue?style=for-the-badge&logo=rocket)](http://localhost:5000)
[![Documentation](https://img.shields.io/badge/Read-Docs-green?style=for-the-badge&logo=book)](docs/)
[![Community](https://img.shields.io/badge/Join-Community-purple?style=for-the-badge&logo=discord)](https://discord.gg/rulepy)

**Made with ❤️ by the RulePy Community**

</div>
```
