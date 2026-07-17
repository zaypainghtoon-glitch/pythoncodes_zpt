Serve the site locally and open it from your phone on the same Wi‑Fi network

1) Start server from VS Code (recommended):

- Open the Command Palette (Ctrl+Shift+P) → `Tasks: Run Task` → choose `Serve site (http-server)`.
- If prompted to install `http-server`, run `npm i -g http-server` or use the Python task below.

2) Alternative: run with npx (no install required):

```bash
npx http-server ./main -p 8080 -a 0.0.0.0
```

3) Alternative: run with Python 3:

```bash
python -m http.server 8080 --directory ./main --bind 0.0.0.0
```

4) Find your PC's local IP address (Windows):

```powershell
ipconfig
# look for 'IPv4 Address' under your active Wi‑Fi/Ethernet adapter, e.g. 192.168.1.42
```

5) On your phone (connected to the same network) open a browser and visit:

```
http://<PC_IPV4_ADDRESS>:8080
```

Notes:
- If a firewall blocks incoming connections, allow the chosen port (8080) or disable the rule temporarily.
- Using `npx` runs without global install; the VS Code task uses `npx` so you don't have to install globally.
- For HTTPS or public access, you need to deploy the site to a host (Render, Netlify, etc.).
