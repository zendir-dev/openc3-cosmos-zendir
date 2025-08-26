# Script Runner test script
cmd("ZENDIR EXAMPLE")
wait_check("ZENDIR STATUS BOOL == 'FALSE'", 5)
