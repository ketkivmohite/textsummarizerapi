# 🚀 Deployment Guide

This guide explains how to deploy your AI Text Summarizer application.

## Option 1: Streamlit Cloud (Recommended - Free & Easy)

### Prerequisites
- GitHub account
- Your code already pushed to GitHub ✅

### Steps:

1. **Go to [Streamlit Cloud](https://streamlit.io/cloud)**

2. **Sign in with GitHub**

3. **Click "New app"**

4. **Fill in the details:**
   - Repository: `ketkivmohite/textsummarizerapi`
   - Branch: `main`
   - Main file path: `app_streamlit_only.py`
   - Advanced settings (optional):
     - Python version: 3.12

5. **Click "Deploy"**

Your app will be live at: `https://your-app-name.streamlit.app`

### Notes:
- First deployment takes 5-10 minutes (downloading AI model)
- Free tier includes: Unlimited public apps, 1GB resources
- App sleeps after inactivity, wakes on visit

---

## Option 2: Heroku (Full Stack with Backend)

### Prerequisites
- Heroku account
- Heroku CLI installed

### Files needed (already in repo):
```
├── Procfile
├── runtime.txt
├── requirements.txt
├── app.py
└── main.py
```

### Steps:

1. **Create Procfile:**
```
web: streamlit run app.py --server.port $PORT
```

2. **Create runtime.txt:**
```
python-3.12.0
```

3. **Deploy:**
```bash
heroku login
heroku create your-app-name
git push heroku main
heroku open
```

**Note:** Heroku free tier ended. You'll need a paid plan (~$5/month).

---

## Option 3: Render (Free Tier Available)

### Steps:

1. **Go to [Render](https://render.com)**

2. **Sign up and connect GitHub**

3. **New Web Service**

4. **Configuration:**
   - Repository: `ketkivmohite/textsummarizerapi`
   - Name: `text-summarizer`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements_streamlit.txt`
   - Start Command: `streamlit run app_streamlit_only.py --server.port $PORT --server.address 0.0.0.0`

5. **Click "Create Web Service"**

**Free Tier:** 750 hours/month, sleeps after 15 mins inactivity

---

## Option 4: Docker + Any Cloud (AWS, GCP, Azure)

### Create Dockerfile:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements_streamlit.txt .
RUN pip install --no-cache-dir -r requirements_streamlit.txt

COPY app_streamlit_only.py .

EXPOSE 8501

CMD ["streamlit", "run", "app_streamlit_only.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Build and Run:
```bash
docker build -t text-summarizer .
docker run -p 8501:8501 text-summarizer
```

### Deploy to cloud:
- **AWS ECS/Fargate**
- **Google Cloud Run**
- **Azure Container Instances**

---

## Option 5: Railway (Simple & Free Tier)

1. Go to [Railway](https://railway.app)
2. Sign in with GitHub
3. New Project → Deploy from GitHub repo
4. Select `ketkivmohite/textsummarizerapi`
5. Set start command: `streamlit run app_streamlit_only.py`
6. Deploy!

---

## 🎯 Recommended: Streamlit Cloud

For your project, **Streamlit Cloud** is the best choice because:
- ✅ Free forever
- ✅ Easy deployment (3 clicks)
- ✅ Automatic updates from GitHub
- ✅ Perfect for Streamlit apps
- ✅ No credit card required

## 📝 Current Deployment Status

To deploy on Streamlit Cloud right now:

1. Push the new files to GitHub:
```bash
git add app_streamlit_only.py requirements_streamlit.txt DEPLOYMENT.md
git commit -m "Add Streamlit Cloud deployment version"
git push
```

2. Go to https://streamlit.io/cloud
3. Click "New app"
4. Select your repo and `app_streamlit_only.py`
5. Deploy!

Your app will be live in minutes! 🚀
