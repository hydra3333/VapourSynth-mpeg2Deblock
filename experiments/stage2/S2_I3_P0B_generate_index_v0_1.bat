@echo off
setlocal EnableExtensions DisableDelayedExpansion
REM S2-I3 P0B. One source label PER INVOCATION. No media under VHSC_samples is written.
set "label=%~1"
if /I "%label%"=="XP" goto picked
if /I "%label%"=="XP_blocky" goto picked
if /I "%label%"=="SP" goto picked
if /I "%label%"=="SP_blocky" goto picked
if /I "%label%"=="3A" goto picked
if /I "%label%"=="3A_blocky" goto picked
echo ERROR: specify one of XP XP_blocky SP SP_blocky 3A 3A_blocky
exit /b 2
:picked
for %%I in ("%~dp0..\..") do set "repo=%%~fI"
set "root=%TEMP%\VapourSynth-mpeg2Deblock_S2_I3_P0_v0_1"
set "ffmpeg=C:\SOFTWARE\ffmpeg\ffmpeg.exe"
set "inspector=%repo%\vs\VapourSynth-mpeg2Deblock\x64\Release\Mpeg2BlockInspector.exe"
set "analyzer=%repo%\tools\Stage1_Inspector_Analyzer_v0_2.py"
set "verifier=%~dp0stage2_i3_preflight_verdict_v0_1.py"
if not exist "%root%\P0A_READY.txt" (echo ERROR: run P0A first& exit /b 2)
for %%F in ("%ffmpeg%" "%inspector%" "%analyzer%" "%verifier%") do if not exist "%%~F" (
  echo ERROR: missing %%~F
  exit /b 2
)
set "source_name="
set "index_name="
for /f "usebackq delims=" %%S in (`python "%verifier%" print-index-path "%label%" --extension mpg`) do set "source_name=%%S"
for /f "usebackq delims=" %%S in (`python "%verifier%" print-index-path "%label%" --extension idx`) do set "index_name=%%S"
if not defined source_name (echo ERROR: could not obtain source name for %label%& exit /b 2)
if not defined index_name (echo ERROR: could not obtain index name for %label%& exit /b 2)
set "source=%repo%\VHSC_samples\%source_name%"
set "git_target=%repo%\VHSC_samples\%index_name%"
set "idx=%root%\indexes\%index_name%"
set "es=%root%\indexes\%index_name:.idx=.m2v%"
set "log=%root%\indexes\%index_name:.idx=.log%"
if not exist "%source%" (echo ERROR: missing source& exit /b 2)
if exist "%git_target%" (echo ERROR: refusing existing repository index target "%git_target%"& exit /b 2)
if exist "%idx%" (echo ERROR: refusing to overwrite scratch index& exit /b 2)
if exist "%es%" (echo ERROR: refusing to overwrite scratch elementary stream& exit /b 2)
if exist "%log%" (echo ERROR: refusing to overwrite scratch log& exit /b 2)
>"%log%" echo S2-I3 scratch index generation %label%
>>"%log%" echo source=%source%
"%ffmpeg%" -y -v error -i "%source%" -c:v copy -an -f mpeg2video "%es%" >>"%log%" 2>&1
set "rc=%ERRORLEVEL%"
if not "%rc%"=="0" goto failed
if not exist "%es%" goto failed
for %%I in ("%es%") do if %%~zI LEQ 0 goto failed
"%inspector%" -b "%es%" -m "%idx%" >>"%log%" 2>&1
set "rc=%ERRORLEVEL%"
if not "%rc%"=="0" goto failed
if not exist "%idx%" goto failed
for %%I in ("%idx%") do if %%~zI LEQ 0 goto failed
python "%analyzer%" summary "%idx%" >>"%log%" 2>&1
set "rc=%ERRORLEVEL%"
if not "%rc%"=="0" goto failed
python "%verifier%" verify-index "%label%" "%idx%" --out "%root%\indexes\%index_name%.verification.json" >>"%log%" 2>&1
set "rc=%ERRORLEVEL%"
if not "%rc%"=="0" goto failed
REM Restricted elementary stream is ALWAYS deleted; only the named owned file.
del /q "%es%"
if exist "%es%" (echo ERROR: Restricted Media cleanup failed& exit /b 2)
echo PASS: %label% scratch index verified against independent Claude SHA. See "%log%"
exit /b 0
:failed
if exist "%es%" del /q "%es%"
echo ERROR: %label% generation failed; cleanup attempted; review "%log%"
if exist "%es%" echo ERROR: Restricted Media cleanup failed -- manual attention required
exit /b 2
