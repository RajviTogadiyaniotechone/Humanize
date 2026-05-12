# 🚀 Render Deployment Guide - Humanizer App

## 📋 Overview
Deploy your AI content humanizer to Render for a free, reliable public URL.

## 🛠️ Step 1: Create Render Account

1. Go to [render.com](https://render.com/)
2. Click **"Sign Up"**
3. Sign up with GitHub, Google, or email
4. Verify your email address

## 🛠️ Step 2: Prepare Your Code

### Push to GitHub (Required by Render)
```bash
# If you don't have Git initialized
git init
git add .
git commit -m "Initial commit - Humanizer app"

# Create GitHub repository first, then:
git remote add origin https://github.com/yourusername/humanizer.git
git branch -M main
git push -u origin main
```

## 🛠️ Step 3: Deploy to Render

### Method A: Web Dashboard (Recommended)

1. **Login to Render Dashboard**
   - Go to [render.com](https://dashboard.render.com/)
   - Click **"New +"** button
   - Select **"Web Service"**

2. **Connect Repository**
   - Click **"Connect a repository"**
   - Authorize GitHub if prompted
   - Select your `humanizer` repository
   - Click **"Connect"**

3. **Configure Web Service**
   ```
   Name: humanizer-app
   Environment: Python 3
   Root Directory: (leave blank)
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn app_production:app
   Instance Type: Free
   ```

4. **Advanced Settings**
   - Click **"Advanced"**
   - Add Environment Variable:
     ```
     Key: PORT
     Value: 10000
     ```
   - Add another:
     ```
     Key: PYTHON_VERSION
     Value: 3.9.18
     ```

5. **Deploy**
   - Click **"Create Web Service"**
   - Wait for deployment (2-5 minutes)
   - Your app will be available at: `https://humanizer-app.onrender.com`

### Method B: Render CLI (Advanced)

```bash
# Install Render CLI
npm install -g @render/cli

# Login
render login

# Deploy
render deploy
```

## 🛠️ Step 4: Verify Deployment

### Check Your App
1. Wait for the green **"Live"** status
2. Click on your service URL
3. Test the humanizer interface
4. Try the API endpoint

### Test API
```bash
curl -X POST https://your-app.onrender.com/api/enhanced-humanize \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Furthermore, we must utilize strategic methodologies.",
    "focused_mode": true,
    "intensity": 0.7
  }'
```

## 🔧 Configuration Files Already Created

### ✅ app_production.py
- Production-ready Flask app
- Security and error handling
- Health check endpoint

### ✅ requirements.txt
- All dependencies including Gunicorn
- Compatible with Render

### ✅ runtime.txt
- Python 3.9.18 specification

## 🌐 Your Public URL

After successful deployment:
- **URL**: `https://your-app-name.onrender.com`
- **API**: `https://your-app-name.onrender.com/api/enhanced-humanize`
- **Health**: `https://your-app-name.onrender.com/health`

## 📊 Features Available

### ✅ Web Interface
- Clean, user-friendly design
- Side-by-side text comparison
- Real-time character counting
- Copy to clipboard functionality

### ✅ API Endpoints
- `POST /api/enhanced-humanize` - Main humanization
- `GET /health` - Health monitoring
- CORS enabled for public access

## 🔍 Troubleshooting

### Common Issues

#### ❌ Build Failed
```
Solution: Check requirements.txt for correct versions
```

#### ❌ Service Not Responding
```
Solution: Check Start Command should be: gunicorn app_production:app
```

#### ❌ 502 Bad Gateway
```
Solution: Ensure PORT environment variable is set to 10000
```

#### ❌ 404 Not Found
```
Solution: Check that app_production.py is in root directory
```

### Debug Steps

1. **Check Build Logs**
   - Go to Render Dashboard
   - Click on your service
   - Click **"Logs"** tab
   - Look for error messages

2. **Check Environment Variables**
   - Go to **"Environment"** tab
   - Verify PORT=10000 is set
   - Check PYTHON_VERSION=3.9.18

3. **Manual Restart**
   - Click **"Manual Deploy"**
   - Select **"Deploy latest commit"**
   - Wait for completion

## 🚀 Quick Deployment Checklist

### ✅ Pre-Deployment
- [ ] Code pushed to GitHub
- [ ] app_production.py in root directory
- [ ] requirements.txt includes gunicorn
- [ ] runtime.txt specifies Python 3.9.18

### ✅ Render Configuration
- [ ] Repository connected
- [ ] Build command: `pip install -r requirements.txt`
- [ ] Start command: `gunicorn app_production:app`
- [ ] Environment variables: PORT=10000

### ✅ Post-Deployment
- [ ] Service shows "Live" status
- [ ] Web interface loads correctly
- [ ] API responds to requests
- [ ] Health check returns 200

## 🎉 Success!

Once deployed, anyone can:
- 🌐 Access your humanizer at the public URL
- 🔌 Use the API for programmatic access
- 📱 Humanize AI content from any device
- 🔄 Get real-time word replacement results

**Share your public URL and let others start humanizing their AI content!** 🎯

## 📞 Support

- **Render Documentation**: [render.com/docs](https://render.com/docs)
- **Status Page**: [status.render.com](https://status.render.com)
- **Support**: [support@render.com](mailto:support@render.com)
