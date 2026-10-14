@echo off
setlocal enableextensions

REM S2-I1 v0.2 bounded generation/validation of TEST_4A_A003_blocky.idx.
REM Writes only to a scratch directory outside the repository by default.
REM Does not create or replace any accepted Stage 1 baseline.
REM
REM IMPORTANT FROZEN-INSPECTOR TRAP:
REM getbits.c Fill_Buffer() treats any read() shorter than 2048 bytes as EOF. A pipe can
REM therefore yield a silently truncated COMPLETE index with rc 0 on some platforms.
REM This procedure deliberately avoids stdin piping: ffmpeg first writes a scratch .m2v,
REM then the frozen inspector reads that regular file.

for %%I in ("%~dp0..\..") do set "repo_root=%%~fI"
set "ffmpeg=C:\SOFTWARE\ffmpeg\ffmpeg.exe"
set "vspipe=D:\TEST\Vapoursynth_x64_R81\lib\site-packages\vapoursynth\vspipe.exe"
set "inspector=%repo_root%\vs\VapourSynth-mpeg2Deblock\x64\Release\Mpeg2BlockInspector.exe"
set "analyzer=%repo_root%\tools\Stage1_Inspector_Analyzer_v0_2.py"
set "reader=%repo_root%\experiments\stage2\stage2_index_reader_v0_2.py"
set "vpy=%repo_root%\experiments\stage2\stage2_validate_bestsource_v0_2.vpy"
set "source=%repo_root%\VHSC_samples\TEST_4A_A003_blocky.mpg"
set "expected_sha=57f3b60d1ea2108f29f222c7c658cb1ddc9eb26c14071cb056112a2f3b296e73"

if defined S2_I1_SCRATCH (
    set "scratch=%S2_I1_SCRATCH%"
) else (
    set "scratch=%TEMP%\VapourSynth-mpeg2Deblock_S2_I1"
)
set "es=%scratch%\TEST_4A_A003_blocky.m2v"
set "index=%scratch%\TEST_4A_A003_blocky.idx"
set "log=%scratch%\TEST_4A_A003_blocky.log"
set "hashout=%scratch%\TEST_4A_A003_blocky.sha256.txt"

for %%F in ("%ffmpeg%" "%vspipe%" "%inspector%" "%analyzer%" "%reader%" "%vpy%" "%source%") do (
    if not exist "%%~F" (
        echo ERROR: required file not found: %%~F
        exit /b 2
    )
)

if not exist "%scratch%" mkdir "%scratch%"
if errorlevel 1 exit /b 2

del /q "%es%" "%index%" "%index%.s1tmp" "%log%" "%hashout%" >NUL 2>&1

echo S2-I1 repository : %repo_root%
echo S2-I1 source     : %source%
echo S2-I1 scratch    : %scratch%
echo S2-I1 ES scratch : %es%
echo S2-I1 index      : %index%
echo S2-I1 log        : %log%

(
    echo S2-I1 v0.2 bounded TEST_4A_A003_blocky candidate generation
    echo repo_root=%repo_root%
    echo source=%source%
    echo elementary_stream=%es%
    echo index=%index%
    echo expected_sha256=%expected_sha%
    echo.
) >"%log%"

echo Creating scratch MPEG-2 elementary stream...
"%ffmpeg%" -y -v error -i "%source%" -c:v copy -an -f mpeg2video "%es%" >>"%log%" 2>&1
if errorlevel 1 (
    echo ERROR: ffmpeg failed while creating scratch elementary stream
    exit /b 2
)
if not exist "%es%" (
    echo ERROR: ffmpeg returned success but scratch elementary stream was not created
    exit /b 2
)

echo Running frozen inspector from regular-file input...
"%inspector%" -b "%es%" -m "%index%" >>"%log%" 2>&1
set "inspector_rc=%ERRORLEVEL%"
>>"%log%" echo Inspector exit code: %inspector_rc%
if not "%inspector_rc%"=="0" (
    echo ERROR: inspector failed with exit code %inspector_rc%
    exit /b %inspector_rc%
)
if not exist "%index%" (
    echo ERROR: inspector returned success but index was not created
    exit /b 2
)

echo Validating all Stage 1 section 8.1 rows plus S2-I1 assertions...
python "%reader%" validate-4a-blocky "%index%" >>"%log%" 2>&1
if errorlevel 1 (
    echo ERROR: Stage 2 reader rejected the 4A-blocky candidate
    exit /b 2
)

REM Analyzer exit code establishes structural validity. Its --expected-frames option is
REM report-only; the Stage 2 reader above enforces the exact 300-record count.
python "%analyzer%" summary "%index%" --expected-frames 300 >>"%log%" 2>&1
if errorlevel 1 (
    echo ERROR: frozen analyzer rejected the 4A-blocky candidate
    exit /b 2
)

echo Checking BestSource/index frame correspondence...
"%vspipe%" --arg "src=%source%" --arg "idx=%index%" --info "%vpy%" >>"%log%" 2>&1
if errorlevel 1 (
    echo ERROR: BestSource/index correspondence validation failed
    exit /b 2
)

echo Computing candidate SHA-256...
certutil -hashfile "%index%" SHA256 >"%hashout%" 2>&1
if errorlevel 1 (
    echo ERROR: certutil SHA-256 failed
    exit /b 2
)
type "%hashout%"
type "%hashout%">>"%log%"
findstr /i /c:"%expected_sha%" "%hashout%" >NUL
if errorlevel 1 (
    echo ERROR: generated candidate SHA-256 does not match expected %expected_sha%
    exit /b 2
)
echo PASS SHA-256 = %expected_sha%

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

echo PASS: S2-I1 v0.2 TEST_4A_A003_blocky candidate generated and validated in scratch.
echo Candidate remains NON-BASELINE and UNCOMMITTED.
echo Log: "%log%"
exit /b 0
