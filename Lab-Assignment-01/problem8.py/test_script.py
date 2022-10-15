import functions

def test_script():
    assert (functions.make_upper("hasan") == "hasan".upper() and 
    functions.make_lower("hasan") == "hasan".lower() and 
    functions.make_capital("hasan") == "hasan".capitalize()
    )