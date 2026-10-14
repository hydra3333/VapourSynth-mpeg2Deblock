@echo off
setlocal enableextensions

REM S2-I1 bounded generation/validation of TEST_4A_A003_blocky.idx.
REM Writes only to a scratch directory outside the repository by default.
REM Does not create or replace any accepted Stage 1 baseline.

for %%I in ("%~dp0..\..") do set "repo_root=%%~fI"
set "ffmpeg=C:\SOFTWARE\ffmpeg\ffmpeg.exe"
set "vspipe=D:\TEST\Vapoursynth_x64_R81\lib\site-packages\vapoursynth\vspipe.exe"
set "inspector=%repo_root%\vs\VapourSynth-mpeg2Deblock\x64\Release\Mpeg2BlockInspector.exe"
set "analyzer=%repo_root%\tools\Stage1_Inspector_Analyzer_v0_2.py"
set "reader=%repo_root%\experiments\stage2\stage2_index_reader_v0_1.py"
set "vpy=%repo_root%\experiments\stage2\stage2_validate_bestsource_v0_1.vpy"
set "source=%repo_root%\VHSC_samples\TEST_4A_A003_blocky.mpg"

if defined S2_I1_SCRATCH (
    set "scratch=%S2_I1_SCRATCH%"
) else (
    set "scratch=%TEMP%\VapourSynth-mpeg2Deblock_S2_I1"
)
set "index=%scratch%\TEST_4A_A003_blocky.idx"
set "log=%scratch%\TEST_4A_A003_blocky.log"

for %%F in ("%ffmpeg%" "%vspipe%" "%inspector%" "%analyzer%" "%reader%" "%vpy%" "%source%") do (
    if not exist "%%~F" (
        echo ERROR: required file not found: %%~F
        exit /b 2
    )
)

if not exist "%scratch%" mkdir "%scratch%"
if errorlevel 1 exit /b 2

del /q "%index%" "%index%.s1tmp" "%log%" >NUL 2>&1

echo S2-I1 repository : %repo_root%
echo S2-I1 source     : %source%
echo S2-I1 scratch    : %scratch%
echo S2-I1 index      : %index%
echo S2-I1 log        : %log%

(
    echo S2-I1 bounded TEST_4A_A003_blocky candidate generation
    echo repo_root=%repo_root%
    echo source=%source%
    echo index=%index%
    echo.
) >"%log%"

REM Use the frozen accepted inspector build.  The pipeline return code is the inspector return code.
"%ffmpeg%" -v error -i "%source%" -c:v copy -an -f mpeg2video - 2>>"%log%" | "%inspector%" -b - -m "%index%" >>"%log%" 2>&1
set "inspector_rc=%ERRORLEVEL%"
echo Inspector exit code: %inspector_rc%>>"%log%"
if not "%inspector_rc%"=="0" (
    echo ERROR: inspector failed with exit code %inspector_rc%
    exit /b %inspector_rc%
)
if not exist "%index%" (
    echo ERROR: inspector returned success but index was not created
    exit /b 2
)

python "%reader%" validate-4a-blocky "%index%" >>"%log%" 2>&1
if errorlevel 1 (
    echo ERROR: Stage 2 reader rejected the 4A-blocky candidate
    exit /b 2
)

python "%analyzer%" summary "%index%" --expected-frames 300 >>"%log%" 2>&1
if errorlevel 1 (
    echo ERROR: frozen analyzer rejected the 4A-blocky candidate
    exit /b 2
)

"%vspipe%" --arg "src=%source%" --arg "idx=%index%" --info "%vpy%" >>"%log%" 2>&1
if errorlevel 1 (
    echo ERROR: BestSource/index correspondence validation failed
    exit /b 2
)

echo.>>"%log%"
echo Repository status after scratch-only generation:>>"%log%"
pushd "%repo_root%"
git status --short >>"%log%" 2>&1
set "git_rc=%ERRORLEVEL%"
popd
if not "%git_rc%"=="0" (
    echo ERROR: git status failed
    exit /b 2
)

echo PASS: S2-I1 TEST_4A_A003_blocky candidate generated and validated in scratch.
echo Candidate remains NON-BASELINE and UNCOMMITTED.
echo Log: "%log%"
exit /b 0
