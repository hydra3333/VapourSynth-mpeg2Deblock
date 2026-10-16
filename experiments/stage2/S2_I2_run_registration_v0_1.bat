@echo off
setlocal EnableExtensions DisableDelayedExpansion
REM S2-I2 v0.1 IMPLEMENTATION CANDIDATE -- DO NOT RUN until Claude independently clears.
REM Usage: S2_I2_run_registration_v0_1.bat LP   or   LP_blocky
REM Uses only original LP and LP_blocky; never any locked hold-outs.

if /I "%~1"=="LP" goto selected
if /I "%~1"=="LP_blocky" goto selected
echo ERROR: specify LP or LP_blocky (no implicit all-source mode)
exit /b 2
:selected
set "stem=LG_576i_3_%~1"
set "kind=%~1"
for %%I in ("%~dp0..\..") do set "repo_root=%%~fI"
set "vspipe=D:\TEST\Vapoursynth_x64_R81\lib\site-packages\vapoursynth\vspipe.exe"
set "preflight=%~dp0stage2_vspipe_env_preflight_v0_1.vpy"
set "script=%~dp0stage2_registration_clip_v0_1.vpy"
set "check=%~dp0stage2_check_result_v0_1.py"
set "validate=%~dp0stage2_validate_bestsource_v0_2.vpy"
set "regression=%~dp0stage2_index_reader_regression_v0_2.py"
set "source=%repo_root%\VHSC_samples\%stem%.mpg"
set "out=%TEMP%\VapourSynth-mpeg2Deblock_S2_I2\%~1"
set "expected_lp_sha=849b6a9c411a7db837268af3ac54501a06f5f1158e68d5245ce2b3ec40a0d011"
set "expected_blocky_sha=b3f1d71483bf8a1376584019a020bd476b8d43dbc431a0a13eaa3795996b5238"
if /I "%kind%"=="LP" (
  set "index=%repo_root%\VHSC_samples\LG_576i_3_LP.idx"
  set "expected_sha=%expected_lp_sha%"
) else (
  set "index=%out%\LG_576i_3_LP_blocky.idx"
  set "expected_sha=%expected_blocky_sha%"
)
for %%F in ("%vspipe%" "%preflight%" "%script%" "%check%" "%validate%" "%regression%" "%source%" "%index%") do (
  if not exist "%%~F" (
    echo ERROR: required file missing: %%~F
    exit /b 2
  )
)
if not exist "%out%" mkdir "%out%"
if errorlevel 1 exit /b 2
set "log=%out%\S2_I2_%kind%.log"
set "shaout=%out%\source_index_sha256.txt"
>"%log%" echo S2-I2 %kind% candidate execution
>>"%log%" echo source=%source%
>>"%log%" echo index=%index%
REM Validate source index independently using certutil with an anchored 64-hex expected token.
certutil -hashfile "%index%" SHA256 >"%shaout%" 2>&1
if errorlevel 1 exit /b 2
findstr /i /c:"%expected_sha%" "%shaout%" >NUL
if errorlevel 1 (
  echo ERROR: frozen/expected index SHA mismatch
  exit /b 2
)
if /I "%kind%"=="LP_blocky" (
  python "%~dp0stage2_validate_lp_blocky_v0_1.py" "%index%" >>"%log%" 2>&1
  if errorlevel 1 exit /b 2
)
echo Checking frozen six-index S2-I1 regression...
python "%regression%" >>"%log%" 2>&1
if errorlevel 1 (
  echo ERROR: S2-I1 regression failed -- see "%log%"
  exit /b 2
)
echo Running vspipe-native dependency provenance preflight...
"%vspipe%" --info "%preflight%" >>"%log%" 2>&1
if errorlevel 1 (
  echo ERROR: vspipe preflight failed -- see "%log%"
  exit /b 2
)
findstr /c:"S2-I2 RUNTIME PREFLIGHT" "%log%" >NUL
if errorlevel 1 (
  echo ERROR: vspipe preflight did not supply provenance
  exit /b 2
)
echo Checking full BestSource/index picture correspondence...
"%vspipe%" --arg "src=%source%" --arg "idx=%index%" --info "%validate%" >>"%log%" 2>&1
if errorlevel 1 (
  echo ERROR: BestSource index correspondence failed -- see "%log%"
  exit /b 2
)
echo Running S2-I2 diagnostics -- no filter output is produced...
"%vspipe%" --arg "src=%source%" --arg "idx=%index%" --arg "out=%out%" --info "%script%" >>"%log%" 2>&1
if errorlevel 1 (
  echo ERROR: S2-I2 statistics script failed -- see "%log%"
  exit /b 2
)
python "%check%" "%out%" >>"%log%" 2>&1
if errorlevel 1 (
  echo S2-I2 registration NOT ACCEPTED. Reports remain available in "%out%".
  exit /b 2
)
echo PASS: S2-I2 %kind% registration and deliberately bad controls. Reports: "%out%"
echo NB: owner reviews all results. LP_blocky cannot rescue the LP primary gate.
exit /b 0
