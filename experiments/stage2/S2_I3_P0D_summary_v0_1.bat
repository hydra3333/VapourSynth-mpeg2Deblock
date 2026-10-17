@echo off
setlocal EnableExtensions DisableDelayedExpansion
set "root=%TEMP%\VapourSynth-mpeg2Deblock_S2_I3_P0_v0_1"
if not exist "%root%\P0A_READY.txt" (echo ERROR: run P0A before requesting summary& exit /b 2)
python "%~dp0stage2_i3_preflight_verdict_v0_1.py" summary "%root%\results"
if errorlevel 1 (
 echo ERROR: global P0 summary not READY; do NOT run filtering. Investigate evidence.
 exit /b 2
)
echo PASS: P0 summary numerical checks. Owner and Claude review still required before P1.
exit /b 0
