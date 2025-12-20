# Chicas Code 👩‍💻

A beautiful tutorial website for learning web development, built with Astro and React.

## 🚀 Quick Start

### Prerequisites

Before you begin, make sure you have:
- **Node.js** (version 18 or higher) - [Download here](https://nodejs.org/)
- **npm** (comes with Node.js)
- **Git** - [Download here](https://git-scm.com/)

### Installation

1. **Clone the repository** (if you haven't already)
   ```bash
   cd /home/david/Projects/chicascode
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start the development server**
   ```bash
   npm run dev
   ```

4. **Open your browser**
   - Navigate to `http://localhost:4321`
   - Your site should now be running locally!

## 📦 Project Structure

```
chicascode/
├── public/              # Static assets (images, favicon)
├── src/
│   ├── components/      # Reusable components
│   │   ├── Counter.tsx  # React counter component
│   │   ├── Counter.css
│   │   └── TutorialCard.astro
│   ├── layouts/         # Page layouts
│   │   └── Layout.astro
│   └── pages/           # File-based routing
│       ├── index.astro  # Home page
│       ├── about.astro
│       └── tutorials/   # Tutorial pages
├── .github/
│   └── workflows/
│       └── deploy.yml   # Cloudflare deployment workflow
├── astro.config.mjs     # Astro configuration
├── package.json
└── tsconfig.json
```

## 🔨 Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build locally

## ☁️ Cloudflare Deployment Setup

### Step 1: Create a Cloudflare Pages Project

1. Go to [Cloudflare Dashboard](https://dash.cloudflare.com/)
2. Navigate to **Workers & Pages**
3. Click **Create Application** → **Pages** → **Connect to Git**
4. Select your GitHub repository: `damont/chicascode`
5. Configure the build settings:
   - **Framework preset**: Astro
   - **Build command**: `npm run build`
   - **Build output directory**: `dist`
6. Click **Save and Deploy**

### Step 2: Get Your Cloudflare Credentials

You need two values for GitHub Actions:

#### A. Cloudflare Account ID
1. In your Cloudflare Dashboard, look at the URL or sidebar
2. Your Account ID is visible in the Workers & Pages section
3. Or go to any domain → Overview (right sidebar shows Account ID)

#### B. Cloudflare API Token
1. Go to [Cloudflare Dashboard](https://dash.cloudflare.com/)
2. Click your profile icon → **My Profile**
3. Go to **API Tokens** tab
4. Click **Create Token**
5. Use the **Edit Cloudflare Workers** template
6. Or create custom token with these permissions:
   - **Account** → **Cloudflare Pages** → **Edit**
7. Click **Continue to summary** → **Create Token**
8. **Copy the token** (you won't see it again!)

### Step 3: Add Secrets to GitHub

1. Go to your GitHub repository: `https://github.com/damont/chicascode`
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add these two secrets:

   **Secret 1:**
   - Name: `CLOUDFLARE_API_TOKEN`
   - Value: (paste the API token from Step 2B)

   **Secret 2:**
   - Name: `CLOUDFLARE_ACCOUNT_ID`
   - Value: (paste the Account ID from Step 2A)

### Step 4: Update Project Name

In `.github/workflows/deploy.yml`, update the `projectName` if your Cloudflare Pages project has a different name:

```yaml
projectName: chicascode  # Change this to match your Cloudflare Pages project name
```

### Step 5: Deploy!

1. Push your code to the `main` branch:
   ```bash
   git add .
   git commit -m "Initial commit with Cloudflare deployment"
   git push origin starting:main
   ```

2. GitHub Actions will automatically:
   - Build your site
   - Deploy to Cloudflare Pages
   - Your site will be live at: `https://chicascode.pages.dev`

## 🎨 Customization

### Update Site Information
- Edit `astro.config.mjs` to change your site URL
- Customize colors in `src/layouts/Layout.astro` (CSS variables)
- Add more tutorials in `src/pages/tutorials/`

### Adding React Components
This project is already configured for React! Just create `.tsx` files in `src/components/` and use them in your Astro pages with the `client:load` directive.

## 🌐 Working with Other React Projects

Since you'll have other React projects, here's how to manage them:

### Option 1: Separate Projects (Recommended)
Keep each React project in its own folder with its own `package.json`. This is cleaner and prevents dependency conflicts.

### Option 2: Add to This Project
You can add React components directly to `src/components/` and create pages that use them. Astro plays nicely with React!

## 📝 Environment Variables

For local development, create a `.env` file if needed (already in `.gitignore`):
```
# Add any environment variables here
```

## 🆘 Troubleshooting

### Build Fails
- Make sure you have Node.js 18+ installed: `node --version`
- Delete `node_modules` and reinstall: `rm -rf node_modules && npm install`

### GitHub Actions Fails
- Double-check your secrets are set correctly in GitHub
- Verify the Cloudflare project name matches in `deploy.yml`
- Check the Actions logs for specific error messages

### Site Not Updating
- Clear your browser cache
- Check the Cloudflare Pages dashboard for deployment status

## 📚 Learn More

- [Astro Documentation](https://docs.astro.build)
- [React Documentation](https://react.dev)
- [Cloudflare Pages Docs](https://developers.cloudflare.com/pages)

## 💝 For My Daughters

This site is made with love to help you learn coding. Have fun exploring, building, and creating amazing things! 🌟

---

Made with ❤️ by Dad
