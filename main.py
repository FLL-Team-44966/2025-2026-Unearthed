from pybricks.tools import hub_menu

# Choose a letter.
selected = hub_menu("1","2","3","4","5","6","7","8", "9")

# Based on the selection, run a program.
if selected == "1":
    import silo
elif selected == "2":
    import angler
elif selected == "3":
    import forge_lived_here
elif selected == "4":
    import whats_on_sale
elif selected == "5":
    import tip_the_scales
elif selected == "6":
    import heavy_lifting
elif selected == "7":
    import brushing_map
elif selected == "8":
    import salvage_operation
elif selected == "9":
    import transition 
