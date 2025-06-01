# Ghumakkad - Indian Cultural Tourism Platform

Ghumakkad is a comprehensive web application built with Streamlit that showcases India's rich cultural heritage, tourism destinations, and endangered art forms. The platform provides interactive features for exploring different states, planning trips, and supporting traditional artisans.

## 🌟 Features

1. **Cultural Map**
   - Interactive map of India
   - State-wise cultural information
   - Detailed state profiles

2. **Plan Your Yatra**
   - AI-powered travel assistant
   - Personalized itinerary suggestions
   - Local insights and recommendations

3. **Destination Insights**
   - Tourism statistics and analytics
   - Cultural information
   - Popular destinations and hidden gems
   - Local cuisine details

4. **Arts Revival**
   - Showcase of endangered art forms
   - Direct support for artisan communities
   - Preservation efforts information

## 🛠️ Technical Stack

- **Frontend**: Streamlit, HTML/CSS, Plotly
- **Backend**: Python 3.11
- **Database**: Snowflake
- **AI/ML**: Google Gemini
- **APIs**: YouTube Data API
- **Data Analysis**: Pandas, NumPy

## 🚀 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ghumakkad.git
   cd ghumakkad
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory with:
   ```
   GOOGLE_API_KEY=your_google_api_key
   GEMINI_API_KEY=your_gemini_api_key
   SNOWFLAKE_USER=your_snowflake_user
   SNOWFLAKE_PASSWORD=your_snowflake_password
   SNOWFLAKE_ACCOUNT=your_snowflake_account
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 📁 Project Structure

```
ghumakkad/
├── app.py                 # Main application file
├── requirements.txt       # Project dependencies
├── README.md             # Project documentation
├── .env                  # Environment variables (create this)
├── data/                 # Data files
│   ├── states_overview.csv
│   ├── tourism_stats.csv
│   ├── cultural_info.csv
│   └── endangered_arts.csv
└── utils/                # Utility functions
    ├── config.py
    ├── map_utils.py
    ├── chatbot_utils.py
    ├── youtube_utils.py
    └── data_loader.py
```

## 🔑 API Keys Required

- Google API Key (for YouTube integration)
- Google Gemini API Key (for AI assistant)
- Snowflake credentials (for database)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- YourStory x Snowflake Hackathon
- Team Squirtle
- Data sources: Government tourism portals
- Open-source community

## 📧 Contact

For any queries or suggestions, please reach out to [kant19krishna@gmail.com] 
