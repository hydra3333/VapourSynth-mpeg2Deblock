@echo off
setlocal EnableExtensions DisableDelayedExpansion
REM Per-source unchanged S2-I2 numerical engine. Informational, NOT admission.
set "label=%~1"
if /I "%label%"=="XP" goto picked
if /I "%label%"=="XP_blocky" goto picked
if /I "%label%"=="SP" goto picked
if /I "%label%"=="SP_blocky" goto picked
if /I "%label%"=="LP" goto picked
if /I "%label%"=="LP_blocky" goto picked
if /I "%label%"=="3A" goto picked
if /I "%label%"=="3A_blocky" goto picked
echo ERROR: invalid diagnostic label - use one of the eight ratified labels
exit /b 2
:picked
for %%I in ("%~dp0..\..") do set "repo=%%~fI"
set "root=%TEMP%\VapourSynth-mpeg2Deblock_S2_I3_P0_v0_1"
set "vspipe=D:\TEST\Vapoursynth_x64_R81\lib\site-packages\vapoursynth\vspipe.exe"
set "verifier=%~dp0stage2_i3_preflight_verdict_v0_1.py"
set "script=%~dp0stage2_i3_diagnostic_clip_v0_1.vpy"
if not exist "%root%\results\%label%\pskip_identity.json" (echo ERROR: admission evidence absent& exit /b 2)
python "%verifier%" check-admission "%label%" "%root%\results"
if errorlevel 1 exit /b 2
set "source_name="
set "index_name="
for /f "usebackq delims=" %%S in (`python "%verifier%" print-index-path "%label%" --extension mpg`) do set "source_name=%%S"
for /f "usebackq delims=" %%S in (`python "%verifier%" print-index-path "%label%" --extension idx`) do set "index_name=%%S"
if not defined source_name (echo ERROR: could not obtain diagnostic source name for %label%& exit /b 2)
if not defined index_name (echo ERROR: could not obtain diagnostic index name for %label%& exit /b 2)
set "source=%repo%\VHSC_samples\%source_name%"
set "idx=%root%\indexes\%index_name%"
if /I "%label%"=="LP" set "idx=%repo%\VHSC_samples\%index_name%"
set "out=%root%\results\%label%"
if exist "%out%\s2i2_diagnostics" (echo ERROR: existing diagnostics; refusing overwrite& exit /b 2)
python "%verifier%" verify-index "%label%" "%idx%"
if errorlevel 1 exit /b 2
"%vspipe%" --arg "label=%label%" --arg "src=%source%" --arg "idx=%idx%" --arg "out=%out%" --info "%script%" >"%out%\diagnostics.log" 2>&1
if errorlevel 1 (echo ERROR: diagnostic execution problem - not a phase-gate failure& exit /b 2)
echo COMPLETE: %label% S2-I2 numerical diagnostics (NOT admission)
exit /b 0
