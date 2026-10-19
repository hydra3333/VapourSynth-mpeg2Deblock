@echo on

set "py_dir=D:\TEST\Vapoursynth_x64_R81"
set "py_exe=%py_dir%\python.exe"
set "py=E:\SOFTWARE-Win11\MULTIMEDIA\VapourSynth-mpeg2Deblock\VapourSynth-mpeg2Deblock\src\mpeg2deblock_fetch_metadata\mpeg2deblock_fetch_metadata.py"
set "sample_dir=E:\SOFTWARE-Win11\MULTIMEDIA\VapourSynth-mpeg2Deblock\VHS_LARGE_samples"
set "sample_name=%sample_dir%\A002"
set "sample_mpg=%sample_name%.mpg
set "sample_bat=%sample_name%_metadata.bat"
set "sample_prefix=SRC_"

REM for /f "tokens=1 delims==" %%V in ('set %sample_prefix% 2^>nul') do set "%%V="
REM set %sample_prefix%

"%py_exe%" "%PY%" "%sample_mpg%" --mediainfo-dir "%py_dir%" --prefix %sample_prefix% --bat "%sample_bat%"
call "%sample_bat%"
set %sample_prefix%

REM for /f "tokens=1 delims==" %%V in ('set %sample_prefix% 2^>nul') do set "%%V="
REM set %sample_prefix%

pause
exit /b
