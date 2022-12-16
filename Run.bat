@echo off

echo "This is the Framework One Project"
echo "Which test case(s) do you want to run?"
echo "[0] Exit
echo "[1] Add Customer"
echo "[2] Login (normal)
echo "[3] Login (DDT)"
echo "[4] Search by Email"
echo "[5] Search by Name"
echo "[6] All"

SET /p "option=Press a button: "
SET /p "report=Would you like to create a report [y\n]? "
SET /p "browser=In which browser would you like to run the test? "

IF "%option%" == "0" exit
IF "%option%" == "1" set choosen=.\testCases\test_add_customer.py
IF "%option%" == "2" set choosen=.\testCases\test_login_normal.py
IF "%option%" == "3" set choosen=.\testCases\test_login_ddt.py
IF "%option%" == "4" set choosen=.\testCases\test_search_customer_by_email.py
IF "%option%" == "5" set choosen=.\testCases\test_search_customer_by_name.py
IF "%option%" == "6" set choosen=

IF "%browser%" == "" (
    IF "%report%" == "y" (
        pytest -v -s --html=.\Reports\report.html %choosen%
        echo "Report saved to the Reports folder"
    ) ELSE (
        pytest -v -s %choosen%
    )
) ELSE (
    IF "%report%" == "y" (
        pytest -v -s --html=.\Reports\report.html %choosen% --browser %browser%
        echo "Report saved to the Reports folder"
    ) ELSE (
        pytest -v -s %choosen% --browser %browser%
    )
)
