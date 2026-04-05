
# Hugo Website — Local Setup

## What You Need
* Git
* Hugo Extended
* Python 3

## Get Started

**1. Clone the Repo**

```bash
git clone https://github.com/NishantSinghhhhh/2.git
cd 2
git submodule update --init --recursive
```

**2. Run the Preprocess Script**

```bash
python preprocess.py
```

**3. Start the Server**

```bash
hugo server
```

**4. Open in Browser**

```
http://localhost:1313
```

## Installing Hugo

### Windows

**Option A — Manual (works on all Windows)**
1. Go to https://github.com/gohugoio/hugo/releases/latest
2. Download `hugo_extended_x.x.x_windows-amd64.zip`
3. Unzip it — you'll get `hugo.exe`
4. Place `hugo.exe` inside your project folder
5. Run it with:

```powershell
.\hugo.exe server
```

**Option B — winget**

```powershell
winget install Hugo.Hugo.Extended
```

**Option C — Chocolatey**

```powershell
choco install hugo-extended
```

Verify install:

```powershell
hugo version
```

### macOS

```bash
brew install hugo
```

Verify:

```bash
hugo version
```

### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install hugo
```

Or download the binary manually:

```bash
wget https://github.com/gohugoio/hugo/releases/download/v0.145.0/hugo_extended_0.145.0_linux-amd64.tar.gz
tar -xzf hugo_extended_0.145.0_linux-amd64.tar.gz
sudo mv hugo /usr/local/bin/
```

Verify:

```bash
hugo version
```

## Troubleshooting
* Blank page? Run `git submodule update --init --recursive`
* Port in use? Run `hugo server -p 1314`
* preprocess.py fails? Make sure Python is installed and in PATH

## Live Site

https://2-one-sigma.vercel.app
