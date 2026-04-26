import { execFile } from "child_process";
import path from "path";
import { promisify } from "util";

const execFileAsync = promisify(execFile);

function getPythonPath() {
  return path.join(process.cwd(), ".venv", "Scripts", "python.exe");
}

function getBridgeScriptPath() {
  return path.join(process.cwd(), "dev_tools", "next_bridge.py");
}

export async function fetchResearchSnapshot(ticker: string) {
  const { stdout, stderr } = await execFileAsync(
    getPythonPath(),
    [getBridgeScriptPath(), "research", ticker],
    {
      cwd: process.cwd(),
      timeout: 120000,
      maxBuffer: 10 * 1024 * 1024
    }
  );

  if (stderr && stderr.trim()) {
    console.warn(stderr.trim());
  }

  const lines = stdout
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter(Boolean);
  const jsonLine = lines.at(-1);

  if (!jsonLine) {
    throw new Error("Python bridge returned no JSON payload.");
  }

  return JSON.parse(jsonLine) as Record<string, unknown>;
}
