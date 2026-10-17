@echo off
setlocal EnableExtensions DisableDelayedExpansion
REM S2-I3 P0A -- candidate only. No media or hold-outs touched.
for %%I in ("%~dp0..\..") do set "repo=%%~fI"
set "root=%TEMP%\VapourSynth-mpeg2Deblock_S2_I3_P0_v0_1"
set "regression=%~dp0stage2_index_reader_regression_v0_2.py"
set "preflight=%~dp0stage2_vspipe_env_preflight_v0_1.vpy"
set "pskip_tests=%~dp0stage2_i3_pskip_tests_v0_1.py"
set "pair_tests=%~dp0stage2_i3_pair_tests_v0_1.py"
set "vspython=D:\TEST\Vapoursynth_x64_R81\python.exe"
set "vspipe=D:\TEST\Vapoursynth_x64_R81\lib\site-packages\vapoursynth\vspipe.exe"
for %%F in ("%regression%" "%preflight%" "%vspipe%" "%pskip_tests%" "%pair_tests%" "%vspython%") do if not exist "%%~F" (
  echo ERROR: missing %%~F
  exit /b 2
)
if exist "%root%" (
  echo ERROR: P0 scratch campaign folder already exists: "%root%"
  echo A new run must use a fresh reviewed campaign path. No deletion is automatic.
  exit /b 2
)
python "%regression%"
if errorlevel 1 exit /b 2
"%vspython%" -c "import os,sys,runpy; script=os.path.abspath(sys.argv[1]); sys.argv=[script]; sys.path.insert(0,os.path.dirname(script)); runpy.run_path(script,run_name='__main__')" "%pskip_tests%"
if errorlevel 1 (echo ERROR: S2-I3 P-skip unit tests failed& exit /b 2)
"%vspython%" -c "import os,sys,runpy; script=os.path.abspath(sys.argv[1]); sys.argv=[script]; sys.path.insert(0,os.path.dirname(script)); runpy.run_path(script,run_name='__main__')" "%pair_tests%"
if errorlevel 1 (echo ERROR: S2-I3 pair unit tests failed& exit /b 2)
"%vspipe%" --info "%preflight%"
if errorlevel 1 exit /b 2
mkdir "%root%"
if errorlevel 1 exit /b 2
mkdir "%root%\indexes"
if errorlevel 1 exit /b 2
mkdir "%root%\results"
if errorlevel 1 exit /b 2
>"%root%\P0A_READY.txt" echo S2-I3 P0A regression and vspipe preflight PASS; indexes pending
if errorlevel 1 exit /b 2
echo PASS: P0A; scratch "%root%". Run P0B for six named sources.
exit /b 0
