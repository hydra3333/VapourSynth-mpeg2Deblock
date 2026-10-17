@echo off
setlocal EnableExtensions DisableDelayedExpansion
REM Copy exact already-admitted S2-I2 scratch index; DO NOT regenerate.
for %%I in ("%~dp0..\..") do set "repo=%%~fI"
set "src=%TEMP%\VapourSynth-mpeg2Deblock_S2_I2\LP_blocky\LG_576i_3_LP_blocky.idx"
set "root=%TEMP%\VapourSynth-mpeg2Deblock_S2_I3_P0_v0_1"
set "dst=%root%\indexes\LG_576i_3_LP_blocky.idx"
set "verifier=%~dp0stage2_i3_preflight_verdict_v0_1.py"
if not exist "%root%\P0A_READY.txt" (echo ERROR: run P0A first& exit /b 2)
if not exist "%src%" (echo ERROR: previous S2-I2 LP_blocky scratch missing, stop for review& exit /b 2)
if exist "%repo%\VHSC_samples\LG_576i_3_LP_blocky.idx" (echo ERROR: repo index target exists& exit /b 2)
if exist "%dst%" (echo ERROR: refusing to overwrite already copied scratch index& exit /b 2)
python "%verifier%" verify-index LP_blocky "%src%"
if errorlevel 1 exit /b 2
copy /b "%src%" "%dst%" >nul
if errorlevel 1 exit /b 2
python "%verifier%" verify-index LP_blocky "%dst%" --out "%root%\indexes\LG_576i_3_LP_blocky.idx.verification.json"
if errorlevel 1 exit /b 2
echo PASS: LP_blocky scratch index bytes copied without regeneration.
exit /b 0
