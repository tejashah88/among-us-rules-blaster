@REM Activate environment
call env\Scripts\activate.bat

@REM Run service
python rules_blaster.py rules/hide-and-seek.txt
