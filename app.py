from flask import Flask, render_template, request, redirect, url_for, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
import csv
import io
# import pandas as pd  # Temporarily disabled
# import plotly.graph_objs as go  # Temporarily disabled
# import plotly.utils  # Temporarily disabled

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rules.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your-secret-key-here'

db = SQLAlchemy(app)

# Database Model
class Rule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    trigger = db.Column(db.Text, nullable=False)
    effect = db.Column(db.Text, nullable=False)
    meta_note = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'category': self.category,
            'trigger': self.trigger,
            'effect': self.effect,
            'meta_note': self.meta_note,
            'timestamp': self.timestamp.isoformat()
        }

# Categories for dropdown
CATEGORIES = [
    'tâm lý', 'xã hội', 'thói quen', 'tự nhiên', 'công việc', 
    'gia đình', 'học tập', 'sức khỏe', 'tài chính', 'khác'
]

@app.route('/')
def index():
    return render_template('index.html', categories=CATEGORIES)

@app.route('/add_rule', methods=['POST'])
def add_rule():
    description = request.form['description']
    category = request.form['category']
    trigger = request.form['trigger']
    effect = request.form['effect']
    meta_note = request.form.get('meta_note', '')
    
    rule = Rule(
        description=description,
        category=category,
        trigger=trigger,
        effect=effect,
        meta_note=meta_note
    )
    
    db.session.add(rule)
    db.session.commit()
    
    return redirect(url_for('index'))

@app.route('/rules')
def rules_list():
    rules = Rule.query.order_by(Rule.timestamp.desc()).all()
    return render_template('rules.html', rules=rules)

@app.route('/analytics')
def analytics():
    rules = Rule.query.all()

    # Category distribution
    category_counts = {}
    for rule in rules:
        category_counts[rule.category] = category_counts.get(rule.category, 0) + 1

    # Timeline data (simplified without plotly)
    timeline_data = {}
    for rule in rules:
        date = rule.timestamp.strftime('%Y-%m-%d')
        timeline_data[date] = timeline_data.get(date, 0) + 1

    # Word frequency analysis
    all_text = ' '.join([rule.description + ' ' + rule.trigger + ' ' + rule.effect for rule in rules])
    words = all_text.lower().split()
    word_freq = {}
    for word in words:
        if len(word) > 3:  # Only count words longer than 3 characters
            word_freq[word] = word_freq.get(word, 0) + 1

    # Top 10 most frequent words
    top_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:10]

    return render_template('analytics.html',
                         category_chart=None,  # Temporarily disabled
                         timeline_chart=None,  # Temporarily disabled
                         top_words=top_words,
                         total_rules=len(rules),
                         category_counts=category_counts,
                         timeline_data=timeline_data)

@app.route('/export/<format>')
def export_data(format):
    rules = Rule.query.all()
    
    if format == 'json':
        data = [rule.to_dict() for rule in rules]
        output = io.StringIO()
        json.dump(data, output, indent=2, ensure_ascii=False)
        output.seek(0)
        
        return send_file(
            io.BytesIO(output.getvalue().encode('utf-8')),
            mimetype='application/json',
            as_attachment=True,
            download_name='rules.json'
        )
    
    elif format == 'csv':
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(['ID', 'Mô tả', 'Lĩnh vực', 'Nguyên nhân', 'Hệ quả', 'Ghi chú', 'Thời gian'])
        
        for rule in rules:
            writer.writerow([
                rule.id, rule.description, rule.category, 
                rule.trigger, rule.effect, rule.meta_note, 
                rule.timestamp.strftime('%Y-%m-%d %H:%M:%S')
            ])
        
        output.seek(0)
        return send_file(
            io.BytesIO(output.getvalue().encode('utf-8')),
            mimetype='text/csv',
            as_attachment=True,
            download_name='rules.csv'
        )

@app.route('/delete_rule/<int:rule_id>', methods=['POST'])
def delete_rule(rule_id):
    rule = Rule.query.get_or_404(rule_id)
    db.session.delete(rule)
    db.session.commit()
    return redirect(url_for('rules_list'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
