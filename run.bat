@echo off
echo Starting Stock Analysis Next.js UI...
if not exist .venv (
    echo Python virtual environment not found.
    pause
    exit /b
)
if not exist node_modules (
    echo Node modules not found. Running npm install...
    call npm install
    if errorlevel 1 (
        echo npm install failed.
        pause
        exit /b
    )
)
if not exist prisma (
    echo Prisma schema not found.
    pause
    exit /b
)
call npm run db:generate
call npm run db:push
call npm run dev
pause
