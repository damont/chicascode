# Setup Checklist for Chicas Code

## ✅ Local Setup

### 1. Install Node.js
- [ ] Download and install Node.js 18+ from https://nodejs.org/
- [ ] Verify installation: `node --version` (should be 18 or higher)
- [ ] Verify npm: `npm --version`

### 2. Install Project Dependencies
```bash
cd /home/david/Projects/chicascode
npm install
```

### 3. Test Locally
```bash
npm run dev
```
- [ ] Open http://localhost:4321 in your browser
- [ ] Verify the homepage loads
- [ ] Click through tutorial pages
- [ ] Test the React counter on the React tutorial page

### 4. Build Test
```bash
npm run build
```
- [ ] Build completes without errors
- [ ] Preview the build: `npm run preview`

## ☁️ Cloudflare Setup

### 1. Create Cloudflare Account
- [ ] Sign up at https://dash.cloudflare.com/ (if you don't have an account)
- [ ] Verify your email

### 2. Create Cloudflare Pages Project
- [ ] Go to Workers & Pages → Create Application → Pages
- [ ] Connect to Git → Select GitHub
- [ ] Authorize Cloudflare to access your GitHub
- [ ] Select repository: damont/chicascode
- [ ] Configure build:
  - Framework: Astro
  - Build command: `npm run build`
  - Build output: `dist`
- [ ] Click Save and Deploy
- [ ] Note your project name (usually: chicascode)

### 3. Get Cloudflare Credentials

#### Get Account ID:
- [ ] In Cloudflare Dashboard, note your Account ID from:
  - URL bar, OR
  - Workers & Pages section, OR
  - Any domain → Overview → right sidebar

#### Create API Token:
- [ ] Go to Profile → API Tokens
- [ ] Click Create Token
- [ ] Use "Edit Cloudflare Workers" template OR create custom with:
  - Permission: Account → Cloudflare Pages → Edit
- [ ] Create Token
- [ ] **IMPORTANT: Copy the token immediately** (you won't see it again)

### 4. Configure GitHub Secrets
- [ ] Go to https://github.com/damont/chicascode
- [ ] Settings → Secrets and variables → Actions
- [ ] Click New repository secret
- [ ] Add secret 1:
  - Name: `CLOUDFLARE_API_TOKEN`
  - Value: (paste your API token)
- [ ] Add secret 2:
  - Name: `CLOUDFLARE_ACCOUNT_ID`
  - Value: (paste your Account ID)

### 5. Update Configuration
- [ ] Open `.github/workflows/deploy.yml`
- [ ] Verify `projectName: chicascode` matches your Cloudflare Pages project name
- [ ] Open `astro.config.mjs`
- [ ] Update `site:` URL to your Cloudflare Pages URL (e.g., https://chicascode.pages.dev)

## 🚀 First Deployment

### 1. Git Setup (if not already done)
```bash
git init
git add .
git commit -m "Initial commit: Chicas Code tutorial site"
git branch -M main
git remote add origin https://github.com/damont/chicascode.git
git push -u origin main
```

### 2. Monitor Deployment
- [ ] Go to GitHub → Actions tab
- [ ] Watch the deployment workflow run
- [ ] Verify it completes successfully (green checkmark)
- [ ] If it fails, check the logs for error messages

### 3. Verify Live Site
- [ ] Visit your Cloudflare Pages URL (e.g., https://chicascode.pages.dev)
- [ ] Test all pages
- [ ] Verify navigation works
- [ ] Test the React counter component

## 🔧 Troubleshooting

### Node.js Issues
- If Node.js version is too old, download latest LTS from nodejs.org
- Use `nvm` (Node Version Manager) for easier version management

### Build Errors
- Delete node_modules: `rm -rf node_modules`
- Clear npm cache: `npm cache clean --force`
- Reinstall: `npm install`

### GitHub Actions Errors
- Verify secrets are correctly named (case-sensitive)
- Check that API token has correct permissions
- Ensure Account ID is correct (no extra spaces)

### Cloudflare Issues
- Verify project name matches exactly in deploy.yml
- Check Cloudflare Pages dashboard for deployment logs
- Ensure your Cloudflare account has Pages enabled

## 📝 Notes

- The GitHub Actions workflow triggers on pushes to `main` branch
- You can also manually trigger deployments from GitHub Actions tab
- Cloudflare Pages also has its own deployment system (in addition to GitHub Actions)
- For subsequent deployments, just push to main: `git push origin main`

## 🎉 Success Criteria

You're all set when:
- ✅ Site builds locally without errors
- ✅ GitHub Actions workflow runs successfully
- ✅ Site is accessible at your Cloudflare Pages URL
- ✅ All pages load correctly
- ✅ React components work (counter increments)

---

Need help? Check README.md for detailed documentation!
