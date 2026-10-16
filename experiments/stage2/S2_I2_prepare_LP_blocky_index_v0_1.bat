@echo off
setlocal EnableExtensions DisableDelayedExpansion
REM S2-I2 candidate ONLY. Claude must audit BAT before owner runs.
REM Scratch index is not a seventh frozen baseline; elementary stream is Restricted Media.
for %%I in ("%~dp0..\..") do set "repo_root=%%~fI"
set "ffmpeg=C:\SOFTWARE\ffmpeg\ffmpeg.exe"
set "vspipe=D:\TEST\Vapoursynth_x64_R81\lib\site-packages\vapoursynth\vspipe.exe"
set "inspector=%repo_root%\vs\VapourSynth-mpeg2Deblock\x64\Release\Mpeg2BlockInspector.exe"
set "analyzer=%repo_root%\tools\Stage1_Inspector_Analyzer_v0_2.py"
set "reader=%~dp0stage2_validate_lp_blocky_v0_1.py"
set "check_vpy=%~dp0stage2_validate_bestsource_v0_2.vpy"
set "source=%repo_root%\VHSC_samples\LG_576i_3_LP_blocky.mpg"
set "scratch=%TEMP%\VapourSynth-mpeg2Deblock_S2_I2\LP_blocky"
set "es=%scratch%\LG_576i_3_LP_blocky.m2v"
set "idx=%scratch%\LG_576i_3_LP_blocky.idx"
set "log=%scratch%\index_preflight.log"
for %%F in ("%ffmpeg%" "%vspipe%" "%inspector%" "%analyzer%" "%reader%" "%check_vpy%" "%source%") do (
  if not exist "%%~F" (
    echo ERROR: missing %%~F
    exit /b 2
  )
)
if not exist "%scratch%" mkdir "%scratch%"
if errorlevel 1 exit /b 2
REM Delete only named previous scratch outputs under this owned directory.
if exist "%es%" del /q "%es%"
if exist "%idx%" del /q "%idx%"
if exist "%idx%.s1tmp" del /q "%idx%.s1tmp"
>"%log%" echo S2-I2 scratch generation for LP_blocky
>>"%log%" echo source=%source%
>>"%log%" echo expected_index_sha=b3f1d71483bf8a1376584019a020bd476b8d43dbc431a0a13eaa3795996b5238
"%ffmpeg%" -y -v error -i "%source%" -c:v copy -an -f mpeg2video "%es%" >>"%log%" 2>&1
if errorlevel 1 (
  echo ERROR: ffmpeg failed. Log: "%log%"
  exit /b 2
)
if not exist "%es%" (
  echo ERROR: regular elementary stream absent
  exit /b 2
)
for %%I in ("%es%") do if %%~zI LEQ 0 (
  echo ERROR: empty elementary stream
  exit /b 2
)
REM No stdin pipes and no simultaneous log writers.
"%inspector%" -b "%es%" -m "%idx%" >>"%log%" 2>&1
set "rc=%ERRORLEVEL%"
>>"%log%" echo Inspector exit code: %rc%
if not "%rc%"=="0" exit /b 2
if not exist "%idx%" (
  echo ERROR: index missing despite exit zero
  exit /b 2
)
for %%I in ("%idx%") do if %%~zI LEQ 0 (
  echo ERROR: generated index empty
  exit /b 2
)
python "%reader%" "%idx%" >>"%log%" 2>&1
if errorlevel 1 (
  echo ERROR: expected SHA or S2 reader identity mismatch
  exit /b 2
)
python "%analyzer%" summary "%idx%" --expected-frames 204 >>"%log%" 2>&1
if errorlevel 1 (
  echo ERROR: frozen analyzer rejected scratch index
  exit /b 2
)
"%vspipe%" --arg "src=%source%" --arg "idx=%idx%" --info "%check_vpy%" >>"%log%" 2>&1
if errorlevel 1 (
  echo ERROR: BestSource/index mismatch
  exit /b 2
)
echo PASS: LP_blocky scratch candidate SHA, reader, analyzer and BestSource correspondence.
echo Scratch media: "%es%"
echo This .m2v is RESTRICTED MEDIA. Preserve until Claude has reviewed the log.
echo Delete it from the scratch folder when evidence review is complete.
echo Index is non-baseline scratch: "%idx%"
echo Log: "%log%"
exit /b 0
