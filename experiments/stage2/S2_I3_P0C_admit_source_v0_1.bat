@echo off
setlocal EnableExtensions DisableDelayedExpansion
REM One source per invocation, BestSource exact gate. Recheck actual index SHA.
set "label=%~1"
if /I "%label%"=="XP" goto picked
if /I "%label%"=="XP_blocky" goto picked
if /I "%label%"=="SP" goto picked
if /I "%label%"=="SP_blocky" goto picked
if /I "%label%"=="LP" goto picked
if /I "%label%"=="LP_blocky" goto picked
if /I "%label%"=="3A" goto picked
if /I "%label%"=="3A_blocky" goto picked
echo ERROR: explicit development source label required
exit /b 2
:picked
for %%I in ("%~dp0..\..") do set "repo=%%~fI"
set "root=%TEMP%\VapourSynth-mpeg2Deblock_S2_I3_P0_v0_1"
set "vspipe=D:\TEST\Vapoursynth_x64_R81\lib\site-packages\vapoursynth\vspipe.exe"
set "verifier=%~dp0stage2_i3_preflight_verdict_v0_1.py"
set "script=%~dp0stage2_i3_admission_clip_v0_1.vpy"
if not exist "%root%\P0A_READY.txt" (echo ERROR: run P0A before admission& exit /b 2)
for %%F in ("%vspipe%" "%script%" "%verifier%") do if not exist "%%~F" (echo ERROR: missing %%~F& exit /b 2)
set "source_name="
set "index_name="
for /f "usebackq delims=" %%S in (`python "%verifier%" print-index-path "%label%" --extension mpg`) do set "source_name=%%S"
for /f "usebackq delims=" %%S in (`python "%verifier%" print-index-path "%label%" --extension idx`) do set "index_name=%%S"
if not defined source_name (echo ERROR: could not obtain source name for %label%& exit /b 2)
if not defined index_name (echo ERROR: could not obtain index name for %label%& exit /b 2)
set "source=%repo%\VHSC_samples\%source_name%"
set "idx=%root%\indexes\%index_name%"
if /I "%label%"=="LP" set "idx=%repo%\VHSC_samples\%index_name%"
set "out=%root%\results\%label%"
if not exist "%source%" (echo ERROR: missing source "%source%"& exit /b 2)
if not exist "%idx%" (echo ERROR: missing index "%idx%"& exit /b 2)
if exist "%out%" (echo ERROR: refusing to mix with existing per-source evidence& exit /b 2)
python "%verifier%" verify-index "%label%" "%idx%"
if errorlevel 1 exit /b 2
mkdir "%out%"
if errorlevel 1 exit /b 2
"%vspipe%" --arg "label=%label%" --arg "src=%source%" --arg "idx=%idx%" --arg "out=%out%" --info "%script%" >"%out%\admission.log" 2>&1
if errorlevel 1 (echo ERROR: %label% did not REGISTER; inspect "%out%\pskip_identity.json"& exit /b 2)
echo PASS: %label% exact P-skip admission, see "%out%"
exit /b 0
