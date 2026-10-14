@echo off
setlocal enableextensions

REM S2-I1 v0.2 BestSource/index correspondence gate for all six accepted baseline pairs.
REM Read-only: does not generate, modify or replace any accepted .idx.

for %%I in ("%~dp0..\..") do set "repo_root=%%~fI"
set "vspipe=D:\TEST\Vapoursynth_x64_R81\lib\site-packages\vapoursynth\vspipe.exe"
set "vpy=%repo_root%\experiments\stage2\stage2_validate_bestsource_v0_2.vpy"

if not exist "%vspipe%" (
    echo ERROR: vspipe not found: %vspipe%
    exit /b 2
)
if not exist "%vpy%" (
    echo ERROR: validation script not found: %vpy%
    exit /b 2
)

call :check "LG_576i_3_LP"
if errorlevel 1 exit /b 2
call :check "LG_576i_4_EP"
if errorlevel 1 exit /b 2
call :check "LG_576i_5_MLS"
if errorlevel 1 exit /b 2
call :check "TEST_2A_A001"
if errorlevel 1 exit /b 2
call :check "TEST_2A_A001_blocky"
if errorlevel 1 exit /b 2
call :check "TEST_4A_A003"
if errorlevel 1 exit /b 2

echo PASS: S2-I1 v0.2 BestSource/index correspondence for all six accepted baseline pairs.
exit /b 0

:check
set "stem=%~1"
set "src=%repo_root%\VHSC_samples\%stem%.mpg"
set "idx=%repo_root%\VHSC_samples\%stem%.idx"
if not exist "%src%" (
    echo ERROR: source not found: %src%
    exit /b 2
)
if not exist "%idx%" (
    echo ERROR: accepted index not found: %idx%
    exit /b 2
)
echo.
echo === S2-I1 BestSource correspondence: %stem% ===
"%vspipe%" --arg "src=%src%" --arg "idx=%idx%" --info "%vpy%"
if errorlevel 1 (
    echo ERROR: correspondence failed: %stem%
    exit /b 2
)
exit /b 0
