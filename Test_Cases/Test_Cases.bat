@echo off
setlocal EnableDelayedExpansion
set "working_dir=C:\AlgoriML\docs\TecMon\cursos\TC4017\4_2_ejer_prg_1\"
:: Exercises to be Tested
set "len_exercises=2"
set "exercises[0]=1_Compute_Statistics"
set "exercises[1]=2_Convert_Numbers"
set "exercises[2]=3_Count_Words"

set "exes[0]=computeStatistics.py"
set "exes[1]=convertNumbers.py"
set "exes[2]=wordCount.py"

set "cases[0]=6"
set "cases[1]=3"
set "cases[2]=4"

:: Loop through the exercises.
echo.
echo ================================================================================
echo                        Loop through the exercises.
echo ================================================================================

for /L %%i in (0,1,%len_exercises%-1) do (
    set cases_count=!cases[%%i]!
    echo.
    echo ================================================================================
    echo Testing this Exercise := !exercises[%%i]!
    echo Working folder set to := %working_dir%!exercises[%%i]!
    cd %working_dir%!exercises[%%i]!

    for /L %%j in (0,1,!cases_count!-1) do (
        set /a file_id=%%j+1
        echo Test using this file := TC!file_id!.txt
        python .\!exes[%%i]! TC!file_id!.txt
    )

)

echo.
echo ================================================================================
echo                 Test of exercises successfully completed.
echo ================================================================================
pause
