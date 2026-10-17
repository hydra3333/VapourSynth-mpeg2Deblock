@echo off
setlocal EnableExtensions DisableDelayedExpansion
REM Same-content original/blocky pair. Decisive-frame rule; no decoded media files.
set "label=%~1"
set "stem="
if /I "%label%"=="XP" set "stem=LG_576i_1_XP"
if /I "%label%"=="SP" set "stem=LG_576i_2_SP"
if /I "%label%"=="LP" set "stem=LG_576i_3_LP"
if /I "%label%"=="3A" set "stem=TEST_3A_A002"
if not defined stem (echo ERROR: choose XP SP LP or 3A& exit /b 2)
for %%I in ("%~dp0..\..") do set "repo=%%~fI"
set "root=%TEMP%\VapourSynth-mpeg2Deblock_S2_I3_P0_v0_1"
set "vspipe=D:\TEST\Vapoursynth_x64_R81\lib\site-packages\vapoursynth\vspipe.exe"
set "script=%~dp0stage2_i3_pair_clip_v0_1.vpy"
set "out=%root%\results\PAIR_%label%"
for %%S in ("%root%\results\%label%\pskip_identity.json" "%root%\results\%label%_blocky\pskip_identity.json") do if not exist "%%~S" (
  echo ERROR: first admit both encodes of this content group
  exit /b 2
)
python "%~dp0stage2_i3_preflight_verdict_v0_1.py" check-admission "%label%" "%root%\results"
if errorlevel 1 exit /b 2
python "%~dp0stage2_i3_preflight_verdict_v0_1.py" check-admission "%label%_blocky" "%root%\results"
if errorlevel 1 exit /b 2
if exist "%out%" (echo ERROR: existing pair output, refusing to overwrite& exit /b 2)
mkdir "%out%"
if errorlevel 1 exit /b 2
"%vspipe%" --arg "label=%label%" --arg "original=%repo%\VHSC_samples\%stem%.mpg" --arg "blocky=%repo%\VHSC_samples\%stem%_blocky.mpg" --arg "out=%out%" --info "%script%" >"%out%\pair.log" 2>&1
if errorlevel 1 (echo ERROR: pair correspondence failed/blocked, inspect "%out%"& exit /b 2)
echo PASS: %label% paired correspondence
exit /b 0
