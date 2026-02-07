@echo off
setlocal EnableDelayedExpansion
set "working_dir=C:\AlgoriML\docs\TecMon\cursos\TC4017\4_2_ejer_prg_1\"
:: Exercises to be Tested
set "len_exercises=2"
set "len_common_cls=3"
set "exercises[0]=1_Compute_Statistics"
set "exercises[1]=2_Convert_Numbers"
set "exercises[2]=3_Count_Words"

set "exes[0]=computeStatistics.py"
set "exes[1]=convertNumbers.py"
set "exes[2]=wordCount.py"

set "common_cls[0]=FileManager.py"
set "common_cls[1]=GlobalSettings.py"
set "common_cls[2]=PrinterHelper.py"
set "common_cls[3]=TimeManager.py"

:: Loop through the exercises.
echo.
echo ================================================================================
echo                       Testing pylin through the files.
echo ================================================================================

for /L %%i in (0,1,%len_exercises%-1) do (
    echo.
    echo ================================================================================
    echo Working folder set to := %working_dir%!exercises[%%i]!
    echo Testing this file := !exercises[%%i]!/!exes[%%i]!
    cd %working_dir%!exercises[%%i]!
    pylint !exes[%%i]! --disable=C0103
)

echo Working folder set to := %working_dir%Common_Functions
cd %working_dir%Common_Functions\

for /L %%j in (0,1,%len_common_cls%-1) do (
    echo.
    echo ================================================================================
    echo Testing this file := Common_Functions\!common_cls[%%j]!
    pylint !common_cls[%%j]! --disable=C0103
)

echo.
echo ================================================================================
echo                            End of Test of pylint
echo ================================================================================
